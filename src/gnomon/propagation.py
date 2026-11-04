"""
Propagation of a revision to the records that rest on the revised record.

A step of an itinerary that revises a record states the kind of the revision, and the theory of
grounds and dependence fixes which dependents a revision flags: a dependent that rests on the
revised record monotonically, by a deductive support, is flagged only by a retraction, a correction
or a taxonomic restructure, and a dependent that rests on it defeasibly is flagged by every kind.
The tool reports the flagged dependents and never edits them; the researcher records the review of
each one in the step, as the decision on revision accountability requires.

Functions
---------
dependents
    Return the records that reference a record, by identifier.
rests_monotonically
    Return whether a dependent rests on the records that it cites by a deductive support.
revisions
    Return each revision of the itineraries, with its flagged dependents and those still to review.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Mapping

from .vocabulary import references

#: The kinds of revision that flag a dependent resting monotonically on the revised record.
MONOTONIC_KINDS = frozenset({"retraction", "correction", "taxonomic-restructure"})

#: The errors of an operation of a derived model that keep the model a deductive consequence of its parent.
EXACT = frozenset({"exact"})

Records = Mapping[str, Mapping[str, Any]]


@dataclass(frozen=True)
class Revision:
    """One revision recorded by a step, with the dependents that it flags."""

    step: str
    record: str
    kind: str
    flagged: tuple[str, ...]
    to_review: tuple[str, ...]


def dependents(revised: str, records: Records) -> list[str]:
    """Return the records that reference ``revised``, or a unit of it, by identifier.

    >>> dependents("mod.a.m", {"ans.a.b": {"route": {"runs_on": ["mod.a.m"]}}, "ans.a.c": {}})
    ['ans.a.b']
    """
    found = []
    for ident, record in sorted(records.items()):
        if ident == revised or record.get("type") == "itinerary":
            continue
        if any(text == revised or text.startswith(revised + ".") for _, text in references(record)):
            found.append(ident)
    return found


def rests_monotonically(record: Mapping[str, Any]) -> bool:
    """Return whether a dependent rests on the records that it cites by a deductive support.

    An answer formally proven and a model derived by exact operations alone follow deductively from
    what they cite; every other dependent rests on it defeasibly.

    >>> rests_monotonically({"type": "answer", "support": "formally-proven"})
    True
    >>> rests_monotonically({"type": "model", "derives_from": ["mod.a"], "operations": [{"error": "uncontrolled"}]})
    False
    """
    if record.get("type") == "answer":
        return record.get("support") == "formally-proven"
    if record.get("type") == "model" and record.get("derives_from"):
        operations = [op for op in record.get("operations") or [] if isinstance(op, Mapping)]
        return bool(operations) and all(op.get("error") in EXACT for op in operations)
    return False


def revisions(records: Records, itineraries: Records | None = None) -> list[Revision]:
    """Return each revision of the itineraries, with its flagged dependents and those still to review.

    ``itineraries`` holds the records whose itineraries are read, such as the records of one
    problem, and defaults to ``records``; the dependents are sought in ``records``.
    """
    found = []
    source = records if itineraries is None else itineraries
    for itinerary in (r for _, r in sorted(source.items()) if r.get("type") == "itinerary"):
        for step in itinerary.get("steps") or []:
            revises = step.get("revises") if isinstance(step, Mapping) else None
            if not isinstance(revises, Mapping) or revises.get("record") not in records:
                continue
            kind = str(revises.get("kind"))
            flagged = tuple(
                d
                for d in dependents(revises["record"], records)
                if kind in MONOTONIC_KINDS or not rests_monotonically(records[d])
            )
            reviewed = {
                str(r.get("dependent"))
                for r in revises.get("reviews") or []
                if isinstance(r, Mapping) and r.get("state") not in (None, "pending")
            }
            found.append(
                Revision(
                    f"{itinerary.get('id')}.{step.get('id')}",
                    revises["record"],
                    kind,
                    flagged,
                    tuple(d for d in flagged if d not in reviewed),
                )
            )
    return found
