"""
What a filled inquiry must carry, read from the registry that declares it.

The requirements that govern a record are declared in two registries rather than restated here:

- the values a closed field admits, listed per record kind in ``data/vocabularies.yml``;
- the general ones, listed per record kind under ``always`` in ``data/requirements.yml``;
- the ones a level of commitment imposes on a target system or a phenomenon, under
  ``by_commitment``;
- the ones a value of a closed field imposes, such as the protocol of an experiment, under
  ``by_value``;
- the ones an epistemic aim adds, and the general ones the inquiry produces, under ``by_aim``. An
  inquiry that produces a phenomenon cannot be asked to state that phenomenon in advance, so
  those paths may stay empty.

An empty value means that a field is not filled. Whether an empty field is a gap or a value that
the inquiry will produce is read from the registry, never from the record.

A third kind is neither: a consistency between fields, such as an accuracy marked inapplicable
while outputs are listed for matching. No aim decides those, so each is its own check.

The specification notes document the same requirements and are checked against the registry, so no
check here reads a document.

See Also
--------
data/requirements.yml : the registry these functions read.
"""

from __future__ import annotations

from pathlib import Path
from typing import Any, Iterable, Mapping

import yaml

from . import findings as rules
from .findings import Entry, Finding, Place, Rule, Segment, finding
from .identifiers import split_reference
from .schemas import kinds, load_base, vocabulary_paths

DATA = Path(__file__).parent / "data"

#: The registry declaring what a filled inquiry must carry.
REQUIREMENT_REGISTRY = DATA / "requirements.yml"

#: The registry declaring the values each closed field admits.
VOCABULARY_REGISTRY = DATA / "vocabularies.yml"

#: The levels of commitment of a target system or a phenomenon, weakest first.
COMMITMENT_LEVELS: tuple[str, ...] = ("identified", "specified")

#: The subject slots of a question, each with the record kind its identifier names.
SUBJECT_SLOTS: Mapping[str, str] = {"target_system": "target-system", "phenomenon": "phenomenon"}

#: The subject slots of a question, each with the one placeholder type it admits.
SLOT_PLACEHOLDERS: Mapping[str, str] = {"target_system": "system", "phenomenon": "phenomenon"}


def is_empty(value: Any) -> bool:
    """Return whether ``value`` leaves its field unfilled: absent, null, or an empty string.

    An empty list or mapping is a value: it states that the block holds no entry.

    >>> [is_empty(v) for v in (None, "", "  ", [], "open")]
    [True, True, True, False, False]
    """
    return value is None or (isinstance(value, str) and not value.strip())


def is_unfilled(value: Any) -> bool:
    """Return whether a required specification is unfilled.

    A value is unfilled when it is empty, and a list or a mapping when every value that it holds is
    unfilled, so that a required block whose fields are all empty fails its requirement as a missing
    block does.

    >>> [is_unfilled(v) for v in (None, [], {}, {"a": None, "b": [""]}, [{"a": ""}], {"a": "x"}, 0)]
    [True, True, True, True, True, False, False]
    """
    if isinstance(value, Mapping):
        return all(is_unfilled(item) for item in value.values())
    if isinstance(value, list):
        return all(is_unfilled(item) for item in value)
    return is_empty(value)


def _registry(source: Path | None) -> dict[str, Any]:
    return yaml.safe_load((source or REQUIREMENT_REGISTRY).read_text(encoding="utf-8")) or {}


def requirements_by_aim(source: Path | None = None) -> dict[str, dict[str, list[str]]]:
    """Return, per epistemic aim, the paths its inquiry fixes and the ones it produces.

    Raises
    ------
    ValueError
        If the registry declares no aim.
    """
    by_aim = _registry(source).get("by_aim") or {}
    if not by_aim:
        raise ValueError(f"{(source or REQUIREMENT_REGISTRY).name} declares no aim")
    return {
        aim: {
            "required": [e["path"] for e in (entry.get("required") or [])],
            "to_produce": list(entry.get("to_produce") or []),
        }
        for aim, entry in by_aim.items()
    }


def always_required(kind: str, source: Path | None = None) -> list[str]:
    """Return the specifications every record of ``kind`` carries, whatever the inquiry."""
    return list((_registry(source).get("always") or {}).get(kind) or [])


def block_requirements(source: Path | None = None) -> dict[str, list[str]]:
    """Return, per path of an aim block of an answer, the specifications that the block carries,
    relative to it."""
    return {
        str(block): list(paths or [])
        for block, paths in (_registry(source).get("by_block") or {}).items()
    }


def record_kinds(source: Path | None = None) -> list[str]:
    """Return every record kind the registry states a general requirement for."""
    return sorted(_registry(source).get("always") or {})


def requirements_by_commitment(source: Path | None = None) -> dict[str, dict[str, list[str]]]:
    """Return, per level of commitment, the specifications each record kind carries at that level.

    Raises
    ------
    ValueError
        If the registry names a level outside :data:`COMMITMENT_LEVELS`.
    """
    table = _registry(source).get("by_commitment") or {}
    unknown = set(table) - set(COMMITMENT_LEVELS)
    if unknown:
        raise ValueError(f"unknown levels of commitment: {sorted(unknown)}")
    return {
        level: {kind: list(paths or []) for kind, paths in (table.get(level) or {}).items()}
        for level in COMMITMENT_LEVELS
    }


def commitment_requirements(
    kind: str, level: str, table: Mapping[str, Mapping[str, list[str]]]
) -> list[str]:
    """Return what a record of ``kind`` carries at ``level``, the weaker levels included.

    >>> table = {"identified": {"phenomenon": ["statement"]},
    ...          "specified": {"phenomenon": ["course"]}}
    >>> commitment_requirements("phenomenon", "specified", table)
    ['statement', 'course']
    """
    if level not in COMMITMENT_LEVELS:
        return []
    paths: list[str] = []
    for weaker in COMMITMENT_LEVELS[: COMMITMENT_LEVELS.index(level) + 1]:
        paths += list((table.get(weaker) or {}).get(kind) or [])
    return paths


def at(record: Mapping[str, Any], path: str) -> Any:
    """Return the value a dotted path names, or None when the path does not resolve.

    A step written ``key[]`` traverses the list it names and collects what the rest of the path
    reaches in each entry, so one path states a requirement bearing on every entry of a block.

    >>> at({"virtues": [{"virtue": "generality"}, {"virtue": "economy"}]}, "virtues[].virtue")
    ['generality', 'economy']
    """
    head, marker, tail = path.partition("[].")
    node: Any = record
    for key in head.split("."):
        if not isinstance(node, Mapping):
            return None
        node = node.get(key)
    if not marker:
        return node
    if not isinstance(node, list):
        return None
    return [at(entry, tail) for entry in node if isinstance(entry, Mapping)]


def path_segments(path: str) -> tuple[tuple[Segment, ...], str | None]:
    """Return the keys of a dotted path up to its first traversed list, and the rest of the path.

    A path written ``key[]`` names a field of every entry of a list, so its locus is the list and
    the field it names inside each entry is returned apart, or None when the path traverses none.

    >>> path_segments("task.required_accuracy")
    (('task', 'required_accuracy'), None)
    >>> path_segments("factors[].target_status")
    (('factors',), 'target_status')
    """
    head, marker, tail = path.partition("[].")
    return tuple(head.split(".")), (tail if marker else None)


def unmet_general(
    record: Mapping[str, Any],
    paths: list[str],
    produced: frozenset[str] | set[str] = frozenset(),
    label: str = "always required",
    rule: Rule = rules.COMPLETENESS_UNMET_REQUIREMENT,
) -> list[Finding]:
    """Return every required specification the record leaves unfilled.

    A specification is unfilled when it is absent, null, an empty string, or an empty list or
    mapping. The aim of the inquiry may produce a required specification, so the caller passes the
    paths that aim produces: those may stay unfilled, since the inquiry supplies their values.
    Each finding of ``rule`` lies at the unfilled path.
    """
    found = []
    for path in paths:
        if path not in produced and is_unfilled(at(record, path)):
            keys, field = path_segments(path)
            found.append(finding(rule, f"{label}: {path}", *keys, value=field))
    return found


def unmet_commitment(
    record: Mapping[str, Any],
    table: Mapping[str, Mapping[str, list[str]]],
    produced: frozenset[str] | set[str] = frozenset(),
) -> list[Finding]:
    """Return every specification that the level of commitment of the record requires and it lacks.

    A record at ``identified`` fixes its referent; a record at ``specified`` also writes the
    declarations that make it checkable. A record stating no admitted level is reported by the
    general requirement on ``commitment`` and by the vocabulary, so it is not reported here.
    """
    level = record.get("commitment")
    paths = commitment_requirements(str(record.get("type")), str(level), table)
    return unmet_general(
        record,
        paths,
        produced,
        label=f"commitment {level} requires",
        rule=rules.COMPLETENESS_UNMET_COMMITMENT,
    )


def requirements_by_presence(
    source: Path | None = None,
) -> dict[str, dict[str, dict[str, list[str]]]]:
    """Return, per record kind and field, the specifications that the presence and the absence of
    the field impose."""
    table = _registry(source).get("by_presence") or {}
    return {
        str(kind): {
            str(field): {
                state: list((cases or {}).get(state) or []) for state in ("present", "absent")
            }
            for field, cases in (fields or {}).items()
        }
        for kind, fields in table.items()
    }


def unmet_by_presence(
    record: Mapping[str, Any], table: Mapping[str, Mapping[str, Mapping[str, list[str]]]]
) -> list[Finding]:
    """Return every specification that the presence or the absence of a field requires and the
    record lacks.

    >>> table = {"model": {"derives_from": {"present": ["operations"], "absent": ["laws"]}}}
    >>> [f.text for f in unmet_by_presence({"type": "model"}, table)]
    ['derives_from absent requires: laws']
    >>> [f.text for f in unmet_by_presence({"type": "model", "derives_from": ["system.a"]}, table)]
    ['derives_from present requires: operations']
    """
    found: list[Finding] = []
    for field, cases in (table.get(str(record.get("type"))) or {}).items():
        state = "absent" if is_unfilled(record.get(field)) else "present"
        found += unmet_general(record, cases.get(state, []), label=f"{field} {state} requires")
    return found


def requirements_by_value(source: Path | None = None) -> dict[str, dict[str, dict[str, list[str]]]]:
    """Return, per record kind, field and value, the specifications that the value imposes."""
    table = _registry(source).get("by_value") or {}
    return {
        str(kind): {
            str(field): {str(value): list(paths or []) for value, paths in (values or {}).items()}
            for field, values in (fields or {}).items()
        }
        for kind, fields in table.items()
    }


def unmet_by_value(
    record: Mapping[str, Any],
    table: Mapping[str, Mapping[str, Mapping[str, list[str]]]],
    produced: frozenset[str] | set[str] = frozenset(),
) -> list[Finding]:
    """Return every specification that the value of a field of the record requires and it lacks.

    >>> table = {"design": {"kind": {"experiment": ["protocol"]}}}
    >>> [f.text for f in unmet_by_value({"type": "design", "kind": "experiment"}, table)]
    ['kind experiment requires: protocol']
    >>> unmet_by_value({"type": "design", "kind": "method"}, table)
    []
    """
    found: list[Finding] = []
    for field, values in (table.get(str(record.get("type"))) or {}).items():
        value = record.get(field)
        if isinstance(value, str) and value in values:
            found += unmet_general(
                record,
                values[value],
                produced,
                label=f"{field} {value} requires",
                rule=rules.COMPLETENESS_UNMET_BY_VALUE,
            )
    return found


def occurrence_by_category(source: Path | None = None) -> dict[str, list[str]]:
    """Return, per phenomenon category, the occurrence classes that the category admits."""
    table = _registry(source).get("occurrence_by_category") or {}
    return {str(category): list(classes or []) for category, classes in table.items()}


def mismatched_occurrence(
    phenomenon: Mapping[str, Any], table: Mapping[str, list[str]]
) -> list[Finding]:
    """Return the occurrence class that the category of the phenomenon does not admit.

    A particular occurrence is one token of a state, a process or an event. A structural property
    holds at each point of the course, as a state does. A regularity relates occurrences without
    being one, and a capacity is a disposition, so neither takes an occurrence class. An empty
    field leaves the pair unfilled, and nothing is reported.

    >>> table = {"regularity": ["not-applicable"],
    ...          "particular-occurrence": ["state", "process", "event"]}
    >>> [f.text for f in mismatched_occurrence({"category": "regularity", "occurrence": "event"},
    ...                                        table)]
    ['occurrence: event is no occurrence class of a regularity, which admits not-applicable']
    """
    category, occurrence = phenomenon.get("category"), phenomenon.get("occurrence")
    if not isinstance(category, str) or not isinstance(occurrence, str):
        return []
    if is_empty(category) or is_empty(occurrence) or category not in table:
        return []
    admitted = table[category]
    if occurrence in admitted:
        return []
    return [
        finding(
            rules.COMPLETENESS_MISMATCHED_OCCURRENCE,
            f"occurrence: {occurrence} is no occurrence class of a {category}, which admits"
            f" {' or '.join(admitted)}",
            "occurrence",
        )
    ]


def placeholder_types(source: Path | None = None) -> frozenset[str]:
    """Return the types a placeholder of a question slot may take, as the vocabulary lists them."""
    return vocabularies("question", source).get("subject.placeholder", frozenset())


def unresolved_slots(
    question: Mapping[str, Any],
    records: Mapping[str, Mapping[str, Any]],
    types: Iterable[str],
) -> list[Finding]:
    """Return every subject slot that holds neither an identified record nor a typed placeholder.

    A slot of a question schema awaits an item of a type from a closed list, described in words, and
    the type fits the slot: the target-system slot awaits a system, and the phenomenon slot a
    phenomenon. A slot of a question names a record that fixes its referent, so the record exists,
    has the kind the slot expects, and carries an identification. Both checks are decidable, and the
    stronger level, a record whose declarations resolve, is checked by the resolution of its
    symbols.

    Parameters
    ----------
    question : mapping
        One filled question record.
    records : mapping
        The records of the problem, keyed by identifier.
    types : iterable of str
        The types a placeholder may take.
    """
    admitted = set(types)
    subject = question.get("subject") or {}
    found = []
    for slot, kind in SUBJECT_SLOTS.items():
        value, where, field = subject.get(slot), f"subject.{slot}", ("subject", slot)
        if isinstance(value, Mapping):
            awaited = value.get("placeholder")
            if awaited not in admitted:
                found.append(
                    finding(
                        rules.COMPLETENESS_UNADMITTED_PLACEHOLDER,
                        f"{where}: the placeholder type {awaited!r} is not admitted",
                        *field,
                        "placeholder",
                    )
                )
            elif awaited != SLOT_PLACEHOLDERS[slot]:
                found.append(
                    finding(
                        rules.COMPLETENESS_MISFIT_PLACEHOLDER,
                        f"{where}: the placeholder type {awaited!r} does not fit the slot, which"
                        f" awaits {SLOT_PLACEHOLDERS[slot]!r}",
                        *field,
                        "placeholder",
                    )
                )
            if not value.get("description"):
                found.append(
                    finding(
                        rules.COMPLETENESS_UNDESCRIBED_PLACEHOLDER,
                        f"{where}: the placeholder carries no description",
                        *field,
                        "description",
                    )
                )
            continue
        if not isinstance(value, str) or is_empty(value):
            found.append(
                finding(
                    rules.COMPLETENESS_UNRESOLVED_SLOT,
                    f"{where}: holds neither a record identifier nor a placeholder",
                    *field,
                )
            )
            continue
        record = records.get(value)
        if record is None:
            found.append(
                finding(
                    rules.COMPLETENESS_UNKNOWN_SLOT_RECORD,
                    f"{where}: no record carries the identifier {value}",
                    *field,
                )
            )
        elif record.get("type") != kind:
            found.append(
                finding(
                    rules.COMPLETENESS_MISTYPED_SLOT_RECORD,
                    f"{where}: {value} is a {record.get('type')} record, not a {kind} record",
                    *field,
                )
            )
        elif not (record.get("identification") or {}).get("description"):
            found.append(
                finding(
                    rules.COMPLETENESS_UNIDENTIFIED_SLOT_RECORD,
                    f"{where}: {value} carries no identification, so its referent is not fixed",
                    *field,
                )
            )
    return found


def unresolved_question_references(
    question: Mapping[str, Any], records: Mapping[str, Mapping[str, Any]]
) -> list[Finding]:
    """Return every problem, linked question and background that a question names and that is
    missing.

    A question names the problem it serves, the questions it is linked to with the shared record
    carrying the link, and the background records whose laws it admits. Each name resolves to a
    record of the expected kind, and an admitted background describes the target of the question,
    since its laws are stated over the quantities of that target.
    """

    def kind_of(identifier: Any) -> Any:
        return (records.get(identifier) or {}).get("type") if isinstance(identifier, str) else None

    found = []
    addressed = question.get("addresses")
    if addressed is not None and kind_of(addressed) != "problem":
        found.append(
            finding(
                rules.COMPLETENESS_UNADDRESSED_PROBLEM,
                f"addresses: {addressed} is no problem record",
                "addresses",
            )
        )
    for index, link in enumerate(question.get("links") or []):
        if not isinstance(link, Mapping):
            continue
        other, via = link.get("question"), link.get("via")
        if kind_of(other) != "question":
            found.append(
                finding(
                    rules.COMPLETENESS_LINK_NOT_QUESTION,
                    f"links[{index}]: {other} is no question record",
                    "links",
                    index,
                    "question",
                )
            )
        elif other == question.get("id"):
            found.append(
                finding(
                    rules.COMPLETENESS_SELF_LINK,
                    f"links[{index}]: a question is linked to itself",
                    "links",
                    index,
                    "question",
                )
            )
        if via is not None and kind_of(via) is None:
            found.append(
                finding(
                    rules.COMPLETENESS_UNKNOWN_LINK_RECORD,
                    f"links[{index}]: no record carries the identifier {via}",
                    "links",
                    index,
                    "via",
                )
            )
    subject = question.get("subject") or {}
    target = subject.get("target_system")
    for index, name in enumerate(subject.get("background") or []):
        if kind_of(name) != "background":
            found.append(
                finding(
                    rules.COMPLETENESS_NOT_BACKGROUND,
                    f"subject.background: {name} is no background record",
                    "subject",
                    "background",
                    index,
                )
            )
        elif isinstance(target, str) and records[name].get("describes") != target:
            found.append(
                finding(
                    rules.COMPLETENESS_FOREIGN_BACKGROUND,
                    f"subject.background: {name} describes another target than {target}",
                    "subject",
                    "background",
                    index,
                )
            )
    return found


def unstated_function_sense(question: Mapping[str, Any]) -> list[Finding]:
    """Return the functional question that does not say which sense of function it requests.

    A function in the causal-role sense is the contribution of a part to a capacity of the system
    that contains it; a function in the etiological sense is the effect for which the part was
    selected. The two call for different answers, a functional analysis or a selection history, so
    a question requesting a functional relation states which one it requests.
    """
    task = question.get("task") or {}
    if task.get("requested_relation") != "functional":
        return []
    if task.get("function_sense") in ("causal-role", "etiological"):
        return []
    return [
        finding(
            rules.COMPLETENESS_UNSTATED_FUNCTION_SENSE,
            "task.function_sense: a functional relation is requested without its sense of function",
            "task",
            "function_sense",
        )
    ]


def malformed_credence(assessment: Mapping[str, Any]) -> list[Finding]:
    """Return the credence that is no degree of belief, or that states no basis.

    A credence is a number between zero and one; a value outside that interval is no probability,
    and a value without its basis cannot be revised when the evidence changes.
    """
    credence = assessment.get("credence")
    if credence is None:
        return []
    if not isinstance(credence, Mapping):
        return [
            finding(
                rules.COMPLETENESS_MALFORMED_CREDENCE,
                "credence: holds neither a value nor a basis",
                "credence",
            )
        ]
    found = []
    value = credence.get("value")
    if isinstance(value, bool) or not isinstance(value, (int, float)) or not 0 <= value <= 1:
        found.append(
            finding(
                rules.COMPLETENESS_CREDENCE_OUT_OF_RANGE,
                f"credence.value: {value!r} is no number between 0 and 1",
                "credence",
                "value",
            )
        )
    if not credence.get("basis"):
        found.append(
            finding(
                rules.COMPLETENESS_CREDENCE_WITHOUT_BASIS,
                "credence.basis: the value states no basis",
                "credence",
                "basis",
            )
        )
    return found


def result_aims(source: Path | None = None) -> dict[str, frozenset[str]]:
    """Return, per type of result of a problem, the aims of the questions that may serve it."""
    registry = yaml.safe_load((source or VOCABULARY_REGISTRY).read_text(encoding="utf-8")) or {}
    types = ((registry.get("vocabularies") or {}).get("problem") or {}).get(".result_type") or []
    return {str(entry["value"]): frozenset(entry.get("admits") or []) for entry in types}


def mismatched_request(
    problem: Mapping[str, Any], records: Mapping[str, Mapping[str, Any]]
) -> list[Finding]:
    """Return the associated question of a problem that does not take the request of its demand.

    The associated question is derived from the problem, so it takes the request of the demand. A
    question record that states it addresses the problem and carries the same request.

    >>> problem = {"id": "prob.a", "request": "one", "associated_question": "quest.a"}
    >>> mismatched_request(problem,
    ...                    {"quest.a": {"type": "question", "addresses": "prob.a",
    ...                                 "request": "one"}})
    []
    """
    named = problem.get("associated_question")
    if not named:
        return []
    question = records.get(named) if isinstance(named, str) else None
    if (
        question is None
        or question.get("type") != "question"
        or question.get("addresses") != problem.get("id")
    ):
        return [
            finding(
                rules.COMPLETENESS_MISMATCHED_REQUEST,
                f"associated_question: {named} is no question record addressing"
                f" {problem.get('id')}",
                "associated_question",
            )
        ]
    if question.get("request") != problem.get("request"):
        return [
            finding(
                rules.COMPLETENESS_MISMATCHED_REQUEST,
                f"associated_question: {named} asks under the request {question.get('request')},"
                f" and the problem under {problem.get('request')}",
                "associated_question",
            )
        ]
    return []


def unbounded_aim(
    question: Mapping[str, Any],
    records: Mapping[str, Mapping[str, Any]],
    aims: Mapping[str, Iterable[str]],
) -> list[Finding]:
    """Return the aim of a question that the type of result of its problem does not admit.

    The demand of a problem bounds the aim of each question that serves it. The bound reads the type
    of result only: a condition that the demand table attaches to an aim, such as a closed
    background for modal knowledge, is not checked.

    >>> records = {"prob.a": {"type": "problem", "result_type": "explanation"}}
    >>> texts = [f.text for f in unbounded_aim({"addresses": "prob.a",
    ...                                         "task": {"epistemic_aim": "prediction"}},
    ...                                        records, {"explanation": ["explanation"]})]
    >>> texts
    ['task.epistemic_aim: prediction does not serve a demand for explanation']
    """
    addresses = question.get("addresses")
    problem = records.get(addresses) if isinstance(addresses, str) else None
    aim = at(question, "task.epistemic_aim")
    kind = (problem or {}).get("result_type")
    if not aim or not isinstance(kind, str) or kind not in aims or aim in set(aims[kind]):
        return []
    return [
        finding(
            rules.COMPLETENESS_UNBOUNDED_AIM,
            f"task.epistemic_aim: {aim} does not serve a demand for {kind}",
            "task",
            "epistemic_aim",
        )
    ]


def demand_met(
    problem: Mapping[str, Any],
    records: Mapping[str, Mapping[str, Any]],
    classes: Mapping[str, str],
    holders: Mapping[str, Iterable[str]],
) -> bool | None:
    """Return whether the records meet the demand of a problem, or None when no rule applies.

    The demand is met once acts of the researcher settle the demanded results. For a result of a
    claim type, an answer to a question that addresses the problem is accepted, gives a complete
    answer, and holds a satisfied assessment; the number and the completeness that the request
    fixes are those of that direct answer. For a result of a construct type, a record that holds
    the type is stabilized, with a satisfied assessment against the problem. Under the request
    ``decision``, every candidate is settled in view of an assessment: an answer accepted or
    retracted, the record of a construct stabilized or retracted. A type of another class has no
    solving rule, so the function returns None.

    Parameters
    ----------
    problem : mapping
        One filled problem record.
    records : mapping
        The records of the problem, keyed by identifier.
    classes : mapping
        The class of each product type, read from the product-type registry.
    holders : mapping
        The record kinds that hold each product type.
    """
    kind, ident = problem.get("result_type"), problem.get("id")
    klass = classes.get(str(kind))
    if klass not in ("claim", "construct"):
        return None
    questions = {
        i for i, r in records.items() if r.get("type") == "question" and r.get("addresses") == ident
    }
    assessments = [r for r in records.values() if r.get("type") == "assessment"]

    def assessed(name: str) -> list[Mapping[str, Any]]:
        return [a for a in assessments if a.get("assesses") == name]

    answers = {
        i: r
        for i, r in records.items()
        if r.get("type") == "answer" and r.get("answers") in questions
    }
    constructs = {
        i: r
        for i, r in records.items()
        if r.get("type") in set(holders.get(str(kind), ()))
        and any(a.get("against") == ident for a in assessed(i))
    }
    if problem.get("request") == "decision":
        candidates = answers if klass == "claim" else constructs
        settled = {"answer": {"accepted", "retracted"}}
        return bool(candidates) and all(
            r.get("status") in settled.get(str(r.get("type")), {"stabilized", "retracted"})
            and bool(assessed(i))
            for i, r in candidates.items()
        )
    if klass == "claim":
        return any(
            r.get("status") == "accepted"
            and at(r, "erotetic_relation.value") == "complete"
            and any(disposition(a) == "satisfied" for a in assessed(i))
            for i, r in answers.items()
        )
    return any(
        r.get("status") == "stabilized"
        and any(a.get("against") == ident and disposition(a) == "satisfied" for a in assessed(i))
        for i, r in constructs.items()
    )


def presupposition_denied(
    problem: Mapping[str, Any], records: Mapping[str, Mapping[str, Any]]
) -> bool | None:
    """Return whether an accepted answer denies a presupposition of the associated question, or None
    when no question is named.

    A corrective answer denies a presupposition of the question that it answers, so an accepted
    corrective answer to the associated question puts the negation of a presupposition of that
    question into the accepted knowledge, which dissolves the problem.

    >>> records = {"ans.a": {"type": "answer", "answers": "quest.a", "status": "accepted",
    ...                      "erotetic_relation": {"value": "corrective"}}}
    >>> presupposition_denied({"associated_question": "quest.a"}, records)
    True
    """
    named = problem.get("associated_question")
    if not named:
        return None
    return any(
        r.get("type") == "answer"
        and r.get("answers") == named
        and r.get("status") == "accepted"
        and at(r, "erotetic_relation.value") == "corrective"
        for r in records.values()
    )


def readable_obstacles(
    problem: Mapping[str, Any],
    records: Mapping[str, Mapping[str, Any]],
    classes: Mapping[str, str],
    holders: Mapping[str, Iterable[str]],
) -> dict[str, bool]:
    """Return, for each knowledge obstacle that the records decide, whether it holds.

    An open gap and unassessed candidates require that the problem exists: its demand is not met
    and no accepted answer denies a presupposition of its associated question. The proposed
    candidates are the answers to the questions of the problem that are neither accepted nor
    retracted: an open gap when none exists, unassessed candidates when some exist and no answer is
    accepted. An unsound presupposition is an accepted answer that denies a presupposition of the
    associated question. An obstacle that the records do not decide is left out.
    """
    found: dict[str, bool] = {}
    denied = presupposition_denied(problem, records)
    if denied is not None:
        found["unsound-presupposition"] = denied
    met = demand_met(problem, records, classes, holders)
    if met is None or denied is None:
        return found
    questions = {
        i
        for i, r in records.items()
        if r.get("type") == "question" and r.get("addresses") == problem.get("id")
    }
    answers = [
        r for r in records.values() if r.get("type") == "answer" and r.get("answers") in questions
    ]
    exists = not met and not denied
    proposed = [r for r in answers if r.get("status") not in ("accepted", "retracted")]
    accepted = [r for r in answers if r.get("status") == "accepted"]
    found["open-gap"] = exists and not proposed
    found["unassessed-candidates"] = exists and bool(proposed) and not accepted
    return found


def misstated_obstacles(
    problem: Mapping[str, Any],
    records: Mapping[str, Mapping[str, Any]],
    classes: Mapping[str, str],
    holders: Mapping[str, Iterable[str]],
) -> list[Finding]:
    """Return every knowledge obstacle that the records decide and the problem states otherwise."""
    stated = {
        str(entry.get("obstacle"))
        for entry in problem.get("knowledge_obstacles") or []
        if isinstance(entry, Mapping)
    }
    found = []
    for name, holds in readable_obstacles(problem, records, classes, holders).items():
        if holds and name not in stated:
            found.append(
                finding(
                    rules.COMPLETENESS_UNSTATED_OBSTACLE,
                    f"knowledge_obstacles: the records show {name}, which the problem does not"
                    " state",
                    "knowledge_obstacles",
                    value=name,
                )
            )
        elif not holds and name in stated:
            found.append(
                finding(
                    rules.COMPLETENESS_UNSUPPORTED_OBSTACLE,
                    f"knowledge_obstacles: the problem states {name}, which its records contradict",
                    "knowledge_obstacles",
                    value=name,
                )
            )
    return found


def unsupported_outcome(
    problem: Mapping[str, Any],
    records: Mapping[str, Mapping[str, Any]],
    classes: Mapping[str, str],
    holders: Mapping[str, Iterable[str]],
) -> list[Finding]:
    """Return a status of the problem that its records contradict.

    The status ``solved`` requires the demand met, and the status ``dissolved`` an accepted answer
    that denies a presupposition of the associated question; each of these, once the records show
    it, ends a problem still posed or refined. An abandoned problem is not read, since that outcome
    records a decision of the researcher only.
    """
    status, denied = problem.get("status"), presupposition_denied(problem, records)
    if denied is not None:
        if status == "dissolved" and not denied:
            return [
                finding(
                    rules.COMPLETENESS_UNSUPPORTED_DISSOLVED,
                    "status: dissolved, and no accepted answer denies a presupposition of"
                    f" {problem.get('associated_question')}",
                    "status",
                )
            ]
        if denied and status in ("posed", "refined"):
            return [
                finding(
                    rules.COMPLETENESS_UNRECORDED_DISSOLUTION,
                    f"status: {status}, and an accepted answer denies a presupposition of"
                    f" {problem.get('associated_question')}",
                    "status",
                )
            ]
    met = demand_met(problem, records, classes, holders)
    if met is None:
        return []
    if status == "solved" and not met:
        return [
            finding(
                rules.COMPLETENESS_UNSUPPORTED_SOLVED,
                "status: solved, and the records do not meet the demand",
                "status",
            )
        ]
    if met and status in ("posed", "refined"):
        return [
            finding(
                rules.COMPLETENESS_UNRECORDED_SOLUTION,
                f"status: {status}, and the records meet the demand",
                "status",
            )
        ]
    return []


def misdirected_assessment(
    assessment: Mapping[str, Any],
    records: Mapping[str, Mapping[str, Any]],
    construct_kinds: Iterable[str],
) -> list[Finding]:
    """Return every mismatch between what an assessment assesses, its standard and its tests.

    An assessment tests a candidate answer against the specification of a question, through its
    tests of admissibility and of warrant, or a construct that a problem demands against the
    constraints of that problem, through one verdict per constraint. The record assessed decides
    which standard and which tests apply.

    Parameters
    ----------
    assessment : mapping
        One filled assessment record.
    records : mapping
        The records of the problem, keyed by identifier.
    construct_kinds : iterable of str
        The record kinds that hold a construct, read from the product-type registry.
    """
    assessed, standard = assessment.get("assesses"), assessment.get("against")
    target = records.get(assessed) if isinstance(assessed, str) else None
    if target is None:
        return [
            finding(
                rules.COMPLETENESS_UNKNOWN_ASSESSED,
                f"assesses: {assessed} is no record",
                "assesses",
            )
        ]
    tests = assessment.get("tests") or {}
    against = records.get(standard) if isinstance(standard, str) else None
    found: list[Finding] = []
    if target.get("type") == "answer":
        expected, shape = "question", ("admissibility", "warrant")
        found += [
            finding(
                rules.COMPLETENESS_MISSHAPEN_TESTS,
                f"tests.{level}: an assessment of an answer holds its tests of {level}",
                "tests",
                level,
            )
            for level in shape
            if not isinstance(tests.get(level), Mapping) or not tests.get(level)
        ]
        if tests.get("constraints"):
            found.append(
                finding(
                    rules.COMPLETENESS_MISSHAPEN_TESTS,
                    "tests.constraints: an assessment of an answer holds no verdict per constraint",
                    "tests",
                    "constraints",
                )
            )
    elif target.get("type") in set(construct_kinds):
        expected = "problem"
        verdicts = tests.get("constraints")
        if not isinstance(verdicts, list) or not verdicts:
            found.append(
                finding(
                    rules.COMPLETENESS_MISSHAPEN_TESTS,
                    "tests.constraints: an assessment of a construct holds one verdict per"
                    " constraint",
                    "tests",
                    "constraints",
                )
            )
            verdicts = []
        found += [
            finding(
                rules.COMPLETENESS_MISSHAPEN_TESTS,
                f"tests.{level}: an assessment of a construct holds no tests of {level}",
                "tests",
                level,
            )
            for level in ("admissibility", "warrant")
            if tests.get(level)
        ]
        stated = {
            c.get("name")
            for c in (against or {}).get("constraints") or []
            if isinstance(c, Mapping)
        }
        if against is not None and against.get("type") == "problem":
            found += [
                finding(
                    rules.COMPLETENESS_UNKNOWN_CONSTRAINT,
                    f"tests.constraints: {entry.get('constraint')} is no constraint of {standard}",
                    "tests",
                    "constraints",
                    Entry(index, entry),
                )
                for index, entry in enumerate(verdicts)
                if isinstance(entry, Mapping) and entry.get("constraint") not in stated
            ]
    else:
        return [
            finding(
                rules.COMPLETENESS_UNASSESSABLE_RECORD,
                f"assesses: {assessed} is a {target.get('type')} record, neither an answer nor a"
                " construct",
                "assesses",
            )
        ]
    against_type = (against or {}).get("type")
    if against_type != expected:
        kind = f"a {against_type} record" if against_type else "no record"
        assessed_kind = str(target.get("type"))
        article = "an" if assessed_kind[:1] in "aeiou" else "a"
        found.insert(
            0,
            finding(
                rules.COMPLETENESS_MISMATCHED_STANDARD,
                f"against: {standard} is {kind}, and an assessment of {article} {assessed_kind} is"
                " made"
                f" against a {expected}",
                "against",
            ),
        )
    return found


def disposition(assessment: Mapping[str, Any], erotetic_relation: str | None = None) -> str:
    """Return the disposition of an assessment, read from its verdicts.

    An answer satisfies its question only when it is admissible and warranted, and a construct meets
    its problem only when it meets every constraint, so one failed test decides the disposition.
    Without a failure, a pending verdict withholds it. A corrective answer shows that a
    presupposition of its question is false, so it cannot satisfy that question: the disposition
    that would be ``satisfied`` is ``corrective`` instead.

    Parameters
    ----------
    assessment : mapping
        One filled assessment record.
    erotetic_relation : str, optional
        The value of the erotetic relation of the assessed answer, read from its field
        ``erotetic_relation.value``. When omitted, the answer is not treated as corrective.

    Examples
    --------
    >>> disposition({"tests": {"admissibility": {"scope": {"verdict": "pass"}},
    ...                        "warrant": {"closure": {"verdict": "fail"}}}})
    'not-satisfied'
    >>> disposition({"tests": {"admissibility": {"scope": {"verdict": "pending"}}}})
    'withheld'
    >>> disposition({"tests": {"warrant": {"selection": {"verdict": "not-applicable"}}}})
    'satisfied'
    >>> disposition({"tests": {"warrant": {"closure": {"verdict": "pass"}}}}, "corrective")
    'corrective'
    >>> disposition({"tests": {"warrant": {"closure": {"verdict": "pending"}}}}, "corrective")
    'withheld'
    >>> disposition({"tests": {"constraints": [{"constraint": "c1", "verdict": "pass"},
    ...                                        {"constraint": "c2", "verdict": "fail"}]}})
    'not-satisfied'
    """
    tests = assessment.get("tests") or {}
    verdicts = [
        (entry or {}).get("verdict")
        for level in ("admissibility", "warrant")
        for entry in (tests.get(level) or {}).values()
    ] + [
        (entry or {}).get("verdict")
        for entry in tests.get("constraints") or []
        if isinstance(entry, Mapping)
    ]
    if "fail" in verdicts:
        return "not-satisfied"
    if any(verdict not in ("pass", "not-applicable") for verdict in verdicts):
        return "withheld"
    return "corrective" if erotetic_relation == "corrective" else "satisfied"


def premature_appraisal(assessment: Mapping[str, Any]) -> list[Finding]:
    """Return the appraisal of an answer that has not passed both tiers of tests.

    A virtue ranks answers that already satisfy the question, and never compensates for a failed
    test, so an answer is appraised only once no test of admissibility or of warrant fails or
    stays pending.

    >>> failing = {"tests": {"warrant": {"closure": {"verdict": "fail"}}},
    ...            "appraisal": [{"virtue": "unification", "assessment": "high"}]}
    >>> [f.text for f in premature_appraisal(failing)]
    ['appraisal: the answer is appraised although its disposition is not-satisfied']
    >>> premature_appraisal({**failing, "appraisal": []})
    []
    """
    state = disposition(assessment)
    if state in ("satisfied", "corrective") or is_unfilled(assessment.get("appraisal")):
        return []
    return [
        finding(
            rules.COMPLETENESS_PREMATURE_APPRAISAL,
            f"appraisal: the answer is appraised although its disposition is {state}",
            "appraisal",
        )
    ]


def unmet_by_aim(
    question: Mapping[str, Any],
    records: Mapping[str, Mapping[str, Any]],
    required: Mapping[str, dict[str, list[str]]],
) -> list[Finding]:
    """Return every specification the aim of this question requires and the records leave open.

    Parameters
    ----------
    question : mapping
        One filled question record.
    records : mapping
        The records its paths reach, keyed by the prefix that names them: ``question``,
        ``phenomenon`` and ``target-system``.
    required : mapping
        The table the registry declares.

    Notes
    -----
    Each finding concerns the question, whose aim imposes the requirement: it lies at
    ``task.epistemic_aim``, with the required path as discriminator, whichever record that path
    reaches.

    An aim fixes what an answer must deliver, so it requires a specification to be filled and
    never a value that specification takes. Which value is right is a judgement of the inquiry,
    and a rule that reaches inside a field belongs to a consistency check between fields.
    """
    aim = at(question, "task.epistemic_aim")
    missing = []
    for path in (required.get(str(aim)) or {}).get("required", []):
        prefix, _, rest = path.partition(".")
        if is_unfilled(at(records.get(prefix, {}), rest)):
            missing.append(
                finding(
                    rules.COMPLETENESS_UNMET_AIM,
                    f"{aim} requires {path}",
                    "task",
                    "epistemic_aim",
                    value=path,
                )
            )
    return missing


def contradictory_accuracy(question: Mapping[str, Any]) -> list[Finding]:
    """Return the matches a question lists while declaring that accuracy does not apply.

    No aim decides whether an answer is matched against a measurement: an inquiry over a formal
    model class may match measured exponents, and one seeking a theorem may match nothing. The
    rule is therefore a consistency between fields rather than a requirement of an aim.
    """
    accuracy = at(question, "task.required_accuracy") or {}
    if accuracy.get("standard") != "not-applicable":
        return []
    return [
        finding(
            rules.COMPLETENESS_CONTRADICTORY_ACCURACY,
            f"task.required_accuracy.{key} is listed although accuracy does not apply",
            "task",
            "required_accuracy",
            key,
        )
        for key in ("outputs_to_match", "structures_to_match")
        if accuracy.get(key)
    ]


def incomplete_operations(model: Mapping[str, Any]) -> list[Finding]:
    """Return every operation of a derived model that lacks a field required by its kind or its
    error.

    A controlled error states its bound, an approximation states its regime, and a singular limit
    states the order of its limits, as the note on derived models requires.

    >>> model = {"operations": [{"id": "near", "kind": "approximate", "error": "controlled"}]}
    >>> for f in incomplete_operations(model):
    ...     print(f.text)
    operations.near: a controlled error states its bound
    operations.near: an approximation states its regime
    """
    found: list[Finding] = []
    for index, entry in enumerate(model.get("operations") or []):
        if not isinstance(entry, Mapping):
            continue
        name = entry.get("id")
        required = [
            ("bound", entry.get("error") == "controlled", "a controlled error states its bound"),
            ("regime", entry.get("kind") == "approximate", "an approximation states its regime"),
            (
                "order",
                entry.get("kind") == "limit" and entry.get("error") == "singular",
                "a singular limit states the order of its limits",
            ),
        ]
        found += [
            finding(
                rules.COMPLETENESS_INCOMPLETE_OPERATION,
                f"operations.{name}: {message}",
                "operations",
                index,
                field,
            )
            for field, applies, message in required
            if applies and is_unfilled(entry.get(field))
        ]
    return found


def unclassified_operations(
    answer: Mapping[str, Any], records: Mapping[str, Mapping[str, Any]]
) -> list[Finding]:
    """Return every operation of a model on the route of the answer that no ground of the answer
    names.

    Only an answer classifies an assumption against its target, so each operation of a model on
    which its route runs is named by a ground, by the identifier of the operation or by a symbol
    that the operation yields: the removal of the noise as an idealization, a restriction as a
    condition, a posited law as a warrant.

    >>> model = {"id": "mod.a.b", "type": "model",
    ...          "operations": [{"id": "near", "yields": ["J"]}, {"id": "drop"}]}
    >>> answer = {"route": {"runs_on": ["mod.a.b"]}, "grounds": [{"record": "mod.a.b.J"}]}
    >>> [f.text for f in unclassified_operations(answer, {"mod.a.b": model})]
    ['operation drop of mod.a.b is named by no ground of the answer']
    """
    named = {
        str(ground.get("record"))
        for ground in answer.get("grounds") or []
        if isinstance(ground, Mapping)
    }
    found: list[Finding] = []
    for identifier in (answer.get("route") or {}).get("runs_on") or []:
        model = records.get(str(identifier)) or {}
        if model.get("type") != "model":
            continue
        for block, label in (("operations", "operation"), ("assumptions", "assumption")):
            for entry in model.get(block) or []:
                units = [entry.get("id"), *(entry.get("yields") or [])]
                if not any(f"{identifier}.{unit}" in named for unit in units if unit):
                    found.append(
                        finding(
                            rules.COMPLETENESS_UNCLASSIFIED_OPERATION,
                            f"{label} {entry.get('id')} of {identifier} is named by no ground of"
                            " the answer",
                            "grounds",
                        )
                    )
    return found


def unbound_outputs(
    answer: Mapping[str, Any], question: Mapping[str, Any], records: Mapping[str, Mapping[str, Any]]
) -> list[Finding]:
    """Return the missing binding of an answer on a model whose question names outputs to match.

    The comparison with the outputs runs through a binding, so a declared use does not replace it,
    even on a formal target, as the rule on a declared use states.

    >>> question = {"task": {"required_accuracy": {"outputs_to_match": [{"target": "phen.a.b.x"}]}}}
    >>> answer = {"route": {"runs_on": ["mod.a.b"]}, "use": {"value": "tool"}}
    >>> [f.text for f in unbound_outputs(answer, question, {"mod.a.b": {"type": "model"}})]
    ['the question names outputs to match, and the answer on a model cites no binding']
    """
    outputs = at(question, "task.required_accuracy.outputs_to_match") or []
    on_model = any(
        (records.get(str(r)) or {}).get("type") == "model"
        for r in (answer.get("route") or {}).get("runs_on") or []
    )
    if outputs and on_model and is_unfilled(answer.get("binding")):
        return [
            finding(
                rules.COMPLETENESS_UNBOUND_OUTPUTS,
                "the question names outputs to match, and the answer on a model cites no binding",
                "binding",
            )
        ]
    return []


#: The types of feature pair that each target status of a factor admits, when the route runs on a
#: model, as the status pairs of the answer specification
#: (docs/specification/answer.md#^status-pairs) state them; an alignment test keeps the two equal.
STATUS_PAIRS: Mapping[str, frozenset[str]] = {
    "denoting": frozenset({"quantity", "component"}),
    "coarse-graining": frozenset({"pattern", "regime"}),
    "limit-construct": frozenset({"invariance-class"}),
    "structural-constraint": frozenset({"invariance-class", "modal-profile"}),
}


def mismatched_status_pairs(
    answer: Mapping[str, Any], records: Mapping[str, Mapping[str, Any]]
) -> list[Finding]:
    """Return every factor whose pair does not carry its target status onto the target.

    When the route runs on a model, the binding carries each factor onto the target through a pair
    of the type that its status requires, and a limit construct cites, as a ground with the role
    `warrant`, the argued pair that places the target in the class of its limit. A route on the
    target needs no pair, since a factor stated over the symbols of the target denotes by
    declaration.

    >>> records = {"mod.a.m": {"type": "model"},
    ...            "bind.a.b": {"feature_pairs": [{"id": "p", "type": "quantity"}]}}
    >>> answer = {"route": {"runs_on": ["mod.a.m"]},
    ...           "aim_block": {"explanation": {"factors": [
    ...               {"id": "f", "target_status": "limit-construct", "pair": "bind.a.b.p"}]}}}
    >>> [f.text for f in mismatched_status_pairs(answer, records)]  # doctest: +NORMALIZE_WHITESPACE
    ['factors.f: the status limit-construct requires a pair of type invariance-class,
      and bind.a.b.p is of type quantity',
     'factors.f: no ground with the role warrant cites the pair bind.a.b.p that places the target
      in the class of the limit']
    """
    on_model = any(
        (records.get(str(r)) or {}).get("type") == "model"
        for r in (answer.get("route") or {}).get("runs_on") or []
    )
    if not on_model:
        return []
    warrants = {
        g.get("record")
        for g in answer.get("grounds") or []
        if isinstance(g, Mapping) and g.get("role") == "warrant"
    }
    found = []
    for index, factor in enumerate(at(answer, "aim_block.explanation.factors") or []):
        if not isinstance(factor, Mapping) or factor.get("target_status") not in STATUS_PAIRS:
            continue
        status, ref = factor["target_status"], factor.get("pair")
        admitted = STATUS_PAIRS[status]
        where = ("aim_block", "explanation", "factors", Entry(index, factor), "pair")
        name = factor.get("id") or index
        if not isinstance(ref, str):
            found.append(
                finding(
                    rules.COMPLETENESS_MISMATCHED_STATUS_PAIR,
                    f"factors.{name}: the status {status} requires a pair of type"
                    f" {' or '.join(sorted(admitted))}, and the factor names none",
                    *where,
                )
            )
            continue
        record, unit = split_reference(ref) or (ref, "")
        pair = next(
            (
                p
                for p in (records.get(record) or {}).get("feature_pairs") or []
                if isinstance(p, Mapping) and p.get("id") == unit
            ),
            None,
        )
        if pair is not None and pair.get("type") not in admitted:
            found.append(
                finding(
                    rules.COMPLETENESS_MISMATCHED_STATUS_PAIR,
                    f"factors.{name}: the status {status} requires a pair of type"
                    f" {' or '.join(sorted(admitted))}, and {ref} is of type {pair.get('type')}",
                    *where,
                )
            )
        if status == "limit-construct" and ref not in warrants:
            found.append(
                finding(
                    rules.COMPLETENESS_MISMATCHED_STATUS_PAIR,
                    f"factors.{name}: no ground with the role warrant cites the pair {ref}"
                    " that places the target in the class of the limit",
                    *where,
                )
            )
    return found


def unrealized_link(question: Mapping[str, Any], answer: Mapping[str, Any]) -> list[Finding]:
    """Return the link a question asks for and the answer does not supply.

    A question may bound the explanans to substrate-specific variables, to substrate-independent
    ones, or to the link between them. The third is not a third kind of variable: it obliges the
    answer to give both descriptions and the mapping that carries one onto the other, since a
    question about how a role is realized is answered by neither description alone. The two
    descriptions are declared in the ordinary blocks; the mapping is what the answer would
    otherwise leave to a reader to reconstruct. Each finding concerns the answer.
    """
    if at(question, "task.admissible_explanans.substrate") != "mapping":
        return []
    realizations = at(answer, "claim.realizations") or []
    if not realizations:
        return [
            finding(
                rules.COMPLETENESS_UNREALIZED_LINK,
                "the question asks for a link, and the answer maps no quantity onto its"
                " realization",
                "claim",
                "realizations",
            )
        ]
    return [
        finding(
            rules.COMPLETENESS_INCOMPLETE_REALIZATION,
            f"claim.realizations[{index}] names what it realizes without saying by what",
            "claim",
            "realizations",
            index,
        )
        for index, entry in enumerate(realizations)
        if isinstance(entry, Mapping) and not (entry.get("realizes") and entry.get("by"))
    ]


def unanchored_explicandum(
    question: Mapping[str, Any], records: Mapping[str, Mapping[str, Any]]
) -> list[Finding]:
    """Return the explicandum of a question of explication that no explicandum of its problem
    anchors.

    The explicandum of such a question is not a slot: it enters through the use that a pointer of
    the problem anchors, so it names a term among the explicanda of the problem that the question
    addresses.

    >>> problem = {"explicanda": [{"term": "disentangled", "pointer": "doi:10.1000/a"}]}
    >>> question = {"addresses": "prob.a.b",
    ...             "task": {"epistemic_aim": "explication", "explicandum": "modular"}}
    >>> [f.text for f in unanchored_explicandum(question, {"prob.a.b": problem})]
    ['task.explicandum: modular is no explicandum of prob.a.b']
    """
    if at(question, "task.epistemic_aim") != "explication":
        return []
    term = at(question, "task.explicandum")
    problem = records.get(str(question.get("addresses"))) or {}
    terms = {str(e.get("term")) for e in problem.get("explicanda") or [] if isinstance(e, Mapping)}
    if is_empty(term) or term in terms:
        return []
    return [
        finding(
            rules.COMPLETENESS_UNANCHORED_EXPLICANDUM,
            f"task.explicandum: {term} is no explicandum of {question.get('addresses')}",
            "task",
            "explicandum",
        )
    ]


def unjustified_explanans_bound(question: Mapping[str, Any]) -> list[Finding]:
    """Return the bound on the explanans that states an axis without saying why.

    A question that leaves the bound empty takes the default: proportionality with the phenomenon
    selects the variables of the explanans, so an empty bound is complete as it stands. A stated
    axis narrows the explanans beyond that default, and only a justification records why the
    research program binds the answer to those variables and what an answer drawing on others
    would lose. A bound that the maturity marks open is still being written, so its justification
    may wait. An empty list of compositional parts states an axis: the system as a whole.
    """
    bound = at(question, "task.admissible_explanans") or {}
    if bound.get("compositional") is None and bound.get("substrate") is None:
        return []
    if bound.get("justification"):
        return []
    if (question.get("maturity") or {}).get("task.admissible_explanans"):
        return []
    return [
        finding(
            rules.COMPLETENESS_UNJUSTIFIED_EXPLANANS_BOUND,
            "task.admissible_explanans states an axis, and no justification says why the answer is"
            " bound to it",
            "task",
            "admissible_explanans",
            "justification",
        )
    ]


def unstated_standing(question: Mapping[str, Any]) -> list[Finding]:
    """Return every virtue the question weighs without saying what failing it costs.

    A virtue bears on an answer in one of two ways, and which one is not derivable from the virtue
    itself: constitutive of the product, so that an answer lacking it is inadmissible however
    accurate, or preferred, so that it ranks answers that are already admissible. No aim decides
    this either, since an inquiry may hold an account to intelligibility whatever product it seeks
    and another may treat the same virtue as a tie-breaker. The question therefore states it, and
    an entry that does not leaves the product test unable to say what it applies.
    """
    return [
        finding(
            rules.COMPLETENESS_UNSTATED_STANDING,
            f"virtues[{index}].standing is unstated for"
            f" {entry.get('virtue') or 'an unnamed virtue'}",
            "virtues",
            index,
            "standing",
        )
        for index, entry in enumerate(question.get("virtues") or [])
        if isinstance(entry, Mapping) and not entry.get("standing")
    ]


def varying_symbols(
    target: Mapping[str, Any], phenomenon: Mapping[str, Any] | None = None
) -> set[str]:
    """Return the symbols that vary along the course of a phenomenon of the target.

    The variables of the target vary, and so does each parameter that the course of the phenomenon
    lists under ``varies``, as the role test of a quantity reads a parameter.

    >>> varying_symbols({"variables": [{"symbol": "x"}], "parameters": [{"symbol": "w"}]},
    ...                 {"course": {"varies": ["w"]}}) == {"x", "w"}
    True
    """
    found = {
        e["symbol"]
        for e in target.get("variables") or []
        if isinstance(e, Mapping) and isinstance(e.get("symbol"), str)
    }
    course = (phenomenon or {}).get("course")
    if isinstance(course, Mapping):
        found |= {s for s in course.get("varies") or [] if isinstance(s, str)}
    return found


def malformed_restrictions(question: Mapping[str, Any], variables: Iterable[str]) -> list[Finding]:
    """Return every domain restriction that does not say what it holds, or holds it wrongly.

    A restriction names one quantity and the set it is held to, or it names none and carries the
    expression it holds under; carrying both says the same thing twice and carrying neither says
    nothing. An entry naming no quantity needs a name, since nothing else identifies it. How a
    quantity is held — clamped, initial, stationary, without an event — applies to something that
    varies, so an entry naming a fixed parameter states no such kind. A parameter that the course
    of the phenomenon lists as varying changes along that course, so it can be held like a variable.

    Parameters
    ----------
    question : mapping
        One filled question record.
    variables : iterable of str
        The symbols that vary along the course of its phenomenon, as :func:`varying_symbols`
        collects them.
    """
    varying = set(variables)
    found = []
    for index, entry in enumerate(at(question, "subject.domain.restrictions") or []):
        if not isinstance(entry, Mapping):
            continue
        where = ("subject", "domain", "restrictions", Entry(index, entry))
        held = entry.get("of")
        symbol = (split_reference(held) or ("", held))[1] if isinstance(held, str) else None
        label = entry.get("name") or held or "an entry"
        carried = [key for key in ("values", "expression") if entry.get(key) is not None]
        if len(carried) != 1:
            found.append(
                finding(
                    rules.COMPLETENESS_RESTRICTION_CONTENT,
                    f"restrictions.{label}: carries {len(carried)} of values and expression",
                    *where,
                )
            )
        if not held and not entry.get("name"):
            found.append(
                finding(
                    rules.COMPLETENESS_ANONYMOUS_RESTRICTION,
                    "restrictions: an entry names neither a quantity nor itself",
                    *where,
                )
            )
        if entry.get("restriction") and symbol not in varying:
            found.append(
                finding(
                    rules.COMPLETENESS_RESTRICTION_WITHOUT_VARIABLE,
                    f"restrictions.{label}: states how it is held although it names no quantity"
                    " that varies",
                    *where,
                    "restriction",
                )
            )
    return found


def undecided_boundaries(record: Mapping[str, Any]) -> list[Finding]:
    """Return every external system whose constraint is neither written nor declared absent.

    An external system either imposes something on the variables it shares, written as
    expressions, or imposes nothing beyond their declared value sets, written as an empty list
    ``[]``. An empty value says neither. A boundary that was never written then reads exactly like
    one that imposes nothing, so the quantities a constraint would have named are never missed: an
    overshoot diagnostic, a measurement coverage. Where a constraint is a genuine scientific
    unknown, the record says so with a ``maturity`` entry rather than by leaving the field empty.
    """
    return [
        finding(
            rules.COMPLETENESS_UNDECIDED_BOUNDARY,
            f"external_systems.{entry.get('symbol')}: constrains is empty, so the boundary is named"
            " without being decided",
            "external_systems",
            Entry(index, entry),
            "constrains",
        )
        for index, entry in enumerate(record.get("external_systems") or [])
        if isinstance(entry, Mapping) and is_empty(entry.get("constrains"))
    ]


def vocabularies(kind: str, source: Path | None = None) -> dict[str, frozenset[str]]:
    """Return, per vocabulary of ``kind`` in the registry, the values it admits, keyed as the
    registry keys it."""
    registry = yaml.safe_load((source or VOCABULARY_REGISTRY).read_text(encoding="utf-8")) or {}
    fields = (registry.get("vocabularies") or {}).get(kind) or {}
    return {name: frozenset(entry["value"] for entry in values) for name, values in fields.items()}


def admitted_values(kind: str, source: Path | None = None) -> dict[str, frozenset[str]]:
    """Return, per closed field of ``kind``, the values it admits, keyed by the path of the field.

    The base schema of the record type binds each closed field to its vocabulary, so the path of
    a field selects its vocabulary, never the name of the vocabulary: in an answer, the field
    ``aim_block.explanation.factors.factor`` takes the kinds of a factor, whereas
    ``aim_block.exploration.space.varied.factor``, which holds a symbol, takes none. A record type
    without a base schema reads each vocabulary of the record level as the field of its name. An
    empty field holds no value, so no vocabulary bears on it.
    """
    values = vocabularies(kind, source)
    if kind in kinds():
        return {
            path: values[key]
            for path, key in vocabulary_paths(load_base(kind)).items()
            if key in values
        }
    return {key[1:]: admitted for key, admitted in values.items() if key.startswith(".")}


def inadmissible_values(
    record: Mapping[str, Any], admitted: Mapping[str, frozenset[str]]
) -> list[Finding]:
    """Return every closed field of the record holding a value its vocabulary does not admit.

    ``admitted`` is keyed by the path of each closed field, an entry of a list adding no segment,
    as :func:`admitted_values` returns it. The message names that path; the finding lies at the
    full path of the field, and at the item of a field holding a list.
    """
    found: list[Finding] = []

    def report(label: str, key: str, value: Any, vocabulary: frozenset[str], where: Place) -> None:
        items = list(enumerate(value)) if isinstance(value, list) else [(None, value)]
        for index, item in items:
            if isinstance(item, str) and item not in vocabulary:
                place = (*where, key) if index is None else (*where, key, index)
                found.append(
                    finding(
                        rules.COMPLETENESS_INADMISSIBLE_VALUE,
                        f"{label}: {item} is not admitted",
                        *place,
                    )
                )

    def visit(node: Any, path: tuple[str, ...], where: Place) -> None:
        if isinstance(node, Mapping):
            for key, value in node.items():
                field_path = ".".join((*path, str(key)))
                vocabulary = admitted.get(field_path)
                if vocabulary is not None:
                    report(field_path, str(key), value, vocabulary, where)
                if isinstance(value, (Mapping, list)):
                    visit(value, (*path, str(key)), (*where, key))
        elif isinstance(node, list):
            for index, item in enumerate(node):
                visit(item, path, (*where, Entry(index, item)))

    visit(record, (), ())
    return found
