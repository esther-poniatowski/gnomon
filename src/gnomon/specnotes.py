"""
The association between the specification notes and the fields of the records that they document.

A specification note states one specification per table row, and a record template holds one key
per specification. The association is lexical, so that the notes stay readable without the
templates: the name of a row is the name of its key, or begins with it ("Domain of conditions" for
``domain``), and a nested specification is written "Parent: child" ("Tests: admissibility" for
``tests.admissibility``). A note holding two tables under the same header names each by the block
anchor that precedes it. The alignment tests and the field index read this one association.

Functions
---------
flatten
    Return every key path of a template, in document order.
slug, row_slugs
    Reduce the name of a row to the slugs of its key path.
resolve
    Find the key path that the name of a row denotes.
table_lines, table_rows
    Return the rows of a table of a note.
"""

from __future__ import annotations

import re
from pathlib import Path
from typing import Any, Mapping, Sequence

#: The folder of the documentation, beside the package in a checkout of the repository.
DOCS = Path(__file__).resolve().parents[2] / "docs"

#: Public location of the documentation read by researchers outside a source checkout.
DOCUMENTATION_BASE_URI = "https://github.com/esther-poniatowski/gnomon/blob/main/docs"


# Fields that identify a record rather than specify an inquiry, so no note documents them.
RECORD_FIELDS = frozenset(
    {
        "_schema",
        "id",
        "type",
        "title",
        "status",
        "answers",
        "target_system",
        "phenomenon",
        "name",
    }
)

# Keys documented in another note than the one under test, with the note that documents them.
ELSEWHERE_MATURITY = {"maturity": "specification/maturity.md"}


def flatten(node: Any, prefix: str = "") -> list[str]:
    """Return every key path of ``node``, in document order.

    A list contributes the paths of its first entry, marked with ``[]``, since every entry of a
    template list shares one shape.
    """
    paths: list[str] = []
    if isinstance(node, Mapping):
        for key, value in node.items():
            path = f"{prefix}.{key}" if prefix else str(key)
            paths.append(path)
            paths.extend(flatten(value, path))
    elif isinstance(node, list) and node:
        paths.extend(flatten(node[0], prefix + "[]"))
    return paths


def slug(text: str) -> str:
    """Reduce the name of a row to the form a key takes."""
    text = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", text)  # links
    text = re.sub(r"[*`\"]", "", text)  # emphasis and quotes
    text = re.sub(r"\$[^$]*\$", "", text)  # math
    text = re.sub(r"\([^)]*\)", "", text)  # parentheses
    return re.sub(r"[^a-z0-9]+", "_", text.strip().lower()).strip("_")


def row_slugs(cell: str) -> list[str]:
    """Split the name of a row into the slugs of its key path."""
    return [slug(part) for part in cell.split(" — ")[0].split(": ")]


def resolve(slugs: Sequence[str], paths: Sequence[str], prefix: str) -> str | None:
    """Find the key path that the name of a row denotes, or None when there is none."""
    parent = prefix
    for name in slugs:
        bases = [""] if not parent else [parent, parent + "[]"]
        children = []
        for path in paths:
            for base in bases:
                if not base:
                    if "." not in path:
                        children.append(path)
                elif path.startswith(base + ".") and path.count(".") == base.count(".") + 1:
                    children.append(path.split(".")[-1])
        candidates = list(dict.fromkeys(children))
        hit = (
            name
            if name in candidates
            else next(  # an exact name wins over a prefix: "data_model" over "data"
                (
                    key
                    for key in candidates
                    if name.startswith(key + "_") or key.startswith(name + "_")
                ),
                None,
            )
        )
        if hit is None:
            return None
        if not parent:
            parent = hit
        elif f"{parent}.{hit}" in paths:
            parent = f"{parent}.{hit}"
        else:
            parent = f"{parent}[].{hit}"
    return parent


#: A table header, or a pair of a block anchor and a header: the first table opened by the header
#: after the line that declares the anchor.
Header = str | tuple[str, str]

#: A note and its template: label, note, table header, template, scope of the reverse check,
#: prefix, and the keys documented elsewhere.
Pair = tuple[str, str, Header, str, str | None, str, Mapping[str, str]]


def table_lines(note: str, header: Header, docs: Path = DOCS) -> list[str]:
    """Return the body rows of the table opened by ``header``, as lines of the note."""
    lines = (docs / note).read_text(encoding="utf-8").splitlines()
    anchor, opening = header if isinstance(header, tuple) else ("", header)
    after = 0
    if anchor:
        after = next(
            (i for i, line in enumerate(lines) if line.rstrip().endswith(f"^{anchor}")),
            -1,
        )
        assert after >= 0, f"no block anchor ^{anchor} in {note}"
    start = next(
        (i for i, line in enumerate(lines) if i >= after and line.startswith(opening)),
        None,
    )
    assert start is not None, f"no table opening with {opening!r} in {note}"
    end = start
    while end + 1 < len(lines) and lines[end + 1].startswith("|"):
        end += 1
    return lines[start + 2 : end + 1]


def table_rows(note: str, header: Header, docs: Path = DOCS) -> list[str]:
    """Return the first cell of every row of the table opened by ``header``."""
    return [line.lstrip("|").split("|")[0].strip() for line in table_lines(note, header, docs)]


# (label, note, table header, template, scope of the reverse check, prefix,
#  keys documented elsewhere)
PAIRS: list[Pair] = [
    (
        "problem",
        "specification/problem.md",
        "| Specification",
        "problem.yml",
        None,
        "",
        ELSEWHERE_MATURITY,
    ),
    (
        "target-system",
        "specification/target-system.md",
        "| Specification",
        "target-system.yml",
        None,
        "",
        ELSEWHERE_MATURITY,
    ),
    (
        "background",
        "specification/background.md",
        "| Specification",
        "background.yml",
        None,
        "",
        ELSEWHERE_MATURITY,
    ),
    (
        "phenomenon",
        "specification/phenomenon.md",
        "| Specification",
        "phenomenon.yml",
        None,
        "",
        ELSEWHERE_MATURITY,
    ),
    (
        "operators",
        "specification/operators.md",
        "| Specification",
        "operators.yml",
        None,
        "",
        ELSEWHERE_MATURITY,
    ),
    (
        "question-links",
        "specification/question.md",
        "| Field",
        "question.yml",
        "links",
        "",
        {
            "subject": "specification/question-subject.md",
            "task": "specification/question-task.md",
            "virtues": "specification/question-virtues.md",
            **ELSEWHERE_MATURITY,
        },
    ),
    (
        "subject-of-inquiry",
        "specification/question-subject.md",
        "| Component",
        "question.yml",
        "subject",
        "subject",
        {},
    ),
    (
        "contrast",
        "specification/question-subject.md",
        ("contrast-fields", "| Specification"),
        "question.yml",
        "subject.contrast",
        "subject.contrast",
        {},
    ),
    (
        "domain",
        "specification/question-subject.md",
        ("domain-fields", "| Specification"),
        "question.yml",
        "subject.domain",
        "subject.domain",
        {},
    ),
    (
        "epistemic-task",
        "specification/question-task.md",
        "| Dimension",
        "question.yml",
        "task",
        "task",
        {},
    ),
    (
        "admissible-explanans",
        "specification/question-task.md",
        ("level-axes", "| Specification"),
        "question.yml",
        "task.admissible_explanans",
        "task.admissible_explanans",
        {},
    ),
    (
        "answer-core",
        "specification/answer.md",
        "| Element",
        "answer.yml",
        None,
        "",
        ELSEWHERE_MATURITY,
    ),
    (
        "answer-aim-blocks",
        "specification/answer.md",
        "| Aim |",
        "answer.yml",
        "aim_block",
        "aim_block",
        {},
    ),
    (
        "answer-explanation-block",
        "specification/answer.md",
        "| Specification",
        "answer.yml",
        "aim_block.explanation",
        "aim_block.explanation",
        {},
    ),
    (
        "model",
        "specification/model.md",
        "| Element",
        "model.yml",
        None,
        "",
        ELSEWHERE_MATURITY,
    ),
    (
        "binding",
        "specification/binding.md",
        ("binding-record", "| Specification"),
        "binding.yml",
        None,
        "",
        ELSEWHERE_MATURITY,
    ),
    (
        "key",
        "specification/key.md",
        ("key-record", "| Specification"),
        "key.yml",
        None,
        "",
        ELSEWHERE_MATURITY,
    ),
    (
        "assessment",
        "specification/assessment.md",
        ("assessment-record", "| Specification"),
        "assessment.yml",
        None,
        "",
        ELSEWHERE_MATURITY,
    ),
    (
        "concept",
        "specification/concept.md",
        "| Specification",
        "concept.yml",
        None,
        "",
        ELSEWHERE_MATURITY,
    ),
    (
        "design",
        "specification/design.md",
        "| Specification",
        "design.yml",
        None,
        "",
        ELSEWHERE_MATURITY,
    ),
    (
        "derivation",
        "specification/derivation.md",
        "| Specification",
        "derivation.yml",
        None,
        "",
        ELSEWHERE_MATURITY,
    ),
    (
        "itinerary",
        "specification/itinerary.md",
        "| Specification",
        "itinerary.yml",
        None,
        "",
        {},
    ),
]


def row_label(cell: str) -> str:
    """Return the name of a specification row as plain words."""
    text = cell.split(" — ")[0]
    text = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", text)
    text = re.sub(r"\$[^$]*\$", "", text)
    return re.sub(r"\s+", " ", re.sub(r"[*`]", "", text)).strip()


def documented_fields(
    kind: str, paths: Sequence[str], docs: Path = DOCS
) -> dict[str, tuple[str, str | None]]:
    """Return the note and row that directly document each resolved field of ``kind``."""
    found: dict[str, tuple[str, str | None]] = {}
    for _, note, header, template, _, prefix, elsewhere in PAIRS:
        if template != f"{kind}.yml":
            continue
        for cell in table_rows(note, header, docs):
            key = resolve(row_slugs(cell), paths, prefix)
            if key is not None:
                found.setdefault(key, (note, row_label(cell)))
        for key, other in elsewhere.items():
            found.setdefault(key, (other, None))
    return found


def field_documentation(
    path: str, documented: Mapping[str, tuple[str, str | None]]
) -> tuple[str | None, str | None]:
    """Return the nearest specification note and row that document ``path``."""
    probe = path
    while probe and probe not in documented:
        head = probe.rsplit(".", 1)[0] if "." in probe else ""
        probe = head.removesuffix("[]")
    if probe:
        return documented[probe]
    child = next(
        (key for key in documented if key.startswith((path + ".", path + "[]."))),
        None,
    )
    if child is None:
        return None, None
    note, row = documented[child]
    return note, (row.split(": ")[0] if row else None)


def documentation_notes(
    kind: str,
    resolution_paths: Sequence[str],
    field_paths: Sequence[str] | None = None,
    docs: Path = DOCS,
) -> dict[str, str]:
    """Return the canonical note of each documented schema field.

    ``resolution_paths`` are the concrete paths of the generated template, used to resolve table
    rows. ``field_paths`` may include deeper schema fields that inherit the resolved row.
    """
    direct = documented_fields(kind, resolution_paths, docs)
    return {
        path: note
        for path in field_paths or resolution_paths
        if (note := field_documentation(path, direct)[0]) is not None
    }


def documentation_target(note: str) -> str:
    """Return the public canonical target of a documentation note."""
    return f"{DOCUMENTATION_BASE_URI}/{note}"
