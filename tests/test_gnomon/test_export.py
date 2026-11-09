"""Tests of the export of a project: its units, the mapping of its relations onto the classes of the
contract, the closure of their ends, and the command `gnomon export`."""

from __future__ import annotations

import shutil
from pathlib import Path
from typing import Any

import yaml
from typer.testing import CliRunner

from gnomon.check import load_workspace
from gnomon.cli import app
from gnomon.completeness import VOCABULARY_REGISTRY
from gnomon.export import build_export, load_export_registry, render_export
from gnomon.relation_registry import load_relation_registry
from gnomon.schemas import load_base

from .paths import EXAMPLES

GROKKING = EXAMPLES / "grokking-delayed-generalization"


def _answer(name: str, **fields: Any) -> dict[str, Any]:
    return {"type": "answer", "id": f"ans.a.{name}", "status": "accepted", **fields}


def _records() -> dict[str, dict[str, Any]]:
    records: list[dict[str, Any]] = [
        {
            "type": "model",
            "id": "mod.a.m",
            "title": "model",
            "laws": [{"symbol": "flow", "reading": "the flow law"}],
            "operations": [{"id": "toy", "gain": "a tractable task"}],
        },
        {
            "type": "binding",
            "id": "bind.a.b",
            "feature_pairs": [{"id": "limit", "exemplified": "x > 0"}],
        },
        {"type": "concept", "id": "concept.a.c", "gloss": "a concept"},
        {"type": "concept", "id": "concept.a.d", "gloss": "a narrower", "broader": "concept.a.c"},
        {"type": "question", "id": "quest.a.q", "statement": "why?", "version": "2"},
        {
            "type": "question",
            "id": "quest.a.s",
            "statement": "how?",
            "links": [{"question": "quest.a.q", "relation": "subquestion-of"}],
        },
        _answer(
            "x",
            answers="quest.a.q",
            claim={"reading": "x holds"},
            grounds=[
                {"id": "law", "role": "warrant", "record": "mod.a.m.flow"},
                {"id": "pair", "role": "warrant", "record": "bind.a.b.limit"},
                {"id": "task", "role": "condition", "record": "mod.a.m.toy"},
                {"id": "ideal", "role": "idealization", "record": "mod.a.m.flow"},
                {"id": "lost", "role": "assumption", "record": "quest.a.q.restriction"},
            ],
            relations=[
                {"relation": "incompatible-with", "members": ["ans.a.z", "ans.a.y"]},
                {"relation": "contrasts-with", "target": "ans.a.y", "respect": ["eta"]},
                {"relation": "defeats", "target": "ans.a.z"},
                {"relation": "exemplifies", "target": "concept.a.c"},
            ],
        ),
        _answer("y", relations=[{"relation": "contrasts-with", "target": "ans.a.x"}]),
        _answer("z", status="retracted"),
        _answer("w", relations=[{"relation": "revises", "target": "ans.a.z"}]),
    ]
    return {str(r["id"]): r for r in records}


def _relations() -> list[dict[str, Any]]:
    export, _ = build_export(_records(), "demo")
    return list(export["relations"])


def test_a_ground_is_exported_from_the_ground_to_the_answer_by_its_role() -> None:
    support = {(r["source"], r["use"]) for r in _relations() if r["class"] == "support"}
    assert support == {("mod.a.m.flow", "warrant"), ("bind.a.b.limit", "warrant")}
    conditions = [r for r in _relations() if r["class"] == "condition"]
    assert [(r["id"], r["source"], r["target"]) for r in conditions] == [
        ("ans.a.x.task", "mod.a.m.toy", "ans.a.x")
    ]


def test_a_set_relation_names_its_sorted_members_once() -> None:
    sets = [r for r in _relations() if "members" in r]
    assert [(r["class"], r["members"], r["symmetric"]) for r in sets] == [
        ("incompatibility", ["ans.a.x", "ans.a.y", "ans.a.z"], True)
    ]


def test_a_symmetric_relation_stated_on_both_ends_is_exported_once() -> None:
    contrasts = [r for r in _relations() if r["class"] == "contrast"]
    assert [(r["source"], r["target"]) for r in contrasts] == [("ans.a.x", "ans.a.y")]


def test_classes_forms_and_omissions_follow_the_registry() -> None:
    by_relation = {r["relation"]: r for r in _relations()}
    assert "defeats" not in by_relation
    assert by_relation["subquestion-of"]["form"] == "whole-part"
    assert by_relation["broader"]["form"] == "generalization-specific"
    assert by_relation["exemplifies"]["class"] == "instance"
    assert (by_relation["answers"]["source"], by_relation["answers"]["target"]) == (
        "quest.a.q",
        "ans.a.x",
    )


def test_a_relation_with_an_end_that_is_no_unit_is_dropped_and_reported() -> None:
    export, dropped = build_export(_records(), "demo")
    assert dropped == ["ans.a.x.lost"]
    units = {u["id"] for u in export["units"]}
    for relation in export["relations"]:
        assert set(relation.get("members") or [relation["source"], relation["target"]]) <= units


def test_units_carry_the_lists_of_a_record_and_its_supersession() -> None:
    export, _ = build_export(_records(), "demo")
    units = {u["id"]: u for u in export["units"]}
    assert "bind.a.b" not in units and units["bind.a.b.limit"]["kind"] == "feature-pair"
    assert units["mod.a.m.toy"]["statement"] == "a tractable task"
    assert units["ans.a.z"]["superseded_by"] == ["ans.a.w"]
    assert units["quest.a.q"]["version"] == "2"


def test_two_runs_write_the_same_bytes() -> None:
    first = render_export(build_export(_records(), "demo")[0])
    assert first == render_export(build_export(_records(), "demo")[0])


def test_every_path_of_the_export_registry_is_a_field_of_its_record() -> None:
    def has(schema: dict[str, Any], path: str) -> bool:
        node: Any = schema
        for key in path.split("."):
            node = (node.get("properties") or {}).get(key)
            if node is None:
                return False
            node = node.get("items", node)
        return True

    registry = load_export_registry()
    for kind, declared in registry["records"].items():
        assert has(load_base(kind), declared["statement"]), (kind, declared)
    for kind, lists in registry["units"].items():
        base = load_base(kind)
        for spec in lists:
            assert has(base, spec["list"]), (kind, spec)
            assert has(base, f"{spec['list']}.{spec['key']}"), (kind, spec)
            source = spec["via"]["list"] if "via" in spec else spec["list"]
            assert has(base, f"{source}.{spec['statement']}"), (kind, spec)


def test_a_mapped_use_names_a_value_of_its_key() -> None:
    fields = load_relation_registry()["fields"]["answer"]["grounds[].record"]
    vocabularies = yaml.safe_load(VOCABULARY_REGISTRY.read_text(encoding="utf-8"))
    admitted = {str(v["value"]) for v in vocabularies["vocabularies"]["answer"]["grounds.role"]}
    assert set(fields["export"]) <= admitted


def _workspace(tmp_path: Path) -> Path:
    shutil.copytree(GROKKING, tmp_path / "grokking")
    (tmp_path / "repository.yml").write_text("schema_version: 1\nrepository:\n  id: demo\n")
    return tmp_path / "grokking"


def test_the_command_writes_a_current_export_that_no_check_reads(tmp_path: Path) -> None:
    folder = _workspace(tmp_path)
    runner = CliRunner()
    assert runner.invoke(app, ["export", str(folder)]).exit_code == 0
    written = yaml.safe_load((folder / "export.yml").read_text())
    assert (written["id"], written["findings_overridden"]) == ("export.demo", False)
    assert runner.invoke(app, ["export", str(folder), "--check"]).exit_code == 0
    assert "export.demo" not in load_workspace(folder).by_id
    (folder / "export.yml").write_text("# stale\n")
    assert runner.invoke(app, ["export", str(folder), "--check"]).exit_code == 1


def test_the_command_needs_a_repository_and_refuses_failing_records(tmp_path: Path) -> None:
    runner = CliRunner()
    shutil.copytree(GROKKING, tmp_path / "bare")
    assert runner.invoke(app, ["export", str(tmp_path / "bare")]).exit_code == 1
    folder = _workspace(tmp_path / "with")
    answer = folder / "answer.yml"
    answer.write_text(answer.read_text().replace("status: hypothesized", "status: guessed", 1))
    assert runner.invoke(app, ["export", str(folder)]).exit_code == 1
    assert not (folder / "export.yml").exists()
    assert runner.invoke(app, ["export", str(folder), "--allow-findings"]).exit_code == 0
    assert yaml.safe_load((folder / "export.yml").read_text())["findings_overridden"] is True


def test_a_condition_ground_citing_a_restriction_is_exported() -> None:
    records = _records()
    records["quest.a.q"]["subject"] = {
        "domain": {"restrictions": [{"id": "gain", "name": "a gain below one"}]}
    }
    records["ans.a.x"]["grounds"][4] = {
        "id": "lost",
        "role": "condition",
        "record": "quest.a.q.gain",
    }
    export, dropped = build_export(records, "demo")
    assert dropped == []
    units = {u["id"]: u for u in export["units"]}
    assert units["quest.a.q.gain"]["kind"] == "restriction"
    conditions = {
        (r["source"], r["target"]) for r in export["relations"] if r["class"] == "condition"
    }
    assert ("quest.a.q.gain", "ans.a.x") in conditions
