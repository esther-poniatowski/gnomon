"""Itineraries of inquiry, checked against the registries of activities and product types.

The registries transcribe the taxonomy of epistemic activities, whose notes are the source of the
content, so the first tests check the registries against those notes. The remaining tests plant
one defect per check of :func:`gnomon.itineraries.itinerary_problems` in an itinerary that passes, and confirm
that the check reports it for the intended reason.
"""

from __future__ import annotations

import copy
import re
from pathlib import Path
from typing import Any

import pytest
import yaml

from gnomon.itineraries import (
    activities,
    record_types,
    product_types,
    cycles,
    malformed_registry,
    itinerary_problems,
)

from .paths import EXAMPLES, ROOT

ACTIVITY_NOTES = ROOT / "docs" / "epistemology" / "processes" / "activities"
VOCABULARY = yaml.safe_load((ROOT / "src" / "gnomon" / "data" / "vocabularies.yml").read_text())
ACTS = activities()
TYPES = product_types()


def test_the_registries_are_consistent() -> None:
    modes = [entry["value"] for entry in VOCABULARY["vocabularies"]["itinerary"]["steps.mode"]]
    assert malformed_registry(ACTS, TYPES, modes) == []


def test_a_registry_naming_an_unknown_type_mode_or_norm_is_reported() -> None:
    act = ACTS["derivation"]
    broken = {"derivation": type(act)(**{**act.__dict__, "output": "theorem", "mode": "intuitive",
                                         "norm": "norm.proof"})}
    assert malformed_registry(broken, TYPES, ["deductive"]) == [
        "derivation: theorem is no product type",
        "derivation: intuitive is no admitted mode",
        "derivation: its norm norm.proof is not the test norm.derivation",
    ]


def signature_rows() -> dict[str, list[str]]:
    """Return, per activity of the notes, the cells of its row in the table of signatures."""
    rows: dict[str, list[str]] = {}
    for note in sorted(ACTIVITY_NOTES.glob("*.md")):
        text = note.read_text(encoding="utf-8")
        table = re.search(r"\| Activity \| Inputs \| Output \| Mode \| Context \|\n\|[^\n]*\n((?:\|[^\n]*\n)+)", text)
        if table is None:
            continue
        for line in table.group(1).splitlines():
            cells = [cell.strip() for cell in re.split(r"(?<!\\)\|", line.strip().strip("|"))]
            rows[cells[0].strip("`")] = [note.stem, *cells[1:]]
    return rows


ROWS = signature_rows()


def typed(cell: str) -> set[str]:
    """Return the type names a cell sets in code, including alternatives written in one span.

    >>> sorted(typed("`hypothesis \\| model`, `data` (several)"))
    ['data', 'hypothesis', 'model']
    """
    return {name for span in re.findall(r"`([^`]*)`", cell) for name in re.findall(r"[a-z][a-z-]*", span)}


@pytest.mark.skipif(not ROWS, reason="the notes of the activity taxonomy carry no table of signatures")
def test_the_registry_lists_the_activities_of_the_notes() -> None:
    assert set(ROWS) == set(ACTS), f"notes and registry differ: {set(ROWS) ^ set(ACTS)}"


@pytest.mark.skipif(not ROWS, reason="the notes of the activity taxonomy carry no table of signatures")
@pytest.mark.parametrize("identifier", sorted(ACTS))
def test_each_activity_has_the_signature_its_note_states(identifier: str) -> None:
    """The family, the input and output types, the mode and the context agree with the note."""
    if identifier not in ROWS:
        pytest.fail(f"{identifier} has no row in the notes")
    family, inputs, output, mode, context = ROWS[identifier][:5]
    act = ACTS[identifier]
    assert act.family == family
    assert typed(inputs) == {t for s in act.inputs for t in s.types}
    assert typed(output) == {act.output}
    assert (act.mode, act.context) == (mode, context)


#: The coverage statuses of a product type, as the header of the product-type registry defines them.
COVERAGE = {"exists", "partial", "to-create"}


def product_rows() -> list[str]:
    """Return the product types that the table of the taxonomy lists."""
    note = ACTIVITY_NOTES / "epistemic-activities.md"
    if not note.is_file():
        return []
    lines = note.read_text(encoding="utf-8").splitlines()
    if "| Type | Epistemic object | Output of |" not in lines:
        return []
    start = lines.index("| Type | Epistemic object | Output of |") + 2
    found = []
    for line in lines[start:]:
        if not line.startswith("| `"):
            break
        found.append(line.strip("|").split("|")[0].strip().strip("`"))
    return found


PRODUCT_ROWS = product_rows()


@pytest.mark.skipif(not PRODUCT_ROWS, reason="the overview of the taxonomy carries no table of product types")
def test_the_registry_lists_the_product_types_of_the_overview() -> None:
    """The taxonomy owns the list of types, and the registry states the coverage of each."""
    registry = yaml.safe_load((ROOT / "src/gnomon/data/registries/product-types.yml").read_text())
    entries = registry["product_types"]
    assert sorted(entry["id"] for entry in entries) == sorted(PRODUCT_ROWS)
    assert {entry["id"]: entry["status"] for entry in entries if entry["status"] not in COVERAGE} == {}


# An itinerary that passes every check, over records that the planted cases modify one at a time.
RECORDS: dict[str, dict[str, Any]] = {
    "prob.geometry": {"type": "problem"},
    "quest.geometry": {"type": "question"},
    "system.networks": {"type": "target-system"},
    "phen.readout": {"type": "phenomenon"},
    "ans.kernel": {"type": "answer"},
    "mod.kernel": {"type": "model"},
}
ITINERARY: dict[str, Any] = {
    "type": "itinerary",
    "addresses": "prob.geometry",
    "steps": [
        {"id": "pose", "activity": "problematization",
         "inputs": [{"type": "source", "ref": "doi:10.1000/anomaly"}],
         "output": {"type": "problem", "ref": "prob.geometry"},
         "norm": {"test": "norm.problematization", "verdict": "pass"}, "mode": "non-inferential"},
        {"id": "derive", "activity": "derivation",
         "inputs": [{"type": "model", "ref": "mod.kernel"}],
         "output": {"type": "consequence"},
         "norm": {"test": "norm.derivation", "verdict": "pending"}, "mode": "deductive"},
        {"id": "design", "activity": "experimental-design",
         "inputs": [{"type": "question", "ref": "quest.geometry"}, {"type": "model", "ref": "mod.kernel"}],
         "output": {"type": "design"},
         "norm": {"test": "norm.experimental-design", "verdict": "pending"}},
        {"id": "observe", "activity": "observation",
         "inputs": [{"type": "design", "ref": "design"}],
         "output": {"type": "data"},
         "norm": {"test": "norm.observation", "verdict": "pending"}},
    ],
}


def planted(**changes: Any) -> dict[str, Any]:
    """Return a copy of the passing itinerary with the steps named in ``changes`` updated."""
    itinerary = copy.deepcopy(ITINERARY)
    for step in itinerary["steps"]:
        step.update(changes.get(step["id"], {}))
    return itinerary


def test_a_well_formed_itinerary_passes() -> None:
    assert itinerary_problems(ITINERARY, RECORDS) == []


def test_an_unregistered_activity_is_reported() -> None:
    assert itinerary_problems(planted(derive={"activity": "intuition"}), RECORDS) == [
        "steps.derive: intuition is no registered activity"
    ]


def test_input_types_that_do_not_fill_the_activity_are_reported() -> None:
    itinerary = planted(derive={"inputs": [{"type": "data", "ref": "phen.readout"}]})
    assert itinerary_problems(itinerary, RECORDS) == [
        "steps.derive: derivation takes one input of admitted-laws or model, and the step gives 0",
        "steps.derive: derivation takes no input of type data",
    ]


def test_a_slot_taking_several_inputs_counts_them() -> None:
    step = {"id": "select", "activity": "model-selection",
            "inputs": [{"type": "model", "ref": "mod.kernel"}, {"type": "data", "ref": "phen.readout"}],
            "output": {"type": "ranking"}, "norm": {"test": "norm.model-selection", "verdict": "pending"}}
    itinerary = copy.deepcopy(ITINERARY)
    itinerary["steps"].append(step)
    assert itinerary_problems(itinerary, RECORDS) == [
        "steps.select: model-selection takes 2 or more inputs of model, and the step gives 1"
    ]
    step["inputs"].append({"type": "model", "ref": "derive"})
    assert itinerary_problems(itinerary, RECORDS) == ["steps.select: the step derive produces consequence, not model"]


def test_an_output_type_other_than_the_activity_output_is_reported() -> None:
    assert itinerary_problems(planted(derive={"output": {"type": "verdict"}}), RECORDS) == [
        "steps.derive: derivation produces consequence, and the step states verdict"
    ]


def test_an_input_reference_of_the_wrong_kind_or_to_nothing_is_reported() -> None:
    wrong = planted(derive={"inputs": [{"type": "model", "ref": "phen.readout"}]})
    assert itinerary_problems(wrong, RECORDS) == [
        "steps.derive: phen.readout holds data or phenomenon or knowledge-state-change, not model"
    ]
    absent = planted(derive={"inputs": [{"type": "model", "ref": "mod.missing"}]})
    assert itinerary_problems(absent, RECORDS) == ["steps.derive: mod.missing is neither a step nor a record"]
    answer = planted(derive={"inputs": [{"type": "model", "ref": "ans.kernel"}]})
    assert itinerary_problems(answer, RECORDS) == [
        "steps.derive: ans.kernel holds consequence or explanation or knowledge-state-change, not model"
    ]


def test_a_type_that_no_record_holds_is_reached_only_through_a_step() -> None:
    itinerary = planted(observe={"inputs": [{"type": "design", "ref": "quest.geometry"}]})
    assert itinerary_problems(itinerary, RECORDS) == [
        "steps.observe: no record holds a design, so its input names a step, and quest.geometry is none"
    ]


def test_an_output_reference_of_the_wrong_kind_is_reported() -> None:
    itinerary = planted(pose={"output": {"type": "problem", "ref": "quest.geometry"}})
    assert itinerary_problems(itinerary, RECORDS) == [
        "steps.pose: quest.geometry holds question or knowledge-state-change, not problem"
    ]


def test_a_norm_verdict_or_mode_outside_the_registries_is_reported() -> None:
    itinerary = planted(derive={"norm": {"test": "norm.simulation", "verdict": "likely"}, "mode": "inductive"})
    assert itinerary_problems(itinerary, RECORDS) == [
        "steps.derive: the norm of derivation is norm.derivation, and the step names norm.simulation",
        "steps.derive: 'likely' is no verdict",
        "steps.derive: derivation proceeds by deductive inference, and the step states inductive",
    ]


def test_a_cycle_among_the_steps_is_reported() -> None:
    itinerary = planted(design={"inputs": [{"type": "question", "ref": "quest.geometry"},
                                      {"type": "model", "ref": "mod.kernel"},
                                      {"type": "data", "ref": "observe"}]})
    found = itinerary_problems(itinerary, RECORDS)
    assert "steps: design -> observe -> design forms a cycle" in found
    assert cycles({"a": {"a"}}) == [["a", "a"]]


def test_a_itinerary_addressing_no_problem_or_question_and_a_repeated_step_are_reported() -> None:
    itinerary = copy.deepcopy(ITINERARY)
    itinerary["addresses"] = "phen.readout"
    itinerary["steps"].append(copy.deepcopy(itinerary["steps"][0]))
    assert itinerary_problems(itinerary, RECORDS)[:2] == [
        "addresses: phen.readout is no problem or question record",
        "steps: the identifier pose names several steps",
    ]


def fixture_itineraries() -> list[Path]:
    return sorted(EXAMPLES.glob("*/itinerary.yml")) if EXAMPLES.is_dir() else []


#: The fixtures whose itinerary still takes an answer record as a model, as the earlier design did.
EARLIER_ANSWER_DESIGN = {"grokking-delayed-generalization"}


def itinerary_cases() -> list[Any]:
    return [
        pytest.param(
            path,
            id=path.parent.name,
            marks=[pytest.mark.xfail(strict=True, reason="fixture follows the earlier answer design until the pilot migrates it (TODO model-design)")]
            if path.parent.name in EARLIER_ANSWER_DESIGN
            else [],
        )
        for path in fixture_itineraries()
    ]


@pytest.mark.skipif(not fixture_itineraries(), reason="no fixture carries an itinerary")
@pytest.mark.parametrize("path", itinerary_cases() or [Path("none")])
def test_every_itinerary_of_the_fixtures_passes(path: Path) -> None:
    records = {}
    for source in sorted(path.parent.glob("*.yml")):
        record = yaml.safe_load(source.read_text(encoding="utf-8"))
        if isinstance(record, dict) and "id" in record:
            records[str(record["id"])] = record
    itinerary = yaml.safe_load(path.read_text(encoding="utf-8"))
    assert itinerary_problems(itinerary, records) == []


def test_the_type_of_a_record_follows_from_its_state() -> None:
    """A schema is a question with a placeholder slot; commitment and status decide the other types."""
    records = {
        "quest.schema": {"type": "question", "subject": {"target_system": "system.a",
                                                         "phenomenon": {"placeholder": "observable"}}},
        "system.a": {"type": "target-system", "commitment": "identified"},
        "ans.a": {"type": "answer", "status": "entertained"},
        "mod.a": {"type": "model"},
        "prob.a": {"type": "problem"},
    }
    itinerary = {
        "addresses": "prob.a",
        "steps": [
            {"id": "select", "activity": "question-decomposition",
             "inputs": [{"type": "question", "ref": "quest.schema"}], "output": {"type": "question"},
             "norm": {"test": "norm.question-decomposition", "verdict": "pending"}},
            {"id": "predict", "activity": "model-prediction",
             "inputs": [{"type": "model", "ref": "mod.a"}, {"type": "target-specification", "ref": "system.a"}],
             "output": {"type": "consequence"}, "norm": {"test": "norm.model-prediction", "verdict": "pending"}},
            {"id": "judge", "activity": "testing",
             "inputs": [{"type": "hypothesis", "ref": "ans.a"}, {"type": "consequence", "ref": "predict"},
                        {"type": "data", "ref": "phen.none"}],
             "output": {"type": "verdict"}, "norm": {"test": "norm.testing", "verdict": "pending"}},
        ],
    }
    assert itinerary_problems(itinerary, records) == [
        "steps.select: quest.schema holds question-schema or knowledge-state-change, not question",
        "steps.predict: system.a holds identified-subject or classification or measurement-procedure"
        " or knowledge-state-change, not target-specification",
        "steps.judge: ans.a holds consequence or explanation or knowledge-state-change, not hypothesis",
        "steps.judge: phen.none is neither a step nor a record",
    ]
    records["quest.schema"]["subject"]["phenomenon"] = "phen.b"
    records["system.a"]["commitment"] = "specified"
    records["ans.a"]["status"] = "hypothesized"
    itinerary["steps"][2]["inputs"][2]["ref"] = "predict"
    assert itinerary_problems(itinerary, records) == ["steps.judge: the step predict produces consequence, not data"]


def test_a_specified_record_still_holds_an_identified_subject() -> None:
    """Commitment is cumulative for the identified subject, and strict for the target specification."""
    specified = {"type": "target-system", "commitment": "specified"}
    identified = {"type": "target-system", "commitment": "identified"}
    assert {"identified-subject", "target-specification"} <= set(record_types(specified, TYPES))
    assert "identified-subject" in record_types(identified, TYPES)
    assert "target-specification" not in record_types(identified, TYPES)
    assert "identified-subject" not in record_types({"type": "target-system"}, TYPES)
