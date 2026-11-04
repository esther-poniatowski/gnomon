"""
The resolution of the identifiers of a record against the symbols and the operators that the
record can see.
"""

from __future__ import annotations

from typing import Any, Iterable, Mapping

from .. import findings as rules
from ..findings import Entry, Finding, Place, finding
from ..identifiers import split_reference
from .declarations import declarations
from .layout import (
    NESTED_REFERENCE,
    PATH_REFERENCE,
    REFERENCE,
    TOLERANCE_NAMES,
    TYPE_PATH_REFERENCE,
    at_item,
    bound,
    entries,
    formulas,
    identifiers,
    indexed,
    items_of,
    reach,
)
from .operators import local_operators


def retired_in_use(record: Mapping[str, Any]) -> list[Finding]:
    """Return every expression of a derived model that uses a symbol which an operation retires.

    >>> model = {"type": "model", "operations": [{"id": "drop", "retires": ["system.a.W"]}],
    ...          "laws": [{"symbol": "law", "expression": "W + u = 0"}]}
    >>> [f.text for f in retired_in_use(model)]
    ['laws.expression uses W, which the operation drop retires']
    """
    retired: dict[str, str] = {}
    for entry in entries(record, "operations"):
        for name in entry.get("retires") or []:
            named = split_reference(name) if isinstance(name, str) else None
            retired[named[1] if named else str(name)] = str(entry.get("id"))
    return (
        [
            finding(
                rules.VOCABULARY_RETIRED_SYMBOL,
                f"{where} uses {name}, which the operation {retired[name]} retires",
                *place,
                value=name,
            )
            for where, place, text, _ in formulas(record)
            for name in sorted(identifiers(text) & set(retired))
        ]
        if retired
        else []
    )


def _cited(record: Mapping[str, Any]) -> list[tuple[str, Place, Any]]:
    """Return each field of a record that holds references, with its path and its field path."""
    cited: list[tuple[str, Place, Any]] = [
        (f"{block}.{key}", (block, Entry(i, entry), key), entry.get(key))
        for block, key in REFERENCE
        for i, entry in indexed(record, block)
    ]
    cited += [
        (
            f"{outer}.{inner}.{key}",
            (outer, Entry(i, entry), inner, Entry(j, nested), key),
            nested.get(key),
        )
        for outer, inner, key in NESTED_REFERENCE
        for i, entry in indexed(record, outer)
        for j, nested in indexed(entry, inner)
    ]
    return cited


def _unresolved_references(record: Mapping[str, Any], known: set[str]) -> list[Finding]:
    """Return each reference of a record, in a field or at a path, that names no known symbol."""
    problems = [
        finding(rules.VOCABULARY_UNRESOLVED, f"{where} -> {name}", *at_item(place, index))
        for where, place, value in _cited(record)
        for index, name in items_of(value)
        if isinstance(name, str) and split_reference(name) is None and name not in known
    ]
    for path in (*PATH_REFERENCE, *TYPE_PATH_REFERENCE.get(str(record.get("type", "")), ())):
        problems += [
            finding(rules.VOCABULARY_UNRESOLVED, f"{path} -> {name}", *at)
            for at, name in reach(record, path)
            if name.strip() and split_reference(name) is None and name not in known
        ]
    return problems


def _unresolved_identifiers(
    record: Mapping[str, Any], known: set[str], available: frozenset[str]
) -> list[Finding]:
    """Return each identifier of a formula that names no symbol, bound variable or operator."""
    problems: list[Finding] = []
    for where, place, text, variables in formulas(record):
        reachable = known | bound(text) | available | variables
        if where.startswith("task.required_accuracy.outputs_to_match[].tolerance"):
            reachable |= TOLERANCE_NAMES
        problems += [
            finding(rules.VOCABULARY_UNRESOLVED, f"{where} -> {name}", *place, value=name)
            for name in sorted(identifiers(text))
            if name not in reachable
        ]
    return problems


def unresolved(
    record: Mapping[str, Any],
    operators: Iterable[str],
    external: Iterable[str] = (),
) -> list[Finding]:
    """Return every reference and formula identifier of the record that resolves to nothing.

    A reference lies at its field, or at its item in a list; a formula identifier lies at its
    expression, with the identifier as discriminator.

    Parameters
    ----------
    record : mapping
        One filled inquiry record.
    operators : iterable of str
        The operators available to this record: the canonical set and its own declarations.
    external : iterable of str
        Symbols declared by a record this one references, such as the target system of a
        phenomenon.
    """
    known = (
        {entry.symbol for entry in declarations(record)}
        | set(external)
        | set(local_operators(record))
    )
    return _unresolved_references(record, known) + _unresolved_identifiers(
        record, known, frozenset(operators)
    )


def misattributed_appeals(record: Mapping[str, Any], systems: Iterable[str]) -> list[Finding]:
    """Return every factor of an explanation appealing to something that is not an external system.

    An answer may explain the phenomenon by the environment rather than by the target alone: by
    the structure of the inputs, or by the class of system that reads the outputs. Naming that
    environment is what makes the appeal checkable, so it resolves to an external system the
    target declares. A quantity that system owns is reached as a term, under its own symbol.
    """
    declared = set(systems)
    explanation = (record.get("aim_block") or {}).get("explanation") or {}
    return [
        finding(
            rules.VOCABULARY_MISATTRIBUTED_APPEAL,
            f"aim_block.explanation.factors.appeals_to: {name} is no external system of the target",
            "aim_block",
            "explanation",
            "factors",
            Entry(position, entry),
            "appeals_to",
            index,
        )
        for position, entry in indexed(explanation, "factors")
        for index, name in enumerate(entry.get("appeals_to") or [])
        if isinstance(name, str) and name not in declared
    ]
