"""Tests of the verdict `inconclusive`, of the subdomain `holds_on` of a failed test, and of the
exposure of the products of a generation or a decision."""

from __future__ import annotations

import shutil
from pathlib import Path
from typing import Any

import yaml

from gnomon.answerability import as_document, diagnose, itinerary_state, render_text
from gnomon.check import check_workspace, load_workspace
from gnomon.completeness import ground_verdict_findings
from gnomon.exposure import answer_exposure
from gnomon.source_state import source_state
from gnomon.stages import itinerary_stage
from gnomon.views import next_act

from .paths import EXAMPLES

GROKKING = EXAMPLES / "grokking-delayed-generalization"


def _itinerary(verdict: str) -> dict[str, Any]:
    return {
        "type": "itinerary",
        "id": "itin.a.i",
        "addresses": "prob.a.p",
        "steps": [
            {
                "id": "build",
                "activity": "model-assembly",
                "output": {"ref": "mod.a.m"},
                "norm": {"verdict": verdict},
            },
            {
                "id": "derive",
                "activity": "derivation",
                "inputs": [{"ref": "mod.a.m"}],
                "output": {"ref": "derivation.a.d"},
                "norm": {"verdict": "pass"},
            },
        ],
    }


def test_an_inconclusive_norm_makes_its_products_conditional_as_a_pending_one() -> None:
    for verdict in ("pending", "inconclusive"):
        impeached, conditional, _ = itinerary_state({"itin.a.i": _itinerary(verdict)})
        assert (impeached, conditional) == (set(), {"mod.a.m", "derivation.a.d"})


def test_an_inconclusive_norm_counts_as_judged_for_the_stage() -> None:
    records = {"prob.a.p": {"status": "solved"}}
    assert itinerary_stage(_itinerary("inconclusive"), records) == "concluded"
    assert itinerary_stage(_itinerary("pending"), records) == "in-progress"


def _narrowed() -> dict[str, dict[str, Any]]:
    return {
        "quest.a.q": {"type": "question", "id": "quest.a.q"},
        "ans.a.x": {"type": "answer", "id": "ans.a.x", "answers": "quest.a.q"},
        "asmt.a.x": {
            "type": "assessment",
            "id": "asmt.a.x",
            "assesses": "ans.a.x",
            "tests": {"warrant": {"fidelity": {"verdict": "fail", "holds_on": "g < 1"}}},
        },
    }


def test_a_failed_test_with_holds_on_proposes_a_scope_narrowing() -> None:
    diagnosis = diagnose(_narrowed())
    assert "narrow the scope of ans.a.x to g < 1" in render_text(diagnosis)
    rows = next_act(as_document(diagnosis), source_state(_narrowed()))["narrowings"]
    assert rows == [
        {
            "answer": "ans.a.x",
            "holds_on": "g < 1",
            "test": "tests.warrant.fidelity",
            "assessment": "asmt.a.x",
        }
    ]


def test_a_revising_answer_withdraws_the_narrowing() -> None:
    records = _narrowed()
    records["ans.a.y"] = {
        "type": "answer",
        "id": "ans.a.y",
        "answers": "quest.a.q",
        "relations": [{"relation": "revises", "target": "ans.a.x"}],
    }
    assert as_document(diagnose(records))["narrowings"] == []


def test_holds_on_is_checked_for_its_symbols_and_its_verdict(tmp_path: Path) -> None:
    folder = tmp_path / "grokking"
    shutil.copytree(GROKKING, folder)
    path = folder / "assessment.yml"
    assessment = yaml.safe_load(path.read_text(encoding="utf-8"))
    tests = assessment["tests"]["warrant"]
    failed = next(name for name, entry in tests.items() if entry.get("verdict") == "fail")
    tests[failed]["holds_on"] = "nosuchsymbol < 1"
    passed = next(name for name, entry in tests.items() if entry.get("verdict") == "pass")
    tests[passed]["holds_on"] = "lambda3 > 0"
    path.write_text(yaml.safe_dump(assessment, sort_keys=False), encoding="utf-8")
    rules = sorted(x.finding.rule.id for x in check_workspace(load_workspace(folder)))
    assert "completeness/misplaced-holds-on" in rules
    assert any(rule.startswith("vocabulary/") for rule in rules)


def test_the_product_of_a_decision_or_a_generation_is_exposed_first() -> None:
    records: dict[str, dict[str, Any]] = {
        "itin.a.i": _itinerary("pass"),
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
    found = answer_exposure(records, "ans.a.b")
    assert (found[0].unit, found[0].kind) == ("mod.a.m", "commitment")
    assert found[0].reason == "generation by model-assembly, step itin.a.i.build"
    assert ("mod.a.m.law", "law") in {(e.unit, e.kind) for e in found}


def _per_ground(**entry: Any) -> dict[str, dict[str, Any]]:
    """An answer resting on a computed law, an itinerary whose simulation obtained it, and an
    assessment that judges the ground of that law."""
    records: dict[str, dict[str, Any]] = {
        "mod.a.m": {
            "type": "model",
            "id": "mod.a.m",
            "laws": [{"symbol": "law", "warrant": "computed"}],
        },
        "ans.a.x": {
            "type": "answer",
            "id": "ans.a.x",
            "grounds": [{"id": "flow", "role": "warrant", "record": "mod.a.m.law"}],
        },
        "itin.a.i": {
            "type": "itinerary",
            "id": "itin.a.i",
            "steps": [
                {
                    "id": "simulate",
                    "activity": "simulation",
                    "norm": {"verdict": "pass"},
                }
            ],
        },
        "asmt.a.x": {
            "type": "assessment",
            "id": "asmt.a.x",
            "assesses": "ans.a.x",
            "tests": {"warrant": {"law-warrant": {"verdict": "pass"}}},
            "grounds": [
                {
                    "ground": "flow",
                    "verdict": "pass",
                    "step": "itin.a.i.simulate",
                    **entry,
                }
            ],
        },
    }
    return records


def _ground_rules(records: dict[str, dict[str, Any]]) -> list[str]:
    return [f.rule.id for f in ground_verdict_findings(records["asmt.a.x"], records)]


def test_a_ground_judged_on_the_step_of_its_computation_has_no_finding() -> None:
    assert _ground_rules(_per_ground()) == []


def test_an_unknown_ground_and_an_unknown_step_are_reported() -> None:
    assert _ground_rules(_per_ground(ground="nope", step="itin.a.i.none")) == [
        "completeness/mismatched-ground",
        "completeness/unknown-evidence-step",
        "completeness/untested-computed-law",
    ]


def test_a_pass_on_a_step_whose_norm_is_not_met_is_a_warning() -> None:
    records = _per_ground()
    records["itin.a.i"]["steps"][0]["norm"]["verdict"] = "inconclusive"
    assert _ground_rules(records) == ["completeness/unsettled-evidence"]


def test_the_test_of_law_warrant_agrees_with_the_verdicts_of_the_grounds() -> None:
    assert _ground_rules(_per_ground(verdict="fail")) == ["completeness/disagreeing-law-warrant"]
    records = _per_ground(verdict="fail", holds_on="g < 1")
    records["asmt.a.x"]["tests"]["warrant"]["law-warrant"]["verdict"] = "fail"
    assert _ground_rules(records) == []
    narrowing = as_document(diagnose(records))["narrowings"]
    assert [(n["answer"], n["test"], n["holds_on"]) for n in narrowing] == [
        ("ans.a.x", "grounds.flow", "g < 1")
    ]
