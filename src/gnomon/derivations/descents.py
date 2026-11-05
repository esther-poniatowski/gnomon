"""
The descent of the laws stated by derivations, across the records of a workspace.

A law marked ``derived`` descends from the premises of the derivation that states it as a
consequence, or from the derivation published at its origin. A consequence of the root sought of a
derivation that serves a law or an operation is stated by that record.

Functions
---------
consequence_records
    Return the record stating each consequence, read from the record served when it names none.
recorded_descents
    Return, for each record that a consequence names, the derivation and the consequence.
unrecorded_descents
    Return the laws marked derived whose descent is recorded nowhere.
underived_records
    Return the consequences whose record names a law not marked derived.
"""

from __future__ import annotations

from typing import Any, Iterable, Mapping

from .. import findings as rules
from ..findings import Entry, Finding, finding
from ..identifiers import split_reference
from .graph import Derivation, entries, root_sought, served_unit


def consequence_records(record: Derivation) -> dict[str, str]:
    """Return the record stating each consequence of a derivation that states one: the record that
    the consequence names, or the record served for a consequence of the root sought.

    >>> derivation = {"serves": "bg.a.b.law",
    ...               "consequences": [{"id": "c", "answers": "bg.a.b.law"}]}
    >>> consequence_records(derivation)
    {'c': 'bg.a.b.law'}
    """
    served = served_unit(record)
    root = root_sought(record)
    found = {}
    for _, c in entries(record, "consequences"):
        stated = c.get("record") or (served if served and c.get("answers") == root else None)
        if c.get("id") and stated:
            found[str(c["id"])] = str(stated)
    return found


def recorded_descents(records: Iterable[Mapping[str, Any]]) -> dict[str, tuple[str, str]]:
    """Return, for each record that a consequence of a derivation states, that derivation and the
    consequence.

    >>> recorded_descents([{"type": "derivation", "id": "derivation.a.b",
    ...                     "consequences": [{"id": "c", "record": "mod.a.m.law"}]}])
    {'mod.a.m.law': ('derivation.a.b', 'c')}
    """
    return {
        stated: (str(record.get("id")), consequence)
        for record in records
        if record.get("type") == "derivation"
        for consequence, stated in consequence_records(record).items()
    }


def unrecorded_descents(record: Mapping[str, Any], descents: Mapping[str, Any]) -> list[Finding]:
    """Return the laws marked ``derived`` whose descent is recorded nowhere: no derivation states
    the law as a consequence, and the law names no published origin holding its derivation.

    >>> law = {"symbol": "bound", "warrant": "derived"}
    >>> [f.text for f in unrecorded_descents({"id": "bg.a.b", "laws": [law]}, {})]
    ['laws.bound: the law is marked derived, and no derivation or origin records its descent']
    >>> unrecorded_descents({"id": "bg.a.b", "laws": [law]}, {"bg.a.b.bound": ("d", "c")})
    []
    """
    found = []
    for i, law in entries(record, "laws"):
        if law.get("warrant") != "derived" or law.get("origin"):
            continue
        if f"{record.get('id')}.{law.get('symbol')}" in descents:
            continue
        found.append(
            finding(
                rules.DERIVATION_UNRECORDED_DESCENT,
                f"laws.{law.get('symbol') or i}: the law is marked derived, and no derivation or"
                " origin records its descent",
                "laws",
                Entry(i, law),
                "warrant",
            )
        )
    return found


def underived_records(
    record: Derivation, records: Mapping[str, Mapping[str, Any]]
) -> list[Finding]:
    """Return the consequences whose record names a law that is not marked derived, since a law
    established by a derivation descends from its premises.

    >>> records = {"mod.a.b": {"id": "mod.a.b", "laws": [{"symbol": "flow", "warrant": "posited"}]}}
    >>> derivation = {"consequences": [{"id": "c", "record": "mod.a.b.flow"}]}
    >>> [f.text for f in underived_records(derivation, records)]
    ['consequences.c.record: mod.a.b.flow is a law marked posited, not derived']
    """
    found = []
    stated = consequence_records(record)
    for i, c in entries(record, "consequences"):
        target = stated.get(str(c.get("id")))
        split = split_reference(target) if target else None
        if split is None:
            continue
        law = next(
            (
                entry
                for _, entry in entries(records.get(split[0]) or {}, "laws")
                if entry.get("symbol") == split[1]
            ),
            None,
        )
        if law is not None and law.get("warrant") != "derived":
            found.append(
                finding(
                    rules.DERIVATION_UNDERIVED_RECORD,
                    f"consequences.{c.get('id') or i}.record: {target} is a law marked"
                    f" {law.get('warrant') or 'without warrant'}, not derived",
                    "consequences",
                    Entry(i, c),
                    "record",
                    value=str(target),
                )
            )
    return found
