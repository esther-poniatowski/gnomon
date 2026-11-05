"""
The structure of a derivation record: its units, its root sought, and the dependence of its objects
through its producers, the moves and the segments.

A derivation names its own units by bare identifiers and the premises held by other records by
dotted references. The fields that name a unit of the record declare the lists that they admit in
the schema of the record, under the key ``x-units``, so that no list of fields is kept apart from
the schema. A producer yields its outputs once all of its inputs are available, so a segment bridges
the routine moves that the record omits.

Functions
---------
load_registry
    Return the registry of the rules of a derivation.
internal_fields
    Return the fields of the derivation schema that name units of the record.
units
    Return the identifiers declared by each list of a derivation.
root_sought
    Return the identifier of the root sought: the record served, or the declared sought.
upstream
    Return the producers and the inputs on which a set of objects of a derivation rests.
downstream
    Return the objects that depend on a move or a segment.
"""

from __future__ import annotations

from functools import cache
from pathlib import Path
from typing import Any, Iterable, Mapping

import yaml

from ..identifiers import split_reference

#: The registry of the rules of a derivation.
REGISTRY = Path(__file__).parent.parent / "data" / "registries" / "derivations.yml"

#: The schema of the derivation record, whose fields declare the units that they name.
SCHEMA = Path(__file__).parent.parent / "data" / "schemas" / "derivation.base.schema.yml"

#: The lists of a derivation whose entries are units named by the key ``id``.
UNIT_LISTS: tuple[str, ...] = (
    "subordinate",
    "objects",
    "posits",
    "moves",
    "orientations",
    "interpretations",
    "features",
    "segments",
    "consequences",
)

#: The ground class of a unit of another record, named by a dotted reference.
REFERENCE = "reference"

Derivation = Mapping[str, Any]
Producers = dict[str, tuple[set[str], set[str]]]
Field = tuple[tuple[str, ...], tuple[str, ...], str]


@cache
def load_registry(source: Path | None = None) -> dict[str, Any]:
    """Return the registry of the rules of a derivation, read once."""
    loaded: dict[str, Any] = yaml.safe_load((source or REGISTRY).read_text(encoding="utf-8")) or {}
    return loaded


@cache
def internal_fields(source: Path | None = None) -> tuple[Field, ...]:
    """Return each field of the derivation schema that names units of the record: its path, the
    lists that it admits, and the placeholder that its template writes.

    >>> ("moves", "warrant", "applies_because") in {path for path, _, _ in internal_fields()}
    True
    """
    schema = yaml.safe_load((source or SCHEMA).read_text(encoding="utf-8"))
    found: list[Field] = []

    def walk(node: Mapping[str, Any], path: tuple[str, ...]) -> None:
        for key, sub in (node.get("properties") or {}).items():
            if not isinstance(sub, Mapping):
                continue
            here = (*path, str(key))
            if sub.get("x-units"):
                template = sub.get("x-template") or mapping(sub.get("items")).get("x-template")
                found.append(
                    (here, tuple(str(u) for u in sub["x-units"]), str(template or "").strip('"'))
                )
            walk(sub, here)
            if isinstance(sub.get("items"), Mapping):
                walk(sub["items"], here)

    walk(schema, ())
    return tuple(found)


def entries(record: Mapping[str, Any], name: str) -> list[tuple[int, Mapping[str, Any]]]:
    """Return the entries of a list of the record that are mappings, with their indices."""
    found = record.get(name)
    if not isinstance(found, list):
        return []
    return [(i, item) for i, item in enumerate(found) if isinstance(item, Mapping)]


def by_id(record: Mapping[str, Any], name: str) -> dict[str, Mapping[str, Any]]:
    """Return the entries of a list of the record, keyed by their identifier."""
    return {str(e["id"]): e for _, e in entries(record, name) if e.get("id")}


def mapping(value: Any) -> Mapping[str, Any]:
    """Return ``value`` when it is a mapping, and an empty mapping otherwise."""
    return value if isinstance(value, Mapping) else {}


def names(value: Any) -> list[str]:
    """Return the identifiers that a field holds: one for a string, one per entry for a list."""
    values = value if isinstance(value, list) else [value]
    return [str(v) for v in values if isinstance(v, str) and v.strip()]


def root_sought(record: Derivation) -> str | None:
    """Return the identifier of the root sought: the record served, from which the root sought is
    read, or the declared sought of a derivation that serves no record.

    >>> root_sought({"sought": {"id": "s"}}), root_sought({"serves": "bg.a.b.law"})
    ('s', 'bg.a.b.law')
    """
    served = record.get("serves")
    if isinstance(served, str) and served.strip():
        return served
    root = record.get("sought")
    return str(root["id"]) if isinstance(root, Mapping) and root.get("id") else None


def units(record: Derivation) -> dict[str, set[str]]:
    """Return the identifiers declared by each list of a derivation, with ``sought`` for the root
    and ``slots`` for the symbols of its slots.

    >>> sorted(units({"sought": {"id": "s"}, "moves": [{"id": "m"}]})["moves"])
    ['m']
    >>> units({"serves": "bg.a.b.law"})["sought"]
    {'bg.a.b.law'}
    """
    declared = {name: set(by_id(record, name)) for name in UNIT_LISTS}
    root = root_sought(record)
    declared["sought"] = {root} if root else set()
    declared["slots"] = {
        str(item.get("symbol")) for _, item in entries(record, "slots") if item.get("symbol")
    }
    return declared


def kind_of(record: Derivation) -> dict[str, str]:
    """Return the list that declares each identifier of a unit of the record."""
    return {ident: name for name, idents in units(record).items() for ident in idents}


def producers_of(record: Derivation) -> Producers:
    """Return the inputs and the outputs of each move and of each segment."""
    return {
        ident: (set(names(entry.get("inputs"))), set(names(entry.get("outputs"))))
        for name in ("moves", "segments")
        for ident, entry in by_id(record, name).items()
    }


def held_moves(record: Derivation) -> dict[str, set[str]]:
    """Return the moves that each segment holds."""
    return {ident: set(names(s.get("moves"))) for ident, s in by_id(record, "segments").items()}


def upstream(record: Derivation, targets: Iterable[str]) -> tuple[set[str], set[str]]:
    """Return the producers (moves and segments) on which a set of objects of a derivation rests,
    and every input that they take, the objects of the record and the dotted premises alike.

    A producer is upstream when it yields an object already needed; its inputs are then needed in
    turn. A segment upstream brings the moves that it holds, since it bridges them.

    >>> derivation = {"moves": [{"id": "a", "inputs": ["p"], "outputs": ["x"]},
    ...                         {"id": "b", "inputs": ["x", "bg.a.b.law"], "outputs": ["y"]},
    ...                         {"id": "c", "inputs": ["q"], "outputs": ["z"]}]}
    >>> producers, needed = upstream(derivation, ["y"])
    >>> sorted(producers), sorted(needed)
    (['a', 'b'], ['bg.a.b.law', 'p', 'x', 'y'])
    """
    producers, held = producers_of(record), held_moves(record)
    needed, used = set(targets), set()
    changed = True
    while changed:
        changed = False
        for ident, (ins, outs) in producers.items():
            if ident not in used and outs & needed:
                used.add(ident)
                needed |= ins
                changed = True
        for segment in list(used):
            for move in held.get(segment, set()) - used:
                if move in producers:
                    used.add(move)
                    needed |= producers[move][0]
                    changed = True
    return used, needed


def enclosing(record: Derivation, unit: str) -> set[str]:
    """Return the segments that hold a move or enclose a segment, with every segment that encloses
    them in turn."""
    within = {ident: s.get("within") for ident, s in by_id(record, "segments").items()}
    found = {ident for ident, moves in held_moves(record).items() if unit in moves}
    if within.get(unit):
        found.add(str(within[unit]))
    frontier = set(found)
    while frontier:
        parents = {str(within[s]) for s in frontier if within.get(s)} - found
        found |= parents
        frontier = parents
    return found


def downstream(record: Derivation, unit: str) -> set[str]:
    """Return the objects that a move or a segment yields, with the outputs of the segments that
    enclose it, and every object that depends on them through the producers of the record."""
    producers = producers_of(record)
    starts = {unit} | enclosing(record, unit)
    reached: set[str] = set().union(*(producers.get(s, (set(), set()))[1] for s in starts))
    changed = True
    while changed:
        changed = False
        for name, (ins, outs) in producers.items():
            if name not in starts and ins & reached and not outs <= reached:
                reached |= outs
                changed = True
    return reached


def concerned(record: Derivation, ident: str) -> set[str]:
    """Return the objects that a unit concerns: an object itself, the outputs of a move or of a
    segment, the object of a feature, or the object that states a consequence."""
    if ident in by_id(record, "objects"):
        return {ident}
    for name in ("moves", "segments"):
        if ident in by_id(record, name):
            return set(names(by_id(record, name)[ident].get("outputs")))
    if ident in by_id(record, "features"):
        return set(names(by_id(record, "features")[ident].get("at")))
    if ident in by_id(record, "consequences"):
        return set(names(by_id(record, "consequences")[ident].get("from")))
    return set()


def reachable(producers: Producers, start: set[str]) -> set[str]:
    """Return what the premises ``start`` make available, a producer firing once all of its inputs
    are available."""
    reached = set(start)
    changed = True
    while changed:
        changed = False
        for ins, outs in producers.values():
            if ins <= reached and not outs <= reached:
                reached |= outs
                changed = True
    return reached


def served_unit(record: Derivation) -> str | None:
    """Return the record served when it names a unit of a record, a law or an operation stated in
    advance, which then states the consequence of the root sought."""
    served = record.get("serves")
    return served if isinstance(served, str) and split_reference(served) else None
