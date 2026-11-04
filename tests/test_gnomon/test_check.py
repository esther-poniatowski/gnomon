"""The commands that check a user's directory and scaffold a problem.

``gnomon check`` runs every check of the package on a directory tree, so it must stay silent on the
worked inquiries and report each defect planted in a copy of one of them. Each checker is observed
during one run on the worked inquiries, so a test of the corpus reads the context that the command
assembles rather than assembling its own. ``gnomon init`` writes the templates in the order of
filling and never overwrites a filled record.
"""

from __future__ import annotations

import shutil
from pathlib import Path
from types import ModuleType
from typing import Any, Callable, Mapping

import pytest
import yaml
from typer.testing import CliRunner

from gnomon import check as check_module
from gnomon import completeness, vocabulary
from gnomon.check import check_workspace, load_workspace
from gnomon.cli import app
from gnomon.findings import Finding, texts
from gnomon.report import render_yaml_report
from gnomon.scaffold import CORE_KINDS, scaffold, template_entries

from .paths import EXAMPLES

CASE = "grokking-delayed-generalization"

#: Each defect planted in a copy of the grokking inquiry: the file, the text replaced, its
#: replacement, and the rule that must report it.
PLANTED = [
    (
        "answer.yml",
        'holds: "0 < lambda3 * eta_rep"',
        'holds: "0 < lambda3 * eta_zzz"',
        "vocabulary/unresolved",
    ),
    (
        "answer.yml",
        "pair: bind.grokking.effective-representation.decoder-limit",
        "pair: bind.grokking.effective-representation.delay-scale",
        "completeness/mismatched-status-pair",
    ),
    (
        "answer.yml",
        "record: mod.grokking.effective-representation.representation_flow",
        "record: mod.grokking.effective-representation.no_such_law",
        "vocabulary/unknown-unit",
    ),
    (
        "assessment.yml",
        "assesses: ans.grokking.slow-structured-representation",
        "assesses: ans.grokking.missing-answer",
        "vocabulary/unknown-record",
    ),
    (
        "answer.yml",
        "modal_strength: actual",
        "modal_strength: certain",
        "completeness/inadmissible-value",
    ),
    ("binding.yml", "grain: qualitative", "grain:", "completeness/unmet-requirement"),
]


@pytest.fixture()
def planted(tmp_path: Path) -> Path:
    """Return a workspace holding a copy of the grokking inquiry with the planted defects."""
    folder = tmp_path / CASE
    shutil.copytree(EXAMPLES / CASE, folder)
    for name, old, new, _ in PLANTED:
        path = folder / name
        text = path.read_text(encoding="utf-8")
        assert old in text, f"{name}: the text to replace is absent: {old}"
        path.write_text(text.replace(old, new, 1), encoding="utf-8")
    return tmp_path


def test_the_worked_inquiries_pass_every_check() -> None:
    workspace = load_workspace(EXAMPLES)
    assert workspace.problems and not workspace.failures
    found = check_workspace(workspace)
    assert not found, [f"{x.file}: {x.finding.text}" for x in found]


#: The checkers that ``check_workspace`` runs, by the module through which it calls each of them.
CHECKERS: dict[ModuleType, tuple[str, ...]] = {
    check_module: ("malformed_answerability", "itinerary_problems"),
    completeness: (
        "undecided_boundaries",
        "unmet_general",
        "unmet_by_value",
        "unmet_commitment",
        "malformed_restrictions",
        "unjustified_explanans_bound",
        "unstated_standing",
        "contradictory_accuracy",
        "unresolved_slots",
        "unresolved_question_references",
        "unstated_function_sense",
        "unbounded_aim",
        "unmet_by_aim",
        "unanchored_explicandum",
        "unclassified_operations",
        "unbound_outputs",
        "mismatched_status_pairs",
        "incomplete_operations",
        "unmet_by_presence",
        "malformed_credence",
        "misdirected_assessment",
        "premature_appraisal",
        "mismatched_occurrence",
        "mismatched_request",
        "unsupported_outcome",
        "misstated_obstacles",
        "inadmissible_values",
    ),
    vocabulary: (
        "unresolved",
        "mistyped_symbols",
        "repeated_symbols",
        "misplaced_sharing",
        "vacuous_shared",
        "unfixed_parameters",
        "doubly_defined",
        "unowned_quantities",
        "unselected_conditions",
        "malformed_relations",
        "split_expressions",
        "corrupted_notation",
        "unordered_interactions",
        "overreaching_declarations",
        "misrouted_interactions",
        "misnamed_variant",
        "mismatched_arity",
        "unborne_variants",
        "overreaching_entries",
        "retired_in_use",
        "dangling_references",
        "unused_declarations",
    ),
}


def _recorded(
    function: Callable[..., list[Any]], calls: list[list[Any]]
) -> Callable[..., list[Any]]:
    """Return ``function``, recording the result of each call into ``calls``."""

    def spy(*args: Any, **kwargs: Any) -> list[Any]:
        result = function(*args, **kwargs)
        calls.append(result)
        return result

    return spy


@pytest.fixture(scope="module")
def corpus_run() -> dict[str, list[list[Any]]]:
    """Run ``check_workspace`` once on the worked inquiries, and return the results of each
    checker."""
    calls: dict[str, list[list[Any]]] = {name: [] for names in CHECKERS.values() for name in names}
    with pytest.MonkeyPatch.context() as patch:
        for module, names in CHECKERS.items():
            for name in names:
                patch.setattr(module, name, _recorded(getattr(module, name), calls[name]))
        check_workspace(load_workspace(EXAMPLES))
    return calls


@pytest.mark.parametrize("name", [name for names in CHECKERS.values() for name in names])
def test_each_checker_runs_on_the_worked_inquiries_and_reports_nothing(
    name: str,
    corpus_run: dict[str, list[list[Any]]],
) -> None:
    """A checker that the command never reaches is reported, as is any finding on the worked
    inquiries."""
    calls = corpus_run[name]
    assert calls, f"gnomon check never runs {name} on the worked inquiries"
    found: list[Finding] = [
        item[-1] if isinstance(item, tuple) else item for result in calls for item in result
    ]
    assert not found, texts(found)


def test_every_planted_defect_is_reported(planted: Path) -> None:
    rules = {x.finding.rule.id for x in check_workspace(load_workspace(planted))}
    missing = [rule for *_, rule in PLANTED if rule not in rules]
    assert not missing, f"not reported: {missing}"


def test_a_check_that_fails_is_reported_and_the_others_still_run(
    planted: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    def broken(record: Mapping[str, Any], ctx: object) -> list[Finding]:
        raise RuntimeError("planted")

    monkeypatch.setitem(check_module.BY_KIND, "binding", (broken,))
    found = check_workspace(load_workspace(planted))
    assert any(
        x.finding.rule.id == "check/failed" and (x.record or "").startswith("bind.") for x in found
    )
    assert any(x.finding.rule.id == "vocabulary/unresolved" for x in found)


def test_an_unreadable_file_is_reported_and_skipped(tmp_path: Path) -> None:
    (tmp_path / "broken.yml").write_text("a: [unclosed", encoding="utf-8")
    workspace = load_workspace(tmp_path)
    assert len(workspace.failures) == 1 and not workspace.problems


def test_the_report_is_stable_and_grouped_by_file(planted: Path) -> None:
    found = check_workspace(load_workspace(planted))
    first = render_yaml_report(found, "plant", 11)
    assert first == render_yaml_report(list(reversed(found)), "plant", 11)
    document = yaml.safe_load(first)
    assert document["findings"] == len(found) and document["files"][0]["file"].startswith(CASE)


def test_the_scaffold_writes_the_templates_in_the_order_of_filling(tmp_path: Path) -> None:
    folder = tmp_path / "my-problem"
    written = scaffold(folder, [*CORE_KINDS, "answer"])
    order = list(template_entries())
    names = [p.stem for p in written if p.suffix == ".yml"]
    assert names == sorted(names, key=order.index) and set(names) == {*CORE_KINDS, "answer"}
    index = (folder / "_index.md").read_text(encoding="utf-8")
    assert (
        index.index("(problem.yml)") < index.index("(question.yml)") < index.index("(answer.yml)")
    )


def test_the_scaffold_never_overwrites_a_record_unless_forced(tmp_path: Path) -> None:
    folder = tmp_path / "my-problem"
    scaffold(folder, CORE_KINDS)
    (folder / "question.yml").write_text("filled\n", encoding="utf-8")
    with pytest.raises(FileExistsError):
        scaffold(folder, CORE_KINDS)
    assert (folder / "question.yml").read_text(encoding="utf-8") == "filled\n"
    with pytest.raises(ValueError):
        scaffold(tmp_path / "other", ["nonsense"])


def test_the_commands_exit_with_the_status_of_their_findings(planted: Path, tmp_path: Path) -> None:
    runner = CliRunner()
    assert runner.invoke(app, ["check", str(EXAMPLES)]).exit_code == 0
    result = runner.invoke(
        app, ["check", str(planted), "--format", "yaml", "--output", str(tmp_path / "r.yml")]
    )
    assert result.exit_code == 1 and (tmp_path / "r.yml").is_file()
    assert runner.invoke(app, ["init", str(tmp_path / "new")]).exit_code == 0
    assert runner.invoke(app, ["init", str(tmp_path / "new")]).exit_code == 1


def test_a_template_not_yet_filled_is_listed_apart_and_not_checked(tmp_path: Path) -> None:
    """A researcher fills the records stage by stage, so the templates of later stages stay
    silent."""
    folder = tmp_path / "my-problem"
    scaffold(folder, CORE_KINDS)
    workspace = load_workspace(tmp_path)
    assert not workspace.by_id and len(workspace.unfilled) == len(CORE_KINDS)
    assert check_workspace(workspace) == []
    problem = folder / "problem.yml"
    problem.write_text(
        problem.read_text(encoding="utf-8").replace("id: prob.TOPIC.NAME", "id: prob.demo.first"),
        encoding="utf-8",
    )
    found = check_workspace(load_workspace(tmp_path))
    assert found and {x.record for x in found} == {"prob.demo.first"}
    assert not any(x.finding.rule.id == "vocabulary/unknown-record" for x in found)


def test_the_scaffold_opens_the_itinerary_and_follows_the_stages(tmp_path: Path) -> None:
    """The itinerary records each act from the first, and the question precedes its subject."""
    entries = template_entries()
    order = list(entries)
    assert order[0] == "itinerary" and order.index("question") < order.index("target-system")
    assert entries["question"].stage.startswith("2.") and entries["answer"].stage.startswith("5.")
    folder = tmp_path / "my-problem"
    scaffold(folder, CORE_KINDS)
    index = (folder / "_index.md").read_text(encoding="utf-8")
    assert (
        index.index("## Throughout the inquiry")
        < index.index("## 1. Problem")
        < index.index("## 2. Question schema")
    )


def test_a_required_block_whose_fields_are_all_empty_fails_its_requirement() -> None:
    from gnomon.completeness import unmet_general

    empty = {"construction": {"procedure": None, "reading": ""}}
    assert [f.text for f in unmet_general(empty, ["construction"])] == [
        "always required: construction"
    ]
    assert (
        unmet_general(
            {"construction": {"procedure": "design.a.b", "reading": ""}}, ["construction"]
        )
        == []
    )
