"""
The LaTeX form of an expression, composed from the notations that the records declare.

An operator states its notation as a template, in the operator registry or in the operator record
of a problem: ``#0`` stands for the indices that a binder consumes, and ``#1``, ``#2`` for its
arguments, so that the form is composed without parsing the template. A symbol states its LaTeX
form in its field ``notation`` when the form differs from the identifier; otherwise the identifier
is written by a fixed rule: a Greek name takes its letter, trailing digits become a subscript, the
part after an underscore becomes a roman subscript, and any other name of several letters is
written upright. The connectives, the comparisons and the arithmetic take their usual signs. The
form is a presentation of the expression, so it decides nothing that a check reads.

Functions
---------
canonical_notations
    Return the notation of each canonical operator.
declared_notations
    Return each symbol that a set of records declares, with its notation.
symbol_form
    Return the LaTeX form of an identifier.
render
    Return the LaTeX form of the tree of an expression.
to_latex
    Return the LaTeX form of an expression, or None when the text is not an expression.
"""

from __future__ import annotations

import re
from fractions import Fraction
from functools import cache
from pathlib import Path
from typing import Any, Mapping

import yaml

from .expressions import Tree, parse_expression

#: The registry of the canonical operators, whose entries state their notation.
OPERATOR_REGISTRY = Path(__file__).parent / "data" / "operators.yml"

#: The names that are written as Greek letters.
GREEK = frozenset(
    {
        "alpha", "beta", "gamma", "delta", "epsilon", "varepsilon", "zeta", "eta", "theta",
        "vartheta", "iota", "kappa", "lambda", "mu", "nu", "xi", "pi", "rho", "sigma", "tau",
        "upsilon", "phi", "varphi", "chi", "psi", "omega", "Gamma", "Delta", "Theta", "Lambda",
        "Xi", "Pi", "Sigma", "Upsilon", "Phi", "Psi", "Omega",
    }
)  # fmt: skip

#: The sign of each connective, comparison and arithmetic operation written infix.
SIGNS: Mapping[str, str] = {
    "implies": r"\Rightarrow",
    "or": r"\lor",
    "and": r"\land",
    "=": "=",
    "==": "=",
    "!=": r"\neq",
    "<": "<",
    "<=": r"\leq",
    ">": ">",
    ">=": r"\geq",
    "in": r"\in",
    "->": r"\to",
    "~": r"\sim",
    "+": "+",
    "-": "-",
    "*": r"\,",
}

#: The binding strength of each construct, from the loosest; an operand binding more loosely than
#: its place requires is written in parentheses.
PRECEDENCE: Mapping[str, int] = {
    "implies": 1,
    "or": 2,
    "and": 3,
    "not": 4,
    "cmp": 5,
    "sum": 6,
    "prod": 7,
    "neg": 8,
    "pow": 9,
}

#: The strength of a number, a symbol, a call and a quotient, which need no parentheses.
ATOM = 10

#: The openings after which a placeholder of a template is already delimited.
DELIMITED = ("(", "[", "{", "|", "\\langle", "\\lvert", "\\lVert", "_{", "^{", "\\{")


@cache
def canonical_notations(source: Path | None = None) -> dict[str, str]:
    """Return the notation of each canonical operator that states one."""
    loaded = yaml.safe_load((source or OPERATOR_REGISTRY).read_text(encoding="utf-8")) or {}
    return {
        str(op["symbol"]): str(op["notation"])
        for op in loaded.get("operators") or []
        if isinstance(op, Mapping) and op.get("notation")
    }


def declared_notations(records: Any) -> dict[str, str]:
    """Return each symbol that a set of records declares, with its notation, empty when the record
    declares none, wherever the declaring entry sits in the record.

    >>> declared_notations([{"variables": [{"symbol": "nu", "notation": "\\nu"}],
    ...                      "manifestations": [{"features": [{"symbol": "z"}]}]}])
    {'nu': '\\nu', 'z': ''}
    """
    found: dict[str, str] = {}

    def walk(node: Any) -> None:
        if isinstance(node, Mapping):
            symbol = node.get("symbol")
            if isinstance(symbol, str) and symbol not in found:
                found[symbol] = str(node.get("notation") or "")
            for value in node.values():
                walk(value)
        elif isinstance(node, list):
            for item in node:
                walk(item)

    for record in records:
        walk(record)
    return found


def symbol_form(name: str, notations: Mapping[str, str] | None = None) -> str:
    """Return the LaTeX form of an identifier: its declared notation, or the fixed rule.

    >>> [symbol_form(n) for n in ("u", "lambda3", "eta_rep", "Ltrain", "theta0")]
    ['u', '\\\\lambda_{3}', '\\\\eta_{\\\\mathrm{rep}}', '\\\\mathrm{Ltrain}', '\\\\theta_{0}']
    >>> symbol_form("initial_optimizer_state")
    '\\\\mathrm{initial}_{\\\\mathrm{optimizer\\\\_state}}'
    >>> symbol_form("Ltrain", {"Ltrain": "L_{\\\\text{train}}"})
    'L_{\\\\text{train}}'
    """
    if notations and notations.get(name):
        return str(notations[name])
    base, _, rest = name.partition("_")
    digits = re.fullmatch(r"([A-Za-z]+?)(\d+)", base)
    if digits:
        base, index = digits.group(1), digits.group(2)
    else:
        index = ""
    if base in GREEK:
        head = f"\\{base}"
    elif len(base) == 1:
        head = base
    else:
        head = f"\\mathrm{{{base}}}"
    subscripts = [index] if index else []
    if rest:
        escaped = rest.replace("_", "\\_")
        subscripts.append(f"\\mathrm{{{escaped}}}")
    return head + (f"_{{{','.join(subscripts)}}}" if subscripts else "")


def _strength(tree: Tree) -> int:
    """Return the binding strength of a tree."""
    kind = tree[0]
    if kind == "logic":
        return PRECEDENCE[str(tree[1])]
    if kind == "prod" and tree[1] == "/":
        return ATOM
    return PRECEDENCE.get(kind, ATOM)


def _number(value: Fraction) -> str:
    """Return the form of a number: an integer, or a decimal."""
    if value.denominator == 1:
        return str(value.numerator)
    return f"{float(value):g}"


class _Renderer:  # pylint: disable=too-few-public-methods  # one entry point, `form`
    """The composition of the LaTeX form of a tree from the declared notations."""

    def __init__(self, operators: Mapping[str, str], symbols: Mapping[str, str]) -> None:
        self.operators = operators
        self.symbols = symbols

    def form(self, tree: Tree, least: int = 0) -> str:
        """Return the form of a tree, in parentheses when it binds more loosely than ``least``."""
        text = self._bare(tree)
        return f"\\left( {text} \\right)" if _strength(tree) < least else text

    # pylint: disable-next=too-many-return-statements  # one return per construct of a tree
    def _bare(self, tree: Tree) -> str:
        """Return the form of a tree, without parentheses around it."""
        kind = tree[0]
        if kind == "num":
            return _number(tree[1])
        if kind == "str":
            return f"\\text{{{str(tree[1]).strip(chr(34))}}}"
        if kind == "sym":
            name = str(tree[1])
            constant = self.operators.get(name)
            if name not in self.symbols and constant and "#" not in constant:
                return constant
            return symbol_form(name, self.symbols)
        if kind == "call":
            return self._call(tree)
        if kind == "not":
            return f"\\lnot {self.form(tree[1], ATOM)}"
        if kind == "neg":
            return f"-{self.form(tree[1], PRECEDENCE['neg'])}"
        if kind == "pow":
            return f"{self.form(tree[1], ATOM)}^{{{self.form(tree[2])}}}"
        if kind == "prod" and tree[1] == "/":
            return f"\\frac{{{self.form(tree[2])}}}{{{self.form(tree[3])}}}"
        return self._infix(tree)

    def _infix(self, tree: Tree) -> str:
        """Return the form of a connective, a comparison, a sum or a product written infix."""
        kind, op = tree[0], str(tree[1])
        strength = _strength(tree)
        if kind == "logic" and op == "implies":
            left, right = strength + 1, strength
        elif kind == "sum" and op == "-":
            left, right = strength, strength + 1
        elif kind == "cmp":
            left, right = strength + 1, strength + 1
        else:
            left, right = strength, strength
        return f"{self.form(tree[2], left)} {SIGNS[op]} {self.form(tree[3], right)}"

    def _indices(self, tree: Tree) -> str:
        """Return the indices of a binder, each with its restriction."""
        restrictions = tree[4] if len(tree) > 4 else (None,) * len(tree[3])
        return ", ".join(
            (self.form(restriction) if restriction else symbol_form(str(index), self.symbols))
            for index, restriction in zip(tree[3], restrictions, strict=False)
        )

    def _call(self, tree: Tree) -> str:
        """Return the form of a call: an operator by its template, or a quantity with its
        indices."""
        name, args = str(tree[1]), tree[2]
        template = self.operators.get(name)
        if template is None:
            head = (
                symbol_form(name, self.symbols)
                if name in self.symbols or not args
                else f"\\operatorname{{{name.replace('_', chr(92) + '_')}}}"
            )
            inner = ", ".join(self.form(arg) for arg in args)
            return f"{head}({inner})" if args else head
        return self._fill(template, tree)

    def _fill(self, template: str, tree: Tree) -> str:
        """Return a template filled with the indices and the arguments of a call; the last
        placeholder takes every remaining argument, joined as the template joins the last two.
        """
        args = tree[2]
        slots = sorted({int(n) for n in re.findall(r"#(\d)", template) if n != "0"})
        count = max(slots) if slots else 0
        separator = ", "
        if count >= 2:
            between = re.search(rf"#{count - 1}(.*?)#{count}", template)
            separator = between.group(1) if between else ", "
        indices = self._indices(tree)
        text = template.replace("_{#0}", "") if not indices else template
        text = text.replace("#0", indices)
        for position in sorted(slots, reverse=True):
            taken = args[position - 1 :] if position == count else args[position - 1 : position]
            text = text.replace(f"#{position}", self._slot(template, position, taken, separator))
        return text

    def _slot(self, template: str, position: int, taken: Any, separator: str) -> str:
        """Return the form that fills one placeholder of a template: the arguments that it takes,
        in parentheses when the template neither delimits them nor lets them bind loosely.
        """
        placed = template.index(f"#{position}")
        opening = template[:placed].rstrip()
        least = 0 if opening.endswith(DELIMITED) else PRECEDENCE["prod"]
        filled = separator.join(self.form(arg, least) for arg in taken)
        if template[placed + 2 :].startswith(("_", "^")) and " " in filled:
            filled = f"\\left( {filled} \\right)"
        return filled


def render(
    tree: Tree, operators: Mapping[str, str], symbols: Mapping[str, str] | None = None
) -> str:
    """Return the LaTeX form of the tree of an expression.

    ``symbols`` holds every declared symbol with its notation, empty when the record declares none,
    so that a call of a quantity is written with its indices and a call of any other name as an
    operator.

    >>> from gnomon.expressions import parse_expression
    >>> operators = {"sum": "\\\\sum_{#0} #1", "grad": "\\\\nabla_{#2} #1"}
    >>> render(parse_expression("sum_{i}( a(i) * b ) = grad(u, x) / 2"), operators, {"a": ""})
    '\\\\sum_{i} a(i) \\\\, b = \\\\frac{\\\\nabla_{x} u}{2}'
    """
    return _Renderer(operators, symbols or {}).form(tree)


def to_latex(
    text: Any, operators: Mapping[str, str], symbols: Mapping[str, str] | None = None
) -> str | None:
    """Return the LaTeX form of an expression, or None when the text is not an expression.

    >>> to_latex("x <= 1 and not (y > 0)", {})
    'x \\\\leq 1 \\\\land \\\\lnot \\\\left( y > 0 \\\\right)'
    >>> to_latex("the state relaxes", {}) is None
    True
    """
    tree = parse_expression(text)
    return None if tree is None else render(tree, operators, symbols)
