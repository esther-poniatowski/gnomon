"""The version of a question, which each assessment of an answer names.

A revision of a question raises its version, so an assessment that names an earlier version is
reported void, and a void assessment settles no demand. Each case is shown on a planted defect, and
the worked inquiries, all at their first version, report none.
"""

from __future__ import annotations

import shutil
from pathlib import Path
from typing import Any

from gnomon.check import check_workspace, load_workspace
from gnomon.completeness import (
    demand_met,
    is_void,
    misversioned_assessment,
    unrecorded_question_revision,
)
from gnomon.itineraries import itinerary_problems

from .paths import EXAMPLES

QUESTION = {"id": "quest.a.q", "type": "question", "version": "2", "addresses": "prob.a.p"}
ANSWER = {
    "id": "ans.a.x",
    "type": "answer",
    "answers": "quest.a.q",
    "status": "accepted",
    "erotetic_relation": {"value": "complete"},
}
RECORDS: dict[str, dict[str, Any]] = {"quest.a.q": QUESTION, "ans.a.x": ANSWER}


def _assessment(**fields: Any) -> dict[str, Any]:
    return {"type": "assessment", "assesses": "ans.a.x", "against": "quest.a.q", **fields}


def _rules(assessment: dict[str, Any]) -> list[str]:
    return [f.rule.id for f in misversioned_assessment(assessment, RECORDS)]


def test_an_assessment_of_an_earlier_version_is_void() -> None:
    assert _rules(_assessment(against_version="1")) == ["completeness/void-assessment"]
    assert is_void(_assessment(against_version="1"), RECORDS)
    assert not is_void(_assessment(against_version="2"), RECORDS)


def test_a_later_or_a_missing_version_is_reported() -> None:
    assert _rules(_assessment(against_version="3")) == ["completeness/unknown-question-version"]
    assert _rules(_assessment()) == ["completeness/unversioned-assessment"]


def test_a_retracted_assessment_is_exempt() -> None:
    retracted = _assessment(against_version="1", status="retracted")
    assert _rules(retracted) == []
    assert not is_void(retracted, RECORDS)


def test_an_assessment_of_a_construct_names_no_version() -> None:
    construct = {"type": "assessment", "assesses": "mod.a.m", "against": "prob.a.p"}
    records = {**RECORDS, "mod.a.m": {"type": "model"}}
    assert misversioned_assessment(construct, records) == []
    found = misversioned_assessment({**construct, "against_version": "1"}, records)
    assert [f.rule.id for f in found] == ["completeness/unversioned-assessment"]


def test_a_void_assessment_settles_no_demand(monkeypatch: Any) -> None:
    """The answer is accepted and complete, so only the voidness of its assessment decides."""
    import gnomon.completeness.problems as problems

    monkeypatch.setattr(problems, "disposition", lambda *args: "satisfied")
    problem = {
        "id": "prob.a.p",
        "type": "problem",
        "result_type": "explanation",
        "request": "one",
    }
    classes: dict[str, str] = {"explanation": "claim"}
    holders: dict[str, list[str]] = {}
    current = {**RECORDS, "prob.a.p": problem, "assess.a.x": _assessment(against_version="2")}
    void = {**RECORDS, "prob.a.p": problem, "assess.a.x": _assessment(against_version="1")}
    assert demand_met(problem, current, classes, holders) is True
    assert demand_met(problem, void, classes, holders) is False


def test_a_question_revised_without_a_recorded_step_is_warned() -> None:
    found = unrecorded_question_revision(QUESTION, RECORDS)
    assert [f.rule.id for f in found] == ["completeness/unrecorded-question-revision"]
    step = {"id": "revise", "activity": "question-revision", "output": {"ref": "quest.a.q"}}
    itinerary = {"type": "itinerary", "steps": [step]}
    assert unrecorded_question_revision(QUESTION, {**RECORDS, "itin.a.i": itinerary}) == []


def test_a_recorded_revision_that_raises_no_version_is_reported() -> None:
    step = {
        "id": "revise",
        "activity": "question-revision",
        "inputs": [{"type": "question", "ref": "quest.a.q", "as_of": "abc123"}],
        "output": {"type": "question", "ref": "quest.a.q"},
        "norm": {"test": "norm.question-revision", "verdict": "pending"},
    }
    itinerary = {"id": "itin.a.i", "type": "itinerary", "addresses": "quest.a.q", "steps": [step]}

    def ids(earlier: dict[str, Any]) -> list[str]:
        found = itinerary_problems(itinerary, RECORDS, states=lambda ident, rev: earlier)
        return [f.rule.id for f in found if f.rule.id == "itinerary/unversioned-question-revision"]

    assert ids({**QUESTION, "version": "2"}) == ["itinerary/unversioned-question-revision"]
    assert ids({**QUESTION, "version": "1"}) == []


def test_a_raised_version_voids_the_assessment_of_a_worked_inquiry(tmp_path: Path) -> None:
    case = "grokking-delayed-generalization"
    shutil.copytree(EXAMPLES / case, tmp_path / case)
    path = tmp_path / case / "question.yml"
    text = path.read_text(encoding="utf-8")
    assert '\nversion: "1"\n' in text
    path.write_text(text.replace('\nversion: "1"\n', '\nversion: "2"\n', 1), encoding="utf-8")
    found = {x.finding.rule.id for x in check_workspace(load_workspace(tmp_path))}
    assert "completeness/void-assessment" in found
    assert "completeness/unrecorded-question-revision" in found


def test_the_worked_inquiries_report_no_version_finding() -> None:
    found = {x.finding.rule.id for x in check_workspace(load_workspace(EXAMPLES))}
    assert not {rule for rule in found if "version" in rule or "void" in rule}
