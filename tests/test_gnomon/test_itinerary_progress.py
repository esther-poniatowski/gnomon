"""The itinerary-progress graph preserves dependency topology and locates state origins."""

from __future__ import annotations

from typing import Any

import yaml
from jsonschema import Draft202012Validator
from referencing import Registry, Resource

import gnomon.views

from .paths import ROOT


def _step(
    identifier: str,
    verdict: str,
    *,
    inputs: list[str] | None = None,
    output: str | None = None,
) -> dict[str, Any]:
    """Return one compact itinerary step for the graph cases."""
    step: dict[str, Any] = {
        "id": identifier,
        "activity": f"activity-{identifier}",
        "inputs": [{"ref": reference} for reference in inputs or []],
        "norm": {"verdict": verdict},
    }
    if output is not None:
        step["output"] = {"type": "result", "ref": output}
    return step


def test_progress_graph_preserves_branches_cycles_and_every_displayed_origin() -> None:
    records = {
        "itin.a": {
            "id": "itin.a",
            "type": "itinerary",
            "steps": [
                _step(
                    "join",
                    "pass",
                    inputs=["itin.a.failed", "out.waiting"],
                    output="out.join",
                ),
                _step("failed", "fail", output="out.failed"),
                _step("waiting", "pending", output="out.waiting"),
                _step("downstream", "pass", inputs=["out.waiting"], output="out.after"),
                _step("independent", "pass", output="out.independent"),
                _step("cycle-a", "pass", inputs=["itin.a.cycle-b"], output="out.a"),
                _step("cycle-b", "fail", inputs=["itin.a.cycle-a"], output="out.b"),
                _step("planned", "pending"),
            ],
        }
    }

    view = gnomon.views.itinerary_progress(
        records,
        impeached={"out.failed", "out.join", "out.a", "out.b"},
        conditional={"out.waiting", "out.after"},
    )
    graph = view["graph"]
    nodes = {node["id"]: node for node in graph["nodes"] if node["category"] == "activity"}
    edges = {(edge["source"], edge["target"], edge["kind"]) for edge in graph["edges"]}

    assert view["_schema"] == "gnomon:view.itinerary-progress@4"
    assert list(nodes) == [
        "itin.a.join",
        "itin.a.failed",
        "itin.a.waiting",
        "itin.a.downstream",
        "itin.a.independent",
        "itin.a.cycle-a",
        "itin.a.cycle-b",
        "itin.a.planned",
    ]
    assert {identifier: (node["state"], node["origins"]) for identifier, node in nodes.items()} == {
        "itin.a.join": ("impeached", ["itin.a.failed"]),
        "itin.a.failed": ("impeached", ["itin.a.failed"]),
        "itin.a.waiting": ("conditional", ["itin.a.waiting"]),
        "itin.a.downstream": ("conditional", ["itin.a.waiting"]),
        "itin.a.independent": ("sound", []),
        "itin.a.cycle-a": ("impeached", ["itin.a.cycle-b"]),
        "itin.a.cycle-b": ("impeached", ["itin.a.cycle-b"]),
        "itin.a.planned": ("not-produced", []),
    }
    assert {
        ("itin.a.failed", "itin.a.join", "step-dependency"),
        ("itin.a.waiting", "itin.a.join", "step-dependency"),
        ("itin.a.waiting", "itin.a.downstream", "step-dependency"),
        ("itin.a.cycle-b", "itin.a.cycle-a", "step-dependency"),
        ("itin.a.cycle-a", "itin.a.cycle-b", "step-dependency"),
    } <= edges
    assert nodes["itin.a.failed"]["status"] == "impeached · origin"
    assert nodes["itin.a.waiting"]["status"] == "conditional · origin"
    assert not [node["id"] for node in graph["nodes"] if node["root"]]


def test_progress_graph_marks_a_state_whose_origin_is_outside_the_displayed_steps() -> None:
    records = {
        "itin.external": {
            "id": "itin.external",
            "type": "itinerary",
            "steps": [_step("affected", "pass", inputs=["outside.failed"], output="out.affected")],
        }
    }

    view = gnomon.views.itinerary_progress(
        records,
        impeached={"outside.failed", "out.affected"},
        conditional=set(),
    )
    graph = view["graph"]
    affected = next(node for node in graph["nodes"] if node["id"] == "itin.external.affected")
    sources = [node for node in graph["nodes"] if node["category"] == "source"]

    assert affected["state"] == "impeached"
    assert affected["external_origin"] is True
    assert affected["status"] == "impeached · external origin"
    assert len(sources) == 1
    assert sources[0]["kind"] == "external-origin"
    assert sources[0]["root"] is False
    assert {(edge["source"], edge["target"], edge["kind"]) for edge in graph["edges"]} == {
        (sources[0]["id"], "itin.external.affected", "impeaches")
    }


def test_progress_graph_links_an_unrecorded_schema_to_its_realized_question() -> None:
    records: dict[str, dict[str, Any]] = {
        "quest.a": {"type": "question", "title": "Mechanism of the observed change."},
        "itin.a": {
            "id": "itin.a",
            "type": "itinerary",
            "steps": [
                {
                    "id": "formulate",
                    "activity": "question-formulation",
                    "output": {"type": "question-schema"},
                    "norm": {"verdict": "pass"},
                    "rationale": {"serves": "quest.a"},
                }
            ],
        },
    }

    graph = gnomon.views.itinerary_progress(records, impeached=set(), conditional=set())["graph"]
    schema = next(node for node in graph["nodes"] if node["id"] == "itin.a.formulate")

    assert schema["state"] == "sound"
    assert schema["label"] == "Produces Mechanism of the observed change"
    assert schema["link"] == "obsidian://ekphrasis?id=quest.a"


def test_current_contract_validates_the_graph_and_retains_the_tabular_predecessor() -> None:
    schema_root = ROOT / "src" / "gnomon" / "data" / "schemas" / "views"
    current = yaml.safe_load(
        (schema_root / "itinerary-progress.schema.yml").read_text(encoding="utf-8")
    )
    retained = yaml.safe_load(
        (schema_root / "compatibility" / "itinerary-progress.v3.schema.yml").read_text(
            encoding="utf-8"
        )
    )
    presentation = yaml.safe_load(
        (schema_root / "components" / "graph-presentation.schema.yml").read_text(encoding="utf-8")
    )
    registry = Registry().with_resource(presentation["$id"], Resource.from_contents(presentation))
    view = gnomon.views.itinerary_progress(
        {
            "itin.a": {
                "id": "itin.a",
                "type": "itinerary",
                "steps": [_step("done", "pass", output="out.done")],
            }
        },
        impeached=set(),
        conditional=set(),
    )

    assert not list(Draft202012Validator(current, registry=registry).iter_errors(view))
    assert current["properties"]["_schema"]["const"] == "gnomon:view.itinerary-progress@4"
    assert current["properties"]["graph"]["x-kind"] == "graph"
    assert retained["properties"]["_schema"]["const"] == "gnomon:view.itinerary-progress@3"
    assert retained["properties"]["steps"]["x-kind"] == "table"
