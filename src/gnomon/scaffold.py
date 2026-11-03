"""
Creation of the folder of a problem, with the record templates in the order of filling.

The templates and their order are read from the folder of templates and from its index, so the
scaffold follows every change of a template without an edit of this module. The index of the new
folder copies, for each template written, the entry of the index of templates: the goal of the
record, in the order of filling.

Constants
---------
CORE_KINDS
    The kinds that every problem receives: the problem, its subject, its question and its operators.

Functions
---------
template_entries
    Return the entry of each template in the index of templates, in the order of that index.
scaffold
    Write the templates of the given kinds and an index into a folder.
"""

from __future__ import annotations

import re
from pathlib import Path
from typing import Sequence

from .schemas import TEMPLATES

#: The kinds that every problem receives, which a researcher fills before any answer.
CORE_KINDS: tuple[str, ...] = ("problem", "target-system", "background", "phenomenon", "question", "operators")

#: An entry of the index of templates: its link text, its file and the goal of the record.
ENTRY = re.compile(r"^(?:\d+\.|-) \[([^\]]+)\]\(([\w-]+)\.yml\): (.+)$")


def template_entries(index: Path | None = None) -> dict[str, tuple[str, str]]:
    """Return, per kind, the title and the goal that the index of templates states, in its order.

    >>> entries = template_entries()
    >>> list(entries)[:2]
    ['problem', 'target-system']
    """
    text = (index or TEMPLATES / "_index.md").read_text(encoding="utf-8")
    return {m.group(2): (m.group(1), m.group(3)) for m in map(ENTRY.match, text.splitlines()) if m}


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
        raise ValueError(f"no template for the kinds {', '.join(unknown)}; the kinds are {', '.join(entries)}")
    chosen = [k for k in entries if k in set(kinds)]
    targets = [folder / f"{k}.yml" for k in chosen] + [folder / "_index.md"]
    existing = [p for p in targets if p.exists()]
    if existing and not force:
        raise FileExistsError(f"{', '.join(map(str, existing))} already exist; pass --force to overwrite")
    folder.mkdir(parents=True, exist_ok=True)
    for kind in chosen:
        (folder / f"{kind}.yml").write_text((TEMPLATES / f"{kind}.yml").read_text(encoding="utf-8"), encoding="utf-8")
    lines = [f"# {folder.name}", "", "Fill the records in the order below, then run `gnomon check` on this folder.", ""]
    lines += [f"{n}. [{entries[k][0]}]({k}.yml): {entries[k][1]}" for n, k in enumerate(chosen, 1)]
    (folder / "_index.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    return targets
