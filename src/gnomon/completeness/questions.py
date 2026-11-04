"""
The checks of a question: its slots and its references, its task, its domain and the virtues that
it weighs.
"""

from __future__ import annotations

from typing import Any, Iterable, Mapping

from .. import findings as rules
from ..findings import Entry, Finding, finding
from ..identifiers import split_reference
from .paths import at, is_empty

#: The subject slots of a question, each with the record kind its identifier names.
SUBJECT_SLOTS: Mapping[str, str] = {"target_system": "target-system", "phenomenon": "phenomenon"}


#: The subject slots of a question, each with the one placeholder type it admits.
SLOT_PLACEHOLDERS: Mapping[str, str] = {"target_system": "system", "phenomenon": "phenomenon"}


def unresolved_slots(
    question: Mapping[str, Any],
    records: Mapping[str, Mapping[str, Any]],
    types: Iterable[str],
) -> list[Finding]:
    """Return every subject slot that holds neither an identified record nor a typed placeholder.

    A slot of a question schema awaits an item of a type from a closed list, described in words, and
    the type fits the slot: the target-system slot awaits a system, and the phenomenon slot a
    phenomenon. A slot of a question names a record that fixes its referent, so the record exists,
    has the kind the slot expects, and carries an identification. Both checks are decidable, and the
    stronger level, a record whose declarations resolve, is checked by the resolution of its
    symbols.

    Parameters
    ----------
    question : mapping
        One filled question record.
    records : mapping
        The records of the problem, keyed by identifier.
    types : iterable of str
        The types a placeholder may take.
    """
    admitted = set(types)
    subject = question.get("subject") or {}
    found = []
    for slot, kind in SUBJECT_SLOTS.items():
        value, where, field = subject.get(slot), f"subject.{slot}", ("subject", slot)
        if isinstance(value, Mapping):
            awaited = value.get("placeholder")
            if awaited not in admitted:
                found.append(
                    finding(
                        rules.COMPLETENESS_UNADMITTED_PLACEHOLDER,
                        f"{where}: the placeholder type {awaited!r} is not admitted",
                        *field,
                        "placeholder",
                    )
                )
            elif awaited != SLOT_PLACEHOLDERS[slot]:
                found.append(
                    finding(
                        rules.COMPLETENESS_MISFIT_PLACEHOLDER,
                        f"{where}: the placeholder type {awaited!r} does not fit the slot, which"
                        f" awaits {SLOT_PLACEHOLDERS[slot]!r}",
                        *field,
                        "placeholder",
                    )
                )
            if not value.get("description"):
                found.append(
                    finding(
                        rules.COMPLETENESS_UNDESCRIBED_PLACEHOLDER,
                        f"{where}: the placeholder carries no description",
                        *field,
                        "description",
                    )
                )
            continue
        if not isinstance(value, str) or is_empty(value):
            found.append(
                finding(
                    rules.COMPLETENESS_UNRESOLVED_SLOT,
                    f"{where}: holds neither a record identifier nor a placeholder",
                    *field,
                )
            )
            continue
        record = records.get(value)
        if record is None:
            found.append(
                finding(
                    rules.COMPLETENESS_UNKNOWN_SLOT_RECORD,
                    f"{where}: no record carries the identifier {value}",
                    *field,
                )
            )
        elif record.get("type") != kind:
            found.append(
                finding(
                    rules.COMPLETENESS_MISTYPED_SLOT_RECORD,
                    f"{where}: {value} is a {record.get('type')} record, not a {kind} record",
                    *field,
                )
            )
        elif not (record.get("identification") or {}).get("description"):
            found.append(
                finding(
                    rules.COMPLETENESS_UNIDENTIFIED_SLOT_RECORD,
                    f"{where}: {value} carries no identification, so its referent is not fixed",
                    *field,
                )
            )
    return found


def unresolved_question_references(
    question: Mapping[str, Any], records: Mapping[str, Mapping[str, Any]]
) -> list[Finding]:
    """Return every problem, linked question and background that a question names and that is
    missing.

    A question names the problem it serves, the questions it is linked to with the shared record
    carrying the link, and the background records whose laws it admits. Each name resolves to a
    record of the expected kind, and an admitted background describes the target of the question,
    since its laws are stated over the quantities of that target.
    """

    def kind_of(identifier: Any) -> Any:
        return (records.get(identifier) or {}).get("type") if isinstance(identifier, str) else None

    found = []
    addressed = question.get("addresses")
    if addressed is not None and kind_of(addressed) != "problem":
        found.append(
            finding(
                rules.COMPLETENESS_UNADDRESSED_PROBLEM,
                f"addresses: {addressed} is no problem record",
                "addresses",
            )
        )
    for index, link in enumerate(question.get("links") or []):
        if not isinstance(link, Mapping):
            continue
        other, via = link.get("question"), link.get("via")
        if kind_of(other) != "question":
            found.append(
                finding(
                    rules.COMPLETENESS_LINK_NOT_QUESTION,
                    f"links[{index}]: {other} is no question record",
                    "links",
                    index,
                    "question",
                )
            )
        elif other == question.get("id"):
            found.append(
                finding(
                    rules.COMPLETENESS_SELF_LINK,
                    f"links[{index}]: a question is linked to itself",
                    "links",
                    index,
                    "question",
                )
            )
        if via is not None and kind_of(via) is None:
            found.append(
                finding(
                    rules.COMPLETENESS_UNKNOWN_LINK_RECORD,
                    f"links[{index}]: no record carries the identifier {via}",
                    "links",
                    index,
                    "via",
                )
            )
    subject = question.get("subject") or {}
    target = subject.get("target_system")
    for index, name in enumerate(subject.get("background") or []):
        if kind_of(name) != "background":
            found.append(
                finding(
                    rules.COMPLETENESS_NOT_BACKGROUND,
                    f"subject.background: {name} is no background record",
                    "subject",
                    "background",
                    index,
                )
            )
        elif isinstance(target, str) and records[name].get("describes") != target:
            found.append(
                finding(
                    rules.COMPLETENESS_FOREIGN_BACKGROUND,
                    f"subject.background: {name} describes another target than {target}",
                    "subject",
                    "background",
                    index,
                )
            )
    return found


def unstated_function_sense(question: Mapping[str, Any]) -> list[Finding]:
    """Return the functional question that does not say which sense of function it requests.

    A function in the causal-role sense is the contribution of a part to a capacity of the system
    that contains it; a function in the etiological sense is the effect for which the part was
    selected. The two call for different answers, a functional analysis or a selection history, so
    a question requesting a functional relation states which one it requests.
    """
    task = question.get("task") or {}
    if task.get("requested_relation") != "functional":
        return []
    if task.get("function_sense") in ("causal-role", "etiological"):
        return []
    return [
        finding(
            rules.COMPLETENESS_UNSTATED_FUNCTION_SENSE,
            "task.function_sense: a functional relation is requested without its sense of function",
            "task",
            "function_sense",
        )
    ]


def unbounded_aim(
    question: Mapping[str, Any],
    records: Mapping[str, Mapping[str, Any]],
    aims: Mapping[str, Iterable[str]],
) -> list[Finding]:
    """Return the aim of a question that the type of result of its problem does not admit.

    The demand of a problem bounds the aim of each question that serves it. The bound reads the type
    of result only: a condition that the demand table attaches to an aim, such as a closed
    background for modal knowledge, is not checked.

    >>> records = {"prob.a": {"type": "problem", "result_type": "explanation"}}
    >>> texts = [f.text for f in unbounded_aim({"addresses": "prob.a",
    ...                                         "task": {"epistemic_aim": "prediction"}},
    ...                                        records, {"explanation": ["explanation"]})]
    >>> texts
    ['task.epistemic_aim: prediction does not serve a demand for explanation']
    """
    addresses = question.get("addresses")
    problem = records.get(addresses) if isinstance(addresses, str) else None
    aim = at(question, "task.epistemic_aim")
    kind = (problem or {}).get("result_type")
    if not aim or not isinstance(kind, str) or kind not in aims or aim in set(aims[kind]):
        return []
    return [
        finding(
            rules.COMPLETENESS_UNBOUNDED_AIM,
            f"task.epistemic_aim: {aim} does not serve a demand for {kind}",
            "task",
            "epistemic_aim",
        )
    ]


def contradictory_accuracy(question: Mapping[str, Any]) -> list[Finding]:
    """Return the matches a question lists while declaring that accuracy does not apply.

    No aim decides whether an answer is matched against a measurement: an inquiry over a formal
    model class may match measured exponents, and one seeking a theorem may match nothing. The
    rule is therefore a consistency between fields rather than a requirement of an aim.
    """
    accuracy = at(question, "task.required_accuracy") or {}
    if accuracy.get("standard") != "not-applicable":
        return []
    return [
        finding(
            rules.COMPLETENESS_CONTRADICTORY_ACCURACY,
            f"task.required_accuracy.{key} is listed although accuracy does not apply",
            "task",
            "required_accuracy",
            key,
        )
        for key in ("outputs_to_match", "structures_to_match")
        if accuracy.get(key)
    ]


def unrealized_link(question: Mapping[str, Any], answer: Mapping[str, Any]) -> list[Finding]:
    """Return the link a question asks for and the answer does not supply.

    A question may bound the explanans to substrate-specific variables, to substrate-independent
    ones, or to the link between them. The third is not a third kind of variable: it obliges the
    answer to give both descriptions and the mapping that carries one onto the other, since a
    question about how a role is realized is answered by neither description alone. The two
    descriptions are declared in the ordinary blocks; the mapping is what the answer would
    otherwise leave to a reader to reconstruct. Each finding concerns the answer.
    """
    if at(question, "task.admissible_explanans.substrate") != "mapping":
        return []
    realizations = at(answer, "claim.realizations") or []
    if not realizations:
        return [
            finding(
                rules.COMPLETENESS_UNREALIZED_LINK,
                "the question asks for a link, and the answer maps no quantity onto its"
                " realization",
                "claim",
                "realizations",
            )
        ]
    return [
        finding(
            rules.COMPLETENESS_INCOMPLETE_REALIZATION,
            f"claim.realizations[{index}] names what it realizes without saying by what",
            "claim",
            "realizations",
            index,
        )
        for index, entry in enumerate(realizations)
        if isinstance(entry, Mapping) and not (entry.get("realizes") and entry.get("by"))
    ]


def unanchored_explicandum(
    question: Mapping[str, Any], records: Mapping[str, Mapping[str, Any]]
) -> list[Finding]:
    """Return the explicandum of a question of explication that no explicandum of its problem
    anchors.

    The explicandum of such a question is not a slot: it enters through the use that a pointer of
    the problem anchors, so it names a term among the explicanda of the problem that the question
    addresses.

    >>> problem = {"explicanda": [{"term": "disentangled", "pointer": "doi:10.1000/a"}]}
    >>> question = {"addresses": "prob.a.b",
    ...             "task": {"epistemic_aim": "explication", "explicandum": "modular"}}
    >>> [f.text for f in unanchored_explicandum(question, {"prob.a.b": problem})]
    ['task.explicandum: modular is no explicandum of prob.a.b']
    """
    if at(question, "task.epistemic_aim") != "explication":
        return []
    term = at(question, "task.explicandum")
    problem = records.get(str(question.get("addresses"))) or {}
    terms = {str(e.get("term")) for e in problem.get("explicanda") or [] if isinstance(e, Mapping)}
    if is_empty(term) or term in terms:
        return []
    return [
        finding(
            rules.COMPLETENESS_UNANCHORED_EXPLICANDUM,
            f"task.explicandum: {term} is no explicandum of {question.get('addresses')}",
            "task",
            "explicandum",
        )
    ]


def unjustified_explanans_bound(question: Mapping[str, Any]) -> list[Finding]:
    """Return the bound on the explanans that states an axis without saying why.

    A question that leaves the bound empty takes the default: proportionality with the phenomenon
    selects the variables of the explanans, so an empty bound is complete as it stands. A stated
    axis narrows the explanans beyond that default, and only a justification records why the
    research program binds the answer to those variables and what an answer drawing on others
    would lose. A bound that the maturity marks open is still being written, so its justification
    may wait. An empty list of compositional parts states an axis: the system as a whole.
    """
    bound = at(question, "task.admissible_explanans") or {}
    if bound.get("compositional") is None and bound.get("substrate") is None:
        return []
    if bound.get("justification"):
        return []
    if (question.get("maturity") or {}).get("task.admissible_explanans"):
        return []
    return [
        finding(
            rules.COMPLETENESS_UNJUSTIFIED_EXPLANANS_BOUND,
            "task.admissible_explanans states an axis, and no justification says why the answer is"
            " bound to it",
            "task",
            "admissible_explanans",
            "justification",
        )
    ]


def unstated_standing(question: Mapping[str, Any]) -> list[Finding]:
    """Return every virtue the question weighs without saying what failing it costs.

    A virtue bears on an answer in one of two ways, and which one is not derivable from the virtue
    itself: constitutive of the product, so that an answer lacking it is inadmissible however
    accurate, or preferred, so that it ranks answers that are already admissible. No aim decides
    this either, since an inquiry may hold an account to intelligibility whatever product it seeks
    and another may treat the same virtue as a tie-breaker. The question therefore states it, and
    an entry that does not leaves the product test unable to say what it applies.
    """
    return [
        finding(
            rules.COMPLETENESS_UNSTATED_STANDING,
            f"virtues[{index}].standing is unstated for"
            f" {entry.get('virtue') or 'an unnamed virtue'}",
            "virtues",
            index,
            "standing",
        )
        for index, entry in enumerate(question.get("virtues") or [])
        if isinstance(entry, Mapping) and not entry.get("standing")
    ]


def varying_symbols(
    target: Mapping[str, Any], phenomenon: Mapping[str, Any] | None = None
) -> set[str]:
    """Return the symbols that vary along the course of a phenomenon of the target.

    The variables of the target vary, and so does each parameter that the course of the phenomenon
    lists under ``varies``, as the role test of a quantity reads a parameter.

    >>> varying_symbols({"variables": [{"symbol": "x"}], "parameters": [{"symbol": "w"}]},
    ...                 {"course": {"varies": ["w"]}}) == {"x", "w"}
    True
    """
    found = {
        e["symbol"]
        for e in target.get("variables") or []
        if isinstance(e, Mapping) and isinstance(e.get("symbol"), str)
    }
    course = (phenomenon or {}).get("course")
    if isinstance(course, Mapping):
        found |= {s for s in course.get("varies") or [] if isinstance(s, str)}
    return found


def malformed_restrictions(question: Mapping[str, Any], variables: Iterable[str]) -> list[Finding]:
    """Return every domain restriction that does not say what it holds, or holds it wrongly.

    A restriction names one quantity and the set it is held to, or it names none and carries the
    expression it holds under; carrying both says the same thing twice and carrying neither says
    nothing. An entry naming no quantity needs a name, since nothing else identifies it. How a
    quantity is held — clamped, initial, stationary, without an event — applies to something that
    varies, so an entry naming a fixed parameter states no such kind. A parameter that the course
    of the phenomenon lists as varying changes along that course, so it can be held like a variable.

    Parameters
    ----------
    question : mapping
        One filled question record.
    variables : iterable of str
        The symbols that vary along the course of its phenomenon, as :func:`varying_symbols`
        collects them.
    """
    varying = set(variables)
    found = []
    for index, entry in enumerate(at(question, "subject.domain.restrictions") or []):
        if not isinstance(entry, Mapping):
            continue
        where = ("subject", "domain", "restrictions", Entry(index, entry))
        held = entry.get("of")
        symbol = (split_reference(held) or ("", held))[1] if isinstance(held, str) else None
        label = entry.get("name") or held or "an entry"
        carried = [key for key in ("values", "expression") if entry.get(key) is not None]
        if len(carried) != 1:
            found.append(
                finding(
                    rules.COMPLETENESS_RESTRICTION_CONTENT,
                    f"restrictions.{label}: carries {len(carried)} of values and expression",
                    *where,
                )
            )
        if not held and not entry.get("name"):
            found.append(
                finding(
                    rules.COMPLETENESS_ANONYMOUS_RESTRICTION,
                    "restrictions: an entry names neither a quantity nor itself",
                    *where,
                )
            )
        if entry.get("restriction") and symbol not in varying:
            found.append(
                finding(
                    rules.COMPLETENESS_RESTRICTION_WITHOUT_VARIABLE,
                    f"restrictions.{label}: states how it is held although it names no quantity"
                    " that varies",
                    *where,
                    "restriction",
                )
            )
    return found
