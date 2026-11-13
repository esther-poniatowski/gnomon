"""Reusable record labels and links for generated graph views."""

from __future__ import annotations

import re
from collections import Counter
from collections.abc import Mapping
from typing import Any, TypedDict
from urllib.parse import quote

from .graph_presentation import NodePresentation

Records = Mapping[str, Mapping[str, Any]]


class GraphNode(TypedDict):
    """Fields shared by every node in a generated graph view."""

    # The serialized graph contract names this field ``id``.
    # pylint: disable-next=disallowed-name
    id: str
    category: str
    category_label: str
    shape: str
    marker: str
    kind: str
    family: str
    label: str
    link: str
    status_axis: str
    status: str
    root: bool
    root_label: str


class GraphEdge(TypedDict):
    """Fields shared by every directed edge in a generated graph view."""

    source: str
    target: str
    kind: str
    label: str


# This constructor spells out the complete serialized node contract in one place.
# pylint: disable-next=too-many-arguments,too-many-positional-arguments
def product_node(
    identifier: str,
    kind: str,
    family: str,
    label: str,
    link: str,
    axis: str,
    status: str,
    root: bool,
    root_label: str,
    display: NodePresentation,
) -> GraphNode:
    """Return the fields shared by every research-product graph node."""
    return {
        "id": identifier,
        "category": "product",
        "category_label": display.category_title,
        "shape": display.shape,
        "marker": display.marker,
        "kind": kind,
        "family": family,
        "label": label,
        "link": link,
        "status_axis": axis,
        "status": status,
        "root": root,
        "root_label": root_label,
    }


def record_statement(record: Mapping[str, Any], identifier: str, records: Records) -> str:
    """Return the sentence that states a research product for a graph card."""
    kind = str(record.get("type") or "")
    if kind == "problem" and record.get("statement"):
        sentences = re.split(r"(?<=[.!?])\s+", str(record["statement"]).strip())
        return sentences[-1]
    if kind == "question" and record.get("statement"):
        statement = str(record["statement"]).strip()
        question, separator, _rest = statement.partition("?")
        return f"{question}?" if separator else statement
    if kind == "answer" and isinstance(record.get("claim"), Mapping):
        reading = record["claim"].get("reading")
        if reading:
            return str(reading)
    if kind == "assessment":
        label = _assessment_statement(record, identifier, records)
        if label:
            return label
    return str(record.get("title") or identifier)


def card_title(label: str) -> str:
    """Return a graph-card title without terminal sentence periods."""
    return label.rstrip().rstrip(".").rstrip()


def record_link(identifier: str) -> str:
    """Return the Ekphrasis URI that opens one authored record by identifier."""
    return f"obsidian://ekphrasis?id={quote(identifier, safe='')}"


def status_axis(kind: str) -> str:
    """Return the semantic axis of a record's top-level status value."""
    return {
        "problem": "Problem status",
        "question": "Question status",
        "answer": "Attitude",
        "assessment": "Maturity",
    }.get(kind, "Maturity")


def _assessment_statement(record: Mapping[str, Any], identifier: str, records: Records) -> str:
    """Return the summarized test verdicts of one assessment."""
    verdicts = Counter(
        str(test.get("verdict"))
        for group in (record.get("tests") or {}).values()
        if isinstance(group, Mapping)
        for test in group.values()
        if isinstance(test, Mapping) and test.get("verdict")
    )
    if not verdicts:
        return ""
    outcomes = [
        f"{count} {word} {'test' if count == 1 else 'tests'}"
        for verdict, word in (
            ("fail", "failed"),
            ("pending", "pending"),
            ("inconclusive", "inconclusive"),
            ("pass", "passed"),
        )
        if (count := verdicts[verdict])
    ]
    assessed = str(record.get("assesses") or "")
    answer = records.get(assessed) or {}
    target = str(answer.get("title") or assessed or identifier)
    return f"The assessment records {_joined(outcomes)} for {target}."


def _joined(items: list[str]) -> str:
    """Return a grammatical enumeration of non-empty phrases."""
    if len(items) < 2:
        return "".join(items)
    if len(items) == 2:
        return " and ".join(items)
    return f"{', '.join(items[:-1])}, and {items[-1]}"
