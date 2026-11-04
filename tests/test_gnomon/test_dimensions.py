"""The dimensional formulas of quantities and the check of homogeneity.

The registry of operators states a rule of dimension for each operator, drawn from the vocabulary of
the operator record. The turbulence case declares a formula for each of its quantities, so its
definitions and its laws are checked, and each rule is shown to fire on one planted defect.
"""

from __future__ import annotations

import shutil
from fractions import Fraction
from pathlib import Path
from typing import Any, Callable

import pytest
import yaml

from gnomon.check import check_workspace, load_workspace
from gnomon.dimensions import base_dimensions, evaluate, parse_formula

ROOT = Path(__file__).resolve().parents[2]
CASE = ROOT / "examples" / "turbulence-anomalous-scaling"
REGISTRY = ROOT / "src" / "gnomon" / "data"


def test_every_canonical_operator_states_an_admitted_rule() -> None:
    operators = yaml.safe_load((REGISTRY / "operators.yml").read_text())["operators"]
    vocabulary = yaml.safe_load((REGISTRY / "vocabularies.yml").read_text())["vocabularies"]
    admitted = {entry["value"] for entry in vocabulary["operators"]["operators.dimension"]}
    assert {op["symbol"]: op.get("dimension") in admitted for op in operators} == {
        op["symbol"]: True for op in operators
    }


def test_the_package_declares_the_seven_base_dimensions() -> None:
    assert base_dimensions() == frozenset({"M", "L", "T", "I", "Theta", "N", "J"})


@pytest.mark.parametrize(
    ("text", "expected"),
    [
        ("1", {}),
        ("M L T^-2", {"M": Fraction(1), "L": Fraction(1), "T": Fraction(-2)}),
        ("L^(1/2)", {"L": Fraction(1, 2)}),
        ("L / T^2", {"L": Fraction(1), "T": Fraction(-2)}),
        ("L T / T", {"L": Fraction(1)}),
    ],
)
def test_formulas_parse(text: str, expected: dict[str, Fraction]) -> None:
    assert parse_formula(text, base_dimensions()) == expected


def test_a_zero_is_homogeneous_with_every_formula() -> None:
    evaluation = evaluate("u = 0", {"u": {"L": Fraction(1)}}, {})
    assert evaluation is not None and not evaluation.violations


def test_the_annotated_case_has_no_finding() -> None:
    assert not check_workspace(load_workspace(CASE))


def _edit(name: str, change: Callable[[dict[str, Any]], None]) -> Callable[[Path], None]:
    def apply(folder: Path) -> None:
        path = folder / name
        record = yaml.safe_load(path.read_text(encoding="utf-8"))
        change(record)
        path.write_text(yaml.safe_dump(record, sort_keys=False), encoding="utf-8")

    return apply


def _parameter(record: dict[str, Any], symbol: str) -> dict[str, Any]:
    entry: dict[str, Any] = next(p for p in record["parameters"] if p["symbol"] == symbol)
    return entry


def _law(expression: str) -> Callable[[dict[str, Any]], None]:
    def change(record: dict[str, Any]) -> None:
        record["laws"].append(
            {"name": "planted law", "symbol": "planted", "expression": expression}
        )

    return change


PLANTED: dict[str, Callable[[Path], None]] = {
    "dimension/mismatched-definition": _edit(
        "target-system.yml",
        lambda r: _parameter(r, "etaK").update(expression="(nu^3 / eps)^(1/3)"),
    ),
    "dimension/malformed-formula": _edit(
        "target-system.yml", lambda r: _parameter(r, "Lc").update(dimensional_formula="L Q")
    ),
    "dimension/inhomogeneous": _edit("background.yml", _law("U + nu = 0")),
    "dimension/impure-argument": _edit("background.yml", _law("U^Lc = U")),
    "dimension/unchecked-law": _edit(
        "target-system.yml", lambda r: _parameter(r, "nu").update(dimensional_formula=None)
    ),
}


@pytest.mark.parametrize("rule", sorted(PLANTED))
def test_each_rule_fires_on_its_planted_defect(rule: str, tmp_path: Path) -> None:
    folder = tmp_path / CASE.name
    shutil.copytree(CASE, folder)
    PLANTED[rule](folder)
    assert rule in {located.finding.rule.id for located in check_workspace(load_workspace(folder))}
