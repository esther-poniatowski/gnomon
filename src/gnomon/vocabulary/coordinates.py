"""
The coordinates of a derivative, checked against the argument that it differentiates.

A derivative names its coordinates as an argument, as in ``grad(u, x)``. The coordinates belong to
the domain of the argument: they name an index of the signature of a quantity that the argument
holds, as ``x`` indexes ``u(x, t)``, or a symbol on which the argument depends, as the parameters
``theta`` of ``loss(theta)``. The type language cannot state that tie, since the coordinates are
often one factor of the domain, so this check reads it from the signatures that the records
declare. The derivatives are the operators whose rule of dimension divides by their coordinates.

Functions
---------
foreign_coordinates
    Return the derivatives whose coordinates index no quantity of their argument and occur
    nowhere in it.
"""

from __future__ import annotations

from typing import Any, Iterable, Iterator, Mapping

from .. import findings as rules
from ..dimensions import DERIVATIVE_RULES
from ..expressions import Tree, parse_expression
from ..findings import Finding, finding
from .layout import formulas


def _derivatives(tree: Tree, rules_: Mapping[str, str]) -> Iterator[tuple[str, Tree, Tree]]:
    """Yield each derivative of a tree with its argument and its coordinates."""
    if not isinstance(tree, tuple) or not tree:
        return
    if tree[0] == "call":
        args = tree[2]
        if rules_.get(tree[1]) in DERIVATIVE_RULES and len(args) >= 2:
            yield tree[1], args[0], args[1]
        for arg in args:
            yield from _derivatives(arg, rules_)
        return
    for part in tree[1:]:
        if isinstance(part, tuple):
            yield from _derivatives(part, rules_)


def _named(tree: Any) -> set[str]:
    """Return the symbols and the names of the calls that a tree holds."""
    if not isinstance(tree, tuple) or not tree:
        return set()
    if tree[0] == "sym":
        return {str(tree[1])}
    if tree[0] == "call":
        found = {str(tree[1]), *(str(index) for index in tree[3])}
        for arg in tree[2]:
            found |= _named(arg)
        return found
    found = set()
    for part in tree[1:]:
        if isinstance(part, tuple):
            found |= _named(part)
    return found


def domain(values: Any) -> str | None:
    """Return the domain of a value set written ``maps(D, R)``, or None for any other set.

    >>> domain("maps(U(sp), U(sp))"), domain("reals")
    ('U(sp)', None)
    """
    text = str(values or "").replace(" ", "")
    if not text.startswith("maps(") or not text.endswith(")"):
        return None
    depth = 0
    for i, char in enumerate(text[5:-1]):
        depth += {"(": 1, ")": -1}.get(char, 0)
        if char == "," and depth == 0:
            return text[5 : 5 + i]
    return None


def _mismatch(
    argument: Tree,
    along: str,
    signatures: Mapping[str, Iterable[str]],
    value_sets: Mapping[str, str],
) -> str | None:
    """Return why coordinates fail the argument that a derivative differentiates, or None when
    they index a quantity of it, occur in it, or form the domain of a map that it names."""
    named = _named(argument)
    if along in named or any(along in set(signatures.get(s, ())) for s in named):
        return None
    domains = {s: domain(value_sets.get(s)) for s in named if domain(value_sets.get(s))}
    coordinate_set = str(value_sets.get(along) or "").replace(" ", "")
    if coordinate_set and coordinate_set in domains.values():
        return None
    shown = argument[1] if argument[0] in ("sym", "call") else "its argument"
    if domains and coordinate_set:
        return (
            f"{shown} along {along}, whose values {value_sets.get(along)} are not the domain of"
            f" {', '.join(sorted(domains))}"
        )
    return f"{shown} along {along}, which indexes no quantity of it and occurs nowhere in it"


def foreign_coordinates(
    record: Mapping[str, Any],
    signatures: Mapping[str, Iterable[str]],
    rules_: Mapping[str, str],
    value_sets: Mapping[str, str] | None = None,
) -> list[Finding]:
    """Return the derivatives whose coordinates index no quantity of their argument and occur
    nowhere in it, unless the argument names a map whose domain is the value set of the
    coordinates, as ``jacobian(F, u, u_star)`` for a map ``F`` from the states ``u``.

    >>> signatures = {"u": ("x", "t"), "Ltrain": ("step",), "theta": ("coord", "step")}
    >>> record = {"type": "background", "laws": [
    ...     {"expression": "diff(u, t) = lap(u, x)"},
    ...     {"expression": "diff(theta, step) = grad(Ltrain, theta)"}]}
    >>> rules_ = {"diff": "derivative", "lap": "second-derivative", "grad": "derivative"}
    >>> for f in foreign_coordinates(record, signatures, rules_):
    ...     print(f.text)  # doctest: +NORMALIZE_WHITESPACE
    laws.expression: grad differentiates Ltrain along theta, which indexes no quantity of it and
    occurs nowhere in it
    """
    found = []
    for where, place, text, _ in formulas(record):
        tree = parse_expression(text)
        if tree is None:
            continue
        for name, argument, coordinates in _derivatives(tree, rules_):
            if coordinates[0] != "sym":
                continue
            along = str(coordinates[1])
            problem = _mismatch(argument, along, signatures, value_sets or {})
            if problem is None:
                continue
            message = f"{where}: {name} differentiates {problem}"
            found.append(
                finding(rules.VOCABULARY_FOREIGN_COORDINATES, message, *place, value=along)
            )
    return found
