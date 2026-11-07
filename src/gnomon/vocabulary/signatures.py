"""
The signature of a defined quantity, checked against the indices that its definition leaves free.

The free indices of a definition form the signature of the quantity that it defines: a binder
consumes the indices that it names, and every other index written in the definition stays free.
A free index may also be the variable of the value of the quantity, when the quantity takes its
values in a set of maps ``maps(D, R)`` whose domain ``D`` names that index. Any other free index is
absent from what the quantity is declared to take, so the signature contradicts the definition.

The converse is not checked. A declared index that the definition does not write may come from a
quantity written without its indices, as ``u`` in ``grad(u, x)``, or from the values of an
operator, as a kernel over inputs from ``ntk(theta, X)``; deciding it requires the result type of
every operator, which the type language does not state.

Functions
---------
free_indices
    Return the indices that a tree leaves free, in the order of the text.
contradicted_signatures
    Return each defined quantity whose definition leaves free an index that its signature omits.
application_counts
    Return the numbers of arguments to which each declared quantity may be applied.
misapplied_quantities
    Return each application of a quantity to a number of arguments that it does not take.
"""

from __future__ import annotations

from typing import Any, Iterable, Mapping

from .. import findings as rules
from ..expressions import Tree, children, parse_expression
from ..findings import Entry, Finding, finding
from .coordinates import domain
from .layout import DECLARING, calls, entries, formulas, identifiers, indexed

#: The blocks whose entries declare a quantity that an expression may define.
QUANTITY_BLOCKS: tuple[str, ...] = ("variables", "parameters", "observables")


def free_indices(tree: Tree, indices: frozenset[str]) -> list[str]:
    """Return the indices that a tree leaves free, in the order of the text.

    A binder consumes the indices that it binds. The set over which a fresh index ranges, as ``a``
    in ``a1 in a``, is consumed with it, while the bound of a restriction, as ``T`` in ``t <= T``,
    stays free.

    >>> tree = parse_expression("mean_{x, t}( u(a, x, t) * u(b, x + r, t + tau) )")
    >>> free_indices(tree, frozenset({"a", "b", "x", "t", "r", "tau"}))
    ['a', 'b', 'r', 'tau']
    >>> free_indices(parse_expression("norm_{a1 in a}( K(a1, t) )"), frozenset({"a", "t"}))
    ['t']
    """
    if tree[0] == "sym":
        return [str(tree[1])] if tree[1] in indices else []
    if tree[0] != "call":
        return [name for child in children(tree) for name in free_indices(child, indices)]
    _, _, args, binds, restrictions = tree
    found = [
        name
        for restriction in restrictions
        if restriction is not None and restriction[1] != "in"
        for name in free_indices(restriction[3], indices)
    ]
    found += [name for arg in args for name in free_indices(arg, indices)]
    return [name for name in found if name not in binds]


def contradicted_signatures(record: Mapping[str, Any], indices: Iterable[str]) -> list[Finding]:
    """Return each defined quantity whose definition leaves free an index that its signature omits
    and that the domain of its values does not name.

    Parameters
    ----------
    record : mapping
        One filled inquiry record.
    indices : iterable of str
        The symbols of the index sets and the constituent kinds that the record can see, which are
        the indices that a quantity may take.

    >>> record = {"observables": [
    ...     {"symbol": "Z", "signature": [], "expression": "sequence(sub, Tev)"},
    ...     {"symbol": "F", "signature": ["sub"], "values": "maps(t, interval(0, 1))",
    ...      "expression": "dist_{r}( Tev(sub) <= t )"}]}
    >>> [f.text for f in contradicted_signatures(record, {"sub", "t", "r"})]
    ['observables.expression of Z: leaves sub free, which its signature omits']
    """
    known = frozenset(indices)
    found: list[Finding] = []
    for block in QUANTITY_BLOCKS:
        for position, entry in indexed(record, block):
            declared = entry.get("signature")
            tree = parse_expression(entry.get("expression"))
            if tree is None or not isinstance(declared, list):
                continue
            allowed = set(declared) | identifiers(domain(entry.get("values")) or "")
            symbol = entry.get("symbol")
            found += [
                finding(
                    rules.VOCABULARY_CONTRADICTED_SIGNATURE,
                    f"{block}.expression of {symbol}: leaves {name} free, which its signature"
                    " omits",
                    block,
                    Entry(position, entry),
                    "expression",
                    value=name,
                )
                for name in dict.fromkeys(free_indices(tree, known))
                if name not in allowed
            ]
    return found


def _map_arities(values: Any) -> set[int]:
    """Return the numbers of arguments of a value map ``maps(D, R)``: the factors of its domain,
    at the top level and once nested products are flattened; none for any other value set.

    >>> sorted(_map_arities("maps(prod(prod(a, b), c), reals)")), sorted(_map_arities("reals"))
    ([2, 3], [])
    """
    stated = domain(values)
    tree = parse_expression(stated) if stated else None
    if tree is None:
        return set()

    def factors(node: Tree) -> list[Tree]:
        if node[0] == "call" and node[1] == "prod":
            return [leaf for arg in node[2] for leaf in factors(arg)]
        return [node]

    top = len(tree[2]) if tree[0] == "call" and tree[1] == "prod" else 1
    return {top, len(factors(tree))}


def application_counts(
    records: Iterable[Mapping[str, Any]],
) -> dict[str, frozenset[int] | None]:
    """Return, per declared quantity, the numbers of arguments to which it may be applied: its
    indices, or the arguments of its value map; None when a declaration leaves its values open, so
    that its applications are not checked.

    >>> application_counts([{"type": "target-system", "variables": [
    ...     {"symbol": "u", "signature": ["x", "t"], "values": "reals"},
    ...     {"symbol": "f", "signature": [], "values": "maps(prod(a, b), reals)"},
    ...     {"symbol": "g", "signature": ["t"], "values": None}]}])
    {'u': frozenset({2}), 'f': frozenset({0, 2}), 'g': None}
    """
    found: dict[str, frozenset[int] | None] = {}
    for record in records:
        for block in DECLARING.get(str(record.get("type", "")), ()):
            for entry in entries(record, block):
                symbol, signature = entry.get("symbol"), entry.get("signature")
                if not isinstance(symbol, str) or not isinstance(signature, list):
                    continue
                values = entry.get("values")
                counts: frozenset[int] | None = (
                    None
                    if not isinstance(values, str) or not values.strip()
                    else frozenset({len(signature), *_map_arities(values)})
                )
                if symbol in found:
                    known = found[symbol]
                    counts = None if known is None or counts is None else known | counts
                found[symbol] = counts
    return found


def misapplied_quantities(
    record: Mapping[str, Any],
    counts: Mapping[str, frozenset[int] | None],
    operators: frozenset[str],
) -> list[Finding]:
    """Return each application of a declared quantity to a number of arguments that neither its
    signature nor its value map takes.

    >>> record = {"type": "phenomenon", "manifestations": [
    ...     {"symbol": "m", "expression": "forall_{y}( tpeak(w, y) > 0 )"}]}
    >>> [f.text for f in misapplied_quantities(record, {"tpeak": frozenset({1})}, frozenset())]
    ['manifestations.expression: tpeak is applied to 2 arguments, where it takes 1']
    """
    found = []
    for where, place, text, _ in formulas(record):
        for name, passed in calls(text):
            taken = counts.get(name)
            if name in operators or taken is None or passed in taken:
                continue
            found.append(
                finding(
                    rules.VOCABULARY_MISMATCHED_INDICES,
                    f"{where}: {name} is applied to {passed} arguments, where it takes"
                    f" {' or '.join(str(n) for n in sorted(taken))}",
                    *place,
                    value=name,
                )
            )
    return found
