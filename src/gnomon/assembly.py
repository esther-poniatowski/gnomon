"""
The assembly of each level of an inquiry, computed from the records that state it.

A level is a problem, or a question that other questions serve, as :mod:`gnomon.completeness.levels`
defines it. Its assembly is never authored: the components, the parts, the citations between them,
the gaps and the limits of validity are read from the questions, their links, the answers and the
relations that the records state, and only the parts that a level leaves out are authored, in the
field ``excludes`` of its question. The decision on the assembly of a level states the rule.

The view reports and never concludes. A citation between two components names the edge of a
record that states it. The count of settled parts is reported beside the synthesis, the answer to
the level that the parts support, and no rule reads the parts as jointly sufficient: the acceptance
of the synthesis records that judgment.

See Also
--------
gnomon.views : the views of a project, among which this one.
gnomon.exposure : the exposure of each answer, which the view does not repeat.
"""

from __future__ import annotations

from typing import Any, Iterator, Mapping

from .completeness.levels import (
    answers_to,
    assessment_state,
    components,
    construct_parts,
    deferred_components,
    exclusions,
    levels,
    settled,
    settled_count,
)
from .completeness.paths import at
from .relations import Edge, edges, owner

Records = Mapping[str, Mapping[str, Any]]


def _accepted(question: str, records: Records) -> list[str]:
    return [a for a in answers_to(question, records) if records[a].get("status") == "accepted"]


def _ends(level: str, records: Records) -> dict[str, str]:
    """Return the question of each answer to the level or to one of its components."""
    questions = [level] + [c.question for c in components(level, records)]
    return {answer: q for q in questions for answer in answers_to(q, records)}


def _edge_end(edge: Edge, records: Records) -> list[str]:
    """Return the records that hold the other ends of an edge, its target or its members."""
    ends = [edge.target, *edge.members]
    return [str(owner(end, records)) for end in ends if owner(end, records)]


def citations(level: str, records: Records) -> list[dict[str, str]]:
    """Return the citations between the components of a level and the level itself.

    A planned citation is a link between two questions of the level; a realized one is an edge of
    an answer to one of them whose other end is an answer to another one, or a unit inside it.
    Each row names, in ``through``, the record and the field that state it.
    """
    record = records.get(level) or {}
    if record.get("type") != "question":
        return []
    questions = {level} | {c.question for c in components(level, records)}
    rows = []
    for question in sorted(questions):
        for link in records[question].get("links") or []:
            if isinstance(link, Mapping) and link.get("question") in questions:
                rows.append(
                    {
                        "level": level,
                        "source": question,
                        "target": str(link["question"]),
                        "relation": str(link.get("relation") or ""),
                        "through": f"{question} links",
                    }
                )
    ends = _ends(level, records)
    for answer, question in sorted(ends.items()):
        for edge in edges(records[answer]):
            for other in _edge_end(edge, records):
                cited = ends.get(other)
                if cited is None or cited == question:
                    continue
                rows.append(
                    {
                        "level": level,
                        "source": question,
                        "target": cited,
                        "relation": edge.relation,
                        "through": f"{answer} -> {other}",
                    }
                )
    unique = {tuple(row.values()): row for row in rows}
    return [unique[key] for key in sorted(unique)]


def _gap(level: str, gap: str, subject: str, detail: str) -> dict[str, str]:
    return {"level": level, "gap": gap, "subject": subject, "detail": detail}


def gaps(level: str, records: Records) -> list[dict[str, str]]:
    """Return the dependencies of a level not yet resolved.

    A component that supplies a part and is not settled is open, deferred or not; a decomposed
    question with no accepted answer of its own lacks its synthesis; an accepted part or synthesis
    whose satisfied assessments were all made against an earlier version of the question, or that
    holds no satisfied assessment, is unassessed.
    """
    record = records.get(level) or {}
    deferred = deferred_components(record)
    found = []
    supplying = [
        c.question for c in components(level, records) if c.supplies or c.link == "addresses"
    ]
    for question in supplying:
        if settled(question, records):
            continue
        kind = "deferred-component" if question in deferred else "open-component"
        detail = f"deferred as {deferred[question]}" if question in deferred else "not settled"
        found.append(_gap(level, kind, question, detail))
    if record.get("type") == "question" and supplying and not _accepted(level, records):
        found.append(_gap(level, "missing-synthesis", level, "no accepted answer to the level"))
    for question in [level, *supplying] if record.get("type") == "question" else supplying:
        for answer in _accepted(question, records):
            state = assessment_state(answer, records)
            if state != "satisfied":
                found.append(_gap(level, "unassessed-part", answer, f"assessment: {state}"))
    return found


def _limit(level: str, part: str, limit: str, unit: str, statement: Any) -> dict[str, str]:
    return {
        "level": level,
        "part": part,
        "limit": limit,
        "unit": unit,
        "statement": str(statement),
    }


def _answer_limits(level: str, answer: str, record: Mapping[str, Any]) -> Iterator[dict[str, str]]:
    """Yield the scope of one accepted answer: its domain, its conditions, the range of each
    idealization, its abstractions and its variant."""
    if record.get("domain"):
        yield _limit(level, answer, "domain", f"{answer}.domain", record["domain"])
    for ground in record.get("grounds") or []:
        if not isinstance(ground, Mapping):
            continue
        unit = f"{answer}.{ground.get('id')}"
        if ground.get("role") == "condition":
            yield _limit(level, answer, "condition", unit, ground.get("content") or "")
        elif ground.get("role") == "idealization" and ground.get("range"):
            yield _limit(level, answer, "idealization", unit, ground["range"])
    for abstraction in record.get("abstractions") or []:
        if isinstance(abstraction, Mapping) and abstraction.get("factor"):
            unit = f"{answer}.{abstraction.get('id')}"
            yield _limit(level, answer, "abstraction", unit, abstraction["factor"])
    if record.get("variant"):
        yield _limit(level, answer, "variant", f"{answer}.variant", record["variant"])


def limits(level: str, records: Records) -> list[dict[str, str]]:
    """Return the limits of validity of a level: the domain restrictions and the limit of its
    question, the scope of each accepted part and of the synthesis, and the parts out of scope.

    The limits are listed, never combined into one domain.
    """
    record = records.get(level) or {}
    if record.get("type") != "question":
        return []
    rows = []
    for restriction in at(record, "subject.domain.restrictions") or []:
        if isinstance(restriction, Mapping):
            text = restriction.get("values") or restriction.get("expression") or ""
            name = restriction.get("name") or restriction.get("of") or ""
            rows.append(_limit(level, level, "question-domain", str(name), text))
    limit = at(record, "subject.domain.limit.expression")
    if limit:
        rows.append(_limit(level, level, "question-limit", f"{level}.subject.domain.limit", limit))
    parts = [level] + [c.question for c in components(level, records) if c.supplies]
    for question in parts:
        for answer in _accepted(question, records):
            rows.extend(_answer_limits(level, answer, records[answer]))
    for entry in exclusions(record, "out-of-scope"):
        rows.append(
            _limit(level, level, "out-of-scope", f"{level}.{entry.get('id')}", entry.get("reading"))
        )
    return rows


def _level_row(level: str, records: Records) -> dict[str, Any]:
    """Return the row of one level: its parts, the parts settled, its synthesis and its gaps."""
    record = records[level]
    done, total = settled_count(level, records)
    synthesis = _accepted(level, records) if record.get("type") == "question" else []
    return {
        "level": level,
        "kind": str(record.get("type") or ""),
        "title": str(record.get("title") or ""),
        "status": str(record.get("status") or ""),
        "version": str(record.get("version") or ""),
        "parts": total,
        "settled": done,
        "synthesis": ", ".join(synthesis),
        "gaps": len(gaps(level, records)),
    }


def _component_rows(level: str, records: Records) -> list[dict[str, Any]]:
    """Return one row per component of a level, with its answers and its deferral."""
    deferred = deferred_components(records[level])
    return [
        {
            "level": level,
            "component": c.question,
            "link": c.link,
            "supplies": c.supplies or c.link == "addresses",
            "answers": ", ".join(answers_to(c.question, records)),
            "accepted": ", ".join(_accepted(c.question, records)),
            "settled": settled(c.question, records),
            "deferred": deferred.get(c.question, ""),
        }
        for c in components(level, records)
    ]


def _part_rows(level: str, records: Records) -> list[dict[str, str]]:
    """Return one row per part of a level: each answer to a supplying component, and each construct
    that a step obtains for it."""
    rows = []
    for c in components(level, records):
        if not (c.supplies or c.link == "addresses"):
            continue
        parts = [(a, "answer") for a in answers_to(c.question, records)]
        parts += [(r, "construct") for r in construct_parts(c.question, records)]
        for part, kind in parts:
            rows.append(
                {
                    "level": level,
                    "part": part,
                    "component": c.question,
                    "kind": kind,
                    "status": str(records[part].get("status") or ""),
                    "erotetic": str(at(records[part], "erotetic_relation.value") or ""),
                    "assessment": assessment_state(part, records),
                }
            )
    return rows


def _excluded_rows(level: str, records: Records) -> list[dict[str, str]]:
    return [
        {
            "level": level,
            "id": str(entry.get("id") or ""),
            "kind": str(entry.get("kind") or ""),
            "question": str(entry.get("question") or ""),
            "reading": str(entry.get("reading") or ""),
            "reason": str(entry.get("reason") or ""),
        }
        for entry in exclusions(records[level])
    ]


def assembly_tables(records: Records) -> dict[str, list[dict[str, Any]]]:
    """Return the tables of the assembly view, one row per level, component, part, citation, gap,
    limit and exclusion."""
    found = levels(records)
    return {
        "levels": [_level_row(level, records) for level in found],
        "components": [row for level in found for row in _component_rows(level, records)],
        "parts": [row for level in found for row in _part_rows(level, records)],
        "citations": [row for level in found for row in citations(level, records)],
        "gaps": [row for level in found for row in gaps(level, records)],
        "limits": [row for level in found for row in limits(level, records)],
        "excluded": [row for level in found for row in _excluded_rows(level, records)],
    }
