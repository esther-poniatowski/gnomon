"""
Creation of an inquiry folder, with sparse records in the order of filling.

The record contents are projected from the generated templates through the requirement registry.
Therefore, a sparse record contains the fields that identify it and the fields required at its
first operational stage, while optional branches remain absent. The complete generated template
remains available for source-based authoring. The template index supplies the record order and the
goal copied into the index of the new folder.

A scaffold never overwrites a filled record by default. In a folder that already holds records, it
writes only the missing templates and registers each of them in the existing index of the folder.
A forced scaffold first preserves every replaced file under ``.gnomon-backup``.

Constants
---------
STARTING_KINDS
    The templates created for each admitted starting record.
CORE_KINDS
    The kinds that open the default greenfield route.

Functions
---------
template_entries
    Return the entry of each template in the index of templates, in the order of that index.
register
    Return the text of an index with an entry for each kind that it does not list yet.
plan_scaffold
    Return the files and backups of a scaffold without writing them.
apply_scaffold
    Apply a plan whose observed target bytes remain current.
scaffold
    Write the missing templates of the given kinds into a folder, and register them in its index.
"""

from __future__ import annotations

import re
from collections.abc import Mapping, Sequence
from copy import deepcopy
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any
from urllib.parse import quote

import yaml

from .completeness.questions import SLOT_PLACEHOLDERS
from .completeness.requirements import (
    always_required,
    commitment_requirements,
    requirements_by_commitment,
    requirements_by_scope,
)
from .schemas import TEMPLATES

#: The starting record is the only difference between the two initialization routes.
STARTING_KINDS: dict[str, tuple[str, ...]] = {
    "problem": ("itinerary", "problem"),
    "question": ("itinerary", "question"),
}

#: The default greenfield route opens with an itinerary and problem record.
CORE_KINDS: tuple[str, ...] = STARTING_KINDS["problem"]

#: An entry of the index of templates: its link text, its file and the goal of the record.
ENTRY = re.compile(r"^(?:\d+\.|-) \[([^\]]+)\]\(([\w-]+)\.yml\): (.+)$")

# These fields designate every authored record before its domain requirements are filled.
DESIGNATION_FIELDS: tuple[str, ...] = ("title", "id", "type")


@dataclass(frozen=True)
class Entry:
    """The entry of one template in the index of templates.

    Attributes
    ----------
    title : str
        The title of the record kind.
    goal : str
        Why a researcher fills the record.
    stage : str
        The heading of the group that holds the entry: a stage of the order of specification.
    guidance : str
        The sentence that opens the group, empty when the group has none.
    """

    title: str
    goal: str
    stage: str
    guidance: str = ""


def template_entries(index: Path | None = None) -> dict[str, Entry]:
    """Return, per kind, the entry that the index of templates states, in its order.

    >>> entries = template_entries()
    >>> list(entries)[:3]
    ['itinerary', 'problem', 'question']
    """
    text = (index or TEMPLATES / "_index.md").read_text(encoding="utf-8")
    found: dict[str, Entry] = {}
    stage = guidance = ""
    for line in text.splitlines():
        if line.startswith("## "):
            stage, guidance = line[3:].strip(), ""
        elif (match := ENTRY.match(line)) is not None:
            found[match.group(2)] = Entry(match.group(1), match.group(3), stage, guidance)
        elif line.strip() and stage and not guidance:
            guidance = line.strip()
    return found


def _item(kind: str, entry: Entry, filename: str | None = None) -> str:
    """Return the line of the index of a folder that registers the template of one kind."""
    target = quote(filename or f"{kind}.yml", safe="._-/")
    return f"- [{entry.title}]({target}): {entry.goal}"


def _heading(entry: Entry) -> list[str]:
    """Return the lines that open the group of a stage, with its guidance when it has one."""
    return [f"## {entry.stage}", ""] + ([entry.guidance, ""] if entry.guidance else [])


def _index_text(name: str, kinds: Sequence[str], entries: dict[str, Entry]) -> str:
    """Return the index of a new folder, listing the templates of ``kinds`` stage by stage."""
    question_led = "question" in kinds and "problem" not in kinds
    ordered_kinds = list(kinds)
    if question_led:
        ordered_kinds = ["question", *(kind for kind in kinds if kind != "question")]
    lines = [
        f"# {name}",
        "",
        (
            "Fill the adopted question first. Then record subsequent acts in the itinerary, and "
            "run `gnomon check` after each addition."
            if question_led
            else "Fill the records stage by stage, and run `gnomon check` on this folder after "
            "each stage."
        ),
    ]
    stage = None
    for kind in ordered_kinds:
        entry = entries[kind]
        if entry.stage != stage:
            stage = entry.stage
            lines += ["", *_heading(entry)]
        lines.append(_item(kind, entry))
    return "\n".join(lines) + "\n"


def register_file(
    text: str,
    kind: str,
    filename: str,
    entries: dict[str, Entry] | None = None,
) -> str:
    """Return the index text with ``filename`` registered as one record of ``kind``.

    The entry joins the group of its stage. A missing stage is inserted before the first later
    stage, or at the end. Every other line remains unchanged.
    """
    entries = entries or template_entries()
    if kind not in entries:
        raise ValueError(f"no index entry is declared for the record kind {kind}")
    order = list(dict.fromkeys(entry.stage for entry in entries.values()))
    lines = text.splitlines()
    target = quote(filename, safe="._-/")
    item = _item(kind, entries[kind], filename)
    if any(f"]({target})" in line for line in lines):
        return text

    entry = entries[kind]
    headings = [(i, line[3:].strip()) for i, line in enumerate(lines) if line.startswith("## ")]
    own = next((i for i, stage in headings if stage == entry.stage), None)
    if own is not None:
        end = next((i for i, _ in headings if i > own), len(lines))
        while end > own + 1 and not lines[end - 1].strip():
            end -= 1
        lines.insert(end, item)
        return "\n".join(lines) + "\n"

    rank = order.index(entry.stage)
    later = next(
        (i for i, stage in headings if stage in order and order.index(stage) > rank),
        None,
    )
    if later is None:
        while lines and not lines[-1].strip():
            lines.pop()
        lines += ["", *_heading(entry), item]
    else:
        lines[later:later] = [*_heading(entry), item, ""]
    return "\n".join(lines) + "\n"


def register(text: str, kinds: Sequence[str], entries: dict[str, Entry] | None = None) -> str:
    r"""Return the text of an index with an entry for each kind that it does not list yet.

    Each entry uses the canonical template filename. The record-specific registration boundary
    calls :func:`register_file` with the filename selected by the researcher.

    >>> index = "# p\n\n## 1. Problem\n\n- [Problem](problem.yml): states the demand\n"
    >>> print(register(index, ["problem", "answer"]), end="")  # doctest: +ELLIPSIS
    # p
    <BLANKLINE>
    ## 1. Problem
    <BLANKLINE>
    - [Problem](problem.yml): states the demand
    <BLANKLINE>
    ## 5. ...
    ...
    - [Answer](answer.yml): ...
    """
    entries = entries or template_entries()
    for kind in kinds:
        text = register_file(text, kind, f"{kind}.yml", entries)
    return text


@dataclass(frozen=True)
class Scaffold:
    """The outcome of a scaffold.

    Attributes
    ----------
    written : list of Path
        The templates written.
    kept : list of Path
        The files that already existed and were left as they stand.
    index : Path
        The index of the folder.
    index_state : str
        ``written`` for a new or overwritten index, ``updated`` when entries were added to it, and
        ``kept`` when it already listed every kind.
    overwritten : list of Path
        Existing files replaced by a forced scaffold.
    backups : list of tuple of Path
        Each overwritten file and the backup that preserves its prior bytes.
    """

    written: list[Path]
    kept: list[Path]
    index: Path
    index_state: str
    overwritten: list[Path] = field(default_factory=list)
    backups: list[tuple[Path, Path]] = field(default_factory=list)


@dataclass(frozen=True)
# The plan binds each write category and its expected bytes as one immutable transaction.
# pylint: disable=too-many-instance-attributes
class ScaffoldPlan:
    """A scaffold write set computed without changing the filesystem."""

    written: list[Path]
    kept: list[Path]
    index: Path
    index_state: str
    overwritten: list[Path]
    backups: list[tuple[Path, Path]]
    _content: tuple[tuple[Path, str], ...] = field(repr=False)
    _expected: tuple[tuple[Path, bytes | None], ...] = field(repr=False)

    @property
    def affected(self) -> list[Path]:
        """Return every file that applying the plan will write."""
        index = [self.index] if self.index_state != "kept" else []
        return [*self.written, *index]


def _backup_path(folder: Path, source: Path) -> Path:
    """Return the deterministic backup path for one overwritten scaffold file."""
    return folder / ".gnomon-backup" / f"{source.name}.bak"


def _scaffold_paths(kind: str) -> tuple[str, ...]:
    """Return the canonical template paths shown when a record of ``kind`` is created.

    General requirements come from the requirement registry. A question is created at its typed
    stage, and a subject record is created at its identified commitment, so those two creation
    contexts contribute their declared paths. The order follows the template wherever the paths
    share a root; duplicates carry no second meaning.
    """
    paths = [*DESIGNATION_FIELDS, *always_required(kind)]
    if kind == "question":
        typed = requirements_by_scope()["question-typed"]
        paths += list((typed.get("required") or {}).get("question") or [])
        if typed.get("minimum_subject_slots") == "typed":
            paths += [
                f"subject.{slot}.{field}"
                for slot in SLOT_PLACEHOLDERS
                for field in ("placeholder", "description")
            ]
    if kind in {"target-system", "phenomenon"}:
        paths += commitment_requirements(kind, "identified", requirements_by_commitment())
    return tuple(dict.fromkeys(paths))


def _empty_collection(value: Any) -> Any:
    """Return an unfilled collection or a copy of one scalar template value."""
    if isinstance(value, Mapping):
        return {}
    if isinstance(value, list):
        return []
    return deepcopy(value)


def _project_path(target: dict[str, Any], template: Mapping[str, Any], path: str) -> None:
    """Project one dotted requirement path from ``template`` into ``target``.

    A path through list entries, such as ``moves[].kind``, creates the empty list itself. No
    placeholder entry is authored before the researcher adds an actual item.
    """
    head = path.partition("[].")[0]
    parts = head.split(".")
    source: Any = template
    destination = target
    for index, part in enumerate(parts):
        if not isinstance(source, Mapping) or part not in source:
            return
        value = source[part]
        if index == len(parts) - 1:
            destination.setdefault(part, _empty_collection(value))
            return
        if isinstance(value, list):
            destination.setdefault(part, [])
            return
        child = destination.setdefault(part, {})
        if not isinstance(child, dict):
            return
        destination = child
        source = value


def scaffold_text(kind: str, full_template: bool = False) -> str:
    """Return the initial YAML of ``kind``.

    The default is a sparse authored record whose optional branches are absent. When
    ``full_template`` is true, return the canonical commented template byte-for-byte.
    """
    source = (TEMPLATES / f"{kind}.yml").read_text(encoding="utf-8")
    if full_template:
        return source
    template = yaml.safe_load(source)
    if not isinstance(template, Mapping):
        raise TypeError(f"template for {kind} is not a YAML mapping")
    projected: dict[str, Any] = {"_schema": template["_schema"]}
    paths = _scaffold_paths(kind)
    for name in template:
        for path in paths:
            if path.partition("[].")[0].split(".", 1)[0] == name:
                _project_path(projected, template, path)
    if kind == "question":
        subject = projected.get("subject") or {}
        for slot, placeholder in SLOT_PLACEHOLDERS.items():
            value = subject.get(slot)
            if isinstance(value, dict):
                value["placeholder"] = placeholder
    return yaml.safe_dump(projected, sort_keys=False, allow_unicode=True, width=1000)


# Planning keeps paths, contents, prior bytes and backup pairs together before any write.
# pylint: disable=too-many-locals
def plan_scaffold(
    folder: Path,
    kinds: Sequence[str],
    force: bool = False,
    full_template: bool = False,
) -> ScaffoldPlan:
    """Return the write set for a scaffold without changing the filesystem.

    A forced plan assigns every existing target a deterministic backup. An existing backup makes
    the plan invalid, because replacing it would destroy the recoverable prior state.

    Raises
    ------
    ValueError
        If a kind has no template or a required backup already exists.
    """
    entries = template_entries()
    unknown = [kind for kind in kinds if kind not in entries]
    if unknown:
        raise ValueError(
            f"no template for the kinds {', '.join(unknown)}; the kinds are {', '.join(entries)}"
        )
    chosen = [kind for kind in entries if kind in set(kinds)]
    written: list[Path] = []
    kept: list[Path] = []
    overwritten: list[Path] = []
    backups: list[tuple[Path, Path]] = []
    content: list[tuple[Path, str]] = []
    expected: list[tuple[Path, bytes | None]] = []

    def schedule(path: Path, text: str) -> None:
        """Add one target and bind the plan to its current bytes."""
        previous = path.read_bytes() if path.exists() else None
        expected.append((path, previous))
        content.append((path, text))
        if previous is not None and force:
            overwritten.append(path)
            backups.append((path, _backup_path(folder, path)))

    for kind in chosen:
        path = folder / f"{kind}.yml"
        if path.exists() and not force:
            kept.append(path)
            continue
        schedule(path, scaffold_text(kind, full_template))
        written.append(path)

    index = folder / "_index.md"
    if force or not index.exists():
        schedule(index, _index_text(folder.name, chosen, entries))
        index_state = "written"
    else:
        text = index.read_text(encoding="utf-8")
        updated = register(text, chosen, entries)
        if updated == text:
            index_state = "kept"
        else:
            schedule(index, updated)
            index_state = "updated"

    collision = next(
        (backup for _, backup in backups if backup.exists() or backup.is_symlink()),
        None,
    )
    if collision is not None:
        raise ValueError(f"backup already exists: {collision}; move it before forcing the scaffold")
    return ScaffoldPlan(
        written,
        kept,
        index,
        index_state,
        overwritten,
        backups,
        tuple(content),
        tuple(expected),
    )


# The apply phase alone consumes the private payload bound by ScaffoldPlan.
# pylint: disable=protected-access
def apply_scaffold(plan: ScaffoldPlan) -> Scaffold:
    """Apply a scaffold plan after verifying that none of its targets changed.

    Every backup is written before any target is replaced. Therefore, a failed target write leaves
    the prior bytes recoverable.

    Raises
    ------
    ValueError
        If a target changed after planning or a backup path appeared.
    """
    for path, expected in plan._expected:
        current = path.read_bytes() if path.exists() else None
        if current != expected:
            raise ValueError(f"scaffold target changed after planning: {path}")
    collision = next(
        (backup for _, backup in plan.backups if backup.exists() or backup.is_symlink()),
        None,
    )
    if collision is not None:
        raise ValueError(f"backup already exists: {collision}; move it before forcing the scaffold")
    expected_by_path = dict(plan._expected)
    for source, backup in plan.backups:
        backup.parent.mkdir(parents=True, exist_ok=True)
        previous = expected_by_path[source]
        if previous is None:
            raise ValueError(f"cannot back up a scaffold target that did not exist: {source}")
        try:
            with backup.open("xb") as stream:
                stream.write(previous)
        except FileExistsError as error:
            raise ValueError(
                f"backup already exists: {backup}; move it before forcing the scaffold"
            ) from error
    for path, expected in plan._expected:
        current = path.read_bytes() if path.exists() else None
        if current != expected:
            raise ValueError(f"scaffold target changed after backup: {path}")
    for path, text in plan._content:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8")
    return Scaffold(
        plan.written,
        plan.kept,
        plan.index,
        plan.index_state,
        plan.overwritten,
        plan.backups,
    )


def scaffold(
    folder: Path,
    kinds: Sequence[str],
    force: bool = False,
    full_template: bool = False,
) -> Scaffold:
    """Write the missing records of ``kinds`` into ``folder``, and register them in its index.

    The kinds are written in the order of the index of templates, each once. The default record is
    sparse; ``full_template`` writes the complete commented template instead. An existing file is
    kept, so a scaffold never overwrites an authored record unless ``force`` is true. A forced
    scaffold preserves every existing target under ``.gnomon-backup`` before replacing it.

    Raises
    ------
    ValueError
        If a kind has no template, a required backup exists, or a target changes after planning.
    """
    return apply_scaffold(plan_scaffold(folder, kinds, force, full_template))
