"""Model of the conditions of answerability and of the choice of the next act, checked against the vault.

The model lives in ``answerability_model.yml``. Its quotations must occur in the notes that they cite,
its clauses must cover each satisfaction test, and the tables of the two notes must state the same
dependencies, assignments and activities as the model. The remaining tests exercise the rules of the
procedure on planted cases and on the records of the inquiry into delayed generalization.
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


def normalize(text: str) -> str:
    """Reduce Markdown to plain words: link text kept, emphasis, code marks, math and citations dropped."""
    text = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", text)
    text = re.sub(r"\[[a-z]+\d{4}[a-z_]*\]", "", text)
    text = text.replace("<br>", " ")
    text = re.sub(r"[*`$]", "", text)
    text = re.sub(r"(^|\s)-\s", " ", text)
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


def bold_names(cell: str) -> set[str]:
    return {name.lower() for name in re.findall(r"\*\*([^*]+)\*\*", cell)}


def satisfaction_tests() -> dict[str, str]:
    """Test name -> normalized text of its cell, from the admissibility and warrant tables."""
    text = read("tests")
    cells: dict[str, str] = {}
    for header in ("| Criterion      | Test", "| Criterion              | Test"):
        for row in table_rows(text, header):
            cells[row[0]] = normalize(row[1])
    return cells


def activity_norms() -> dict[str, str]:
    norms: dict[str, str] = {}
    for path in sorted((ROOT / MODEL["sources"]["norms"]).glob("*.md")):
        for line in path.read_text(encoding="utf-8").splitlines():
            cells = [c.strip() for c in line.strip().strip("|").split("|")]
            if len(cells) == 3 and re.fullmatch(r"`[a-z-]+`", cells[0]):
                norms[cells[0].strip("`")] = normalize(cells[2])
    return norms


def dependencies(condition: str, route: str | None = None) -> set[str]:
    spec = MODEL["dependencies"][condition]
    routes = [route] if route else list(spec)
    return {d for r in routes for d in spec.get(r, spec.get("both", []))}


# --------------------------------------------------------------------------- quotations


@pytest.mark.parametrize("entry", MODEL["tests"], ids=lambda e: f"{e['test']}:{e['condition']}")
def test_test_quotation_occurs(entry: Mapping[str, Any]) -> None:
    assert normalize(entry["quote"]) in satisfaction_tests()[entry["test"]]


def test_clauses_cover_each_test() -> None:
    cells = satisfaction_tests()
    assert set(cells) == {e["test"] for e in MODEL["tests"]}
    for name, cell in cells.items():
        rest = cell
        for entry in MODEL["tests"]:
            if entry["test"] == name:
                rest = rest.replace(normalize(entry["quote"]), " ")
        leftover = re.sub(r"\b(and|also)\b|[^a-z]", "", rest)
        assert not leftover, f"{name}: unassigned text {rest!r}"


@pytest.mark.parametrize("entry", MODEL["activities"], ids=lambda e: f"{e['id']}:{e['condition']}")
def test_norm_quotation_occurs(entry: Mapping[str, Any]) -> None:
    assert normalize(entry["norm"]) in activity_norms()[entry["id"]]


def test_task_components_are_named_in_the_task_note() -> None:
    task = normalize(read("task"))
    assert all(name.lower() in task for name in MODEL["task_components"])


# --------------------------------------------------------------------------- dependencies


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


def test_cycle_check_fires_on_a_planted_cycle() -> None:
    assert has_cycle({"a": {"b"}, "b": {"a"}})


def test_dependencies_are_acyclic_and_follow_the_stated_order() -> None:
    edges = {c: dependencies(c) for c in CONDITIONS}
    assert not has_cycle(edges)
    rank = {c: i for i, c in enumerate(CONDITIONS)}
    assert all(rank[d] < rank[c] for c in CONDITIONS for d in edges[c])


def test_dependency_table_of_the_note_matches_the_model() -> None:
    rows = table_rows(read("conditions"), "| Condition | Depends on |")
    stated = {row[0].lower(): bold_names(row[1]) for row in rows}
    assert stated == {c: dependencies(c) for c in CONDITIONS}


def test_test_table_of_the_note_matches_the_model() -> None:
    rows = table_rows(read("conditions"), "| Test | Level | Conditions |")
    stated = {row[0]: bold_names(row[2]) for row in rows}
    model: dict[str, set[str]] = {}
    for entry in MODEL["tests"]:
        model.setdefault(entry["test"], set()).add(entry["condition"])
    assert stated == model


def test_activity_map_of_the_note_matches_the_model() -> None:
    rows = table_rows(read("procedure"), "| Condition | Activities that establish it |")
    ids = lambda cell: set(re.findall(r"`([a-z-]+)`", cell))
    stated = {row[0].lower(): (ids(row[1]), ids(row[2])) for row in rows}
    model: dict[str, tuple[set[str], set[str]]] = {c: (set(), set()) for c in CONDITIONS}
    for entry in MODEL["activities"]:
        model[entry["condition"]][entry["role"] == "contributes"].add(entry["id"])
    assert stated == {c: v for c, v in model.items() if c in stated}
    assert set(stated) == set(CONDITIONS)


def test_mapped_activities_exist_in_the_registry() -> None:
    registry = yaml.safe_load((ROOT / "src/gnomon/data/registries/activities.yml").read_text(encoding="utf-8"))
    known = {a["id"] for a in registry["activities"]}
    assert {e["id"] for e in MODEL["activities"]} <= known


# --------------------------------------------------------------------------- rules of the procedure

EST, NE = "established", "not established"


def open_conditions(states: Mapping[str, str], route: str) -> list[str]:
    applicable = [c for c in CONDITIONS if route in MODEL["dependencies"][c] or "both" in MODEL["dependencies"][c]]
    return [c for c in applicable
            if states.get(c, NE) == NE and all(states.get(d, NE) == EST for d in dependencies(c, route))]


@pytest.mark.parametrize("route", ["selection", "construction"])
def test_diagnosis_never_stalls_when_nothing_is_refuted(route: str) -> None:
    states: dict[str, str] = {}
    while (opened := open_conditions(states, route)):
        states[opened[0]] = EST
    applicable = {c for c in CONDITIONS if route in MODEL["dependencies"][c] or "both" in MODEL["dependencies"][c]}
    assert {c for c, s in states.items() if s == EST} == applicable


class CandidateSet:
    """The set H under the rule on negative verdicts, with the record of withdrawn contents."""

    def __init__(self, contents: set[str]) -> None:
        self.contents, self.withdrawn = set(contents), set()

    def withdraw(self, content: str) -> None:
        self.contents.remove(content)
        self.withdrawn.add(content)

    def revise(self, old: str, new: str) -> None:
        if new in self.withdrawn | self.contents:
            raise ValueError("a revised candidate must differ from every withdrawn or present candidate")
        self.withdraw(old)
        self.contents.add(new)


def test_negative_verdicts_never_restore_an_earlier_state() -> None:
    h = CandidateSet({"A"})
    h.revise("A", "B")
    with pytest.raises(ValueError):
        h.revise("B", "A")
    h.withdraw("B")
    assert not h.contents


def producers() -> dict[str, list[str]]:
    plan = yaml.safe_load((CASE / "plan.yml").read_text(encoding="utf-8"))
    out: dict[str, list[str]] = {}
    for step in plan["steps"]:
        if step["output"].get("ref"):
            out.setdefault(step["output"]["ref"], []).append(step["norm"]["verdict"])
    return out


def readiness(records: list[str]) -> str:
    verdicts = [v for r in records for v in producers().get(r, [])]
    if "fail" in verdicts:
        return "blocked"
    return "conditional" if "pending" in verdicts else "ready"


def test_readiness_on_the_records_of_delayed_generalization() -> None:
    assert readiness(["phen.grokking.delayed_generalization"]) == "ready"
    assert readiness(["ans.grokking.slow-structured-representation", "system.delayed_generalization_networks"]) == "conditional"
    assert readiness(["bg.delayed_generalization_networks.training-specification"]) == "blocked"


def test_failed_admissibility_tests_of_the_example() -> None:
    tests = yaml.safe_load((CASE / "assessment.yml").read_text(encoding="utf-8"))["tests"]
    failed = {k for k, v in tests["admissibility"].items() if v["verdict"] == "fail"}
    assert failed == {"scope", "grain", "modal-strength", "product"}
    assert tests["admissibility"]["admissible-explanans"]["verdict"] == "pending"
