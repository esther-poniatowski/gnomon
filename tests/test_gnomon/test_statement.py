"""The statement of a question composed from its fields in the statement frame.

The aim selects the interrogative and the locus the connective of contrast; a slot left unfilled
enters as its letter in brackets, so that no slot is filled from outside the fields.
"""

from __future__ import annotations

import doctest
from typing import Any

import yaml

import gnomon.statement
from gnomon.schemas import vocabulary_options
from gnomon.statement import compose_statement, load_statement_registry

from .paths import EXAMPLES

RECORDS: dict[str, dict[str, Any]] = {
    "system.a": {"title": "Wide networks", "variables": [{"name": "learning rate", "symbol": "eta"}]},
    "phen.a.b": {"title": "Lazy training"},
}


def question(**task: Any) -> dict[str, Any]:
    return {"subject": {"target_system": "system.a", "phenomenon": "phen.a.b", "contrast": {"locus": "none"}},
            "task": task}


def test_the_registry_covers_each_aim_locus_and_kind_of_restriction() -> None:
    registry, options = load_statement_registry(), vocabulary_options("question")
    for key, field in (("interrogatives", "task.epistemic_aim"), ("contrasts", "subject.locus"),
                       ("restriction_kinds", "subject.restriction")):
        assert set(registry[key]) == {value for value, _ in options[field]}, key


def test_the_worked_explanation_composes_its_subject_domain_and_foils() -> None:
    records = {}
    for path in (EXAMPLES / "grokking-delayed-generalization").glob("*.yml"):
        record = yaml.safe_load(path.read_text(encoding="utf-8"))
        records[record["id"]] = record
    composed = compose_statement(records["quest.grokking.explain_delay"], records)
    assert composed.text == (
        "In finite neural networks and their training under algorithmic supervised task and overparameterized"
        " architecture, what explains delayed generalization rather than immediate generalization or persistent"
        " memorization?"
    )
    assert composed.gaps == ()


def test_a_question_without_contrast_drops_the_last_clause() -> None:
    assert compose_statement(question(epistemic_aim="prediction"), RECORDS).text == (
        "In wide networks, what will lazy training be?")


def test_the_locus_selects_the_connective_and_default_foils_fill_an_empty_set() -> None:
    record = question(epistemic_aim="explanation")
    record["subject"]["contrast"] = {"locus": "other-condition", "foil_set": [{"name": "small learning rate"}]}
    assert compose_statement(record, RECORDS).text.endswith("rather than under small learning rate?")
    record["subject"]["contrast"] = {"locus": "other-outcome", "foil_set": []}
    assert compose_statement(record, RECORDS).text.endswith("rather than the other values of the explanandum variable?")


def test_an_explication_puts_its_explicandum_in_place_of_the_phenomenon() -> None:
    record = question(epistemic_aim="explication", explicandum="laziness")
    assert compose_statement(record, RECORDS).text == "In wide networks, which criterion should define laziness?"
    del record["task"]["explicandum"]
    assert compose_statement(record, RECORDS).gaps == ("E",)


def test_an_unfilled_slot_is_bracketed_and_a_placeholder_shows_its_description() -> None:
    composed = compose_statement({"subject": {"phenomenon": {"placeholder": "phenomenon", "description": "a delay"}}}, {})
    assert composed.text == "In [S], [interrogative] [a delay] rather than [X]?"
    assert composed.gaps == ("S", "aim", "X")


def test_a_restriction_named_by_its_quantity_reads_its_kind_and_the_declared_name() -> None:
    record = question(epistemic_aim="description")
    record["subject"]["domain"] = {"restrictions": [{"of": "system.a.eta", "restriction": "clamped", "values": "{0.1}"}],
                                   "limit": {"expression": "width -> infinity"}}
    assert compose_statement(record, RECORDS).text == (
        "In wide networks under clamped learning rate, in the limit width -> infinity,"
        " what structure characterizes lazy training?")


def test_the_examples_of_the_module_hold() -> None:
    assert doctest.testmod(gnomon.statement).failed == 0
