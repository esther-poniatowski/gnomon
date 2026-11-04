"""
The checks of the records of a subject: the occurrence class of a phenomenon, and the boundaries
that a target system draws with its external systems.
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
