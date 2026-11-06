"""The findings of level warning: reported, marked as warnings, and failing no check.

The domain of an answer is never required. Its absence is a warning when the route makes it
meaningful: a deductive route, which implies it from the grounds, or a route on a model, which
bounds it by the domain of comparison of the binding.
"""

from __future__ import annotations

import shutil
from pathlib import Path

from typer.testing import CliRunner

from gnomon.cli import app
from gnomon.completeness import unstated_domain

from .paths import EXAMPLES

CASE = "grokking-delayed-generalization"


def test_a_domain_is_expected_on_a_deductive_route_or_a_route_on_a_model() -> None:
    records = {"mod.a.b": {"type": "model"}}
    assert unstated_domain({"route": {"kind": "proof", "runs_on": ["system.a"]}}, records)
    assert unstated_domain({"route": {"kind": "simulation", "runs_on": ["mod.a.b"]}}, records)
    assert not unstated_domain({"route": {"kind": "measurement", "runs_on": ["system.a"]}}, records)
    assert not unstated_domain(
        {"domain": "x > 0", "route": {"kind": "proof", "runs_on": ["system.a"]}}, records
    )


def test_a_warning_is_marked_and_fails_no_check(tmp_path: Path) -> None:
    folder = tmp_path / CASE
    shutil.copytree(EXAMPLES / CASE, folder)
    path = folder / "answer.yml"
    lines = path.read_text(encoding="utf-8").splitlines(keepends=True)
    start = next(i for i, line in enumerate(lines) if line.startswith("domain:"))
    end = next(i for i in range(start + 1, len(lines)) if lines[i][:1] not in (" ", ""))
    path.write_text("".join(lines[:start] + lines[end:]), encoding="utf-8")
    result = CliRunner().invoke(app, ["check", str(tmp_path)])
    assert result.exit_code == 0, result.output
    assert "warning: completeness/unstated-domain: domain: not stated" in result.output
    assert "0 findings, 1 warnings," in result.output
