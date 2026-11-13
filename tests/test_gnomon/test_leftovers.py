"""The values that a started record still holds from its template.

Every command reads a started record without them, and the check reports each one with its repair:
fill it or delete it. A placeholder is recognized by equality with a string of a template, so a
symbol in capitals stays content.
"""

from __future__ import annotations

from pathlib import Path

from gnomon.answerability import diagnose
from gnomon.check import check_workspace, load_workspace
from gnomon.leftovers import placeholder_values, strip_leftovers
from gnomon.scaffold import CORE_KINDS, scaffold
from gnomon.vocabulary import load_problem


def test_the_placeholders_are_the_uppercase_strings_of_the_templates() -> None:
    values = placeholder_values()
    assert {"SYMBOL", "RECORD.ID", "FIELD.PATH", "quest.TOPIC.NAME"} <= values
    assert not {"provisional", "pending", "open", "DGMT"} & values


def test_an_untouched_block_is_removed_and_reported_once() -> None:
    record = {
        "type": "question",
        "id": "quest.flu.winter-timing",
        "construction": {"procedure": '"THE PROCEDURE"', "reading": None},
    }
    cleaned, found = strip_leftovers({**record, "maturity": {"FIELD.PATH": "open"}})
    assert "maturity" not in cleaned
    assert [f.text for f in found][-1] == (
        "maturity: is the template block left untouched; fill it or delete it"
    )


def test_a_placeholder_in_a_filled_entry_becomes_empty() -> None:
    record = {
        "type": "model",
        "id": "mod.flu.humidity",
        "laws": [
            {
                "name": "survival",
                "symbol": "survival",
                "expression": "EXPRESSION OVER DECLARED SYMBOLS",
            }
        ],
        "variables": [{"symbol": "DGMT", "name": "SYMBOL"}],
    }
    cleaned, found = strip_leftovers(record)
    assert cleaned["laws"][0]["expression"] is None and cleaned["variables"][0]["symbol"] == "DGMT"
    assert [f.text.split(":")[0] for f in found] == [
        "laws[0].expression",
        "variables[0].name",
    ]


def _started(tmp_path: Path) -> Path:
    """Return a new folder whose problem and question carry an identifier and nothing else."""
    folder = tmp_path / "flu"
    scaffold(folder, [*CORE_KINDS, "question"])
    for name, placeholder, ident in (
        ("problem.yml", "prob.TOPIC.NAME", "prob.flu.winter-peak"),
        ("question.yml", "quest.TOPIC.NAME", "quest.flu.winter-timing"),
    ):
        path = folder / name
        path.write_text(
            path.read_text(encoding="utf-8").replace(f"id: {placeholder}", f"id: {ident}", 1),
            encoding="utf-8",
        )
    return folder


def test_a_leftover_is_reported_instead_of_being_read_as_content(
    tmp_path: Path,
) -> None:
    _started(tmp_path)
    rules = [x.finding.rule.id for x in check_workspace(load_workspace(tmp_path))]
    assert "completeness/template-leftover" in rules
    assert not {
        "vocabulary/unparsed-expression",
        "completeness/misplaced-maturity",
    } & set(rules)


def test_an_untouched_block_opens_no_route(tmp_path: Path) -> None:
    _started(tmp_path)
    workspace = load_workspace(tmp_path)
    routes = {r.route for q in diagnose(workspace.by_id).questions for r in q.routes}
    assert routes == {"selection"}


def test_the_vocabulary_reads_neither_templates_nor_leftovers(tmp_path: Path) -> None:
    folder = _started(tmp_path)
    problem = load_problem(folder)
    assert not problem.declarations and problem.name == "flu"
