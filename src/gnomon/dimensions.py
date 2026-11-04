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
parse_expression
    Return the tree of an expression, or None when the text is not an expression.
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
from .findings import Entry, Finding, finding

#: The registry of the base dimensions.
REGISTRY = Path(__file__).parent / "data" / "registries" / "dimensions.yml"

#: The registry of the canonical operators, whose entries state their rule of dimension.
OPERATOR_REGISTRY = Path(__file__).parent / "data" / "operators.yml"

#: The blocks whose entries are quantities, whose definitions are checked against their formula.
QUANTITY_BLOCKS: tuple[str, ...] = ("variables", "parameters", "observables")

#: The blocks whose entries may carry a dimensional formula: the quantities, and the index sets,
#: whose formula a derivative along the index divides by.
FORMULA_BLOCKS: tuple[str, ...] = (*QUANTITY_BLOCKS, "index_sets")

#: The blocks whose entries are laws, whose expressions must be homogeneous.
LAW_BLOCKS: tuple[str, ...] = ("laws",)

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

FACTOR = re.compile(r"([A-Za-z][A-Za-z0-9_]*)(?:\^\(?(-?\d+(?:/\d+)?)\)?)?")

#: A factor of a dimensional formula with its exponent, a slash, or any other character.
FORMULA_TOKEN = re.compile(r"[A-Za-z][A-Za-z0-9_]*(?:\^\(-?\d+(?:/\d+)?\)|\^-?\d+(?:/\d+)?)?|/|\S")


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

    Factors are separated by spaces or by ``*``; a ``/`` makes the factors after it negative.

    >>> sorted(parse_formula("M L T^-2", {"M", "L", "T"}).items())
    [('L', Fraction(1, 1)), ('M', Fraction(1, 1)), ('T', Fraction(-2, 1))]
    >>> parse_formula("1", {"M"})
    {}
    >>> parse_formula("L / T", {"L", "T"}) == {"L": 1, "T": -1}
    True
    >>> parse_formula("Q", {"M"})
    Traceback (most recent call last):
    ...
    ValueError: Q is no declared base dimension
    """
    known = set(bases)
    source = str(text).strip()
    if source in ("1", "1.0"):
        return {}
    exponents: dict[str, Fraction] = {}
    sign = 1
    for token in FORMULA_TOKEN.findall(source.replace("*", " ")):
        if token == "/":
            sign = -1
            continue
        match = FACTOR.fullmatch(token)
        if match is None:
            raise ValueError(f"{token} is not a factor of a dimensional formula")
        base, power = match.group(1), Fraction(match.group(2) or 1)
        if base not in known:
            raise ValueError(f"{base} is no declared base dimension")
        exponents[base] = exponents.get(base, Fraction(0)) + sign * power
    return {base: power for base, power in exponents.items() if power}


# --- Expressions ----------------------------------------------------------------------------------

TOKEN = re.compile(
    r"\s*(?:(?P<num>\d+(?:\.\d+)?(?:[eE][-+]?\d+)?)|(?P<str>\"[^\"]*\")"
    r"|(?P<name>[A-Za-z][A-Za-z0-9_]*)|(?P<op><=|>=|!=|==|[-+*/^=<>(),{}]))"
)

#: A tree of an expression: a tuple whose first item names the construct.
Tree = tuple[Any, ...]

COMPARISONS = frozenset({"=", "==", "!=", "<", "<=", ">", ">=", "in"})


def _tokens(text: str) -> list[tuple[str, str]] | None:
    """Return the tokens of an expression, or None when a character opens no token."""
    found: list[tuple[str, str]] = []
    position = 0
    text = text.rstrip()
    while position < len(text):
        match = TOKEN.match(text, position)
        if match is None or match.end() == position:
            return None
        kind = match.lastgroup or ""
        found.append((kind, match.group(kind)))
        position = match.end()
    return found


@dataclass
class _Parser:
    """A recursive-descent parser over the tokens of one expression."""

    tokens: list[tuple[str, str]]
    position: int = 0

    def peek(self) -> str | None:
        """Return the text of the next token, or None at the end."""
        return self.tokens[self.position][1] if self.position < len(self.tokens) else None

    def take(self, expected: str | None = None) -> tuple[str, str]:
        """Consume the next token, which must read ``expected`` when it is given."""
        if self.position >= len(self.tokens):
            raise ValueError("the expression ends early")
        token = self.tokens[self.position]
        if expected is not None and token[1] != expected:
            raise ValueError(f"expected {expected}, found {token[1]}")
        self.position += 1
        return token

    def expression(self) -> Tree:
        """Parse an implication, the loosest construct."""
        left = self.disjunction()
        if self.peek() == "implies":
            self.take()
            return ("logic", "implies", left, self.expression())
        return left

    def disjunction(self) -> Tree:
        """Parse a disjunction."""
        left = self.conjunction()
        while self.peek() == "or":
            self.take()
            left = ("logic", "or", left, self.conjunction())
        return left

    def conjunction(self) -> Tree:
        """Parse a conjunction."""
        left = self.negation()
        while self.peek() == "and":
            self.take()
            left = ("logic", "and", left, self.negation())
        return left

    def negation(self) -> Tree:
        """Parse a negation."""
        if self.peek() == "not":
            self.take()
            return ("not", self.negation())
        return self.comparison()

    def comparison(self) -> Tree:
        """Parse an equation or an inequality."""
        left = self.additive()
        while self.peek() in COMPARISONS:
            op = self.take()[1]
            left = ("cmp", op, left, self.additive())
        return left

    def additive(self) -> Tree:
        """Parse a sum or a difference."""
        left = self.multiplicative()
        while self.peek() in ("+", "-"):
            op = self.take()[1]
            left = ("sum", op, left, self.multiplicative())
        return left

    def multiplicative(self) -> Tree:
        """Parse a product or a quotient."""
        left = self.unary()
        while self.peek() in ("*", "/"):
            op = self.take()[1]
            left = ("prod", op, left, self.unary())
        return left

    def unary(self) -> Tree:
        """Parse a negated term."""
        if self.peek() == "-":
            self.take()
            return ("neg", self.unary())
        return self.power()

    def power(self) -> Tree:
        """Parse a power."""
        base = self.primary()
        if self.peek() == "^":
            self.take()
            return ("pow", base, self.unary())
        return base

    def primary(self) -> Tree:
        """Parse a number, a string, a symbol, a call, a binder or a parenthesized expression."""
        kind, text = self.take()
        if kind == "num":
            return ("num", Fraction(text))
        if kind == "str":
            return ("str", text)
        if text == "(":
            inner = self.expression()
            self.take(")")
            return inner
        if kind != "name":
            raise ValueError(f"unexpected {text}")
        name, binds = text, []
        if name.endswith("_") and self.peek() == "{":
            name = name[:-1]
            self.take("{")
            while self.peek() != "}":
                binds.append(self.take()[1])
                if self.peek() == ",":
                    self.take()
            self.take("}")
        if self.peek() == "(":
            self.take()
            args = []
            while self.peek() != ")":
                args.append(self.expression())
                if self.peek() == ",":
                    self.take()
            self.take(")")
            return ("call", name, tuple(args), tuple(binds))
        return ("sym", name)


def parse_expression(text: Any) -> Tree | None:
    """Return the tree of an expression, or None when the text is not an expression.

    >>> parse_expression("U * L / nu")
    ('prod', '/', ('prod', '*', ('sym', 'U'), ('sym', 'L')), ('sym', 'nu'))
    >>> parse_expression("mean_{x}( u(x) )")
    ('call', 'mean', (('call', 'u', (('sym', 'x'),), ()),), ('x',))
    >>> parse_expression("the state maps to tipped") is None
    True
    """
    if not isinstance(text, str) or not text.strip():
        return None
    tokens = _tokens(text)
    if not tokens:
        return None
    parser = _Parser(tokens)
    try:
        tree = parser.expression()
    except ValueError:
        return None
    return tree if parser.position == len(tokens) else None


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
    """The formula of an expression, and the violations met while computing it."""

    symbols: Mapping[str, Formula | None]
    rules: Mapping[str, str]
    violations: list[tuple[str, str]] = field(default_factory=list)
    missing: set[str] = field(default_factory=set)
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
            for part in tree[1:]:
                if isinstance(part, tuple):
                    self.value(part)
            return STATEMENT
        if kind == "neg":
            return self.value(tree[1])
        if kind == "pow":
            return self._power(tree[1], tree[2])
        return self._binary(tree)

    def _binary(self, tree: Tree) -> Value:
        """Return the formula of a product, a quotient, a sum, a difference or a comparison."""
        kind = tree[0]
        left, right = self.value(tree[2]), self.value(tree[3])
        if kind == "prod":
            if isinstance(left, Mapping) and isinstance(right, Mapping):
                return _add(left, right, 1 if tree[1] == "*" else -1)
            return None
        if isinstance(left, Mapping) and isinstance(right, Mapping) and left != right:
            what = "the terms of a sum" if kind == "sum" else f"the sides of {tree[1]}"
            self.violations.append(
                ("inhomogeneous", f"{what} have the formulas {show(left)} and {show(right)}")
            )
            return STATEMENT if kind == "cmp" else None
        if kind == "cmp":
            return STATEMENT
        return left if isinstance(left, Mapping) else right

    def _symbol(self, name: str) -> Value:
        """Return the formula of a declared symbol, recording it as missing when it states none."""
        if name not in self.symbols:
            return None
        found = self.symbols[name]
        if found is None and not self.quiet:
            self.missing.add(name)
        return found

    # pylint: disable-next=too-many-return-statements  # one return per rule of dimension
    def _call(self, name: str, args: tuple[Tree, ...]) -> Value:
        """Return the formula of a call: a quantity with its indices, or an operator by its rule."""
        if name in self.symbols:
            return self._symbol(name)
        rule = self.rules.get(name)
        values = [self._argument(arg, rule, position) for position, arg in enumerate(args)]
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
                        ("impure-argument", f"the argument of {name} has the formula {show(v)}")
                    )
            return PURE
        if rule == "pure":
            return PURE
        return None

    def _derivative(self, name: str, rule: str, values: list[Value]) -> Value:
        """Return the formula of a derivative: the function divided by its coordinates, once or
        twice, with the point of evaluation, when given, sharing the formula of the coordinates."""
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
        of the operator uses that argument."""
        used = rule in ("product", "pure-argument", *DERIVATIVE_RULES) or (
            rule == "preserve" and position == 0
        )
        if used:
            return self.value(tree)
        self.quiet += 1
        try:
            return self.value(tree)
        finally:
            self.quiet -= 1

    def _power(self, base: Tree, exponent: Tree) -> Value:
        """Return the formula of a power, whose exponent must be a pure number."""
        left, right = self.value(base), self.value(exponent)
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
        return None


def number(tree: Tree) -> Fraction | None:
    """Return the value of a tree built from numbers alone, or None.

    >>> number(parse_expression("-(1/4)"))
    Fraction(-1, 4)
    """
    if tree[0] == "num":
        return Fraction(tree[1])
    if tree[0] == "neg":
        inner = number(tree[1])
        return -inner if inner is not None else None
    if tree[0] == "prod":
        left, right = number(tree[2]), number(tree[3])
        if left is None or right is None or (tree[1] == "/" and right == 0):
            return None
        return left * right if tree[1] == "*" else left / right
    return None


def evaluate(
    text: Any, symbols: Mapping[str, Formula | None], rules_: Mapping[str, str] | None = None
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


def declared_formulas(
    records: Iterable[Mapping[str, Any]], bases: Iterable[str]
) -> dict[str, Formula | None]:
    """Return the formula of each quantity and each index set that the records declare, None when
    it states none or states a malformed one."""
    known = set(bases)
    table: dict[str, Formula | None] = {}
    for record in records:
        for block in FORMULA_BLOCKS:
            for _, entry in _entries(record, block):
                symbol = entry.get("symbol")
                if not isinstance(symbol, str):
                    continue
                stated = entry.get("dimensional_formula")
                try:
                    table[symbol] = parse_formula(stated, known) if stated is not None else None
                except ValueError:
                    table[symbol] = None
    return table


def malformed_formulas(record: Mapping[str, Any], bases: Iterable[str]) -> list[Finding]:
    """Return the dimensional formulas of a record that are not monomials over declared bases.

    >>> record = {"variables": [{"symbol": "u", "dimensional_formula": "L Q"}]}
    >>> [f.text for f in malformed_formulas(record, {"L"})]
    ['variables.u.dimensional_formula: Q is no declared base dimension']
    """
    found = []
    for block in FORMULA_BLOCKS:
        for i, entry in _entries(record, block):
            stated = entry.get("dimensional_formula")
            if stated is None:
                continue
            try:
                parse_formula(stated, bases)
            except ValueError as error:
                found.append(
                    finding(
                        rules.DIMENSION_MALFORMED_FORMULA,
                        f"{block}.{entry.get('symbol') or i}.dimensional_formula: {error}",
                        block,
                        Entry(i, entry),
                        "dimensional_formula",
                    )
                )
    return found


@dataclass(frozen=True)
class Scope:
    """What the dimensional checks of one record read: the formulas that it sees, the rules of the
    operators, and whether its problem declares any formula."""

    symbols: Mapping[str, Formula | None]
    rules: Mapping[str, str]
    opted_in: bool


def _violations(evaluation: Evaluation, where: str, place: tuple[Any, ...]) -> list[Finding]:
    """Return one finding per violation of homogeneity met by an evaluation."""
    rule = {
        "inhomogeneous": rules.DIMENSION_INHOMOGENEOUS,
        "impure-argument": rules.DIMENSION_IMPURE_ARGUMENT,
    }
    return [
        finding(rule[kind], f"{where}: {text}", *place, value=text)
        for kind, text in evaluation.violations
    ]


def dimension_problems(record: Mapping[str, Any], scope: Scope) -> list[Finding]:
    """Return the violations of homogeneity of the laws and the definitions of a record, the
    definitions whose formula differs from the declared one, and, in a problem that declares
    formulas, the laws left unchecked for want of a formula.

    >>> scope = Scope({"F": {"M": 1}, "m": {"M": 1}, "x": None}, {}, True)
    >>> record = {"laws": [{"symbol": "newton", "expression": "F = m + x"}]}
    >>> [f.text for f in dimension_problems(record, scope)]
    ['laws.newton.expression: no dimensional formula is declared for x, so the law is not checked']
    """
    found: list[Finding] = []
    for block in LAW_BLOCKS:
        for i, entry in _entries(record, block):
            evaluation = evaluate(entry.get("expression"), scope.symbols, scope.rules)
            if evaluation is None:
                continue
            where = f"{block}.{entry.get('symbol') or entry.get('name') or i}.expression"
            place = (block, Entry(i, entry), "expression")
            found += _violations(evaluation, where, place)
            if scope.opted_in and evaluation.missing:
                found.append(
                    finding(
                        rules.DIMENSION_UNCHECKED_LAW,
                        f"{where}: no dimensional formula is declared for"
                        f" {', '.join(sorted(evaluation.missing))}, so the law is not checked",
                        *place,
                    )
                )
    for block in QUANTITY_BLOCKS:
        for i, entry in _entries(record, block):
            symbol = entry.get("symbol")
            place = (block, Entry(i, entry), "expression")
            where = f"{block}.{symbol or i}.expression"
            evaluation = evaluate(entry.get("expression"), scope.symbols, scope.rules)
            if evaluation is None:
                continue
            found += _violations(evaluation, where, place)
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
                        f"{where}: the definition has the formula {show(computed)}, and the"
                        f" quantity declares {show(declared)}",
                        *place,
                    )
                )
    return found
