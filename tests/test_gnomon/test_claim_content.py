"""The content of a claim: its presuppositions, its interventions, and the quantifier binders.

A presupposition of the strength axiom names a background law or a concept record, a counterfactual
claim names an experiment or a simulation run that states an intervention, and an undischarged
presupposition enters the view of exposure. Each rule is shown to fire on one planted defect.
"""

from __future__ import annotations

import shutil
from fractions import Fraction
from pathlib import Path
from typing import Any

import yaml

from gnomon.check import check_workspace, load_workspace
from gnomon.completeness import misdirected_interventions, unheld_axioms
from gnomon.dimensions import evaluate
from gnomon.views import exposure

ROOT = Path(__file__).resolve().parents[2]
GROKKING = ROOT / "examples" / "grokking-delayed-generalization"
LAW = "bg.nonreciprocal-active-matter.local-dynamics.evolve"
DESIGN = "design.nonreciprocal-active-matter.coupling-sweep"
CONCEPT = "concept.microbial.stable-coexistence"


def _records() -> dict[str, dict[str, Any]]:
    """Return the records of the workspace of examples, keyed by identifier."""
    return {
        ident: dict(record) for ident, record in load_workspace(ROOT / "examples").by_id.items()
    }


def _answer(**claim: Any) -> dict[str, Any]:
    return {"type": "answer", "id": "ans.a.b", "claim": claim}


def _axiom(held_by: str | None) -> dict[str, Any]:
    return _answer(presuppositions=[{"id": "p", "strength": "axiom", "held_by": held_by}])


def test_an_axiom_is_held_by_a_background_law_or_a_concept() -> None:
    records = _records()
    assert not unheld_axioms(_axiom(LAW), records)
    assert not unheld_axioms(_axiom(CONCEPT), records)
    assert [f.rule.id for f in unheld_axioms(_axiom(None), records)] == [
        "completeness/unheld-axiom"
    ]
    assert [f.rule.id for f in unheld_axioms(_axiom(DESIGN), records)] == [
        "completeness/unheld-axiom"
    ]


def test_a_provisional_commitment_needs_no_corpus_record() -> None:
    answer = _answer(presuppositions=[{"id": "p", "strength": "provisional"}])
    assert not unheld_axioms(answer, _records())


def test_interventions_name_a_design_that_states_one() -> None:
    records = _records()
    assert not misdirected_interventions(_answer(interventions=DESIGN), records)
    records[DESIGN] = {**records[DESIGN], "kind": "method"}
    assert [
        f.rule.id for f in misdirected_interventions(_answer(interventions=DESIGN), records)
    ] == ["completeness/misdirected-interventions"]


def test_an_undischarged_presupposition_enters_the_view_until_a_record_holds_it() -> None:
    records = _records()
    via = [row["via"] for row in exposure(records)["exposures"]]
    assert "claim" in via
    answer = records["ans.grokking.slow-structured-representation"]
    claim = dict(answer["claim"])
    claim["presuppositions"] = [{**claim["presuppositions"][0], "held_by": LAW}]
    records[answer["id"]] = {**answer, "claim": claim}
    assert "claim" not in [row["via"] for row in exposure(records)["exposures"]]


def test_an_undeclared_symbol_of_a_presupposition_is_reported(tmp_path: Path) -> None:
    folder = tmp_path / GROKKING.name
    shutil.copytree(GROKKING, folder)
    path = folder / "answer.yml"
    answer = yaml.safe_load(path.read_text(encoding="utf-8"))
    answer["claim"]["presuppositions"][0]["expression"] = "lambda9 > 0"
    path.write_text(yaml.safe_dump(answer, sort_keys=False), encoding="utf-8")
    texts = [located.finding.text for located in check_workspace(load_workspace(folder))]
    assert any("lambda9" in text for text in texts), texts


def test_a_quantified_statement_is_a_pure_number() -> None:
    evaluation = evaluate("exists_{i}( lambda(i) > 0 )", {"lambda": {"T": Fraction(-1)}}, None)
    assert evaluation is not None and evaluation.result == {}
    assert not evaluation.violations
