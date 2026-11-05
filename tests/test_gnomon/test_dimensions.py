"""The dimensional formulas of quantities and the check of homogeneity.

The registry of operators states a rule of dimension for each operator, drawn from the vocabulary of
the operator record. The turbulence case declares a formula for each of its quantities whose formula
is a monomial, and a rule for each of its operators, so its definitions, its laws and its conditions
are checked; the structure functions, whose formula depends on the order of the moment, declare
none. Each rule is shown to fire on one planted defect.
"""

from __future__ import annotations

import shutil
from fractions import Fraction
from pathlib import Path
from typing import Any, Callable

import pytest
import yaml

from gnomon.check import check_workspace, load_workspace
from gnomon.dimensions import (
    STATEMENT,
    base_dimensions,
    declared_formulas,
    evaluate,
    parse_formula,
)
from gnomon.expressions import Tree, parse_expression

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
        ("1/T", {"T": Fraction(-1)}),
    ],
)
def test_formulas_parse(text: str, expected: dict[str, Fraction]) -> None:
    assert parse_formula(text, base_dimensions()) == expected


@pytest.mark.parametrize("text", ["", "  ", "T^1/2", "T^(1/0)", "L Q"])
def test_malformed_formulas_are_rejected(text: str) -> None:
    with pytest.raises(ValueError):
        parse_formula(text, base_dimensions())


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
    "dimension/mistyped-operand": _edit("background.yml", _law("(U > 0) + U = U")),
    "dimension/colliding-base": _edit(
        "operators.yml", lambda r: r.update(base_scales=[{"symbol": "L", "name": "loss"}])
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


def _terms(tree: Tree) -> list[Tree]:
    """Return the terms of every sum of a tree, the sides of a comparison included."""
    if tree[0] in ("sum", "cmp"):
        return _terms(tree[2]) + _terms(tree[3])
    if tree[0] == "neg":
        return _terms(tree[1])
    return [tree]


def test_every_term_of_the_momentum_law_is_decided() -> None:
    records = [
        yaml.safe_load((CASE / name).read_text(encoding="utf-8"))
        for name in ("target-system.yml", "background.yml")
    ]
    symbols = declared_formulas(records, base_dimensions())
    law = next(entry for entry in records[1]["laws"] if entry["symbol"] == "momentum")
    tree = parse_expression(law["expression"])
    assert tree is not None and tree[0] == "cmp"
    terms = _terms(tree)
    assert len(terms) == 5
    for term in terms:
        evaluation = evaluate(law["expression"], symbols)
        assert evaluation is not None
        assert evaluation.value(term) == {"L": Fraction(1), "T": Fraction(-2)}, term


def test_a_divergence_divides_by_the_formula_of_its_coordinates() -> None:
    symbols = {"u": {"L": Fraction(1), "T": Fraction(-1)}, "x": {"L": Fraction(1)}}
    evaluation = evaluate("div(u, x)", symbols)
    assert evaluation is not None and evaluation.result == {"T": Fraction(-1)}


def test_a_quantified_statement_is_a_statement_over_a_checked_body() -> None:
    symbols = {"lambda": {"T": Fraction(-1)}, "u": None}
    evaluation = evaluate("exists_{i}( lambda(i) > 0 )", symbols)
    assert evaluation is not None and evaluation.result == STATEMENT
    evaluation = evaluate("forall_{i}( u > 0 )", symbols)
    assert evaluation is not None and evaluation.missing == {"u"}
    evaluation = evaluate("exists_{i}( lambda(i) )", symbols)
    assert evaluation is not None
    assert evaluation.violations == [
        ("mistyped-operand", "the operator exists takes a quantity of formula T^-1")
    ]


def test_a_relation_checks_each_argument_on_its_own() -> None:
    symbols = {"d": {"T": Fraction(1)}, "r": {"T": Fraction(-1)}, "a": {"L": Fraction(1)}}
    evaluation = evaluate("depends_on(d, 1 / r)", symbols)
    assert evaluation is not None and evaluation.result == STATEMENT
    assert not evaluation.violations
    evaluation = evaluate("depends_on(d, r + a)", symbols)
    assert evaluation is not None and evaluation.violations


def test_a_chained_comparison_is_reported() -> None:
    symbols = {"a": {"L": Fraction(1)}, "x": {"L": Fraction(1)}}
    evaluation = evaluate("a < x < a", symbols)
    assert evaluation is not None
    assert evaluation.violations == [("mistyped-operand", "the relation < takes a statement")]


def test_membership_is_no_comparison_of_formulas() -> None:
    symbols = {"x": {"L": Fraction(1)}, "Om": {"L": Fraction(1)}, "q": None}
    evaluation = evaluate("x in subset(Om, q)", symbols)
    assert evaluation is not None and not evaluation.violations


def test_the_index_of_a_quantity_is_checked() -> None:
    symbols = {"u": {"L": Fraction(1)}, "x": {"L": Fraction(1)}, "t": {"T": Fraction(1)}}
    evaluation = evaluate("u(x + t) = u", symbols)
    assert evaluation is not None
    assert evaluation.violations == [
        ("inhomogeneous", "the terms of a sum have the formulas L and T")
    ]


def test_an_operator_requiring_a_pure_argument() -> None:
    symbols = {"x": {"L": Fraction(1)}, "x0": {"L": Fraction(1)}}
    impure = evaluate("exp(x) = 1", symbols, {"exp": "pure-argument"})
    assert impure is not None
    assert impure.violations == [("impure-argument", "the argument of exp has the formula L")]
    pure = evaluate("exp(x / x0) = 1", symbols, {"exp": "pure-argument"})
    assert pure is not None and not pure.violations


def test_an_operator_without_a_rule_is_reported_and_a_waiver_is_not() -> None:
    symbols = {"u": {"L": Fraction(1)}}
    assert evaluate("f(u) = u", symbols, {}).unruled == {"f"}  # type: ignore[union-attr]
    assert not evaluate("f(u) = u", symbols, {"f": "unchecked"}).unruled  # type: ignore[union-attr]
    assert evaluate("u^n = u", symbols, {}).unruled == {"^"}  # type: ignore[union-attr]


@pytest.mark.parametrize("text", ["f(a b)", "f(a,)", "rate(per step)", "sum_{i j}( a )"])
def test_a_list_without_its_commas_is_no_expression(text: str) -> None:
    assert parse_expression(text) is None


def test_the_operator_of_a_boundary_law_needs_a_rule(tmp_path: Path) -> None:
    folder = tmp_path / CASE.name
    shutil.copytree(CASE, folder)

    def drop(record: dict[str, Any]) -> None:
        next(op for op in record["operators"] if op["symbol"] == "restrict").pop("dimension")

    _edit("operators.yml", drop)(folder)
    texts = [located.finding.text for located in check_workspace(load_workspace(folder))]
    assert any(
        "laws.boundary_law.expression: the operator restrict states no rule of dimension" in text
        for text in texts
    ), texts


@pytest.mark.parametrize(
    ("name", "change", "fragment"),
    [
        (
            "phenomenon.yml",
            lambda r: r["conditions_and_byproducts"]["precipitating"][0].update(
                expression="rmag > nu"
            ),
            "the sides of > have the formulas L and L^2 T^-1",
        ),
        (
            "background.yml",
            lambda r: r["laws"][0].update(range="U > Lc"),
            "the sides of > have the formulas L T^-1 and L",
        ),
    ],
    ids=["condition of a phenomenon", "range of a law"],
)
def test_conditions_and_ranges_are_checked(
    name: str, change: Callable[[dict[str, Any]], None], fragment: str, tmp_path: Path
) -> None:
    folder = tmp_path / CASE.name
    shutil.copytree(CASE, folder)
    _edit(name, change)(folder)
    texts = [located.finding.text for located in check_workspace(load_workspace(folder))]
    assert any(fragment in text for text in texts), texts


def test_two_formulas_of_one_symbol_conflict(tmp_path: Path) -> None:
    folder = tmp_path / CASE.name
    shutil.copytree(CASE, folder)

    def rename(record: dict[str, Any]) -> None:
        rmag = next(s for s in record["index_sets"] if s["symbol"] == "rmag")
        rmag["dimensional_formula"] = "T"

    _edit("phenomenon.yml", rename)(folder)
    _edit(
        "target-system.yml",
        lambda r: r["index_sets"].append({"symbol": "rmag", "dimensional_formula": "L"}),
    )(folder)
    rules = {located.finding.rule.id for located in check_workspace(load_workspace(folder))}
    assert "dimension/conflicting-formula" in rules


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


ACTIVE = ROOT / "examples" / "active-matter-phase-exploration"
GROKKING = ROOT / "examples" / "grokking-delayed-generalization"


def _foreign(folder: Path) -> list[str]:
    return [
        located.finding.text
        for located in check_workspace(load_workspace(folder))
        if located.finding.rule.id == "vocabulary/foreign-coordinates"
    ]


def test_a_gradient_along_coordinates_outside_its_argument_is_reported(tmp_path: Path) -> None:
    folder = tmp_path / GROKKING.name
    shutil.copytree(GROKKING, folder)

    def ill_posed(record: dict[str, Any]) -> None:
        law = next(entry for entry in record["laws"] if entry["symbol"] == "update")
        law["expression"] = "diff(theta, step) = opt(grad(Ltrain, theta), z)"

    _edit("background.yml", ill_posed)(folder)
    assert _foreign(folder) == [
        "laws.expression: grad differentiates Ltrain along theta, which indexes no quantity of it"
        " and occurs nowhere in it"
    ]


def test_the_coordinates_of_a_map_are_its_domain(tmp_path: Path) -> None:
    folder = tmp_path / ACTIVE.name
    shutil.copytree(ACTIVE, folder)
    assert not _foreign(folder)

    def other_domain(record: dict[str, Any]) -> None:
        state = next(entry for entry in record["variables"] if entry["symbol"] == "u")
        state["values"] = "reals"

    _edit("target-system.yml", other_domain)(folder)
    texts = _foreign(folder)
    assert len(texts) == 1 and "whose values reals are not the domain of F, G" in texts[0], texts


def test_an_existence_is_held_by_a_statement(tmp_path: Path) -> None:
    folder = tmp_path / GROKKING.name
    shutil.copytree(GROKKING, folder)

    def concept(record: dict[str, Any]) -> None:
        entry = next(v for v in record["variables"] if v["symbol"] == "lambda3")
        entry["held_by"] = "mod.grokking.effective-representation.Hrep"

    _edit("model.yml", concept)(folder)
    texts = [located.finding.text for located in check_workspace(load_workspace(folder))]
    assert (
        "variables.lambda3.held_by: mod.grokking.effective-representation.Hrep is no law and no"
        " consequence of a derivation" in texts
    ), texts
