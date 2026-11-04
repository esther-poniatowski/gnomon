"""
The operators that a formula may call: those of the operator registry, those that a problem
declares, and the number of arguments of each.
"""

from __future__ import annotations

from pathlib import Path
from typing import Any, Mapping

import yaml

from .. import findings as rules
from ..findings import Finding, finding
from .layout import calls, entries, formulas

DATA = Path(__file__).resolve().parent.parent / "data"


#: The registry declaring the operators the framework supplies.
OPERATOR_REGISTRY = DATA / "operators.yml"


def canonical_operators(source: Path | None = None) -> frozenset[str]:
    """Return the operator vocabulary the framework supplies.

    The registry beside this module owns the vocabulary, so extending the framework means editing
    one data file. The specification note documents the same set and is checked against it, and no
    check reads that note.

    Raises
    ------
    ValueError
        If the registry declares no operator.
    """
    registry = yaml.safe_load((source or OPERATOR_REGISTRY).read_text(encoding="utf-8")) or {}
    found = frozenset(
        entry["symbol"]
        for entry in registry.get("operators") or []
        if isinstance(entry.get("symbol"), str)
    )
    if not found:
        raise ValueError(f"{(source or OPERATOR_REGISTRY).name} declares no operator")
    return found


def operator_arity(entry: Mapping[str, Any]) -> tuple[int, bool] | None:
    """Return the arity of an operator entry and whether its last argument repeats.

    The arity counts the arguments apart from the indices that a binder consumes. An entry with a
    signature takes one argument per entry of it; any other entry states its arity. An entry that
    states both, or neither, has no arity, and the registry check reports it.

    >>> operator_arity({"symbol": "dot", "signature": ["vectors(S, n)", "vectors(S, n)"]})
    (2, False)
    >>> operator_arity({"symbol": "enum", "arity": 1, "variadic": True})
    (1, True)
    >>> operator_arity({"symbol": "odd", "arity": 1, "signature": ["S"]}) is None
    True
    """
    signature, stated = entry.get("signature"), entry.get("arity")
    if (signature is None) == (stated is None):
        return None
    count = len(signature) if isinstance(signature, list) else stated
    if not isinstance(count, int) or isinstance(count, bool) or count < 0:
        return None
    return count, bool(entry.get("variadic"))


def local_operators(record: Mapping[str, Any]) -> dict[str, str]:
    """Return the operators the record declares for its own formulas, each with its name."""
    return {
        str(e["symbol"]): str(e.get("name") or "")
        for e in entries(record, "operators")
        if isinstance(e.get("symbol"), str)
    }


def mismatched_arity(record: Mapping[str, Any], taken: Mapping[str, int]) -> list[Finding]:
    """Return every call passing a number of arguments its operator does not take.

    An operator states what it takes, so a call that passes more or fewer is reported. Only an
    operator whose signature is a list of sets is checked: one left open states no arity, and a
    quantity applied to its own indices is not an operator call at all.
    """
    found = []
    for where, place, text, _ in formulas(record):
        for name, passed in calls(text):
            expected = taken.get(name)
            if expected is not None and passed != expected:
                found.append(
                    finding(
                        rules.VOCABULARY_MISMATCHED_ARITY,
                        f"{where}: {name} takes {expected} arguments and is passed {passed}",
                        *place,
                        value=name,
                    )
                )
    return found


def arities(*records: Mapping[str, Any], source: Path | None = None) -> dict[str, int]:
    """Return the number of arguments each operator takes, where its signature says."""
    registry = yaml.safe_load((source or OPERATOR_REGISTRY).read_text(encoding="utf-8"))
    found = {}
    for entry in list(registry.get("operators") or []) + [
        e for record in records for e in entries(record, "operators")
    ]:
        signature = entry.get("signature")
        if isinstance(signature, list) and all(isinstance(s, str) for s in signature):
            found[str(entry.get("symbol"))] = len(signature)
    return found
