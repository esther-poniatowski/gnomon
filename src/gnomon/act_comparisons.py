"""Validate authored act appraisals and derive transparent ordinal comparisons.

The researcher supplies every criterion, scale, preferred direction, value, and basis. This module
checks that those inputs form one comparison and applies only the declared ordinal-dominance rule.
It assigns no weights and supplies no judgment.
"""

from __future__ import annotations

from collections import Counter
from collections.abc import Mapping, Sequence
from dataclasses import dataclass
from typing import Any

from . import findings as rules
from .findings import Entry, Finding, finding

Records = Mapping[str, Mapping[str, Any]]

ORDINAL_DOMINANCE = "ordinal-dominance"
RULE_STATEMENT = (
    "An act dominates another when it is no worse on every criterion and better on at least one."
)


@dataclass(frozen=True)
class _Criterion:
    """One valid authored criterion used by the comparison."""

    identifier: str
    question: str
    scale: tuple[str, ...]
    preferred: str


@dataclass(frozen=True)
class _Act:
    """One valid authored act and its judgments, keyed by criterion."""

    identifier: str
    activity: str
    acts_on: str
    available_means: tuple[str, ...]
    judgments: Mapping[str, Mapping[str, Any]]


@dataclass(frozen=True)
class _Issue:
    """One defect of an appraisal before it is converted to a located finding."""

    text: str
    segments: tuple[str | int, ...]
    value: str | None = None


def _entries(value: Any) -> list[Mapping[str, Any]]:
    """Return the mapping entries of one authored sequence."""
    if not isinstance(value, Sequence) or isinstance(value, (str, bytes)):
        return []
    return [entry for entry in value if isinstance(entry, Mapping)]


def _names(entries: Sequence[Mapping[str, Any]]) -> list[str]:
    """Return the non-empty identifiers of ``entries`` in their authored order."""
    return [str(entry.get("id")) for entry in entries if str(entry.get("id") or "").strip()]


def _duplicate_issues(
    entries: Sequence[Mapping[str, Any]], collection: str, subject: str
) -> list[_Issue]:
    """Report identifiers repeated inside one keyed appraisal collection."""
    counts = Counter(_names(entries))
    return [
        _Issue(
            f"{collection}: {identifier} identifies several {subject}",
            (collection,),
            identifier,
        )
        for identifier in sorted(name for name, count in counts.items() if count > 1)
    ]


def _criterion_issues(criteria: Sequence[Mapping[str, Any]]) -> list[_Issue]:
    """Return defects that prevent the criteria from defining ordered preferences."""
    found = _duplicate_issues(criteria, "criteria", "criteria")
    if not criteria:
        found.append(_Issue("criteria: state at least one criterion", ("criteria",)))
    for index, criterion in enumerate(criteria):
        identifier = str(criterion.get("id") or "").strip()
        prefix = f"criteria.{identifier or index}"
        if not identifier:
            found.append(_Issue(f"{prefix}: state an identifier", ("criteria", index, "id")))
        if not str(criterion.get("question") or "").strip():
            found.append(
                _Issue(
                    f"{prefix}: state the property being judged",
                    ("criteria", index, "question"),
                )
            )
        scale = [str(value) for value in criterion.get("scale") or [] if str(value).strip()]
        if len(scale) < 2:
            found.append(
                _Issue(
                    f"{prefix}.scale: state at least two ordered values",
                    ("criteria", index, "scale"),
                )
            )
        repeated = sorted(name for name, count in Counter(scale).items() if count > 1)
        for value in repeated:
            found.append(
                _Issue(
                    f"{prefix}.scale: {value} occurs more than once",
                    ("criteria", index, "scale"),
                    value,
                )
            )
        if criterion.get("preferred") not in ("higher", "lower"):
            found.append(
                _Issue(
                    f"{prefix}.preferred: state higher or lower",
                    ("criteria", index, "preferred"),
                )
            )
    return found


def _declared_scales(
    criteria: Sequence[Mapping[str, Any]],
) -> dict[str, tuple[str, ...]]:
    """Return the scale of each criterion that has a non-empty identifier."""
    return {
        str(criterion.get("id")): tuple(str(value) for value in criterion.get("scale") or [])
        for criterion in criteria
        if str(criterion.get("id") or "").strip()
    }


def _act_field_issues(act: Mapping[str, Any], index: int, prefix: str) -> list[_Issue]:
    """Return missing fields that identify and make one act operational."""
    found: list[_Issue] = []
    if not str(act.get("id") or "").strip():
        found.append(_Issue(f"{prefix}: state an identifier", ("acts", index, "id")))
    for field, label in (("activity", "activity"), ("acts_on", "condition")):
        if not str(act.get(field) or "").strip():
            found.append(_Issue(f"{prefix}: state its {label}", ("acts", index, field)))
    means = [str(value) for value in act.get("available_means") or [] if str(value).strip()]
    if not means:
        found.append(
            _Issue(
                f"{prefix}: state the means available for the act",
                ("acts", index, "available_means"),
            )
        )
    return found


def _judgment_issues(
    judgments: Sequence[Mapping[str, Any]],
    declared: Mapping[str, tuple[str, ...]],
    act_index: int,
    prefix: str,
) -> list[_Issue]:
    """Return duplicate, unknown, invalid, incomplete, and unsupported judgments."""
    found: list[_Issue] = []
    names = [str(item.get("criterion") or "") for item in judgments]
    for name, count in sorted(Counter(names).items()):
        if name and count > 1:
            found.append(
                _Issue(
                    f"{prefix}.judgments: {name} is judged more than once",
                    ("acts", act_index, "judgments"),
                    name,
                )
            )
    for judgment_index, judgment in enumerate(judgments):
        found.extend(_one_judgment_issues(judgment, declared, act_index, judgment_index, prefix))
    for name in declared:
        if name not in names:
            found.append(
                _Issue(
                    f"{prefix}: states no judgment of {name}",
                    ("acts", act_index, "judgments"),
                    name,
                )
            )
    return found


def _one_judgment_issues(
    judgment: Mapping[str, Any],
    declared: Mapping[str, tuple[str, ...]],
    act_index: int,
    judgment_index: int,
    prefix: str,
) -> list[_Issue]:
    """Return the defects of one authored criterion judgment."""
    found: list[_Issue] = []
    name = str(judgment.get("criterion") or "")
    value = str(judgment.get("value") or "")
    place = ("acts", act_index, "judgments", judgment_index)
    if name not in declared:
        found.append(
            _Issue(
                f"{prefix}.judgments: {name or '(empty)'} names no declared criterion",
                (*place, "criterion"),
                name or "(empty)",
            )
        )
    elif value not in declared[name]:
        found.append(
            _Issue(
                f"{prefix}.judgments: {value or '(empty)'} is not on the scale of {name}",
                (*place, "value"),
                value or "(empty)",
            )
        )
    if not str(judgment.get("basis") or "").strip():
        found.append(
            _Issue(
                f"{prefix}.judgments: {name or judgment_index} states no basis",
                (*place, "basis"),
            )
        )
    return found


def _act_issues(
    acts: Sequence[Mapping[str, Any]], criteria: Sequence[Mapping[str, Any]]
) -> list[_Issue]:
    """Return defects that prevent the acts from sharing one complete judgment matrix."""
    found = _duplicate_issues(acts, "acts", "acts")
    if len(acts) < 2:
        found.append(_Issue("acts: state at least two acts to compare", ("acts",)))
    declared = _declared_scales(criteria)
    for act_index, act in enumerate(acts):
        identifier = str(act.get("id") or "").strip()
        prefix = f"acts.{identifier or act_index}"
        found.extend(_act_field_issues(act, act_index, prefix))
        found.extend(_judgment_issues(_entries(act.get("judgments")), declared, act_index, prefix))
    return found


def _issues(appraisal: Mapping[str, Any]) -> list[_Issue]:
    """Return every defect that prevents one appraisal from being compared."""
    found: list[_Issue] = []
    if appraisal.get("rule") != ORDINAL_DOMINANCE:
        found.append(
            _Issue(
                f"rule: state {ORDINAL_DOMINANCE} before comparing the acts",
                ("rule",),
            )
        )
    criteria = _entries(appraisal.get("criteria"))
    acts = _entries(appraisal.get("acts"))
    return found + _criterion_issues(criteria) + _act_issues(acts, criteria)


def appraisal_findings(itinerary: Mapping[str, Any]) -> list[Finding]:
    """Return every authored appraisal that cannot support its declared comparison."""
    found: list[Finding] = []
    for index, appraisal in enumerate(_entries(itinerary.get("act_appraisals"))):
        name = str(appraisal.get("id") or index)
        for issue in _issues(appraisal):
            found.append(
                finding(
                    rules.ITINERARY_MALFORMED_APPRAISAL,
                    f"act_appraisals.{name}.{issue.text}",
                    "act_appraisals",
                    Entry(index, appraisal),
                    *issue.segments,
                    value=issue.value,
                )
            )
    return found


def _criterion(entry: Mapping[str, Any]) -> _Criterion:
    """Return one criterion after :func:`_issues` has validated its fields."""
    return _Criterion(
        str(entry["id"]),
        str(entry["question"]),
        tuple(str(value) for value in entry["scale"]),
        str(entry["preferred"]),
    )


def _act(entry: Mapping[str, Any]) -> _Act:
    """Return one act after :func:`_issues` has validated its fields."""
    judgments = {str(item["criterion"]): item for item in _entries(entry.get("judgments"))}
    return _Act(
        str(entry["id"]),
        str(entry["activity"]),
        str(entry["acts_on"]),
        tuple(str(value) for value in entry["available_means"]),
        judgments,
    )


def _relation(left: _Act, right: _Act, criteria: Sequence[_Criterion]) -> dict[str, Any]:
    """Return the ordinal relation of two acts and the criteria that determine it."""
    better: list[str] = []
    worse: list[str] = []
    equal: list[str] = []
    for criterion in criteria:
        left_value = str(left.judgments[criterion.identifier]["value"])
        right_value = str(right.judgments[criterion.identifier]["value"])
        left_rank = criterion.scale.index(left_value)
        right_rank = criterion.scale.index(right_value)
        if criterion.preferred == "lower":
            left_rank, right_rank = -left_rank, -right_rank
        target = equal if left_rank == right_rank else better if left_rank > right_rank else worse
        target.append(criterion.identifier)
    relation = (
        "equivalent"
        if not better and not worse
        else (
            "dominates"
            if better and not worse
            else "dominated-by" if worse and not better else "incomparable"
        )
    )
    return {
        "act": left.identifier,
        "other": right.identifier,
        "relation": relation,
        "better_on": better,
        "worse_on": worse,
        "equal_on": equal,
    }


def _comparison(itinerary: str, appraisal: Mapping[str, Any]) -> dict[str, Any]:
    """Return one transparent comparison after its authored appraisal has passed validation."""
    criteria = [_criterion(entry) for entry in _entries(appraisal.get("criteria"))]
    acts = [_act(entry) for entry in _entries(appraisal.get("acts"))]
    relations = [
        _relation(left, right, criteria)
        for index, left in enumerate(acts)
        for right in acts[index + 1 :]
    ]
    dominated = {
        row["other"] if row["relation"] == "dominates" else row["act"]
        for row in relations
        if row["relation"] in ("dominates", "dominated-by")
    }
    leaders = [act.identifier for act in acts if act.identifier not in dominated]
    return {
        "itinerary": itinerary,
        "appraisal": str(appraisal["id"]),
        "question": str(appraisal.get("question") or ""),
        "route": str(appraisal.get("route") or ""),
        "rule": ORDINAL_DOMINANCE,
        "rule_statement": RULE_STATEMENT,
        "selection": "determined" if len(leaders) == 1 else "unresolved",
        "leading_acts": leaders,
        "criteria": [
            {
                "criterion": item.identifier,
                "question": item.question,
                "scale": list(item.scale),
                "preferred": item.preferred,
            }
            for item in criteria
        ],
        "acts": [
            {
                "act": item.identifier,
                "activity": item.activity,
                "acts_on": item.acts_on,
                "available_means": list(item.available_means),
            }
            for item in acts
        ],
        "judgments": [
            {
                "act": act.identifier,
                "criterion": criterion.identifier,
                "value": str(act.judgments[criterion.identifier]["value"]),
                "basis": str(act.judgments[criterion.identifier]["basis"]),
            }
            for act in acts
            for criterion in criteria
        ],
        "relations": relations,
    }


def comparisons(records: Records) -> list[dict[str, Any]]:
    """Return valid authored appraisals compared by their declared rule.

    Invalid or incomplete appraisals yield no computed row. :func:`appraisal_findings` reports each
    blocking field through the normal check pipeline.
    """
    return [
        _comparison(identifier, appraisal)
        for identifier in sorted(records)
        if records[identifier].get("type") == "itinerary"
        for appraisal in _entries(records[identifier].get("act_appraisals"))
        if not _issues(appraisal)
    ]
