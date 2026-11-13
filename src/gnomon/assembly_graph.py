"""Project the computed assembly tables into one focused composition graph."""

from __future__ import annotations

from collections.abc import Mapping, Sequence
from dataclasses import dataclass
from typing import Any, TypedDict

from .graph_presentation import (
    GraphPresentation,
    GraphPresentationContract,
    load_graph_presentation,
)
from .graph_records import (
    GraphEdge,
    GraphNode,
    card_title,
    product_node,
    record_link,
    record_statement,
    status_axis,
)

Records = Mapping[str, Mapping[str, Any]]
AssemblyTables = Mapping[str, Sequence[Mapping[str, Any]]]


class AssemblyNode(GraphNode):
    """One record displayed in its assembly roles."""

    roles: list[str]
    assembly_states: list[str]


class AssemblyEdge(GraphEdge):
    """One aggregated assembly-composition relation."""

    levels: list[str]


class AssemblyGraph(TypedDict):
    """Assembly composition data and its reusable presentation profile."""

    presentation: GraphPresentationContract
    nodes: list[AssemblyNode]
    edges: list[AssemblyEdge]


@dataclass(frozen=True)
class _EdgeRelation:
    """One edge before repeated contexts are aggregated."""

    source: str
    target: str
    kind: str
    label: str
    level: str


class _AssemblyGraphBuilder:
    """Aggregate assembly table rows into canonical graph nodes and edges."""

    def __init__(self, records: Records, presentation: GraphPresentation) -> None:
        self.records = records
        self.presentation = presentation
        self.nodes: dict[str, AssemblyNode] = {}
        self.edges: dict[tuple[str, str, str, str], AssemblyEdge] = {}

    def add_node(self, identifier: str, role: str, state: str = "") -> None:
        """Add one role and contextual state to a canonical record node."""
        if not identifier:
            return
        record = self.records.get(identifier) or {}
        kind = str(record.get("type") or "product")
        node = self.nodes.get(identifier)
        if node is None:
            display = self.presentation.node("product", kind)
            node = AssemblyNode(
                **product_node(
                    identifier,
                    kind,
                    "assembly",
                    card_title(record_statement(record, identifier, self.records)),
                    record_link(identifier) if record else "",
                    status_axis(kind),
                    str(record.get("status") or ""),
                    False,
                    "",
                    display,
                ),
                roles=[],
                assembly_states=[],
            )
            self.nodes[identifier] = node
        _append(node["roles"], role)
        _append(node["assembly_states"], state)
        if role == "level":
            node["root"] = True
            node["root_label"] = "Assembly level"

    def add_edge(self, relation: _EdgeRelation) -> None:
        """Add one edge context to an aggregated canonical relation."""
        display = self.presentation.edge(relation.kind)
        label = relation.label or display.title
        key = (relation.source, relation.target, relation.kind, label)
        edge = self.edges.setdefault(
            key,
            {
                "source": relation.source,
                "target": relation.target,
                "kind": relation.kind,
                "label": label,
                "levels": [],
            },
        )
        _append(edge["levels"], relation.level)

    def project(self, tables: AssemblyTables) -> AssemblyGraph:
        """Project every assembly table that contributes topology."""
        self._add_levels(tables.get("levels", []))
        self._add_components(tables.get("components", []))
        self._add_parts(tables.get("parts", []))
        return {
            "presentation": self.presentation.contract(),
            "nodes": list(self.nodes.values()),
            "edges": list(self.edges.values()),
        }

    def _add_levels(self, rows: Sequence[Mapping[str, Any]]) -> None:
        """Add each assembly level with its settled-part and gap counts."""
        for row in rows:
            level = str(row.get("level") or "")
            settled = int(row.get("settled") or 0)
            parts = int(row.get("parts") or 0)
            gaps = int(row.get("gaps") or 0)
            part_noun = "part" if parts == 1 else "parts"
            gap_noun = "gap" if gaps == 1 else "gaps"
            self.add_node(level, "level", f"{settled}/{parts} {part_noun} settled")
            self.add_node(level, "level", f"{gaps} {gap_noun}")

    def _add_components(self, rows: Sequence[Mapping[str, Any]]) -> None:
        """Add each level-to-component relation and its contextual state."""
        for row in rows:
            level = str(row.get("level") or "")
            component = str(row.get("component") or "")
            relation = str(row.get("link") or "component")
            self.add_node(level, "level")
            self.add_node(component, "component", f"{level}: {_component_state(row)}")
            self.add_edge(
                _EdgeRelation(
                    level,
                    component,
                    "assembly-component",
                    _component_label(relation),
                    level,
                )
            )

    def _add_parts(self, rows: Sequence[Mapping[str, Any]]) -> None:
        """Add each component-to-part relation and its assessment state."""
        for row in rows:
            level = str(row.get("level") or "")
            component = str(row.get("component") or "")
            part = str(row.get("part") or "")
            kind = str(row.get("kind") or "part")
            assessment = str(row.get("assessment") or "unassessed")
            self.add_node(component, "component")
            self.add_node(part, "part", f"{level}: assessment {assessment}")
            label = "answered by" if kind == "answer" else "realized by"
            self.add_edge(
                _EdgeRelation(
                    component,
                    part,
                    "assembly-part",
                    label,
                    level,
                )
            )


def assembly_graph(
    records: Records,
    tables: AssemblyTables,
    *,
    presentation: GraphPresentation | None = None,
) -> AssemblyGraph:
    """Return the level, component, and part relations of an assembly."""
    presentation = presentation or load_graph_presentation()
    return _AssemblyGraphBuilder(records, presentation).project(tables)


def _component_state(row: Mapping[str, Any]) -> str:
    """Return one level-relative state for a component."""
    if row.get("deferred"):
        return "deferred"
    if not row.get("supplies"):
        return "supporting"
    return "settled" if row.get("settled") else "open"


def _component_label(relation: str) -> str:
    """Return the relation label in the level-to-component direction."""
    return {
        "addresses": "addressed by",
        "subquestion-of": "has subquestion",
        "enables": "enabled by",
        "presupposes": "presupposes",
        "explanans-from": "draws explanans from",
    }.get(relation, relation.replace("-", " "))


def _append(values: list[str], value: str) -> None:
    """Append one non-empty value once, preserving producer order."""
    if value and value not in values:
        values.append(value)
