"""Reading a record at a revision of a git repository.

A record moved to another file since the revision is still read, by the identifier that its file
states. A revision absent from a clone that lacks the full history is told apart from a wrong
revision, so that the check of an itinerary reports a warning, not an error.
"""

from __future__ import annotations

import subprocess
from pathlib import Path

from gnomon.history import git_states
from gnomon.itineraries import itinerary_problems

RECORD = "_schema: gnomon:model@1\nid: mod.a.m\ntype: model\n"


def _git(*args: str, cwd: Path) -> str:
    done = subprocess.run(["git", *args], cwd=cwd, capture_output=True, text=True, check=True)
    return done.stdout.strip()


def _repository(root: Path) -> tuple[str, Path]:
    """Return the first revision of a repository whose record then moves, and its new path."""
    root.mkdir()
    _git("init", "-q", cwd=root)
    _git("config", "user.email", "test@example.org", cwd=root)
    _git("config", "user.name", "Test", cwd=root)
    (root / "old").mkdir()
    (root / "old" / "model.yml").write_text(RECORD, encoding="utf-8")
    _git("add", ".", cwd=root)
    _git("commit", "-q", "-m", "first", cwd=root)
    first = _git("rev-parse", "HEAD", cwd=root)
    (root / "new").mkdir()
    _git("mv", "old/model.yml", "new/model.yml", cwd=root)
    _git("commit", "-q", "-m", "move", cwd=root)
    return first, root / "new" / "model.yml"


def test_a_record_moved_since_the_revision_is_read_by_its_identifier(tmp_path: Path) -> None:
    first, path = _repository(tmp_path / "repo")
    read = git_states({"mod.a.m": path})
    assert (read("mod.a.m", first) or {}).get("id") == "mod.a.m"
    assert read("mod.a.m", "no-such-revision") is None


def test_a_revision_absent_from_a_shallow_clone_is_a_warning(tmp_path: Path) -> None:
    first, _ = _repository(tmp_path / "repo")
    clone = tmp_path / "clone"
    _git("clone", "-q", "--depth", "1", f"file://{tmp_path / 'repo'}", str(clone), cwd=tmp_path)
    read = git_states({"mod.a.m": clone / "new" / "model.yml"})
    assert read("mod.a.m", first) is None
    assert read.unavailable("mod.a.m", first)
    assert not read.unavailable("mod.a.m", "HEAD")
    step = {
        "id": "derive",
        "activity": "derivation",
        "inputs": [{"type": "model", "ref": "mod.a.m", "as_of": first}],
        "output": {"type": "model"},
        "norm": {"test": "norm.derivation", "verdict": "pending"},
    }
    itinerary = {"id": "itin.a.i", "type": "itinerary", "steps": [step]}
    found = itinerary_problems(itinerary, {"mod.a.m": {"type": "model"}}, states=read)
    rules = {f.rule.id for f in found}
    assert "itinerary/unavailable-history" in rules
    assert "itinerary/unreadable-state" not in rules
