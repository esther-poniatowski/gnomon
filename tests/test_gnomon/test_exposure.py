"""The exposure of an answer, walked back through its dependencies.

Each rule of the walk is shown on a planted case: the premise laws of a derivation expose the
answer once the derivation stands for its ground, a unit whose state is not stated counts as
exposed, a refutation removes the support of a posit, and a posit exposes only the consequences
resting on it.
"""

from __future__ import annotations

import copy
from pathlib import Path
from typing import Any

from gnomon.check import load_workspace
from gnomon.exposure import answer_exposure, exposure_rows
from gnomon.views import exposure

ROOT = Path(__file__).resolve().parents[2]
GROKKING = ROOT / "examples" / "grokking-delayed-generalization"
ANSWER = "ans.grokking.slow-structured-representation"
DERIVATION = "derivation.grokking.delay-scale"
FLOW = "mod.grokking.effective-representation.representation_flow"


def _records() -> dict[str, dict[str, Any]]:
    """Return the records of the grokking workspace, as records that a test may change."""
    return {k: copy.deepcopy(dict(v)) for k, v in load_workspace(GROKKING).by_id.items()}


def _units(records: dict[str, dict[str, Any]], answer: str = ANSWER) -> dict[str, str]:
    """Return the reason of each unit that exposes an answer."""
    return {found.unit: found.reason for found in answer_exposure(records, answer)}


def _derivation_only(records: dict[str, dict[str, Any]]) -> None:
    """Keep only the ground that the derivation records, so that the walk reaches the premises
    through the derivation alone."""
    answer = records[ANSWER]
    answer["grounds"] = [g for g in answer["grounds"] if g["id"] == "timescale-law"]


def test_the_premise_laws_of_a_derivation_expose_the_answer() -> None:
    records = _records()
    _derivation_only(records)
    found = {f.unit: f.via for f in answer_exposure(records, ANSWER)}
    assert found[FLOW] == f"derivation {DERIVATION}"
    assert f"{DERIVATION}.slowest-dominates" in found


def test_a_move_without_an_error_counts_as_exposed() -> None:
    records = _records()
    move = next(m for m in records[DERIVATION]["moves"] if m["id"] == "crossing")
    move["warrant"].pop("error")
    assert _units(records)[f"{DERIVATION}.crossing"] == "warrant error not stated"


def test_a_refuted_posit_stays_exposed_whatever_its_tests() -> None:
    records = _records()
    posit = records[DERIVATION]["posits"][0]
    posit["tests"] = [{"kind": "computation", "verdict": "supports", "standard": "certified"}]
    assert f"{DERIVATION}.{posit['id']}" not in _units(records)
    records[DERIVATION]["refutations"] = [{"id": "r", "target": posit["id"]}]
    assert _units(records)[f"{DERIVATION}.{posit['id']}"] == "refuted"


def test_a_posit_exposes_only_the_consequences_resting_on_it() -> None:
    records = _records()
    lemma = next(c for c in records[DERIVATION]["consequences"] if c["id"] == "threshold-lemma")
    lemma["record"] = "mod.grokking.effective-representation.lemma"
    model = records["mod.grokking.effective-representation"]
    model["laws"].append({"symbol": "lemma", "warrant": "derived"})
    records[ANSWER]["grounds"] = [{"id": "g", "record": lemma["record"]}]
    records[ANSWER]["route"]["derivations"] = []
    found = _units(records)
    assert f"{DERIVATION}.quality-tracks-slow-mode" in found
    assert f"{DERIVATION}.slowest-dominates" in found
    lemma["from"] = "modal-flow"
    found = _units(records)
    assert f"{DERIVATION}.quality-tracks-slow-mode" not in found
    assert f"{DERIVATION}.slowest-dominates" not in found


def test_a_law_without_a_warrant_counts_as_exposed() -> None:
    records = {
        "mod.a.b": {"type": "model", "id": "mod.a.b", "laws": [{"symbol": "law"}]},
        "ans.a.b": {"type": "answer", "id": "ans.a.b", "grounds": [{"record": "mod.a.b.law"}]},
    }
    assert _units(records, "ans.a.b") == {"mod.a.b.law": "warrant not stated"}


def test_an_origin_records_the_descent_of_a_derived_law() -> None:
    law = {"symbol": "onset", "warrant": "derived", "origin": "https://doi.org/10.0/example"}
    records = {
        "mod.a.b": {"type": "model", "id": "mod.a.b", "laws": [law]},
        "ans.a.b": {"type": "answer", "id": "ans.a.b", "grounds": [{"record": "mod.a.b.onset"}]},
    }
    assert _units(records, "ans.a.b") == {"mod.a.b.onset": "descent in its origin"}
    law.pop("origin")
    assert _units(records, "ans.a.b") == {"mod.a.b.onset": "descent not recorded"}


def test_the_view_states_the_kind_of_each_unit() -> None:
    view = exposure(load_workspace(GROKKING).by_id)
    assert view["_schema"] == "gnomon:view.exposure@2"
    kinds = {row["unit"]: row["kind"] for row in view["exposures"]}
    assert kinds[f"{DERIVATION}.slowest-dominates"] == "move"
    assert kinds["mod.grokking.effective-representation.decoder-step"] == "operation"
    assert list(exposure_rows({})) == []


def test_a_consequence_carries_the_least_favourable_error_upstream() -> None:
    records = _records()
    found = {f.unit: f.reason for f in answer_exposure(records, ANSWER)}
    scale = f"{DERIVATION}.scale-law"
    assert found[scale] == "controlled error, within the regimes of slowest-dominates"
    move = next(m for m in records[DERIVATION]["moves"] if m["id"] == "solve-modes")
    move["warrant"]["error"] = "singular"
    found = {f.unit: f.reason for f in answer_exposure(records, ANSWER)}
    assert found[scale] == "singular error, within the regimes of slowest-dominates, solve-modes"


LAMBDA = "mod.grokking.effective-representation.lambda3"


def test_the_existence_that_a_condition_presupposes_exposes_the_answer() -> None:
    records = _records()
    found = {f.unit: (f.kind, f.reason) for f in answer_exposure(records, ANSWER)}
    assert found[LAMBDA] == ("existence", "existence and uniqueness not discharged")
    model = records["mod.grokking.effective-representation"]
    entry = next(v for v in model["variables"] if v["symbol"] == "lambda3")
    entry["held_by"] = FLOW
    held = {f.unit: f.via for f in answer_exposure(records, ANSWER)}
    assert LAMBDA not in held
    assert held[FLOW] in ("direct", f"existence of {LAMBDA}")


def test_a_settled_obligation_passes_on_the_exposure_of_its_derivation() -> None:
    records = _records()
    _derivation_only(records)
    records[ANSWER]["grounds"] = []
    records[ANSWER]["route"]["derivations"] = []
    assessment = next(r for r in records.values() if r.get("type") == "assessment")
    assessment["assesses"] = ANSWER
    assessment["obligations"] = [{"verdict": "pending", "derivation": DERIVATION}]
    assert f"{DERIVATION}.slowest-dominates" not in _units(records)
    assessment["obligations"][0]["verdict"] = "pass"
    found = {f.unit: f.via for f in answer_exposure(records, ANSWER)}
    assert found[f"{DERIVATION}.slowest-dominates"] == f"derivation {DERIVATION}"
