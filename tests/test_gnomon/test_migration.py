"""Write-free planning of migrations from retained to current record contracts."""

from __future__ import annotations

import shutil
from pathlib import Path

import pytest
from typer.testing import CliRunner

from gnomon import migration
from gnomon.cli import app
from gnomon.migration import MigrationApplyError, apply_migration, plan_migration


def _write(path: Path, text: str) -> bytes:
    """Write one fixture and return its exact initial bytes."""
    path.write_text(text, encoding="utf-8")
    return path.read_bytes()


def test_safe_migration_changes_only_the_binding_in_the_preview(tmp_path: Path) -> None:
    """A safe proposal preserves comments and every value beside the binding."""
    path = tmp_path / "problem.yml"
    before = _write(
        path,
        "# authored comment\n_schema: 'gnomon:problem@1' # binding\n"
        "type: problem\nid: prob.topic.name\nstatus: posed\n",
    )

    plan = plan_migration(tmp_path)

    assert len(plan.changes) == 1
    assert not plan.blocked
    assert "-_schema: 'gnomon:problem@1' # binding" in plan.changes[0].diff
    assert "+_schema: gnomon:problem@3 # binding" in plan.changes[0].diff
    assert path.read_bytes() == before


def test_semantic_repair_is_blocked_instead_of_inferred(tmp_path: Path) -> None:
    """A narrowed vocabulary produces a blocking reason, not an invented replacement."""
    path = tmp_path / "problem.yml"
    before = _write(
        path,
        "_schema: gnomon:problem@1\ntype: problem\nid: prob.topic.name\nstatus: posed\n"
        "maturity:\n  statement: banana\n",
    )

    plan = plan_migration(tmp_path)

    assert not plan.changes
    assert len(plan.blocked) == 1
    assert plan.blocked[0].current == "gnomon:problem@3"
    assert any("banana is not admitted" in reason for reason in plan.blocked[0].reasons)
    assert path.read_bytes() == before


def test_current_records_generated_views_and_foreign_yaml_need_no_migration(
    tmp_path: Path,
) -> None:
    """The planner limits its scope to outdated authored Gnomon records."""
    current = _write(
        tmp_path / "problem.yml",
        "_schema: gnomon:problem@3\ntype: problem\nid: prob.topic.name\nstatus: posed\n",
    )
    generated = _write(
        tmp_path / "view.yml",
        "_schema: gnomon:view.problem-state@1\ntype: view\nid: view.problem-state\n",
    )
    foreign = _write(tmp_path / "other.yaml", "type: bibliography\nentries: []\n")

    plan = plan_migration(tmp_path)

    assert not plan.pending
    assert (tmp_path / "problem.yml").read_bytes() == current
    assert (tmp_path / "view.yml").read_bytes() == generated
    assert (tmp_path / "other.yaml").read_bytes() == foreign


def test_unknown_contract_missing_binding_and_malformed_yaml_are_reported(
    tmp_path: Path,
) -> None:
    """Every unreadable or unresolvable Gnomon record remains visible in the plan."""
    _write(
        tmp_path / "unknown.yml",
        "_schema: gnomon:problem@99\ntype: problem\nid: prob.topic.unknown\n",
    )
    _write(tmp_path / "missing.yml", "type: question\nid: quest.topic.missing\n")
    _write(tmp_path / "broken.yml", "type: [\n")

    plan = plan_migration(tmp_path)

    assert len(plan.blocked) == 2
    assert any("not a published" in reason for block in plan.blocked for reason in block.reasons)
    assert any("no _schema" in reason for block in plan.blocked for reason in block.reasons)
    assert len(plan.failures) == 1


def test_check_command_reports_diff_and_never_writes(tmp_path: Path) -> None:
    """Check mode reports a reviewable patch while preserving the complete directory tree."""
    path = tmp_path / "problem.yml"
    before = _write(
        path,
        "_schema: gnomon:problem@1\ntype: problem\nid: prob.topic.name\nstatus: posed\n",
    )
    initial_files = sorted(tmp_path.rglob("*"))

    result = CliRunner().invoke(app, ["migrate", str(tmp_path), "--check"])

    assert result.exit_code == 1
    assert "problem.yml: would update gnomon:problem@1 -> gnomon:problem@3" in result.output
    assert "--- problem.yml (current)" in result.output
    assert "1 migration proposed; 0 blocked; 0 unreadable; 0 files written" in result.output
    assert path.read_bytes() == before
    assert sorted(tmp_path.rglob("*")) == initial_files


def test_check_command_is_repeatable_and_current_workspace_succeeds(
    tmp_path: Path,
) -> None:
    """A current workspace yields the same clean result on every preview."""
    path = tmp_path / "problem.yml"
    before = _write(
        path,
        "_schema: gnomon:problem@3\ntype: problem\nid: prob.topic.name\nstatus: posed\n",
    )
    runner = CliRunner()

    first = runner.invoke(app, ["migrate", str(tmp_path), "--check"])
    second = runner.invoke(app, ["migrate", str(tmp_path), "--check"])

    assert first.exit_code == second.exit_code == 0
    assert first.output == second.output == "no migrations required; 0 files written\n"
    assert path.read_bytes() == before


def test_migrate_without_mode_refuses_to_select_a_write_route(tmp_path: Path) -> None:
    """The bare command exposes neither an implicit preview nor an implicit application."""
    result = CliRunner().invoke(app, ["migrate", str(tmp_path)])

    assert result.exit_code == 2
    assert "choose exactly one migration mode: --check or --apply" in result.output


def test_migrate_rejects_ambiguous_or_inapplicable_options(tmp_path: Path) -> None:
    """The CLI requires one explicit mode and limits automatic confirmation to application."""
    runner = CliRunner()

    ambiguous = runner.invoke(app, ["migrate", str(tmp_path), "--check", "--apply"])
    preview_yes = runner.invoke(app, ["migrate", str(tmp_path), "--check", "--yes"])

    assert ambiguous.exit_code == preview_yes.exit_code == 2
    assert "choose exactly one migration mode" in ambiguous.output
    assert "--yes requires the migration mode --apply" in preview_yes.output


def test_declining_application_preserves_the_complete_tree(tmp_path: Path) -> None:
    """A declined review writes neither a migrated record nor its recovery copy."""
    path = tmp_path / "problem.yml"
    before = _write(
        path,
        "_schema: gnomon:problem@1\ntype: problem\nid: prob.topic.name\nstatus: posed\n",
    )

    result = CliRunner().invoke(app, ["migrate", str(tmp_path), "--apply"], input="n\n")

    assert result.exit_code == 1
    assert "--- problem.yml (current)" in result.output
    assert "Preserve and migrate 1 authored records?" in result.output
    assert path.read_bytes() == before
    assert not (tmp_path / ".gnomon-backup").exists()


def test_confirmed_application_preserves_then_migrates_the_reviewed_bytes(
    tmp_path: Path,
) -> None:
    """Confirmation backs up exact source bytes before applying the displayed binding diff."""
    folder = tmp_path / "nested"
    folder.mkdir()
    path = folder / "problem.yml"
    before = _write(
        path,
        "# retained\n_schema: 'gnomon:problem@1' # binding\n"
        "type: problem\nid: prob.topic.name\nstatus: posed\n",
    )

    result = CliRunner().invoke(app, ["migrate", str(tmp_path), "--apply"], input="y\n")

    backup = (
        tmp_path / ".gnomon-backup" / "migrations" / "gnomon-problem-1" / "nested" / "problem.yml"
    )
    assert result.exit_code == 0, result.output
    assert result.output.index("--- nested/problem.yml (current)") < result.output.index(
        "Preserve and migrate 1 authored records?"
    )
    assert backup.read_bytes() == before
    assert path.read_bytes() == before.replace(b"'gnomon:problem@1'", b"gnomon:problem@3")
    assert f"{path}: preserved as {backup}" in result.output
    assert "1 file migrated" in result.output

    migrated = path.read_bytes()
    current_copy = tmp_path.parent / f"{tmp_path.name}-post-migration" / "nested" / "problem.yml"
    current_copy.parent.mkdir(parents=True)
    shutil.copyfile(path, current_copy)
    shutil.copyfile(backup, path)

    validation = CliRunner().invoke(app, ["validate", str(tmp_path)])
    preview = CliRunner().invoke(app, ["migrate", str(tmp_path), "--check"])

    assert path.read_bytes() == before
    assert validation.exit_code == 0, validation.output
    assert preview.exit_code == 1
    assert "1 migration proposed; 0 blocked; 0 unreadable; 0 files written" in preview.output
    shutil.copyfile(current_copy, path)
    assert path.read_bytes() == migrated


def test_yes_option_applies_the_reviewed_plan_without_a_prompt(tmp_path: Path) -> None:
    """Explicit automatic confirmation preserves the same review and backup guarantees."""
    path = tmp_path / "problem.yml"
    _write(
        path,
        "_schema: gnomon:problem@1\ntype: problem\nid: prob.topic.name\nstatus: posed\n",
    )

    result = CliRunner().invoke(app, ["migrate", str(tmp_path), "--apply", "--yes"])

    assert result.exit_code == 0, result.output
    assert "Preserve and migrate" not in result.output
    assert "_schema: gnomon:problem@3" in path.read_text(encoding="utf-8")


def test_one_blocked_record_prevents_every_planned_write(tmp_path: Path) -> None:
    """A semantic blocker keeps safe sibling migrations unapplied."""
    safe = tmp_path / "safe.yml"
    before = _write(
        safe,
        "_schema: gnomon:problem@1\ntype: problem\nid: prob.topic.safe\nstatus: posed\n",
    )
    _write(
        tmp_path / "blocked.yml",
        "_schema: gnomon:problem@1\ntype: problem\nid: prob.topic.blocked\n"
        "status: posed\nmaturity:\n  statement: banana\n",
    )

    result = CliRunner().invoke(app, ["migrate", str(tmp_path), "--apply", "--yes"])

    assert result.exit_code == 1
    assert "1 migration proposed; 1 blocked; 0 unreadable; 0 files written" in result.output
    assert safe.read_bytes() == before
    assert not (tmp_path / ".gnomon-backup").exists()


def test_application_rejects_a_source_changed_after_review(tmp_path: Path) -> None:
    """A concurrent source edit survives and no recovery copy is created from stale bytes."""
    path = tmp_path / "problem.yml"
    _write(
        path,
        "_schema: gnomon:problem@1\ntype: problem\nid: prob.topic.name\nstatus: posed\n",
    )
    plan = plan_migration(tmp_path)
    concurrent = b"concurrent authored content\n"
    path.write_bytes(concurrent)

    try:
        apply_migration(plan)
    except ValueError as error:
        assert "migration target changed after planning" in str(error)
    else:
        raise AssertionError("a stale migration plan was applied")

    assert path.read_bytes() == concurrent
    assert not (tmp_path / ".gnomon-backup").exists()


def test_application_refuses_to_replace_an_existing_recovery_copy(
    tmp_path: Path,
) -> None:
    """Reapplication cannot overwrite the exact prior state kept for recovery."""
    path = tmp_path / "problem.yml"
    before = _write(
        path,
        "_schema: gnomon:problem@1\ntype: problem\nid: prob.topic.name\nstatus: posed\n",
    )
    plan = plan_migration(tmp_path)
    backup = plan.changes[0].backup
    backup.parent.mkdir(parents=True)
    backup.write_bytes(b"existing recovery state\n")

    try:
        apply_migration(plan)
    except ValueError as error:
        assert "migration backup already exists" in str(error)
    else:
        raise AssertionError("an existing recovery copy was overwritten")

    assert path.read_bytes() == before
    assert backup.read_bytes() == b"existing recovery state\n"


def test_application_never_follows_a_record_symlink_outside_the_inquiry(
    tmp_path: Path,
) -> None:
    """A linked YAML path is reported and its external target remains unchanged."""
    inquiry = tmp_path / "inquiry"
    inquiry.mkdir()
    external = tmp_path / "external.yml"
    before = _write(
        external,
        "_schema: gnomon:problem@1\ntype: problem\nid: prob.topic.name\nstatus: posed\n",
    )
    (inquiry / "problem.yml").symlink_to(external)

    plan = plan_migration(inquiry)
    result = CliRunner().invoke(app, ["migrate", str(inquiry), "--apply", "--yes"])

    assert not plan.changes and len(plan.failures) == 1
    assert result.exit_code == 1
    assert "symbolic-link records are not migrated" in result.output
    assert external.read_bytes() == before
    assert not (inquiry / ".gnomon-backup").exists()


def test_duplicate_root_contract_fields_block_the_plan(tmp_path: Path) -> None:
    """An ambiguous binding cannot produce a successful but ineffective migration."""
    path = tmp_path / "problem.yml"
    before = _write(
        path,
        "_schema: gnomon:problem@1\n_schema: gnomon:problem@1\n"
        "type: problem\nid: prob.topic.name\nstatus: posed\n",
    )

    plan = plan_migration(tmp_path)
    result = CliRunner().invoke(app, ["migrate", str(tmp_path), "--apply", "--yes"])

    assert not plan.changes and len(plan.blocked) == 1
    assert any("multiple root _schema fields" in reason for reason in plan.blocked[0].reasons)
    assert result.exit_code == 1
    assert "multiple root _schema fields" in result.output
    assert path.read_bytes() == before
    assert not (tmp_path / ".gnomon-backup").exists()


def test_application_rejects_a_source_replaced_by_a_symlink_after_review(
    tmp_path: Path,
) -> None:
    """The write boundary does not follow a new link whose target has reviewed bytes."""
    path = tmp_path / "problem.yml"
    before = _write(
        path,
        "_schema: gnomon:problem@1\ntype: problem\nid: prob.topic.name\nstatus: posed\n",
    )
    plan = plan_migration(tmp_path)
    external = tmp_path / "external.yml"
    external.write_bytes(before)
    path.unlink()
    path.symlink_to(external)

    with pytest.raises(MigrationApplyError, match="cannot open migration target") as caught:
        apply_migration(plan)

    assert not caught.value.backups and not caught.value.changed
    assert external.read_bytes() == before
    assert path.is_symlink()
    assert not (tmp_path / ".gnomon-backup").exists()


def test_application_rejects_a_symlinked_backup_directory(tmp_path: Path) -> None:
    """Recovery files cannot be redirected outside the inquiry through a linked parent."""
    path = tmp_path / "problem.yml"
    before = _write(
        path,
        "_schema: gnomon:problem@1\ntype: problem\nid: prob.topic.name\nstatus: posed\n",
    )
    plan = plan_migration(tmp_path)
    external = tmp_path / "external-backups"
    external.mkdir()
    (tmp_path / ".gnomon-backup").symlink_to(external, target_is_directory=True)

    with pytest.raises(MigrationApplyError, match="backup directory is a symbolic link") as caught:
        apply_migration(plan)

    assert not caught.value.backups and not caught.value.changed
    assert path.read_bytes() == before
    assert not list(external.iterdir())


def test_partial_write_failure_reports_every_backup_and_completed_change(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    """A later write failure exposes the exact recovery paths and partial state."""
    first = tmp_path / "a.yml"
    second = tmp_path / "b.yml"
    first_before = _write(
        first,
        "_schema: gnomon:problem@1\ntype: problem\nid: prob.topic.a\nstatus: posed\n",
    )
    second_before = _write(
        second,
        "_schema: gnomon:problem@1\ntype: problem\nid: prob.topic.b\nstatus: posed\n",
    )
    original_writer = getattr(migration, "_write_change")  # noqa: B009
    calls = 0

    def fail_second_write(change: migration.MigrationChange) -> None:
        """Apply the first write and inject a failure before the second."""
        nonlocal calls
        calls += 1
        if calls == 2:
            raise OSError("injected second-write failure")
        original_writer(change)

    monkeypatch.setattr(migration, "_write_change", fail_second_write)

    result = CliRunner().invoke(app, ["migrate", str(tmp_path), "--apply", "--yes"])

    backup_root = tmp_path / ".gnomon-backup" / "migrations" / "gnomon-problem-1"
    assert result.exit_code == 1
    assert (backup_root / "a.yml").read_bytes() == first_before
    assert (backup_root / "b.yml").read_bytes() == second_before
    assert b"gnomon:problem@3" in first.read_bytes()
    assert second.read_bytes() == second_before
    assert f"{first}: migrated before failure" in result.output
    assert "migration stopped after 1 completed writes; 2 recovery files available" in result.output

    shutil.copyfile(backup_root / "a.yml", first)
    shutil.copyfile(backup_root / "b.yml", second)
    assert first.read_bytes() == first_before
    assert second.read_bytes() == second_before
