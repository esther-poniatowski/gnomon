"""
The relations of the organization of a record, read as a directed graph, and their checks.
"""

from __future__ import annotations

import re
from typing import Any, Mapping, Sequence

from .. import findings as rules
from ..findings import Entry, Finding, finding
from .declarations import declarations
from .layout import entries, identifiers, indexed


def interaction_graph(
    record: Mapping[str, Any], upstream: Mapping[str, Any] | None = None
) -> list[dict[str, Any]]:
    """Return the directed interaction graph the record states, one entry per relation.

    An edge is an entry of the organization: the ordered tuples the relation runs along, the reach
    last and every source before it, and the laws that state it. A tuple of three or more carries a
    joint relation, which no pair of endpoints could state. What the relation passes through is read
    from the expressions of the laws realizing it, being the quantities indexed by every place, so
    neither the endpoints nor the carriers are written a second time.

    The nodes are constituent kinds and index sets, not identified members: which tuples are joined
    is fixed by a parameter of a member model, which the record does not value, so the relation says
    where the edges of one member are to be read from.

    The relations and their laws stand in a background record, whereas the quantities that carry
    them are declared by the target system it describes, passed as ``upstream``.

    >>> target = {"type": "target-system",
    ...           "variables": [{"symbol": "u", "signature": ["sub", "sub", "t"]}]}
    >>> background = {"type": "background",
    ...               "laws": [{"symbol": "transmit", "expression": "u = emit(z)"}],
    ...               "organization": [{"symbol": "coupling", "relates": "prod(sub, sub)",
    ...                                 "realized_by": ["transmit"]}]}
    >>> interaction_graph(background, target)  # doctest: +NORMALIZE_WHITESPACE
    [{'edge': 'coupling', 'sources': ['sub'], 'reach': 'sub', 'through': ['u'],
      'tuples': 'prod(sub, sub)'}]
    """
    signatures = {
        d.symbol: d.signature for d in declarations(upstream or {}) + declarations(record)
    }
    stated = {
        str(law.get("symbol")): str(law["expression"])
        for law in entries(record, "laws")
        if isinstance(law.get("expression"), str)
    }
    graph = []
    for relation in entries(record, "organization"):
        places = influence_places(str(relation.get("relates") or ""))
        text = " ".join(stated.get(str(name), "") for name in relation.get("realized_by") or [])
        carriers = [
            name
            for name in sorted(identifiers(text))
            if places and joins(list(signatures.get(name, ())), places)
        ]
        graph.append(
            {
                "edge": relation.get("symbol"),
                "sources": places[:-1],
                "reach": places[-1] if places else None,
                "through": carriers,
                "tuples": relation.get("relates"),
            }
        )
    return graph


def influence_places(influence: str) -> list[str]:
    """Return the places an influence runs along, the reach last.

    >>> influence_places("subset(prod(sub, sub), Aij)")
    ['sub', 'sub']
    >>> influence_places("prod(pop, pop, pop)")
    ['pop', 'pop', 'pop']
    """
    found = re.search(r"prod\(([^()]*)\)", influence)
    if not found:
        return []
    places = [part.strip() for part in found.group(1).split(",")]
    return (
        places if len(places) > 1 and all(re.fullmatch(r"[A-Za-z_]\w*", p) for p in places) else []
    )


def unordered_interactions(
    record: Mapping[str, Any], upstream: Mapping[str, Any] | None = None
) -> list[Finding]:
    """Return every influence that names no ordered product of declared kinds.

    The direction of an influence is the order of the tuples it runs along, so a tuple set that
    is not a product of two or more declared kinds leaves the edge without a reach. The kinds are
    declared by the target system, passed as ``upstream`` when the relation stands elsewhere.
    """
    kinds = {
        entry.get("symbol")
        for source in (record, upstream or {})
        for block in ("constituents", "index_sets")
        for entry in entries(source, block)
    }
    found = []
    for index, relation in indexed(record, "organization"):
        if relation.get("among"):
            continue  # its ends are laws, and malformed_relations checks those
        places = influence_places(str(relation.get("relates") or ""))
        if not places or any(place not in kinds for place in places):
            found.append(
                finding(
                    rules.VOCABULARY_UNORDERED_INTERACTION,
                    f"organization.{relation.get('symbol')}:"
                    " the relation names no ordered product of declared kinds",
                    "organization",
                    Entry(index, relation),
                    "relates",
                )
            )
    return found


def malformed_relations(record: Mapping[str, Any]) -> list[Finding]:
    """Return every relation of the organization that does not say what its ends are.

    A relation runs between parts or between laws, never both. Between parts it names the tuples
    it runs along, one per pair of members, and the laws realizing it supply what it carries.
    Between laws it names the laws themselves, in order, with the reach last: two activities may
    stand in an order that no quantity carries, as when one runs only after another has completed
    and no index of the model relates their clocks. Where a shared index already fixes the order,
    the expressions carry it and the relation would restate them, which is why the corpus states
    none.
    """
    laws = {law.get("symbol") for law in entries(record, "laws")}
    found = []
    for index, relation in indexed(record, "organization"):
        where = f"organization.{relation.get('symbol')}"
        place = ("organization", Entry(index, relation))
        relates, among = relation.get("relates"), relation.get("among")
        if bool(relates) == bool(among):
            found.append(
                finding(
                    rules.VOCABULARY_RELATION_ENDS,
                    f"{where}: a relation runs between parts or between laws, and this one names"
                    f" {'both' if relates else 'neither'}",
                    *place,
                )
            )
            continue
        if not among:
            continue
        if not isinstance(among, list) or len(among) < 2:
            found.append(
                finding(
                    rules.VOCABULARY_SHORT_RELATION,
                    f"{where}: a relation among laws orders two or more of them",
                    *place,
                    "among",
                )
            )
            continue
        for position, name in enumerate(among):
            if name not in laws:
                found.append(
                    finding(
                        rules.VOCABULARY_UNKNOWN_RELATION_LAW,
                        f"{where}: {name} is no law of the record",
                        *place,
                        "among",
                        position,
                    )
                )
    return found


def joins(signature: list[str], endpoints: Sequence[Any]) -> bool:
    """Return whether the signature carries every endpoint, counting a repeated kind twice."""
    remaining = list(signature)
    for endpoint in endpoints:
        if not isinstance(endpoint, str):
            return False
        if endpoint not in remaining:
            return False
        remaining.remove(endpoint)
    return True


def misrouted_interactions(
    record: Mapping[str, Any], upstream: Mapping[str, Any] | None = None
) -> list[Finding]:
    """Return every interaction whose law names no quantity indexed by both its endpoints.

    An influence from one part to another is carried by something the ordered pair shares, so the
    law asserting it names a quantity taking both endpoints in its signature. A law naming only
    quantities of the source states a property of the source, not an influence on anything.
    """
    # the graph holds one edge per entry of the organization, in the order of the entries
    return [
        finding(
            rules.VOCABULARY_MISROUTED_INTERACTION,
            f"organization.{edge['edge']}: the laws stating it name no quantity indexed by"
            f" every one of {edge['sources'] + [edge['reach']]}",
            "organization",
            Entry(index, relation),
            "realized_by",
        )
        for (index, relation), edge in zip(
            indexed(record, "organization"), interaction_graph(record, upstream), strict=True
        )
        if not edge["through"]
    ]
