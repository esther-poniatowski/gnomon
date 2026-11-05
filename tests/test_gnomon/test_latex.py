"""The LaTeX form of the expressions of the records.

The form is composed from the notation of each operator and of each symbol, and the view of the
worked inquiries holds one row per expression that parses. Each rule of composition is shown on a
case whose form is known.
"""

from __future__ import annotations

from pathlib import Path

import pytest

from gnomon.check import load_workspace
from gnomon.latex import canonical_notations, to_latex
from gnomon.views import expression_forms

ROOT = Path(__file__).resolve().parents[2]
SYMBOLS = {"u": "", "x": "", "t": "", "nu": "", "N": "", "E": "", "T": "", "K": ""}


@pytest.mark.parametrize(
    ("text", "form"),
    [
        ("diff(u, t) = nu * lap(u, x)", r"\partial_{t} u = \nu \, \Delta_{x} u"),
        ("max_{t <= T}( E(t) ) <= 1", r"\max_{t \leq T} E(t) \leq 1"),
        ("norm_{a1 in a}( K(a1) )", r"\lVert K(a_{1}) \rVert_{a_{1} \in a}"),
        ("min(pos(reals))", r"\min \mathbb{R}_{>0}"),
        ("(u + x) * nu", r"\left( u + x \right) \, \nu"),
        ("u - (x - t)", r"u - \left( x - t \right)"),
        ("N >= 0 implies not (u > 0)", r"N \geq 0 \Rightarrow \lnot \left( u > 0 \right)"),
        ("prod(reals, reals, ints)", r"\mathbb{R} \times \mathbb{R} \times \mathbb{Z}"),
        ("f(u)", r"\operatorname{f}(u)"),
    ],
)
def test_the_form_of_an_expression(text: str, form: str) -> None:
    assert to_latex(text, canonical_notations(), SYMBOLS) == form


def test_the_view_holds_the_form_of_each_law_with_its_declared_notations() -> None:
    view = expression_forms(load_workspace(ROOT / "examples").by_id)
    forms = {(row["record"], row["field"]): row["latex"] for row in view["expressions"]}
    momentum = (
        "bg.turbulence-incompressible-navier-stokes.navier-stokes",
        "laws.momentum.expression",
    )
    assert forms[momentum] == (
        r"\partial_{t} u + u \cdot \nabla_{x} u = -\nabla_{x} \mathrm{pr} + \nu \, \Delta_{x} u + f"
    )
    grokking = (
        "bg.delayed-generalization-networks.training-specification",
        "laws.update.expression",
    )
    assert r"\partial_{\mathrm{step}} \theta" in forms[grokking]
