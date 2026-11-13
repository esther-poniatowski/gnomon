"""The commands that check a user's directory and scaffold a problem.

``gnomon check`` runs every check of the package on a directory tree, so it must stay silent on the
worked inquiries and report each defect planted in a copy of one of them. Each checker is observed
during one run on the worked inquiries, so a test of the corpus reads the context that the command
assembles rather than assembling its own. ``gnomon init`` writes sparse records in the order of
filling and never overwrites a filled record. The canonical full templates remain an explicit
source-authoring option.
"""

from __future__ import annotations

import json
import shutil
from collections.abc import Callable, Mapping
from pathlib import Path
from types import ModuleType
from typing import Any

import pytest
import yaml
from typer.testing import CliRunner

from gnomon import check as check_module
from gnomon import completeness, vocabulary
from gnomon.check import (
    check_workspace,
    check_workspace_result,
    future_record_requirements,
    load_workspace,
)
from gnomon.cli import app
from gnomon.findings import Finding, texts
from gnomon.report import render_yaml_report
from gnomon.scaffold import (
    CORE_KINDS,
    apply_scaffold,
    plan_scaffold,
    scaffold,
    scaffold_text,
    template_entries,
)
from gnomon.schemas import TEMPLATES

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
        "misstated_limit",
        "unjustified_explanans_bound",
        "unstated_standing",
        "contradictory_accuracy",
        "unresolved_slots",
        "foreign_backgrounds",
        "unstated_function_sense",
        "unbounded_aim",
        "unmet_by_aim",
        "unanchored_explicandum",
        "unclassified_operations",
        "unbound_outputs",
        "unstated_domain",
        "mismatched_status_pairs",
        "incomplete_operations",
        "unmet_by_presence",
        "malformed_credence",
        "misdirected_assessment",
        "premature_appraisal",
        "mismatched_occurrence",
        "mismatched_request",
        "unsupported_outcome",
        "unsupported_question_dissolution",
        "unbounded_censoring",
        "misdirected_rival",
        "unrealized_link",
        "unlinked_explanans",
        "misversioned_assessment",
        "unrecorded_question_revision",
        "misstated_obstacles",
        "inadmissible_values",
        "misplaced_maturity",
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
        "contradicted_signatures",
        "unordered_relations",
        "overreaching_declarations",
        "misrouted_relations",
        "misnamed_variant",
        "mismatched_arity",
        "misused_binders",
        "misapplied_quantities",
        "unborne_variants",
        "overreaching_entries",
        "retired_in_use",
        "malformed_identifier",
        "dangling_references",
        "foreign_topics",
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


@pytest.fixture()
def integrity_planted(planted: Path) -> Path:
    """Add one schema violation and one malformed identifier to the planted workspace."""
    folder = planted / CASE
    problem_path = folder / "problem.yml"
    problem = yaml.safe_load(problem_path.read_text(encoding="utf-8"))
    problem["unexpected"] = "not admitted by the problem contract"
    problem_path.write_text(yaml.safe_dump(problem, sort_keys=False), encoding="utf-8")

    target_path = folder / "target-system.yml"
    target = yaml.safe_load(target_path.read_text(encoding="utf-8"))
    target["id"] = "Malformed.Identifier"
    target_path.write_text(yaml.safe_dump(target, sort_keys=False), encoding="utf-8")
    return planted


@pytest.mark.parametrize("scope", completeness.validation_scopes())
def test_global_integrity_findings_remain_active_at_every_scope(
    integrity_planted: Path, scope: str
) -> None:
    rules = {
        item.finding.rule.id
        for item in check_workspace(load_workspace(integrity_planted), scope=scope)
    }
    assert {
        "contract/violation",
        "vocabulary/malformed-identifier",
        "vocabulary/unknown-record",
    } <= rules


def test_an_unknown_validation_scope_is_rejected() -> None:
    workspace = load_workspace(EXAMPLES)
    with pytest.raises(ValueError, match="unknown validation scope 'draft'"):
        check_workspace(workspace, scope="draft")
    with pytest.raises(ValueError, match="unknown validation scope 'draft'"):
        future_record_requirements(workspace, scope="draft")


def test_a_missing_field_becomes_a_finding_only_when_its_scope_is_due(
    tmp_path: Path,
) -> None:
    folder = tmp_path / CASE
    shutil.copytree(EXAMPLES / CASE, folder)
    binding_path = folder / "binding.yml"
    binding = yaml.safe_load(binding_path.read_text(encoding="utf-8"))
    binding["grain"] = None
    binding_path.write_text(yaml.safe_dump(binding, sort_keys=False), encoding="utf-8")

    early = check_workspace_result(load_workspace(tmp_path), scope="question-typed")
    due = check_workspace_result(load_workspace(tmp_path), scope="candidate-proposed")

    assert not early.findings
    assert any(
        item.due_scope == "candidate-proposed"
        and item.record == binding["id"]
        and item.path == "/grain"
        for item in early.future_work
    )
    assert any(
        item.record == binding["id"]
        and item.finding.rule.id == "completeness/unmet-requirement"
        and item.finding.locus == "/grain"
        for item in due.findings
    )
    assert not any(item.record == binding["id"] for item in due.future_work)


def test_the_scoped_command_serializes_future_work_without_failing(
    tmp_path: Path,
) -> None:
    folder = tmp_path / CASE
    shutil.copytree(EXAMPLES / CASE, folder)
    binding_path = folder / "binding.yml"
    binding = yaml.safe_load(binding_path.read_text(encoding="utf-8"))
    binding["grain"] = None
    binding_path.write_text(yaml.safe_dump(binding, sort_keys=False), encoding="utf-8")

    early = CliRunner().invoke(
        app, ["check", str(folder), "--scope", "question-typed", "--format", "yaml"]
    )
    sarif = CliRunner().invoke(
        app, ["check", str(folder), "--scope", "question-typed", "--format", "sarif"]
    )
    due = CliRunner().invoke(app, ["check", str(folder), "--scope", "candidate-proposed"])

    assert early.exit_code == 0, early.output
    report = yaml.safe_load(early.stdout)
    grain = [item for item in report["future_work"] if item["field_path"] == "/grain"]
    assert grain == [
        {
            "due_scope": "candidate-proposed",
            "source_file": "binding.yml",
            "record_identifier": binding["id"],
            "record_kind": "binding",
            "field_path": "/grain",
            "result_class": "computed inquiry diagnosis",
            "message": "always required: grain",
        }
    ]
    assert sarif.exit_code == 0, sarif.output
    sarif_run = json.loads(sarif.stdout)["runs"][0]
    assert sarif_run["results"] == []
    assert sarif_run["properties"]["gnomon/validationScope"][0]["value"] == "question-typed"
    assert due.exit_code == 1
    assert "completeness/unmet-requirement" in due.stdout


def test_the_scoped_command_rejects_an_unknown_scope() -> None:
    result = CliRunner().invoke(app, ["check", str(EXAMPLES), "--scope", "draft"])

    assert result.exit_code == 2
    assert "unknown validation scope 'draft'" in result.output


def test_a_problem_record_is_required_only_at_its_exact_checkpoint(
    tmp_path: Path,
) -> None:
    at_problem = check_workspace_result(load_workspace(tmp_path), scope="problem-posed")
    at_question = check_workspace_result(load_workspace(tmp_path), scope="question-typed")

    assert any(
        item.finding.rule.id == "completeness/unmet-scope"
        and item.finding.text == "scope problem-posed requires problem record"
        for item in at_problem.findings
    )
    assert not any(item.kind == "problem" for item in at_question.future_work)
    assert not any(
        item.finding.text == "scope problem-posed requires problem record"
        for item in at_question.findings
    )


def test_narrow_future_record_requirements_match_the_full_scoped_check(
    tmp_path: Path,
) -> None:
    """A view obtains missing record kinds without changing their scoped classification."""
    (tmp_path / "problem.yml").write_text(
        yaml.safe_dump({"id": "prob.a", "type": "problem"}), encoding="utf-8"
    )
    workspace = load_workspace(tmp_path)

    full = check_workspace_result(workspace, scope="problem-posed")
    narrow = future_record_requirements(workspace, scope="problem-posed")

    assert narrow == tuple(item for item in full.future_work if item.record is None)


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


def test_the_scaffold_writes_the_templates_in_the_order_of_filling(
    tmp_path: Path,
) -> None:
    folder = tmp_path / "my-problem"
    outcome = scaffold(folder, [*CORE_KINDS, "answer"])
    order = list(template_entries())
    names = [p.stem for p in outcome.written]
    assert names == sorted(names, key=order.index) and set(names) == {
        *CORE_KINDS,
        "answer",
    }
    index = (folder / "_index.md").read_text(encoding="utf-8")
    assert index.index("(problem.yml)") < index.index("(answer.yml)")


def test_the_default_scaffold_omits_optional_template_branches() -> None:
    """A new form starts with its working fields, not placeholder content in optional fields."""
    problem = yaml.safe_load(scaffold_text("problem"))
    assert list(problem) == [
        "_schema",
        "title",
        "statement",
        "id",
        "type",
        "status",
        "kind",
        "demand",
        "result_type",
        "request",
    ]
    assert not {
        "associated_question",
        "constraints",
        "explicanda",
        "sources",
        "knowledge_obstacles",
        "answerability_obstacles",
        "maturity",
    } & set(problem)

    itinerary = yaml.safe_load(scaffold_text("itinerary"))
    assert list(itinerary) == ["_schema", "title", "id", "type", "addresses", "steps"]
    assert itinerary["steps"] == [] and "act_appraisals" not in itinerary


def test_a_sparse_question_and_subject_expose_their_first_stage() -> None:
    """Creation context adds typed-question and identified-subject fields from the registry."""
    question = yaml.safe_load(scaffold_text("question"))
    assert list(question["subject"]) == ["target_system", "phenomenon", "contrast"]
    assert question["subject"]["target_system"] == {
        "placeholder": "system",
        "description": "THE ITEM AWAITED BY THE SLOT",
    }
    assert question["subject"]["phenomenon"] == {
        "placeholder": "phenomenon",
        "description": "THE ITEM AWAITED BY THE SLOT",
    }
    assert question["subject"]["contrast"] == {"locus": None}
    assert question["task"] == {
        "epistemic_aim": None,
        "modal_strength": None,
        "required_accuracy": {"standard": None},
    }
    assert not {"links", "sources", "virtues", "maturity"} & set(question)

    target = yaml.safe_load(scaffold_text("target-system"))
    assert {
        "commitment",
        "target_type",
        "identification",
        "reference_class",
    } <= set(target)
    assert target["identification"] == {} and target["reference_class"] == {}
    assert "variables" not in target


def test_full_template_scaffolding_preserves_the_canonical_source() -> None:
    """The source-authoring option returns the generated template without transformation."""
    assert scaffold_text("problem", full_template=True) == (TEMPLATES / "problem.yml").read_text(
        encoding="utf-8"
    )


def test_init_can_request_the_complete_commented_template(tmp_path: Path) -> None:
    folder = tmp_path / "source-authored"

    result = CliRunner().invoke(app, ["init", str(folder), "--full-template"])

    assert result.exit_code == 0, result.output
    for kind in CORE_KINDS:
        assert (folder / f"{kind}.yml").read_bytes() == (TEMPLATES / f"{kind}.yml").read_bytes()


def test_init_creates_only_the_greenfield_starting_records(tmp_path: Path) -> None:
    """A new inquiry starts with one problem and its itinerary; later records are requested."""
    folder = tmp_path / "my-problem"

    result = CliRunner().invoke(app, ["init", str(folder)])

    assert result.exit_code == 0
    assert {path.name for path in folder.iterdir()} == {
        "_index.md",
        "itinerary.yml",
        "problem.yml",
    }
    index = (folder / "_index.md").read_text(encoding="utf-8")
    assert "(problem.yml)" in index and "(itinerary.yml)" in index
    assert "(question.yml)" not in index

    question = CliRunner().invoke(app, ["init", str(folder), "--with", "question"])

    assert question.exit_code == 0
    assert (folder / "question.yml").is_file()
    updated = (folder / "_index.md").read_text(encoding="utf-8")
    assert updated.index("(problem.yml)") < updated.index("(question.yml)")


def test_init_can_start_from_one_existing_question(tmp_path: Path) -> None:
    """Question-led adoption reaches a clean check without an artificial problem record."""
    folder = tmp_path / "active-question"

    result = CliRunner().invoke(app, ["init", str(folder), "--start-with", "question"])

    assert result.exit_code == 0
    assert {path.name for path in folder.iterdir()} == {
        "_index.md",
        "itinerary.yml",
        "question.yml",
    }
    index = (folder / "_index.md").read_text(encoding="utf-8")
    assert "(question.yml)" in index and "(problem.yml)" not in index
    assert index.index("(question.yml)") < index.index("(itinerary.yml)")
    assert "Fill the adopted question first" in index
    assert "Fill " + str(folder / "question.yml") + " first" in result.output

    question = {
        "_schema": "gnomon:question@3",
        "title": "Cause of an active observation",
        "statement": "What produces the active observation?",
        "id": "quest.adoption.active-observation",
        "type": "question",
        "status": "posed",
        "version": "1",
        "sources": [
            "notes/active-question.md#candidate-mechanism",
            "data/run-17.zarr",
        ],
        "request": "one",
        "links": [],
        "subject": {
            "target_system": {
                "placeholder": "system",
                "description": "the system already studied by the project",
            },
            "background": [],
            "phenomenon": {
                "placeholder": "phenomenon",
                "description": "the active observation",
            },
            "contrast": {
                "locus": "none",
                "foil_set": [],
                "compatibility": "derived",
                "foil_status": "not-applicable",
            },
        },
        "task": {
            "epistemic_aim": "explanation",
            "requested_relation": "nomological",
            "modal_strength": "actual",
            "admissible_explanans": None,
            "required_accuracy": {"standard": "qualitative"},
        },
        "virtues": [],
    }
    assert "addresses" not in question
    (folder / "question.yml").write_text(
        yaml.safe_dump(question, sort_keys=False), encoding="utf-8"
    )

    validated = CliRunner().invoke(app, ["validate", str(folder)])
    checked = CliRunner().invoke(app, ["check", str(folder)])
    scoped = CliRunner().invoke(app, ["check", str(folder), "--scope", "question-typed"])

    assert validated.exit_code == 0, validated.output
    assert "0 errors" in validated.output
    assert checked.exit_code == 0, checked.output
    assert "0 findings" in checked.output and "0 warnings" in checked.output
    assert scoped.exit_code == 0, scoped.output
    assert "0 findings" in scoped.output and "0 warnings" in scoped.output

    continued = CliRunner().invoke(
        app,
        [
            "init",
            str(folder),
            "--with",
            "target-system",
            "--with",
            "phenomenon",
        ],
    )

    assert continued.exit_code == 0, continued.output
    assert not (folder / "problem.yml").exists()
    assert (folder / "target-system.yml").is_file()
    assert (folder / "phenomenon.yml").is_file()
    assert "Fill the new subject records" in continued.output
    assert "then update " + str(folder / "question.yml") in continued.output


def test_adoption_promotes_only_source_units_required_by_the_question(
    tmp_path: Path,
) -> None:
    """Missing subject records are added while an unrelated model remains external."""
    folder = tmp_path / "selective-promotion"
    runner = CliRunner()
    assert runner.invoke(app, ["init", str(folder), "--start-with", "question"]).exit_code == 0

    target_id = "system.adoption-studied-system"
    phenomenon_id = "phen.adoption.active-observation"
    question = {
        "_schema": "gnomon:question@3",
        "title": "Cause of an active observation",
        "statement": "What produces the active observation?",
        "id": "quest.adoption.active-observation",
        "type": "question",
        "status": "posed",
        "version": "1",
        "sources": [
            "notes/active-question.md#active-observation",
            "data/run-17.zarr",
            "models/baseline.pkl",
        ],
        "request": "one",
        "links": [],
        "subject": {
            "target_system": target_id,
            "background": [],
            "phenomenon": phenomenon_id,
            "contrast": {
                "locus": "none",
                "foil_set": [],
                "compatibility": "derived",
                "foil_status": "not-applicable",
            },
        },
        "task": {
            "epistemic_aim": "explanation",
            "requested_relation": "nomological",
            "modal_strength": "actual",
            "admissible_explanans": None,
            "required_accuracy": {"standard": "qualitative"},
        },
        "virtues": [],
    }
    question_path = folder / "question.yml"
    question_path.write_text(yaml.safe_dump(question, sort_keys=False), encoding="utf-8")

    missing = runner.invoke(app, ["check", str(folder)])

    assert missing.exit_code == 1
    assert "no record carries the identifier" in missing.output
    question_before_promotion = question_path.read_bytes()
    added = runner.invoke(
        app,
        [
            "init",
            str(folder),
            "--with",
            "target-system",
            "--with",
            "phenomenon",
        ],
    )
    assert added.exit_code == 0, added.output
    assert question_path.read_bytes() == question_before_promotion
    assert {path.name for path in folder.iterdir()} == {
        "_index.md",
        "itinerary.yml",
        "phenomenon.yml",
        "question.yml",
        "target-system.yml",
    }
    target: dict[str, Any] = {
        "_schema": "gnomon:target-system@2",
        "title": "System already studied by the project",
        "id": target_id,
        "type": "target-system",
        "status": "provisional",
        "commitment": "identified",
        "target_type": "particular",
        "identification": {
            "description": "the system recorded in run 17",
            "pointers": ["data/run-17.zarr"],
        },
        "reference_class": {
            "name": "the system recorded in run 17",
            "projectibility": {"status": "not-claimed"},
            "selection_criteria": [],
        },
    }
    phenomenon: dict[str, Any] = {
        "_schema": "gnomon:phenomenon@2",
        "title": "Active observation",
        "statement": "The studied system displays the active observation.",
        "id": phenomenon_id,
        "type": "phenomenon",
        "status": "provisional",
        "commitment": "identified",
        "target_system": target["id"],
        "identification": {
            "description": "the active observation reported for the studied system",
            "pointers": ["notes/active-question.md#active-observation"],
        },
    }
    (folder / "target-system.yml").write_text(
        yaml.safe_dump(target, sort_keys=False), encoding="utf-8"
    )
    (folder / "phenomenon.yml").write_text(
        yaml.safe_dump(phenomenon, sort_keys=False), encoding="utf-8"
    )
    promoted = runner.invoke(app, ["check", str(folder)])

    assert promoted.exit_code == 0, promoted.output
    assert "0 findings" in promoted.output and "0 warnings" in promoted.output
    assert target["identification"]["pointers"] == ["data/run-17.zarr"]
    assert phenomenon["identification"]["pointers"] == [
        "notes/active-question.md#active-observation"
    ]


def test_init_rejects_an_unknown_starting_kind_without_writing(tmp_path: Path) -> None:
    """The CLI rejects an unsupported adoption unit before creating its folder."""
    folder = tmp_path / "unsupported"

    result = CliRunner().invoke(app, ["init", str(folder), "--start-with", "source"])

    assert result.exit_code == 2
    assert not folder.exists()


@pytest.mark.parametrize("kind", ["problem", "phenomenon", "model", "answer"])
def test_init_scaffolds_named_standalone_record_kinds(tmp_path: Path, kind: str) -> None:
    """Each named standalone kind maps to its record template."""
    folder = tmp_path / kind

    result = CliRunner().invoke(
        app, ["init", str(folder), "--start-with", "question", "--with", kind]
    )

    assert result.exit_code == 0, result.output
    assert (folder / f"{kind}.yml").is_file()


@pytest.mark.parametrize("kind", ["law", "warrant"])
def test_init_rejects_nested_classifications_as_record_kinds_without_writing(
    tmp_path: Path, kind: str
) -> None:
    """A nested law or warrant role cannot be scaffolded as a standalone record."""
    folder = tmp_path / kind

    result = CliRunner().invoke(
        app, ["init", str(folder), "--start-with", "question", "--with", kind]
    )

    assert result.exit_code == 1
    assert "no template for the kinds" in result.output
    assert not folder.exists()


def test_the_scaffold_never_overwrites_a_record_unless_forced(tmp_path: Path) -> None:
    folder = tmp_path / "my-problem"
    scaffold(folder, CORE_KINDS)
    (folder / "problem.yml").write_text("filled\n", encoding="utf-8")
    again = scaffold(folder, CORE_KINDS)
    assert not again.written and again.index_state == "kept" and len(again.kept) == len(CORE_KINDS)
    assert (folder / "problem.yml").read_text(encoding="utf-8") == "filled\n"
    forced = scaffold(folder, CORE_KINDS, force=True)
    assert len(forced.written) == len(CORE_KINDS) and forced.index_state == "written"
    assert (folder / "problem.yml").read_text(encoding="utf-8") != "filled\n"
    with pytest.raises(ValueError):
        scaffold(tmp_path / "other", ["nonsense"])


def test_a_forced_scaffold_preserves_each_overwritten_file(tmp_path: Path) -> None:
    """A forced scaffold keeps the exact authored bytes before replacing them."""
    folder = tmp_path / "my-problem"
    scaffold(folder, CORE_KINDS)
    problem = folder / "problem.yml"
    index = folder / "_index.md"
    problem.write_bytes(b"authored problem\n")
    index.write_bytes(b"# Authored index\n")

    outcome = scaffold(folder, CORE_KINDS, force=True)

    assert problem in outcome.overwritten and index in outcome.overwritten
    backup = folder / ".gnomon-backup"
    assert (backup / "problem.yml.bak").read_bytes() == b"authored problem\n"
    assert (backup / "_index.md.bak").read_bytes() == b"# Authored index\n"
    assert problem.read_bytes() != b"authored problem\n"


def test_a_scaffold_plan_refuses_to_overwrite_a_concurrent_change(
    tmp_path: Path,
) -> None:
    """A target changed after planning remains byte-for-byte unchanged."""
    folder = tmp_path / "my-problem"
    scaffold(folder, CORE_KINDS)
    plan = plan_scaffold(folder, CORE_KINDS, force=True)
    problem = folder / "problem.yml"
    problem.write_bytes(b"concurrent problem\n")

    with pytest.raises(ValueError, match="scaffold target changed after planning"):
        apply_scaffold(plan)

    assert problem.read_bytes() == b"concurrent problem\n"
    assert not (folder / ".gnomon-backup").exists()


def test_a_forced_scaffold_refuses_to_overwrite_an_existing_backup(
    tmp_path: Path,
) -> None:
    """A second force cannot replace the only recoverable copy from the first force."""
    folder = tmp_path / "my-problem"
    scaffold(folder, CORE_KINDS)
    scaffold(folder, CORE_KINDS, force=True)
    current = (folder / "problem.yml").read_bytes()

    with pytest.raises(ValueError, match="backup already exists"):
        scaffold(folder, CORE_KINDS, force=True)

    assert (folder / "problem.yml").read_bytes() == current


def test_init_force_dry_run_enumerates_changes_without_writing(tmp_path: Path) -> None:
    """The force preview is repeatable and leaves both records and backups absent."""
    folder = tmp_path / "my-problem"
    scaffold(folder, CORE_KINDS)
    problem = folder / "problem.yml"
    problem.write_text("authored\n", encoding="utf-8")
    before = {path: path.read_bytes() for path in folder.iterdir() if path.is_file()}
    runner = CliRunner()

    first = runner.invoke(app, ["init", str(folder), "--force", "--dry-run"])
    second = runner.invoke(app, ["init", str(folder), "--force", "--dry-run"])

    assert first.exit_code == second.exit_code == 0
    assert first.output == second.output
    for name in [*(f"{kind}.yml" for kind in CORE_KINDS), "_index.md"]:
        line = next(line for line in first.output.splitlines() if name in line)
        assert "would overwrite" in line
    assert {path: path.read_bytes() for path in folder.iterdir() if path.is_file()} == before
    assert not (folder / ".gnomon-backup").exists()

    fresh = tmp_path / "fresh"
    preview = runner.invoke(app, ["init", str(fresh), "--force", "--dry-run"])
    assert preview.exit_code == 0 and not fresh.exists()


def test_init_force_requires_confirmation_and_preserves_declined_files(
    tmp_path: Path,
) -> None:
    """Declining the overwrite prompt leaves the authored record unchanged."""
    folder = tmp_path / "my-problem"
    scaffold(folder, CORE_KINDS)
    problem = folder / "problem.yml"
    problem.write_text("authored\n", encoding="utf-8")

    result = CliRunner().invoke(app, ["init", str(folder), "--force"], input="n\n")

    assert result.exit_code == 1
    assert problem.read_text(encoding="utf-8") == "authored\n"
    assert not (folder / ".gnomon-backup").exists()


def test_init_force_confirmation_preserves_then_replaces_files(tmp_path: Path) -> None:
    """Confirming force writes templates only after preserving the prior bytes."""
    folder = tmp_path / "my-problem"
    scaffold(folder, CORE_KINDS)
    problem = folder / "problem.yml"
    problem.write_text("authored\n", encoding="utf-8")

    result = CliRunner().invoke(app, ["init", str(folder), "--force"], input="y\n")

    assert result.exit_code == 0
    assert (folder / ".gnomon-backup" / "problem.yml.bak").read_text(
        encoding="utf-8"
    ) == "authored\n"
    assert problem.read_text(encoding="utf-8") != "authored\n"


def test_a_later_kind_joins_a_folder_that_holds_records(tmp_path: Path) -> None:
    """The missing templates are written and registered under their stage, and every file and
    every entry that the researcher wrote stays as it stands."""
    folder = tmp_path / "my-problem"
    scaffold(folder, CORE_KINDS)
    (folder / "problem.yml").write_text("filled\n", encoding="utf-8")
    index = folder / "_index.md"
    edited = (
        index.read_text(encoding="utf-8") + "- [Second key](key-b.yml): pairs a second feature\n"
    )
    index.write_text(edited, encoding="utf-8")
    outcome = scaffold(folder, [*CORE_KINDS, "answer", "binding"])
    assert [p.name for p in outcome.written] == ["binding.yml", "answer.yml"]
    assert outcome.index_state == "updated"
    assert (folder / "problem.yml").read_text(encoding="utf-8") == "filled\n"
    text = index.read_text(encoding="utf-8")
    assert "(key-b.yml)" in text and text.startswith(edited.split("\n## ", 1)[0])
    stage = template_entries()["answer"].stage
    assert text.index(f"## {stage}") < text.index("(answer.yml)")
    assert text.count("(answer.yml)") == 1 and text.count("(binding.yml)") == 1
    assert scaffold(folder, [*CORE_KINDS, "answer", "binding"]).index_state == "kept"


def test_the_commands_exit_with_the_status_of_their_findings(planted: Path, tmp_path: Path) -> None:
    runner = CliRunner()
    assert runner.invoke(app, ["check", str(EXAMPLES)]).exit_code == 0
    result = runner.invoke(
        app,
        [
            "check",
            str(planted),
            "--format",
            "yaml",
            "--output",
            str(tmp_path / "r.yml"),
        ],
    )
    assert result.exit_code == 1 and (tmp_path / "r.yml").is_file()
    assert runner.invoke(app, ["init", str(tmp_path / "new")]).exit_code == 0
    again = runner.invoke(app, ["init", str(tmp_path / "new"), "--with", "answer"])
    assert again.exit_code == 0 and "answer.yml: written" in again.output
    assert f"{len(CORE_KINDS)} existing files kept" in again.output
    assert runner.invoke(app, ["init", str(tmp_path / "new"), "--with", "nonsense"]).exit_code == 1


def test_a_template_not_yet_filled_is_listed_apart_and_not_checked(
    tmp_path: Path,
) -> None:
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


def test_the_scaffold_opens_the_itinerary_and_follows_the_stages(
    tmp_path: Path,
) -> None:
    """The itinerary opens with the problem; a requested question joins the next stage."""
    entries = template_entries()
    order = list(entries)
    assert order[0] == "itinerary" and order.index("question") < order.index("target-system")
    assert entries["question"].stage.startswith("2.") and entries["answer"].stage.startswith("5.")
    folder = tmp_path / "my-problem"
    scaffold(folder, CORE_KINDS)
    index = (folder / "_index.md").read_text(encoding="utf-8")
    assert index.index("## Throughout the inquiry") < index.index("## 1. Problem")
    assert "## 2. Question schema" not in index

    scaffold(folder, [*CORE_KINDS, "question"])
    updated = (folder / "_index.md").read_text(encoding="utf-8")
    assert updated.index("## 1. Problem") < updated.index("## 2. Question schema")


def test_a_required_block_whose_fields_are_all_empty_fails_its_requirement() -> None:
    from gnomon.completeness import unmet_general

    empty = {"construction": {"procedure": None, "reading": ""}}
    assert [f.text for f in unmet_general(empty, ["construction"])] == [
        "always required: construction"
    ]
    assert (
        unmet_general(
            {"construction": {"procedure": "design.a.b", "reading": ""}},
            ["construction"],
        )
        == []
    )
