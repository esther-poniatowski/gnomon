"""
The dimensional formulas of quantities, and the check of the dimensional homogeneity of laws.

A dimensional formula is a monomial over base dimensions, such as ``M L T^-2``, or ``1`` for a pure
number. The base dimensions are the seven of the International System of Quantities, declared in
the registry of dimensions, and the base scales that the operator record of a problem declares. The
formula of an expression is computed by declared rules: a product adds the exponents, a quotient
subtracts them, a power multiplies them by a pure exponent, and each operator of the registry
states its rule. A part of an expression whose formula no rule fixes is left unchecked, so the
check reports only what the declared formulas decide.

Functions
---------
parse_formula
    Return the exponents of a dimensional formula, or raise ``ValueError``.
evaluate
    Return the formula of an expression tree, with the violations of homogeneity that it holds.
dimension_problems
    Return the findings of the dimensional checks of one record.
"""

from __future__ import annotations

import re
from dataclasses import dataclass, field
from fractions import Fraction
from functools import cache
from pathlib import Path
from typing import Any, Iterable, Mapping

import yaml

from . import findings as rules
from .expressions import Tree, number, parse_expression
from .findings import Entry, Finding, finding, values_at, where

#: The registry of the base dimensions.
REGISTRY = Path(__file__).parent / "data" / "registries" / "dimensions.yml"

#: The registry of the canonical operators, whose entries state their rule of dimension.
OPERATOR_REGISTRY = Path(__file__).parent / "data" / "operators.yml"

#: The blocks whose entries are quantities, whose definitions are checked against their formula.
QUANTITY_BLOCKS: tuple[str, ...] = ("variables", "parameters", "observables")

#: The blocks whose entries may carry a dimensional formula: the quantities, the index sets, whose
#: formula a derivative along the index divides by, and the features of a manifestation.
FORMULA_BLOCKS: tuple[str, ...] = (
    *QUANTITY_BLOCKS,
    "index_sets",
    "manifestations.features",
)


#: A dimensional formula: the exponent of each base dimension; empty for a pure number.
Formula = Mapping[str, Fraction]

#: The value of a statement, such as an equation, which has no dimension.
STATEMENT = "statement"

Value = Formula | str | None

PURE: Formula = {}

#: The rules of the operators that divide their first argument by the formula of their coordinates.
DERIVATIVE_RULES: tuple[str, ...] = ("derivative", "second-derivative", "derivative-at")

#: The order in which a formula writes the base dimensions of the package, before the base scales.
ISQ_ORDER: tuple[str, ...] = ("M", "L", "T", "I", "Theta", "N", "J")

#: A factor of a dimensional formula: a base with an integer exponent, or with a fractional exponent
#: written in parentheses, so that ``T^1/2`` cannot read as ``T^(1/2)`` in one grammar and as
#: ``T / 2`` in the grammar of expressions.
FACTOR = re.compile(r"([A-Za-z][A-Za-z0-9_]*)(?:\^(?:(-?\d+)|\((-?\d+(?:/\d+)?)\)))?")

#: A factor of a dimensional formula with its exponent, a slash, or any other run of characters.
FORMULA_TOKEN = re.compile(r"[A-Za-z][A-Za-z0-9_]*(?:\^\(-?\d+(?:/\d+)?\)|\^-?\d+)?|/|[^\s/]+")

#: The value of a symbol whose declared formula is malformed, which its declaration reports.
MALFORMED = "malformed"


@cache
def base_dimensions(source: Path | None = None) -> frozenset[str]:
    """Return the symbols of the base dimensions that the package declares."""
    loaded = yaml.safe_load((source or REGISTRY).read_text(encoding="utf-8")) or {}
    return frozenset(str(entry["symbol"]) for entry in loaded.get("base_dimensions") or [])


@cache
def operator_rules(source: Path | None = None) -> dict[str, str]:
    """Return the rule of dimension of each canonical operator that states one."""
    loaded = yaml.safe_load((source or OPERATOR_REGISTRY).read_text(encoding="utf-8")) or {}
    return {
        str(op["symbol"]): str(op["dimension"])
        for op in loaded.get("operators") or []
        if isinstance(op, Mapping) and op.get("dimension")
    }


def parse_formula(text: Any, bases: Iterable[str]) -> dict[str, Fraction]:
    """Return the exponents of a dimensional formula over the declared bases.

    Factors are separated by spaces or by ``*``; a ``/`` makes the factors after it negative, and a
    leading ``1`` stands for no factor. A fractional exponent is written in parentheses.

    >>> sorted(parse_formula("M L T^-2", {"M", "L", "T"}).items())
    [('L', Fraction(1, 1)), ('M', Fraction(1, 1)), ('T', Fraction(-2, 1))]
    >>> parse_formula("1", {"M"}), parse_formula("1/T", {"T"}) == {"T": -1}
    ({}, True)
    >>> parse_formula("L / T", {"L", "T"}) == {"L": 1, "T": -1}
    True
    >>> parse_formula("T^(1/2)", {"T"}) == {"T": Fraction(1, 2)}
    True
    >>> for text in ("Q", "", "T^1/2", "T^(1/0)"):
    ...     try:
    ...         parse_formula(text, {"T"})
    ...     except ValueError as error:
    ...         print(error)
    Q is no declared base dimension
    the formula is empty; a pure number is written 1
    2 is not a factor; write a fractional exponent in parentheses, as T^(1/2)
    T^(1/0) divides by zero
    """
    known = set(bases)
    source = str(text).strip()
    if not source:
        raise ValueError("the formula is empty; a pure number is written 1")
    if source in ("1", "1.0"):
        return {}
    exponents: dict[str, Fraction] = {}
    sign = 1
    for position, token in enumerate(FORMULA_TOKEN.findall(source.replace("*", " "))):
        if token == "/":
            sign = -1
            continue
        if token == "1" and position == 0:
            continue
        match = FACTOR.fullmatch(token)
        if match is None:
            raise ValueError(
                f"{token} is not a factor; write a fractional exponent in parentheses, as T^(1/2)"
            )
        try:
            power = Fraction(match.group(2) or match.group(3) or 1)
        except ZeroDivisionError:
            raise ValueError(f"{token} divides by zero") from None
        base = match.group(1)
        if base not in known:
            raise ValueError(f"{base} is no declared base dimension")
        exponents[base] = exponents.get(base, Fraction(0)) + sign * power
    return {base: power for base, power in exponents.items() if power}


# --- Formulas of expressions ----------------------------------------------------------------------


def _add(a: Formula, b: Formula, sign: int = 1) -> dict[str, Fraction]:
    """Return the product of two formulas, or their quotient when ``sign`` is -1."""
    out = dict(a)
    for base, power in b.items():
        out[base] = out.get(base, Fraction(0)) + sign * power
    return {base: power for base, power in out.items() if power}


def _scale(a: Formula, factor: Fraction) -> dict[str, Fraction]:
    """Return a formula raised to a power."""
    return {base: power * factor for base, power in a.items() if power * factor}


def show(formula: Formula) -> str:
    """Return a formula written as a monomial.

    >>> show({"M": Fraction(1), "T": Fraction(-2)})
    'M T^-2'
    >>> show({})
    '1'
    """
    if not formula:
        return "1"
    order = {base: i for i, base in enumerate(ISQ_ORDER)}
    ranked = sorted(formula.items(), key=lambda item: (order.get(item[0], len(order)), item[0]))
    return " ".join(base if power == 1 else f"{base}^{power}" for base, power in ranked)


@dataclass
class Evaluation:
    """The formula of an expression, the violations met while computing it, and the causes that
    leave a part of it undecided: the symbols declaring no formula, and the operators stating no
    rule of dimension."""

    symbols: Mapping[str, Formula | str | None]
    rules: Mapping[str, str]
    violations: list[tuple[str, str]] = field(default_factory=list)
    missing: set[str] = field(default_factory=set)
    unruled: set[str] = field(default_factory=set)
    result: Value = None
    quiet: int = 0

    # pylint: disable-next=too-many-return-statements  # one return per construct of a tree
    def value(self, tree: Tree) -> Value:
        """Return the formula of a tree, ``STATEMENT`` for a statement, None when undecided."""
        kind = tree[0]
        if kind == "num":
            return None if tree[1] == 0 else PURE
        if kind == "str":
            return None
        if kind == "sym":
            return self._symbol(tree[1])
        if kind == "call":
            return self._call(tree[1], tree[2])
        if kind in ("logic", "not"):
            label = tree[1] if kind == "logic" else "not"
            for part in tree[1:]:
                if isinstance(part, tuple):
                    self._statement(self.value(part), f"the connective {label}")
            return STATEMENT
        if kind == "neg":
            return self._quantity(self.value(tree[1]), "a negation")
        if kind == "pow":
            return self._power(tree[1], tree[2])
        if kind == "cmp" and tree[1] == "~":
            return self._scaling(tree)
        return self._binary(tree)

    def _statement(self, value: Value, site: str) -> None:
        """Report a quantity where a statement is required."""
        if isinstance(value, Mapping):
            self.violations.append(
                (
                    "mistyped-operand",
                    f"{site} takes a quantity of formula {show(value)}",
                )
            )

    def _quantity(self, value: Value, site: str) -> Value:
        """Report a statement where a quantity is required, and return the value of a quantity."""
        if value == STATEMENT:
            self.violations.append(("mistyped-operand", f"{site} takes a statement"))
            return None
        return value

    def _binary(self, tree: Tree) -> Value:
        """Return the formula of a product, a quotient, a sum, a difference or a relation other than
        a scaling."""
        kind, op = tree[0], tree[1]
        what = {"prod": "a product", "sum": "a sum"}.get(kind, f"the relation {op}")
        left = self._quantity(self.value(tree[2]), what)
        right = self._quantity(self.value(tree[3]), what)
        if kind == "prod":
            if isinstance(left, Mapping) and isinstance(right, Mapping):
                return _add(left, right, 1 if op == "*" else -1)
            return None
        if kind == "cmp" and op == "in":
            return STATEMENT
        if isinstance(left, Mapping) and isinstance(right, Mapping) and left != right:
            sides = "the terms of a sum" if kind == "sum" else f"the sides of {op}"
            self.violations.append(
                (
                    "inhomogeneous",
                    f"{sides} have the formulas {show(left)} and {show(right)}",
                )
            )
            return STATEMENT if kind == "cmp" else None
        if kind == "cmp":
            return STATEMENT
        return left if isinstance(left, Mapping) else right

    def _scaling(self, tree: Tree) -> Value:
        """Return the statement of a scaling ``a ~ b``, whose sides are evaluated quietly for their
        own defects: the prefactor absorbs any formula, so neither side leaves the relation
        unchecked."""
        self.quiet += 1
        try:
            for side in (tree[2], tree[3]):
                self._quantity(self.value(side), "the relation ~")
        finally:
            self.quiet -= 1
        return STATEMENT

    def _symbol(self, name: str) -> Value:
        """Return the formula of a declared symbol, recording it as missing when it states none; a
        symbol whose formula is malformed is reported where it is declared."""
        if name not in self.symbols:
            return None
        found = self.symbols[name]
        if found == MALFORMED:
            return None
        if found is None and not self.quiet:
            self.missing.add(name)
        return found if isinstance(found, Mapping) else None

    def _call(self, name: str, args: tuple[Tree, ...]) -> Value:
        """Return the formula of a call: a quantity with its indices, or an operator by its rule."""
        if name in self.symbols:
            self.quiet += 1
            try:
                for arg in args:
                    self.value(arg)
            finally:
                self.quiet -= 1
            return self._symbol(name)
        rule = self.rules.get(name)
        if rule is None and not self.quiet:
            self.unruled.add(name)
        values = [self._argument(arg, rule, position) for position, arg in enumerate(args)]
        return self._apply(name, rule, values)

    # pylint: disable-next=too-many-return-statements  # one return per rule of dimension
    def _apply(self, name: str, rule: str | None, values: list[Value]) -> Value:
        """Return the formula that the rule of an operator gives its arguments."""
        if rule == "connective":
            for v in values:
                self._statement(v, f"the operator {name}")
            return STATEMENT
        if rule == "statement":
            return STATEMENT
        if rule == "preserve" and values:
            return values[0] if isinstance(values[0], Mapping) else None
        if rule == "product":
            if values and all(isinstance(v, Mapping) for v in values):
                total: dict[str, Fraction] = {}
                for v in values:
                    total = _add(total, v)  # type: ignore[arg-type]
                return total
            return None
        if rule in DERIVATIVE_RULES:
            return self._derivative(name, rule, values)
        if rule == "pure-argument":
            for v in values:
                if isinstance(v, Mapping) and v:
                    self.violations.append(
                        (
                            "impure-argument",
                            f"the argument of {name} has the formula {show(v)}",
                        )
                    )
            return PURE
        if rule == "pure":
            return PURE
        return None

    def _derivative(self, name: str, rule: str, values: list[Value]) -> Value:
        """Return the formula of a derivative: the function divided by its coordinates, once or
        twice, with the point of evaluation, when given, sharing the formula of the coordinates.
        """
        if len(values) < 2:
            return None
        if rule == "derivative-at" and len(values) >= 3:
            variable, point = values[1], values[2]
            if isinstance(variable, Mapping) and isinstance(point, Mapping) and variable != point:
                self.violations.append(
                    (
                        "inhomogeneous",
                        f"the point of {name} has the formula {show(point)}, and its coordinates"
                        f" {show(variable)}",
                    )
                )
        if isinstance(values[0], Mapping) and isinstance(values[1], Mapping):
            order = 2 if rule == "second-derivative" else 1
            return _add(values[0], _scale(values[1], Fraction(order)), -1)
        return None

    def _argument(self, tree: Tree, rule: str | None, position: int) -> Value:
        """Return the formula of an argument, counting its missing formulas only where the rule
        of the operator uses that argument: a connective and a relation use each argument.
        """
        used = rule in (
            "product",
            "pure-argument",
            "connective",
            "statement",
            *DERIVATIVE_RULES,
        )
        used = used or (rule == "preserve" and position == 0)
        if used:
            return self.value(tree)
        self.quiet += 1
        try:
            return self.value(tree)
        finally:
            self.quiet -= 1

    def _power(self, base: Tree, exponent: Tree) -> Value:
        """Return the formula of a power, whose exponent must be a pure number; a symbolic exponent
        leaves the formula of a dimensioned base undecided."""
        left = self._quantity(self.value(base), "a power")
        right = self._quantity(self.value(exponent), "an exponent")
        if isinstance(right, Mapping) and right:
            self.violations.append(
                ("impure-argument", f"an exponent has the formula {show(right)}")
            )
            return None
        constant = number(exponent)
        if isinstance(left, Mapping) and constant is not None:
            return _scale(left, constant)
        if isinstance(left, Mapping) and not left:
            return PURE
        if isinstance(left, Mapping) and not self.quiet:
            self.unruled.add("^")
        return None


def evaluate(
    text: Any,
    symbols: Mapping[str, Formula | str | None],
    rules_: Mapping[str, str] | None = None,
) -> Evaluation | None:
    """Return the evaluation of an expression, or None when the text is not an expression.

    >>> symbols = {"F": {"M": 1, "L": 1, "T": -2}, "m": {"M": 1}, "a": {"L": 1, "T": -2}, "v": None}
    >>> evaluate("F = m * a", symbols).violations
    []
    >>> evaluate("F = m + a", symbols).violations
    [('inhomogeneous', 'the terms of a sum have the formulas M and L T^-2')]
    >>> sorted(evaluate("F = m * v", symbols).missing)
    ['v']
    """
    tree = parse_expression(text)
    if tree is None:
        return None
    evaluation = Evaluation(symbols, operator_rules() if rules_ is None else rules_)
    evaluation.result = evaluation.value(tree)
    return evaluation


# --- Checks of a record ---------------------------------------------------------------------------


def _entries(record: Mapping[str, Any], block: str) -> list[tuple[int, Mapping[str, Any]]]:
    """Return the entries of a block of the record that are mappings, with their indices."""
    found = record.get(block)
    if not isinstance(found, list):
        return []
    return [(i, item) for i, item in enumerate(found) if isinstance(item, Mapping)]


@cache
def checked_fields(source: Path | None = None) -> tuple[tuple[str, ...], ...]:
    """Return the paths of the fields that hold a statement whose homogeneity the check reads."""
    loaded = yaml.safe_load((source or REGISTRY).read_text(encoding="utf-8")) or {}
    return tuple(tuple(str(path).split(".")) for path in loaded.get("checked_fields") or [])


def formula_entries(
    record: Mapping[str, Any],
) -> list[tuple[tuple[Any, ...], Mapping[str, Any]]]:
    """Return each entry of a record that may carry a dimensional formula, with its locus.

    >>> record = {"manifestations": [{"symbol": "m", "features": [{"symbol": "z"}]}]}
    >>> [entry["symbol"] for _, entry in formula_entries(record)]
    ['z']
    """
    found = []
    for block in FORMULA_BLOCKS:
        for locus, entries in values_at(record, tuple(block.split("."))):
            for i, entry in enumerate(entries if isinstance(entries, list) else []):
                if isinstance(entry, Mapping):
                    found.append(((*locus, Entry(i, entry)), entry))
    return found


def declares_formula(record: Mapping[str, Any]) -> bool:
    """Tell whether some entry of a record states a dimensional formula."""
    return any(entry.get("dimensional_formula") is not None for _, entry in formula_entries(record))


def _parsed(stated: Any, known: set[str]) -> Formula | str | None:
    """Return the formula that a field states, ``MALFORMED`` when it is no monomial over the
    declared bases, or None when the field states none."""
    if stated is None:
        return None
    try:
        return parse_formula(stated, known)
    except ValueError:
        return MALFORMED


def declared_formulas(
    records: Iterable[Mapping[str, Any]], bases: Iterable[str]
) -> dict[str, Formula | str | None]:
    """Return the formula of each quantity and each index set that the records declare, None when
    it states none, and ``MALFORMED`` when it states a malformed one."""
    known = set(bases)
    table: dict[str, Formula | str | None] = {}
    for record in records:
        for _, entry in formula_entries(record):
            symbol = entry.get("symbol")
            if isinstance(symbol, str):
                table[symbol] = _parsed(entry.get("dimensional_formula"), known)
    return table


def malformed_formulas(record: Mapping[str, Any], bases: Iterable[str]) -> list[Finding]:
    """Return the dimensional formulas of a record that are not monomials over declared bases.

    >>> record = {"variables": [{"symbol": "u", "dimensional_formula": "L Q"}]}
    >>> [f.text for f in malformed_formulas(record, {"L"})]
    ['variables.u.dimensional_formula: Q is no declared base dimension']
    """
    found = []
    for locus, entry in formula_entries(record):
        stated = entry.get("dimensional_formula")
        if stated is None:
            continue
        try:
            parse_formula(stated, bases)
        except ValueError as error:
            found.append(
                finding(
                    rules.DIMENSION_MALFORMED_FORMULA,
                    f"{where(locus)}.dimensional_formula: {error}",
                    *locus,
                    "dimensional_formula",
                )
            )
    return found


def conflicting_formulas(
    record: Mapping[str, Any], seen: Iterable[Mapping[str, Any]], bases: Iterable[str]
) -> list[Finding]:
    """Return the formulas that a record declares for a symbol to which another record that it
    sees gives another formula, since a symbol carries one formula.

    >>> a = {"id": "a", "variables": [{"symbol": "u", "dimensional_formula": "L"}]}
    >>> b = {"id": "b", "variables": [{"symbol": "u", "dimensional_formula": "T"}]}
    >>> [f.text for f in conflicting_formulas(a, [a, b], {"L", "T"})]
    ['variables.u.dimensional_formula: L, whereas b declares T']
    """
    known = set(bases)
    others: dict[str, list[tuple[str, Formula]]] = {}
    for other in seen:
        if other is record:
            continue
        for _, entry in formula_entries(other):
            parsed = _parsed(entry.get("dimensional_formula"), known)
            if isinstance(entry.get("symbol"), str) and isinstance(parsed, Mapping):
                others.setdefault(entry["symbol"], []).append((str(other.get("id")), parsed))
    found = []
    for locus, entry in formula_entries(record):
        mine = _parsed(entry.get("dimensional_formula"), known)
        if not isinstance(mine, Mapping):
            continue
        for owner, theirs in others.get(str(entry.get("symbol")), []):
            if dict(theirs) != dict(mine):
                found.append(
                    finding(
                        rules.DIMENSION_CONFLICTING_FORMULA,
                        f"{where(locus)}.dimensional_formula: {show(mine)}, whereas {owner}"
                        f" declares {show(theirs)}",
                        *locus,
                        "dimensional_formula",
                        value=owner,
                    )
                )
    return found


def colliding_bases(record: Mapping[str, Any]) -> list[Finding]:
    """Return the base scales of an operator record whose symbol is already a base dimension of
    the package, since a base scale adds a dimension and its symbol is unique among them.

    >>> [f.text for f in colliding_bases({"base_scales": [{"symbol": "L", "name": "loss"}]})]
    ['base_scales.L: the symbol is already the base dimension L']
    """
    taken = base_dimensions()
    return [
        finding(
            rules.DIMENSION_COLLIDING_BASE,
            f"base_scales.{entry.get('symbol')}: the symbol is already the base dimension"
            f" {entry.get('symbol')}",
            "base_scales",
            Entry(i, entry),
            "symbol",
        )
        for i, entry in _entries(record, "base_scales")
        if entry.get("symbol") in taken
    ]


@dataclass(frozen=True)
class Scope:
    """What the dimensional checks of one record read: the formulas that it sees, the rules of the
    operators, and whether its problem declares any formula."""

    symbols: Mapping[str, Formula | str | None]
    rules: Mapping[str, str]
    opted_in: bool


def _violations(evaluation: Evaluation, where_: str, place: tuple[Any, ...]) -> list[Finding]:
    """Return one finding per violation met by an evaluation."""
    rule = {
        "inhomogeneous": rules.DIMENSION_INHOMOGENEOUS,
        "impure-argument": rules.DIMENSION_IMPURE_ARGUMENT,
        "mistyped-operand": rules.DIMENSION_MISTYPED_OPERAND,
    }
    return [
        finding(rule[kind], f"{where_}: {text}", *place, value=text)
        for kind, text in evaluation.violations
    ]


def _undecided(evaluation: Evaluation) -> str:
    """Return the causes that leave an expression unchecked, or an empty string."""
    causes = []
    if evaluation.missing:
        causes.append(
            f"no dimensional formula is declared for {', '.join(sorted(evaluation.missing))}"
        )
    for name in sorted(evaluation.unruled):
        causes.append(
            "a power has a symbolic exponent"
            if name == "^"
            else f"the operator {name} states no rule of dimension"
        )
    return "; ".join(causes)


def dimension_problems(record: Mapping[str, Any], scope: Scope) -> list[Finding]:
    """Return the violations of homogeneity of the statements and the definitions of a record, the
    definitions whose formula differs from the declared one, and, in a problem that declares
    formulas, the statements left unchecked for want of a formula or of a rule of dimension.

    >>> scope = Scope({"F": {"M": 1}, "m": {"M": 1}, "x": None}, {}, True)
    >>> record = {"laws": [{"symbol": "newton", "expression": "F = m + x"}]}
    >>> [f.text for f in dimension_problems(record, scope)]
    ['laws.newton.expression: no dimensional formula is declared for x, so the law is not checked']
    >>> record = {"laws": [{"symbol": "edge", "expression": "restrict(F) = m"}]}
    >>> for f in dimension_problems(record, scope):
    ...     print(f.text)  # doctest: +NORMALIZE_WHITESPACE
    laws.edge.expression: the operator restrict states no rule of dimension, so the law is not
    checked
    """
    found: list[Finding] = []
    for path in checked_fields():
        for locus, text in values_at(record, path):
            evaluation = evaluate(text, scope.symbols, scope.rules)
            if evaluation is None:
                continue
            place = tuple(locus)
            found += _violations(evaluation, where(locus), place)
            causes = _undecided(evaluation)
            if scope.opted_in and causes:
                found.append(
                    finding(
                        rules.DIMENSION_UNCHECKED_LAW,
                        f"{where(locus)}: {causes}, so the law is not checked",
                        *place,
                    )
                )
    for block in QUANTITY_BLOCKS:
        for i, entry in _entries(record, block):
            symbol = entry.get("symbol")
            place = (block, Entry(i, entry), "expression")
            evaluation = evaluate(entry.get("expression"), scope.symbols, scope.rules)
            if evaluation is None:
                continue
            found += _violations(evaluation, f"{block}.{symbol or i}.expression", place)
            declared = scope.symbols.get(str(symbol))
            computed = evaluation.result
            if (
                isinstance(declared, Mapping)
                and isinstance(computed, Mapping)
                and dict(declared) != dict(computed)
            ):
                found.append(
                    finding(
                        rules.DIMENSION_MISMATCHED_DEFINITION,
                        f"{block}.{symbol or i}.expression: the definition has the formula"
                        f" {show(computed)}, and the quantity declares {show(declared)}",
                        *place,
                    )
                )
    return found
