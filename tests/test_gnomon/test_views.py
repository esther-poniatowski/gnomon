"""The question tree generated from the records of a project."""

from __future__ import annotations

import datetime
import doctest
import json
from pathlib import Path
from typing import Any

import pytest
import yaml
from jsonschema import Draft202012Validator
from referencing import Registry, Resource
from typer.testing import CliRunner

import gnomon.stages
import gnomon.views
from gnomon.cli import app
from gnomon.completeness import validation_scopes
from gnomon.source_state import source_state
from gnomon.view_coverage import attach_view_coverage
from gnomon.view_routes import view_routes
from gnomon.views import question_tree, render_tree

from .paths import EXAMPLES

RECORDS: dict[str, dict[str, Any]] = {
    "prob.geometry.readout": {
        "type": "problem",
        "title": "Readout",
        "statement": (
            "The readout changes with geometry. "
            "The geometry that permits a readout is not yet identified."
        ),
        "status": "posed",
    },
    "quest.geometry.capacity": {
        "type": "question",
        "addresses": "prob.geometry.readout",
        "statement": (
            "Which geometry permits the required readout? "
            "The answer must state the capacity of the readout."
        ),
        "status": "posed",
    },
    "quest.geometry.dimension": {
        "type": "question",
        "addresses": "prob.geometry.readout",
        "links": [{"question": "quest.geometry.capacity", "relation": "subquestion-of"}],
    },
    "quest.geometry.loose": {"type": "question"},
    "ans.geometry.kernel": {
        "type": "answer",
        "answers": "quest.geometry.capacity",
        "status": "entertained",
    },
    "assess.geometry.kernel": {
        "type": "assessment",
        "assesses": "ans.geometry.kernel",
        "tests": {
            "warrant": {
                "closure": {"verdict": "fail"},
                "fidelity": {"verdict": "pass"},
            }
        },
    },
    "design.geometry.sweep": {"type": "design", "serves": "quest.geometry.capacity"},
    "design.geometry.method": {"type": "design", "serves": "prob.geometry.readout"},
}


def test_a_problem_governs_its_questions_and_a_question_its_subquestions_answers_and_designs() -> (
    None
):
    assert render_tree(question_tree(RECORDS)) == (
        "problem prob.geometry.readout: Readout [posed]\n"
        "  question quest.geometry.capacity [posed]\n"
        "    question quest.geometry.dimension\n"
        "    answer ans.geometry.kernel [entertained]\n"
        "      assessment assess.geometry.kernel\n"
        "    design design.geometry.sweep\n"
        "  design design.geometry.method\n"
        "question quest.geometry.loose\n"
    )


def test_a_subquestion_of_an_absent_question_forms_a_root() -> None:
    records = {
        "quest.a.b": {
            "type": "question",
            "links": [{"question": "quest.a.absent", "relation": "subquestion-of"}],
        }
    }
    assert render_tree(question_tree(records)) == "question quest.a.b\n"


def test_questions_on_a_cycle_of_links_appear_once() -> None:
    records = {
        "quest.a.b": {
            "type": "question",
            "links": [{"question": "quest.a.c", "relation": "subquestion-of"}],
        },
        "quest.a.c": {
            "type": "question",
            "links": [{"question": "quest.a.b", "relation": "subquestion-of"}],
        },
    }
    text = render_tree(question_tree(records))
    assert text == "question quest.a.b\n  question quest.a.c\n"


def test_an_empty_project_yields_an_empty_tree() -> None:
    assert render_tree(question_tree({})) == ""


def test_the_command_prints_the_tree_of_a_directory_read_recursively(
    tmp_path: Path,
) -> None:
    (tmp_path / "sub").mkdir()
    for key, record in RECORDS.items():
        (tmp_path / "sub" / f"{key}.yml").write_text(
            yaml.safe_dump({"id": key, **record}), encoding="utf-8"
        )
    result = CliRunner().invoke(app, ["tree", str(tmp_path)])
    assert result.exit_code == 0
    assert result.output == render_tree(question_tree(RECORDS))


def test_the_question_tree_maps_research_fields_to_generic_tree_roles() -> None:
    """Gnomon owns the operational nodes; the schema alone maps them to renderer roles."""
    view = gnomon.views.question_tree_view(RECORDS)
    schema = _view_schema("question-tree", 3)
    nodes = schema["properties"]["nodes"]
    properties = nodes["items"]["properties"]

    assert view["_schema"] == "gnomon:view.question-tree@3"
    assert nodes["x-kind"] == "tree"
    assert nodes["title"] == "Inquiry hierarchy"
    assert schema["properties"]["edges"]["x-collapsed"] is True
    assert {name: field.get("x-tree-role") for name, field in properties.items()} == {
        "id": "identifier",
        "kind": "detail",
        "title": "label",
        "status": "detail",
        "depth": "depth",
    }
    retained = _view_schema("question-tree", 2)
    assert retained["properties"]["nodes"]["x-kind"] == "table"
    assert not any(
        "x-tree-role" in field
        for field in retained["properties"]["nodes"]["items"]["properties"].values()
    )


def test_the_inquiry_graph_connects_products_through_typed_activities() -> None:
    records = {
        **RECORDS,
        "itin.geometry.readout": {
            "type": "itinerary",
            "addresses": "prob.geometry.readout",
            "steps": [
                {
                    "id": "pose",
                    "activity": "problematization",
                    "inputs": [{"type": "source", "ref": "paper:readout"}],
                    "output": {
                        "type": "problem",
                        "ref": "prob.geometry.readout",
                    },
                    "norm": {"verdict": "pass"},
                    "rationale": {"serves": "prob.geometry.readout"},
                },
                {
                    "id": "propose",
                    "activity": "abduction",
                    "inputs": [
                        {
                            "type": "problem",
                            "ref": "itin.geometry.readout.pose",
                        }
                    ],
                    "output": {
                        "type": "target-claim",
                        "ref": "ans.geometry.kernel",
                    },
                    "norm": {"verdict": "pending"},
                    "rationale": {"serves": "quest.geometry.capacity"},
                },
            ],
        },
    }

    view = gnomon.views.inquiry_graph_view(records)
    graph = view["graph"]
    presentation = graph["presentation"]
    nodes = {node["id"]: node for node in graph["nodes"]}
    edges = {
        (edge["source"], edge["target"], edge["kind"], edge["label"]) for edge in graph["edges"]
    }

    assert view["_schema"] == "gnomon:view.inquiry-graph@1"
    assert presentation["profile"] == "gnomon-operational"
    assert presentation["layouts"]["recommended"] == "layered-directed"
    assert {item["id"] for item in presentation["node_kinds"]} >= {
        "problem",
        "question",
        "answer",
        "assessment",
    }
    assert {item["layer"] for item in presentation["edge_kinds"]} == {
        "assembly",
        "citation",
        "dependency",
        "exposure",
        "inquiry",
        "provenance",
        "state-origin",
    }
    assert nodes["prob.geometry.readout"]["root"] is True
    assert {
        nodes[identifier]["marker"]
        for identifier in (
            "prob.geometry.readout",
            "quest.geometry.capacity",
            "ans.geometry.kernel",
            "assess.geometry.kernel",
        )
    } == {"!", "?", "✦", "⚖"}
    assert {
        nodes[identifier]["shape"]
        for identifier in (
            "prob.geometry.readout",
            "quest.geometry.capacity",
            "ans.geometry.kernel",
            "assess.geometry.kernel",
        )
    } == {"rectangle"}
    assert nodes["itin.geometry.readout.pose"] == {
        "id": "itin.geometry.readout.pose",
        "category": "activity",
        "category_label": "Research activity",
        "shape": "capsule",
        "marker": "⚙",
        "kind": "problematization",
        "family": "problem-posing",
        "label": "Produces a problem",
        "link": "",
        "status_axis": "Norm verdict",
        "status": "pass",
        "root": False,
        "root_label": "",
    }
    assert len([node for node in graph["nodes"] if node["id"] == "ans.geometry.kernel"]) == 1
    source = next(node["id"] for node in graph["nodes"] if node["category"] == "source")
    assert (
        source,
        "itin.geometry.readout.pose",
        "takes",
        "input",
    ) in edges
    assert (
        "itin.geometry.readout.pose",
        "prob.geometry.readout",
        "produces",
        "output",
    ) in edges
    assert (
        "prob.geometry.readout",
        "itin.geometry.readout.propose",
        "takes",
        "input",
    ) in edges
    assert nodes["prob.geometry.readout"]["label"] == (
        "The geometry that permits a readout is not yet identified"
    )
    assert nodes["quest.geometry.capacity"]["label"] == (
        "Which geometry permits the required readout?"
    )
    assert nodes["assess.geometry.kernel"]["label"] == (
        "The assessment records 1 failed test and 1 passed test for ans.geometry.kernel"
    )
    assert nodes["prob.geometry.readout"]["link"] == (
        "obsidian://ekphrasis?id=prob.geometry.readout"
    )
    assert not [edge for edge in graph["edges"] if edge["label"] == "served by activity"]
    assert (
        "prob.geometry.readout",
        "quest.geometry.capacity",
        "addresses",
        "addressed by",
    ) in edges
    presentation_schema = _view_component("graph-presentation")
    registry = Registry().with_resource(
        presentation_schema["$id"], Resource.from_contents(presentation_schema)
    )
    assert not list(
        Draft202012Validator(_view_schema("inquiry-graph"), registry=registry).iter_errors(view)
    )


def test_the_inquiry_graph_schema_declares_every_generic_graph_role() -> None:
    schema = _view_schema("inquiry-graph")
    graph = schema["properties"]["graph"]
    nodes = graph["properties"]["nodes"]
    edges = graph["properties"]["edges"]

    assert graph["x-kind"] == "graph"
    assert graph["properties"]["presentation"]["x-graph-role"] == "presentation"
    assert nodes["x-graph-role"] == "nodes"
    assert edges["x-graph-role"] == "edges"
    assert {field["x-graph-role"] for field in nodes["items"]["properties"].values()} == {
        "node-id",
        "node-category",
        "node-category-label",
        "node-shape",
        "node-marker",
        "node-kind",
        "node-family",
        "node-label",
        "node-link",
        "node-status-axis",
        "node-status",
        "node-root",
        "node-root-label",
    }
    assert {field["x-graph-role"] for field in edges["items"]["properties"].values()} == {
        "edge-source",
        "edge-target",
        "edge-kind",
        "edge-label",
    }


def test_the_graph_presentation_contract_rejects_executable_icon_text() -> None:
    contract = gnomon.views.inquiry_graph_view(RECORDS)["graph"]["presentation"]
    problem = next(item for item in contract["node_kinds"] if item["id"] == "problem")
    problem["icon"] = "<script>unsafe</script>"
    schema = _view_component("graph-presentation")

    errors = list(Draft202012Validator(schema).iter_errors(contract))

    assert [error.json_path for error in errors] == ["$.node_kinds[0].icon"]


def test_the_inquiry_graph_reuses_a_source_and_keeps_each_unrecorded_output() -> None:
    records = {
        "itin.a": {
            "type": "itinerary",
            "steps": [
                {
                    "id": name,
                    "activity": "question-formulation",
                    "inputs": [{"type": "source", "ref": "paper:a"}],
                    "output": {"type": "question-schema"},
                    "norm": {"verdict": "pending"},
                }
                for name in ("first", "second")
            ],
        }
    }

    graph = gnomon.views.inquiry_graph_view(records)["graph"]

    assert len([node for node in graph["nodes"] if node["category"] == "source"]) == 1
    assert {node["id"] for node in graph["nodes"] if node["status"] == "unrecorded"} == {
        "product:itin.a.first",
        "product:itin.a.second",
    }


def test_a_question_schema_uses_its_realized_question_as_its_title_and_link() -> None:
    records: dict[str, dict[str, Any]] = {
        "quest.a": {
            "type": "question",
            "statement": "How does the system change? A model must explain the change.",
        },
        "itin.a": {
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

    graph = gnomon.views.inquiry_graph_view(records)["graph"]
    nodes = {node["id"]: node for node in graph["nodes"]}
    schema = nodes["product:itin.a.formulate"]

    assert schema["kind"] == "question-schema"
    assert schema["label"] == "How does the system change?"
    assert schema["link"] == "obsidian://ekphrasis?id=quest.a"
    assert nodes["itin.a.formulate"]["label"] == "Produces a question schema"
    assert not [node["id"] for node in graph["nodes"] if node["label"].endswith(".")]


def test_the_examples_of_the_module_hold() -> None:
    assert doctest.testmod(gnomon.views).failed == 0


def test_the_source_state_is_canonical_and_changes_with_an_authored_record() -> None:
    """Mapping order leaves the digest fixed, while a record value changes it."""
    first = {
        "prob.a": {"type": "problem", "status": "posed"},
        "quest.a": {"type": "question", "addresses": "prob.a"},
    }
    reordered = {
        "quest.a": {"addresses": "prob.a", "type": "question"},
        "prob.a": {"status": "posed", "type": "problem"},
    }
    changed = {**first, "prob.a": {**first["prob.a"], "status": "refined"}}

    state = source_state(first)

    assert state.startswith("sha256:") and len(state) == 71
    assert source_state(reordered) == state
    assert source_state(changed) != state


def test_the_source_state_distinguishes_a_yaml_date_from_quoted_text() -> None:
    """An invalid YAML date must remain hashable without becoming its quoted text equivalent."""
    parsed = {"prob.a": {"judged": datetime.date(2026, 10, 27)}}
    quoted = {"prob.a": {"judged": "2026-10-27"}}
    assert source_state(parsed) != source_state(quoted)
    assert source_state(parsed) == source_state(parsed)


def test_the_source_state_command_publishes_the_digest_used_by_views(
    tmp_path: Path,
) -> None:
    """A consumer obtains freshness state from Gnomon instead of reimplementing serialization."""
    inquiry = EXAMPLES / "grokking-delayed-generalization"
    runner = CliRunner()
    state_result = runner.invoke(app, ["source-state", str(inquiry)])
    target = tmp_path / "views"
    views_result = runner.invoke(app, ["views", str(inquiry), "--output", str(target)])

    assert state_result.exit_code == 0
    assert views_result.exit_code == 0
    view = yaml.safe_load((target / "problem-state.yml").read_text(encoding="utf-8"))
    assert state_result.stdout.strip() == view["source_state"]


def test_the_source_state_command_prints_no_digest_after_a_read_failure(
    tmp_path: Path,
) -> None:
    """A partial workspace must not produce an identifier that a consumer treats as current."""
    broken = tmp_path / "broken.yml"
    broken.write_text("id: [", encoding="utf-8")

    result = CliRunner().invoke(app, ["source-state", str(tmp_path)])

    assert result.exit_code == 1
    assert result.stdout == ""
    assert str(broken) in result.stderr


def test_every_validation_scope_has_one_primary_view_route() -> None:
    """A new completion target cannot enter the method without a view decision."""
    assert tuple(view_routes()) == validation_scopes()


@pytest.mark.parametrize(
    ("scope", "view"),
    [
        ("problem-posed", "problem-state"),
        ("question-typed", "next-act"),
        ("subject-identified", "next-act"),
        ("subject-specified", "next-act"),
        ("candidate-proposed", "exposure"),
        ("candidate-assessed", "problem-state"),
    ],
)
def test_a_named_scope_writes_only_its_primary_view(tmp_path: Path, scope: str, view: str) -> None:
    """Each completed stage exposes the view for its associated research task."""
    target = tmp_path / scope

    result = CliRunner().invoke(
        app,
        [
            "views",
            str(EXAMPLES / "grokking-delayed-generalization"),
            "--scope",
            scope,
            "--output",
            str(target),
        ],
    )

    assert result.exit_code == 0
    assert sorted(path.stem for path in target.glob("*.yml")) == [view]
    assert f"{scope}: open {target / f'{view}.yml'} to " in result.stdout
    document = yaml.safe_load((target / f"{view}.yml").read_text(encoding="utf-8"))
    assert document["coverage"]["scope"] == scope
    assert list(document).index("coverage") == list(document).index("source_state") + 1
    schema = yaml.safe_load(
        (
            Path(__file__).resolve().parents[2] / f"src/gnomon/data/schemas/views/{view}.schema.yml"
        ).read_text(encoding="utf-8")
    )
    assert schema["properties"]["coverage"]["$ref"].endswith(
        "/schemas/views/components/coverage.schema.yml"
    )
    coverage_schema = yaml.safe_load(
        (
            Path(__file__).resolve().parents[2]
            / "src/gnomon/data/schemas/views/components/coverage.schema.yml"
        ).read_text(encoding="utf-8")
    )
    registry = Registry().with_resource(
        coverage_schema["$id"], Resource.from_contents(coverage_schema)
    )
    if view == "exposure":
        presentation_schema = _view_component("graph-presentation")
        registry = registry.with_resource(
            presentation_schema["$id"], Resource.from_contents(presentation_schema)
        )
    assert not list(Draft202012Validator(schema, registry=registry).iter_errors(document))
    if view == "problem-state":
        retained_schema = yaml.safe_load(
            (
                Path(__file__).resolve().parents[2]
                / "src/gnomon/data/schemas/views/compatibility/problem-state.v2.schema.yml"
            ).read_text(encoding="utf-8")
        )
        retained_document = {**document, "_schema": "gnomon:view.problem-state@2"}
        retained_errors = [
            error.message
            for error in Draft202012Validator(retained_schema).iter_errors(retained_document)
        ]
        assert retained_errors == [
            "Additional properties are not allowed ('coverage' was unexpected)"
        ]


def test_a_named_scope_can_report_its_primary_view_as_json(tmp_path: Path) -> None:
    """A renderer receives the selected path without reproducing the scope-to-view route."""
    target = tmp_path / "views"

    result = CliRunner().invoke(
        app,
        [
            "views",
            str(EXAMPLES / "grokking-delayed-generalization"),
            "--scope",
            "candidate-proposed",
            "--output",
            str(target),
            "--result",
            "json",
        ],
    )

    assert result.exit_code == 0
    assert json.loads(result.stdout) == {
        "path": str(target / "exposure.yml"),
        "target": "candidate-proposed",
        "purpose": "inspect the candidate's revisable units and their dependencies",
    }


def test_a_json_view_result_requires_one_selected_scope(tmp_path: Path) -> None:
    result = CliRunner().invoke(
        app,
        [
            "views",
            str(EXAMPLES / "grokking-delayed-generalization"),
            "--output",
            str(tmp_path / "views"),
            "--result",
            "json",
        ],
    )

    assert result.exit_code == 2
    assert "requires --scope" in result.stderr


def test_a_selected_view_names_its_authored_records_and_absent_later_kinds(
    tmp_path: Path,
) -> None:
    """Coverage separates the records read now from record kinds due after the selected target."""
    inquiry = tmp_path / "inquiry"
    inquiry.mkdir()
    (inquiry / "problem.yml").write_text(
        yaml.safe_dump({"id": "prob.a", "type": "problem"}), encoding="utf-8"
    )
    target = tmp_path / "views"

    result = CliRunner().invoke(
        app,
        [
            "views",
            str(inquiry),
            "--scope",
            "problem-posed",
            "--output",
            str(target),
        ],
    )

    assert result.exit_code == 0
    document = yaml.safe_load((target / "problem-state.yml").read_text(encoding="utf-8"))
    assert document["coverage"] == {
        "scope": "problem-posed",
        "authored_records": [{"record": "prob.a", "kind": "problem"}],
        "later_record_kinds": [
            {
                "due_scope": "question-typed",
                "kind": "question",
                "expected_file": "question.yml",
            },
            {
                "due_scope": "subject-identified",
                "kind": "phenomenon",
                "expected_file": "phenomenon.yml",
            },
            {
                "due_scope": "subject-identified",
                "kind": "target-system",
                "expected_file": "target-system.yml",
            },
            {
                "due_scope": "candidate-proposed",
                "kind": "answer",
                "expected_file": "answer.yml",
            },
        ],
    }


def test_coverage_requires_the_shared_view_header() -> None:
    """Coverage cannot be placed predictably when the source-state header is absent."""
    with pytest.raises(ValueError, match="must carry source_state"):
        attach_view_coverage(
            {"_schema": "gnomon:view.problem-state@3"},
            {
                "scope": "problem-posed",
                "authored_records": [],
                "later_record_kinds": [],
            },
        )


def test_an_unknown_view_scope_writes_nothing(tmp_path: Path) -> None:
    """A misspelled completion target must not leave a plausible generated artifact."""
    target = tmp_path / "views"

    result = CliRunner().invoke(
        app,
        [
            "views",
            str(EXAMPLES),
            "--scope",
            "draft",
            "--output",
            str(target),
        ],
    )

    assert result.exit_code == 1
    assert "unknown view scope 'draft'" in result.stderr
    assert not target.exists()


def test_the_next_act_view_separates_ready_choices_from_required_predecessors() -> None:
    """Each mapped activity appears as a current choice or behind its required inputs."""
    diagnosis = {
        "questions": [
            {
                "question": "quest.a",
                "routes": [
                    {
                        "route": "construction",
                        "conditions": [],
                        "open": [
                            {
                                "condition": "definiteness",
                                "acts": [
                                    {
                                        "activity": "explication",
                                        "ready": True,
                                        "conditional": True,
                                        "required_inputs": ["concept | problem"],
                                        "output_type": "concept",
                                        "produces_in": ["concept record"],
                                        "may_unblock": ["operationalization"],
                                    },
                                    {
                                        "activity": "operationalization",
                                        "ready": False,
                                        "missing": ["concept"],
                                        "required_inputs": ["concept"],
                                        "output_type": "measurement-procedure",
                                        "produces_in": [
                                            "partial: target-system.variables[].scale",
                                            "partial: target-system.variables[].expression",
                                        ],
                                        "may_unblock": [],
                                    },
                                ],
                            },
                            {
                                "condition": "soundness",
                                "acts": [
                                    {
                                        "activity": "derivation",
                                        "ready": True,
                                        "required_inputs": ["admitted-laws | model | target-claim"],
                                        "output_type": "consequence",
                                        "produces_in": [
                                            "answer.aim_block.model_properties",
                                            "assessment.obligations",
                                            "model.laws[].warrant=derived",
                                            "background.laws[].warrant=derived",
                                        ],
                                        "may_unblock": [],
                                    }
                                ],
                            },
                        ],
                        "refuted": [],
                    }
                ],
            }
        ]
    }

    view = gnomon.views.next_act(diagnosis, "sha256:" + "0" * 64)

    assert view["_schema"] == "gnomon:view.next-act@8"
    assert view["comparisons"] == []
    assert [group["condition"] for group in view["open_conditions"]] == [
        "definiteness",
        "soundness",
    ]
    assert view["open_conditions"][0]["ready_acts"] == [
        {
            "activity": "explication",
            "required_inputs": ["concept | problem"],
            "output_type": "concept",
            "produces_in": ["concept record"],
            "may_unblock": ["operationalization"],
            "conditional": True,
        }
    ]
    assert view["open_conditions"][0]["required_predecessors"] == [
        {
            "activity": "operationalization",
            "missing_inputs": ["concept"],
            "required_inputs": ["concept"],
            "output_type": "measurement-procedure",
            "produces_in": [
                "partial: target-system.variables[].scale",
                "partial: target-system.variables[].expression",
            ],
            "may_unblock": [],
        }
    ]
    assert view["open_conditions"][1]["ready_acts"] == [
        {
            "activity": "derivation",
            "required_inputs": ["admitted-laws | model | target-claim"],
            "output_type": "consequence",
            "produces_in": [
                "answer.aim_block.model_properties",
                "assessment.obligations",
                "model.laws[].warrant=derived",
                "background.laws[].warrant=derived",
            ],
            "may_unblock": [],
            "conditional": False,
        }
    ]
    assert view["open_conditions"][1]["required_predecessors"] == []


def _view_for_retained_contract(name: str, version: int, view: dict[str, Any]) -> dict[str, Any]:
    """Return the equivalent generated content under a retained view contract."""
    retained = {**view, "_schema": f"gnomon:view.{name}@{version}"}
    if name == "assembly" and version < 3:
        retained.pop("graph")
    if name == "exposure" and version < 6:
        retained.pop("graph")
    if name == "itinerary-progress" and version < 4:
        graph = retained.pop("graph")
        retained["steps"] = [
            {
                "itinerary": node["itinerary"],
                "step": node["step"],
                "activity": node["activity"],
                "verdict": node["verdict"],
                "output": node["output"],
                "state": node["state"] if node["state"] != "not-produced" else "sound",
            }
            for node in graph["nodes"]
            if node["category"] == "activity"
        ]
        retained["edges"] = [
            {
                "itinerary": edge["target"].rsplit(".", 1)[0],
                "from": edge["source"].rsplit(".", 1)[1],
                "to": edge["target"].rsplit(".", 1)[1],
            }
            for edge in graph["edges"]
            if edge["kind"] == "step-dependency"
        ]
    if name == "next-act" and version < 7:
        retained.pop("comparisons")
    if name == "next-act" and version < 6:
        retained["open_conditions"] = [
            {
                "question": group["question"],
                "route": group["route"],
                "condition": group["condition"],
                "required_predecessors": [
                    {
                        "activity": predecessor["activity"],
                        "inputs": "; ".join(predecessor["missing_inputs"]),
                    }
                    for predecessor in group["required_predecessors"]
                ],
                "ready_acts": [
                    {
                        "activity": act["activity"],
                        "conditional": act["conditional"],
                    }
                    for act in group["ready_acts"]
                ],
            }
            for group in retained["open_conditions"]
        ]
    if name == "next-act" and version < 5:
        groups = [
            {
                "question": group["question"],
                "route": group["route"],
                "condition": group["condition"],
                "acts": [
                    {
                        "activity": act["activity"],
                        "ready": True,
                        "missing": "",
                    }
                    for act in group["ready_acts"]
                ]
                + [
                    {
                        "activity": predecessor["activity"],
                        "ready": False,
                        "missing": predecessor["inputs"],
                    }
                    for predecessor in group["required_predecessors"]
                ],
            }
            for group in retained["open_conditions"]
        ]
        retained["open_conditions"] = groups
    if name == "next-act" and version < 4:
        groups = retained.pop("open_conditions")
        retained["acts"] = [
            {
                "question": group["question"],
                "route": group["route"],
                "condition": group["condition"],
                **act,
            }
            for group in groups
            for act in group["acts"]
        ]
    return retained


def test_every_view_of_the_worked_inquiries_follows_its_schema_and_is_stable(
    tmp_path: Path,
) -> None:
    """A renderer reads each view through its schema, and two runs write the same files."""
    root = Path(__file__).resolve().parents[2]
    schemas = root / "src/gnomon/data/schemas/views"
    registry = yaml.safe_load((root / "specs/schema-registry.yml").read_text(encoding="utf-8"))
    component_resources = []
    for path in (schemas / "components").glob("*.schema.yml"):
        component = yaml.safe_load(path.read_text(encoding="utf-8"))
        component_resources.append((component["$id"], Resource.from_contents(component)))
    resource_registry = Registry().with_resources(component_resources)
    runner = CliRunner()
    first, second = tmp_path / "a", tmp_path / "b"
    assert runner.invoke(app, ["views", str(EXAMPLES), "--output", str(first)]).exit_code == 0
    assert runner.invoke(app, ["views", str(EXAMPLES), "--output", str(second)]).exit_code == 0
    written = sorted(p.name for p in first.glob("*.yml"))
    assert written == sorted(
        p.name.replace(".schema", "")
        for p in schemas.glob("*.schema.yml")
        if p.name != "vocabulary.schema.yml"
    )
    for name in written:
        assert (first / name).read_text() == (second / name).read_text()
        view = yaml.safe_load((first / name).read_text())
        assert view["source_state"].startswith("sha256:")
        schema = yaml.safe_load((schemas / name.replace(".yml", ".schema.yml")).read_text())
        validator = Draft202012Validator(schema, registry=resource_registry)
        errors = [e.message for e in validator.iter_errors(view)]
        assert not errors, f"{name}: {errors}"
        family = view["_schema"].rsplit("@", 1)[0]
        assert registry["schemas"][view["_schema"]] == str(
            Path("src/gnomon/data/schemas/views") / name.replace(".yml", ".schema.yml")
        )
        missing_state = {**view}
        missing_state.pop("source_state")
        current_rejections = [e.message for e in validator.iter_errors(missing_state)]
        assert current_rejections == ["'source_state' is a required property"]
        retained = sorted(
            int(contract.rsplit("@", 1)[1])
            for contract in registry["schemas"]
            if contract.startswith(f"{family}@") and contract != view["_schema"]
        )
        if not retained:
            assert view["_schema"].endswith("@1"), f"{name}: no retained contract"
            continue
        stateless = None
        stateless_with_state = None
        for version in retained:
            retained_path = (
                schemas / "compatibility" / name.replace(".yml", f".v{version}.schema.yml")
            )
            assert registry["schemas"][f"{family}@{version}"] == str(
                retained_path.relative_to(root)
            )
            retained_schema = yaml.safe_load(retained_path.read_text(encoding="utf-8"))
            retained_view = _view_for_retained_contract(name.removesuffix(".yml"), version, view)
            if "source_state" not in retained_schema["properties"]:
                stateless = retained_schema
                stateless_with_state = {**retained_view}
                retained_view.pop("source_state")
            retained_errors = [
                e.message for e in Draft202012Validator(retained_schema).iter_errors(retained_view)
            ]
            assert not retained_errors, f"{name}@{version}: {retained_errors}"
        assert stateless is not None, f"{name}: no contract retained without source_state"
        assert stateless_with_state is not None
        assert "Additional properties are not allowed ('source_state' was unexpected)" in [
            e.message for e in Draft202012Validator(stateless).iter_errors(stateless_with_state)
        ]


#: The generated fields whose values are sentences, by view file, list and field, with the kind
#: that the current contract declares; the contract retained before the change declares a label.
SENTENCE_FIELDS = {
    ("exposure", "exposures", "reason"): "text",
    ("question-statements", "statements", "authored"): "markdown-line",
    ("question-statements", "statements", "composed"): "markdown-line",
}

#: The contract of each view retained from before its sentence fields left the kind label.
LABEL_PREDECESSORS = {"exposure": 3, "question-statements": 2}

#: The contract that introduced each sentence kind, before later independent transitions.
LABEL_SUCCESSORS = {"exposure": 4, "question-statements": None}


def _view_schema(name: str, version: int | None = None) -> dict[str, Any]:
    """Return the current schema of a view, or the retained schema of one version."""
    folder = Path(__file__).resolve().parents[2] / "src/gnomon/data/schemas/views"
    path = (
        folder / f"{name}.schema.yml"
        if version is None
        else folder / "compatibility" / f"{name}.v{version}.schema.yml"
    )
    loaded: dict[str, Any] = yaml.safe_load(path.read_text(encoding="utf-8"))
    return loaded


def _view_component(name: str) -> dict[str, Any]:
    """Return one shared component of a generated-view schema."""
    path = (
        Path(__file__).resolve().parents[2]
        / "src/gnomon/data/schemas/views/components"
        / f"{name}.schema.yml"
    )
    loaded: dict[str, Any] = yaml.safe_load(path.read_text(encoding="utf-8"))
    return loaded


def test_sentence_fields_change_kind_only_in_the_contract_that_introduces_them() -> None:
    """Each sentence-kind transition remains isolated from later contract changes."""
    for (name, rows, field), kind in SENTENCE_FIELDS.items():
        current = _view_schema(name)
        retained = _view_schema(name, LABEL_PREDECESSORS[name])
        current_item = current["properties"][rows]["items"]["properties"]
        retained_item = retained["properties"][rows]["items"]["properties"]
        assert current_item[field]["x-kind"] == kind
        assert retained_item[field]["x-kind"] == "label"
        family = current["properties"]["_schema"]["const"].rsplit("@", 1)[0]
        assert retained["properties"]["_schema"]["const"] == (
            f"{family}@{LABEL_PREDECESSORS[name]}"
        )
    for name, version in LABEL_PREDECESSORS.items():
        successor = _view_schema(name, LABEL_SUCCESSORS[name])
        retained = _view_schema(name, version)
        retained["$id"] = successor["$id"]
        retained["properties"]["_schema"] = successor["properties"]["_schema"]
        for (view, rows, field), kind in SENTENCE_FIELDS.items():
            if view == name:
                retained["properties"][rows]["items"]["properties"][field]["x-kind"] = kind
        if name == "exposure":
            retained["properties"]["exposures"]["items"]["properties"]["kind"]["enum"].append(
                "commitment"
            )
        assert retained == successor, name


def _multiword_labels(node: Any, value: Any, path: str) -> list[str]:
    """Return the path of each value of kind label that holds more than one word."""
    if isinstance(value, dict):
        return [
            found
            for key, child in value.items()
            if key in (node.get("properties") or {})
            for found in _multiword_labels(node["properties"][key], child, f"{path}.{key}")
        ]
    if isinstance(value, list) and isinstance(node.get("items"), dict):
        return [
            found for item in value for found in _multiword_labels(node["items"], item, f"{path}[]")
        ]
    if node.get("x-kind") == "label" and isinstance(value, str) and len(value.split()) > 1:
        return [path]
    return []


def test_no_generated_view_holds_several_words_in_a_label(tmp_path: Path) -> None:
    """A renderer reads a label as one word, so a sentence of a view never takes that kind; the
    retained contracts, which still declare the sentences as labels, show that the check fires.
    """
    assert (
        CliRunner().invoke(app, ["views", str(EXAMPLES), "--output", str(tmp_path)]).exit_code == 0
    )
    views = {p.stem: yaml.safe_load(p.read_text()) for p in tmp_path.glob("*.yml")}
    assert not [
        found
        for name, view in views.items()
        for found in _multiword_labels(_view_schema(name), view, name)
    ]
    retained = {
        found.rsplit(".", 1)[1]
        for name, version in LABEL_PREDECESSORS.items()
        for found in _multiword_labels(_view_schema(name, version), views[name], name)
    }
    assert retained == {field for _, _, field in SENTENCE_FIELDS}


def test_the_exposure_contract_admits_a_commitment_emitted_by_the_generator() -> None:
    """A decision product is an exposure kind, so the current view contract must admit it."""
    records = {
        "itin.a.i": {
            "type": "itinerary",
            "id": "itin.a.i",
            "steps": [
                {
                    "id": "build",
                    "activity": "model-assembly",
                    "output": {"ref": "mod.a.m"},
                    "norm": {"verdict": "pass"},
                }
            ],
        },
        "mod.a.m": {
            "type": "model",
            "id": "mod.a.m",
            "laws": [{"symbol": "law", "warrant": "posited"}],
        },
        "ans.a.b": {
            "type": "answer",
            "id": "ans.a.b",
            "grounds": [{"record": "mod.a.m.law"}],
        },
    }

    view = gnomon.views.exposure(records)

    assert view["exposures"][0]["kind"] == "commitment"
    presentation_schema = _view_component("graph-presentation")
    registry = Registry().with_resource(
        presentation_schema["$id"], Resource.from_contents(presentation_schema)
    )
    assert not list(
        Draft202012Validator(_view_schema("exposure"), registry=registry).iter_errors(view)
    )


def test_the_progress_of_an_itinerary_preserves_dependencies_and_marks_impeachment() -> None:
    records = {
        "itin.a.b": {
            "type": "itinerary",
            "steps": [
                {
                    "id": "late",
                    "activity": "testing",
                    "inputs": [{"ref": "itin.a.b.early"}],
                    "output": {"ref": "assess.a"},
                    "norm": {"verdict": "pending"},
                },
                {
                    "id": "early",
                    "activity": "derivation",
                    "inputs": [],
                    "output": {"ref": "mod.a"},
                    "norm": {"verdict": "fail"},
                },
            ],
        }
    }
    view = gnomon.views.itinerary_progress(
        records, impeached={"mod.a", "assess.a"}, conditional=set()
    )
    graph = view["graph"]
    nodes = {node["id"]: node for node in graph["nodes"]}
    assert nodes["itin.a.b.early"]["state"] == "impeached"
    assert nodes["itin.a.b.late"]["state"] == "impeached"
    assert graph["edges"] == [
        {
            "source": "itin.a.b.early",
            "target": "itin.a.b.late",
            "kind": "step-dependency",
            "label": "supplies",
        }
    ]


def test_the_progress_reports_the_stage_of_each_itinerary() -> None:
    view = gnomon.views.itinerary_progress(
        {
            "prob.a.b": {"type": "problem", "status": "posed"},
            "itin.a.b": {
                "type": "itinerary",
                "addresses": "prob.a.b",
                "steps": [{"id": "s", "output": {"ref": "mod.a"}, "norm": {"verdict": "pass"}}],
            },
        },
        impeached=set(),
        conditional=set(),
    )
    assert view["_schema"] == "gnomon:view.itinerary-progress@4"
    assert view["itineraries"] == [
        {"itinerary": "itin.a.b", "addresses": "prob.a.b", "stage": "in-progress"}
    ]


def test_an_itinerary_concludes_only_when_its_record_ends_and_every_act_is_judged() -> None:
    done = {"id": "done", "output": {"ref": "ans.a"}, "norm": {"verdict": "fail"}}
    waiting = {
        "id": "waiting",
        "output": {"ref": "ans.b"},
        "norm": {"verdict": "pending"},
    }
    branch = {"id": "branch", "norm": {"verdict": "pending"}}

    def stage(status: str, *steps: dict[str, Any]) -> str:
        records = {"quest.a": {"status": status}}
        itinerary = {"addresses": "quest.a", "steps": list(steps)}
        return gnomon.stages.itinerary_stage(itinerary, records)

    assert stage("answered", done, branch) == "concluded"
    assert stage("answered", done, waiting) == "in-progress"
    assert stage("posed", done) == "in-progress"
    assert stage("posed", branch) == "planned"
    assert stage("abandoned", done) == "abandoned"


def test_a_refined_problem_whose_demand_is_met_may_close(monkeypatch: Any) -> None:
    monkeypatch.setattr(gnomon.views, "demand_met", lambda *args: True)
    records = {
        f"prob.a.{status}": {"type": "problem", "status": status}
        for status in ("posed", "refined", "solved")
    }
    rows = {
        row["problem"]: row["may_close"] for row in gnomon.views.problem_state(records)["problems"]
    }
    assert rows == {
        "prob.a.posed": True,
        "prob.a.refined": True,
        "prob.a.solved": False,
    }
