"""Transparent comparisons of researcher-authored appraisals."""

from __future__ import annotations

from pathlib import Path
from typing import Any

import yaml
from jsonschema import Draft202012Validator

from gnomon.act_comparisons import appraisal_findings, comparisons
from gnomon.itineraries import itinerary_problems
from gnomon.views import next_act


def _appraisal(*, second_cost: str = "high") -> dict[str, Any]:
    """Return one complete appraisal under the ordinal-dominance rule."""
    return {
        "id": "ready-acts",
        "question": "quest.demo.cause",
        "route": "selection",
        "rule": "ordinal-dominance",
        "criteria": [
            {
                "id": "feasibility",
                "question": "How likely is completion with the available means?",
                "scale": ["unavailable", "uncertain", "feasible"],
                "preferred": "higher",
            },
            {
                "id": "cost",
                "question": "What effort does the act require?",
                "scale": ["low", "medium", "high"],
                "preferred": "lower",
            },
        ],
        "acts": [
            {
                "id": "explain-term",
                "activity": "explication",
                "acts_on": "definiteness",
                "available_means": ["source passage"],
                "judgments": [
                    {
                        "criterion": "feasibility",
                        "value": "feasible",
                        "basis": "The defining passage is available.",
                    },
                    {
                        "criterion": "cost",
                        "value": "low",
                        "basis": "No new data are required.",
                    },
                ],
            },
            {
                "id": "collect-data",
                "activity": "measurement",
                "acts_on": "access",
                "available_means": ["existing instrument"],
                "judgments": [
                    {
                        "criterion": "feasibility",
                        "value": "uncertain",
                        "basis": "Instrument time is not confirmed.",
                    },
                    {
                        "criterion": "cost",
                        "value": second_cost,
                        "basis": "The measurement requires a new run.",
                    },
                ],
            },
        ],
    }


def _itinerary(appraisal: dict[str, Any]) -> dict[str, Any]:
    """Return an itinerary containing ``appraisal``."""
    return {
        "_schema": "gnomon:itinerary@3",
        "type": "itinerary",
        "id": "itin.demo.cause",
        "addresses": "quest.demo.cause",
        "act_appraisals": [appraisal],
    }


def test_dominance_exposes_the_rule_inputs_and_pairwise_result() -> None:
    """A dominant act follows only from the declared scales and preferred directions."""
    itinerary = _itinerary(_appraisal())

    assert appraisal_findings(itinerary) == []
    [comparison] = comparisons({"itin.demo.cause": itinerary})

    assert comparison["rule"] == "ordinal-dominance"
    assert comparison["rule_statement"].startswith("An act dominates another")
    assert comparison["leading_acts"] == ["explain-term"]
    assert comparison["selection"] == "determined"
    assert comparison["relations"] == [
        {
            "act": "explain-term",
            "other": "collect-data",
            "relation": "dominates",
            "better_on": ["feasibility", "cost"],
            "worse_on": [],
            "equal_on": [],
        }
    ]
    assert {row["criterion"] for row in comparison["judgments"]} == {
        "feasibility",
        "cost",
    }
    assert all(row["basis"] for row in comparison["judgments"])


def test_conflicting_criteria_leave_both_acts_undominated() -> None:
    """Dominance reports an unresolved choice instead of inventing weights between criteria."""
    appraisal = _appraisal(second_cost="low")
    first = appraisal["acts"][0]
    first["judgments"][1]["value"] = "high"

    [comparison] = comparisons({"itin.demo.cause": _itinerary(appraisal)})

    assert comparison["leading_acts"] == ["explain-term", "collect-data"]
    assert comparison["selection"] == "unresolved"
    assert comparison["relations"][0] == {
        "act": "explain-term",
        "other": "collect-data",
        "relation": "incomparable",
        "better_on": ["feasibility"],
        "worse_on": ["cost"],
        "equal_on": [],
    }


def test_the_next_act_contract_displays_a_complete_comparison() -> None:
    """The generated comparison follows the contract consumed by a read-only renderer."""
    itinerary = _itinerary(_appraisal())
    view = next_act({}, "sha256:" + "0" * 64, {"itin.demo.cause": itinerary})
    schema_path = (
        Path(__file__).resolve().parents[2] / "src/gnomon/data/schemas/views/next-act.schema.yml"
    )
    schema = yaml.safe_load(schema_path.read_text(encoding="utf-8"))

    assert view["_schema"] == "gnomon:view.next-act@8"
    assert view["comparisons"][0]["selection"] == "determined"
    assert list(Draft202012Validator(schema).iter_errors(view)) == []


def test_invalid_judgments_are_located_and_not_compared() -> None:
    """Unknown criteria, foreign values, and missing judgments block a computed comparison."""
    appraisal = _appraisal()
    first = appraisal["acts"][0]
    first["judgments"] = [
        {
            "criterion": "speed",
            "value": "fast",
            "basis": "The operation is short.",
        },
        {
            "criterion": "feasibility",
            "value": "certain",
            "basis": "The source is present.",
        },
    ]
    itinerary = _itinerary(appraisal)

    found = appraisal_findings(itinerary)

    assert {item.rule.id for item in found} == {"itinerary/malformed-appraisal"}
    assert any("speed names no declared criterion" in item.text for item in found)
    assert any("certain is not on the scale of feasibility" in item.text for item in found)
    assert any("states no judgment of cost" in item.text for item in found)
    assert comparisons({"itin.demo.cause": itinerary}) == []
    checked = itinerary_problems(
        itinerary,
        {"quest.demo.cause": {"type": "question", "id": "quest.demo.cause"}},
    )
    assert [item.text for item in checked] == [item.text for item in found]
