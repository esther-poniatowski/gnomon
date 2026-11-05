"""The checks of a derivation record and its registry.

The registry of derivations restates three rules of the theory notes, so its kinds are checked
against the vocabularies of the record and its admitted pairs against the table of the note on
interpretation. Each check is shown to fire on one planted defect of the worked derivation, which
carries none.
"""

from __future__ import annotations

import copy
from pathlib import Path
from typing import Any, Callable

import pytest
import yaml

from gnomon.check import check_workspace, load_workspace
from gnomon.derivations import (
    derivation_problems,
    load_registry,
    unrecorded_descents,
)

ROOT = Path(__file__).resolve().parents[2]
EXAMPLE = ROOT / "examples" / "grokking-delayed-generalization"
NOTE = ROOT / "docs" / "epistemology" / "objects" / "derivation" / "interpretation.md"
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
    assert set(registry["licensing_kinds"]) <= kinds
    assert {k for ks in registry["admitted_pairs"].values() for k in ks} <= kinds
    assert set(registry["confirming_tests"]) <= values("posits.test")
    assert registry["confirming_computation"] in values("posits.standard")


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


def _avoidable_kernel(record: dict[str, Any]) -> None:
    record["kernel"] = "solve-modes"
    record["segments"] = []
    record["moves"].append(
        {"id": "shortcut", "kind": "estimate", "inputs": ["modal-flow"], "outputs": ["mode-decay"]}
    )


def _set(name: str, ident: str, key: str, value: Any) -> Callable[[dict[str, Any]], None]:
    def change(record: dict[str, Any]) -> None:
        unit(record, name, ident)[key] = value

    return change


def _cycle(record: dict[str, Any]) -> None:
    unit(record, "moves", "diagonalize")["inputs"].append("delay-law")


def _detour(record: dict[str, Any]) -> None:
    record["objects"].append({"id": "stray", "form": "object", "reading": "an unused object"})
    record["moves"].append(
        {"id": "detour", "kind": "rescale", "inputs": ["mode-decay"], "outputs": ["stray"]}
    )


PLANTED: dict[str, Callable[[dict[str, Any]], None]] = {
    "derivation/repeated-unit": _set("objects", "hessian", "id", "diagonalize"),
    "derivation/unknown-unit": _set("moves", "crossing", "inputs", ["slowest-mode", "ghost"]),
    "derivation/unadmitted-pair": _set("interpretations", "hessian-symmetric", "kind", "variation"),
    "derivation/mistyped-ground": _set("interpretations", "memorization-limit", "grounds", []),
    "derivation/cycle": _cycle,
    "derivation/retrospective-orientation": _set(
        "orientations", "isolate-slow-mode", "occasion", "memorization-limit"
    ),
    "derivation/ambiguous-purpose": _set("orientations", "isolate-slow-mode", "determines", "x"),
    "derivation/unoriented-move": _set(
        "orientations", "time-the-crossing", "of", "keep-dependence"
    ),
    "derivation/failed-kernel": _avoidable_kernel,
    "derivation/unrecorded-consequence": _set("consequences", "scale-law", "record", None),
    "derivation/unbound-slot": _set("moves", "solve-modes", "binds", []),
    "derivation/idle-move": _detour,
    "derivation/cyclic-nesting": _set("segments", "relaxation", "within", "relaxation"),
}


@pytest.mark.parametrize("rule", sorted(PLANTED))
def test_each_check_fires_on_its_planted_defect(rule: str) -> None:
    record = worked()
    PLANTED[rule](record)
    assert rule in {f.rule.id for f in derivation_problems(record)}


DERIVATIONS = sorted((ROOT / "examples").glob("*/derivation.yml"))


@pytest.mark.parametrize("path", DERIVATIONS, ids=lambda p: p.parent.name)
def test_every_worked_derivation_has_no_finding(path: Path) -> None:
    assert not derivation_problems(yaml.safe_load(path.read_text(encoding="utf-8")))


def test_a_derived_law_without_its_derivation_is_reported(tmp_path: Path) -> None:
    import shutil

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
    step["output"]["ref"] = "bg.delayed_generalization_networks.training-specification"


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
    import shutil

    folder = tmp_path / EXAMPLE.name
    shutil.copytree(EXAMPLE, folder)
    assert rule in _derive_step(folder, change)
