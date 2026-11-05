"""
Every file that ``gnomon schemas`` generates: the contracts and the templates of the record types,
and, in a checkout of the repository, the field index of the user guide.

Functions
---------
generated_files
    Return every generated file with its content.
stale_files
    Return every generated file whose content differs from its generated form.
"""

from __future__ import annotations

from pathlib import Path

from .fieldindex import field_index
from .schemas import schema_files


def generated_files() -> dict[Path, str]:
    """Return every generated file with its content."""
    files = schema_files()
    index = field_index()
    if index is not None:
        files[index[0]] = index[1]
    return files


def stale_files() -> list[Path]:
    """Return every generated file whose content differs from its generated form."""
    return [
        path
        for path, text in generated_files().items()
        if not path.is_file() or path.read_text(encoding="utf-8") != text
    ]
