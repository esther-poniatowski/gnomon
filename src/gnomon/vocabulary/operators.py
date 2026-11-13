"""
The operators that a formula may call: those of the operator registry, those that a problem
declares, and the number of arguments of each.
"""

from __future__ import annotations

from pathlib import Path
from typing import Any, Mapping

import yaml

from .. import findings as rules
from ..expressions import Tree, children, parse_expression
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


def mismatched_arity(
    record: Mapping[str, Any], taken: Mapping[str, tuple[int, bool]]
) -> list[Finding]:
    """Return every call passing a number of arguments its operator does not take.

    An operator states what it takes, so a call that passes more or fewer is reported. Only an
    operator whose signature is a list of sets is checked: one left open states no arity, and a
    quantity applied to its own indices is not an operator call at all.
    """
    found = []
    for where, place, text, _ in formulas(record):
        for name, passed in calls(text):
            if name not in taken:
                continue
            expected, repeats = taken[name]
            if passed < expected or (passed > expected and not repeats):
                least = "at least " if repeats else ""
                found.append(
                    finding(
                        rules.VOCABULARY_MISMATCHED_ARITY,
                        f"{where}: {name} takes {least}{expected} arguments and is passed"
                        f" {passed}",
                        *place,
                        value=name,
                    )
                )
    return found


def arities(*records: Mapping[str, Any], source: Path | None = None) -> dict[str, tuple[int, bool]]:
    """Return the number of arguments that each operator takes, and whether its last argument
    repeats, from its signature or from its stated arity; an open signature states none.
    """
    registry = yaml.safe_load((source or OPERATOR_REGISTRY).read_text(encoding="utf-8"))
    found = {}
    for entry in list(registry.get("operators") or []) + [
        e for record in records for e in entries(record, "operators")
    ]:
        signature = entry.get("signature")
        if signature is not None and not (
            isinstance(signature, list) and all(isinstance(s, str) for s in signature)
        ):
            continue
        arity = operator_arity(entry)
        if arity is not None:
            found[str(entry.get("symbol"))] = arity
    return found


def binder_operators(*records: Mapping[str, Any], source: Path | None = None) -> frozenset[str]:
    """Return the operators of kind binder: those of the registry and those that the operator
    record of a problem declares as binders."""
    registry = yaml.safe_load((source or OPERATOR_REGISTRY).read_text(encoding="utf-8"))
    return frozenset(
        str(entry.get("symbol"))
        for entry in list(registry.get("operators") or [])
        + [e for record in records for e in entries(record, "operators")]
        if entry.get("kind") == "binder"
    )


def _bound_calls(tree: Tree) -> list[tuple[str, tuple[str, ...]]]:
    """Return each call of a tree that binds indices, with the indices that it binds."""
    found = [(str(tree[1]), tuple(tree[3]))] if tree[0] == "call" and tree[3] else []
    for child in children(tree):
        found += _bound_calls(child)
    return found


def misused_binders(
    record: Mapping[str, Any], operators: frozenset[str], binders: frozenset[str]
) -> list[Finding]:
    """Return every operator that a formula writes as a binder, ``op_{indices}(...)``, although its
    kind is not binder.

    >>> record = {"type": "phenomenon",
    ...           "observables": [{"symbol": "T", "expression": "argmax_{w}( c(w) )"}]}
    >>> [f.text for f in misused_binders(record, frozenset({"argmax", "max"}), frozenset({"max"}))]
    ['observables.expression: argmax binds the indices w, but its kind is not binder']
    """
    found = []
    for where, place, text, _ in formulas(record):
        tree = parse_expression(text)
        for name, bound in _bound_calls(tree) if tree is not None else []:
            if name in operators and name not in binders:
                found.append(
                    finding(
                        rules.VOCABULARY_MISUSED_BINDER,
                        f"{where}: {name} binds the indices {', '.join(bound)}, but its kind is"
                        " not binder",
                        *place,
                        value=name,
                    )
                )
    return found
