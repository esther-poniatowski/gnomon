"""The status of a question against the accepted answers to it.

A question is ``dissolved`` once an accepted corrective answer denies one of its presuppositions.
The status is shown unsupported on a defect planted in a copy of a worked inquiry, and the
unchanged inquiries report no such finding.
"""

from __future__ import annotations

import shutil
from pathlib import Path

from gnomon.check import check_workspace, load_workspace

from .paths import EXAMPLES

CASE = "neural-tangent-kernel-model-properties"


def _found(folder: Path) -> list[str]:
    return [f"{x.record} {x.finding.rule.id}" for x in check_workspace(load_workspace(folder))]


def test_a_question_marked_dissolved_without_a_corrective_answer_is_reported(
    tmp_path: Path,
) -> None:
    folder = tmp_path / CASE
    shutil.copytree(EXAMPLES / CASE, folder)
    path = folder / "question.yml"
    text = path.read_text(encoding="utf-8")
    assert "\nstatus: posed\n" in text
    path.write_text(text.replace("\nstatus: posed\n", "\nstatus: dissolved\n", 1), encoding="utf-8")
    assert "quest.ntk.linearized-dynamics-validity completeness/unsupported-dissolved" in _found(
        tmp_path
    )


def test_the_worked_inquiries_report_no_unsupported_dissolution() -> None:
    assert not [f for f in _found(EXAMPLES) if "dissolv" in f]
