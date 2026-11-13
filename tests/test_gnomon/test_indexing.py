"""Registration of records created outside the Gnomon initializer."""

from pathlib import Path

import pytest
from typer.testing import CliRunner

from gnomon.cli import app
from gnomon.indexing import apply_registration, plan_registration, register_record
from gnomon.scaffold import CORE_KINDS, scaffold, scaffold_text


def _inquiry(tmp_path: Path) -> Path:
    """Create the existing inquiry whose index each test protects."""
    folder = tmp_path / "inquiry"
    scaffold(folder, CORE_KINDS)
    index = folder / "_index.md"
    index.write_text(
        index.read_text(encoding="utf-8") + "\nAuthored note kept at the end.\n",
        encoding="utf-8",
    )
    return folder


def test_an_existing_record_joins_its_canonical_stage(tmp_path: Path) -> None:
    """A caller supplies only the record path; Gnomon supplies the entry and its order."""
    folder = _inquiry(tmp_path)
    record = folder / "research question.yaml"
    record.write_text(scaffold_text("question"), encoding="utf-8")

    result = register_record(record)

    assert result.kind == "question" and result.state == "updated"
    index = result.index.read_text(encoding="utf-8")
    assert "[Question](research%20question.yaml)" in index
    assert index.index("## 1. Problem") < index.index("## 2. Question schema")
    assert "Authored note kept at the end." in index


def test_registration_is_idempotent(tmp_path: Path) -> None:
    """A repeated post-creation call writes no duplicate index entry."""
    folder = _inquiry(tmp_path)
    record = folder / "question.yml"
    record.write_text(scaffold_text("question"), encoding="utf-8")

    first = register_record(record)
    first_bytes = first.index.read_bytes()
    second = register_record(record)

    assert second.state == "kept"
    assert second.index.read_bytes() == first_bytes
    assert first_bytes.count(b"](question.yml)") == 1


@pytest.mark.parametrize(
    ("content", "message"),
    [
        ("- not a mapping\n", "one YAML mapping"),
        ("_schema: other:record@1\n", "published Gnomon contract"),
        ("a: [unclosed\n", "not valid UTF-8 YAML"),
    ],
)
def test_registration_rejects_a_record_without_an_indexable_contract(
    tmp_path: Path, content: str, message: str
) -> None:
    """Malformed and foreign records leave the inquiry index byte-for-byte unchanged."""
    folder = _inquiry(tmp_path)
    record = folder / "record.yml"
    record.write_text(content, encoding="utf-8")
    index = folder / "_index.md"
    before = index.read_bytes()

    with pytest.raises(ValueError, match=message):
        register_record(record)

    assert index.read_bytes() == before


def test_registration_requires_an_existing_sibling_index(tmp_path: Path) -> None:
    """The command does not invent an inquiry around an isolated YAML record."""
    record = tmp_path / "question.yml"
    record.write_text(scaffold_text("question"), encoding="utf-8")

    with pytest.raises(ValueError, match="inquiry index does not exist"):
        register_record(record)


def test_a_concurrent_index_change_rejects_the_planned_write(tmp_path: Path) -> None:
    """An index edited after planning remains byte-for-byte unchanged."""
    folder = _inquiry(tmp_path)
    record = folder / "question.yml"
    record.write_text(scaffold_text("question"), encoding="utf-8")
    plan = plan_registration(record)
    plan.index.write_bytes(b"# Concurrent index\n")

    with pytest.raises(ValueError, match="index changed after registration was planned"):
        apply_registration(plan)

    assert plan.index.read_bytes() == b"# Concurrent index\n"


def test_register_command_reports_the_index_state(tmp_path: Path) -> None:
    """The command supplies a stable success line to a generic post-creation caller."""
    folder = _inquiry(tmp_path)
    record = folder / "question.yml"
    record.write_text(scaffold_text("question"), encoding="utf-8")

    result = CliRunner().invoke(app, ["register", str(record)])

    assert result.exit_code == 0
    assert result.stdout == f"{folder / '_index.md'}: updated\n"
