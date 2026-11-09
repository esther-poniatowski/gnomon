"""Tests of the assembly of a level: the questions of a problem, the components of a question, the
exclusions and their checks, and the assembly view on a decomposed question."""

from __future__ import annotations

import copy
from typing import Any

from gnomon.assembly import assembly_tables
from gnomon.completeness import components, demand_met, problem_questions, readable_obstacles
from gnomon.completeness.levels import decomposition_findings, settled
from gnomon.itineraries import type_classes, type_holders

PASSED = {"tests": {"admissibility": {"scope": {"verdict": "pass"}}}}


def _part(name: str) -> dict[str, Any]:
    return {
        "type": "question",
        "id": f"quest.a.{name}",
        "version": "1",
        "links": [{"question": "quest.a.goal", "relation": "subquestion-of"}],
    }


def _answer(name: str, status: str = "accepted", **fields: Any) -> dict[str, Any]:
    return {
        "type": "answer",
        "id": f"ans.a.{name}",
        "answers": f"quest.a.{name}",
        "status": status,
        "erotetic_relation": {"value": "complete"},
        **fields,
    }


def _assessment(name: str, version: str = "1") -> dict[str, Any]:
    return {
        "type": "assessment",
        "id": f"asmt.a.{name}",
        "assesses": f"ans.a.{name}",
        "against": f"quest.a.{name}",
        "against_version": version,
        **PASSED,
    }


def _records() -> dict[str, dict[str, Any]]:
    """A goal question decomposed into three parts, one deferred, served by an enabling question,
    with a synthesis answer that the accepted parts support, and one part out of scope."""
    goal = {
        "type": "question",
        "id": "quest.a.goal",
        "addresses": "prob.a.p",
        "version": "1",
        "status": "posed",
        "subject": {"domain": {"restrictions": [{"name": "gain", "values": "g > 0"}]}},
        "excludes": [
            {
                "id": "noise",
                "kind": "deferred",
                "question": "quest.a.noise",
                "reading": "the dependence on the noise level",
                "reason": "the noiseless case comes first",
            },
            {
                "id": "learning",
                "kind": "out-of-scope",
                "reading": "the course of learning",
                "reason": "the question concerns trained networks only",
            },
        ],
    }
    geometry = {**_part("geometry"), "addresses": "prob.a.p"}
    records: list[dict[str, Any]] = [
        {
            "type": "problem",
            "id": "prob.a.p",
            "result_type": "target-claim",
            "request": "one",
            "associated_question": "quest.a.goal",
        },
        goal,
        geometry,
        _part("gain"),
        _part("noise"),
        {
            "type": "question",
            "id": "quest.a.reduced",
            "links": [{"question": "quest.a.goal", "relation": "enables"}],
        },
        _answer(
            "geometry",
            relations=[{"relation": "supports", "target": "ans.a.goal"}],
        ),
        _answer(
            "gain",
            grounds=[{"id": "shape", "role": "warrant", "record": "ans.a.geometry"}],
            domain="g < 2",
        ),
        _answer("goal", status="hypothesized"),
        _assessment("geometry"),
        _assessment("gain"),
    ]
    return {str(r["id"]): r for r in records}


def _rules(records: dict[str, dict[str, Any]], question: str) -> list[str]:
    return [f.rule.id for f in decomposition_findings(records[question], records)]


def test_a_subquestion_that_addresses_the_problem_is_no_question_of_the_problem() -> None:
    assert problem_questions("prob.a.p", _records()) == {"quest.a.goal"}


def test_the_components_of_a_question_carry_the_relation_of_their_link() -> None:
    found = [(c.question, c.link, c.supplies) for c in components("quest.a.goal", _records())]
    assert found == [
        ("quest.a.gain", "subquestion-of", True),
        ("quest.a.geometry", "subquestion-of", True),
        ("quest.a.noise", "subquestion-of", True),
        ("quest.a.reduced", "enables", False),
    ]


def test_an_accepted_part_answer_does_not_meet_the_demand_of_the_problem() -> None:
    records = _records()
    classes, holders = type_classes(), type_holders()
    assert demand_met(records["prob.a.p"], records, classes, holders) is False
    obstacles = readable_obstacles(records["prob.a.p"], records, classes, holders)
    assert obstacles.get("unassessed-candidates") is True


def test_the_accepted_synthesis_meets_the_demand() -> None:
    records = _records()
    records["ans.a.goal"]["status"] = "accepted"
    records["asmt.a.goal"] = _assessment("goal")
    assert demand_met(records["prob.a.p"], records, type_classes(), type_holders()) is True


def test_a_part_assessed_against_an_earlier_version_is_not_settled() -> None:
    records = _records()
    records["quest.a.gain"]["version"] = "2"
    assert not settled("quest.a.gain", records)
    gaps = assembly_tables(records)["gaps"]
    assert {
        "level": "quest.a.goal",
        "gap": "unassessed-part",
        "subject": "ans.a.gain",
        "detail": "assessment: void",
    } in gaps


def test_the_level_reports_its_parts_its_synthesis_and_its_gaps() -> None:
    tables = assembly_tables(_records())
    goal = next(row for row in tables["levels"] if row["level"] == "quest.a.goal")
    assert (goal["parts"], goal["settled"], goal["synthesis"]) == (3, 2, "")
    gaps = {(g["gap"], g["subject"]) for g in tables["gaps"] if g["level"] == "quest.a.goal"}
    assert gaps == {
        ("deferred-component", "quest.a.noise"),
        ("missing-synthesis", "quest.a.goal"),
    }
    deferred = [c["deferred"] for c in tables["components"] if c["component"] == "quest.a.noise"]
    assert deferred == ["noise"]


def test_each_citation_names_the_edge_or_the_link_that_states_it() -> None:
    cited = {
        (c["source"], c["target"], c["relation"], c["through"])
        for c in assembly_tables(_records())["citations"]
    }
    assert (
        "quest.a.gain",
        "quest.a.geometry",
        "grounds[].record",
        "ans.a.gain -> ans.a.geometry",
    ) in cited
    assert ("quest.a.geometry", "quest.a.goal", "supports", "ans.a.geometry -> ans.a.goal") in cited
    assert ("quest.a.reduced", "quest.a.goal", "enables", "quest.a.reduced links") in cited


def test_the_limits_are_listed_and_never_combined() -> None:
    limits = {(row["limit"], row["statement"]) for row in assembly_tables(_records())["limits"]}
    assert {
        ("question-domain", "g > 0"),
        ("domain", "g < 2"),
        ("out-of-scope", "the course of learning"),
    } <= limits


def test_a_well_placed_decomposition_has_no_finding() -> None:
    assert _rules(_records(), "quest.a.goal") == []


def test_a_deferral_of_no_subquestion_and_a_component_out_of_scope_are_misplaced() -> None:
    records = _records()
    excludes = records["quest.a.goal"]["excludes"]
    excludes[0]["question"] = "quest.a.reduced"
    excludes[1]["question"] = "quest.a.gain"
    assert _rules(records, "quest.a.goal") == ["completeness/misplaced-exclusion"] * 2


def test_a_deferred_subquestion_with_an_accepted_answer_is_a_stale_deferral() -> None:
    records = _records()
    records["ans.a.noise"] = _answer("noise")
    assert _rules(records, "quest.a.goal") == ["completeness/excluded-answered"]


def test_a_question_answered_with_an_open_subquestion_is_reported() -> None:
    records = copy.deepcopy(_records())
    records["quest.a.goal"]["status"] = "answered"
    assert _rules(records, "quest.a.goal") == ["completeness/answered-with-open-component"]
