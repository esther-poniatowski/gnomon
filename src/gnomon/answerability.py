"""
Diagnosis of the conditions of answerability of the questions of a workspace.

The theory of the conditions of answerability states eight conditions for obtaining an answer, on
two routes, with their dependencies, and the choice of the next act defines an open condition and a
ready act instance. This module computes them from the records:

- the state of each condition is read from the assertions of the question (its block
  ``answerability``), else from a field whose definition shows it, else it is ``not-established``;
- a condition is open when it is not established and every condition on which it depends is;
- each open condition lists the activities that act on it, from the registry of answerability, and
  an activity is ready when every input that it requires is held by a record that no failed step of
  an itinerary impeached;
- a step whose verdict is pending while its record is stabilized is listed, so that its norm is
  judged anew.

The judgment of the researcher is never replaced: a state that the records do not show stays
``not-established`` until the researcher asserts it with pointers.

Functions
---------
answerability_registry
    Read the registry of the conditions, their dependencies and their activities.
diagnose
    Return the diagnosis of every question of a set of records.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Mapping

import yaml

from . import completeness as c
from . import findings as rules
from .findings import Entry, Finding, finding
from .itineraries import Activity, activities, holds, product_types
from .propagation import Revision, revisions

#: The registry of the conditions of answerability.
REGISTRY = Path(__file__).parent / "data" / "registries" / "answerability.yml"

#: The routes of an answer, and the key under which a dependency holds on both.
ROUTES = ("selection", "construction")
BOTH = "both"

#: The evidential statuses of a phenomenon that refute the topic presupposition of a question.
REFUTING_STATUSES = frozenset({"absent", "disproved"})

#: The activities that revise after a refuted condition, as the choice of the next act lists them.
REVISIONS = ("question-revision", "problem-decomposition", "concept-revision")

Records = Mapping[str, Mapping[str, Any]]


def answerability_registry(source: Path | None = None) -> dict[str, Any]:
    """Read the registry of the conditions, their dependencies and their activities."""
    return yaml.safe_load((source or REGISTRY).read_text(encoding="utf-8")) or {}


@dataclass(frozen=True)
class ConditionState:
    """The state of one condition on one route, with what shows it."""

    condition: str
    state: str
    source: str
    pointers: tuple[str, ...] = ()


@dataclass(frozen=True)
class Act:
    """An activity that acts on an open condition, with its readiness."""

    activity: str
    ready: bool
    missing: tuple[str, ...] = ()
    conditional: bool = False


@dataclass(frozen=True)
class RouteDiagnosis:
    """The diagnosis of one route of one question."""

    route: str
    states: tuple[ConditionState, ...]
    open: dict[str, tuple[Act, ...]]
    refuted: tuple[str, ...]


@dataclass(frozen=True)
class QuestionDiagnosis:
    """The diagnosis of one question, route by route."""

    question: str
    routes: tuple[RouteDiagnosis, ...]


@dataclass
class Diagnosis:
    """The diagnosis of every question of a set of records, and the state of their itineraries."""

    questions: list[QuestionDiagnosis] = field(default_factory=list)
    revisions: list[Revision] = field(default_factory=list)
    impeached: set[str] = field(default_factory=set)
    conditional: set[str] = field(default_factory=set)
    judge_anew: list[str] = field(default_factory=list)


def routes_of(question: Mapping[str, Any]) -> tuple[str, ...]:
    """Return the routes on which a question is diagnosed: selection, and construction once named.

    >>> routes_of({}), routes_of({"construction": {"procedure": "design.a.b"}})
    (('selection',), ('selection', 'construction'))
    """
    named = (question.get("construction") or {}).get("procedure")
    return ROUTES if isinstance(named, str) and named.strip() else ROUTES[:1]


def conditions_on(
    route: str, dependencies: Mapping[str, Mapping[str, list[str]]]
) -> dict[str, list[str]]:
    """Return the conditions that apply on a route, each with the conditions on which it depends
    there."""
    return {
        condition: [*(table.get(BOTH) or []), *(table.get(route) or [])]
        for condition, table in dependencies.items()
        if BOTH in table or route in table
    }


def asserted(question: Mapping[str, Any], condition: str, route: str) -> ConditionState | None:
    """Return the state that the question asserts for a condition on a route, or None."""
    entries = [
        e
        for e in question.get("answerability") or []
        if isinstance(e, Mapping)
        and e.get("condition") == condition
        and e.get("route", BOTH) in (route, BOTH)
    ]
    for state in ("refuted", "established"):
        chosen = [e for e in entries if e.get("state") == state]
        if chosen:
            pointers = tuple(str(p) for e in chosen for p in e.get("pointers") or [])
            return ConditionState(condition, state, "asserted", pointers)
    return None


def derived(question: Mapping[str, Any], condition: str, records: Records) -> ConditionState | None:
    """Return the state that a field of the records shows for a condition, or None.

    Three fields show a state without an assertion: the evidential status of the phenomenon refutes
    soundness when it is ``absent`` or ``disproved``; a stated aim whose requirements are met
    establishes the answer type; an answer whose admissibility tests all pass establishes the
    candidates.
    """
    stated = question.get("subject")
    subject: Mapping[str, Any] = stated if isinstance(stated, Mapping) else {}
    if condition == "soundness":
        phenomenon = records.get(str(subject.get("phenomenon"))) or {}
        if phenomenon.get("evidential_status") in REFUTING_STATUSES:
            return ConditionState(
                condition, "refuted", "derived", (str(subject.get("phenomenon")),)
            )
    if condition == "answer-type":
        reached = {
            "question": question,
            "phenomenon": records.get(str(subject.get("phenomenon"))) or {},
            "target-system": records.get(str(subject.get("target_system"))) or {},
        }
        unmet = c.unmet_by_aim(question, reached, c.requirements_by_aim())
        unmet += c.unmet_general(question, c.always_required("question"))
        if c.at(question, "task.epistemic_aim") and not unmet:
            return ConditionState(condition, "established", "derived")
    if condition == "candidates":
        for answer in (
            r
            for r in records.values()
            if r.get("type") == "answer" and r.get("answers") == question.get("id")
        ):
            for assessment in (
                r
                for r in records.values()
                if r.get("type") == "assessment" and r.get("assesses") == answer.get("id")
            ):
                verdicts = [
                    (t or {}).get("verdict")
                    for t in ((assessment.get("tests") or {}).get("admissibility") or {}).values()
                ]
                if verdicts and all(v in ("pass", "not-applicable") for v in verdicts):
                    return ConditionState(
                        condition, "established", "derived", (str(assessment.get("id")),)
                    )
    return None


def _inputs_of(step: Mapping[str, Any]) -> list[str]:
    """Return the references that the inputs of a step name."""
    return [str(i.get("ref")) for i in step.get("inputs") or [] if isinstance(i, Mapping)]


def _output_of(step: Mapping[str, Any]) -> str:
    """Return the reference of the output of a step, empty when it names none."""
    return str((step.get("output") or {}).get("ref") or "")


def _spread(
    steps: Mapping[str, Mapping[str, Any]], own: str, verdict: str, marked: set[str]
) -> set[str]:
    """Return the outputs of the steps that a verdict reaches in one itinerary.

    A step is reached when its norm has the verdict, or when it takes as input a marked record, the
    output of a reached step, or a reached step named in full by ``own`` and its identifier.
    """
    reached: set[str] = set()
    products: set[str] = set()
    changed = True
    while changed:
        changed = False
        for name, step in steps.items():
            if name in reached:
                continue
            upstream = any(
                r in marked or r in products or (r.startswith(own) and r[len(own) :] in reached)
                for r in _inputs_of(step)
            )
            if (step.get("norm") or {}).get("verdict") == verdict or upstream:
                reached.add(name)
                changed = True
                if _output_of(step):
                    products.add(_output_of(step))
    return products


def _awaiting(steps: Mapping[str, Mapping[str, Any]], own: str, records: Records) -> list[str]:
    """Return the steps whose verdict is pending while their output record is stabilized."""
    return [
        f"{own}{name}"
        for name, step in sorted(steps.items())
        if (step.get("norm") or {}).get("verdict") == "pending"
        and (records.get(_output_of(step)) or {}).get("status") == "stabilized"
    ]


def itinerary_state(records: Records) -> tuple[set[str], set[str], list[str]]:
    """Return the impeached records, the conditional records, and the steps whose norm awaits a new
    judgment.

    A record is impeached when a step that produced it failed its norm, or took an impeached record
    or the output of an impeached step as input; a pending verdict propagates the same way and makes
    its products conditional. A step whose verdict is pending while its record is stabilized awaits
    a new judgment of its norm.
    """
    impeached: set[str] = set()
    conditional: set[str] = set()
    anew: list[str] = []
    for itinerary in (r for r in records.values() if r.get("type") == "itinerary"):
        own = f"{itinerary.get('id')}."
        steps = {
            str(s.get("id")): s for s in itinerary.get("steps") or [] if isinstance(s, Mapping)
        }
        impeached |= _spread(steps, own, "fail", impeached)
        conditional |= _spread(steps, own, "pending", conditional)
        anew += _awaiting(steps, own, records)
    return impeached, conditional - impeached, anew


def readiness(
    act: Activity,
    records: Records,
    types: Mapping[str, Any],
    impeached: set[str],
    conditional: set[str],
) -> Act:
    """Return whether every input that an activity requires is held by an unimpeached record."""
    missing: list[str] = []
    rests_on_pending = False
    for held in act.inputs:
        if held.least == 0 or held.types & {"source"}:
            continue
        holders = [
            ident
            for ident, r in records.items()
            if ident not in impeached and any(holds(r, types.get(t) or {}) for t in held.types)
        ]
        if len(holders) < held.least:
            missing.append(" | ".join(sorted(held.types)))
        elif all(h in conditional for h in holders):
            rests_on_pending = True
    return Act(act.id, not missing, tuple(missing), rests_on_pending)


def merge(diagnoses: list[Diagnosis]) -> Diagnosis:
    """Return one diagnosis gathering the diagnoses of several problems."""
    merged = Diagnosis()
    for d in diagnoses:
        merged.questions += d.questions
        merged.impeached |= d.impeached
        merged.conditional |= d.conditional
        merged.judge_anew += d.judge_anew
        merged.revisions += [r for r in d.revisions if r not in merged.revisions]
    merged.questions.sort(key=lambda q: q.question)
    return merged


@dataclass(frozen=True)
class _Model:
    """The model of answerability that the registry declares.

    Attributes
    ----------
    order : list of str
        The conditions, each listed after the conditions on which it depends.
    deps : mapping
        Per condition and route, the conditions on which it depends.
    acting : mapping
        Per condition, the activities that act on it, in the order of the registry.
    """

    order: list[str]
    deps: Mapping[str, Mapping[str, list[str]]]
    acting: Mapping[str, list[str]]


@dataclass(frozen=True)
class _Reach:
    """What the readiness of an act reads: the registries, the local records and their state."""

    acts: Mapping[str, Activity]
    types: Mapping[str, Any]
    local: Records
    impeached: set[str]
    conditional: set[str]


def _model(registry: Mapping[str, Any]) -> _Model:
    """Return the model of answerability that a registry declares, with hyphenated names."""
    deps = {
        str(k).replace(" ", "-"): {
            route: [str(d).replace(" ", "-") for d in names] for route, names in (v or {}).items()
        }
        for k, v in (registry.get("dependencies") or {}).items()
    }
    acting: dict[str, list[str]] = {}
    for entry in registry.get("activities") or []:
        name = str(entry.get("condition")).replace(" ", "-")
        if entry.get("id") not in acting.setdefault(name, []):
            acting[name].append(str(entry.get("id")))
    order = [str(name).replace(" ", "-") for name in registry.get("conditions") or []]
    return _Model(order, deps, acting)


def _route_diagnosis(
    question: Mapping[str, Any], route: str, model: _Model, records: Records, reach: _Reach
) -> RouteDiagnosis:
    """Return the states, the open and the refuted conditions of a question on a route."""
    applicable = conditions_on(route, model.deps)
    if c.at(question, "task.epistemic_aim") == "explication":
        # the explicandum is not a slot, so its definiteness is no condition and a
        # dependency on it is void
        applicable = {
            k: [d for d in v if d != "definiteness"]
            for k, v in applicable.items()
            if k != "definiteness"
        }
    states: dict[str, ConditionState] = {}
    for condition in (name for name in model.order if name in applicable):
        states[condition] = (
            asserted(question, condition, route)
            or derived(question, condition, records)
            or ConditionState(condition, "not-established", "default")
        )
    established = ConditionState("", "established", "default")
    opened = {
        condition: tuple(
            readiness(reach.acts[a], reach.local, reach.types, reach.impeached, reach.conditional)
            for a in model.acting.get(condition, [])
            if a in reach.acts
        )
        for condition, state in states.items()
        if state.state == "not-established"
        and all(states.get(d, established).state == "established" for d in applicable[condition])
    }
    refuted = tuple(cond for cond, state in states.items() if state.state == "refuted")
    return RouteDiagnosis(route, tuple(states.values()), opened, refuted)


def diagnose(
    records: Records, registry: Mapping[str, Any] | None = None, local: Records | None = None
) -> Diagnosis:
    """Return the diagnosis of every question of a set of records.

    ``records`` holds every record that a state may read, such as the phenomenon of another folder;
    ``local`` holds the records of one problem, whose questions are diagnosed and whose records fill
    the inputs of an act, and defaults to ``records``.

    >>> diagnosis = diagnose({"quest.a.b": {"id": "quest.a.b", "type": "question"}})
    >>> [s.condition for s in diagnosis.questions[0].routes[0].states][:2]
    ['definiteness', 'answer-type']
    >>> list(diagnosis.questions[0].routes[0].open)
    ['definiteness']
    """
    model = _model(registry or answerability_registry())
    local = records if local is None else local
    impeached, conditional, anew = itinerary_state(local)
    reach = _Reach(activities(), product_types(), local, impeached, conditional)
    result = Diagnosis(
        impeached=impeached,
        conditional=conditional,
        judge_anew=anew,
        revisions=revisions(records, itineraries=local),
    )
    for ident in sorted(i for i, r in local.items() if r.get("type") == "question"):
        question = local[ident]
        routes = tuple(
            _route_diagnosis(question, route, model, records, reach)
            for route in routes_of(question)
        )
        result.questions.append(QuestionDiagnosis(ident, routes))
    return result


def as_document(diagnosis: Diagnosis) -> dict[str, Any]:
    """Return the diagnosis as a mapping in a stable order, for a YAML report."""
    return {
        "questions": [
            {
                "question": q.question,
                "routes": [
                    {
                        "route": r.route,
                        "conditions": [
                            {
                                "condition": s.condition,
                                "state": s.state,
                                "source": s.source,
                                **({"pointers": list(s.pointers)} if s.pointers else {}),
                            }
                            for s in r.states
                        ],
                        "open": [
                            {
                                "condition": cond,
                                "acts": [
                                    {
                                        "activity": a.activity,
                                        "ready": a.ready,
                                        **({"missing": list(a.missing)} if a.missing else {}),
                                        **({"conditional": True} if a.conditional else {}),
                                    }
                                    for a in acts_
                                ],
                            }
                            for cond, acts_ in r.open.items()
                        ],
                        "refuted": [
                            {"condition": cond, "revisions": list(REVISIONS)} for cond in r.refuted
                        ],
                    }
                    for r in q.routes
                ],
            }
            for q in diagnosis.questions
        ],
        "revisions": [
            {
                "step": r.step,
                "record": r.record,
                "kind": r.kind,
                "flagged": list(r.flagged),
                "to_review": list(r.to_review),
            }
            for r in sorted(diagnosis.revisions, key=lambda x: x.step)
        ],
        "itineraries": {
            "impeached": sorted(diagnosis.impeached),
            "conditional": sorted(diagnosis.conditional),
            "judge_anew": sorted(diagnosis.judge_anew),
        },
    }


def render_text(diagnosis: Diagnosis) -> str:
    """Return the diagnosis as lines for a terminal: per question and route, the open and refuted
    conditions."""
    lines: list[str] = []
    for q in diagnosis.questions:
        for r in q.routes:
            lines.append(f"{q.question} [{r.route}]")
            for cond, acts_ in r.open.items():
                ready = (
                    ", ".join(
                        a.activity + ("" if a.ready else " (missing " + "; ".join(a.missing) + ")")
                        for a in acts_
                    )
                    or "no registered activity"
                )
                lines.append(f"  open {cond}: {ready}")
            for cond in r.refuted:
                lines.append(f"  refuted {cond}: revise by {', '.join(REVISIONS)}")
            if not r.open and not r.refuted:
                lines.append(
                    "  every condition is established: obtain the answer, then evaluate it"
                )
    for rev in sorted(diagnosis.revisions, key=lambda x: x.step):
        if rev.to_review:
            lines.append(
                f"review after the {rev.kind} of {rev.record} ({rev.step}):"
                f" {', '.join(rev.to_review)}"
            )
    for step in sorted(diagnosis.judge_anew):
        lines.append(f"judge anew the norm of {step}, whose record is stabilized")
    if diagnosis.impeached:
        lines.append(f"impeached records: {', '.join(sorted(diagnosis.impeached))}")
    return "\n".join(lines) + ("\n" if lines else "")


def malformed_answerability(question: Mapping[str, Any], records: Records) -> list[Finding]:
    """Return every asserted state that the question states incompletely or against its records.

    A refutation states its kind, a refutation for lack of means its means, and every assertion its
    pointers. Definiteness requires the level ``specified`` of the slot whose term it states.
    """
    found = []
    for index, entry in enumerate(question.get("answerability") or []):
        if not isinstance(entry, Mapping):
            continue
        where = ("answerability", Entry(index, entry))
        label = f"answerability.{entry.get('condition')}"
        if entry.get("state") == "refuted" and not entry.get("refutation"):
            found.append(
                finding(
                    rules.COMPLETENESS_MALFORMED_ANSWERABILITY,
                    f"{label}: a refutation states no kind",
                    *where,
                    "refutation",
                )
            )
        if entry.get("refutation") == "lack-of-means" and not entry.get("means"):
            found.append(
                finding(
                    rules.COMPLETENESS_MALFORMED_ANSWERABILITY,
                    f"{label}: a refutation for lack of means names no means tried",
                    *where,
                    "means",
                )
            )
        if entry.get("state") in ("established", "refuted") and not entry.get("pointers"):
            found.append(
                finding(
                    rules.COMPLETENESS_MALFORMED_ANSWERABILITY,
                    f"{label}: the state {entry.get('state')} cites no pointer",
                    *where,
                    "pointers",
                )
            )
        term = records.get(str(entry.get("term"))) or {}
        if (
            entry.get("condition") == "definiteness"
            and entry.get("state") == "established"
            and term.get("type") in ("target-system", "phenomenon")
            and term.get("commitment") != "specified"
        ):
            found.append(
                finding(
                    rules.COMPLETENESS_MALFORMED_ANSWERABILITY,
                    f"{label}: {entry.get('term')} is not specified, which definiteness requires",
                    *where,
                    "term",
                )
            )
    return found
