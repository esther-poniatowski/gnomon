"""Itineraries of inquiry, checked against the registries of activities and product types.

The registries transcribe the taxonomy of epistemic activities, whose notes are the source of the
content, so the first tests check the registries against those notes. The remaining tests plant
one defect per check of :func:`gnomon.itineraries.itinerary_problems` in an itinerary that passes, and confirm
that the check reports it for the intended reason.
"""

from __future__ import annotations

import copy
import re
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
from gnomon.findings import texts

from .paths import EXAMPLES, ROOT

ACTIVITY_NOTES = ROOT / "docs" / "epistemology" / "processes" / "activities"
VOCABULARY = yaml.safe_load((ROOT / "src" / "gnomon" / "data" / "vocabularies.yml").read_text())
ACTS = activities()
TYPES = product_types()
ATTITUDES = {entry["value"] for entry in VOCABULARY["vocabularies"]["answer"][".status"]}


def test_the_registries_are_consistent() -> None:
    modes = [entry["value"] for entry in VOCABULARY["vocabularies"]["itinerary"]["steps.mode"]]
    assert malformed_registry(ACTS, TYPES, modes) == []


def test_a_registry_naming_an_unknown_type_mode_or_norm_is_reported() -> None:
    act = ACTS["derivation"]
    broken = {"derivation": type(act)(**{**act.__dict__, "output": "theorem", "mode": "intuitive",
                                         "norm": "norm.proof"})}
    assert texts(malformed_registry(broken, TYPES, ["deductive"])) == [
        "derivation: theorem is no product type",
        "derivation: intuitive is no admitted mode",
        "derivation: its norm norm.proof is not the test norm.derivation",
    ]


def test_a_registry_naming_an_unknown_attitude_is_reported() -> None:
    act = ACTS["testing"]
    claim = type(act.inputs[0])(frozenset({"target-claim"}), attitudes=frozenset({"believed"}))
    broken = {"testing": type(act)(**{**act.__dict__, "inputs": (claim, *act.inputs[1:])})}
    assert texts(malformed_registry(broken, TYPES, [act.mode])) == ["testing: believed is no attitude of an answer"]


def test_a_registry_restricting_an_output_to_an_unknown_value_is_reported() -> None:
    act = ACTS["experimental-design"]
    assert act.output_values == {"kind": ("experiment", "simulation-run")}
    broken = {act.id: type(act)(**{**act.__dict__, "output_values": {"kind": ("experiment", "survey")}})}
    assert texts(malformed_registry(broken, TYPES, [act.mode])) == ["experimental-design: survey is no kind of a design"]


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

    >>> sorted(typed("`target-claim \\| model` (hypothesized), `data` (several)"))
    ['data', 'model', 'target-claim']
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
    qualifiers = {word.strip() for group in re.findall(r"\(([^)]*)\)", inputs) for word in group.split(",")}
    assert qualifiers & ATTITUDES == {a for s in act.inputs for a in s.attitudes}
    assert ("optional" in qualifiers) == any(s.least == 0 for s in act.inputs)
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
def test_the_classes_of_the_product_types_are_those_of_the_inventory() -> None:
    """Each type takes the class under which the inventory of epistemic objects lists it."""
    inventory = (ROOT / "docs/epistemology/objects/status/epistemic-objects.md").read_text(encoding="utf-8")
    labels = {"Claim types": "claim", "Construct types": "construct", "Types not yet classed": "unclassed",
              "Evaluative types": "evaluative", "Types outside these classes": "other"}
    listed = {}
    for label, token in labels.items():
        line = re.search(rf"^- \*\*{label}\*\*[^:]*: (.*)$", inventory, re.M)
        assert line is not None, f"the inventory lists no {label.lower()}"
        names = re.split(r", | and ", line.group(1).split(". ")[0].rstrip("."))
        listed.update({name.strip().replace(" ", "-"): token for name in names})
    registry = yaml.safe_load((ROOT / "src/gnomon/data/registries/product-types.yml").read_text())
    assert {entry["id"]: entry["class"] for entry in registry["product_types"]} == listed


def test_the_registry_lists_the_product_types_of_the_overview() -> None:
    """The taxonomy owns the list of types, and the registry states the coverage of each."""
    registry = yaml.safe_load((ROOT / "src/gnomon/data/registries/product-types.yml").read_text())
    entries = registry["product_types"]
    assert sorted(entry["id"] for entry in entries) == sorted(PRODUCT_ROWS)
    assert {entry["id"]: entry["status"] for entry in entries if entry["status"] not in COVERAGE} == {}


# An itinerary that passes every check, over records that the planted cases modify one at a time.
RECORDS: dict[str, dict[str, Any]] = {
    "prob.geometry": {"type": "problem"},
    "quest.geometry": {"type": "question", "request": "one"},
    "system.networks": {"type": "target-system"},
    "phen.readout": {"type": "phenomenon", "data": [{"pointer": "doi:10.1000/recordings"}]},
    "ans.kernel": {"type": "answer"},
    "mod.kernel": {"type": "model"},
}
ITINERARY: dict[str, Any] = {
    "id": "itin.geometry.route",
    "type": "itinerary",
    "addresses": "prob.geometry",
    "steps": [
        {"id": "pose", "activity": "problematization",
         "inputs": [{"type": "source", "ref": "doi:10.1000/anomaly"}],
         "output": {"type": "problem", "ref": "prob.geometry"},
         "norm": {"test": "norm.problematization", "verdict": "pass", "evidence": "The demand is stated.",
                  "judged": "2026-11-03"}, "mode": "non-inferential"},
        {"id": "derive", "activity": "derivation",
         "inputs": [{"type": "model", "ref": "mod.kernel"}],
         "output": {"type": "consequence"},
         "norm": {"test": "norm.derivation", "verdict": "pending"}, "mode": "deductive"},
        {"id": "design", "activity": "experimental-design",
         "inputs": [{"type": "question", "ref": "quest.geometry"}, {"type": "model", "ref": "mod.kernel"}],
         "output": {"type": "design"},
         "norm": {"test": "norm.experimental-design", "verdict": "pending"}},
        {"id": "observe", "activity": "observation",
         "inputs": [{"type": "design", "ref": "itin.geometry.route.design"}],
         "output": {"type": "data"},
         "norm": {"test": "norm.observation", "verdict": "pending"}},
    ],
}


def served(itinerary: dict[str, Any]) -> dict[str, Any]:
    """Return the itinerary with a rationale that serves its problem on every step that states none."""
    for step in itinerary.get("steps") or []:
        step.setdefault("rationale", {"serves": itinerary.get("addresses")})
    return itinerary


def planted(**changes: Any) -> dict[str, Any]:
    """Return a copy of the passing itinerary with the steps named in ``changes`` updated."""
    itinerary = copy.deepcopy(ITINERARY)
    for step in itinerary["steps"]:
        step.update(changes.get(step["id"], {}))
    return itinerary


def test_a_well_formed_itinerary_passes() -> None:
    assert itinerary_problems(served(ITINERARY), RECORDS) == []


def test_an_unregistered_activity_is_reported() -> None:
    assert texts(itinerary_problems(served(planted(derive={"activity": "intuition"})), RECORDS)) == [
        "steps.derive: intuition is no registered activity"
    ]


def test_input_types_that_do_not_fill_the_activity_are_reported() -> None:
    itinerary = planted(derive={"inputs": [{"type": "data", "ref": "phen.readout"}]})
    assert texts(itinerary_problems(served(itinerary), RECORDS)) == [
        "steps.derive: derivation takes one input of admitted-laws or model or target-claim, and the step gives 0",
        "steps.derive: derivation takes no input of type data",
    ]


def test_a_slot_taking_several_inputs_counts_them() -> None:
    step = {"id": "select", "activity": "model-selection",
            "inputs": [{"type": "model", "ref": "mod.kernel"}, {"type": "data", "ref": "phen.readout"}],
            "output": {"type": "ranking"}, "norm": {"test": "norm.model-selection", "verdict": "pending"}}
    itinerary = copy.deepcopy(ITINERARY)
    itinerary["steps"].append(step)
    assert texts(itinerary_problems(served(itinerary), RECORDS)) == [
        "steps.select: model-selection takes 2 or more inputs of model, and the step gives 1"
    ]
    step["inputs"].append({"type": "model", "ref": "itin.geometry.route.derive"})
    assert texts(itinerary_problems(served(itinerary), RECORDS)) == ["steps.select: the step itin.geometry.route.derive produces consequence, not model"]


def test_an_output_type_other_than_the_activity_output_is_reported() -> None:
    assert texts(itinerary_problems(served(planted(derive={"output": {"type": "verdict"}})), RECORDS)) == [
        "steps.derive: derivation produces consequence, and the step states verdict"
    ]


def test_an_input_reference_of_the_wrong_kind_or_to_nothing_is_reported() -> None:
    wrong = planted(derive={"inputs": [{"type": "model", "ref": "phen.readout"}]})
    assert texts(itinerary_problems(served(wrong), RECORDS)) == [
        "steps.derive: phen.readout holds data or phenomenon, not model"
    ]
    absent = planted(derive={"inputs": [{"type": "model", "ref": "mod.missing"}]})
    assert texts(itinerary_problems(served(absent), RECORDS)) == ["steps.derive: mod.missing is neither a step nor a record"]
    answer = planted(derive={"inputs": [{"type": "model", "ref": "ans.kernel"}]})
    assert texts(itinerary_problems(served(answer), RECORDS)) == [
        "steps.derive: ans.kernel holds target-claim, not model"
    ]


def unrecorded_design() -> dict[str, Any]:
    """Return the product types with `design` held by no record, so that a planted case can reach that rule."""
    types = dict(product_types())
    types["design"] = {**types["design"], "record": "to-create"}
    return types


def test_a_type_that_no_record_holds_is_reached_only_through_a_step() -> None:
    itinerary = planted(observe={"inputs": [{"type": "design", "ref": "quest.geometry"}]})
    assert texts(itinerary_problems(served(itinerary), RECORDS, types=unrecorded_design())) == [
        "steps.observe: no record holds a design, so its input names a step, and quest.geometry is none"
    ]


def test_an_output_whose_value_the_activity_does_not_produce_is_reported() -> None:
    """Experimental design outputs protocols; a design of the kind `method` comes from method design."""
    records = {**RECORDS, "design.geometry.protocol": {"type": "design", "kind": "method"}}
    itinerary = planted(design={"output": {"type": "design", "ref": "design.geometry.protocol"}})
    assert texts(itinerary_problems(served(itinerary), records)) == [
        "steps.design: design.geometry.protocol has the kind method, and experimental-design produces"
        " a design of the kind experiment or simulation-run"
    ]
    records["design.geometry.protocol"] = {"type": "design", "kind": "simulation-run"}
    assert itinerary_problems(served(itinerary), records) == []


def test_an_output_reference_of_the_wrong_kind_is_reported() -> None:
    itinerary = planted(pose={"output": {"type": "problem", "ref": "quest.geometry"}})
    assert texts(itinerary_problems(served(itinerary), RECORDS)) == [
        "steps.pose: quest.geometry holds question, not problem"
    ]


def test_a_norm_verdict_or_mode_outside_the_registries_is_reported() -> None:
    itinerary = planted(derive={"norm": {"test": "norm.simulation", "verdict": "likely"}, "mode": "inductive"})
    assert texts(itinerary_problems(served(itinerary), RECORDS)) == [
        "steps.derive: the norm of derivation is norm.derivation, and the step names norm.simulation",
        "steps.derive: 'likely' is no verdict",
        "steps.derive: derivation proceeds by deductive inference, and the step states inductive",
    ]


def test_a_cycle_among_the_steps_is_reported() -> None:
    itinerary = planted(design={"inputs": [{"type": "question", "ref": "quest.geometry"},
                                      {"type": "model", "ref": "mod.kernel"},
                                      {"type": "data", "ref": "itin.geometry.route.observe"}]})
    found = itinerary_problems(served(itinerary), RECORDS)
    assert "steps: design -> observe -> design forms a cycle" in texts(found)
    assert cycles({"a": {"a"}}) == [["a", "a"]]


def test_a_itinerary_addressing_no_problem_or_question_and_a_repeated_step_are_reported() -> None:
    itinerary = copy.deepcopy(ITINERARY)
    itinerary["addresses"] = "phen.readout"
    itinerary["steps"].append(copy.deepcopy(itinerary["steps"][0]))
    assert texts(itinerary_problems(served(itinerary), RECORDS))[:2] == [
        "addresses: phen.readout is no problem or question record",
        "steps: the identifier pose names several steps",
    ]


def test_the_type_of_a_record_follows_from_its_state() -> None:
    """A schema is a question with a placeholder slot; commitment and status decide the other types."""
    records = {
        "quest.schema": {"type": "question", "request": "one", "subject": {"target_system": "system.a",
                                                         "phenomenon": {"placeholder": "phenomenon"}}},
        "system.a": {"type": "target-system", "commitment": "identified"},
        "ans.a": {"type": "answer", "status": "entertained"},
        "mod.a": {"type": "model"},
        "prob.a": {"type": "problem"},
    }
    itinerary = {
        "id": "itin.a.route",
        "addresses": "prob.a",
        "steps": [
            {"id": "select", "activity": "question-decomposition",
             "inputs": [{"type": "question", "ref": "quest.schema"}], "output": {"type": "question"},
             "norm": {"test": "norm.question-decomposition", "verdict": "pending"}},
            {"id": "predict", "activity": "model-prediction",
             "inputs": [{"type": "model", "ref": "mod.a"}, {"type": "target-specification", "ref": "system.a"}],
             "output": {"type": "consequence"}, "norm": {"test": "norm.model-prediction", "verdict": "pending"}},
            {"id": "judge", "activity": "testing",
             "inputs": [{"type": "target-claim", "ref": "ans.a"}, {"type": "consequence", "ref": "itin.a.route.predict"},
                        {"type": "data", "ref": "phen.none"}],
             "output": {"type": "verdict"}, "norm": {"test": "norm.testing", "verdict": "pending"}},
        ],
    }
    assert texts(itinerary_problems(served(itinerary), records)) == [
        "steps.select: quest.schema holds question-schema, not question",
        "steps.predict: system.a holds identified-subject, not target-specification",
        "steps.judge: ans.a is entertained, and testing takes a target-claim held as hypothesized",
        "steps.judge: phen.none is neither a step nor a record",
    ]
    records["quest.schema"]["subject"]["phenomenon"] = "phen.b"
    records["system.a"]["commitment"] = "specified"
    records["ans.a"]["status"] = "hypothesized"
    itinerary["steps"][2]["inputs"][2]["ref"] = "itin.a.route.predict"
    assert texts(itinerary_problems(served(itinerary), records)) == ["steps.judge: the step itin.a.route.predict produces consequence, not data"]


def test_an_attitude_restricts_an_answer_only() -> None:
    """A qualifier of attitude binds an answer; a model in the same slot, or an output, is unaffected."""
    records = {
        "prob.a": {"type": "problem"},
        "mod.a": {"type": "model", "status": "provisional"},
        "ans.a": {"type": "answer", "status": "accepted"},
        "phen.a": {"type": "phenomenon"},
    }

    def step(activity: str, inputs: list[dict[str, str]], output: dict[str, str]) -> dict[str, Any]:
        return {"addresses": "prob.a", "steps": [{"id": "act", "activity": activity, "inputs": inputs,
                "output": output, "norm": {"test": f"norm.{activity}", "verdict": "pending"}}]}

    on_model = step("critique", [{"type": "model", "ref": "mod.a"}], {"type": "verdict"})
    assert texts(itinerary_problems(served(on_model), records)) == []
    on_answer = step("critique", [{"type": "target-claim", "ref": "ans.a"}], {"type": "verdict"})
    assert texts(itinerary_problems(served(on_answer), records)) == [
        "steps.act: ans.a is accepted, and critique takes a target-claim held as hypothesized"
    ]
    produced = step("abduction", [{"type": "phenomenon", "ref": "phen.a"}], {"type": "target-claim", "ref": "ans.a"})
    assert texts(itinerary_problems(served(produced), records)) == []


def test_an_explanation_may_run_on_the_target_description() -> None:
    """The input model of an explanation is optional: a route on the target description takes none."""
    records = {"prob.a": {"type": "problem"}, "phen.a": {"type": "phenomenon"}, "mod.a": {"type": "model"},
               "quest.a": {"type": "question", "request": "one", "subject": {"phenomenon": "phen.a"}}}
    inputs = [{"type": "phenomenon", "ref": "phen.a"}, {"type": "question", "ref": "quest.a"}]

    def explain(given: list[dict[str, str]]) -> dict[str, Any]:
        return {"addresses": "prob.a", "steps": [{"id": "explain", "activity": "explanation", "inputs": given,
                "output": {"type": "explanation"}, "norm": {"test": "norm.explanation", "verdict": "pending"}}]}

    assert texts(itinerary_problems(served(explain(inputs)), records)) == []
    assert texts(itinerary_problems(served(explain([*inputs, {"type": "model", "ref": "mod.a"}])), records)) == []
    twice = [*inputs, {"type": "model", "ref": "mod.a"}, {"type": "model", "ref": "mod.a"}]
    assert texts(itinerary_problems(served(explain(twice)), records)) == [
        "steps.explain: explanation takes at most one input of model, and the step gives 2"
    ]


def test_a_question_without_a_request_stays_a_schema() -> None:
    """Identified slots make the possible answers definite; the request then fixes the direct answers."""
    question = {"type": "question", "subject": {"target_system": "system.a", "phenomenon": "phen.a"}}
    assert {"question-schema"} == {"question-schema", "question"} & set(record_types(question, TYPES))
    question["request"] = "all"
    assert {"question"} == {"question-schema", "question"} & set(record_types(question, TYPES))


def test_a_specified_record_still_holds_an_identified_subject() -> None:
    """Commitment is cumulative for the identified subject, and strict for the target specification."""
    specified = {"type": "target-system", "commitment": "specified"}
    identified = {"type": "target-system", "commitment": "identified"}
    assert {"identified-subject", "target-specification"} <= set(record_types(specified, TYPES))
    assert "identified-subject" in record_types(identified, TYPES)
    assert "target-specification" not in record_types(identified, TYPES)
    assert "identified-subject" not in record_types({"type": "target-system"}, TYPES)


def test_a_step_is_referenced_by_its_full_identifier() -> None:
    """A reference names a step by the identifier of the itinerary followed by that of the step."""
    short = planted(observe={"inputs": [{"type": "design", "ref": "design"}]})
    assert texts(itinerary_problems(served(short), RECORDS, types=unrecorded_design())) == [
        "steps.observe: no record holds a design, so its input names a step, and design is none"
    ]


def test_a_judged_verdict_states_its_evidence_and_its_date() -> None:
    itinerary = planted(derive={"norm": {"test": "norm.derivation", "verdict": "fail", "judged": "03/11/2026"}})
    assert texts(itinerary_problems(served(itinerary), RECORDS)) == [
        "steps.derive: the verdict fail states no evidence",
        "steps.derive: the verdict fail states no date of judgment, written YYYY-MM-DD",
    ]


def test_a_step_serves_a_question_or_a_problem_and_names_what_it_acts_on() -> None:
    itinerary = planted(derive={"rationale": {"serves": "quest.geometry"}},
                        design={"rationale": {"serves": "mod.kernel", "acts_on": "access"}})
    assert texts(itinerary_problems(served(itinerary), RECORDS)) == [
        "steps.derive: the rationale serves a question and names no condition or act among access, answer-type, "
        "bridging, candidates, definiteness, discrimination, evaluation, obtaining, representation, soundness",
        "steps.design: the rationale serves mod.kernel, which is no question or problem record",
    ]


def test_an_input_named_as_of_a_revision_is_read_at_that_revision() -> None:
    """A step stays valid once its record is revised, since it names the state that it read."""
    then = {"type": "model"}
    itinerary = planted(derive={"inputs": [{"type": "model", "ref": "mod.earlier", "as_of": "abc123"}]})
    revised = {**RECORDS, "mod.earlier": {"type": "answer"}}
    assert itinerary_problems(served(itinerary), revised, states=lambda ident, rev: then) == []
    assert texts(itinerary_problems(served(itinerary), revised, states=lambda ident, rev: None)) == [
        "steps.derive: mod.earlier cannot be read at the revision abc123"
    ]
    assert texts(itinerary_problems(served(itinerary), revised)) == [
        "steps.derive: mod.earlier cannot be read at the revision abc123"
    ]


def test_the_history_reads_a_record_at_a_revision_of_its_repository() -> None:
    from gnomon.history import git_states

    path = EXAMPLES / "grokking-delayed-generalization" / "question.yml"
    ident = yaml.safe_load(path.read_text(encoding="utf-8"))["id"]
    read = git_states({ident: path})
    assert (read(ident, "HEAD") or {}).get("id") == ident
    assert read(ident, "no-such-revision") is None
    assert read("quest.absent", "HEAD") is None


def test_a_branch_names_a_condition_and_an_alternative_of_the_same_output() -> None:
    itinerary = planted(derive={"branch": {"otherwise": "observe"}, "iterate": {"until": "the bound is tight"}})
    assert texts(itinerary_problems(served(itinerary), RECORDS)) == [
        "steps.derive: the branch states no condition",
        "steps.derive: the branch names no step that produces consequence otherwise",
        "steps.derive: derivation takes no input of its output type consequence, so it cannot repeat on it",
    ]


def test_a_well_formed_branch_passes() -> None:
    itinerary = served(planted(derive={"branch": {"condition": "a closed form is found", "otherwise": "simulate"}}))
    itinerary["steps"].append({"id": "simulate", "activity": "simulation",
                               "inputs": [{"type": "model", "ref": "mod.kernel"},
                                          {"type": "design", "ref": "itin.geometry.route.design"}],
                               "output": {"type": "consequence"}, "rationale": {"serves": "prob.geometry"},
                               "norm": {"test": "norm.simulation", "verdict": "pending"}})
    assert itinerary_problems(itinerary, RECORDS) == []


def test_a_change_of_knowledge_state_differs_from_the_status_before_it() -> None:
    records = {**RECORDS, "ans.kernel": {"type": "answer", "status": "accepted"},
               "assess.kernel": {"type": "assessment", "tests": {"warrant": {}}}}
    step = {"id": "accept", "activity": "belief-revision", "inputs": [{"type": "verdict", "ref": "assess.kernel"}],
            "output": {"type": "knowledge-state-change", "ref": "ans.kernel", "before": "abc123"},
            "norm": {"test": "norm.belief-revision", "verdict": "pending"}, "rationale": {"serves": "prob.geometry"}}
    itinerary = served(copy.deepcopy(ITINERARY))
    itinerary["steps"].append(step)
    assert itinerary_problems(itinerary, records, states=lambda i, r: {"status": "hypothesized"}) == []
    assert texts(itinerary_problems(itinerary, records, states=lambda i, r: {"status": "accepted"})) == [
        "steps.accept: the status of ans.kernel is accepted before and after the step"
    ]
