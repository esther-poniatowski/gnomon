"""
Reading a record at a revision of the repository that holds it.

The history of the repository keeps every earlier state of a record, as the decision on versions
states. A step of an itinerary that names a record ``as_of`` a
revision is therefore checked against the record read from that history. This module is the only
one that calls git, so the checks receive the reader as an argument and stay free of it.

Contents
--------
GitStates
    Read the records of a workspace at a revision, and tell a revision absent from a shallow
    clone.
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


def _load(text: str | None, ident: str) -> Mapping[str, Any] | None:
    """Return the record that a file holds, when it parses and carries the identifier."""
    if text is None:
        return None
    try:
        loaded = yaml.safe_load(text)
    except yaml.YAMLError:
        return None
    return loaded if isinstance(loaded, Mapping) and loaded.get("id") == ident else None


class GitStates:
    """A reader of the records of a workspace at a revision of the repository, backed by git.

    ``files`` maps each identifier to the file that holds its record in the working tree. The
    reader first reads that file at the revision; when the file then held another record, or did
    not exist, it searches the revision for the file whose line ``id:`` names the identifier, so a
    record moved since the revision is still read.
    """

    def __init__(self, files: Mapping[str, Path]) -> None:
        self.files = files
        self.cache: dict[tuple[str, str], Mapping[str, Any] | None] = {}

    def _top(self, ident: str) -> Path | None:
        """Return the root of the repository that holds the file of a record."""
        path = self.files.get(ident)
        if path is None:
            return None
        top = _git(["rev-parse", "--show-toplevel"], path.resolve().parent)
        return Path(top.strip()).resolve() if top is not None else None

    def __call__(self, ident: str, revision: str) -> Mapping[str, Any] | None:
        if (ident, revision) not in self.cache:
            self.cache[(ident, revision)] = self._read(ident, revision)
        return self.cache[(ident, revision)]

    def _read(self, ident: str, revision: str) -> Mapping[str, Any] | None:
        """Read the record at its present path, then at the path that its identifier names."""
        top = self._top(ident)
        if top is None:
            return None
        relative = self.files[ident].resolve().relative_to(top).as_posix()
        found = _load(_git(["show", f"{revision}:{relative}"], top), ident)
        if found is not None:
            return found
        listed = _git(["grep", "-l", "-F", "-e", f"id: {ident}", revision], top) or ""
        for line in listed.splitlines():
            moved = line.split(":", 1)[1] if line.startswith(f"{revision}:") else line
            found = _load(_git(["show", f"{revision}:{moved}"], top), ident)
            if found is not None:
                return found
        return None

    def unavailable(self, ident: str, revision: str) -> bool:
        """Return whether a revision is absent from a clone that lacks the full history.

        A clone made at a limited depth holds no older commit, so a revision absent from it
        cannot be told from a wrong revision; the check then reports a warning, not an error.
        """
        top = self._top(ident)
        if top is None:
            return False
        shallow = (_git(["rev-parse", "--is-shallow-repository"], top) or "").strip() == "true"
        known = _git(["cat-file", "-e", f"{revision}^{{commit}}"], top) is not None
        return shallow and not known


def git_states(files: Mapping[str, Path]) -> GitStates:
    """Return a reader of the records of a workspace at a revision, backed by git."""
    return GitStates(files)
