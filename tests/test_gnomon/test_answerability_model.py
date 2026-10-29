"""Model of the conditions for obtaining an answer, checked against the notes that state it.

The model lives in ``answerability_model.yml``. These tests check that each quoted norm occurs in the
note of its activity, that the dependency table of the conditions note states the model's dependencies
route by route, that the activity map of the procedure note lists the model's activities, and that the
dependencies are acyclic in the stated order. A last test checks the facts of the records that the
worked example of the procedure cites; it reads the records, not the prose of the example.
"""

from __future__ import annotations

import re
from pathlib import Path
from typing import Any, Mapping

import pytest
import yaml

ROOT = Path(__file__).resolve().parents[2]
MODEL = yaml.safe_load((Path(__file__).with_name("answerability_model.yml")).read_text(encoding="utf-8"))
CASE = ROOT / "test" / "grokking-delayed-generalization"
CONDITIONS: list[str] = MODEL["conditions"]
ROUTES = ("selection", "construction")


def normalize(text: str) -> str:
    """Reduce Markdown to plain words: link text kept, emphasis, code marks, math and citations dropped."""
    text = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", text)
    text = re.sub(r"\[[a-z]+\d{4}[a-z_]*\]", "", text)
    text = re.sub(r"[*`$]", "", text)
    return re.sub(r"\s+", " ", text).strip().lower()


def read(key: str) -> str:
    return (ROOT / MODEL["sources"][key]).read_text(encoding="utf-8")


def table_rows(text: str, header: str) -> list[list[str]]:
    """Cells of the rows of the first table whose header row starts with ``header``."""
    lines = text.splitlines()
    start = next(i for i, line in enumerate(lines) if line.startswith(header))
    rows = []
    for line in lines[start + 2 :]:
        if not line.startswith("|"):
            break
        rows.append([cell.strip() for cell in line.strip().strip("|").split("|")])
    return rows


def activity_norms() -> dict[str, str]:
    norms: dict[str, str] = {}
    for path in sorted((ROOT / MODEL["sources"]["norms"]).glob("*.md")):
        for line in path.read_text(encoding="utf-8").splitlines():
            cells = [c.strip() for c in line.strip().strip("|").split("|")]
            if len(cells) == 3 and re.fullmatch(r"`[a-z-]+`", cells[0]):
                norms[cells[0].strip("`")] = normalize(cells[2])
    return norms


def applies(condition: str, route: str) -> bool:
    spec = MODEL["dependencies"][condition]
    return "both" in spec or route in spec


def dependencies(condition: str, route: str) -> set[str]:
    spec = MODEL["dependencies"][condition]
    return set(spec.get("both", [])) | set(spec.get(route, []))


def stated_dependencies(cell: str, route: str) -> set[str]:
    """Bold condition names of a cell, keeping the segments unqualified or qualified by ``route``."""
    names: set[str] = set()
    for segment in cell.split(";"):
        qualifier = re.match(r"\s*under (selection|construction)\b", segment)
        if qualifier is None or qualifier.group(1) == route:
            names |= {name.lower() for name in re.findall(r"\*\*([^*]+)\*\*", segment)}
    return names


def has_cycle(edges: Mapping[str, set[str]]) -> bool:
    state: dict[str, int] = {}

    def visit(node: str) -> bool:
        if state.get(node) == 1:
            return True
        if state.get(node) == 2:
            return False
        state[node] = 1
        cyclic = any(visit(m) for m in edges.get(node, set()))
        state[node] = 2
        return cyclic

    return any(visit(n) for n in edges)


@pytest.mark.parametrize("entry", MODEL["activities"], ids=lambda e: f"{e['id']}:{e['condition']}")
def test_norm_quotation_occurs(entry: Mapping[str, Any]) -> None:
    assert normalize(entry["norm"]) in activity_norms()[entry["id"]]


def test_mapped_activities_exist_in_the_registry() -> None:
    registry = yaml.safe_load((ROOT / "src/gnomon/data/registries/activities.yml").read_text(encoding="utf-8"))
    assert {e["id"] for e in MODEL["activities"]} <= {a["id"] for a in registry["activities"]}


def test_activity_map_of_the_procedure_matches_the_model() -> None:
    rows = table_rows(read("procedure"), "| Condition | Activities that act on it |")
    stated = {row[0].lower(): set(re.findall(r"`([a-z-]+)`", row[1])) for row in rows}
    model: dict[str, set[str]] = {c: set() for c in CONDITIONS}
    for entry in MODEL["activities"]:
        model[entry["condition"]].add(entry["id"])
    assert stated == model


def test_cycle_check_fires_on_a_planted_cycle() -> None:
    assert has_cycle({"a": {"b"}, "b": {"a"}})


@pytest.mark.parametrize("route", ROUTES)
def test_dependencies_are_acyclic_and_follow_the_stated_order(route: str) -> None:
    edges = {c: dependencies(c, route) for c in CONDITIONS if applies(c, route)}
    assert not has_cycle(edges)
    rank = {c: i for i, c in enumerate(CONDITIONS)}
    assert all(d in edges and rank[d] < rank[c] for c in edges for d in edges[c])


@pytest.mark.parametrize("route", ROUTES)
def test_dependency_table_of_the_conditions_note_matches_the_model(route: str) -> None:
    rows = table_rows(read("conditions"), "| Condition | Depends on |")
    stated = {row[0].lower(): stated_dependencies(row[1], route) for row in rows}
    assert set(stated) == set(CONDITIONS)
    assert {c: stated[c] for c in CONDITIONS if applies(c, route)} == {
        c: dependencies(c, route) for c in CONDITIONS if applies(c, route)
    }


def test_record_facts_cited_by_the_example() -> None:
    plan = yaml.safe_load((CASE / "plan.yml").read_text(encoding="utf-8"))
    verdicts = {step["id"]: step["norm"]["verdict"] for step in plan["steps"]}
    assert {k: verdicts[k] for k in ("identify", "propose", "derive", "admit", "test")} == {
        "identify": "pass", "propose": "pass", "derive": "pending", "admit": "fail", "test": "pending"
    }
    tests = yaml.safe_load((CASE / "assessment.yml").read_text(encoding="utf-8"))["tests"]
    failed = {level: {k for k, v in t.items() if v["verdict"] == "fail"} for level, t in tests.items()}
    assert failed == {"admissibility": {"scope", "grain", "modal-strength", "product"},
                      "warrant": {"closure", "fidelity", "robustness"}}
