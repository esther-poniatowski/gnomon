"""Alignment between the specification notes and the templates they document.

A specification note in ``docs/specification`` states one specification per table row; a template
in ``src/gnomon/data/templates`` holds one key per specification. These tests check that the
two agree: every documented specification exists in its template, in the same order, and no
template key is left undocumented.

The association is lexical, so that the notes stay readable without the templates: the name of
a row is the name of its key, or begins with it ("Domain of conditions" for ``domain``), and a
nested specification is written "Parent: child" ("Tests: admissibility" for ``tests.admissibility``).
A note holding two tables under the same header names each by the block anchor that precedes it.
"""

from __future__ import annotations

import re
from pathlib import Path
from typing import Any, Iterable, Mapping, Sequence

import pytest
import yaml

ROOT = Path(__file__).resolve().parents[2]
DOCS = ROOT / "docs"
TEMPLATES = ROOT / "src" / "gnomon" / "data" / "templates"
REGISTRY = ROOT / "src" / "gnomon" / "data"

# Fields that identify a record rather than specify an inquiry, so no note documents them.
RECORD_FIELDS = frozenset(
    {"id", "type", "title", "status", "answers", "target_system", "phenomenon", "name"}
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
        hit = name if name in candidates else next(  # an exact name wins over a prefix: "data_model" over "data"
            (key for key in candidates if name.startswith(key + "_") or key.startswith(name + "_")),
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


#: A table header, or a pair of a block anchor and a header: the first table opened by the header
#: after the line that declares the anchor.
Header = str | tuple[str, str]


def table_lines(note: str, header: Header) -> list[str]:
    """Return the body rows of the table opened by ``header``, as lines of the note."""
    lines = (DOCS / note).read_text(encoding="utf-8").splitlines()
    anchor, opening = header if isinstance(header, tuple) else ("", header)
    after = 0
    if anchor:
        after = next((i for i, line in enumerate(lines) if line.rstrip().endswith(f"^{anchor}")), -1)
        assert after >= 0, f"no block anchor ^{anchor} in {note}"
    start = next((i for i, line in enumerate(lines) if i >= after and line.startswith(opening)), None)
    assert start is not None, f"no table opening with {opening!r} in {note}"
    end = start
    while end + 1 < len(lines) and lines[end + 1].startswith("|"):
        end += 1
    return lines[start + 2 : end + 1]


def table_rows(note: str, header: Header) -> list[str]:
    """Return the first cell of every row of the table opened by ``header``."""
    return [line.lstrip("|").split("|")[0].strip() for line in table_lines(note, header)]


def template(name: str) -> dict[str, Any]:
    return yaml.safe_load((TEMPLATES / name).read_text(encoding="utf-8"))


def documented_keys(note: str, header: Header, paths: Sequence[str], prefix: str) -> list[str]:
    keys = []
    for row in table_rows(note, header):
        key = resolve(row_slugs(row), paths, prefix)
        assert key is not None, f"{note}: no key of the template answers to the row {row!r}"
        keys.append(key)
    return keys


# (label, note, table header, template, scope of the reverse check, prefix, keys documented elsewhere)
PAIRS = [
    ("problem", "specification/problem.md", "| Specification", "problem.yml", None, "", {}),
    ("target-system", "specification/target-system.md", "| Specification", "target-system.yml", None, "", ELSEWHERE_MATURITY),
    ("background", "specification/background.md", "| Specification", "background.yml", None, "", ELSEWHERE_MATURITY),
    ("phenomenon", "specification/phenomenon.md", "| Specification", "phenomenon.yml", None, "", ELSEWHERE_MATURITY),
    (
        "operators",
        "specification/operators.md",
        "| Specification",
        "operators.yml",
        None,
        "",
        ELSEWHERE_MATURITY,
    ),
    ("question-links", "specification/question.md", "| Field", "question.yml", "links", "", {}),
    ("subject-of-inquiry", "specification/question-subject.md", "| Component", "question.yml", "subject", "subject", {}),
    ("contrast", "specification/question-subject.md", ("contrast-fields", "| Specification"), "question.yml", "subject.contrast", "subject.contrast", {}),
    ("domain", "specification/question-subject.md", ("domain-fields", "| Specification"), "question.yml", "subject.domain", "subject.domain", {}),
    ("epistemic-task", "specification/question-task.md", "| Dimension", "question.yml", "task", "task", {}),
    (
        "admissible-explanans",
        "specification/question-task.md",
        ("level-axes", "| Specification"),
        "question.yml",
        "task.admissible_explanans",
        "task.admissible_explanans",
        {},
    ),
    ("answer-core", "specification/answer.md", "| Element", "answer.yml", None, "", ELSEWHERE_MATURITY),
    ("answer-aim-blocks", "specification/answer.md", "| Aim |", "answer.yml", "aim_block", "aim_block", {}),
    (
        "answer-explanation-block",
        "specification/answer.md",
        "| Specification",
        "answer.yml",
        "aim_block.explanation",
        "aim_block.explanation",
        {},
    ),
    ("model", "specification/model.md", "| Element", "model.yml", None, "", ELSEWHERE_MATURITY),
    (
        "binding",
        "specification/binding.md",
        ("binding-record", "| Specification"),
        "binding.yml",
        None,
        "",
        ELSEWHERE_MATURITY,
    ),
    ("key", "specification/key.md", ("key-record", "| Specification"), "key.yml", None, "", ELSEWHERE_MATURITY),
    (
        "assessment",
        "specification/assessment.md",
        ("assessment-record", "| Specification"),
        "assessment.yml",
        None,
        "",
        ELSEWHERE_MATURITY,
    ),
    ("itinerary", "specification/itinerary.md", "| Specification", "itinerary.yml", None, "", {}),
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
    note = (DOCS / "specification/expressions.md").read_text(encoding="utf-8")
    bullet = re.search(r"- \*\*The canonical operators.*?\^operator-groups", note, re.S)
    assert bullet is not None, "the note declares no canonical operators"
    documented = set(re.findall(r"`([A-Za-z_][A-Za-z_0-9]*)`", bullet.group(0)))
    declared = {e["symbol"] for e in yaml.safe_load((REGISTRY / "operators.yml").read_text())["operators"]}
    assert documented == declared, f"note and registry differ: {documented ^ declared}"


def test_no_operator_notation_doubles_a_backslash() -> None:
    """A single-quoted YAML scalar keeps every backslash, so a doubled one reaches LaTeX as a line break."""
    operators = yaml.safe_load((REGISTRY / "operators.yml").read_text())["operators"]
    doubled = [e["symbol"] for e in operators if re.search(r"\\\\[A-Za-z]", e.get("notation") or "")]
    assert not doubled, f"notations that double a backslash before a command: {doubled}"


def test_the_aim_note_lists_the_requirement_registry() -> None:
    """Each row of the aim table states what the registry declares for that aim."""
    note = (DOCS / "specification/question-task.md").read_text(encoding="utf-8")
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
    for aim, (required, produced) in documented.items():
        entry = declared[aim]
        assert required == [e["path"] for e in entry.get("required") or []], f"{aim}: required differs"
        assert produced == list(entry.get("to_produce") or []), f"{aim}: produced differs"


#: The cell openings of the column "When it is required" that state a registered requirement.
REQUIREMENT_CELLS = {"always": "always", "from `identified`": "identified", "from `specified`": "specified"}

# (registry entry, note, table header, template, prefix): a record kind is read under `always` and
# `by_commitment`, and the path of an aim block under `by_block`.
REQUIREMENT_TABLES = [
    ("target-system", "specification/target-system.md", "| Specification", "target-system.yml", ""),
    ("phenomenon", "specification/phenomenon.md", "| Specification", "phenomenon.yml", ""),
    ("background", "specification/background.md", "| Specification", "background.yml", ""),
    ("problem", "specification/problem.md", "| Specification", "problem.yml", ""),
    ("itinerary", "specification/itinerary.md", "| Specification", "itinerary.yml", ""),
    ("answer", "specification/answer.md", "| Element", "answer.yml", ""),
    ("aim_block.explanation", "specification/answer.md", "| Specification", "answer.yml", "aim_block.explanation"),
    ("model", "specification/model.md", "| Element", "model.yml", ""),
    ("binding", "specification/binding.md", ("binding-record", "| Specification"), "binding.yml", ""),
    ("key", "specification/key.md", ("key-record", "| Specification"), "key.yml", ""),
    ("assessment", "specification/assessment.md", ("assessment-record", "| Specification"), "assessment.yml", ""),
]


@pytest.mark.parametrize(
    "entry,note,header,tpl,prefix", REQUIREMENT_TABLES, ids=[table[0] for table in REQUIREMENT_TABLES]
)
def test_the_requirement_rows_of_a_note_are_the_registry_entries(
    entry: str, note: str, header: Header, tpl: str, prefix: str
) -> None:
    """A row marked required always, or from a level of commitment, is one the registry lists there.

    Each row resolves to the key path of its template, so a list traversed on the way is written
    ``[]``, as the registry writes it; a path inside an aim block is relative to that block.
    """
    paths = flatten(template(tpl))
    documented: dict[str, list[str]] = {section: [] for section in REQUIREMENT_CELLS.values()}
    for line in table_lines(note, header):
        cells = [c.strip() for c in line.strip("|").split("|")]
        for opening, section in REQUIREMENT_CELLS.items():
            if len(cells) > 1 and cells[1].lower().startswith(opening):
                key = resolve(row_slugs(cells[0]), paths, prefix)
                assert key is not None, f"{note}: no key of {tpl} answers to the row {cells[0]!r}"
                documented[section].append(key[len(prefix) + 1 :] if prefix else key)
    registry = yaml.safe_load((REGISTRY / "requirements.yml").read_text())
    if entry in (registry.get("by_block") or {}):
        declared = {"always": registry["by_block"][entry], "identified": [], "specified": []}
    else:
        declared = {
            "always": registry["always"].get(entry, []),
            **{
                level: (registry["by_commitment"].get(level) or {}).get(entry, [])
                for level in ("identified", "specified")
            },
        }
    assert documented == declared, f"{note}: {documented} against {declared}"


@pytest.mark.parametrize(
    "name",
    [
        "problem.yml",
        "target-system.yml",
        "background.yml",
        "phenomenon.yml",
        "question.yml",
        "answer.yml",
        "assessment.yml",
        "itinerary.yml",
        "model.yml",
        "binding.yml",
        "key.yml",
    ],
)
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
    note = (DOCS / "epistemology/epistemic-task/epistemic-pragmatic-virtues.md").read_text(encoding="utf-8")
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


def criteria(header: Header, column: int) -> list[str]:
    """Return the criteria of a table of tests, as the assessment template writes them."""
    return [
        line.strip("|").split("|")[column].strip().lower().replace(" ", "-")
        for line in table_lines("epistemology/answer/satisfaction-conditions.md", header)
    ]


#: The tables of tests of each tier: the tests of the core and of each aim block for admissibility,
#: and the table of the warrant level. The column holds the name of the criterion.
TIERS = {
    "admissibility": [(("admissibility-per-block", "| Criterion"), 0), ("| Aim block |", 1)],
    "warrant": [(("warrant-through-binding", "| Criterion"), 0)],
}


@pytest.mark.parametrize("tier", sorted(TIERS))
def test_the_criteria_of_the_note_are_the_tests_of_the_assessment(tier: str) -> None:
    """Each criterion of the tables of a tier is one test of the template, in the order of the note."""
    documented = [name for header, column in TIERS[tier] for name in criteria(header, column)]
    assert documented == list(template("assessment.yml")["tests"][tier])


def test_every_template_parses_and_declares_its_kind() -> None:
    files = sorted(TEMPLATES.glob("*.yml"))
    assert files, "no template to check"
    for path in files:
        record = template(path.name)
        assert "id" in record and "type" in record, f"{path.name} declares no identifier or kind"


def test_the_occurrence_table_of_the_phenomenon_note_is_the_registry() -> None:
    """The note documents which occurrence classes each category admits; the registry decides."""
    note = (DOCS / "specification/phenomenon.md").read_text(encoding="utf-8")
    section = re.search(r"\| Category \| Admitted occurrence \|[^\n]*\n\|[^\n]*\n((?:\|[^\n]*\n)+)", note)
    assert section is not None, "the note carries no table of occurrence classes"
    documented = {}
    for row in section.group(1).splitlines():
        cells = [c.strip() for c in row.strip("|").split("|")]
        documented[cells[0].strip("`")] = re.findall(r"`([a-z-]+)`", cells[1])
    declared = yaml.safe_load((REGISTRY / "requirements.yml").read_text())["occurrence_by_category"]
    assert documented == declared


def test_the_laws_of_a_model_take_the_keys_of_the_laws_of_a_background() -> None:
    """A model states its laws in background form, so its law entries carry every key of a background law."""
    model_keys = set(template("model.yml")["laws"][0])
    background_keys = set(template("background.yml")["laws"][0])
    assert background_keys <= model_keys, sorted(background_keys - model_keys)


def test_the_aim_categories_of_the_note_are_the_registry() -> None:
    """The Category column of the registry of aims states the category that the registry declares.

    An exploration takes its category from the origin of its equivalence criterion, so its cell
    names one category per origin.
    """
    names = {"answer content": "answer-content", "conceptual work": "conceptual-work", "mode of inquiry": "mode-of-inquiry"}
    documented: dict[str, Any] = {}
    for line in table_lines("epistemology/epistemic-task/epistemic-aim.md", "| Epistemic aim | Category"):
        cells = [c.strip() for c in line.strip("|").split("|")]
        aim = re.search(r"\(`([a-z-]+)`\)", cells[0])
        assert aim is not None, f"no aim value in {cells[0]!r}"
        by_origin = re.findall(r"(answer content|conceptual work|mode of inquiry), when (?:its|the) (?:equivalence )?criterion is an (input|output)", cells[1])
        documented[aim.group(1)] = {o: names[c] for c, o in by_origin} if by_origin else names[cells[1]]
    aims = yaml.safe_load((REGISTRY / "vocabularies.yml").read_text())["vocabularies"]["question"]["task.epistemic_aim"]
    assert documented == {entry["value"]: entry.get("category") for entry in aims}


def test_the_answer_conditions_of_the_note_are_the_registry() -> None:
    """Each row of the table of answer conditions states the three conditions that the registry declares."""
    def plain(cell: str) -> str:
        return re.sub(r"\s*\[[a-z0-9_]+\]", "", cell).strip()

    documented = {}
    for line in table_lines("epistemology/epistemic-task/epistemic-aim.md", "| Aim | Direct answer |"):
        cells = [plain(c) for c in line.strip("|").split("|")]
        documented[cells[0].strip("`")] = tuple(cells[1:4])
    aims = yaml.safe_load((REGISTRY / "vocabularies.yml").read_text())["vocabularies"]["question"]["task.epistemic_aim"]
    declared = {e["value"]: (e.get("direct_answer"), e.get("conclusive_when"), e.get("presupposes")) for e in aims}
    assert documented == declared

