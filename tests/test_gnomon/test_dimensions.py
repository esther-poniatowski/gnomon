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


def test_a_derivative_divides_by_the_formula_of_its_index() -> None:
    symbols = {"u": {"L": Fraction(1), "T": Fraction(-1)}, "t": {"T": Fraction(1)}}
    evaluation = evaluate("diff(u, t)", symbols)
    assert evaluation is not None
    assert evaluation.result == {"L": Fraction(1), "T": Fraction(-2)}


def _index(record: dict[str, Any], symbol: str) -> dict[str, Any]:
    entry: dict[str, Any] = next(s for s in record["index_sets"] if s["symbol"] == symbol)
    return entry


@pytest.mark.parametrize(
    ("formula", "rule", "text"),
    [
        ("L", "dimension/inhomogeneous", "the terms of a sum have the formulas T^-1 and L T^-2"),
        (None, "dimension/unchecked-law", "no dimensional formula is declared for t"),
    ],
)
def test_the_formula_of_the_time_axis_decides_the_momentum_law(
    formula: str | None, rule: str, text: str, tmp_path: Path
) -> None:
    folder = tmp_path / CASE.name
    shutil.copytree(CASE, folder)
    _edit("target-system.yml", lambda r: _index(r, "t").update(dimensional_formula=formula))(folder)
    found = [
        located.finding
        for located in check_workspace(load_workspace(folder))
        if located.finding.rule.id == rule
    ]
    assert any("laws.momentum" in f.text and text in f.text for f in found), [f.text for f in found]


def test_every_term_of_the_momentum_law_is_decided() -> None:
    from gnomon.dimensions import declared_formulas, parse_expression

    records = [
        yaml.safe_load((CASE / name).read_text(encoding="utf-8"))
        for name in ("target-system.yml", "background.yml")
    ]
    symbols = declared_formulas(records, base_dimensions())
    law = next(entry for entry in records[1]["laws"] if entry["symbol"] == "momentum")
    tree = parse_expression(law["expression"])
    assert tree is not None and tree[0] == "cmp"
    for side in tree[2:]:
        evaluation = evaluate(law["expression"], symbols)
        assert evaluation is not None
        assert evaluation.value(side) == {"L": Fraction(1), "T": Fraction(-2)}


def test_a_laplacian_divides_by_the_square_of_its_coordinates() -> None:
    symbols = {"u": {"L": Fraction(1), "T": Fraction(-1)}, "x": {"L": Fraction(1)}}
    evaluation = evaluate("lap(u, x)", symbols)
    assert evaluation is not None
    assert evaluation.result == {"L": Fraction(-1), "T": Fraction(-1)}


def test_a_wrong_pressure_breaks_the_momentum_law(tmp_path: Path) -> None:
    folder = tmp_path / CASE.name
    shutil.copytree(CASE, folder)

    def pressure(record: dict[str, Any]) -> None:
        entry = next(v for v in record["variables"] if v["symbol"] == "pr")
        entry["dimensional_formula"] = "L T^-2"

    _edit("target-system.yml", pressure)(folder)
    texts = [
        located.finding.text
        for located in check_workspace(load_workspace(folder))
        if located.finding.rule.id == "dimension/inhomogeneous"
    ]
    assert any(text.startswith("laws.momentum.expression") for text in texts), texts


def test_a_gradient_without_its_coordinates_is_reported(tmp_path: Path) -> None:
    folder = tmp_path / CASE.name
    shutil.copytree(CASE, folder)

    def implicit(record: dict[str, Any]) -> None:
        law = next(entry for entry in record["laws"] if entry["symbol"] == "incompressible")
        law["expression"] = "div(u) = 0"

    _edit("background.yml", implicit)(folder)
    rules = {located.finding.rule.id for located in check_workspace(load_workspace(folder))}
    assert "vocabulary/mismatched-arity" in rules


ENERGY = {"M": Fraction(1), "L": Fraction(2), "T": Fraction(-2)}


def test_a_hessian_divides_by_the_square_of_its_coordinates() -> None:
    symbols = {"E": ENERGY, "x": {"L": Fraction(1)}, "x0": {"L": Fraction(1)}}
    evaluation = evaluate("jacobian(grad(E, x), x, x0)", symbols)
    assert evaluation is not None and not evaluation.violations
    assert evaluation.result == {"M": Fraction(1), "T": Fraction(-2)}


def test_a_jacobian_at_a_point_of_another_dimension_is_inhomogeneous() -> None:
    symbols = {"E": ENERGY, "x": {"L": Fraction(1)}, "t0": {"T": Fraction(1)}}
    evaluation = evaluate("jacobian(grad(E, x), x, t0)", symbols)
    assert evaluation is not None
    assert evaluation.violations == [
        ("inhomogeneous", "the point of jacobian has the formula T, and its coordinates L")
    ]
