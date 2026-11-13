"""Build the dependency graph that reports whether itinerary outputs remain usable."""

from __future__ import annotations

from collections import defaultdict
from collections.abc import Mapping
from dataclasses import dataclass
from typing import Any, TypedDict
from urllib.parse import quote

from .graph_presentation import (
    GraphPresentation,
    GraphPresentationContract,
    load_graph_presentation,
)
from .graph_records import GraphEdge, GraphNode
from .itineraries import activities

Records = Mapping[str, Mapping[str, Any]]
UNSETTLED = frozenset({"pending", "inconclusive"})


class ProgressNode(GraphNode):
    """One itinerary step or external state origin displayed in the progress graph."""

    itinerary: str
    step: str
    activity: str
    verdict: str
    output: str
    state: str
    origins: list[str]
    external_origin: bool


class ProgressEdge(GraphEdge):
    """One dependency or external-state relation in the progress graph."""


class ProgressGraph(TypedDict):
    """Itinerary progress data and its reusable presentation profile."""

    presentation: GraphPresentationContract
    nodes: list[ProgressNode]
    edges: list[ProgressEdge]


@dataclass(frozen=True)
class _Output:
    """The declared product of one step and its later concrete realization."""

    reference: str
    kind: str
    produced: bool
    realization: str


@dataclass(frozen=True)
class _Step:
    """The fields of one authored step needed to compute graph topology and state."""

    identifier: str
    itinerary: str
    local_id: str
    activity: str
    verdict: str
    inputs: tuple[str, ...]
    output: _Output


@dataclass(frozen=True)
class _OriginMaps:
    """Displayed failed and unsettled origins propagated to every step."""

    failed: Mapping[str, set[str]]
    conditional: Mapping[str, set[str]]


@dataclass(frozen=True)
class _ExternalStates:
    """Direct and propagated states whose origins lie outside the displayed steps."""

    direct_impeached: set[str]
    direct_conditional: set[str]
    impeached: set[str]
    conditional: set[str]


@dataclass(frozen=True)
class _NodeContext:
    """Shared inputs used to construct every step node."""

    records: Records
    presentation: GraphPresentation
    activity_types: Mapping[str, Any]
    origins: _OriginMaps
    external: _ExternalStates


def itinerary_progress_graph(
    records: Records,
    impeached: set[str],
    conditional: set[str],
    *,
    presentation: GraphPresentation | None = None,
) -> ProgressGraph:
    """Return every itinerary step, dependency, and origin of its output-usability state."""
    presentation = presentation or load_graph_presentation()
    steps = _steps(records)
    dependencies = _dependencies(steps)
    origins = _origin_maps(steps, dependencies)
    external = _external_states(steps, dependencies, origins, impeached, conditional)
    context = _NodeContext(records, presentation, activities(), origins, external)
    nodes = _step_nodes(steps, context)
    external_nodes, external_edges = _external_graph(steps, external, presentation)
    edges = [
        _edge(source, target, "step-dependency", presentation) for source, target in dependencies
    ]

    return {
        "presentation": presentation.contract(),
        "nodes": [*nodes, *external_nodes],
        "edges": [*edges, *external_edges],
    }


def _steps(records: Records) -> list[_Step]:
    """Return valid itinerary steps in itinerary and authored step order."""
    found: list[_Step] = []
    for itinerary_id, itinerary in sorted(records.items()):
        if itinerary.get("type") != "itinerary":
            continue
        for raw in itinerary.get("steps") or []:
            if not isinstance(raw, Mapping) or not raw.get("id"):
                continue
            local_id = str(raw["id"])
            output = raw.get("output")
            produced = isinstance(output, Mapping) and bool(output.get("ref") or output.get("type"))
            output_mapping: Mapping[str, Any] = output if isinstance(output, Mapping) else {}
            norm = raw.get("norm")
            norm_mapping: Mapping[str, Any] = norm if isinstance(norm, Mapping) else {}
            rationale = raw.get("rationale")
            rationale_mapping: Mapping[str, Any] = (
                rationale if isinstance(rationale, Mapping) else {}
            )
            realization = str(rationale_mapping.get("serves") or "")
            realized_record = records.get(realization)
            if not (
                output_mapping.get("type") == "question-schema"
                and realized_record is not None
                and realized_record.get("type") == "question"
            ):
                realization = ""
            found.append(
                _Step(
                    identifier=f"{itinerary_id}.{local_id}",
                    itinerary=itinerary_id,
                    local_id=local_id,
                    activity=str(raw.get("activity") or "unspecified-activity"),
                    verdict=str(norm_mapping.get("verdict") or "pending"),
                    inputs=tuple(
                        str(item.get("ref") or "")
                        for item in raw.get("inputs") or []
                        if isinstance(item, Mapping) and item.get("ref")
                    ),
                    output=_Output(
                        reference=str(output_mapping.get("ref") or ""),
                        kind=str(output_mapping.get("type") or ""),
                        produced=produced,
                        realization=realization,
                    ),
                )
            )
    return found


def _dependencies(steps: list[_Step]) -> list[tuple[str, str]]:
    """Return every displayed producer-to-consumer dependency without sorting or cycle removal."""
    identifiers = {step.identifier for step in steps}
    producers: dict[str, list[str]] = defaultdict(list)
    for step in steps:
        if step.output.reference:
            producers[step.output.reference].append(step.identifier)
    dependencies: list[tuple[str, str]] = []
    for step in steps:
        for reference in step.inputs:
            sources = [reference] if reference in identifiers else producers.get(reference, [])
            for source in sources:
                edge = (source, step.identifier)
                if edge not in dependencies:
                    dependencies.append(edge)
    return dependencies


def _origin_maps(steps: list[_Step], dependencies: list[tuple[str, str]]) -> _OriginMaps:
    """Return the displayed failed and unsettled origins propagated through dependencies."""
    return _OriginMaps(
        failed=_propagated_origins(steps, dependencies, {"fail"}),
        conditional=_propagated_origins(steps, dependencies, UNSETTLED),
    )


def _external_states(
    steps: list[_Step],
    dependencies: list[tuple[str, str]],
    origins: _OriginMaps,
    impeached: set[str],
    conditional: set[str],
) -> _ExternalStates:
    """Return direct and propagated states whose origins are outside the graph."""
    direct_impeached, direct_conditional = _external_entries(
        steps, dependencies, origins, impeached, conditional
    )
    return _ExternalStates(
        direct_impeached=direct_impeached,
        direct_conditional=direct_conditional,
        impeached=_propagated_flags(steps, dependencies, direct_impeached),
        conditional=_propagated_flags(steps, dependencies, direct_conditional),
    )


def _step_nodes(steps: list[_Step], context: _NodeContext) -> list[ProgressNode]:
    """Return one graph node per displayed itinerary step."""
    return [_step_node(step, context) for step in steps]


def _step_node(step: _Step, context: _NodeContext) -> ProgressNode:
    """Return one step node with its propagated output-usability state."""
    state = _state(
        step,
        context.origins.failed[step.identifier],
        context.origins.conditional[step.identifier],
        step.identifier in context.external.impeached,
        step.identifier in context.external.conditional,
    )
    origins = (
        context.origins.failed[step.identifier]
        if state == "impeached"
        else (context.origins.conditional[step.identifier] if state == "conditional" else set())
    )
    external = (
        step.identifier in context.external.impeached
        if state == "impeached"
        else (step.identifier in context.external.conditional if state == "conditional" else False)
    )
    display = context.presentation.node("activity", step.activity)
    activity_type = context.activity_types.get(step.activity)
    target = _output_target(step)
    return {
        "id": step.identifier,
        "category": "activity",
        "category_label": display.category_title,
        "shape": display.shape,
        "marker": display.marker,
        "kind": step.activity,
        "family": activity_type.family if activity_type is not None else "",
        "label": _output_label(step, context.records),
        "link": _record_link(target) if target in context.records else "",
        "status_axis": "Output usability",
        "status": _visible_status(state, origins, external, step.identifier),
        "root": False,
        "root_label": "",
        "itinerary": step.itinerary,
        "step": step.local_id,
        "activity": step.activity,
        "verdict": step.verdict,
        "output": step.output.reference,
        "state": state,
        "origins": sorted(origins),
        "external_origin": external,
    }


def _external_graph(
    steps: list[_Step],
    external: _ExternalStates,
    presentation: GraphPresentation,
) -> tuple[list[ProgressNode], list[ProgressEdge]]:
    """Return explicit nodes and edges for states that originate outside the graph."""
    nodes: list[ProgressNode] = []
    edges: list[ProgressEdge] = []
    for itinerary in dict.fromkeys(step.itinerary for step in steps):
        for state, entries, kind in (
            ("impeached", external.direct_impeached, "impeaches"),
            ("conditional", external.direct_conditional, "conditions"),
        ):
            affected = [
                step.identifier
                for step in steps
                if step.itinerary == itinerary and step.identifier in entries
            ]
            if not affected:
                continue
            source = f"external-origin:{itinerary}:{state}"
            nodes.append(_external_node(source, itinerary, state, presentation))
            edges.extend(_edge(source, target, kind, presentation) for target in affected)
    return nodes, edges


def _propagated_origins(
    steps: list[_Step],
    dependencies: list[tuple[str, str]],
    verdicts: set[str] | frozenset[str],
) -> dict[str, set[str]]:
    """Return every matching verdict origin that reaches each displayed step."""
    origins = {
        step.identifier: ({step.identifier} if step.verdict in verdicts else set())
        for step in steps
    }
    changed = True
    while changed:
        changed = False
        for source, target in dependencies:
            added = origins[source] - origins[target]
            if added:
                origins[target].update(added)
                changed = True
    return origins


def _external_entries(
    steps: list[_Step],
    dependencies: list[tuple[str, str]],
    origins: _OriginMaps,
    impeached: set[str],
    conditional: set[str],
) -> tuple[set[str], set[str]]:
    """Return steps whose supplied state has no origin among displayed producer steps."""
    displayed_inputs: dict[str, set[str]] = {step.identifier: set() for step in steps}
    for source, target in dependencies:
        displayed_inputs[target].add(source)
    direct_impeached: set[str] = set()
    direct_conditional: set[str] = set()
    for step in steps:
        external_inputs = [
            reference
            for reference in step.inputs
            if reference not in displayed_inputs[step.identifier]
            and not any(
                producer.output.reference == reference
                for producer in steps
                if producer.identifier in displayed_inputs[step.identifier]
            )
        ]
        if any(reference in impeached for reference in external_inputs) or (
            step.output.reference in impeached and not origins.failed[step.identifier]
        ):
            direct_impeached.add(step.identifier)
        if any(reference in conditional for reference in external_inputs) or (
            step.output.reference in conditional and not origins.conditional[step.identifier]
        ):
            direct_conditional.add(step.identifier)
    return direct_impeached, direct_conditional


def _propagated_flags(
    steps: list[_Step],
    dependencies: list[tuple[str, str]],
    entries: set[str],
) -> set[str]:
    """Return every displayed step reached from an external-state entry."""
    reached = set(entries)
    changed = True
    while changed:
        changed = False
        for source, target in dependencies:
            if source in reached and target not in reached:
                reached.add(target)
                changed = True
    return reached & {step.identifier for step in steps}


def _state(
    step: _Step,
    fail_origins: set[str],
    conditional_origins: set[str],
    external_impeached: bool,
    external_conditional: bool,
) -> str:
    """Return the usability state of one output, with absence taking precedence."""
    if not step.output.produced:
        return "not-produced"
    if fail_origins or external_impeached:
        return "impeached"
    if conditional_origins or external_conditional:
        return "conditional"
    return "sound"


def _visible_status(state: str, origins: set[str], external: bool, identifier: str) -> str:
    """Return the compact status that distinguishes an origin from transmitted state."""
    if external:
        return f"{state} · external origin"
    if identifier in origins:
        return f"{state} · origin"
    return state


def _output_label(step: _Step, records: Records) -> str:
    """Return the compact outcome title of one step without sentence punctuation."""
    if not step.output.produced:
        return "No output has been produced"
    target = _output_target(step)
    record = records.get(target)
    if record is not None and record.get("title"):
        return f"Produces {str(record['title']).rstrip().rstrip('.').rstrip()}"
    if step.output.reference:
        return f"Produces {step.output.reference}"
    product = step.output.kind.replace("-", " ")
    article = "an" if product[:1].lower() in "aeiou" else "a"
    return f"Produces {article} {product}"


def _output_target(step: _Step) -> str:
    """Return the authored record opened from one produced output, if one exists."""
    return step.output.reference or step.output.realization


def _record_link(identifier: str) -> str:
    """Return the Ekphrasis URI that opens one authored output record."""
    return f"obsidian://ekphrasis?id={quote(identifier, safe='')}"


def _edge(
    source: str,
    target: str,
    kind: str,
    presentation: GraphPresentation,
) -> ProgressEdge:
    """Return one typed edge with its registered display label."""
    return {
        "source": source,
        "target": target,
        "kind": kind,
        "label": presentation.edge(kind).title,
    }


def _external_node(
    identifier: str,
    itinerary: str,
    state: str,
    presentation: GraphPresentation,
) -> ProgressNode:
    """Return one explicit root for a state whose origin is outside the displayed steps."""
    display = presentation.node("source", "external-origin")
    noun = "impeachment" if state == "impeached" else "condition"
    return {
        "id": identifier,
        "category": "source",
        "category_label": display.category_title,
        "shape": display.shape,
        "marker": display.marker,
        "kind": "external-origin",
        "family": "",
        "label": f"External {noun}",
        "link": "",
        "status_axis": "Output usability",
        "status": state,
        "root": False,
        "root_label": "",
        "itinerary": itinerary,
        "step": "",
        "activity": "",
        "verdict": "",
        "output": "",
        "state": state,
        "origins": [],
        "external_origin": True,
    }
