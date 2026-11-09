"""
The checks of an assessment, and the disposition that its tests give to the record assessed.
"""

from __future__ import annotations

from typing import Any, Iterable, Mapping

from .. import findings as rules
from ..findings import Entry, Finding, finding
from .paths import at, is_unfilled


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


def _named(entry: Mapping[str, Any], block: str, key: str) -> Any:
    """Return the value of a key in a block of an entry, or None when the block is no mapping."""
    value = entry.get(block)
    return value.get(key) if isinstance(value, Mapping) else None


def _version(value: Any) -> int | None:
    """Return a version label as a whole number, or None when it is no positive whole number."""
    text = str(value) if value is not None else ""
    return int(text) if text.isdigit() and int(text) > 0 else None


def is_void(assessment: Mapping[str, Any], records: Mapping[str, Mapping[str, Any]]) -> bool:
    """Return whether an assessment names a version of its question other than the present one.

    A retracted assessment is never void, since it no longer bears on the question.

    >>> records = {"quest.a": {"type": "question", "version": "2"}}
    >>> is_void({"against": "quest.a", "against_version": "1"}, records)
    True
    >>> is_void({"against": "quest.a", "against_version": "2"}, records)
    False
    """
    question = records.get(str(assessment.get("against")))
    if not isinstance(question, Mapping) or question.get("type") != "question":
        return False
    if assessment.get("status") == "retracted" or question.get("version") is None:
        return False
    return str(assessment.get("against_version")) != str(question.get("version"))


def misversioned_assessment(
    assessment: Mapping[str, Any], records: Mapping[str, Mapping[str, Any]]
) -> list[Finding]:
    """Return the version that an assessment names when it does not match its question.

    An assessment of an answer names the version of its question that its verdicts read, so that
    a revision of the question reports those verdicts void; an assessment of a construct is made
    against a problem, which carries no version.

    >>> records = {"quest.a": {"type": "question", "version": "2"}, "ans.a": {"type": "answer"}}
    >>> [f.rule.id for f in misversioned_assessment(
    ...     {"assesses": "ans.a", "against": "quest.a", "against_version": "1"}, records)]
    ['completeness/void-assessment']
    >>> [f.rule.id for f in misversioned_assessment(
    ...     {"assesses": "ans.a", "against": "quest.a"}, records)]
    ['completeness/unversioned-assessment']
    """
    assessed = records.get(str(assessment.get("assesses")))
    of_answer = isinstance(assessed, Mapping) and assessed.get("type") == "answer"
    named, ident = assessment.get("against_version"), assessment.get("against")
    if of_answer == (named is None):
        text = (
            f"against_version: the assessment names no version of {ident}"
            if of_answer
            else "against_version: an assessment of a construct is made against a problem"
        )
        return [finding(rules.COMPLETENESS_UNVERSIONED_ASSESSMENT, text, "against_version")]
    question = records.get(str(ident))
    read = _version(named)
    present = _version(question.get("version")) if isinstance(question, Mapping) else None
    if (
        not of_answer
        or assessment.get("status") == "retracted"
        or read is None
        or present is None
        or read == present
    ):
        return []
    if read > present:
        text = f"against_version: {ident} is at version {present}, not yet at version {read}"
        return [finding(rules.COMPLETENESS_UNKNOWN_QUESTION_VERSION, text, "against_version")]
    text = (
        f"against_version: read version {read} of {ident}, now at version {present}, so the"
        f" verdicts are void; renew them against version {present} or retract the assessment"
    )
    return [finding(rules.COMPLETENESS_VOID_ASSESSMENT, text, "against_version")]


def unrecorded_question_revision(
    question: Mapping[str, Any], records: Mapping[str, Mapping[str, Any]]
) -> list[Finding]:
    """Return a warning for a question revised without a step of an itinerary that records it.

    A question past its first version, or refined, was revised, and every revision records its
    trigger in a step: a step of the activity ``question-revision`` whose output is the question,
    or a step whose ``revises`` names it.

    >>> [f.rule.id for f in unrecorded_question_revision({"id": "quest.a", "version": "2"}, {})]
    ['completeness/unrecorded-question-revision']
    """
    ident = question.get("id")
    present = _version(question.get("version"))
    if not ident or not ((present or 1) > 1 or question.get("status") == "refined"):
        return []
    for record in records.values():
        if record.get("type") != "itinerary":
            continue
        for step in record.get("steps") or []:
            if not isinstance(step, Mapping):
                continue
            if _named(step, "revises", "record") == ident or (
                step.get("activity") == "question-revision"
                and _named(step, "output", "ref") == ident
            ):
                return []
    text = f"version: {ident} was revised, and no step of an itinerary records the revision"
    return [finding(rules.COMPLETENESS_UNRECORDED_QUESTION_REVISION, text, "version")]


def mismatched_obligations(
    assessment: Mapping[str, Any], records: Mapping[str, Mapping[str, Any]]
) -> list[Finding]:
    """Return each obligation of an assessment that names no proof obligation of its question, or
    names one twice, and a warning for each proof obligation of the question left without an entry.

    An entry names the obligation that it settles by the identifier of that obligation in the
    question, so that an entry stays attached to its obligation when the question reorders them.

    >>> question = {"type": "question", "task": {"proof_obligations": [{"id": "necessity"},
    ...                                                                {"id": "sufficiency"}]}}
    >>> assessment = {"against": "quest.a", "obligations": [{"obligation": "necessity"},
    ...                                                     {"obligation": "necessity"},
    ...                                                     {"obligation": "converse"}]}
    >>> [f.rule.id for f in mismatched_obligations(assessment, {"quest.a": question})]
    ... # doctest: +NORMALIZE_WHITESPACE
    ['completeness/mismatched-obligation', 'completeness/mismatched-obligation',
     'completeness/unassessed-obligation']
    """
    question = records.get(str(assessment.get("against")))
    if not isinstance(question, Mapping) or question.get("type") != "question":
        return []
    declared = [
        str(o.get("id"))
        for o in at(question, "task.proof_obligations") or []
        if isinstance(o, Mapping) and o.get("id")
    ]
    found, named = [], set()
    for index, entry in enumerate(assessment.get("obligations") or []):
        if not isinstance(entry, Mapping):
            continue
        ident = str(entry.get("obligation") or "")
        if ident not in declared or ident in named:
            reason = (
                "is named twice" if ident in named else "is no proof obligation of the question"
            )
            text = f"obligations: {ident or 'an entry without identifier'} {reason}"
            found.append(
                finding(rules.COMPLETENESS_MISMATCHED_OBLIGATION, text, "obligations", index)
            )
        named.add(ident)
    if assessment.get("status") != "retracted":
        for ident in declared:
            if ident not in named:
                text = f"obligations: the proof obligation {ident} of the question has no entry"
                found.append(finding(rules.COMPLETENESS_UNASSESSED_OBLIGATION, text, "obligations"))
    return found


def _judged_entries(
    assessment: Mapping[str, Any],
) -> list[tuple[tuple[Any, ...], Mapping[str, Any]]]:
    """Return each test and each obligation of an assessment, with its path in the record."""
    stated = assessment.get("tests")
    tests: Mapping[str, Any] = stated if isinstance(stated, Mapping) else {}
    found: list[tuple[tuple[Any, ...], Mapping[str, Any]]] = [
        (("tests", level, name), entry)
        for level in ("admissibility", "warrant")
        for name, entry in (tests.get(level) or {}).items()
        if isinstance(entry, Mapping)
    ]
    found += [
        (("obligations", index), entry)
        for index, entry in enumerate(assessment.get("obligations") or [])
        if isinstance(entry, Mapping)
    ]
    return found


def misplaced_holds_on(assessment: Mapping[str, Any]) -> list[Finding]:
    """Return each subdomain ``holds_on`` stated on a test or an obligation that did not fail.

    A test that passes holds over the whole domain of the claim, so only a failed test names the
    subdomain over which its evidence still supports the claim.

    >>> [f.rule.id for f in misplaced_holds_on(
    ...     {"tests": {"warrant": {"fidelity": {"verdict": "pass", "holds_on": "g < 1"}}}})]
    ['completeness/misplaced-holds-on']
    """
    found = []
    for path, entry in _judged_entries(assessment):
        if entry.get("holds_on") and entry.get("verdict") != "fail":
            text = (
                f"{'.'.join(str(p) for p in path)}: holds_on names a subdomain, and the verdict is"
                f" {entry.get('verdict')}, not fail"
            )
            found.append(finding(rules.COMPLETENESS_MISPLACED_HOLDS_ON, text, *path, "holds_on"))
    return found


def scope_narrowings(records: Mapping[str, Mapping[str, Any]]) -> list[dict[str, str]]:
    """Return the narrowings of scope that the failed tests of the assessments propose.

    A test or an obligation that fails while naming, under ``holds_on``, the subdomain over which
    its evidence still supports the claim proposes to revise the assessed answer by narrowing its
    scope to that subdomain. The proposal is withdrawn once another answer revises the assessed
    one, and it is never made by a retracted or a void assessment.

    >>> records = {"asmt.a": {"type": "assessment", "assesses": "ans.a", "tests": {"warrant": {
    ...     "fidelity": {"verdict": "fail", "holds_on": "g < 1"}}}}}
    >>> scope_narrowings(records)  # doctest: +NORMALIZE_WHITESPACE
    [{'assessment': 'asmt.a', 'answer': 'ans.a', 'test': 'tests.warrant.fidelity',
      'holds_on': 'g < 1'}]
    """
    revised = {
        str(entry.get("target"))
        for record in records.values()
        if record.get("type") == "answer"
        for entry in record.get("relations") or []
        if isinstance(entry, Mapping) and entry.get("relation") == "revises"
    }
    found = []
    for ident in sorted(records):
        assessment = records[ident]
        answer = str(assessment.get("assesses") or "")
        if (
            assessment.get("type") != "assessment"
            or assessment.get("status") == "retracted"
            or is_void(assessment, records)
            or answer in revised
        ):
            continue
        for path, entry in _judged_entries(assessment):
            if entry.get("verdict") == "fail" and entry.get("holds_on"):
                where = (
                    f"obligations.{entry.get('obligation') or path[1]}"
                    if path[0] == "obligations"
                    else ".".join(str(p) for p in path)
                )
                found.append(
                    {
                        "assessment": ident,
                        "answer": answer,
                        "test": where,
                        "holds_on": str(entry["holds_on"]),
                    }
                )
    return found
