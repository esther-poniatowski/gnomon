"""
The keys of the block ``maturity``, checked against the fields that the schema of their record
declares.

A key is the path of a field, its segments joined by dots from the root of the record. A segment
names a field of a mapping. Inside a list, a segment names one entry by its ``symbol`` or its
``id``, or else a field of the entries, which then marks that field in every entry. A field is
resolved against the base schema, so a field marked ``open`` in a list that holds no entry yet is
still named; an entry is resolved against the record, since only the record holds its entries.

Functions
---------
names_field
    Return whether a path names a field that a schema declares, through the values of a record.
misplaced_maturity
    Return each key of the block ``maturity`` of a record that names no field of it.
"""

from __future__ import annotations

from typing import Any, Mapping, Sequence

from .. import findings as rules
from ..findings import Finding, Key, finding
from ..schemas import load_base, record_kinds


def _step(schema: Mapping[str, Any], mappings: list[Mapping[str, Any]], head: str) -> Any:
    """Return the schema of the field ``head`` of a mapping, or None when it declares none; an
    open mapping declares a key that one of its values holds."""
    declared = (schema.get("properties") or {}).get(head)
    if declared is not None:
        return declared
    extra = schema.get("additionalProperties")
    return extra if isinstance(extra, Mapping) and any(head in m for m in mappings) else None


def names_field(schema: Mapping[str, Any], nodes: Sequence[Any], segments: Sequence[str]) -> bool:
    """Return whether ``segments`` name a field that ``schema`` declares, read through ``nodes``,
    the values of the record at the place of the schema.

    >>> schema = {"properties": {"observables": {"items": {"properties": {
    ...     "symbol": {}, "values": {}}}}}}
    >>> record = {"observables": [{"symbol": "Z", "values": None}]}
    >>> [names_field(schema, [record], path.split(".")) for path in
    ...  ("observables.values", "observables.Z.values", "observables.W.values", "observables.form")]
    [True, True, False, False]
    """
    if not segments:
        return True
    head, rest = segments[0], segments[1:]
    items = schema.get("items")
    if isinstance(items, Mapping):
        entries = [e for n in nodes if isinstance(n, list) for e in n if isinstance(e, Mapping)]
        chosen = [e for e in entries if head in (e.get("symbol"), e.get("id"))]
        if chosen:
            return names_field(items, chosen, rest)
        schema, nodes = items, entries
    mappings = [n for n in nodes if isinstance(n, Mapping)]
    declared = _step(schema, mappings, head)
    if not isinstance(declared, Mapping):
        return False
    return names_field(declared, [m.get(head) for m in mappings], rest)


def misplaced_maturity(record: Mapping[str, Any]) -> list[Finding]:
    """Return each key of the block ``maturity`` of a record that names no field of it.

    >>> question = {"type": "question", "task": {"proof_obligations": [
    ...     {"id": "necessity", "consequent": None}]},
    ...     "maturity": {"task.proof_obligations.necessity.consequent": "open",
    ...                  "task.proof_obligations.sufficiency.consequent": "open"}}
    >>> [f.text for f in misplaced_maturity(question)]
    ['maturity.task.proof_obligations.sufficiency.consequent: names no field of the record']
    """
    marked = record.get("maturity")
    kind = record_kinds().get(str(record.get("type")))
    if not isinstance(marked, Mapping) or kind is None:
        return []
    base = load_base(kind)
    return [
        finding(
            rules.COMPLETENESS_MISPLACED_MATURITY,
            f"maturity.{key}: names no field of the record",
            "maturity",
            Key(str(key)),
        )
        for key in marked
        if not names_field(base, [record], str(key).split("."))
    ]
