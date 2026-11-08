"""
The checks of the declarations of a record that read no other record.
"""

from __future__ import annotations

from typing import Any, Mapping

from .. import findings as rules
from ..findings import Entry, Finding, finding
from .layout import DECLARING, FORMULA, REFERENCE, entries, indexed


def mistyped_symbols(record: Mapping[str, Any]) -> list[Finding]:
    """Return every ``symbol`` entry that YAML did not resolve to a string.

    YAML 1.1 reads ``on``, ``off``, ``yes``, ``no``, ``y``, ``n``, ``true`` and ``false`` as
    booleans, and ``null`` and ``~`` as nothing, so an unquoted symbol drawn from that set
    silently becomes a value of another type. Reporting it prevents a declaration from
    disappearing without a diagnostic.
    """
    blocks = (*DECLARING.get(str(record.get("type", "")), ()), "operators")
    found = []
    for block in blocks:
        for index, entry in indexed(record, block):
            if "symbol" in entry and not isinstance(entry["symbol"], str):
                found.append(
                    finding(
                        rules.VOCABULARY_MISTYPED_SYMBOL,
                        f"{block}: {entry['symbol']!r} is {type(entry['symbol']).__name__}, not a"
                        " symbol",
                        block,
                        Entry(index, entry),
                        "symbol",
                    )
                )
    return found


def split_expressions(record: Mapping[str, Any]) -> list[Finding]:
    """Return every expression a serializer split into fragments.

    An unquoted expression inside a bracketed list splits on its commas, so the record holds
    plausible fragments rather than one value. A fragment is reported by its unbalanced
    parentheses.
    """
    found = []
    for block, key in (*FORMULA, *REFERENCE):
        for position, entry in indexed(record, block):
            value = entry.get(key)
            for index, item in enumerate(value) if isinstance(value, list) else []:
                if isinstance(item, str) and item.count("(") != item.count(")"):
                    found.append(
                        finding(
                            rules.VOCABULARY_SPLIT_EXPRESSION,
                            f"{block}.{key}: {item!r} is a fragment of a split expression",
                            block,
                            Entry(position, entry),
                            key,
                            index,
                        )
                    )
    return found


def corrupted_notation(record: Mapping[str, Any]) -> list[Finding]:
    """Return every notation a serializer damaged by reading a backslash as an escape.

    A double-quoted YAML scalar processes ``\\n``, ``\\t`` and their kin, so a LaTeX form such as
    ``\\nu`` arrives as a newline followed by a letter. A control character in a notation is the
    trace of that reading.
    """
    found = []
    for block in (
        "constituents",
        "index_sets",
        "variables",
        "parameters",
        "observables",
        "operators",
        "terms",
    ):
        for index, entry in indexed(record, block):
            form = entry.get("notation")
            if isinstance(form, str) and any(c in form for c in "\n\t\r\x0b\x0c\x08\x07"):
                found.append(
                    finding(
                        rules.VOCABULARY_CORRUPTED_NOTATION,
                        f"{block}.{entry.get('symbol')}: the notation holds a control character",
                        block,
                        Entry(index, entry),
                        "notation",
                    )
                )
    return found


def misplaced_sharing(record: Mapping[str, Any]) -> list[Finding]:
    """Return every shared variable that names something other than a quantity.

    A variable crosses the boundary of the system, so it is one the record declares as a state
    variable, an exogenous variable or a parameter. A constituent kind and an index set are sets,
    and a set does not cross a boundary. The direction of the exchange is read from the declaring
    block rather than declared again.
    """
    quantities = {
        e["symbol"]
        for block in ("variables", "parameters")
        for e in entries(record, block)
        if isinstance(e.get("symbol"), str)
    }
    found = []
    for position, entry in indexed(record, "external_systems"):
        for index, name in enumerate(entry.get("shares") or []):
            if isinstance(name, str) and name not in quantities:
                found.append(
                    finding(
                        rules.VOCABULARY_MISPLACED_SHARING,
                        f"external_systems.shares: {name} is no declared quantity",
                        "external_systems",
                        Entry(position, entry),
                        "shares",
                        index,
                    )
                )
    return found


def unfixed_parameters(record: Mapping[str, Any]) -> list[Finding]:
    """Return every parameter whose signature runs along the index of evolution.

    A parameter is held fixed while the phenomenon unfolds, so a quantity indexed by the index
    along which the state evolves varies during the dynamics and is an exogenous variable instead.
    """
    running = {
        e["symbol"]
        for e in entries(record, "index_sets")
        if isinstance(e.get("symbol"), str) and e.get("structure") == "evolution"
    }
    found = []
    for index, entry in indexed(record, "parameters"):
        running_along = [s for s in entry.get("signature") or [] if s in running]
        if running_along:
            found.append(
                finding(
                    rules.VOCABULARY_UNFIXED_PARAMETER,
                    f"parameters.{entry.get('symbol')}: held fixed yet indexed by {running_along}",
                    "parameters",
                    Entry(index, entry),
                    "signature",
                )
            )
    return found


def doubly_defined(record: Mapping[str, Any]) -> list[Finding]:
    """Return every quantity carrying both an expression and a condition.

    An expression builds the quantity and cannot be false; a condition states what it satisfies
    and presupposes that such a value exists. Carrying both would define the quantity twice.
    """
    found = []
    for block in ("variables", "parameters", "observables"):
        for index, entry in indexed(record, block):
            if entry.get("expression") and entry.get("condition"):
                found.append(
                    finding(
                        rules.VOCABULARY_DOUBLY_DEFINED,
                        f"{block}.{entry.get('symbol')}: both an expression and a condition",
                        block,
                        Entry(index, entry),
                    )
                )
    return found


def unowned_quantities(record: Mapping[str, Any]) -> list[Finding]:
    """Return every quantity naming an owner that the record declares no external system for.

    A quantity characterizes the target system unless it names an external system as its owner,
    so an owner that resolves to nothing leaves the quantity attached to no system at all.
    """
    systems = {
        e["symbol"] for e in entries(record, "external_systems") if isinstance(e.get("symbol"), str)
    }
    found = []
    for block in ("variables", "parameters"):
        for index, entry in indexed(record, block):
            owner = entry.get("of")
            if isinstance(owner, str) and owner not in systems:
                found.append(
                    finding(
                        rules.VOCABULARY_UNOWNED_QUANTITY,
                        f"{block}.{entry.get('symbol')}: no external system named {owner}",
                        block,
                        Entry(index, entry),
                        "of",
                    )
                )
    return found


def unselected_conditions(record: Mapping[str, Any]) -> list[Finding]:
    """Return every quantity fixed by a condition without saying which value it denotes.

    A condition may hold of several values, so the record states whether exactly one is
    presupposed, whether the claim holds of any of them, or whether the quantity is the set.
    """
    found = []
    for block in ("variables", "parameters", "observables"):
        for index, entry in indexed(record, block):
            if entry.get("condition") and entry.get("selects") not in ("unique", "any", "all"):
                found.append(
                    finding(
                        rules.VOCABULARY_UNSELECTED_CONDITION,
                        f"{block}.{entry.get('symbol')}: a condition without a selection rule",
                        block,
                        Entry(index, entry),
                        "selects",
                    )
                )
    for position, entry in indexed(record, "manifestations"):
        for index, feature in indexed(entry, "features"):
            if feature.get("condition") and feature.get("selects") not in ("unique", "any", "all"):
                found.append(
                    finding(
                        rules.VOCABULARY_UNSELECTED_CONDITION,
                        f"manifestations.features.{feature.get('symbol')}: a condition without a"
                        " selection rule",
                        "manifestations",
                        Entry(position, entry),
                        "features",
                        Entry(index, feature),
                        "selects",
                    )
                )
    return found


def vacuous_shared(record: Mapping[str, Any]) -> list[Finding]:
    """Return every quantity that marks ``shared`` while taking no signature.

    ``shared`` asserts that one value holds across every tuple of the signature, so a quantity
    with no signature has nothing to hold it across and the field states nothing.
    """
    found = []
    for block in ("variables", "parameters"):
        for index, entry in indexed(record, block):
            if "shared" in entry and not (entry.get("signature") or []):
                found.append(
                    finding(
                        rules.VOCABULARY_VACUOUS_SHARED,
                        f"{block}.{entry.get('symbol')}: shared without a signature",
                        block,
                        Entry(index, entry),
                        "shared",
                    )
                )
    return found
