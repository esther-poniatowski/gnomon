"""The form of record identifiers: the prefix of each type, lowercase segments joined by hyphens,
and the topic shared by the records of one problem.

The contract of each type carries the pattern of its identifiers, so a form rejects a malformed
identifier as the check does. A template not yet started keeps its placeholder identifier, and
both commands set it apart. Each rule is shown on a planted case in a copy of a worked inquiry.
"""

from __future__ import annotations

import shutil
from pathlib import Path

from typer.testing import CliRunner

from gnomon.check import check_workspace, load_workspace
from gnomon.cli import app
from gnomon.scaffold import CORE_KINDS, scaffold
from gnomon.schemas import identifier_prefixes, record_errors

from .paths import EXAMPLES

CASE = "grokking-delayed-generalization"


def _rules(tmp_path: Path, name: str, old: str, new: str) -> set[str]:
    """Return the rules reported on a copy of the grokking inquiry with one planted change."""
    folder = tmp_path / CASE
    shutil.copytree(EXAMPLES / CASE, folder)
    path = folder / name
    text = path.read_text(encoding="utf-8")
    assert old in text, f"{name}: the text to replace is absent: {old}"
    path.write_text(text.replace(old, new, 1), encoding="utf-8")
    return {located.finding.rule.id for located in check_workspace(load_workspace(tmp_path))}


def test_every_record_type_declares_the_prefix_of_its_identifiers() -> None:
    prefixes = identifier_prefixes()
    assert prefixes["target-system"] == "system" and prefixes["operators"] == "ops"
    assert len(set(prefixes.values())) == len(prefixes)


def test_the_contract_rejects_an_identifier_outside_the_grammar() -> None:
    record = {"_schema": "gnomon:question@1", "type": "question", "id": "quest.delay.explain_delay"}
    errors = record_errors(record)
    assert len(errors) == 1 and errors[0].startswith(
        "id: 'quest.delay.explain_delay' does not match"
    )
    record["id"] = "quest.delay.explain-delay"
    assert not record_errors(record)


def test_an_underscore_in_a_segment_is_reported(tmp_path: Path) -> None:
    rules = _rules(
        tmp_path,
        "derivation.yml",
        "id: derivation.grokking.delay-scale",
        "id: derivation.grokking.delay_scale",
    )
    assert "vocabulary/malformed-identifier" in rules


def test_a_record_of_another_topic_is_reported(tmp_path: Path) -> None:
    rules = _rules(
        tmp_path,
        "derivation.yml",
        "id: derivation.grokking.delay-scale",
        "id: derivation.delays.delay-scale",
    )
    assert "vocabulary/foreign-topic" in rules


def test_a_background_takes_the_topic_of_its_target(tmp_path: Path) -> None:
    rules = _rules(
        tmp_path,
        "background.yml",
        "id: bg.delayed-generalization-networks.training-specification",
        "id: bg.grokking.training-specification",
    )
    assert "vocabulary/foreign-topic" in rules


def test_validate_sets_apart_the_templates_not_yet_started(tmp_path: Path) -> None:
    scaffold(tmp_path / "new", CORE_KINDS)
    result = CliRunner().invoke(app, ["validate", str(tmp_path / "new")])
    assert result.exit_code == 0
    assert f"0 records checked, 0 errors found, {len(CORE_KINDS)} templates not yet filled" in (
        result.output
    )
