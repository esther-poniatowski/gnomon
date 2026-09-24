"""Alignment between the method notes and the templates they specify.

A method note in ``docs/epistemology`` states one specification per table row; a template
in ``src/gnomon/data/templates`` holds one key per specification. These tests check that the
two agree: every documented specification exists in its template, in the same order, and no
template key is left undocumented.

The association is lexical, so that the notes stay readable without the templates: the name of
a row is the name of its key, or begins with it ("Domain of conditions" for ``domain``), and a
nested specification is written "Parent: child" ("Tests: admissibility" for ``tests.admissibility``).
"""

from __future__ import annotations

import re
from pathlib import Path
from typing import Any, Iterable, Mapping, Sequence

import pytest
import yaml

ROOT = Path(__file__).resolve().parents[2]
DOCS = ROOT / "docs" / "epistemology"
TEMPLATES = ROOT / "src" / "gnomon" / "data" / "templates"
REGISTRY = ROOT / "src" / "gnomon" / "data"

# Fields that identify a record rather than specify an inquiry, so no note documents them.
RECORD_FIELDS = frozenset(
    {"id", "type", "title", "status", "answers", "target_system", "phenomenon", "name"}
)

# Keys documented in another note than the one under test, with the note that documents them.
ELSEWHERE_MATURITY = {"maturity": "subject-of-inquiry.md"}


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
        hit = next(
            (
                key
                for key in dict.fromkeys(children)
                if name == key or name.startswith(key + "_") or key.startswith(name + "_")
            ),
            None,
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


def table_rows(note: str, header: str) -> list[str]:
    """Return the first cell of every row of the table opened by ``header``."""
    lines = (DOCS / note).read_text(encoding="utf-8").splitlines()
    start = next((i for i, line in enumerate(lines) if line.startswith(header)), None)
    assert start is not None, f"no table opening with {header!r} in {note}"
    end = start
    while end + 1 < len(lines) and lines[end + 1].startswith("|"):
        end += 1
    return [line.lstrip("|").split("|")[0].strip() for line in lines[start + 2 : end + 1]]


def template(name: str) -> dict[str, Any]:
    return yaml.safe_load((TEMPLATES / name).read_text(encoding="utf-8"))


def documented_keys(note: str, header: str, paths: Sequence[str], prefix: str) -> list[str]:
    keys = []
    for row in table_rows(note, header):
        key = resolve(row_slugs(row), paths, prefix)
        assert key is not None, f"{note}: no key of the template answers to the row {row!r}"
        keys.append(key)
    return keys


# (label, note, table header, template, scope of the reverse check, prefix, keys documented elsewhere)
PAIRS = [
    ("target-system", "target-system.md", "| Specification", "target-system.yml", None, "", ELSEWHERE_MATURITY),
    ("phenomenon", "phenomenon.md", "| Specification", "phenomenon.yml", None, "", ELSEWHERE_MATURITY),
    (
        "operators",
        "symbols-and-expressions.md",
        "| Specification",
        "operators.yml",
        None,
        "",
        ELSEWHERE_MATURITY,
    ),
    ("subject-of-inquiry", "subject-of-inquiry.md", "| Component", "question.yml", "subject", "subject", {}),
    ("contrast", "contrast.md", "| Specification", "question.yml", "subject.contrast", "subject.contrast", {}),
    ("domain", "domain.md", "| Specification", "question.yml", "subject.domain", "subject.domain", {}),
    ("epistemic-task", "epistemic-task.md", "| Dimension", "question.yml", "task", "task", {}),
    (
        "admissible-explanans",
        "admissible-explanans.md",
        "| Specification",
        "question.yml",
        "task.admissible_explanans",
        "task.admissible_explanans",
        {},
    ),
    (
        "answer-form",
        "answer-form.md",
        "| Element",
        "answer.yml",
        None,
        "",
        {**ELSEWHERE_MATURITY, "answer_statement": "answer-form.md"},
    ),
    (
        "assessment",
        "satisfaction-conditions.md",
        "| Specification",
        "assessment.yml",
        None,
        "",
        {**ELSEWHERE_MATURITY, "assesses": "satisfaction-conditions.md", "against": "satisfaction-conditions.md"},
    ),
]

IDS = [pair[0] for pair in PAIRS]


@pytest.mark.parametrize("pair", PAIRS, ids=IDS)
def test_every_specification_of_the_note_exists_in_its_template(pair: tuple) -> None:
    _, note, header, tpl, _, prefix, _ = pair
    paths = flatten(template(tpl))
    documented_keys(note, header, paths, prefix)  # asserts on the first row without a key


@pytest.mark.parametrize("pair", PAIRS, ids=IDS)
def test_the_note_and_its_template_agree_on_the_order(pair: tuple) -> None:
    _, note, header, tpl, _, prefix, _ = pair
    paths = flatten(template(tpl))
    keys = documented_keys(note, header, paths, prefix)
    positions = [paths.index(key) for key in keys]
    out_of_order = [
        (keys[i], keys[i + 1]) for i in range(len(positions) - 1) if positions[i] > positions[i + 1]
    ]
    assert not out_of_order, f"{note}: {out_of_order} appear in the reverse order in {tpl}"


@pytest.mark.parametrize("pair", PAIRS, ids=IDS)
def test_no_key_of_the_template_is_undocumented(pair: tuple) -> None:
    _, note, header, tpl, scope, prefix, elsewhere = pair
    paths = flatten(template(tpl))
    keys = documented_keys(note, header, paths, prefix)
    depth = max((key.count(".") for key in keys), default=0)
    scoped: Iterable[str] = (
        paths if scope is None else [p for p in paths if p == scope or p.startswith(scope + ".")]
    )
    undocumented = [
        path
        for path in scoped
        if "[]" not in path  # an attribute of a list entry: described by the frame of its row
        and path.count(".") <= depth
        and path != scope
        and path not in keys
        and not any(key.startswith(path + ".") for key in keys)
        and not any(path == e or path.startswith(e + ".") for e in elsewhere)
        and path.split(".")[-1] not in RECORD_FIELDS
    ]
    assert not undocumented, f"{tpl}: {undocumented} appear in no row of {note}"


def test_the_operator_note_lists_the_registry(): 
    """The registry is the source; the note documents it and must not drift from it."""
    note = (DOCS / "symbols-and-expressions.md").read_text(encoding="utf-8")
    bullet = re.search(r"- \*\*The canonical operators.*?\^operator-groups", note, re.S)
    assert bullet is not None, "the note declares no canonical operators"
    documented = set(re.findall(r"`([A-Za-z_][A-Za-z_0-9]*)`", bullet.group(0)))
    declared = {e["symbol"] for e in yaml.safe_load((REGISTRY / "operators.yml").read_text())["operators"]}
    assert documented == declared, f"note and registry differ: {documented ^ declared}"


def test_the_aim_note_lists_the_requirement_registry() -> None:
    """Each row of the aim table states what the registry declares for that aim."""
    note = (DOCS / "epistemic-aim.md").read_text(encoding="utf-8")
    section = re.search(r"\| Aim \| Additionally required \|[^\n]*\n\|[^\n]*\n((?:\|[^\n]*\n)+)", note)
    assert section is not None, "the note carries no requirement table"
    documented = {}
    for row in section.group(1).splitlines():
        cells = [c.strip() for c in row.strip("|").split("|")]
        documented[cells[0].strip("`")] = (
            [i.split("=")[0].strip() for i in re.findall(r"`([^`]+)`", cells[1])],
            re.findall(r"`([^`]+)`", cells[2]) if len(cells) > 2 else [],
        )
    declared = yaml.safe_load((REGISTRY / "requirements.yml").read_text())["by_aim"]
    assert set(documented) == set(declared), f"aims differ: {set(documented) ^ set(declared)}"
    for aim, (required, relaxed) in documented.items():
        entry = declared[aim]
        assert required == [e["path"] for e in entry.get("required") or []], f"{aim}: required differs"
        assert relaxed == list(entry.get("open") or []), f"{aim}: relaxed differs"


@pytest.mark.parametrize("kind,note", [("target-system", "target-system.md"), ("phenomenon", "phenomenon.md")])
def test_the_always_rows_of_a_note_are_the_registry_entries(kind: str, note: str) -> None:
    """A specification the note marks required always is one the registry lists."""
    lines = (DOCS / note).read_text(encoding="utf-8").splitlines()
    start = next(i for i, line in enumerate(lines) if line.startswith("| Specification"))
    documented = []
    for line in lines[start + 2:]:
        if not line.startswith("|"):
            break
        cells = [c.strip() for c in line.strip("|").split("|")]
        if len(cells) > 1 and cells[1].lower().startswith("always"):
            documented.append(".".join(slug(part) for part in cells[0].split(" — ")[0].split(": ")))
    declared = yaml.safe_load((REGISTRY / "requirements.yml").read_text())["always"][kind]
    assert documented == declared, f"{note}: {documented} against {declared}"


@pytest.mark.parametrize("name", ["target-system.yml", "phenomenon.yml", "question.yml", "answer.yml", "assessment.yml"])
def test_the_option_lists_of_a_template_are_the_registry(name: str) -> None:
    """The registry is the source; a template comment documents it and must not drift from it."""
    vocab = re.compile(r"#\s*([a-z][a-z-]*(?: \([^)]*\))?(?: \| [a-z][a-z-]*(?: \([^)]*\))?)+)")
    documented, block = {}, ""
    for line in (TEMPLATES / name).read_text(encoding="utf-8").splitlines():
        m = re.match(r"^(\s*)(- )?([a-z_]+):(.*)$", line)
        if not m:
            continue
        if len(m.group(1)) == 0:
            block = m.group(3)
        found = vocab.search(m.group(4))
        if found:
            key = f"{'' if len(m.group(1)) == 0 else block}.{m.group(3)}"
            documented[key] = [
                re.match(r"([a-z-]+)", option.strip()).group(1)
                for option in found.group(1).split(" | ")
            ]
    kind = template(name)["type"]
    declared = yaml.safe_load((REGISTRY / "vocabularies.yml").read_text())["vocabularies"][kind]
    assert set(documented) == set(declared), f"{name}: {set(documented) ^ set(declared)}"
    for key, options in documented.items():
        assert options == [e["value"] for e in declared[key]], f"{name} {key}: {options}"


def test_the_virtues_of_the_note_are_the_options_of_the_question() -> None:
    note = (DOCS / "epistemic-pragmatic-virtues.md").read_text(encoding="utf-8")
    table = re.search(r"\| Virtue.*?\n\n", note, re.S)
    assert table is not None, "no virtue table in the note"
    names = [
        name.split(" / ")[0].strip().lower().replace(" ", "-")
        for name in re.findall(r"^\| \*\*([^|*]+)\*\*", table.group(0), re.M)
    ]
    question = (TEMPLATES / "question.yml").read_text(encoding="utf-8")
    options = re.search(r"^ *- virtue: *#(.*)$", question, re.M)
    assert options is not None, "no option list beside the virtues of the question"
    assert names == [opt.strip() for opt in options.group(1).split("|")]


@pytest.mark.parametrize("tier", ["admissibility", "warrant"])
def test_the_criteria_of_the_note_are_the_tests_of_the_assessment(tier: str) -> None:
    note = (DOCS / "satisfaction-conditions.md").read_text(encoding="utf-8")
    stop = "\n## Warrant" if tier == "admissibility" else r"\n\*Example\*"
    section = re.search(rf"## {tier.capitalize()}\n(.*?){stop}", note, re.S)
    assert section is not None, f"no {tier} table in the note"
    rows = [line for line in section.group(1).splitlines() if line.startswith("|")][2:]
    criteria = [row.split("|")[1].strip().lower().replace(" ", "-") for row in rows]
    assert criteria == list(template("assessment.yml")["tests"][tier])


def test_every_template_parses_and_declares_its_kind() -> None:
    files = sorted(TEMPLATES.glob("*.yml"))
    assert files, "no template to check"
    for path in files:
        record = template(path.name)
        assert "id" in record and "type" in record, f"{path.name} declares no identifier or kind"
