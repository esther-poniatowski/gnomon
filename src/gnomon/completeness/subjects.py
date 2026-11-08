"""
The checks of the records of a subject: the occurrence class and the evidential status of a
phenomenon, and the boundaries that a target system draws with its external systems.
"""

from __future__ import annotations

from pathlib import Path
from typing import Any, Mapping

from .. import findings as rules
from ..findings import Entry, Finding, finding
from .paths import is_empty
from .requirements import read_requirements


def occurrence_by_category(source: Path | None = None) -> dict[str, list[str]]:
    """Return, per phenomenon category, the occurrence classes that the category admits."""
    table = read_requirements(source).get("occurrence_by_category") or {}
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


def target_types_by_evidential_status(source: Path | None = None) -> dict[str, list[str]]:
    """Return, per evidential status obtained by derivation, the target types that admit it."""
    table = read_requirements(source).get("target_types_by_evidential_status") or {}
    return {str(status): list(types or []) for status, types in table.items()}


#: The repair named by a mismatched evidential status: the status that the target type admits.
EVIDENCE_REPAIR: dict[str, str] = {
    "derived": "a behavior derived for a target with actual members is predicted",
    "predicted": "a behavior derived for a target without actual members is derived",
}


def mismatched_evidence(
    phenomenon: Mapping[str, Any],
    target: Mapping[str, Any],
    table: Mapping[str, list[str]],
) -> list[Finding]:
    """Return the evidential status that the type of the target system does not admit.

    A behavior obtained by derivation is `derived` when it is asserted of a model or of a target
    without actual members, since the derivation establishes it, and `predicted` when it is
    asserted of a target with actual members, since it awaits detection. An empty field, or a
    target that states no type, leaves the pair unfilled, and nothing is reported.

    >>> table = {"derived": ["no-external-target"], "predicted": ["particular"]}
    >>> found = mismatched_evidence({"evidential_status": "derived"},
    ...                             {"id": "system.flow", "target_type": "particular"}, table)
    >>> for part in found[0].text.split("; "):
    ...     print(part)
    evidential_status: derived, whereas system.flow is of type particular
    a behavior derived for a target with actual members is predicted
    """
    status, kind = phenomenon.get("evidential_status"), target.get("target_type")
    if not isinstance(status, str) or not isinstance(kind, str) or is_empty(kind):
        return []
    if status not in table or kind in table[status]:
        return []
    return [
        finding(
            rules.COMPLETENESS_MISMATCHED_EVIDENCE,
            f"evidential_status: {status}, whereas {target.get('id')} is of type {kind};"
            f" {EVIDENCE_REPAIR.get(status, 'the target type does not admit the status')}",
            "evidential_status",
            value=status,
        )
    ]


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


def unbounded_censoring(phenomenon: Mapping[str, Any]) -> list[Finding]:
    """Return each observable whose event time is censored on the left without a stated bound.

    A left-censored time is known only to precede the first observation. The event states that
    time in ``first_observation``, or leaves it empty when observation starts at the origin, which
    then bounds the time.

    >>> event = {"censoring": "left", "origin": None}
    >>> [f.rule.id for f in unbounded_censoring({"observables": [{"symbol": "T", "event": event}]})]
    ['completeness/unbounded-censoring']
    >>> bounded = {**event, "origin": "t = 0"}
    >>> unbounded_censoring({"observables": [{"symbol": "T", "event": bounded}]})
    []
    """
    found: list[Finding] = []
    for index, entry in enumerate(phenomenon.get("observables") or []):
        if not isinstance(entry, Mapping) or not isinstance(entry.get("event"), Mapping):
            continue
        event = entry["event"]
        if event.get("censoring") != "left":
            continue
        if is_empty(event.get("first_observation")) and is_empty(event.get("origin")):
            found.append(
                finding(
                    rules.COMPLETENESS_UNBOUNDED_CENSORING,
                    f"observables.{entry.get('symbol') or index}: the event time is censored on the"
                    " left, and neither a first observation nor an origin bounds it",
                    "observables",
                    Entry(index, entry),
                    "event",
                )
            )
    return found
