"""The diagnosis of the conditions of answerability that ``gnomon status`` reports.

A state is read from an assertion of the question, else from a field that shows it, else it is not
established; a condition is open when the conditions on which it depends are established; an act is
ready when its required inputs exist unimpeached; impeachment propagates along the itineraries.
"""

from __future__ import annotations

from typing import Any

from typer.testing import CliRunner

from gnomon.answerability import (
    diagnose,
    itinerary_state,
    malformed_answerability,
    render_text,
    routes_of,
)
from gnomon.cli import app
from gnomon.findings import texts

from .paths import EXAMPLES


def states(diagnosis: Any, route: int = 0) -> dict[str, str]:
    return {s.condition: s.state for s in diagnosis.questions[0].routes[route].states}


def test_a_condition_left_unasserted_is_not_established_and_opens_in_order() -> None:
    found = diagnose({"quest.a.b": {"id": "quest.a.b", "type": "question"}})
    assert set(states(found).values()) == {"not-established"}
    assert list(found.questions[0].routes[0].open) == ["definiteness"]


def test_an_asserted_state_opens_the_conditions_that_depend_on_it() -> None:
    question = {
        "id": "quest.a.b",
        "type": "question",
        "answerability": [
            {"condition": "definiteness", "state": "established", "pointers": ["phen.a.b"]},
            {
                "condition": "access",
                "route": "construction",
                "state": "refuted",
                "refutation": "outright",
                "pointers": ["doi:10.1000/proof"],
            },
        ],
    }
    found = diagnose({"quest.a.b": question})
    assert states(found)["definiteness"] == "established"
    assert "answer-type" in found.questions[0].routes[0].open
    assert "access" not in found.questions[0].routes[0].refuted


def test_the_route_of_construction_is_diagnosed_once_a_procedure_is_named() -> None:
    question = {
        "id": "quest.a.b",
        "type": "question",
        "construction": {"procedure": "design.a.method"},
        "answerability": [
            {
                "condition": "access",
                "route": "construction",
                "state": "refuted",
                "refutation": "outright",
                "pointers": ["doi:10.1000/proof"],
            }
        ],
    }
    assert routes_of(question) == ("selection", "construction")
    found = diagnose({"quest.a.b": question})
    assert found.questions[0].routes[1].refuted == ("access",)
    assert "candidates" not in states(found, 1)


def test_a_negative_phenomenon_refutes_soundness() -> None:
    records: dict[str, dict[str, Any]] = {
        "quest.a.b": {"id": "quest.a.b", "type": "question", "subject": {"phenomenon": "phen.a.b"}},
        "phen.a.b": {"id": "phen.a.b", "type": "phenomenon", "evidential_status": "absent"},
    }
    assert states(diagnose(records))["soundness"] == "refuted"


def test_an_answer_passing_admissibility_establishes_the_candidates() -> None:
    records: dict[str, dict[str, Any]] = {
        "quest.a.b": {"id": "quest.a.b", "type": "question"},
        "ans.a.b": {"id": "ans.a.b", "type": "answer", "answers": "quest.a.b"},
        "assess.a.b": {
            "id": "assess.a.b",
            "type": "assessment",
            "assesses": "ans.a.b",
            "tests": {"admissibility": {"scope": {"verdict": "pass"}}},
        },
    }
    assert states(diagnose(records))["candidates"] == "established"
    records["assess.a.b"]["tests"]["admissibility"]["grain"] = {"verdict": "pending"}
    assert states(diagnose(records))["candidates"] == "not-established"


def test_an_act_is_ready_only_when_its_required_inputs_exist() -> None:
    found = diagnose({"quest.a.b": {"id": "quest.a.b", "type": "question"}})
    acts = {a.activity: a for a in found.questions[0].routes[0].open["definiteness"]}
    assert not acts["operationalization"].ready and acts["operationalization"].missing == (
        "concept",
    )


def test_impeachment_and_pending_verdicts_propagate_along_an_itinerary() -> None:
    itinerary = {
        "id": "itin.a.b",
        "type": "itinerary",
        "steps": [
            {"id": "admit", "inputs": [], "output": {"ref": "bg.a.b"}, "norm": {"verdict": "fail"}},
            {
                "id": "derive",
                "inputs": [{"ref": "bg.a.b"}],
                "output": {"ref": "ans.a.b"},
                "norm": {"verdict": "pass"},
            },
            {
                "id": "guess",
                "inputs": [],
                "output": {"ref": "ans.a.c"},
                "norm": {"verdict": "pending"},
            },
            {
                "id": "test",
                "inputs": [{"ref": "itin.a.b.guess"}],
                "output": {"ref": "assess.a.c"},
                "norm": {"verdict": "pending"},
            },
        ],
    }
    records: dict[str, dict[str, Any]] = {
        "itin.a.b": itinerary,
        "assess.a.c": {"type": "assessment", "status": "stabilized"},
    }
    impeached, conditional, anew = itinerary_state(records)
    assert impeached == {"bg.a.b", "ans.a.b"}
    assert conditional == {"ans.a.c", "assess.a.c"}
    assert anew == ["itin.a.b.test"]


def test_an_assertion_states_its_kind_its_means_and_its_pointers() -> None:
    question = {
        "answerability": [
            {"condition": "access", "state": "refuted", "refutation": "lack-of-means"},
            {
                "condition": "definiteness",
                "state": "established",
                "term": "phen.a.b",
                "pointers": ["phen.a.b"],
            },
            {"condition": "soundness", "state": "refuted", "pointers": ["phen.a.b"]},
        ]
    }
    records = {"phen.a.b": {"type": "phenomenon", "commitment": "identified"}}
    assert texts(malformed_answerability(question, records)) == [
        "answerability.access: a refutation for lack of means names no means tried",
        "answerability.access: the state refuted cites no pointer",
        "answerability.definiteness: phen.a.b is not specified, which definiteness requires",
        "answerability.soundness: a refutation states no kind",
    ]


def test_the_command_reports_the_diagnosis_of_the_worked_inquiries() -> None:
    runner = CliRunner()
    text = runner.invoke(app, ["status", str(EXAMPLES)])
    assert (
        text.exit_code == 0
        and "judge anew the norm of itin.grokking.explain-delay.check" in text.output
    )
    first = runner.invoke(app, ["status", str(EXAMPLES), "--format", "yaml"]).output
    assert first == runner.invoke(app, ["status", str(EXAMPLES), "--format", "yaml"]).output
    assert "bg.delayed-generalization-networks.training-specification" in first


def test_a_question_of_explication_has_no_condition_of_definiteness() -> None:
    """Its explicandum is not a slot, so a dependency on its definiteness is void."""
    question = {"id": "quest.a.b", "type": "question", "task": {"epistemic_aim": "explication"}}
    found = diagnose({"quest.a.b": question})
    assert "definiteness" not in states(found)
    assert "answer-type" in found.questions[0].routes[0].open


def test_a_revision_flags_its_dependents_by_kind_and_warrant() -> None:
    """A narrowing flags a proven answer and a defeasible one; a reorientation only the second."""
    from gnomon.propagation import revisions

    records: dict[str, dict[str, Any]] = {
        "bg.a.b": {"id": "bg.a.b", "type": "background"},
        "ans.proven": {
            "id": "ans.proven",
            "type": "answer",
            "support": "formally-proven",
            "grounds": [{"record": "bg.a.b.law"}],
        },
        "ans.fitted": {
            "id": "ans.fitted",
            "type": "answer",
            "support": "informal",
            "grounds": [{"record": "bg.a.b.law"}],
        },
        "itin.a.b": {
            "id": "itin.a.b",
            "type": "itinerary",
            "steps": [
                {"id": "narrow", "revises": {"record": "bg.a.b", "kind": "scope-narrowing"}},
                {"id": "reorient", "revises": {"record": "bg.a.b", "kind": "reorientation"}},
                {
                    "id": "retract",
                    "revises": {
                        "record": "bg.a.b",
                        "kind": "retraction",
                        "reviews": [{"dependent": "ans.proven", "state": "unaffected"}],
                    },
                },
            ],
        },
    }
    narrow, reorient, retract = revisions(records)
    assert narrow.flagged == ("ans.fitted", "ans.proven")
    assert reorient.flagged == ("ans.fitted",)
    assert reorient.reasons == {"ans.fitted": "grounds[].record (defeasible)"}
    assert retract.flagged == ("ans.fitted", "ans.proven") and retract.to_review == ("ans.fitted",)
    assert (
        "review after the retraction of bg.a.b (itin.a.b.retract): ans.fitted via grounds[].record"
        " (defeasible)" in render_text(diagnose(records))
    )
