"""
Creation of the folder of a problem, with the record templates in the order of filling.

The templates and their order are read from the folder of templates and from its index, which
groups them by the stages of the order of specification, so the scaffold follows every change of a
template or of the order without an edit of this module. The index of the new folder copies, for
each template written, its stage and the entry of the index of templates: the goal of the record.

Constants
---------
CORE_KINDS
    The kinds that every problem receives: its itinerary, and the records of its first four stages.

Functions
---------
template_entries
    Return the entry of each template in the index of templates, in the order of that index.
scaffold
    Write the templates of the given kinds and an index into a folder.
"""

from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path
from typing import Sequence

from .schemas import TEMPLATES

#: The kinds that every problem receives: the itinerary, opened with the problem, and the records
#: of the stages that precede any candidate answer.
CORE_KINDS: tuple[str, ...] = (
    "itinerary",
    "problem",
    "question",
    "target-system",
    "phenomenon",
    "background",
    "operators",
)

#: An entry of the index of templates: its link text, its file and the goal of the record.
ENTRY = re.compile(r"^(?:\d+\.|-) \[([^\]]+)\]\(([\w-]+)\.yml\): (.+)$")


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


def scaffold(folder: Path, kinds: Sequence[str], force: bool = False) -> list[Path]:
    """Write the templates of ``kinds`` and an index into ``folder``, and return the files written.

    The kinds are written in the order of the index of templates, each once. No file is written
    when one of them exists and ``force`` is false, so a scaffold never overwrites a filled record.

    Raises
    ------
    ValueError
        If a kind has no template.
    FileExistsError
        If a file to write exists and ``force`` is false.
    """
    entries = template_entries()
    unknown = [k for k in kinds if k not in entries]
    if unknown:
        raise ValueError(
            f"no template for the kinds {', '.join(unknown)}; the kinds are {', '.join(entries)}"
        )
    chosen = [k for k in entries if k in set(kinds)]
    targets = [folder / f"{k}.yml" for k in chosen] + [folder / "_index.md"]
    existing = [p for p in targets if p.exists()]
    if existing and not force:
        raise FileExistsError(
            f"{', '.join(map(str, existing))} already exist; pass --force to overwrite"
        )
    folder.mkdir(parents=True, exist_ok=True)
    for kind in chosen:
        (folder / f"{kind}.yml").write_text(
            (TEMPLATES / f"{kind}.yml").read_text(encoding="utf-8"), encoding="utf-8"
        )
    lines = [
        f"# {folder.name}",
        "",
        "Fill the records stage by stage, and run `gnomon check` on this folder after each stage.",
    ]
    stage = None
    for kind in chosen:
        entry = entries[kind]
        if entry.stage != stage:
            stage = entry.stage
            lines += ["", f"## {stage}", ""] + ([entry.guidance, ""] if entry.guidance else [])
        lines.append(f"- [{entry.title}]({kind}.yml): {entry.goal}")
    (folder / "_index.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    return targets
