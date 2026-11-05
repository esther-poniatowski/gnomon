"""The content of a claim: its presuppositions and its interventions.

A presupposition of a claim is held by a law of a background or a model, or by a consequence of a
derivation, and a presupposition that another answer holds is a relation ``presupposes``. A claim
inherits the presuppositions of its question and does not restate them. An undischarged
presupposition exposes the answer, and a held one passes on the exposure of its holder. The
interventions of a counterfactual claim name experiments, simulation runs or quantities of a model.
Each rule is shown on a planted case.
"""

from __future__ import annotations

import copy
import shutil
from pathlib import Path
from typing import Any

import yaml

from gnomon.check import check_workspace, load_workspace
from gnomon.completeness import (
    inherited_presuppositions,
    misdirected_interventions,
    misheld_presuppositions,
)
from gnomon.exposure import answer_exposure

ROOT = Path(__file__).resolve().parents[2]
GROKKING = ROOT / "examples" / "grokking-delayed-generalization"
ANSWER = "ans.grokking.slow-structured-representation"
POSITED = "mod.grokking.effective-representation.representation_flow"
DERIVED = "mod.grokking.effective-representation.representation_time"
CONSEQUENCE = "derivation.grokking.delay-scale.scale-law"
CONCEPT = "concept.microbial.stable-coexistence"
DESIGN = "design.nonreciprocal-active-matter.coupling-sweep"


def _records() -> dict[str, dict[str, Any]]:
    """Return the records of every worked example, keyed by identifier, as records a test may
    change."""
    return {
        ident: copy.deepcopy(dict(record))
        for ident, record in load_workspace(ROOT / "examples").by_id.items()
    }


def _answer(**claim: Any) -> dict[str, Any]:
    return {"type": "answer", "id": "ans.a.b", "claim": claim}


def _held(holder: str | None) -> dict[str, Any]:
    return _answer(presuppositions=[{"id": "p", "reading": "a commitment", "held_by": holder}])


def test_a_presupposition_is_held_by_a_law_or_a_consequence() -> None:
    records = _records()
    for holder in (POSITED, DERIVED, CONSEQUENCE):
        assert not misheld_presuppositions(_held(holder), records), holder
    for holder in (CONCEPT, ANSWER, "ans.a.b.claim", "free text"):
        texts = [f.text for f in misheld_presuppositions(_held(holder), records)]
        assert texts == [
            f"claim.presuppositions.p.held_by: {holder} is no law and no consequence of a"
            " derivation"
        ], holder


def test_an_undischarged_presupposition_needs_no_holder() -> None:
    assert not misheld_presuppositions(_held(None), _records())


def test_a_claim_does_not_restate_a_presupposition_of_its_question() -> None:
    question = {
        "type": "question",
        "presuppositions": [{"id": "q", "reading": "a positive rate exists", "expression": "x>0"}],
    }
    restated = _answer(presuppositions=[{"id": "p", "expression": "x > 0"}])
    assert [f.text for f in inherited_presuppositions(restated, question)] == [
        "claim.presuppositions.p: the question presupposes it already, as q"
    ]
    other = _answer(presuppositions=[{"id": "p", "expression": "y > 0"}])
    assert not inherited_presuppositions(other, question)


def test_interventions_name_a_design_or_a_quantity_of_a_model() -> None:
    records = _records()
    quantity = "mod.grokking.effective-representation.eta_rep"
    assert not misdirected_interventions(_answer(interventions=[DESIGN, quantity]), records)
    records[DESIGN] = {**records[DESIGN], "kind": "method"}
    texts = [f.text for f in misdirected_interventions(_answer(interventions=[DESIGN]), records)]
    assert texts == [
        f"claim.interventions: {DESIGN} sets no intervention: no experiment or simulation run"
        " stating one, and no quantity of a model"
    ]
    assert misdirected_interventions(_answer(interventions=[CONCEPT]), records)


def _exposure(records: dict[str, dict[str, Any]], holder: str | None) -> dict[str, str]:
    answer = records[ANSWER]
    answer["claim"]["presuppositions"] = [{"id": "p", "reading": "a commitment", "held_by": holder}]
    return {f.unit: f.via for f in answer_exposure(records, ANSWER)}


def test_a_presupposition_exposes_the_answer_until_a_statement_holds_it() -> None:
    records = _records()
    records[ANSWER]["grounds"] = []
    records[ANSWER]["route"]["derivations"] = []
    assert _exposure(records, None) == {f"{ANSWER}.claim.presuppositions.p": "claim"}
    assert _exposure(records, POSITED) == {POSITED: "presupposition p"}
    held = _exposure(records, DERIVED)
    assert f"{ANSWER}.claim.presuppositions.p" not in held
    assert POSITED in held


def test_a_relation_presupposes_passes_on_the_exposure_of_the_other_answer() -> None:
    records = _records()
    other: dict[str, Any] = {
        "type": "answer",
        "id": "ans.a.other",
        "grounds": [],
        "relations": [{"answer": ANSWER, "relation": "presupposes"}],
    }
    records[other["id"]] = other
    units = {f.unit for f in answer_exposure(records, "ans.a.other")}
    assert POSITED in units


def test_an_undeclared_symbol_of_a_presupposition_is_reported(tmp_path: Path) -> None:
    folder = tmp_path / GROKKING.name
    shutil.copytree(GROKKING, folder)
    path = folder / "answer.yml"
    answer = yaml.safe_load(path.read_text(encoding="utf-8"))
    answer["claim"]["presuppositions"] = [
        {"id": "p", "reading": "a commitment", "expression": "lambda9 > 0"}
    ]
    path.write_text(yaml.safe_dump(answer, sort_keys=False), encoding="utf-8")
    texts = [located.finding.text for located in check_workspace(load_workspace(folder))]
    assert any("lambda9" in text for text in texts), texts
