"""Links between the records of an inquiry, and the closed fields of every record kind.

A question names its subject through slots that hold a record or a typed placeholder, names the
problem it serves, the questions it is linked to and the background records it admits. These tests
check each name against the records of its problem, and check every closed field of every record
kind against the vocabulary registry, answers and assessments included. Each rule carries a
planted case that fails for the intended reason. The worked inquiries are checked in
``test_check.py``, through the context that ``gnomon check`` assembles.
"""

from __future__ import annotations

from typing import Any

import yaml

from gnomon.completeness import (
    admitted_values,
    demand_met,
    disposition,
    foreign_backgrounds,
    inadmissible_values,
    malformed_credence,
    misdirected_assessment,
    mismatched_occurrence,
    mismatched_request,
    misstated_obstacles,
    occurrence_by_category,
    placeholder_types,
    premature_appraisal,
    result_aims,
    unbounded_aim,
    unresolved_slots,
    unstated_function_sense,
    unsupported_outcome,
)
from gnomon.findings import texts
from gnomon.itineraries import construct_record_kinds, type_classes, type_holders

from .paths import EXAMPLES

TYPES = placeholder_types()
CONSTRUCTS = construct_record_kinds()
CLASSES, HOLDERS = type_classes(), type_holders()


def test_a_slot_without_an_identified_record_or_a_typed_placeholder_is_reported() -> None:
    records: dict[str, dict[str, Any]] = {
        "system.a": {"type": "target-system", "identification": {"description": "the basin"}},
        "system.b": {"type": "target-system"},
        "phen.a": {"type": "phenomenon", "identification": {"description": "the flow"}},
    }
    question: dict[str, Any] = {"subject": {"target_system": "system.a", "phenomenon": "phen.a"}}
    assert unresolved_slots(question, records, TYPES) == []
    question["subject"] = {
        "target_system": "system.b",
        "phenomenon": {
            "placeholder": "phenomenon",
            "description": "the geometry of the representation",
        },
    }
    assert texts(unresolved_slots(question, records, TYPES)) == [
        "subject.target_system: system.b carries no identification, so its referent is not fixed"
    ]
    question["subject"] = {"target_system": "phen.a", "phenomenon": {"placeholder": "mood"}}
    assert texts(unresolved_slots(question, records, TYPES)) == [
        "subject.target_system: phen.a is a phenomenon record, not a target-system record",
        "subject.phenomenon: the placeholder type 'mood' is not admitted",
        "subject.phenomenon: the placeholder carries no description",
    ]
    question["subject"] = {"target_system": "system.z", "phenomenon": None}
    assert texts(unresolved_slots(question, records, TYPES)) == [
        "subject.target_system: no record carries the identifier system.z",
        "subject.phenomenon: holds neither a record identifier nor a placeholder",
    ]


def test_an_admitted_background_describes_the_target_of_the_question() -> None:
    records: dict[str, dict[str, Any]] = {
        "bg.a": {"type": "background", "describes": "system.a"},
        "bg.b": {"type": "background", "describes": "system.b"},
    }
    question = {"subject": {"target_system": "system.a", "background": ["bg.a"]}}
    assert foreign_backgrounds(question, records) == []
    question["subject"]["background"] = ["bg.b", "bg.z"]
    assert texts(foreign_backgrounds(question, records)) == [
        "subject.background: bg.b describes another target than system.a"
    ]


def test_a_functional_question_without_a_sense_of_function_is_reported() -> None:
    question = {"task": {"requested_relation": "functional", "function_sense": None}}
    assert texts(unstated_function_sense(question)) == [
        "task.function_sense: a functional relation is requested without its sense of function"
    ]
    question["task"]["function_sense"] = "causal-role"
    assert unstated_function_sense(question) == []
    assert unstated_function_sense({"task": {"requested_relation": "causal-mechanistic"}}) == []


def test_a_credence_outside_the_unit_interval_or_without_basis_is_reported() -> None:
    assert malformed_credence({}) == []
    assert malformed_credence({"credence": {"value": 0.7, "basis": "two replications"}}) == []
    assert texts(malformed_credence({"credence": {"value": 1.4}})) == [
        "credence.value: 1.4 is no number between 0 and 1",
        "credence.basis: the value states no basis",
    ]
    assert texts(malformed_credence({"credence": {"value": True, "basis": "x"}})) == [
        "credence.value: True is no number between 0 and 1"
    ]


def test_an_answer_status_outside_the_attitudes_is_reported() -> None:
    """The former status `informally-backed` mixed an attitude with a support, and is now
    refused."""
    record = {
        "type": "answer",
        "status": "informally-backed",
        "support": "informal",
        "grounds": [{"role": "idealization", "removable": "partly"}],
    }
    assert texts(inadmissible_values(record, admitted_values("answer"))) == [
        "status: informally-backed is not admitted; the admitted values are accepted,"
        " entertained, hypothesized, retracted",
        "grounds.removable: partly is not admitted; the admitted values are controlled,"
        " ineliminable, unknown",
    ]


OCCURRENCES = occurrence_by_category()


def test_an_occurrence_class_that_the_category_does_not_admit_is_reported() -> None:
    """A regularity relates occurrences without being one; a structural property holds pointwise."""
    assert texts(
        mismatched_occurrence({"category": "regularity", "occurrence": "event"}, OCCURRENCES)
    ) == ["occurrence: event is no occurrence class of a regularity, which admits not-applicable"]
    assert texts(
        mismatched_occurrence(
            {"category": "structural-property", "occurrence": "process"}, OCCURRENCES
        )
    ) == ["occurrence: process is no occurrence class of a structural-property, which admits state"]
    assert (
        mismatched_occurrence(
            {"category": "particular-occurrence", "occurrence": "event"}, OCCURRENCES
        )
        == []
    )
    assert mismatched_occurrence({"category": None, "occurrence": None}, OCCURRENCES) == []


def test_a_placeholder_whose_type_does_not_fit_its_slot_is_reported() -> None:
    """The target-system slot awaits a system, and the phenomenon slot a phenomenon."""
    question = {
        "subject": {
            "target_system": {"placeholder": "phenomenon", "description": "a readout"},
            "phenomenon": {"placeholder": "system", "description": "a network"},
        }
    }
    assert texts(unresolved_slots(question, {}, TYPES)) == [
        "subject.target_system: the placeholder type 'phenomenon' does not fit the slot, which"
        " awaits 'system'",
        "subject.phenomenon: the placeholder type 'system' does not fit the slot, which awaits"
        " 'phenomenon'",
    ]
    question["subject"] = {
        "target_system": {"placeholder": "system", "description": "networks of the benchmark"},
        "phenomenon": {"placeholder": "phenomenon", "description": "their geometry"},
    }
    assert unresolved_slots(question, {}, TYPES) == []


def test_the_dispositions_of_the_fixture_assessments() -> None:
    """Each fixture assessment has a determinate disposition, and the cases with a failed test are
    not satisfied."""
    root = EXAMPLES
    found = {}
    for path in sorted(root.glob("*/assessment.yml")):
        found[path.parent.name] = disposition(yaml.safe_load(path.read_text(encoding="utf-8")))
    assert set(found.values()) <= {"satisfied", "not-satisfied", "withheld"}
    assert found["grokking-delayed-generalization"] == "not-satisfied"


def test_a_corrective_answer_that_passes_its_tests_is_corrective_rather_than_satisfied() -> None:
    """A corrective answer shows that its question has no true direct answer, so it cannot satisfy
    it."""
    passing = {
        "tests": {
            "admissibility": {"product": {"verdict": "not-applicable"}},
            "warrant": {"closure": {"verdict": "pass"}},
        }
    }
    assert disposition(passing) == "satisfied"
    assert disposition(passing, "partial") == "satisfied"
    assert disposition(passing, "corrective") == "corrective"
    failing = {"tests": {"warrant": {"closure": {"verdict": "fail"}}}}
    assert disposition(failing, "corrective") == "not-satisfied"


def test_an_appraisal_is_reported_unless_the_answer_passes() -> None:
    appraisal = [{"virtue": "unification", "assessment": "high"}]
    pending = {
        "tests": {"admissibility": {"scope": {"verdict": "pending"}}},
        "appraisal": appraisal,
    }
    assert texts(premature_appraisal(pending)) == [
        "appraisal: the answer is appraised although its disposition is withheld"
    ]
    passing = {"tests": {"admissibility": {"scope": {"verdict": "pass"}}}, "appraisal": appraisal}
    assert premature_appraisal(passing) == []


def test_an_assessment_of_a_construct_holds_one_verdict_per_constraint() -> None:
    """A construct is tested against the constraints of its problem; an answer against its
    question."""
    records: dict[str, dict[str, Any]] = {
        "prob.a": {
            "type": "problem",
            "constraints": [{"name": "reproduces-delay"}, {"name": "derives-duration"}],
        },
        "quest.a": {"type": "question"},
        "mod.a": {"type": "model"},
        "ans.a": {"type": "answer"},
        "phen.a": {"type": "phenomenon"},
    }
    verdicts = [
        {"constraint": "reproduces-delay", "verdict": "pass"},
        {"constraint": "derives-duration", "verdict": "fail"},
    ]
    of_model = {"assesses": "mod.a", "against": "prob.a", "tests": {"constraints": verdicts}}
    assert texts(misdirected_assessment(of_model, records, CONSTRUCTS)) == []
    assert disposition(of_model) == "not-satisfied"
    wrong = {
        "assesses": "mod.a",
        "against": "quest.a",
        "tests": {"constraints": [{"constraint": "stable"}]},
    }
    assert texts(misdirected_assessment(wrong, records, CONSTRUCTS)) == [
        "against: quest.a is a question record, and an assessment of a model is made against a"
        " problem",
    ]
    unknown = {
        "assesses": "mod.a",
        "against": "prob.a",
        "tests": {
            "constraints": [{"constraint": "stable"}],
            "warrant": {"closure": {"verdict": "pass"}},
        },
    }
    assert texts(misdirected_assessment(unknown, records, CONSTRUCTS)) == [
        "tests.warrant: an assessment of a construct holds no tests of warrant",
        "tests.constraints: stable is no constraint of prob.a",
    ]
    empty = {"assesses": "mod.a", "against": "prob.a", "tests": {}}
    assert texts(misdirected_assessment(empty, records, CONSTRUCTS)) == [
        "tests.constraints: an assessment of a construct holds one verdict per constraint",
    ]


def test_an_assessment_of_an_answer_keeps_its_two_levels_of_tests() -> None:
    records = {
        "prob.a": {"type": "problem"},
        "ans.a": {"type": "answer"},
        "phen.a": {"type": "phenomenon"},
        "quest.a": {"type": "question"},
    }
    tests = {
        "admissibility": {"scope": {"verdict": "pass"}},
        "warrant": {"closure": {"verdict": "pass"}},
    }
    assert (
        texts(
            misdirected_assessment(
                {"assesses": "ans.a", "against": "quest.a", "tests": tests}, records, CONSTRUCTS
            )
        )
        == []
    )
    misread = {
        "assesses": "ans.a",
        "against": "prob.a",
        "tests": {
            "admissibility": {"scope": {"verdict": "pass"}},
            "constraints": [{"constraint": "c"}],
        },
    }
    assert texts(misdirected_assessment(misread, records, CONSTRUCTS)) == [
        "against: prob.a is a problem record, and an assessment of an answer is made against a"
        " question",
        "tests.warrant: an assessment of an answer holds its tests of warrant",
        "tests.constraints: an assessment of an answer holds no verdict per constraint",
    ]
    assert texts(misdirected_assessment({"assesses": "phen.a"}, records, CONSTRUCTS)) == [
        "assesses: phen.a is a phenomenon record, neither an answer nor a construct"
    ]
    assert texts(misdirected_assessment({"assesses": "ans.none"}, records, CONSTRUCTS)) == [
        "assesses: ans.none is no record"
    ]


def test_a_problem_bounds_the_aim_and_the_request_of_its_questions() -> None:
    """The associated question takes the request of the demand; each serving question an admitted
    aim."""
    problem = {
        "id": "prob.a",
        "type": "problem",
        "result_type": "explanation",
        "request": "one",
        "associated_question": "quest.a",
    }
    question: dict[str, Any] = {
        "type": "question",
        "addresses": "prob.a",
        "request": "one",
        "task": {"epistemic_aim": "explanation"},
    }
    records: dict[str, dict[str, Any]] = {
        "prob.a": problem,
        "quest.a": question,
        "phen.a": {"type": "phenomenon"},
    }
    assert texts(mismatched_request(problem, records)) == []
    assert texts(unbounded_aim(question, records, result_aims())) == []
    question["request"] = "all"
    assert texts(mismatched_request(problem, records)) == [
        "associated_question: quest.a asks under the request all, and the problem under one"
    ]
    assert texts(mismatched_request({**problem, "associated_question": "phen.a"}, records)) == [
        "associated_question: phen.a is no question record addressing prob.a"
    ]
    question["task"]["epistemic_aim"] = "prediction"
    assert texts(unbounded_aim(question, records, result_aims())) == [
        "task.epistemic_aim: prediction does not serve a demand for explanation"
    ]
    concept: dict[str, dict[str, Any]] = {
        **records,
        "prob.a": {**problem, "result_type": "concept"},
    }
    question["task"]["epistemic_aim"] = "description"
    assert texts(unbounded_aim(question, concept, result_aims())) == [
        "task.epistemic_aim: description does not serve a demand for concept"
    ]


PASSING = {
    "admissibility": {"scope": {"verdict": "pass"}},
    "warrant": {"closure": {"verdict": "pass"}},
}


def test_a_demand_for_a_claim_is_met_by_an_accepted_complete_satisfied_answer() -> None:
    problem = {
        "id": "prob.a",
        "type": "problem",
        "result_type": "explanation",
        "request": "one",
        "status": "solved",
    }
    records: dict[str, dict[str, Any]] = {
        "prob.a": problem,
        "quest.a": {"type": "question", "addresses": "prob.a"},
        "ans.a": {
            "type": "answer",
            "answers": "quest.a",
            "status": "accepted",
            "erotetic_relation": {"value": "complete"},
        },
        "assess.a": {
            "type": "assessment",
            "assesses": "ans.a",
            "against": "quest.a",
            "tests": PASSING,
        },
    }
    assert demand_met(problem, records, CLASSES, HOLDERS) is True
    assert texts(unsupported_outcome(problem, records, CLASSES, HOLDERS)) == []
    records["ans.a"]["erotetic_relation"]["value"] = "partial"
    assert texts(unsupported_outcome(problem, records, CLASSES, HOLDERS)) == [
        "status: solved, and the records do not meet the demand"
    ]
    records["ans.a"]["erotetic_relation"]["value"] = "complete"
    problem["status"] = "posed"
    assert texts(unsupported_outcome(problem, records, CLASSES, HOLDERS)) == [
        "status: posed, and the records meet the demand"
    ]


def test_a_demand_for_a_construct_is_met_by_a_stabilized_satisfied_construct() -> None:
    problem = {
        "id": "prob.a",
        "type": "problem",
        "result_type": "model",
        "request": "one",
        "constraints": [{"name": "reproduces-delay"}],
    }
    verdicts = [{"constraint": "reproduces-delay", "verdict": "pass"}]
    records: dict[str, dict[str, Any]] = {
        "prob.a": problem,
        "mod.a": {"type": "model", "status": "provisional"},
        "assess.a": {
            "type": "assessment",
            "assesses": "mod.a",
            "against": "prob.a",
            "tests": {"constraints": verdicts},
        },
    }
    assert demand_met(problem, records, CLASSES, HOLDERS) is False
    records["mod.a"]["status"] = "stabilized"
    assert demand_met(problem, records, CLASSES, HOLDERS) is True
    verdicts[0]["verdict"] = "fail"
    assert demand_met(problem, records, CLASSES, HOLDERS) is False


def test_a_decision_is_met_once_every_candidate_is_settled() -> None:
    problem = {
        "id": "prob.a",
        "type": "problem",
        "result_type": "explanation",
        "request": "decision",
    }
    records: dict[str, dict[str, Any]] = {
        "prob.a": problem,
        "quest.a": {"type": "question", "addresses": "prob.a"},
        "ans.a": {"type": "answer", "answers": "quest.a", "status": "retracted"},
        "ans.b": {"type": "answer", "answers": "quest.a", "status": "hypothesized"},
        "assess.a": {"type": "assessment", "assesses": "ans.a", "tests": PASSING},
        "assess.b": {"type": "assessment", "assesses": "ans.b", "tests": PASSING},
    }
    assert demand_met(problem, records, CLASSES, HOLDERS) is False
    records["ans.b"]["status"] = "retracted"
    assert demand_met(problem, records, CLASSES, HOLDERS) is True
    del records["assess.b"]
    assert demand_met(problem, records, CLASSES, HOLDERS) is False


def test_a_demand_of_a_type_without_a_solving_rule_is_not_read() -> None:
    problem = {
        "id": "prob.a",
        "type": "problem",
        "result_type": "phenomenon",
        "request": "one",
        "status": "solved",
    }
    assert demand_met(problem, {"prob.a": problem}, CLASSES, HOLDERS) is None
    assert unsupported_outcome(problem, {"prob.a": problem}, CLASSES, HOLDERS) == []


def test_an_accepted_corrective_answer_to_the_associated_question_dissolves_the_problem() -> None:
    problem = {
        "id": "prob.a",
        "type": "problem",
        "result_type": "explanation",
        "request": "one",
        "status": "posed",
        "associated_question": "quest.a",
    }
    records: dict[str, dict[str, Any]] = {
        "prob.a": problem,
        "quest.a": {"type": "question", "addresses": "prob.a", "request": "one"},
        "ans.a": {
            "type": "answer",
            "answers": "quest.a",
            "status": "accepted",
            "erotetic_relation": {"value": "corrective"},
        },
    }
    assert texts(unsupported_outcome(problem, records, CLASSES, HOLDERS)) == [
        "status: posed, and an accepted answer denies a presupposition of quest.a"
    ]
    problem["status"] = "dissolved"
    assert texts(unsupported_outcome(problem, records, CLASSES, HOLDERS)) == []
    records["ans.a"]["status"] = "hypothesized"
    assert texts(unsupported_outcome(problem, records, CLASSES, HOLDERS)) == [
        "status: dissolved, and no accepted answer denies a presupposition of quest.a"
    ]


def test_the_stated_knowledge_obstacles_agree_with_the_records() -> None:
    """A stated obstacle that the records contradict is reported; an obstacle that the records
    show need not be stated."""
    problem = {
        "id": "prob.a",
        "type": "problem",
        "result_type": "explanation",
        "request": "one",
        "associated_question": "quest.a",
        "knowledge_obstacles": [{"obstacle": "open-gap"}],
    }
    records: dict[str, dict[str, Any]] = {
        "prob.a": problem,
        "quest.a": {"type": "question", "addresses": "prob.a", "request": "one"},
    }
    assert texts(misstated_obstacles(problem, records, CLASSES, HOLDERS)) == []
    records["ans.a"] = {"type": "answer", "answers": "quest.a", "status": "hypothesized"}
    assert texts(misstated_obstacles(problem, records, CLASSES, HOLDERS)) == [
        "knowledge_obstacles: the problem states open-gap, which its records contradict",
    ]
    problem["knowledge_obstacles"] = [
        {"obstacle": "unassessed-candidates"},
        {"obstacle": "conflict"},
    ]
    assert texts(misstated_obstacles(problem, records, CLASSES, HOLDERS)) == []
    records["ans.a"].update(status="accepted", erotetic_relation={"value": "corrective"})
    assert texts(misstated_obstacles(problem, records, CLASSES, HOLDERS)) == [
        "knowledge_obstacles: the problem states unassessed-candidates, which its records"
        " contradict",
    ]
    problem["knowledge_obstacles"] = []
    assert texts(misstated_obstacles(problem, records, CLASSES, HOLDERS)) == []
