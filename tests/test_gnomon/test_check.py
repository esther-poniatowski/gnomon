"""The commands that check a user's directory and scaffold a problem.

``gnomon check`` runs every check of the package on a directory tree, so it must stay silent on the
worked inquiries and report each defect planted in a copy of one of them. ``gnomon init`` writes the
templates in the order of filling and never overwrites a filled record.
"""

from __future__ import annotations

import shutil
from pathlib import Path

import pytest
import yaml
from typer.testing import CliRunner

from gnomon import check as check_module
from gnomon.check import check_workspace, load_workspace
from gnomon.cli import app
from gnomon.report import render_markdown_report, render_yaml_report
from gnomon.scaffold import CORE_KINDS, scaffold, template_entries

from .paths import EXAMPLES

CASE = "grokking-delayed-generalization"

#: Each defect planted in a copy of the grokking inquiry: the file, the text replaced, its
#: replacement, and the rule that must report it.
PLANTED = [
    ("answer.yml", 'holds: "0 < lambda3 * eta_rep"', 'holds: "0 < lambda3 * eta_zzz"', "vocabulary/unresolved"),
    ("answer.yml", "pair: bind.grokking.effective-representation.decoder-limit",
     "pair: bind.grokking.effective-representation.delay-scale", "completeness/mismatched-status-pair"),
    ("answer.yml", "record: mod.grokking.effective-representation.representation_flow",
     "record: mod.grokking.effective-representation.no_such_law", "vocabulary/unknown-unit"),
    ("assessment.yml", "assesses: ans.grokking.slow-structured-representation",
     "assesses: ans.grokking.missing-answer", "vocabulary/unknown-record"),
    ("answer.yml", "modal_strength: actual", "modal_strength: certain", "completeness/inadmissible-value"),
    ("binding.yml", "grain: qualitative", "grain:", "completeness/unmet-requirement"),
]


@pytest.fixture()
def planted(tmp_path: Path) -> Path:
    """Return a workspace holding a copy of the grokking inquiry with the planted defects."""
    folder = tmp_path / CASE
    shutil.copytree(EXAMPLES / CASE, folder)
    for name, old, new, _ in PLANTED:
        path = folder / name
        text = path.read_text(encoding="utf-8")
        assert old in text, f"{name}: the text to replace is absent: {old}"
        path.write_text(text.replace(old, new, 1), encoding="utf-8")
    return tmp_path


def test_the_worked_inquiries_pass_every_check() -> None:
    workspace = load_workspace(EXAMPLES)
    assert workspace.problems and not workspace.failures
    found = check_workspace(workspace)
    assert not found, [f"{x.file}: {x.finding.text}" for x in found]


def test_every_planted_defect_is_reported(planted: Path) -> None:
    rules = {x.finding.rule.id for x in check_workspace(load_workspace(planted))}
    missing = [rule for *_, rule in PLANTED if rule not in rules]
    assert not missing, f"not reported: {missing}"


def test_a_check_that_fails_is_reported_and_the_others_still_run(planted: Path, monkeypatch) -> None:
    def broken(record, ctx):
        raise RuntimeError("planted")

    monkeypatch.setitem(check_module.BY_KIND, "binding", (broken,))
    found = check_workspace(load_workspace(planted))
    assert any(x.finding.rule.id == "check/failed" and x.record.startswith("bind.") for x in found)
    assert any(x.finding.rule.id == "vocabulary/unresolved" for x in found)


def test_an_unreadable_file_is_reported_and_skipped(tmp_path: Path) -> None:
    (tmp_path / "broken.yml").write_text("a: [unclosed", encoding="utf-8")
    workspace = load_workspace(tmp_path)
    assert len(workspace.failures) == 1 and not workspace.problems


def test_the_reports_are_stable_and_link_each_file(planted: Path, tmp_path: Path) -> None:
    found = check_workspace(load_workspace(planted))
    first = render_yaml_report(found, "plant", 11)
    assert first == render_yaml_report(list(reversed(found)), "plant", 11)
    document = yaml.safe_load(first)
    assert document["findings"] == len(found) and document["files"][0]["file"].startswith(CASE)
    page = render_markdown_report(found, "plant", 11, planted, planted / "reports")
    assert f"](../{CASE}/answer.yml)" in page


def test_the_scaffold_writes_the_templates_in_the_order_of_filling(tmp_path: Path) -> None:
    folder = tmp_path / "my-problem"
    written = scaffold(folder, [*CORE_KINDS, "answer"])
    order = list(template_entries())
    names = [p.stem for p in written if p.suffix == ".yml"]
    assert names == sorted(names, key=order.index) and set(names) == {*CORE_KINDS, "answer"}
    index = (folder / "_index.md").read_text(encoding="utf-8")
    assert index.index("(problem.yml)") < index.index("(question.yml)") < index.index("(answer.yml)")


def test_the_scaffold_never_overwrites_a_record_unless_forced(tmp_path: Path) -> None:
    folder = tmp_path / "my-problem"
    scaffold(folder, CORE_KINDS)
    (folder / "question.yml").write_text("filled\n", encoding="utf-8")
    with pytest.raises(FileExistsError):
        scaffold(folder, CORE_KINDS)
    assert (folder / "question.yml").read_text(encoding="utf-8") == "filled\n"
    with pytest.raises(ValueError):
        scaffold(tmp_path / "other", ["nonsense"])


def test_the_commands_exit_with_the_status_of_their_findings(planted: Path, tmp_path: Path) -> None:
    runner = CliRunner()
    assert runner.invoke(app, ["check", str(EXAMPLES)]).exit_code == 0
    result = runner.invoke(app, ["check", str(planted), "--format", "yaml", "--output", str(tmp_path / "r.yml")])
    assert result.exit_code == 1 and (tmp_path / "r.yml").is_file()
    assert runner.invoke(app, ["init", str(tmp_path / "new")]).exit_code == 0
    assert runner.invoke(app, ["init", str(tmp_path / "new")]).exit_code == 1
