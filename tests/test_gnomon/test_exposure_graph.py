"""The exposure graph preserves answer-to-unit reachability without duplicating units."""

from __future__ import annotations

from typing import Any

from gnomon.exposure_graph import exposure_graph


def _records() -> dict[str, dict[str, Any]]:
    """Return two answers that share one revisable law."""
    return {
        "ans.example.first": {
            "id": "ans.example.first",
            "type": "answer",
            "title": "First answer.",
            "claim": {"reading": "The first account explains the effect."},
        },
        "ans.example.second": {
            "id": "ans.example.second",
            "type": "answer",
            "title": "Second answer.",
            "claim": {"reading": "The second account explains the effect."},
        },
        "mod.example.system": {
            "id": "mod.example.system",
            "type": "model",
            "title": "Example system",
        },
    }


def test_shared_exposure_is_one_linked_node_reached_by_both_answers() -> None:
    """A shared unit appears once while each affected answer retains its own edge."""
    graph = exposure_graph(
        _records(),
        [
            {
                "answer": "ans.example.first",
                "unit": "mod.example.system.response-law",
                "kind": "law",
                "reason": "posited",
                "via": "direct",
            },
            {
                "answer": "ans.example.second",
                "unit": "mod.example.system.response-law",
                "kind": "law",
                "reason": "measured",
                "via": "law mod.example.system.input-law",
            },
        ],
    )

    nodes = {node["id"]: node for node in graph["nodes"]}
    assert set(nodes) == {
        "ans.example.first",
        "ans.example.second",
        "mod.example.system.response-law",
    }
    assert nodes["ans.example.first"]["label"] == "The first account explains the effect"
    assert nodes["ans.example.first"]["link"].endswith("ans.example.first")
    assert nodes["mod.example.system.response-law"]["label"] == "Response law"
    assert nodes["mod.example.system.response-law"]["link"].endswith("mod.example.system")
    assert nodes["mod.example.system.response-law"]["kind"] == "law"
    assert {(edge["source"], edge["target"]) for edge in graph["edges"]} == {
        ("ans.example.first", "mod.example.system.response-law"),
        ("ans.example.second", "mod.example.system.response-law"),
    }


def test_duplicate_relations_aggregate_reasons_and_routes() -> None:
    """One answer-unit pair produces one edge without discarding distinct evidence."""
    graph = exposure_graph(
        _records(),
        [
            {
                "answer": "ans.example.first",
                "unit": "mod.example.system.response-law",
                "kind": "law",
                "reason": "posited",
                "via": "direct",
            },
            {
                "answer": "ans.example.first",
                "unit": "mod.example.system.response-law",
                "kind": "law",
                "reason": "warrant not stated",
                "via": "derivation derivation.example.route",
            },
        ],
    )

    assert graph["edges"] == [
        {
            "source": "ans.example.first",
            "target": "mod.example.system.response-law",
            "kind": "exposed-by",
            "label": "exposed by",
            "reasons": ["posited", "warrant not stated"],
            "vias": ["direct", "derivation derivation.example.route"],
        }
    ]
