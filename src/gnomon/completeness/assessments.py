"""
The checks of an assessment, and the disposition that its tests give to the record assessed.
"""

from __future__ import annotations

from typing import Any, Iterable, Mapping

from .. import findings as rules
from ..findings import Entry, Finding, finding
from .paths import is_unfilled


def malformed_credence(assessment: Mapping[str, Any]) -> list[Finding]:
    """Return the credence that is no degree of belief, or that states no basis.

    A credence is a number between zero and one; a value outside that interval is no probability,
    and a value without its basis cannot be revised when the evidence changes.
    """
    credence = assessment.get("credence")
    if credence is None:
        return []
    if not isinstance(credence, Mapping):
        return [
            finding(
                rules.COMPLETENESS_MALFORMED_CREDENCE,
                "credence: holds neither a value nor a basis",
                "credence",
            )
        ]
    found = []
    value = credence.get("value")
    if isinstance(value, bool) or not isinstance(value, (int, float)) or not 0 <= value <= 1:
        found.append(
            finding(
                rules.COMPLETENESS_CREDENCE_OUT_OF_RANGE,
                f"credence.value: {value!r} is no number between 0 and 1",
                "credence",
                "value",
            )
        )
    if not credence.get("basis"):
        found.append(
            finding(
                rules.COMPLETENESS_CREDENCE_WITHOUT_BASIS,
                "credence.basis: the value states no basis",
                "credence",
                "basis",
            )
        )
    return found


def _answer_tests(tests: Mapping[str, Any]) -> list[Finding]:
    """Report an assessment of an answer missing a level of tests, or with constraint verdicts."""
    found = [
        finding(
            rules.COMPLETENESS_MISSHAPEN_TESTS,
            f"tests.{level}: an assessment of an answer holds its tests of {level}",
            "tests",
            level,
        )
        for level in ("admissibility", "warrant")
        if not isinstance(tests.get(level), Mapping) or not tests.get(level)
    ]
    if tests.get("constraints"):
        text = "tests.constraints: an assessment of an answer holds no verdict per constraint"
        found.append(finding(rules.COMPLETENESS_MISSHAPEN_TESTS, text, "tests", "constraints"))
    return found


def _construct_tests(
    tests: Mapping[str, Any], against: Mapping[str, Any] | None, standard: Any
) -> list[Finding]:
    """Report an assessment of a construct whose verdicts miss the constraints of its problem."""
    found = []
    verdicts = tests.get("constraints")
    if not isinstance(verdicts, list) or not verdicts:
        text = "tests.constraints: an assessment of a construct holds one verdict per constraint"
        found.append(finding(rules.COMPLETENESS_MISSHAPEN_TESTS, text, "tests", "constraints"))
        verdicts = []
    found += [
        finding(
            rules.COMPLETENESS_MISSHAPEN_TESTS,
            f"tests.{level}: an assessment of a construct holds no tests of {level}",
            "tests",
            level,
        )
        for level in ("admissibility", "warrant")
        if tests.get(level)
    ]
    if against is None or against.get("type") != "problem":
        return found
    stated = {c.get("name") for c in against.get("constraints") or [] if isinstance(c, Mapping)}
    found += [
        finding(
            rules.COMPLETENESS_UNKNOWN_CONSTRAINT,
            f"tests.constraints: {entry.get('constraint')} is no constraint of {standard}",
            "tests",
            "constraints",
            Entry(index, entry),
        )
        for index, entry in enumerate(verdicts)
        if isinstance(entry, Mapping) and entry.get("constraint") not in stated
    ]
    return found


def _mismatched_standard(
    target: Mapping[str, Any], against: Mapping[str, Any] | None, standard: Any, expected: str
) -> list[Finding]:
    """Report a standard that is not the kind of record against which the target is assessed."""
    against_type = (against or {}).get("type")
    if against_type == expected:
        return []
    kind = f"a {against_type} record" if against_type else "no record"
    assessed_kind = str(target.get("type"))
    article = "an" if assessed_kind[:1] in "aeiou" else "a"
    text = (
        f"against: {standard} is {kind}, and an assessment of {article} {assessed_kind}"
        f" is made against a {expected}"
    )
    return [finding(rules.COMPLETENESS_MISMATCHED_STANDARD, text, "against")]


def misdirected_assessment(
    assessment: Mapping[str, Any],
    records: Mapping[str, Mapping[str, Any]],
    construct_kinds: Iterable[str],
) -> list[Finding]:
    """Return every mismatch between what an assessment assesses, its standard and its tests.

    An assessment tests a candidate answer against the specification of a question, through its
    tests of admissibility and of warrant, or a construct that a problem demands against the
    constraints of that problem, through one verdict per constraint. The record assessed decides
    which standard and which tests apply.

    Parameters
    ----------
    assessment : mapping
        One filled assessment record.
    records : mapping
        The records of the problem, keyed by identifier.
    construct_kinds : iterable of str
        The record kinds that hold a construct, read from the product-type registry.
    """
    assessed, standard = assessment.get("assesses"), assessment.get("against")
    target = records.get(assessed) if isinstance(assessed, str) else None
    if target is None:
        text = f"assesses: {assessed} is no record"
        return [finding(rules.COMPLETENESS_UNKNOWN_ASSESSED, text, "assesses")]
    tests = assessment.get("tests") or {}
    against = records.get(standard) if isinstance(standard, str) else None
    if target.get("type") == "answer":
        expected, found = "question", _answer_tests(tests)
    elif target.get("type") in set(construct_kinds):
        expected, found = "problem", _construct_tests(tests, against, standard)
    else:
        text = (
            f"assesses: {assessed} is a {target.get('type')} record, neither an answer nor a"
            " construct"
        )
        return [finding(rules.COMPLETENESS_UNASSESSABLE_RECORD, text, "assesses")]
    return _mismatched_standard(target, against, standard, expected) + found


def disposition(assessment: Mapping[str, Any], erotetic_relation: str | None = None) -> str:
    """Return the disposition of an assessment, read from its verdicts.

    An answer satisfies its question only when it is admissible and warranted, and a construct meets
    its problem only when it meets every constraint, so one failed test decides the disposition.
    Without a failure, a pending verdict withholds it. A corrective answer shows that a
    presupposition of its question is false, so it cannot satisfy that question: the disposition
    that would be ``satisfied`` is ``corrective`` instead.

    Parameters
    ----------
    assessment : mapping
        One filled assessment record.
    erotetic_relation : str, optional
        The value of the erotetic relation of the assessed answer, read from its field
        ``erotetic_relation.value``. When omitted, the answer is not treated as corrective.

    Examples
    --------
    >>> disposition({"tests": {"admissibility": {"scope": {"verdict": "pass"}},
    ...                        "warrant": {"closure": {"verdict": "fail"}}}})
    'not-satisfied'
    >>> disposition({"tests": {"admissibility": {"scope": {"verdict": "pending"}}}})
    'withheld'
    >>> disposition({"tests": {"warrant": {"selection": {"verdict": "not-applicable"}}}})
    'satisfied'
    >>> disposition({"tests": {"warrant": {"closure": {"verdict": "pass"}}}}, "corrective")
    'corrective'
    >>> disposition({"tests": {"warrant": {"closure": {"verdict": "pending"}}}}, "corrective")
    'withheld'
    >>> disposition({"tests": {"constraints": [{"constraint": "c1", "verdict": "pass"},
    ...                                        {"constraint": "c2", "verdict": "fail"}]}})
    'not-satisfied'
    """
    tests = assessment.get("tests") or {}
    verdicts = [
        (entry or {}).get("verdict")
        for level in ("admissibility", "warrant")
        for entry in (tests.get(level) or {}).values()
    ] + [
        (entry or {}).get("verdict")
        for entry in tests.get("constraints") or []
        if isinstance(entry, Mapping)
    ]
    if "fail" in verdicts:
        return "not-satisfied"
    if any(verdict not in ("pass", "not-applicable") for verdict in verdicts):
        return "withheld"
    return "corrective" if erotetic_relation == "corrective" else "satisfied"


def premature_appraisal(assessment: Mapping[str, Any]) -> list[Finding]:
    """Return the appraisal of an answer that has not passed both tiers of tests.

    A virtue ranks answers that already satisfy the question, and never compensates for a failed
    test, so an answer is appraised only once no test of admissibility or of warrant fails or
    stays pending.

    >>> failing = {"tests": {"warrant": {"closure": {"verdict": "fail"}}},
    ...            "appraisal": [{"virtue": "unification", "assessment": "high"}]}
    >>> [f.text for f in premature_appraisal(failing)]
    ['appraisal: the answer is appraised although its disposition is not-satisfied']
    >>> premature_appraisal({**failing, "appraisal": []})
    []
    """
    state = disposition(assessment)
    if state in ("satisfied", "corrective") or is_unfilled(assessment.get("appraisal")):
        return []
    return [
        finding(
            rules.COMPLETENESS_PREMATURE_APPRAISAL,
            f"appraisal: the answer is appraised although its disposition is {state}",
            "appraisal",
        )
    ]
