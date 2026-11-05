"""The checks of a derivation record and its registry.

The registry of derivations restates three rules of the theory notes, so its kinds are checked
against the vocabularies of the record and its admitted pairs against the table of the note on
interpretation. Each check is shown to fire on one planted defect of the worked derivation, which
carries none.
"""

from __future__ import annotations

import copy
import re
import shutil
from pathlib import Path
from typing import Any, Callable

import pytest
import yaml

from gnomon.check import check_workspace, load_workspace
from gnomon.derivations import (
    SCHEMA,
    derivation_problems,
    internal_fields,
    load_registry,
    unrecorded_descents,
)
from gnomon.findings import RULES

ROOT = Path(__file__).resolve().parents[2]
EXAMPLE = ROOT / "examples" / "grokking-delayed-generalization"
NOTE = ROOT / "docs" / "epistemology" / "objects" / "derivation" / "interpretation.md"
SPEC = ROOT / "docs" / "specification" / "derivation.md"
VOCABULARIES = ROOT / "src" / "gnomon" / "data" / "vocabularies.yml"

#: The items of the table of admitted pairs, by the label of their row in the note.
ITEM_ROWS = {
    "object": "object",
    "expression": "expression",
    "transformation": "transformation",
    "feature of the calculation": "feature",
    "composite": "composite",
}


def values(key: str) -> set[str]:
    """Return the values of one vocabulary of the derivation record."""
    registry = yaml.safe_load(VOCABULARIES.read_text(encoding="utf-8"))
    return {entry["value"] for entry in registry["vocabularies"]["derivation"][key]}


def worked() -> dict[str, Any]:
    """Return the worked derivation, as a record that a test may change."""
    loaded: dict[str, Any] = yaml.safe_load((EXAMPLE / "derivation.yml").read_text("utf-8"))
    return copy.deepcopy(loaded)


def unit(record: dict[str, Any], name: str, ident: str) -> dict[str, Any]:
    """Return the entry of a list of the record that carries an identifier."""
    entry: dict[str, Any] = next(e for e in record[name] if e.get("id") == ident)
    return entry


def test_registry_kinds_are_vocabulary_values() -> None:
    registry = load_registry()
    kinds = values("interpretations.kind")
    assert set(registry["non_routine_kinds"]) <= values("moves.kind")
    assert {k for ks in registry["cited_kinds"].values() for k in ks} <= kinds
    assert set(registry["ground_types"]) == kinds
    classes = {c for cs in registry["ground_types"].values() for c in cs}
    assert classes <= {"reference", "objects", "moves", "posits", "slots", "features"}
    assert {k for ks in registry["admitted_pairs"].values() for k in ks} <= kinds
    assert set(registry["confirming_tests"]) <= values("posits.tests.kind")
    assert registry["confirming_computation"] in values("posits.tests.standard")


#: The fields that name other records, by their dotted identifiers, rather than units of the record.
RECORD_FIELDS = {("serves",), ("runs_on",), ("uses",)}


def test_every_field_naming_a_unit_declares_its_lists() -> None:
    """A label field whose template names a unit of the record declares the lists it admits, so
    that no such field escapes the resolution of the record."""
    declared = {path for path, _, _ in internal_fields()}
    schema = yaml.safe_load(SCHEMA.read_text(encoding="utf-8"))
    naming: set[tuple[str, ...]] = set()

    def walk(node: dict[str, Any], path: tuple[str, ...]) -> None:
        for key, sub in (node.get("properties") or {}).items():
            here = (*path, key)
            template = str(
                sub.get("x-template") or (sub.get("items") or {}).get("x-template") or ""
            )
            label = "label" in (sub.get("x-kind"), (sub.get("items") or {}).get("x-kind"))
            declaring = key in ("id", "symbol") or here in RECORD_FIELDS
            if label and not declaring and re.fullmatch(r"[A-Z]+(-[A-Z]+)*", template):
                naming.add(here)
            walk(sub, here)
            if isinstance(sub.get("items"), dict):
                walk(sub["items"], here)

    walk(schema, ())
    assert naming - declared == set()


def test_the_specification_lists_every_rule_of_a_derivation() -> None:
    """The list of checks of the specification is the one statement of the checks, so it names
    exactly the rules of a derivation that the catalogue declares."""
    text = SPEC.read_text(encoding="utf-8")
    listed = set(re.findall(r"`(derivation/[a-z-]+)`", text[text.index("^derivation-checks") :]))
    declared = {rule.id for rule in RULES if rule.id.startswith("derivation/")}
    assert listed == declared


def test_admitted_pairs_match_the_note() -> None:
    lines = NOTE.read_text(encoding="utf-8").splitlines()
    start = next(i for i, line in enumerate(lines) if line.rstrip().endswith("^admitted-pairs"))
    header = next(line for line in lines[start:] if line.startswith("| Item"))
    kinds = [cell.strip() for cell in header.strip("|").split("|")][1:]
    table: dict[str, list[str]] = {}
    for line in lines[lines.index(header) + 2 :]:
        if not line.startswith("|"):
            break
        cells = [cell.strip() for cell in line.strip("|").split("|")]
        table[ITEM_ROWS[cells[0]]] = [
            k for k, cell in zip(kinds, cells[1:], strict=True) if cell == "✓"
        ]
    assert table == load_registry()["admitted_pairs"]


def test_worked_derivation_has_no_finding() -> None:
    assert not derivation_problems(worked())


def test_worked_workspace_has_no_finding() -> None:
    assert not check_workspace(load_workspace(EXAMPLE))


Change = Callable[[dict[str, Any]], None]


def _set(name: str, ident: str, key: str, value: Any) -> Change:
    def change(record: dict[str, Any]) -> None:
        unit(record, name, ident)[key] = value

    return change


def _warrant(ident: str, key: str, value: Any) -> Change:
    def change(record: dict[str, Any]) -> None:
        unit(record, "moves", ident)["warrant"][key] = value

    return change


def _avoidable_kernel(record: dict[str, Any]) -> None:
    record["kernel"] = "solve-modes"
    record["segments"] = []
    record["moves"].append(
        {"id": "shortcut", "kind": "estimate", "inputs": ["modal-flow"], "outputs": ["mode-decay"]}
    )


def _cycle(record: dict[str, Any]) -> None:
    unit(record, "moves", "diagonalize")["inputs"].append("delay-law")


def _cycle_through_segment(record: dict[str, Any]) -> None:
    record["segments"].append(
        {"id": "loop", "inputs": ["delay-law"], "outputs": ["hessian"], "moves": []}
    )
    record["orientations"].append(
        {"id": "o-loop", "of": "loop", "purpose": "to loop", "change": "reduce"}
    )


def _detour(record: dict[str, Any]) -> None:
    record["objects"].append({"id": "stray", "form": "object", "reading": "an unused object"})
    record["moves"].append(
        {"id": "detour", "kind": "rescale", "inputs": ["mode-decay"], "outputs": ["stray"]}
    )


def _late_interpretation(field: str) -> Change:
    def change(record: dict[str, Any]) -> None:
        record["interpretations"].append(
            {"id": "late", "of": "delay-law", "kind": "structural", "reading": "a late property"}
        )
        if field == "occasion":
            unit(record, "orientations", "find-the-law")["occasion"] = "late"
        else:
            unit(record, "moves", "diagonalize")["warrant"]["applies_because"] = "late"

    return change


def _bridge(record: dict[str, Any]) -> None:
    unit(record, "segments", "relaxation")["inputs"].remove("hessian")


def _orphan(record: dict[str, Any]) -> None:
    record["objects"].append({"id": "orphan", "form": "expression", "reading": "an orphan"})
    unit(record, "consequences", "scale-law")["from"] = "orphan"


def _serves_and_states(record: dict[str, Any]) -> None:
    record["serves"] = "mod.grokking.effective-representation.representation_time"


def _premise_variation(record: dict[str, Any]) -> None:
    entry = unit(record, "interpretations", "hessian-symmetric")
    entry.update(of="mod.grokking.effective-representation.Hrep", kind="variation")


def _act(record: dict[str, Any]) -> None:
    unit(record, "moves", "keep-dependence")["warrant"]["source"] = "act-verdict"


def _unbound_upper(record: dict[str, Any]) -> None:
    unit(record, "moves", "solve-modes")["binds"] = ["B"]


def _diagnosis(record: dict[str, Any], grounds: list[str]) -> None:
    """Plant a feature of the calculation and the diagnostic interpretation that reads it."""
    record["features"] = [{"id": "stall", "kind": "divergence", "at": "crossing-time"}]
    record["interpretations"].append(
        {"id": "stalled", "of": "stall", "kind": "diagnostic", "reading": "x", "grounds": grounds}
    )


def _groundless_diagnosis(record: dict[str, Any]) -> None:
    _diagnosis(record, [])


def _impasse_elsewhere(record: dict[str, Any]) -> None:
    unit(record, "moves", "solve-modes")["binds"] = []
    _diagnosis(record, ["slowest-dominates"])
    record["impasses"] = [{"sought": "threshold-time", "obstacle": "stalled"}]


#: Each planted defect of the worked derivation, with the rule that reports it and a fragment of
#: the text of the finding, so that a finding of the right rule at the wrong place does not pass.
PLANTED: dict[str, tuple[Change, str, str]] = {
    "repeated identifier": (
        _set("objects", "hessian", "id", "diagonalize"),
        "derivation/repeated-unit",
        "diagonalize: the identifier names several units",
    ),
    "unknown input": (
        _set("moves", "crossing", "inputs", ["slowest-mode", "ghost"]),
        "derivation/unknown-unit",
        "moves.crossing.inputs: ghost names no unit",
    ),
    "unknown license": (
        _warrant("diagonalize", "applies_because", "ghost"),
        "derivation/unknown-unit",
        "moves.diagonalize.warrant.applies_because: ghost names no unit among interpretations",
    ),
    "uppercase slot": (
        _unbound_upper,
        "derivation/unknown-unit",
        "moves.solve-modes.binds: B names no unit among slots",
    ),
    "unknown tester": (
        _set("posits", "quality-tracks-slow-mode", "tests", [{"kind": "limit", "by": "ghost"}]),
        "derivation/unknown-unit",
        "posits.quality-tracks-slow-mode.tests.0.by: ghost names no unit among moves",
    ),
    "unadmitted pair": (
        _set("interpretations", "hessian-symmetric", "kind", "variation"),
        "derivation/unadmitted-pair",
        "interpretations.hessian-symmetric: a object admits no variation interpretation",
    ),
    "unadmitted premise": (
        _premise_variation,
        "derivation/unadmitted-pair",
        "interpretations.hessian-symmetric: a premise admits no variation interpretation",
    ),
    "groundless diagnosis": (
        _groundless_diagnosis,
        "derivation/mistyped-ground",
        "interpretations.stalled: a diagnostic interpretation cites no ground",
    ),
    "groundless magnitude": (
        _set("interpretations", "spectral-gap", "grounds", []),
        "derivation/mistyped-ground",
        "interpretations.spectral-gap: a magnitude interpretation cites no ground",
    ),
    "structural principle": (
        _set("consequences", "scale-law", "principle", "hessian-symmetric"),
        "derivation/mistyped-ground",
        "consequences.scale-law.principle: hessian-symmetric is a structural interpretation",
    ),
    "cycle": (_cycle, "derivation/cycle", "depend on one another in a cycle"),
    "cycle through a segment": (_cycle_through_segment, "derivation/cycle", "loop"),
    "late occasion of a segment": (
        _late_interpretation("occasion"),
        "derivation/retrospective-orientation",
        "orientations.find-the-law.occasion: late interprets delay-law, which relaxation",
    ),
    "late license": (
        _late_interpretation("applies_because"),
        "derivation/retrospective-license",
        "moves.diagonalize.warrant.applies_because: late interprets delay-law",
    ),
    "ambiguous purpose": (
        _set("orientations", "isolate-slow-mode", "determines", "threshold-time"),
        "derivation/ambiguous-purpose",
        "orientations.isolate-slow-mode: the purpose states both",
    ),
    "unoriented move": (
        _set("orientations", "time-the-crossing", "of", "keep-dependence"),
        "derivation/unoriented-move",
        "moves.crossing: the move is non-routine by the posit that it uses",
    ),
    "unoriented segment": (
        _set("orientations", "find-the-law", "of", "keep-dependence"),
        "derivation/unoriented-move",
        "segments.relaxation: no orientation selects the segment",
    ),
    "imported output": (
        _act,
        "derivation/unoriented-move",
        "moves.keep-dependence: the move is non-routine by the output of an act that it imports",
    ),
    "broken bridge": (
        _bridge,
        "derivation/broken-bridge",
        "segments.relaxation: the move diagonalize takes hessian",
    ),
    "avoidable kernel": (
        _avoidable_kernel,
        "derivation/failed-kernel",
        "kernel: a route from the premises reaches delay-law without the kernel solve-modes",
    ),
    "unreached consequence": (
        _orphan,
        "derivation/unreached-consequence",
        "consequences.scale-law: no move and no segment yields orphan",
    ),
    "unrecorded consequence": (
        _set("consequences", "scale-law", "record", None),
        "derivation/unrecorded-consequence",
        "consequences.scale-law: a consequence of the root sought names no record",
    ),
    "restated sought": (
        _serves_and_states,
        "derivation/restated-fact",
        "sought: the derivation serves mod.grokking.effective-representation.representation_time",
    ),
    "unbound slot": (
        _set("moves", "solve-modes", "binds", []),
        "derivation/unbound-slot",
        "slots.a_mode: no move binds the slot",
    ),
    "impasse on another route": (
        _impasse_elsewhere,
        "derivation/unbound-slot",
        "slots.a_mode: no move binds the slot",
    ),
    "idle move": (
        _detour,
        "derivation/idle-move",
        "moves.detour: the outputs of the move reach no outcome",
    ),
    "cyclic nesting": (
        _set("segments", "relaxation", "within", "relaxation"),
        "derivation/cyclic-nesting",
        "segments: relaxation -> relaxation enclose one another in a cycle",
    ),
}


@pytest.mark.parametrize("case", sorted(PLANTED))
def test_each_check_fires_on_its_planted_defect(case: str) -> None:
    change, rule, fragment = PLANTED[case]
    record = worked()
    change(record)
    texts = [f.text for f in derivation_problems(record) if f.rule.id == rule]
    assert any(fragment in text for text in texts), texts


def test_a_move_carrying_a_test_of_a_posit_is_not_idle() -> None:
    record = worked()
    _detour(record)
    unit(record, "posits", "quality-tracks-slow-mode")["tests"] = [
        {"kind": "consistency", "verdict": "supports", "by": "detour"}
    ]
    assert "derivation/idle-move" not in {f.rule.id for f in derivation_problems(record)}


def test_a_move_without_a_warrant_is_a_gap(tmp_path: Path) -> None:
    folder = tmp_path / EXAMPLE.name
    shutil.copytree(EXAMPLE, folder)
    path = folder / "derivation.yml"
    record = yaml.safe_load(path.read_text(encoding="utf-8"))
    unit(record, "moves", "solve-modes").pop("warrant")
    path.write_text(yaml.safe_dump(record, sort_keys=False), encoding="utf-8")
    texts = [located.finding.text for located in check_workspace(load_workspace(folder))]
    assert "always required: moves[].warrant.error" in texts, texts


def test_the_record_of_a_consequence_is_a_derived_law(tmp_path: Path) -> None:
    folder = tmp_path / EXAMPLE.name
    shutil.copytree(EXAMPLE, folder)
    path = folder / "derivation.yml"
    record = yaml.safe_load(path.read_text(encoding="utf-8"))
    flow = "mod.grokking.effective-representation.representation_flow"
    unit(record, "consequences", "scale-law")["record"] = flow
    path.write_text(yaml.safe_dump(record, sort_keys=False), encoding="utf-8")
    texts = [
        located.finding.text
        for located in check_workspace(load_workspace(folder))
        if located.finding.rule.id == "derivation/underived-record"
    ]
    assert texts == [f"consequences.scale-law.record: {flow} is a law marked posited, not derived"]


DERIVATIONS = sorted((ROOT / "examples").glob("*/derivation.yml"))


@pytest.mark.parametrize("path", DERIVATIONS, ids=lambda p: p.parent.name)
def test_every_worked_derivation_has_no_finding(path: Path) -> None:
    assert not derivation_problems(yaml.safe_load(path.read_text(encoding="utf-8")))


def test_a_derived_law_without_its_derivation_is_reported(tmp_path: Path) -> None:
    folder = tmp_path / "microbial-stable-coexistence"
    shutil.copytree(ROOT / "examples" / folder.name, folder)
    (folder / "derivation.yml").unlink()
    found = [
        located.finding.text
        for located in check_workspace(load_workspace(folder))
        if located.finding.rule.id == "derivation/unrecorded-descent"
    ]
    assert found == [
        "laws.abundance_nonneg: the law is marked derived, and no derivation or origin records"
        " its descent"
    ]


def test_an_origin_records_the_descent_of_a_derived_law() -> None:
    law = {"symbol": "onset", "warrant": "derived", "origin": "https://doi.org/10.0/example"}
    assert not unrecorded_descents({"type": "model", "id": "mod.a.b", "laws": [law]}, {})


def _derive_step(folder: Path, change: Callable[[dict[str, Any]], None]) -> set[str]:
    path = folder / "itinerary.yml"
    itinerary = yaml.safe_load(path.read_text(encoding="utf-8"))
    change(next(s for s in itinerary["steps"] if s["id"] == "derive"))
    path.write_text(yaml.safe_dump(itinerary, sort_keys=False), encoding="utf-8")
    return {located.finding.rule.id for located in check_workspace(load_workspace(folder))}


def _passed_without_record(step: dict[str, Any]) -> None:
    step.pop("derivation")
    step["norm"].update(verdict="pass", evidence="each move cites its warrant", judged="2026-11-04")


def _elsewhere(step: dict[str, Any]) -> None:
    step["output"]["ref"] = "bg.delayed-generalization-networks.training-specification"


@pytest.mark.parametrize(
    ("change", "rule"),
    [
        (_passed_without_record, "itinerary/unrecorded-derivation"),
        (_elsewhere, "itinerary/foreign-derivation"),
    ],
)
def test_the_derive_step_and_its_derivation_agree(
    change: Callable[[dict[str, Any]], None], rule: str, tmp_path: Path
) -> None:
    folder = tmp_path / EXAMPLE.name
    shutil.copytree(EXAMPLE, folder)
    assert rule in _derive_step(folder, change)


def _rewrite(folder: Path, name: str, change: Change) -> set[str]:
    """Change one record of a copied example, and return the texts of the findings of a check."""
    path = folder / name
    record = yaml.safe_load(path.read_text(encoding="utf-8"))
    change(record)
    path.write_text(yaml.safe_dump(record, sort_keys=False), encoding="utf-8")
    return {located.finding.text for located in check_workspace(load_workspace(folder))}


def test_a_segment_applies_a_scheme(tmp_path: Path) -> None:
    folder = tmp_path / EXAMPLE.name
    shutil.copytree(EXAMPLE, folder)
    texts = _rewrite(folder, "design.yml", lambda r: r.update(kind="method"))
    assert (
        "segments.relaxation.applies: design.grokking.slowest-mode-relaxation is no design of the"
        " kind scheme" in texts
    ), texts


def test_a_scheme_states_its_conditions_and_needs_no_stopping(tmp_path: Path) -> None:
    folder = tmp_path / EXAMPLE.name
    shutil.copytree(EXAMPLE, folder)
    texts = _rewrite(folder, "design.yml", lambda r: r.update(applies_when=None))
    assert "kind scheme requires: applies_when" in " ".join(texts), texts
    assert not any("stopping" in text for text in texts), texts
    texts = _rewrite(folder, "design.yml", lambda r: r.update(kind="method", applies_when=["x"]))
    assert any("stopping" in text for text in texts), texts


def test_a_law_requires_units_on_which_it_may_rest(tmp_path: Path) -> None:
    folder = tmp_path / EXAMPLE.name
    shutil.copytree(EXAMPLE, folder)

    def requirements(record: dict[str, Any]) -> None:
        laws = {law["symbol"]: law for law in record["laws"]}
        laws["representation_flow"]["requires"] = [
            "mod.grokking.effective-representation.representation_flow",
            "phen.grokking.delay",
        ]
        laws["representation_time"]["requires"] = [
            "mod.grokking.effective-representation.representation_flow"
        ]

    texts = _rewrite(folder, "model.yml", requirements)
    flow = "mod.grokking.effective-representation.representation_flow"
    assert f"laws.representation_flow.requires: {flow} is the law itself" in texts, texts
    assert (
        "laws.representation_flow.requires: phen.grokking.delay is no unit on which a law may"
        " rest" in texts
    ), texts
    assert (
        "laws.representation_time.requires: the derivation derivation.grokking.delay-scale"
        " records the premises of the law" in texts
    ), texts
