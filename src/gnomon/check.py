"""
Every check of the records of a workspace, run together on a user's directory.

A workspace is a directory tree of records. Each folder that holds records is one problem, whose
records are checked together, as the worked inquiries are: a question against its phenomenon and
its target system, an answer against the records that it can see, an assessment against the answer
that it assesses. A reference may reach any record of the workspace, so a problem can cite a record
held in another folder.

This module only orchestrates. Each check lives in the module that owns its rule:
:mod:`gnomon.vocabulary`, :mod:`gnomon.completeness`, :mod:`gnomon.itineraries`,
:mod:`gnomon.derivations` or :mod:`gnomon.dimensions`. A generated
record, such as the symbol table that ``gnomon vocabulary`` writes, is not checked, and neither is a
template not yet filled, whose identifier is still the placeholder of its template: a researcher
fills the records stage by stage, so a template of a later stage is listed apart, not reported.

Classes
-------
Problem
    The records of one folder, keyed by identifier, with the file of each.
Workspace
    The problems of a directory tree, and the files that could not be read.

Functions
---------
parse_file
    Return the content of a YAML file, or the line that reports why it cannot be read.
load_workspace
    Read the records of a directory tree, folder by folder.
check_workspace
    Run every check on a workspace and return its findings, each placed in its file and record.
"""

from __future__ import annotations

import re
from dataclasses import dataclass, field
from functools import cached_property
from pathlib import Path, PurePosixPath
from typing import Any, Callable, Iterable, Mapping

import yaml

from . import completeness as c
from . import vocabulary as v
from .answerability import malformed_answerability
from .derivations import derivation_problems
from .dimensions import (
    FORMULA_BLOCKS,
    Scope,
    base_dimensions,
    declared_formulas,
    dimension_problems,
    malformed_formulas,
    operator_rules,
)
from .findings import CHECK_FAILED, Finding, finding
from .history import StateReader, git_states
from .itineraries import construct_record_kinds, itinerary_problems, type_classes, type_holders
from .sarif import Located

#: The kinds of record that a tool generates from the others, which no check reads.
GENERATED_KINDS = frozenset({"vocabulary", "view"})

#: A segment of an identifier that is still the placeholder of a template, such as ``TOPIC``.
PLACEHOLDER_SEGMENT = re.compile(r"(?:^|\.)[A-Z][A-Z0-9_]*(?:\.|$)")

Records = Mapping[str, Mapping[str, Any]]


@dataclass(frozen=True)
class Problem:
    """The records of one folder, keyed by identifier, with the file of each.

    Attributes
    ----------
    folder : Path
        The folder that holds the records.
    records : dict
        The records of the folder, keyed by identifier.
    files : dict
        The file of each record, keyed by identifier.
    """

    folder: Path
    records: dict[str, Mapping[str, Any]]
    files: dict[str, Path]

    def of_kind(self, kind: str) -> list[Mapping[str, Any]]:
        """Return the records of one kind, in the order of their identifiers."""
        return [r for _, r in sorted(self.records.items()) if r.get("type") == kind]


@dataclass(frozen=True)
class Workspace:
    """The problems of a directory tree, and the files that could not be read.

    Attributes
    ----------
    root : Path
        The directory read.
    problems : tuple of Problem
        One problem per folder that holds records, in the order of the folders.
    failures : tuple of str
        One line per file that could not be read or parsed.
    unfilled : tuple of Path
        The files whose record is still a template, which no check reads.
    """

    root: Path
    problems: tuple[Problem, ...]
    failures: tuple[str, ...] = ()
    unfilled: tuple[Path, ...] = ()

    @cached_property
    def by_id(self) -> dict[str, Mapping[str, Any]]:
        """Every record of the workspace, keyed by identifier."""
        return {
            ident: record for problem in self.problems for ident, record in problem.records.items()
        }

    @cached_property
    def files(self) -> dict[str, Path]:
        """The file of every record of the workspace, keyed by identifier."""
        return {ident: path for problem in self.problems for ident, path in problem.files.items()}

    @cached_property
    def states(self) -> StateReader:
        """A reader of the records of the workspace at a revision of their repository."""
        return git_states(self.files)


def parse_file(path: Path) -> tuple[Any, str | None]:
    """Return the content of a YAML file, or None and the line that reports why it cannot be read.

    The line names the file and the error, so that a command lists each unreadable file apart.
    """
    try:
        return yaml.safe_load(path.read_text(encoding="utf-8")), None
    except (OSError, ValueError, yaml.YAMLError) as error:
        return None, f"{path}: {error}"


def load_workspace(root: Path) -> Workspace:
    """Read the records of a directory tree, folder by folder.

    A file that does not parse is reported and skipped, so the other records are still checked. A
    file that holds no mapping with an identifier and a type is not a record, and a generated
    record is left out.
    """
    folders: dict[Path, Problem] = {}
    failures: list[str] = []
    unfilled: list[Path] = []
    for path in sorted(root.rglob("*.yml")):
        if any(part.startswith(".") for part in path.relative_to(root).parts):
            continue
        record, failure = parse_file(path)
        if failure is not None:
            failures.append(failure)
            continue
        if not isinstance(record, Mapping) or "id" not in record or "type" not in record:
            continue
        if record.get("type") in GENERATED_KINDS:
            continue
        if PLACEHOLDER_SEGMENT.search(str(record["id"])):
            unfilled.append(path)
            continue
        problem = folders.setdefault(path.parent, Problem(path.parent, {}, {}))
        problem.records[str(record["id"])] = record
        problem.files[str(record["id"])] = path
    return Workspace(
        root, tuple(folders[f] for f in sorted(folders)), tuple(failures), tuple(unfilled)
    )


@dataclass
# pylint: disable-next=too-many-instance-attributes  # one attribute per registry
class _Registries:
    """The registries that the checks read, loaded once per run."""

    canonical: frozenset[str] = field(default_factory=v.canonical_operators)
    by_aim: dict[str, dict[str, list[str]]] = field(default_factory=c.requirements_by_aim)
    by_commitment: dict[str, dict[str, list[str]]] = field(
        default_factory=c.requirements_by_commitment
    )
    by_presence: dict[str, Any] = field(default_factory=c.requirements_by_presence)
    by_value: dict[str, Any] = field(default_factory=c.requirements_by_value)
    blocks: dict[str, list[str]] = field(default_factory=c.block_requirements)
    kinds: list[str] = field(default_factory=c.record_kinds)
    slot_types: frozenset[str] = field(default_factory=c.placeholder_types)
    aims: dict[str, frozenset[str]] = field(default_factory=c.result_aims)
    occurrences: dict[str, list[str]] = field(default_factory=c.occurrence_by_category)
    constructs: frozenset[str] = field(default_factory=construct_record_kinds)
    classes: dict[str, str] = field(default_factory=type_classes)
    holders: dict[str, frozenset[str]] = field(default_factory=type_holders)
    admitted: dict[str, dict[str, frozenset[str]]] = field(default_factory=dict)

    def admitted_values(self, kind: str) -> dict[str, frozenset[str]]:
        """Return the admitted values of the closed fields of one kind, read once."""
        if kind not in self.admitted:
            self.admitted[kind] = c.admitted_values(kind)
        return self.admitted[kind]


@dataclass(frozen=True)
class _Context:
    """What a check of one record may read: its problem, the workspace and the registries."""

    problem: Problem
    workspace: Workspace
    registries: _Registries

    @cached_property
    def operators(self) -> frozenset[str]:
        """The operators that every record of the problem may use."""
        local = {op for record in self.problem.records.values() for op in v.local_operators(record)}
        return self.registries.canonical | frozenset(local)

    @cached_property
    def symbols(self) -> list[str]:
        """Every symbol that a record of the problem declares."""
        return [
            d.symbol for record in self.problem.records.values() for d in v.declarations(record)
        ]

    @cached_property
    def bases(self) -> frozenset[str]:
        """The base dimensions of the package and the base scales that the problem declares."""
        scales = {
            str(entry.get("symbol"))
            for record in self.problem.of_kind("operators")
            for entry in record.get("base_scales") or []
            if isinstance(entry, Mapping) and entry.get("symbol")
        }
        return base_dimensions() | frozenset(scales)

    @cached_property
    def dimension_rules(self) -> dict[str, str]:
        """The rule of dimension of each operator that the problem may use."""
        local = {
            str(op.get("symbol")): str(op.get("dimension"))
            for record in self.problem.of_kind("operators")
            for op in record.get("operators") or []
            if isinstance(op, Mapping) and op.get("symbol") and op.get("dimension")
        }
        return {**operator_rules(), **local}

    @cached_property
    def declares_formulas(self) -> bool:
        """Whether some quantity or index set of the problem declares a dimensional formula."""
        return any(
            isinstance(entry, Mapping) and entry.get("dimensional_formula") is not None
            for record in self.problem.records.values()
            for block in FORMULA_BLOCKS
            for entry in record.get(block) or []
        )

    @cached_property
    def arities(self) -> dict[str, int]:
        """The number of arguments of each operator that the problem may use."""
        return v.arities(*self.problem.records.values())

    @cached_property
    def produced(self) -> dict[str, set[str]]:
        """Per record kind, the paths that the aims of the questions of the problem produce."""
        found: dict[str, set[str]] = {}
        for question in self.problem.of_kind("question"):
            aim = str(c.at(question, "task.epistemic_aim"))
            for path in (self.registries.by_aim.get(aim) or {}).get("to_produce", []):
                kind, _, rest = path.partition(".")
                found.setdefault(kind, set()).add(rest)
        return found

    def record(self, ident: Any) -> Mapping[str, Any]:
        """Return the record of the workspace that carries ``ident``, or an empty mapping."""
        return self.workspace.by_id.get(str(ident), {}) if ident else {}

    def target_of(self, record: Mapping[str, Any]) -> Mapping[str, Any]:
        """Return the target system that a record is stated against, through its question for an
        answer."""
        upstream = v.upstream_of(record, self.workspace.by_id)
        if upstream:
            return upstream
        if record.get("type") == "answer":
            question = self.record(record.get("answers"))
            return self.record(c.at(question, "subject.target_system"))
        targets = self.problem.of_kind("target-system")
        return targets[0] if len(targets) == 1 else {}


Check = Callable[[Mapping[str, Any], _Context], list[Finding]]


def _symbols(record: Mapping[str, Any], ctx: _Context) -> list[Finding]:
    """Resolve the symbols and the operators of a record against the records that it can see."""
    kind = record.get("type")
    if kind in ("operators", "question"):
        external: Iterable[str] = ctx.symbols
    elif kind in ("answer", "model", "binding", "derivation"):
        external = [
            d.symbol
            for seen in v.visible_records(record, ctx.workspace.by_id)
            for d in v.declarations(seen)
        ]
    else:
        external = [d.symbol for d in v.declarations(v.upstream_of(record, ctx.workspace.by_id))]
    return v.unresolved(record, ctx.operators, external)


def _structure(record: Mapping[str, Any], _ctx: _Context) -> list[Finding]:
    """The checks of the declarations of a record that need no other record."""
    return (
        v.mistyped_symbols(record)
        + v.repeated_symbols(record)
        + c.undecided_boundaries(record)
        + v.misplaced_sharing(record)
        + v.vacuous_shared(record)
        + v.unfixed_parameters(record)
        + v.doubly_defined(record)
        + v.unowned_quantities(record)
        + v.unselected_conditions(record)
        + v.malformed_relations(record)
        + v.split_expressions(record)
        + v.corrupted_notation(record)
    )


def _against_target(record: Mapping[str, Any], ctx: _Context) -> list[Finding]:
    """The checks of a record against the target system that it is stated against."""
    upstream = v.upstream_of(record, ctx.workspace.by_id)
    target = ctx.target_of(record)
    backgrounds = [
        r
        for r in ctx.workspace.by_id.values()
        if r.get("type") == "background" and r.get("describes") == record.get("id")
    ]
    found = (
        v.unordered_interactions(record, upstream)
        + v.overreaching_declarations(record, upstream)
        + v.misrouted_interactions(record, upstream)
        + v.misnamed_variant(record, v.declared_variants(target))
        + v.mismatched_arity(record, ctx.arities)
        + v.unborne_variants(record, backgrounds)
    )
    if record.get("type") in ("phenomenon", "answer"):
        found += v.overreaching_entries(record, v.variant_symbols(target))
    return found


def _requirements(record: Mapping[str, Any], ctx: _Context) -> list[Finding]:
    """The specifications that every record of a kind carries, those that a value of a field
    imposes, and those of its commitment."""
    kind = str(record.get("type"))
    if kind not in ctx.registries.kinds:
        return []
    produced = ctx.produced.get(kind, set())
    found = c.unmet_general(record, c.always_required(kind), produced)
    found += c.unmet_by_value(record, ctx.registries.by_value, produced)
    if kind in ("target-system", "phenomenon"):
        found += c.unmet_commitment(record, ctx.registries.by_commitment, produced)
    return found


def _question(record: Mapping[str, Any], ctx: _Context) -> list[Finding]:
    """The checks of a question against its problem, its phenomenon and its target system."""
    phenomenon = ctx.record(c.at(record, "subject.phenomenon"))
    target = ctx.record(c.at(record, "subject.target_system"))
    reached = {"question": record, "phenomenon": phenomenon, "target-system": target}
    records = {**ctx.workspace.by_id, **ctx.problem.records}
    return (
        c.malformed_restrictions(record, c.varying_symbols(target, phenomenon))
        + c.unjustified_explanans_bound(record)
        + c.unstated_standing(record)
        + c.contradictory_accuracy(record)
        + c.unresolved_slots(record, records, ctx.registries.slot_types)
        + c.unresolved_question_references(record, records)
        + c.unstated_function_sense(record)
        + c.unbounded_aim(record, records, ctx.registries.aims)
        + c.unmet_by_aim(record, reached, ctx.registries.by_aim)
        + malformed_answerability(record, records)
        + c.unanchored_explicandum(record, records)
    )


def _answer(record: Mapping[str, Any], ctx: _Context) -> list[Finding]:
    """The checks of an answer: its operations, its block, its binding and its status pairs."""
    by_id = ctx.workspace.by_id
    found = (
        c.unclassified_operations(record, by_id)
        + c.unbound_outputs(record, ctx.record(record.get("answers")), by_id)
        + c.mismatched_status_pairs(record, by_id)
    )
    for block, paths in ctx.registries.blocks.items():
        if c.at(record, block) is not None:
            found += c.unmet_general(record, [f"{block}.{path}" for path in paths])
    return found


def _model(record: Mapping[str, Any], ctx: _Context) -> list[Finding]:
    """The checks of a model: retired symbols, its operations and the requirements of its
    parents."""
    return (
        v.retired_in_use(record)
        + c.incomplete_operations(record)
        + c.unmet_by_presence(record, ctx.registries.by_presence)
    )


def _assessment(record: Mapping[str, Any], ctx: _Context) -> list[Finding]:
    """The checks of an assessment: its credence, what it assesses, and its appraisal."""
    records = {**ctx.workspace.by_id, **ctx.problem.records}
    return (
        c.malformed_credence(record)
        + c.misdirected_assessment(record, records, ctx.registries.constructs)
        + c.premature_appraisal(record)
    )


def _phenomenon(record: Mapping[str, Any], ctx: _Context) -> list[Finding]:
    """The occurrence class of a phenomenon against its category."""
    return c.mismatched_occurrence(record, ctx.registries.occurrences)


def _problem(record: Mapping[str, Any], ctx: _Context) -> list[Finding]:
    """The checks of a problem against the records that serve it."""
    records = {**ctx.workspace.by_id, **ctx.problem.records}
    reg = ctx.registries
    return (
        c.mismatched_request(record, records)
        + c.unsupported_outcome(record, records, reg.classes, reg.holders)
        + c.misstated_obstacles(record, records, reg.classes, reg.holders)
    )


#: The kinds of record whose quantities and laws carry dimensional formulas.
DIMENSIONED_KINDS = frozenset({"target-system", "background", "phenomenon", "model"})


def _dimensions(record: Mapping[str, Any], ctx: _Context) -> list[Finding]:
    """The dimensional formulas of a record, and the homogeneity of its laws and definitions,
    against the formulas of the records that it sees."""
    if record.get("type") not in DIMENSIONED_KINDS:
        return []
    by_id = ctx.workspace.by_id
    seen = [*v.visible_records(record, by_id), v.upstream_of(record, by_id), record]
    scope = Scope(
        declared_formulas([r for r in seen if r], ctx.bases),
        ctx.dimension_rules,
        ctx.declares_formulas,
    )
    return malformed_formulas(record, ctx.bases) + dimension_problems(record, scope)


def _derivation(record: Mapping[str, Any], _ctx: _Context) -> list[Finding]:
    """The units, the interpretations, the orientations, the kernel and the slots of a
    derivation."""
    return derivation_problems(record)


def _itinerary(record: Mapping[str, Any], ctx: _Context) -> list[Finding]:
    """The steps of an itinerary against the registries and the records that they name."""
    return itinerary_problems(
        record, {**ctx.workspace.by_id, **ctx.problem.records}, states=ctx.workspace.states
    )


def _every_record(record: Mapping[str, Any], ctx: _Context) -> list[Finding]:
    """The checks that every record undergoes: references and closed values."""
    return v.dangling_references(record, ctx.workspace.by_id) + c.inadmissible_values(
        record, ctx.registries.admitted_values(str(record.get("type")))
    )


#: The checks of each kind of record, in the order of their reports.
BY_KIND: Mapping[str, tuple[Check, ...]] = {
    "question": (_question,),
    "answer": (_answer,),
    "model": (_model,),
    "assessment": (_assessment,),
    "phenomenon": (_phenomenon,),
    "problem": (_problem,),
    "itinerary": (_itinerary,),
    "derivation": (_derivation,),
}


def check_workspace(workspace: Workspace) -> list[Located]:
    """Run every check on a workspace and return its findings, each placed in its file and record.

    The findings follow the order of the folders, then of the records within a folder, then of the
    checks, so that two runs on unchanged records report the same list.
    """
    registries = _Registries()
    found: list[Located] = []
    for problem in workspace.problems:
        ctx = _Context(problem, workspace, registries)
        for ident in sorted(problem.records):
            record = problem.records[ident]
            checks: list[Check] = [_every_record, _requirements]
            if record.get("type") in v.RECORD_KINDS:
                checks += [_symbols, _structure, _against_target, _dimensions]
            checks += list(BY_KIND.get(str(record.get("type")), ()))
            file = PurePosixPath(problem.files[ident].relative_to(workspace.root).as_posix())
            for run in checks:
                try:
                    results = run(record, ctx)
                # pylint: disable-next=broad-exception-caught  # a malformed record must not stop the other checks
                except Exception as error:
                    results = [
                        finding(
                            CHECK_FAILED,
                            f"{run.__name__.strip('_')}: stopped on {type(error).__name__}:"
                            f" {error}",
                            value=run.__name__,
                        )
                    ]
                found += [Located(f, file, ident) for f in results]
        unused = v.unused_declarations(problem.folder)
        for ident, f in unused:
            if ident in problem.files:
                found.append(
                    Located(
                        f,
                        PurePosixPath(problem.files[ident].relative_to(workspace.root).as_posix()),
                        ident,
                    )
                )
    return found
