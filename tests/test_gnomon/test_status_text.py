"""The text of `gnomon status` and the messages of the itinerary, written for a researcher.

Each open condition lists its ready acts apart from the acts waiting for an input, the condition of
candidates says why it stays open, and the command says so when it finds no question. A step named
without its itinerary is reported with its full form.
"""

from __future__ import annotations

import shutil
from pathlib import Path

from typer.testing import CliRunner

from gnomon.answerability import ACTIVITY_NOTES, PRODUCT_TYPE_NOTE, diagnose, render_text
from gnomon.check import load_workspace
from gnomon.cli import app

from .paths import EXAMPLES, ROOT

CASE = "grokking-delayed-generalization"


def test_no_question_is_said_rather_than_printing_nothing() -> None:
    assert render_text(diagnose({})).startswith("no question to diagnose")


def test_an_open_condition_lists_its_ready_acts_apart_and_the_choice_is_left_open() -> None:
    text = render_text(diagnose(load_workspace(EXAMPLES / CASE).by_id))
    assert "  open definiteness\n    ready: explication" in text
    assert "    waiting for an input: operationalization (concept)" in text
    assert "open candidates: 1 answer recorded, none yet passes the admissibility tests" in text
    assert "as docs/procedures/inquiry/next-act.md states\n" in text


def test_the_activities_and_the_input_types_named_are_pointed_to_their_definitions() -> None:
    """The status names activities and product types without defining them, so its last line
    names the notes that define them, and both notes exist."""
    text = render_text(diagnose(load_workspace(EXAMPLES / CASE).by_id))
    last = text.rstrip().splitlines()[-1]
    assert last.startswith("each activity is defined in the note of its family")
    assert ACTIVITY_NOTES in last and PRODUCT_TYPE_NOTE in last
    assert (ROOT / ACTIVITY_NOTES).is_file() and (ROOT / PRODUCT_TYPE_NOTE).is_file()


def test_a_step_named_without_its_itinerary_is_given_in_full(tmp_path: Path) -> None:
    folder = tmp_path / CASE
    shutil.copytree(EXAMPLES / CASE, folder)
    path = folder / "itinerary.yml"
    text = path.read_text(encoding="utf-8")
    path.write_text(text.replace("ref: itin.grokking.explain-delay.pose", "ref: pose", 1))
    result = CliRunner().invoke(app, ["itinerary", str(folder)])
    assert "pose names a step of this itinerary without its itinerary; write it in full, as" in (
        result.output
    )
    assert "itin.grokking.explain-delay.pose" in result.output
