"""The checks that read the tree of an expression rather than its words.

The grammar writes a limit ``m -> infinity`` and a scaling ``S ~ r^z`` as relations. Resolution
scopes each binder index to its binder, and a formula field whose text the grammar does not cover
is reported once. The free indices of a definition must belong to the signature of the quantity, or
to the domain of its values. A domain limit names a variable or a parameter of the target on its
left side. Each rule is shown on a planted case, and the end-to-end cases plant the defect in a
copy of a worked inquiry.
"""

from __future__ import annotations

import shutil
from fractions import Fraction
from pathlib import Path

from gnomon.check import check_workspace, load_workspace
from gnomon.completeness import misstated_limit
from gnomon.dimensions import Formula, evaluate
from gnomon.expressions import parse_expression
from gnomon.findings import texts
from gnomon.latex import to_latex
from gnomon.vocabulary import contradicted_signatures, free_indices, unresolved_names

from .paths import EXAMPLES


def test_a_limit_and_a_scaling_are_relations() -> None:
    assert parse_expression("Re -> infinity") == ("cmp", "->", ("sym", "Re"), ("sym", "infinity"))
    assert parse_expression("S ~ r^z") == (
        "cmp",
        "~",
        ("sym", "S"),
        ("pow", ("sym", "r"), ("sym", "z")),
    )
    limit = parse_expression("limit_{t -> infinity}( E(t) )")
    assert limit is not None and limit[4] == (("cmp", "->", ("sym", "t"), ("sym", "infinity")),)
    assert parse_expression("S ~ ~ r") is None
    assert to_latex("m -> infinity", {"infinity": r"\infty"}) == r"m \to \infty"
    assert to_latex("S ~ r", {}) == r"S \sim r"


def test_a_fresh_index_resolves_only_inside_its_binder() -> None:
    known = frozenset({"norm", "K", "S", "a"})
    inside = parse_expression("norm_{a1 in a, a2 in S(a1)}( K(a1, a2) )")
    assert inside is not None and unresolved_names(inside, known, known) == []
    outside = parse_expression("norm_{a1 in a}( K(a1) ) + K(a1)")
    assert outside is not None and unresolved_names(outside, known, known) == ["a1"]


def test_a_ranged_index_must_be_declared() -> None:
    known = frozenset({"mean", "u"})
    tree = parse_expression("mean_{x}( u(x) )")
    assert tree is not None and unresolved_names(tree, known, known) == ["x"]


def test_a_scaling_compares_no_formulas_and_leaves_no_law_unchecked() -> None:
    symbols: dict[str, Formula | str | None] = {
        "S": {"L": Fraction(2), "T": Fraction(-2)},
        "r": {"L": Fraction(1)},
        "z": {},
    }
    found = evaluate("S ~ r^z", symbols)
    assert found is not None and found.violations == [] and not found.unruled
    equal = evaluate("S = r^z", symbols)
    assert equal is not None and equal.unruled == {"^"}
    statement = evaluate("S ~ (r > 0)", symbols)
    assert statement is not None and statement.violations == [
        ("mistyped-operand", "the relation ~ takes a statement")
    ]


def test_the_free_indices_of_a_definition() -> None:
    indices = frozenset({"a", "t", "s", "T"})
    tree = parse_expression("max_{t <= T}( norm_{a1 in a}( K(a1, t, s) ) )")
    assert tree is not None and free_indices(tree, indices) == ["T", "s"]


def test_a_free_index_belongs_to_the_signature_or_to_the_domain_of_the_values() -> None:
    def record(signature: list[str], values: str | None = None) -> dict[str, object]:
        entry = {"symbol": "F", "signature": signature, "expression": "dist_{r}( T(s) <= t )"}
        return {"type": "phenomenon", "observables": [{**entry, "values": values}]}

    assert not contradicted_signatures(record(["s", "t"]), {"r", "s", "t"})
    assert not contradicted_signatures(record(["s"], "maps(t, interval(0, 1))"), {"r", "s", "t"})
    assert texts(contradicted_signatures(record(["s"]), {"r", "s", "t"})) == [
        "observables.expression of F: leaves t free, which its signature omits"
    ]


def test_a_domain_limit_names_a_quantity_of_the_target() -> None:
    def question(text: str) -> dict[str, object]:
        return {"subject": {"domain": {"limit": {"expression": text}}}}

    assert not misstated_limit(question("Re -> infinity"), {"Re"})
    assert not misstated_limit(question("the limit of large width"), {"Re"})
    assert texts(misstated_limit(question("t -> infinity"), {"Re"})) == [
        "subject.domain.limit.expression: t is no variable or parameter of the target"
    ]
    assert texts(misstated_limit(question("2 * Re -> infinity"), {"Re"})) == [
        "subject.domain.limit.expression: the left side of the limit is no symbol"
    ]


def _planted(tmp_path: Path, case: str, name: str, old: str, new: str) -> set[str]:
    """Return the rules reported on a copy of a worked inquiry holding one planted change."""
    folder = tmp_path / case
    shutil.copytree(EXAMPLES / case, folder)
    path = folder / name
    text = path.read_text(encoding="utf-8")
    assert old in text, f"{name}: the text to replace is absent: {old}"
    path.write_text(text.replace(old, new, 1), encoding="utf-8")
    return {located.finding.rule.id for located in check_workspace(load_workspace(tmp_path))}


def test_a_formula_outside_the_grammar_is_reported(tmp_path: Path) -> None:
    rules = _planted(
        tmp_path,
        "turbulence-anomalous-scaling",
        "question.yml",
        'expression: "Re -> infinity"',
        'expression: "Re tends to infinity"',
    )
    assert "vocabulary/unparsed-expression" in rules


def test_a_definition_that_leaves_an_index_free_is_reported(tmp_path: Path) -> None:
    rules = _planted(
        tmp_path,
        "earth-system-tipping-cascades",
        "phenomenon.yml",
        'expression: "sequence_{sub}( Tev )"',
        'expression: "sequence_{t}( Tev(sub) )"',
    )
    assert "vocabulary/contradicted-signature" in rules


def test_a_limit_of_an_index_is_reported(tmp_path: Path) -> None:
    rules = _planted(
        tmp_path,
        "turbulence-anomalous-scaling",
        "question.yml",
        'expression: "Re -> infinity"',
        'expression: "t -> infinity"',
    )
    assert "completeness/misstated-limit" in rules
