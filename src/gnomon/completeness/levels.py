"""
The levels of a decomposition: the questions of a problem, the components of a question, the parts
that settle a component, and the parts that a question excludes.

A level is a problem, or a question that other questions serve. The questions of a problem are the
questions that address it and narrow no other question, as the question tree shows them: a
question that narrows another one belongs to that question, not to the problem. Every computation
of the state of a problem reads the questions of the problem through :func:`problem_questions`,
so that an answer to a subquestion never counts as an answer to the problem.

The components of a question are the questions that serve it, each with the link that relates
them. A link names the other question, and its relation fixes the direction of service:

- a question linked by ``subquestion-of`` or ``enables`` to the level serves the level;
- a question that the level links by ``presupposes`` or ``explanans-from`` serves the level, since
  the level draws on its answer.

Only a component linked by ``subquestion-of`` supplies a part of the answer, since only an answer to
it narrows the answers to the level. The parts are composed by an answer to the level itself, its
synthesis, which the parts support; the acceptance of the synthesis is the act by which the
researcher judges the parts jointly sufficient. No rule here therefore reads the settled parts as
meeting a demand: the count of settled parts is reported, and the demand stays read from the
accepted answers to the questions of the problem.

A part that a level leaves out is stated in its field ``excludes``, of one of two kinds. A
``deferred`` part stays inside the demand: its component keeps its link and counts as open. An
``out-of-scope`` part lies outside the demand, so it is no component.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Mapping

from .. import findings as rules
from ..findings import Finding, finding
from .assessments import disposition, is_void
from .paths import at

Records = Mapping[str, Mapping[str, Any]]

#: The links by which the question that holds them serves the linked question.
SERVING_LINKS = ("subquestion-of", "enables")

#: The links by which the linked question serves the question that holds them.
SERVED_LINKS = ("presupposes", "explanans-from")

#: The link whose components supply the parts of an answer.
SUPPLYING_LINK = "subquestion-of"

#: The condition on which a step acts when it obtains a construct that counts as a part of the
#: answer to the question that the step serves.
OBTAINING = "obtaining"


def _links(question: Mapping[str, Any]) -> list[Mapping[str, Any]]:
    return [link for link in question.get("links") or [] if isinstance(link, Mapping)]


def narrowed(question: Mapping[str, Any]) -> list[str]:
    """Return the questions that a question narrows, through its links ``subquestion-of``.

    >>> narrowed({"links": [{"question": "quest.a.b", "relation": "subquestion-of"},
    ...                     {"question": "quest.a.c", "relation": "presupposes"}]})
    ['quest.a.b']
    """
    return [
        str(link["question"])
        for link in _links(question)
        if link.get("relation") == SUPPLYING_LINK and link.get("question")
    ]


def problem_questions(problem: str, records: Records) -> set[str]:
    """Return the questions of a problem: those that address it and narrow no other question.

    >>> problem_questions("prob.a", {
    ...     "quest.a": {"type": "question", "addresses": "prob.a"},
    ...     "quest.b": {"type": "question", "addresses": "prob.a",
    ...                 "links": [{"question": "quest.a", "relation": "subquestion-of"}]}})
    {'quest.a'}
    """
    return {
        key
        for key, record in records.items()
        if record.get("type") == "question"
        and record.get("addresses") == problem
        and not narrowed(record)
    }


@dataclass(frozen=True)
class Component:
    """One question that serves a level, with the relation of the link between them."""

    question: str
    link: str

    @property
    def supplies(self) -> bool:
        """Whether the answers to the component are parts of the answer to the level."""
        return self.link == SUPPLYING_LINK


def components(level: str, records: Records) -> list[Component]:
    """Return the components of a level, a question or a problem, sorted by question.

    >>> records = {"quest.p": {"type": "question",
    ...                        "links": [{"question": "quest.r", "relation": "presupposes"}]},
    ...            "quest.c": {"type": "question",
    ...                        "links": [{"question": "quest.p", "relation": "subquestion-of"}]},
    ...            "quest.r": {"type": "question"}}
    >>> [(c.question, c.link) for c in components("quest.p", records)]
    [('quest.c', 'subquestion-of'), ('quest.r', 'presupposes')]
    """
    record = records.get(level) or {}
    if record.get("type") == "problem":
        return [Component(q, "addresses") for q in sorted(problem_questions(level, records))]
    found = {
        Component(key, str(link.get("relation")))
        for key, other in records.items()
        if other.get("type") == "question"
        for link in _links(other)
        if link.get("question") == level and link.get("relation") in SERVING_LINKS
    }
    found |= {
        Component(str(link["question"]), str(link.get("relation")))
        for link in _links(record)
        if link.get("relation") in SERVED_LINKS and link.get("question") in records
    }
    return sorted(found, key=lambda c: (c.question, c.link))


def levels(records: Records) -> list[str]:
    """Return every level of a set of records: each problem, and each question with a component."""
    return sorted(
        key
        for key, record in records.items()
        if record.get("type") == "problem"
        or (record.get("type") == "question" and components(key, records))
    )


def exclusions(question: Mapping[str, Any], kind: str | None = None) -> list[Mapping[str, Any]]:
    """Return the entries of ``excludes`` of a question, of one kind when one is given."""
    return [
        entry
        for entry in question.get("excludes") or []
        if isinstance(entry, Mapping) and (kind is None or entry.get("kind") == kind)
    ]


def answers_to(question: str, records: Records) -> list[str]:
    """Return the answers to a question, sorted by identifier."""
    return sorted(
        key
        for key, record in records.items()
        if record.get("type") == "answer" and record.get("answers") == question
    )


def assessment_state(record: str, records: Records) -> str:
    """Return the state of the assessments of a record: ``satisfied`` when a current assessment is
    satisfied, ``void`` when only an assessment against an earlier version of the question is,
    ``unsatisfied`` when assessments exist and none is satisfied, and ``none`` otherwise.

    >>> records = {"quest.a": {"type": "question", "version": "2"},
    ...            "asmt.a": {"type": "assessment", "assesses": "ans.a", "against": "quest.a",
    ...                       "against_version": "1",
    ...                       "tests": {"admissibility": {"scope": {"verdict": "pass"}}}}}
    >>> assessment_state("ans.a", records)
    'void'
    """
    erotetic = at(records.get(record) or {}, "erotetic_relation.value")
    own = [
        r for r in records.values() if r.get("type") == "assessment" and r.get("assesses") == record
    ]
    satisfied = [
        a for a in own if disposition(a, str(erotetic) if erotetic else None) == "satisfied"
    ]
    if any(not is_void(a, records) for a in satisfied):
        return "satisfied"
    if satisfied:
        return "void"
    return "unsatisfied" if own else "none"


def construct_parts(question: str, records: Records) -> list[str]:
    """Return the records that steps of an itinerary obtain for a question: the output of each step
    whose rationale serves the question and acts on the condition ``obtaining``, when that output is
    a record other than an answer."""
    found = set()
    for itinerary in records.values():
        if itinerary.get("type") != "itinerary":
            continue
        for step in itinerary.get("steps") or []:
            if not isinstance(step, Mapping):
                continue
            output = at(step, "output.ref")
            if (
                at(step, "rationale.serves") == question
                and at(step, "rationale.acts_on") == OBTAINING
                and isinstance(output, str)
                and (records.get(output) or {}).get("type") not in (None, "answer", "question")
            ):
                found.add(output)
    return sorted(found)


def settled(question: str, records: Records) -> bool:
    """Return whether a component is settled: an accepted answer to it, or a stabilized construct
    obtained for it, holds a satisfied assessment against the present version of its question."""
    accepted = [a for a in answers_to(question, records) if records[a].get("status") == "accepted"]
    built = [
        c for c in construct_parts(question, records) if records[c].get("status") == "stabilized"
    ]
    return any(assessment_state(part, records) == "satisfied" for part in accepted + built)


def deferred_components(question: Mapping[str, Any]) -> dict[str, str]:
    """Return the components that a question defers, each with the identifier of its exclusion."""
    return {
        str(entry["question"]): str(entry.get("id") or "")
        for entry in exclusions(question, "deferred")
        if entry.get("question")
    }


def misplaced_exclusions(question: Mapping[str, Any], records: Records) -> list[Finding]:
    """Return each exclusion that contradicts the components of its question.

    A deferred part stays inside the demand, so a question that it names is a component linked by
    ``subquestion-of``; a part out of scope lies outside the demand, so a question that it names is
    no such component.

    >>> records = {"quest.c": {"type": "question",
    ...                        "links": [{"question": "quest.p", "relation": "subquestion-of"}]}}
    >>> question = {"id": "quest.p", "excludes": [
    ...     {"id": "later", "kind": "deferred", "question": "quest.x"},
    ...     {"id": "beyond", "kind": "out-of-scope", "question": "quest.c"}]}
    >>> [f.text for f in misplaced_exclusions(question, records)]  # doctest: +NORMALIZE_WHITESPACE
    ['excludes: later defers quest.x, which is no subquestion of quest.p',
     'excludes: beyond puts quest.c out of scope, which is still a subquestion of quest.p']
    """
    ident = str(question.get("id") or "")
    parts = {c.question for c in components(ident, records) if c.supplies}
    found = []
    for index, entry in enumerate(question.get("excludes") or []):
        if not isinstance(entry, Mapping) or not entry.get("question"):
            continue
        named, kind = str(entry["question"]), entry.get("kind")
        if kind == "deferred" and named not in parts:
            text = f"excludes: {entry.get('id')} defers {named}, which is no subquestion of {ident}"
        elif kind == "out-of-scope" and named in parts:
            text = (
                f"excludes: {entry.get('id')} puts {named} out of scope, which is still a"
                f" subquestion of {ident}"
            )
        else:
            continue
        found.append(
            finding(rules.COMPLETENESS_MISPLACED_EXCLUSION, text, "excludes", index, "question")
        )
    return found


def stale_deferrals(question: Mapping[str, Any], records: Records) -> list[Finding]:
    """Return each deferred component that holds an accepted answer, so that its deferral is stale.

    >>> records = {"ans.c": {"type": "answer", "answers": "quest.c", "status": "accepted"}}
    >>> [f.rule.id for f in stale_deferrals(
    ...     {"excludes": [{"id": "later", "kind": "deferred", "question": "quest.c"}]}, records)]
    ['completeness/excluded-answered']
    """
    found = []
    for index, entry in enumerate(question.get("excludes") or []):
        if not isinstance(entry, Mapping) or entry.get("kind") != "deferred":
            continue
        named = str(entry.get("question") or "")
        accepted = [a for a in answers_to(named, records) if records[a].get("status") == "accepted"]
        if named and accepted:
            text = (
                f"excludes: {entry.get('id')} defers {named}, which holds the accepted answer"
                f" {', '.join(accepted)}"
            )
            found.append(
                finding(rules.COMPLETENESS_EXCLUDED_ANSWERED, text, "excludes", index, "question")
            )
    return found


def answered_with_open_component(question: Mapping[str, Any], records: Records) -> list[Finding]:
    """Return a warning for a question marked ``answered`` while a subquestion is not settled.

    A deferred subquestion stays inside the demand, so it counts as open.

    >>> records = {"quest.c": {"type": "question",
    ...                        "links": [{"question": "quest.p", "relation": "subquestion-of"}]}}
    >>> [f.rule.id for f in answered_with_open_component(
    ...     {"id": "quest.p", "status": "answered"}, records)]
    ['completeness/answered-with-open-component']
    """
    if question.get("status") != "answered":
        return []
    ident = str(question.get("id") or "")
    open_parts = [
        c.question
        for c in components(ident, records)
        if c.supplies and not settled(c.question, records)
    ]
    if not open_parts:
        return []
    text = f"status: answered, and the subquestions {', '.join(open_parts)} are not settled"
    return [finding(rules.COMPLETENESS_ANSWERED_WITH_OPEN_COMPONENT, text, "status")]


def decomposition_findings(question: Mapping[str, Any], records: Records) -> list[Finding]:
    """Return the findings of the decomposition of a question: its exclusions and its status."""
    return (
        misplaced_exclusions(question, records)
        + stale_deferrals(question, records)
        + answered_with_open_component(question, records)
    )


def settled_count(level: str, records: Records) -> tuple[int, int]:
    """Return the number of settled parts of a level and the number of its supplying components."""
    supplying = [
        c.question for c in components(level, records) if c.supplies or c.link == "addresses"
    ]
    return sum(settled(q, records) for q in supplying), len(supplying)
