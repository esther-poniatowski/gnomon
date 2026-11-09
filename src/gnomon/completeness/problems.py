"""
The state of a problem: the request of its questions, the demand that its records meet, the
presuppositions that an accepted answer denies, and the obstacles that its records show.
"""

from __future__ import annotations

from typing import Any, Iterable, Mapping

from .. import findings as rules
from ..findings import Finding, finding
from .assessments import disposition, is_void
from .levels import problem_questions
from .paths import at


def mismatched_request(
    problem: Mapping[str, Any], records: Mapping[str, Mapping[str, Any]]
) -> list[Finding]:
    """Return the associated question of a problem that does not take the request of its demand.

    The associated question is derived from the problem, so it takes the request of the demand. A
    question record that states it addresses the problem and carries the same request.

    >>> problem = {"id": "prob.a", "request": "one", "associated_question": "quest.a"}
    >>> mismatched_request(problem,
    ...                    {"quest.a": {"type": "question", "addresses": "prob.a",
    ...                                 "request": "one"}})
    []
    """
    named = problem.get("associated_question")
    if not named:
        return []
    question = records.get(named) if isinstance(named, str) else None
    if (
        question is None
        or question.get("type") != "question"
        or question.get("addresses") != problem.get("id")
    ):
        return [
            finding(
                rules.COMPLETENESS_MISMATCHED_REQUEST,
                f"associated_question: {named} is no question record addressing"
                f" {problem.get('id')}",
                "associated_question",
            )
        ]
    if question.get("request") != problem.get("request"):
        return [
            finding(
                rules.COMPLETENESS_MISMATCHED_REQUEST,
                f"associated_question: {named} asks under the request {question.get('request')},"
                f" and the problem under {problem.get('request')}",
                "associated_question",
            )
        ]
    return []


def demand_met(
    problem: Mapping[str, Any],
    records: Mapping[str, Mapping[str, Any]],
    classes: Mapping[str, str],
    holders: Mapping[str, Iterable[str]],
) -> bool | None:
    """Return whether the records meet the demand of a problem, or None when no rule applies.

    The demand is met once acts of the researcher settle the demanded results. For a result of a
    claim type, an answer to a question of the problem is accepted, gives a complete
    answer, and holds a satisfied assessment; the number and the completeness that the request
    fixes are those of that direct answer. For a result of a construct type, a record that holds
    the type is stabilized, with a satisfied assessment against the problem. Under the request
    ``decision``, every candidate is settled in view of an assessment: an answer accepted or
    retracted, the record of a construct stabilized or retracted. A type of another class has no
    solving rule, so the function returns None.

    Parameters
    ----------
    problem : mapping
        One filled problem record.
    records : mapping
        The records of the problem, keyed by identifier.
    classes : mapping
        The class of each product type, read from the product-type registry.
    holders : mapping
        The record kinds that hold each product type.
    """
    kind, ident = problem.get("result_type"), problem.get("id")
    klass = classes.get(str(kind))
    if klass not in ("claim", "construct"):
        return None
    questions = problem_questions(str(ident), records)
    assessments = [r for r in records.values() if r.get("type") == "assessment"]

    def assessed(name: str) -> list[Mapping[str, Any]]:
        return [a for a in assessments if a.get("assesses") == name and not is_void(a, records)]

    answers = {
        i: r
        for i, r in records.items()
        if r.get("type") == "answer" and r.get("answers") in questions
    }
    constructs = {
        i: r
        for i, r in records.items()
        if r.get("type") in set(holders.get(str(kind), ()))
        and any(a.get("against") == ident for a in assessed(i))
    }
    if problem.get("request") == "decision":
        candidates = answers if klass == "claim" else constructs
        settled = {"answer": {"accepted", "retracted"}}
        return bool(candidates) and all(
            r.get("status") in settled.get(str(r.get("type")), {"stabilized", "retracted"})
            and bool(assessed(i))
            for i, r in candidates.items()
        )
    if klass == "claim":
        return any(
            r.get("status") == "accepted"
            and at(r, "erotetic_relation.value") == "complete"
            and any(disposition(a) == "satisfied" for a in assessed(i))
            for i, r in answers.items()
        )
    return any(
        r.get("status") == "stabilized"
        and any(a.get("against") == ident and disposition(a) == "satisfied" for a in assessed(i))
        for i, r in constructs.items()
    )


def presupposition_denied(
    problem: Mapping[str, Any], records: Mapping[str, Mapping[str, Any]]
) -> bool | None:
    """Return whether an accepted answer denies a presupposition of the associated question, or None
    when no question is named.

    A corrective answer denies a presupposition of the question that it answers, so an accepted
    corrective answer to the associated question puts the negation of a presupposition of that
    question into the accepted knowledge, which dissolves the problem.

    >>> records = {"ans.a": {"type": "answer", "answers": "quest.a", "status": "accepted",
    ...                      "erotetic_relation": {"value": "corrective"}}}
    >>> presupposition_denied({"associated_question": "quest.a"}, records)
    True
    """
    named = problem.get("associated_question")
    if not named:
        return None
    return any(
        r.get("type") == "answer"
        and r.get("answers") == named
        and r.get("status") == "accepted"
        and at(r, "erotetic_relation.value") == "corrective"
        for r in records.values()
    )


def readable_obstacles(
    problem: Mapping[str, Any],
    records: Mapping[str, Mapping[str, Any]],
    classes: Mapping[str, str],
    holders: Mapping[str, Iterable[str]],
) -> dict[str, bool]:
    """Return, for each knowledge obstacle that the records decide, whether it holds.

    An open gap and unassessed candidates require that the problem exists: its demand is not met
    and no accepted answer denies a presupposition of its associated question. The proposed
    candidates are the answers to the questions of the problem that are neither accepted nor
    retracted: an open gap when none exists, unassessed candidates when some exist and no answer is
    accepted. An unsound presupposition is an accepted answer that denies a presupposition of the
    associated question. An obstacle that the records do not decide is left out.
    """
    found: dict[str, bool] = {}
    denied = presupposition_denied(problem, records)
    if denied is not None:
        found["unsound-presupposition"] = denied
    met = demand_met(problem, records, classes, holders)
    if met is None or denied is None:
        return found
    questions = problem_questions(str(problem.get("id")), records)
    answers = [
        r for r in records.values() if r.get("type") == "answer" and r.get("answers") in questions
    ]
    exists = not met and not denied
    proposed = [r for r in answers if r.get("status") not in ("accepted", "retracted")]
    accepted = [r for r in answers if r.get("status") == "accepted"]
    found["open-gap"] = exists and not proposed
    found["unassessed-candidates"] = exists and bool(proposed) and not accepted
    return found


def misstated_obstacles(
    problem: Mapping[str, Any],
    records: Mapping[str, Mapping[str, Any]],
    classes: Mapping[str, str],
    holders: Mapping[str, Iterable[str]],
) -> list[Finding]:
    """Return every knowledge obstacle that the problem states and its records contradict.

    An obstacle that the records show, such as an open gap, need not be stated, since the views
    compute it from the records; a stated obstacle that the records decide against is a stale claim.
    """
    stated = {
        str(entry.get("obstacle"))
        for entry in problem.get("knowledge_obstacles") or []
        if isinstance(entry, Mapping)
    }
    found = []
    for name, holds in readable_obstacles(problem, records, classes, holders).items():
        if not holds and name in stated:
            found.append(
                finding(
                    rules.COMPLETENESS_UNSUPPORTED_OBSTACLE,
                    f"knowledge_obstacles: the problem states {name}, which its records contradict",
                    "knowledge_obstacles",
                    value=name,
                )
            )
    return found


def unsupported_question_dissolution(
    question: Mapping[str, Any], records: Mapping[str, Mapping[str, Any]]
) -> list[Finding]:
    """Return a status of a question that the accepted answers to it contradict.

    An accepted corrective answer to a question denies one of its presuppositions, which dissolves
    the question as it dissolves a problem whose associated question it is. The status
    ``dissolved`` requires such an answer, and such an answer ends a question still posed or
    refined.

    >>> answer = {"type": "answer", "answers": "quest.a", "status": "accepted",
    ...           "erotetic_relation": {"value": "corrective"}}
    >>> [f.rule.id for f in unsupported_question_dissolution(
    ...     {"id": "quest.a", "status": "posed"}, {"ans.a": answer})]
    ['completeness/unrecorded-dissolution']
    >>> [f.rule.id for f in unsupported_question_dissolution(
    ...     {"id": "quest.a", "status": "dissolved"}, {})]
    ['completeness/unsupported-dissolved']
    """
    name = question.get("id")
    if not name:
        return []
    status = question.get("status")
    denied = bool(presupposition_denied({"associated_question": name}, records))
    if status == "dissolved" and not denied:
        return [
            finding(
                rules.COMPLETENESS_UNSUPPORTED_DISSOLVED,
                "status: dissolved, and no accepted answer denies a presupposition of the question",
                "status",
            )
        ]
    if denied and status in ("posed", "refined"):
        return [
            finding(
                rules.COMPLETENESS_UNRECORDED_DISSOLUTION,
                f"status: {status}, and an accepted answer denies a presupposition of the question",
                "status",
            )
        ]
    return []


def unsupported_outcome(
    problem: Mapping[str, Any],
    records: Mapping[str, Mapping[str, Any]],
    classes: Mapping[str, str],
    holders: Mapping[str, Iterable[str]],
) -> list[Finding]:
    """Return a status of the problem that its records contradict.

    The status ``solved`` requires the demand met, and the status ``dissolved`` an accepted answer
    that denies a presupposition of the associated question; each of these, once the records show
    it, ends a problem still posed or refined. An abandoned problem is not read, since that outcome
    records a decision of the researcher only.
    """
    status, denied = problem.get("status"), presupposition_denied(problem, records)
    if denied is not None:
        if status == "dissolved" and not denied:
            return [
                finding(
                    rules.COMPLETENESS_UNSUPPORTED_DISSOLVED,
                    "status: dissolved, and no accepted answer denies a presupposition of"
                    f" {problem.get('associated_question')}",
                    "status",
                )
            ]
        if denied and status in ("posed", "refined"):
            return [
                finding(
                    rules.COMPLETENESS_UNRECORDED_DISSOLUTION,
                    f"status: {status}, and an accepted answer denies a presupposition of"
                    f" {problem.get('associated_question')}",
                    "status",
                )
            ]
    met = demand_met(problem, records, classes, holders)
    if met is None:
        return []
    if status == "solved" and not met:
        return [
            finding(
                rules.COMPLETENESS_UNSUPPORTED_SOLVED,
                "status: solved, and the records do not meet the demand",
                "status",
            )
        ]
    if met and status in ("posed", "refined"):
        return [
            finding(
                rules.COMPLETENESS_UNRECORDED_SOLUTION,
                f"status: {status}, and the records meet the demand",
                "status",
            )
        ]
    return []
