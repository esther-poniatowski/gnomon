"""
The field index of the records: every field of every record type, by its path, with its title, its
description and the row of the specification note that documents it.

The fields, their titles and their descriptions are read from the base schemas, and the row that
documents a field is found by the association of :mod:`gnomon.specnotes`. A field of a list entry,
or a nested field without a row of its own, takes the row of its nearest documented parent. A field
that identifies the record rather than specifies the inquiry, such as ``id``, has no row. A table
row carries no anchor in Markdown, so an entry links to the note and names the row.

Functions
---------
index_fields
    Return the fields of each record type, with the row that documents each of them.
render_index
    Return the text of the field index.
field_index
    Return the path and the text of the field index, or None outside a checkout of the repository.
"""

from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Mapping

import yaml

from .schemas import kinds, load_base, render_template, vocabulary_options
from .specnotes import (
    DOCS,
    documented_fields,
    field_documentation,
    flatten,
)

#: The file of the field index, in the user guide.
INDEX_PATH = Path("guide") / "field-index.md"


@dataclass(frozen=True)
class Field:
    """One field of a record type, with the row of the note that documents it.

    Attributes
    ----------
    path : str
        The path of the field, ``[]`` marking the entries of a list.
    title : str
        The title that the base schema gives the field.
    description : str
        The description that the base schema gives the field.
    note : str or None
        The note that documents the field, relative to the folder of the documentation.
    row : str or None
        The name of the row that documents the field, or None for a note without a table row.
    """

    path: str
    title: str
    description: str
    note: str | None = None
    row: str | None = None


def _schema_fields(
    node: Mapping[str, Any], prefix: str = ""
) -> list[tuple[str, Mapping[str, Any]]]:
    """Return every field of a schema with its path, the entries of a list marked ``[]``."""
    found: list[tuple[str, Mapping[str, Any]]] = []
    for name, child in (node.get("properties") or {}).items():
        path = f"{prefix}.{name}" if prefix else str(name)
        found.append((path, child))
        found += _schema_fields(child, path)
        items = child.get("items")
        if isinstance(items, Mapping):
            found += _schema_fields(items, f"{path}[]")
    return found


def _documented(kind: str, paths: list[str], docs: Path) -> dict[str, tuple[str, str | None]]:
    """Return, per key path of a record type, the note and the row that document it."""
    return documented_fields(kind, paths, docs)


def _documentation(
    path: str, documented: Mapping[str, tuple[str, str | None]]
) -> tuple[str | None, str | None]:
    """Return the note and the row that document a field: its own, else those of its nearest
    documented parent, else the note of its first documented child, named by the part of its row
    before the colon, as "Tests" for the row "Tests: admissibility"."""
    return field_documentation(path, documented)


def index_fields(docs: Path = DOCS) -> dict[str, list[Field]]:
    """Return the fields of each record type, keyed by the type, each field with the row that
    documents it or that documents its nearest documented parent."""
    found: dict[str, list[Field]] = {}
    for kind in kinds():
        base, options = load_base(kind), vocabulary_options(kind)
        paths = flatten(yaml.safe_load(render_template(kind, base, options)))
        documented = _documented(kind, paths, docs)
        fields = []
        for path, node in _schema_fields(base):
            note, row = _documentation(path, documented)
            fields.append(
                Field(
                    path,
                    str(node.get("title") or ""),
                    str(node.get("description") or ""),
                    note,
                    row,
                )
            )
        found[kind] = sorted(fields, key=lambda field: field.path)
    return found


def _cell(text: str) -> str:
    """Return a text as one cell of a Markdown table."""
    return re.sub(r"\s+", " ", text).replace("|", "\\|").strip()


def _note_title(note: str, docs: Path) -> str:
    """Return the title of a note: its first heading of level one, or its file name."""
    for line in (docs / note).read_text(encoding="utf-8").splitlines():
        if line.startswith("# "):
            return line[2:].strip()
    return Path(note).stem


def _link(field: Field, docs: Path) -> str:
    """Return the link from the index to the note that documents a field, named by its row, or by
    the title of the note when no row documents it."""
    if field.note is None:
        return "—"
    name = field.row or _note_title(field.note, docs)
    return f"[{_cell(name)}](../{field.note})"


def render_index(fields: Mapping[str, list[Field]], docs: Path = DOCS) -> str:
    """Return the text of the field index, one table per record type, in alphabetical order."""
    lines = [
        "---",
        "tags:",
        "  - guide",
        'index: "[User guide](docs/guide/_index.md)"',
        "aliases:",
        "  - Field index",
        "---",
        "# Field index",
        "",
        "Looks up each field of each record by its path, with its title, its description and the"
        " row of the specification that documents it.",
        "",
        "> [!IMPORTANT] Generated file",
        "> `gnomon schemas` writes this index from the base schemas and the specification notes."
        " Edit a schema or a note, not this file. A path marks the entries of a list with `[]`,"
        " and a field without a row of its own links to the row of its parent.",
    ]
    for kind in sorted(fields):
        lines += [
            "",
            f"## `{kind}`",
            "",
            "| Path | Title | Description | Documented in |",
            "| ---- | ----- | ----------- | ------------- |",
        ]
        lines += [
            f"| `{field.path}` | {_cell(field.title)} | {_cell(field.description)} |"
            f" {_link(field, docs)} |"
            for field in fields[kind]
        ]
    return "\n".join(lines) + "\n"


def field_index(docs: Path = DOCS) -> tuple[Path, str] | None:
    """Return the path and the text of the field index, or None when the folder of the
    documentation is absent, as in an installed package."""
    if not docs.is_dir():
        return None
    return docs / INDEX_PATH, render_index(index_fields(docs), docs)
