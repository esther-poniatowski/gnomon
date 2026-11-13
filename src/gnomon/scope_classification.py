"""Classify completeness findings by the stage at which they become due.

The ordinary checking pipeline reports every defect visible in the records that
exist.  This module applies a selected validation scope to those reports and
adds record-existence requirements.  Integrity and consistency defects remain
current; incomplete content required only by a later stage becomes future
work.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path, PurePosixPath
from typing import Any, Mapping, Protocol, Sequence

from . import completeness as c
from .findings import COMPLETENESS_UNMET_SCOPE, Finding, finding
from .sarif import Located


class ProblemView(Protocol):
    """The problem data needed to classify scoped findings."""

    @property
    def folder(self) -> Path:
        """The folder that owns the problem."""

    @property
    def records(self) -> Mapping[str, Mapping[str, Any]]:
        """The records keyed by identifier."""

    def of_kind(self, kind: str) -> list[Mapping[str, Any]]:
        """Return the records of one kind."""


class WorkspaceView(Protocol):
    """The workspace data needed to classify scoped findings."""

    @property
    def root(self) -> Path:
        """The workspace root."""

    @property
    def problems(self) -> Sequence[ProblemView]:
        """The problems represented by started records."""

    @property
    def unfilled(self) -> Sequence[Path]:
        """The unfilled record templates."""

    @property
    def leftovers(self) -> Mapping[str, tuple[Finding, ...]]:
        """The template leftovers keyed by record identifier."""

    @property
    def by_id(self) -> Mapping[str, Mapping[str, Any]]:
        """Every record keyed by identifier."""


class ScopeRegistries(Protocol):
    """The registries that define validation scopes and result types."""

    @property
    def classes(self) -> Mapping[str, str]:
        """The class of each result type."""

    @property
    def holders(self) -> Mapping[str, frozenset[str]]:
        """The record kinds that can hold each result type."""

    @property
    def scopes(self) -> tuple[str, ...]:
        """The ordered validation scopes."""

    @property
    def by_scope(self) -> Mapping[str, Mapping[str, Any]]:
        """The requirements declared by scope."""


@dataclass(frozen=True)
class FutureWork:
    """One unmet requirement that becomes due only at a later validation scope."""

    due_scope: str
    file: PurePosixPath
    record: str | None
    kind: str
    path: str
    message: str


@dataclass(frozen=True)
class CheckResult:
    """The current findings and later work produced by one scoped check."""

    findings: tuple[Located, ...]
    future_work: tuple[FutureWork, ...] = ()


@dataclass(frozen=True)
class _ProblemRecords:
    """The records relevant to one folder, including an empty template folder."""

    folder: Path
    records: Mapping[str, Mapping[str, Any]]

    def of_kind(self, kind: str) -> list[Mapping[str, Any]]:
        """Return the records of one kind, ordered by identifier."""
        return [record for _, record in sorted(self.records.items()) if record.get("type") == kind]


_DEFERABLE_RULES = frozenset(
    {
        "completeness/incomplete-operation",
        "completeness/incomplete-realization",
        "completeness/template-leftover",
        "completeness/unmet-aim",
        "completeness/unmet-by-value",
        "completeness/unmet-commitment",
        "completeness/unmet-requirement",
        "completeness/unmet-scope",
    }
)


def scope_path_findings(
    record: Mapping[str, Any],
    problem: ProblemView,
    workspace: WorkspaceView,
    registries: ScopeRegistries,
    scope: str | None,
) -> list[Finding]:
    """Return the explicit field and state requirements declared by every scope."""
    if scope is None:
        return []
    kind = str(record.get("type"))
    leftovers = {found.locus for found in workspace.leftovers.get(str(record.get("id")), ())}
    found: list[Finding] = []
    for due_scope, entry in registries.by_scope.items():
        tables: list[Mapping[str, list[str]]] = [entry.get("required") or {}]
        for condition, table in (entry.get("when_record_present") or {}).items():
            if problem.of_kind(str(condition)):
                tables.append(table)
        candidate_class = _candidate_class(record, problem, workspace, registries)
        if candidate_class is not None:
            tables.append((entry.get("by_candidate") or {}).get(candidate_class) or {})
        for table in tables:
            scoped = c.unmet_general(
                record,
                list(table.get(kind) or []),
                label=f"scope {due_scope} requires",
                rule=COMPLETENESS_UNMET_SCOPE,
            )
            found += [item for item in scoped if item.locus not in leftovers]
        found += _minimum_state_findings(record, kind, due_scope, entry)
    return found


def _candidate_class(
    record: Mapping[str, Any],
    problem: ProblemView,
    workspace: WorkspaceView,
    registries: ScopeRegistries,
) -> str | None:
    """Return the answer or construct class relevant to one record."""
    kind = str(record.get("type"))
    if kind == "question":
        expected = _candidate_kinds(problem, registries)
        return "answer" if expected == {"answer"} else "construct"
    if kind == "assessment":
        candidate = workspace.by_id.get(str(record.get("assesses"))) or {}
        if candidate:
            return "answer" if candidate.get("type") == "answer" else "construct"
    return None


def _minimum_state_findings(
    record: Mapping[str, Any],
    kind: str,
    scope: str,
    entry: Mapping[str, Any],
) -> list[Finding]:
    """Return commitment, identification, and settled-state findings for one scope."""
    found: list[Finding] = []
    minimum = (entry.get("minimum_commitment") or {}).get(kind)
    actual = str(record.get("commitment") or "")
    if minimum and (
        actual not in c.COMMITMENT_LEVELS
        or c.COMMITMENT_LEVELS.index(actual) < c.COMMITMENT_LEVELS.index(minimum)
    ):
        found.append(
            finding(
                COMPLETENESS_UNMET_SCOPE,
                f"scope {scope} requires commitment {minimum}",
                "commitment",
                value=scope,
            )
        )
    if kind == "question" and entry.get("minimum_subject_slots") == "identified":
        subject = record.get("subject") or {}
        for slot in ("target_system", "phenomenon"):
            if isinstance(subject.get(slot), Mapping):
                found.append(
                    finding(
                        COMPLETENESS_UNMET_SCOPE,
                        f"scope {scope} requires an identified {slot.replace('_', ' ')}",
                        "subject",
                        slot,
                        value=scope,
                    )
                )
    for block in (entry.get("settled") or {}).get(kind) or []:
        if _has_unsettled_verdict(c.at(record, block)):
            found.append(
                finding(
                    COMPLETENESS_UNMET_SCOPE,
                    f"scope {scope} requires every verdict under {block} to be settled",
                    *block.split("."),
                    value=scope,
                )
            )
    return found


def _has_unsettled_verdict(node: Any) -> bool:
    """Return whether a nested block contains a pending or inconclusive verdict."""
    if isinstance(node, Mapping):
        if node.get("verdict") in {"pending", "inconclusive"}:
            return True
        return any(_has_unsettled_verdict(value) for value in node.values())
    if isinstance(node, list):
        return any(_has_unsettled_verdict(value) for value in node)
    return False


def classify_scope(
    workspace: WorkspaceView,
    registries: ScopeRegistries,
    scope: str | None,
    raw: Sequence[Located],
) -> CheckResult:
    """Partition raw findings and add missing-record work for one optional scope."""
    validate_scope(scope, registries)
    if scope is None:
        return CheckResult(tuple(raw))
    return _ScopeClassifier(workspace, registries, scope).classify(raw)


def future_record_requirements(
    workspace: WorkspaceView,
    registries: ScopeRegistries,
    scope: str,
) -> tuple[FutureWork, ...]:
    """Return absent record kinds first required after ``scope``."""
    validate_scope(scope, registries)
    return _ScopeClassifier(workspace, registries, scope).classify(()).future_work


def validate_scope(scope: str | None, registries: ScopeRegistries) -> None:
    """Reject a scope that is absent from the declared validation sequence."""
    if scope is not None and scope not in registries.scopes:
        admitted = ", ".join(registries.scopes)
        raise ValueError(f"unknown validation scope {scope!r}; expected one of {admitted}")


@dataclass
class _Partition:
    """The mutable output accumulated by one scoped classification."""

    current: list[Located]
    future: list[FutureWork]


# pylint: disable-next=too-few-public-methods  # one public classification operation
class _ScopeClassifier:
    """Apply one validation scope consistently across all workspace findings."""

    def __init__(
        self,
        workspace: WorkspaceView,
        registries: ScopeRegistries,
        scope: str,
    ) -> None:
        self.workspace = workspace
        self.registries = registries
        self.scope = scope
        self.selected = registries.scopes.index(scope)
        self.activation_scopes = _activation_scopes(registries)
        self.path_scopes = _path_scopes(registries)
        self.partition = _Partition([], [])

    def classify(self, raw: Sequence[Located]) -> CheckResult:
        """Return current findings and ordered, unique future work."""
        for located in raw:
            due_scope = self._due_scope(located)
            if due_scope is not None and self._is_later(due_scope):
                self.partition.future.append(self._future_item(located, due_scope))
            else:
                self.partition.current.append(located)
        self._add_missing_record_work()
        return CheckResult(tuple(self.partition.current), self._ordered_future_work())

    def _ordered_future_work(self) -> tuple[FutureWork, ...]:
        """Return future work in inquiry order without duplicate requirements."""
        order = {name: index for index, name in enumerate(self.registries.scopes)}
        unique = {
            (item.due_scope, item.file, item.record, item.path, item.message): item
            for item in self.partition.future
        }
        ordered = sorted(
            unique.values(),
            key=lambda item: (
                order[item.due_scope],
                str(item.file),
                item.record or "",
                item.path,
                item.message,
            ),
        )
        return tuple(ordered)

    def _due_scope(self, located: Located) -> str | None:
        """Return the first scope at which one deferable finding becomes current."""
        if located.finding.rule.id not in _DEFERABLE_RULES or located.record is None:
            return None
        record = self.workspace.by_id.get(located.record) or {}
        kind = str(record.get("type") or "")
        activation = self.activation_scopes.get(kind)
        handled, due_scope = self._rule_due_scope(located, record, activation)
        if handled:
            return due_scope
        return self._path_due_scope(located.finding, kind, activation)

    def _rule_due_scope(
        self,
        located: Located,
        record: Mapping[str, Any],
        activation: str | None,
    ) -> tuple[bool, str | None]:
        """Resolve rules whose due scope does not follow their visible field path."""
        rule = located.finding.rule.id
        if rule == "completeness/unmet-scope":
            discriminator = located.finding.discriminator
            if discriminator in self.registries.scopes:
                return True, discriminator
        if rule == "completeness/unmet-aim":
            full_path = located.finding.discriminator.split("/", 1)[0]
            target_kind, _, path = full_path.partition(".")
            return True, self.path_scopes.get((target_kind, path), activation)
        if rule == "completeness/unmet-commitment":
            return True, activation
        if rule == "completeness/template-leftover" and record.get("commitment") == "specified":
            return True, activation
        return False, None

    def _path_due_scope(
        self,
        found: Finding,
        kind: str,
        activation: str | None,
    ) -> str | None:
        """Resolve a finding from the earliest scope that declares its field path."""
        path = _finding_path(found)
        exact = self.path_scopes.get((kind, path))
        if exact is not None:
            return exact
        prefixes = [
            (candidate, due)
            for (record_kind, candidate), due in self.path_scopes.items()
            if record_kind == kind and (path == candidate or path.startswith(candidate + "."))
        ]
        if prefixes:
            return min(
                prefixes,
                key=lambda item: self.registries.scopes.index(item[1]),
            )[1]
        return activation

    def _future_item(self, located: Located, due_scope: str) -> FutureWork:
        """Convert one later-stage completeness finding to computed future work."""
        record = self.workspace.by_id.get(located.record or "") or {}
        return FutureWork(
            due_scope,
            located.file,
            located.record,
            str(record.get("type") or "record"),
            located.finding.locus or "/",
            located.finding.text,
        )

    def _add_missing_record_work(self) -> None:
        """Add current and later record-existence requirements for every problem folder."""
        for problem in _problem_folders(self.workspace):
            existing = {str(record.get("type")) for record in problem.records.values()}
            aims = {
                str(c.at(question, "task.epistemic_aim"))
                for question in problem.of_kind("question")
                if c.at(question, "task.epistemic_aim")
            }
            for kind, due_scope in self._required_records(aims).items():
                if kind not in existing:
                    self._add_missing(problem, kind, due_scope)
            for kind in self.registries.by_scope[self.scope].get("checkpoint_records") or []:
                if kind not in existing:
                    self._add_missing(problem, str(kind), self.scope)
            self._add_candidate_work(problem)

    def _required_records(self, aims: set[str]) -> dict[str, str]:
        """Return each generally required record and its first due scope."""
        required: dict[str, str] = {}
        for due_scope, entry in self.registries.by_scope.items():
            for kind in entry.get("required_records") or []:
                required.setdefault(str(kind), due_scope)
            for kind, excluded in (entry.get("required_unless_aim") or {}).items():
                if not aims or not aims.issubset(set(excluded)):
                    required.setdefault(str(kind), due_scope)
        return required

    def _add_candidate_work(self, problem: ProblemView) -> None:
        """Add missing candidate and candidate-assessment requirements."""
        candidate_kinds = _candidate_kinds(problem, self.registries)
        candidates = [
            record for record in problem.records.values() if record.get("type") in candidate_kinds
        ]
        if not candidates:
            self._add_missing(
                problem,
                min(candidate_kinds),
                "candidate-proposed",
                label="candidate",
            )
        assessments = problem.of_kind("assessment")
        for candidate in candidates:
            ident = str(candidate.get("id"))
            if not any(record.get("assesses") == ident for record in assessments):
                self._add_missing(
                    problem,
                    "assessment",
                    "candidate-assessed",
                    label=f"assessment of {ident}",
                )

    def _add_missing(
        self,
        problem: ProblemView,
        kind: str,
        due_scope: str,
        *,
        label: str | None = None,
    ) -> None:
        """Place one missing record requirement in the current or later collection."""
        file = _expected_file(self.workspace, problem, kind)
        name = label or f"{kind} record"
        message = f"scope {due_scope} requires {name}"
        if not self._is_later(due_scope):
            self.partition.current.append(
                Located(finding(COMPLETENESS_UNMET_SCOPE, message, value=kind), file)
            )
        elif due_scope != self.scope:
            self.partition.future.append(FutureWork(due_scope, file, None, kind, "/", message))

    def _is_later(self, scope: str) -> bool:
        """Return whether a scope follows the selected scope."""
        return self.registries.scopes.index(scope) > self.selected


def _activation_scopes(registries: ScopeRegistries) -> dict[str, str]:
    """Return the first scope that applies ordinary requirements to each record kind."""
    activated: dict[str, str] = {}
    for scope, entry in registries.by_scope.items():
        kinds = [
            *(entry.get("checkpoint_records") or []),
            *(entry.get("required_records") or []),
            *(entry.get("activate_when_present") or []),
            *(entry.get("required_unless_aim") or {}),
        ]
        for kind in kinds:
            activated.setdefault(str(kind), scope)
    return activated


def _path_scopes(registries: ScopeRegistries) -> dict[tuple[str, str], str]:
    """Return the first scope that declares each explicit record path."""
    declared: dict[tuple[str, str], str] = {}
    for scope, entry in registries.by_scope.items():
        tables: list[Mapping[str, list[str]]] = [
            entry.get("required") or {},
            entry.get("on_demand") or {},
            entry.get("settled") or {},
        ]
        for key in ("by_aim", "by_candidate", "when_record_present"):
            tables.extend((entry.get(key) or {}).values())
        for table in tables:
            for kind, paths in table.items():
                for path in paths:
                    declared.setdefault((str(kind), str(path)), scope)
        for kind in entry.get("minimum_commitment") or {}:
            declared.setdefault((str(kind), "commitment"), scope)
        if entry.get("minimum_subject_slots") == "identified":
            for path in ("subject.target_system", "subject.phenomenon"):
                declared.setdefault(("question", path), scope)
    return declared


def _finding_path(found: Finding) -> str:
    """Return a registry-style path for the visible part of a finding locus."""
    parts: list[str] = []
    for segment in found.path:
        if isinstance(segment, int):
            if parts:
                parts[-1] += "[]"
        else:
            parts.append(segment)
    return ".".join(parts)


def _candidate_kinds(problem: ProblemView, registries: ScopeRegistries) -> frozenset[str]:
    """Return the record kinds that can satisfy the candidate demand of one problem."""
    kinds: set[str] = set()
    for demand in problem.of_kind("problem"):
        result_type = str(demand.get("result_type") or "")
        if registries.classes.get(result_type) == "construct":
            kinds.update(registries.holders.get(result_type) or ())
        else:
            kinds.add("answer")
    return frozenset(kinds or {"answer"})


def _problem_folders(workspace: WorkspaceView) -> list[_ProblemRecords]:
    """Return every folder represented by a started record or an unfilled template."""
    by_folder = {
        problem.folder: _ProblemRecords(problem.folder, problem.records)
        for problem in workspace.problems
    }
    for path in workspace.unfilled:
        by_folder.setdefault(path.parent, _ProblemRecords(path.parent, {}))
    if not by_folder:
        by_folder[workspace.root] = _ProblemRecords(workspace.root, {})
    return [by_folder[path] for path in sorted(by_folder)]


def _expected_file(workspace: WorkspaceView, problem: ProblemView, kind: str) -> PurePosixPath:
    """Return the project-relative path at which a missing record would be created."""
    return PurePosixPath((problem.folder / f"{kind}.yml").relative_to(workspace.root).as_posix())
