"""
Reading a record at a revision of the repository that holds it.

The records keep no successive versions, and the history of the repository keeps every earlier
state, as the decision on versions states. A step of an itinerary that names a record ``as_of`` a
revision is therefore checked against the record read from that history. This module is the only
one that calls git, so the checks receive the reader as an argument and stay free of it.

Functions
---------
git_states
    Return a reader of the records of a workspace at a revision, backed by git.
"""

from __future__ import annotations

import subprocess
from pathlib import Path
from typing import Any, Callable, Mapping

import yaml

#: A reader of a record at a revision: it takes an identifier and a revision, and returns the
#: record at that revision, or None when the revision or the record cannot be read.
StateReader = Callable[[str, str], "Mapping[str, Any] | None"]


def _git(args: list[str], cwd: Path) -> str | None:
    """Return the standard output of a git command, or None when it fails."""
    try:
        done = subprocess.run(["git", *args], cwd=cwd, capture_output=True, text=True, check=False)
    except OSError:
        return None
    return done.stdout if done.returncode == 0 else None


def git_states(files: Mapping[str, Path]) -> StateReader:
    """Return a reader of the records of a workspace at a revision, backed by git.

    ``files`` maps each identifier to the file that holds its record in the working tree. The
    reader reads that file at the revision, so a record moved to another file since that revision
    cannot be read, and the reader returns None for it.
    """
    cache: dict[tuple[str, str], Mapping[str, Any] | None] = {}

    def read(ident: str, revision: str) -> Mapping[str, Any] | None:
        if (ident, revision) in cache:
            return cache[(ident, revision)]
        found: Mapping[str, Any] | None = None
        path = files.get(ident)
        if path is not None:
            folder = path.resolve().parent
            top = _git(["rev-parse", "--show-toplevel"], folder)
            if top is not None:
                relative = path.resolve().relative_to(Path(top.strip()).resolve()).as_posix()
                text = _git(["show", f"{revision}:{relative}"], folder)
                if text is not None:
                    try:
                        loaded = yaml.safe_load(text)
                    except yaml.YAMLError:
                        loaded = None
                    if isinstance(loaded, Mapping) and loaded.get("id") == ident:
                        found = loaded
        cache[(ident, revision)] = found
        return found

    return read
