"""The checks of a derivation record, its registry, and the exposure that a derivation adds.

The registry of derivations restates three rules of the theory notes, so its kinds are checked
against the vocabularies of the record and its admitted pairs against the table of the note on
interpretation. Each check is shown to fire on one planted defect of the worked derivation, which
carries none.
"""

from __future__ import annotations

import copy
import re
from pathlib import Path
from typing import Any, Callable

import pytest
import yaml

from gnomon.check import check_workspace, load_workspace
from gnomon.derivations import derivation_problems, exposed_units, load_registry
from gnomon.views import exposure

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
    assert set(registry["confirming_tests"]) <= values("tests.kind")
    assert registry["confirming_computation"] in values("tests.standard")


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
}


@pytest.mark.parametrize("rule", sorted(PLANTED))
def test_each_check_fires_on_its_planted_defect(rule: str) -> None:
    record = worked()
    PLANTED[rule](record)
    assert rule in {f.rule.id for f in derivation_problems(record)}


def test_exposure_reports_the_units_of_the_derivation() -> None:
    record = worked()
    assert list(exposed_units(record)) == [
        ("quality-tracks-slow-mode", "posit not confirmed"),
        ("slowest-dominates", "controlled warrant"),
    ]
    unit(record, "posits", "quality-tracks-slow-mode")["tests"] = [
        {"kind": "computation", "verdict": "supports", "standard": "certified"}
    ]
    assert [u for u, _ in exposed_units(record)] == ["slowest-dominates"]


def test_the_view_follows_the_derivation_of_a_derived_law() -> None:
    rows = exposure(load_workspace(EXAMPLE).by_id)["exposures"]
    via = {row["law"]: row["via"] for row in rows}
    assert "mod.grokking.effective-representation.representation_time" not in via
    assert via["derivation.grokking.delay-scale.slowest-dominates"] == (
        "derivation derivation.grokking.delay-scale"
    )
    assert re.fullmatch(r"derivation .*", via["mod.grokking.effective-representation.decoder-step"])
