"""The question tree generated from the records of a project."""

from __future__ import annotations

import doctest
from pathlib import Path
from typing import Any

import yaml
from typer.testing import CliRunner

import gnomon.views
from gnomon.cli import app
from gnomon.views import question_tree, render_tree

RECORDS: dict[str, dict[str, Any]] = {
    "prob.geometry.readout": {"type": "problem", "title": "Readout", "status": "posed"},
    "quest.geometry.capacity": {"type": "question", "addresses": "prob.geometry.readout", "status": "posed"},
    "quest.geometry.dimension": {
        "type": "question",
        "addresses": "prob.geometry.readout",
        "links": [{"question": "quest.geometry.capacity", "relation": "subquestion-of"}],
    },
    "quest.geometry.loose": {"type": "question"},
    "ans.geometry.kernel": {"type": "answer", "answers": "quest.geometry.capacity", "status": "entertained"},
    "assess.geometry.kernel": {"type": "assessment", "assesses": "ans.geometry.kernel"},
    "design.geometry.sweep": {"type": "design", "serves": "quest.geometry.capacity"},
    "design.geometry.method": {"type": "design", "serves": "prob.geometry.readout"},
}


def test_a_problem_governs_its_questions_and_a_question_its_subquestions_answers_and_designs() -> None:
    assert render_tree(question_tree(RECORDS)) == (
        "problem prob.geometry.readout: Readout [posed]\n"
        "  question quest.geometry.capacity [posed]\n"
        "    question quest.geometry.dimension\n"
        "    answer ans.geometry.kernel [entertained]\n"
        "      assessment assess.geometry.kernel\n"
        "    design design.geometry.sweep\n"
        "  design design.geometry.method\n"
        "question quest.geometry.loose\n"
    )


def test_a_subquestion_of_an_absent_question_forms_a_root() -> None:
    records = {"quest.a.b": {"type": "question",
                             "links": [{"question": "quest.a.absent", "relation": "subquestion-of"}]}}
    assert render_tree(question_tree(records)) == "question quest.a.b\n"


def test_questions_on_a_cycle_of_links_appear_once() -> None:
    records = {
        "quest.a.b": {"type": "question", "links": [{"question": "quest.a.c", "relation": "subquestion-of"}]},
        "quest.a.c": {"type": "question", "links": [{"question": "quest.a.b", "relation": "subquestion-of"}]},
    }
    text = render_tree(question_tree(records))
    assert text == "question quest.a.b\n  question quest.a.c\n"


def test_an_empty_project_yields_an_empty_tree() -> None:
    assert render_tree(question_tree({})) == ""


def test_the_command_prints_the_tree_of_a_directory_read_recursively(tmp_path: Path) -> None:
    (tmp_path / "sub").mkdir()
    for key, record in RECORDS.items():
        (tmp_path / "sub" / f"{key}.yml").write_text(yaml.safe_dump({"id": key, **record}), encoding="utf-8")
    result = CliRunner().invoke(app, ["tree", str(tmp_path)])
    assert result.exit_code == 0
    assert result.output == render_tree(question_tree(RECORDS))


def test_the_examples_of_the_module_hold() -> None:
    assert doctest.testmod(gnomon.views).failed == 0
