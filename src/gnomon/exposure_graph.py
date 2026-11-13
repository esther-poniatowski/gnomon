"""Project computed answer exposure into a generic bipartite graph."""

from __future__ import annotations

from collections.abc import Iterable, Mapping
from typing import Any, TypedDict

from .graph_presentation import (
    GraphPresentation,
    GraphPresentationContract,
    NodePresentation,
    load_graph_presentation,
)
from .graph_records import GraphEdge, GraphNode, card_title, product_node, record_link

Records = Mapping[str, Mapping[str, Any]]


class ExposureNode(GraphNode):
    """One answer or revisable unit displayed in the exposure graph."""

    reference: str
    record: str
    role: str


class ExposureEdge(GraphEdge):
    """One aggregated answer-to-unit exposure relation."""

    reasons: list[str]
    vias: list[str]


class ExposureGraph(TypedDict):
    """Exposure reachability data and its reusable presentation profile."""

    presentation: GraphPresentationContract
    nodes: list[ExposureNode]
    edges: list[ExposureEdge]


def exposure_graph(
    records: Records,
    rows: Iterable[Mapping[str, str]],
    *,
    presentation: GraphPresentation | None = None,
) -> ExposureGraph:
    """Return one node per answer and revisable unit, with one edge per related pair."""
    presentation = presentation or load_graph_presentation()
    materialized = list(rows)
    answers = list(dict.fromkeys(row["answer"] for row in materialized))
    units = list(dict.fromkeys(row["unit"] for row in materialized))
    kinds = {row["unit"]: row["kind"] for row in materialized}
    return {
        "presentation": presentation.contract(),
        "nodes": [
            *(_answer_node(answer, records, presentation) for answer in answers),
            *(_unit_node(unit, kinds[unit], records, presentation) for unit in units),
        ],
        "edges": _edges(materialized, presentation),
    }


def _answer_node(answer: str, records: Records, presentation: GraphPresentation) -> ExposureNode:
    """Return the node from which the exposure relations of one answer leave."""
    display = presentation.node("product", "answer")
    record = records.get(answer) or {}
    claim = record.get("claim")
    claim_mapping = claim if isinstance(claim, Mapping) else {}
    label = str(claim_mapping.get("reading") or record.get("title") or answer).rstrip()
    return _node(
        answer,
        "answer",
        card_title(label),
        answer,
        display,
    )


def _unit_node(
    unit: str,
    kind: str,
    records: Records,
    presentation: GraphPresentation,
) -> ExposureNode:
    """Return one revisable unit shared by every answer that reaches it."""
    display = presentation.node("product", kind)
    owner = _owner(unit, records)
    label = unit.rsplit(".", 1)[-1].replace("_", " ").replace("-", " ")
    return _node(
        unit,
        kind,
        label[:1].upper() + label[1:],
        owner,
        display,
    )


def _node(
    identifier: str,
    kind: str,
    label: str,
    record: str,
    display: NodePresentation,
) -> ExposureNode:
    """Return the common graph fields of an answer or revisable unit."""
    role = "answer" if kind == "answer" else "revisable-unit"
    status = "Answer" if role == "answer" else "Revisable unit"
    return ExposureNode(
        **product_node(
            identifier,
            kind,
            "exposure",
            label,
            record_link(record) if record else "",
            "Exposure role",
            status,
            False,
            "",
            display,
        ),
        reference=identifier,
        record=record,
        role=role,
    )


def _edges(rows: list[Mapping[str, str]], presentation: GraphPresentation) -> list[ExposureEdge]:
    """Aggregate every row for the same answer and unit into one relation."""
    grouped: dict[tuple[str, str], ExposureEdge] = {}
    edge_display = presentation.edge("exposed-by")
    for row in rows:
        key = (row["answer"], row["unit"])
        edge = grouped.setdefault(
            key,
            {
                "source": row["answer"],
                "target": row["unit"],
                "kind": "exposed-by",
                "label": edge_display.title,
                "reasons": [],
                "vias": [],
            },
        )
        for field, target in (("reason", edge["reasons"]), ("via", edge["vias"])):
            value = row[field]
            if value not in target:
                target.append(value)
    return list(grouped.values())


def _owner(reference: str, records: Records) -> str:
    """Return the longest record identifier that owns a nested unit reference."""
    candidates = [
        identifier
        for identifier in records
        if reference == identifier or reference.startswith(f"{identifier}.")
    ]
    return max(candidates, key=len, default="")
