"""The hints of the messages: the closest known name, where an operator is declared, the grammar,
and the admitted values. Each hint is shown on a planted case.
"""

from __future__ import annotations

from gnomon.findings import close_match_hint, texts
from gnomon.vocabulary import unresolved

OPERATORS = frozenset({"mean", "max"})


def test_a_misspelled_symbol_suggests_the_closest_declared_one() -> None:
    record = {
        "type": "target-system",
        "variables": [{"symbol": "eta_rep"}, {"symbol": "lambda3"}],
        "parameters": [{"symbol": "q", "expression": "lambda3 * eta_rp"}],
    }
    assert texts(unresolved(record, OPERATORS)) == [
        "parameters.expression -> eta_rp; did you mean eta_rep?"
    ]


def test_an_unknown_call_says_where_an_operator_is_declared() -> None:
    record = {"type": "target-system", "parameters": [{"symbol": "q", "expression": "argmax(q)"}]}
    assert texts(unresolved(record, OPERATORS)) == [
        "parameters.expression -> argmax; an operator is declared in the operator record of the"
        " problem"
    ]


def test_a_distant_name_gets_no_suggestion() -> None:
    assert close_match_hint("eta_zzz", {"eta_rep"}) == ""
