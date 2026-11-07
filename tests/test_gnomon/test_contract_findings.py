"""The contract of each record, checked by `gnomon check` as by `gnomon validate`.

A violation is stated in words with its repair: a date written without quotes, a type, a key that
is no field. A violation that another rule reports, an unadmitted value or the form of an
identifier, is reported once, by that rule.
"""

from __future__ import annotations

import shutil
from pathlib import Path

from typer.testing import CliRunner

from gnomon.check import check_workspace, load_workspace
from gnomon.cli import app

from .paths import EXAMPLES

CASE = "grokking-delayed-generalization"


def _planted(tmp_path: Path, name: str, old: str, new: str) -> list[str]:
    """Return the findings, as rule and text, of a copy of the grokking inquiry with one change."""
    folder = tmp_path / CASE
    shutil.copytree(EXAMPLES / CASE, folder)
    path = folder / name
    text = path.read_text(encoding="utf-8")
    assert old in text, f"{name}: the text to replace is absent: {old}"
    path.write_text(text.replace(old, new, 1), encoding="utf-8")
    found = check_workspace(load_workspace(tmp_path))
    return [f"{x.finding.rule.id} {x.finding.text}" for x in found]


def test_a_date_without_quotes_is_reported_with_its_repair(tmp_path: Path) -> None:
    texts = _planted(tmp_path, "itinerary.yml", 'judged: "2026-10-27"', "judged: 2026-10-27")
    assert (
        "contract/violation steps[0].norm.judged: a date written without quotes; write it in"
        ' quotes, as "2026-10-27"'
    ) in texts


def test_a_key_that_is_no_field_is_reported(tmp_path: Path) -> None:
    texts = _planted(tmp_path, "problem.yml", "status: posed", "status: posed\nnotes: free")
    assert any(t.startswith("contract/violation (record): notes is no field here") for t in texts)


def test_an_unadmitted_value_is_reported_once(tmp_path: Path) -> None:
    texts = _planted(tmp_path, "problem.yml", "status: posed", "status: pending")
    assert [t.split(" ")[0] for t in texts] == ["completeness/inadmissible-value"]


def test_validate_reports_a_missing_path(tmp_path: Path) -> None:
    result = CliRunner().invoke(app, ["validate", str(tmp_path / "absent")])
    assert result.exit_code == 1 and "no such file or directory" in result.output
