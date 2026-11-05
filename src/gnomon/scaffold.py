"""
Creation of the folder of a problem, with the record templates in the order of filling.

The templates and their order are read from the folder of templates and from its index, which
groups them by the stages of the order of specification, so the scaffold follows every change of a
template or of the order without an edit of this module. The index of the new folder copies, for
each template written, its stage and the entry of the index of templates: the goal of the record.

A scaffold never overwrites a filled record: in a folder that already holds records, it writes only
the missing templates, and registers each of them in the existing index of the folder, under the
heading of its stage, so that the entries that the researcher wrote stay in place.

Constants
---------
CORE_KINDS
    The kinds that every problem receives: its itinerary, and the records of its first four stages.

Functions
---------
template_entries
    Return the entry of each template in the index of templates, in the order of that index.
register
    Return the text of an index with an entry for each kind that it does not list yet.
scaffold
    Write the missing templates of the given kinds into a folder, and register them in its index.
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


def _item(kind: str, entry: Entry) -> str:
    """Return the line of the index of a folder that registers the template of one kind."""
    return f"- [{entry.title}]({kind}.yml): {entry.goal}"


def _heading(entry: Entry) -> list[str]:
    """Return the lines that open the group of a stage, with its guidance when it has one."""
    return [f"## {entry.stage}", ""] + ([entry.guidance, ""] if entry.guidance else [])


def _index_text(name: str, kinds: Sequence[str], entries: dict[str, Entry]) -> str:
    """Return the index of a new folder, listing the templates of ``kinds`` stage by stage."""
    lines = [
        f"# {name}",
        "",
        "Fill the records stage by stage, and run `gnomon check` on this folder after each stage.",
    ]
    stage = None
    for kind in kinds:
        entry = entries[kind]
        if entry.stage != stage:
            stage = entry.stage
            lines += ["", *_heading(entry)]
        lines.append(_item(kind, entry))
    return "\n".join(lines) + "\n"


def register(text: str, kinds: Sequence[str], entries: dict[str, Entry] | None = None) -> str:
    r"""Return the text of an index with an entry for each kind that it does not list yet.

    An entry joins the group of its stage, after the last line of that group. A stage that the
    index does not hold yet receives its group before the first group of a later stage, or at the
    end. Every other line of the index is kept as it stands.

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
    order = list(dict.fromkeys(entry.stage for entry in entries.values()))
    lines = text.splitlines()
    for kind in kinds:
        if any(f"]({kind}.yml)" in line for line in lines):
            continue
        entry = entries[kind]
        headings = [(i, line[3:].strip()) for i, line in enumerate(lines) if line.startswith("## ")]
        own = next((i for i, stage in headings if stage == entry.stage), None)
        if own is not None:
            end = next((i for i, _ in headings if i > own), len(lines))
            while end > own + 1 and not lines[end - 1].strip():
                end -= 1
            lines.insert(end, _item(kind, entry))
            continue
        rank = order.index(entry.stage)
        later = next(
            (i for i, stage in headings if stage in order and order.index(stage) > rank), None
        )
        if later is None:
            while lines and not lines[-1].strip():
                lines.pop()
            lines += ["", *_heading(entry), _item(kind, entry)]
        else:
            lines[later:later] = [*_heading(entry), _item(kind, entry), ""]
    return "\n".join(lines) + "\n"


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
    """

    written: list[Path]
    kept: list[Path]
    index: Path
    index_state: str


def scaffold(folder: Path, kinds: Sequence[str], force: bool = False) -> Scaffold:
    """Write the missing templates of ``kinds`` into ``folder``, and register them in its index.

    The kinds are written in the order of the index of templates, each once. A template whose file
    exists is kept, so a scaffold never overwrites a filled record unless ``force`` is true; with
    ``force``, every template and the index are written anew.

    Raises
    ------
    ValueError
        If a kind has no template.
    """
    entries = template_entries()
    unknown = [k for k in kinds if k not in entries]
    if unknown:
        raise ValueError(
            f"no template for the kinds {', '.join(unknown)}; the kinds are {', '.join(entries)}"
        )
    chosen = [k for k in entries if k in set(kinds)]
    folder.mkdir(parents=True, exist_ok=True)
    written: list[Path] = []
    kept: list[Path] = []
    for kind in chosen:
        path = folder / f"{kind}.yml"
        if path.exists() and not force:
            kept.append(path)
            continue
        path.write_text((TEMPLATES / f"{kind}.yml").read_text(encoding="utf-8"), encoding="utf-8")
        written.append(path)
    index = folder / "_index.md"
    if force or not index.exists():
        index.write_text(_index_text(folder.name, chosen, entries), encoding="utf-8")
        return Scaffold(written, kept, index, "written")
    text = index.read_text(encoding="utf-8")
    updated = register(text, chosen, entries)
    if updated == text:
        return Scaffold(written, kept, index, "kept")
    index.write_text(updated, encoding="utf-8")
    return Scaffold(written, kept, index, "updated")
