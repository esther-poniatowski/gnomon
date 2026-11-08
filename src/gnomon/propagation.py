"""
Propagation of a revision to the records that rest on the revised record.

A step of an itinerary that revises a record states the kind of the revision, and each relation
that connects the revised record to another carries a warrant class, which decides whether that
kind flags the other record, as the transmission of a revision states. The relations are read by
:mod:`gnomon.relations`. The tool reports the flagged dependents, each with the relation and the
class that flag it, and never edits them; the researcher records the review of each one in the
step, as the decision on revision accountability requires.

Functions
---------
revisions
    Return each revision of the itineraries, with its flagged dependents and those still to review.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Mapping

from .relations import flagged_dependents, owner

Records = Mapping[str, Mapping[str, Any]]


@dataclass(frozen=True)
class Revision:
    """One revision recorded by a step, with the dependents that it flags and why."""

    step: str
    record: str
    kind: str
    flagged: tuple[str, ...]
    to_review: tuple[str, ...]
    reasons: Mapping[str, str] = field(default_factory=dict)


def revisions(records: Records, itineraries: Records | None = None) -> list[Revision]:
    """Return each revision of the itineraries, with its flagged dependents and those still to
    review.

    ``itineraries`` holds the records whose itineraries are read, such as the records of one
    problem, and defaults to ``records``; the dependents are sought in ``records``.
    """
    found = []
    source = records if itineraries is None else itineraries
    for itinerary in (r for _, r in sorted(source.items()) if r.get("type") == "itinerary"):
        for step in itinerary.get("steps") or []:
            revises = step.get("revises") if isinstance(step, Mapping) else None
            if (
                not isinstance(revises, Mapping)
                or owner(str(revises.get("record")), records) is None
            ):
                continue
            kind = str(revises.get("kind"))
            reasons = flagged_dependents(revises["record"], kind, records)
            flagged = tuple(sorted(reasons))
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
                    reasons,
                )
            )
    return found
