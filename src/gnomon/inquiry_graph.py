"""Build the operational graph of research products and epistemic activities.

The graph combines two relations that the authored records keep separate. Inquiry relations
connect problems, questions, answers, assessments, and serving designs. Itinerary steps supply
provenance relations from typed input products, through an activity instance, to its typed output.
"""

from __future__ import annotations

import hashlib
from collections.abc import Mapping
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
from .itineraries import activities

Records = Mapping[str, Mapping[str, Any]]


class InquiryGraph(TypedDict):
    """Operational graph data and its reusable presentation profile."""

    presentation: GraphPresentationContract
    nodes: list[GraphNode]
    edges: list[GraphEdge]


# The builder keeps the canonical node and edge stores beside the itinerary traversal they serve.
# pylint: disable-next=too-many-locals
def inquiry_graph(
    records: Records, *, presentation: GraphPresentation | None = None
) -> InquiryGraph:
    """Return the nodes and directed edges of the operational inquiry graph.

    A record is represented by one product node even when several activities read or produce it.
    An output without a record reference receives a stable node local to its producing step. Direct
    inputs that name neither a record nor a step receive a stable external-source node.

    Parameters
    ----------
    records
        Authored records keyed by their identifiers.
    presentation
        Validated producer-owned presentation defaults. Package data is read when omitted.

    Returns
    -------
    dict
        The producer-ordered ``nodes`` and ``edges`` consumed by a generic graph renderer.
    """
    nodes: dict[str, GraphNode] = {}
    edges: dict[tuple[str, str, str, str], GraphEdge] = {}
    activity_types = activities()
    presentation = presentation or load_graph_presentation()

    def add_node(node: GraphNode) -> None:
        node["label"] = card_title(node["label"])
        nodes.setdefault(node["id"], node)

    def add_record(identifier: str, product_type: str = "", realization: str = "") -> None:
        record = records.get(identifier)
        if record is None:
            kind = product_type or "unrecorded-product"
            display = presentation.node("product", kind)
            realized_record = records.get(realization)
            add_node(
                product_node(
                    identifier,
                    kind,
                    "",
                    (
                        record_statement(realized_record, realization, records)
                        if realized_record is not None
                        else identifier
                    ),
                    record_link(realization) if realized_record is not None else "",
                    "Record state",
                    "unrecorded",
                    False,
                    "",
                    display,
                )
            )
            return
        kind = str(record.get("type") or product_type or "product")
        display = presentation.node("product", kind)
        add_node(
            product_node(
                identifier,
                kind,
                "",
                record_statement(record, identifier, records),
                record_link(identifier),
                status_axis(kind),
                str(record.get("status") or ""),
                kind == "problem",
                "Starting problem" if kind == "problem" else "",
                display,
            )
        )

    def add_edge(source: str, target: str, kind: str) -> None:
        label = presentation.edge(kind).title
        edge: GraphEdge = {
            "source": source,
            "target": target,
            "kind": kind,
            "label": label,
        }
        edges.setdefault((source, target, kind, label), edge)

    _add_inquiry_relations(records, add_record, add_edge)

    step_outputs: dict[str, tuple[str, str]] = {}
    steps: list[tuple[str, Mapping[str, Any]]] = []
    for itinerary_id, itinerary in sorted(records.items()):
        if itinerary.get("type") != "itinerary":
            continue
        for step in itinerary.get("steps") or []:
            if not isinstance(step, Mapping):
                continue
            step_id = str(step.get("id") or "")
            if not step_id:
                continue
            activity_id = f"{itinerary_id}.{step_id}"
            output: Mapping[str, Any] = (
                step["output"] if isinstance(step.get("output"), Mapping) else {}
            )
            output_ref = str(output.get("ref") or f"product:{activity_id}")
            output_type = str(output.get("type") or "product")
            step_outputs[activity_id] = (output_ref, output_type)
            steps.append((activity_id, step))

    for activity_id, step in steps:
        activity = str(step.get("activity") or "unspecified-activity")
        activity_type = activity_types.get(activity)
        output_id, output_type = step_outputs[activity_id]
        norm: Mapping[str, Any] = step["norm"] if isinstance(step.get("norm"), Mapping) else {}
        display = presentation.node("activity", activity)
        add_node(
            {
                "id": activity_id,
                "category": "activity",
                "category_label": display.category_title,
                "shape": display.shape,
                "marker": display.marker,
                "kind": activity,
                "family": activity_type.family if activity_type is not None else "",
                "label": _activity_statement(output_type),
                "link": "",
                "status_axis": "Norm verdict",
                "status": str(norm.get("verdict") or "pending"),
                "root": False,
                "root_label": "",
            }
        )
        for index, item in enumerate(step.get("inputs") or []):
            if not isinstance(item, Mapping):
                continue
            product_type = str(item.get("type") or "product")
            reference = str(item.get("ref") or "")
            input_id = _input_node(
                activity_id,
                index,
                reference,
                product_type,
                records,
                step_outputs,
                presentation,
                add_node,
            )
            add_edge(input_id, activity_id, "takes")

        realization = _output_realization(step, output_type, records)
        add_record(output_id, output_type, realization)
        add_edge(activity_id, output_id, "produces")

    return {
        "presentation": presentation.contract(),
        "nodes": list(nodes.values()),
        "edges": list(edges.values()),
    }


# Each branch implements one registered product relation in its authored direction.
# pylint: disable-next=too-many-branches
def _add_inquiry_relations(
    records: Records,
    add_record: Any,
    add_edge: Any,
) -> None:
    """Add the problem-to-assessment route and serving designs in its reading direction."""
    for identifier, record in sorted(records.items()):
        kind = record.get("type")
        if kind == "problem":
            add_record(identifier)
        if kind == "question":
            add_record(identifier)
            problem = str(record.get("addresses") or "")
            if problem:
                add_record(problem)
                add_edge(problem, identifier, "addresses")
            for link in record.get("links") or []:
                if not isinstance(link, Mapping) or link.get("relation") != "subquestion-of":
                    continue
                parent = str(link.get("question") or "")
                if parent:
                    add_record(parent)
                    add_edge(parent, identifier, "subquestion-of")
        elif kind == "answer":
            add_record(identifier)
            question = str(record.get("answers") or "")
            if question:
                add_record(question)
                add_edge(question, identifier, "answers")
        elif kind == "assessment":
            add_record(identifier)
            answer = str(record.get("assesses") or "")
            if answer:
                add_record(answer)
                add_edge(answer, identifier, "assesses")
        elif kind == "design":
            add_record(identifier)
            served = str(record.get("serves") or "")
            if served:
                add_record(served)
                add_edge(served, identifier, "serves")


# The input resolver receives both record and itinerary namespaces plus their presentation boundary.
# pylint: disable-next=too-many-arguments,too-many-positional-arguments
def _input_node(
    activity_id: str,
    index: int,
    reference: str,
    product_type: str,
    records: Records,
    step_outputs: Mapping[str, tuple[str, str]],
    presentation: GraphPresentation,
    add_node: Any,
) -> str:
    """Return the product node read by one activity input, creating an external node if needed."""
    if reference in step_outputs:
        return step_outputs[reference][0]
    if reference in records:
        record = records[reference]
        kind = str(record.get("type") or product_type)
        display = presentation.node("product", kind)
        add_node(
            product_node(
                reference,
                kind,
                "",
                record_statement(record, reference, records),
                record_link(reference),
                status_axis(kind),
                str(record.get("status") or ""),
                record.get("type") == "problem",
                "Starting problem" if record.get("type") == "problem" else "",
                display,
            )
        )
        return reference
    external_id = _source_id(reference or f"{activity_id}:{index}")
    display = presentation.node("source", "source")
    add_node(
        {
            "id": external_id,
            "category": "source",
            "category_label": display.category_title,
            "shape": display.shape,
            "marker": display.marker,
            "kind": "source",
            "family": "",
            "label": reference or product_type,
            "link": _external_link(reference),
            "status_axis": "Source state",
            "status": "external",
            "root": False,
            "root_label": "",
        }
    )
    return external_id


def _source_id(reference: str) -> str:
    """Return a stable node identifier for one external pointer."""
    digest = hashlib.sha256(reference.strip().encode("utf-8")).hexdigest()
    return f"source:{digest}"


def _activity_statement(output_type: str) -> str:
    """Return a short verbal statement of the state change made by an activity."""
    product = output_type.replace("-", " ")
    article = "an" if product[:1].lower() in "aeiou" else "a"
    if product.endswith("s") or product in {
        "background",
        "data",
        "evidence",
        "knowledge",
    }:
        return f"Produces {product}."
    return f"Produces {article} {product}."


def _output_realization(step: Mapping[str, Any], output_type: str, records: Records) -> str:
    """Return the concrete question that realizes an unrecorded question schema, if declared."""
    if output_type != "question-schema":
        return ""
    rationale = step.get("rationale")
    if not isinstance(rationale, Mapping):
        return ""
    served = str(rationale.get("serves") or "")
    record = records.get(served)
    return served if record is not None and record.get("type") == "question" else ""


def _external_link(reference: str) -> str:
    """Return the URL written in an external pointer, when it holds one."""
    for token in reference.split():
        if token.startswith(("https://", "http://")):
            return token
    return ""
