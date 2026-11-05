"""
The expressions of the records: their tokens, their grammar, and the tree that a parser builds.

An expression is written over declared symbols and the operators of the canonical set or of a
problem, as the decision on the expression syntax fixes it. The parser turns it into a tree whose
head names the construct, so that every check and every view reads one structure: a number, a
string, a symbol, a call with its arguments and the indices that a binder binds, a connective, a
negation, a power, a product, a sum or a comparison. Text that the grammar does not cover, such as
prose, parses to no tree.

Functions
---------
parse_expression
    Return the tree of an expression, or None when the text is not an expression.
number
    Return the value of a tree built from numbers alone, or None.
"""

from __future__ import annotations

import re
from dataclasses import dataclass
from fractions import Fraction
from typing import Any, Callable

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
            binds = self._list("}", self._index)
        if self.peek() == "(":
            self.take()
            args = self._list(")", self.expression)
            return ("call", name, tuple(args), tuple(binds))
        return ("sym", name)

    def _index(self) -> str:
        """Parse one index of a binder, with its restriction when it carries one, as in
        ``t <= T`` or ``a1 in a``, and return the name of the index."""
        kind, name = self.take()
        if kind != "name":
            raise ValueError(f"expected an index, found {name}")
        if self.peek() in COMPARISONS:
            self.take()
            self.additive()
        return name

    def _list(self, closing: str, item: Callable[[], Any]) -> list[Any]:
        """Parse the items of a list separated by commas up to its closing token, so that two
        items without a comma, or a trailing comma, make the text no expression."""
        items: list[Any] = []
        if self.peek() == closing:
            self.take()
            return items
        while True:
            items.append(item())
            if self.peek() == ",":
                self.take()
                if self.peek() == closing:
                    raise ValueError("a list ends with a comma")
                continue
            self.take(closing)
            return items


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
