"""
The checks of a question: its slots and its references, its task, its domain and the virtues that
it weighs.
"""

from __future__ import annotations

import re
from typing import Any, Iterable, Mapping

from .. import findings as rules
from ..expressions import parse_expression
from ..findings import Entry, Finding, finding
from ..identifiers import split_reference
from ..vocabulary.declarations import declarations
from .paths import at, is_empty

#: The accuracy standards that admit no stated tolerance: two state none, and `order-of-magnitude`
#: fixes its own metric and bound.
UNTOLERATED_STANDARDS = frozenset({"qualitative", "structural-only", "order-of-magnitude"})

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


def foreign_backgrounds(
    question: Mapping[str, Any], records: Mapping[str, Mapping[str, Any]]
) -> list[Finding]:
    """Return each background admitted by a question that describes another target.

    An admitted background states its laws over the quantities of the target that it describes, so
    it must describe the target of the question. A name that resolves to no record, or to a record
    of another kind, is reported by the resolution of references and by the checks of relations.

    >>> records = {"bg.a": {"type": "background", "describes": "system.b"}}
    >>> question = {"subject": {"target_system": "system.a", "background": ["bg.a"]}}
    >>> [f.text for f in foreign_backgrounds(question, records)]
    ['subject.background: bg.a describes another target than system.a']
    """
    subject = question.get("subject") or {}
    target = subject.get("target_system")
    found = []
    for index, name in enumerate(subject.get("background") or []):
        record = records.get(name) if isinstance(name, str) else None
        if (
            isinstance(record, Mapping)
            and record.get("type") == "background"
            and isinstance(target, str)
            and record.get("describes") != target
        ):
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
    rule is therefore a consistency between fields rather than a requirement of an aim. A standard
    that states no tolerance, or fixes its own, as ``order-of-magnitude`` does, admits no stated
    tolerance either.
    """
    accuracy = at(question, "task.required_accuracy") or {}
    standard = accuracy.get("standard")
    if standard in UNTOLERATED_STANDARDS:
        return [
            finding(
                rules.COMPLETENESS_CONTRADICTORY_ACCURACY,
                f"task.required_accuracy.outputs_to_match: a tolerance is stated although the"
                f" standard {standard} admits none",
                "task",
                "required_accuracy",
                "outputs_to_match",
                Entry(index, entry),
                "tolerance",
            )
            for index, entry in enumerate(accuracy.get("outputs_to_match") or [])
            if isinstance(entry, Mapping) and not is_empty(entry.get("tolerance"))
        ]
    if standard != "not-applicable":
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


#: An identifier inside a factor: a bare symbol, or a dotted reference to a record or its unit.
FACTOR_TOKEN = re.compile(r"[A-Za-z_][A-Za-z_0-9]*(?:\.[A-Za-z_][A-Za-z_0-9-]*)*")


def _factor_tokens(factor: Mapping[str, Any]) -> set[str]:
    """Return the identifiers that the content of an explanans factor names."""
    texts = [factor.get("holds")]
    for key in ("bears_on", "appeals_to", "through"):
        value = factor.get(key)
        texts += value if isinstance(value, list) else [value]
    return {
        token for text in texts if isinstance(text, str) for token in FACTOR_TOKEN.findall(text)
    }


def unlinked_explanans(
    question: Mapping[str, Any],
    answer: Mapping[str, Any],
    records: Mapping[str, Mapping[str, Any]],
) -> list[Finding]:
    """Return each link ``explanans-from`` of the answered question that the answer leaves unmet.

    The link bounds the admissible answers: each answer states an explanans factor over the
    phenomenon that the link shares with the linked question, so that the factor names a symbol
    declared by that phenomenon or a reference into its record. Each finding concerns the answer.

    >>> question = {"links": [{"question": "quest.a.geometry", "relation": "explanans-from",
    ...                        "via": "phen.a.geometry"}]}
    >>> records = {"phen.a.geometry": {"type": "phenomenon", "observables": [{"symbol": "D"}]}}
    >>> factor = {"id": "dim", "holds": "D > 3"}
    >>> unlinked_explanans(question, {"aim_block": {"explanation": {"factors": [factor]}}}, records)
    []
    >>> [f.rule.id for f in unlinked_explanans(question, {}, records)]
    ['completeness/unlinked-explanans']
    """
    factors = [
        f for f in at(answer, "aim_block.explanation.factors") or [] if isinstance(f, Mapping)
    ]
    found = []
    for link in question.get("links") or []:
        if not isinstance(link, Mapping) or link.get("relation") != "explanans-from":
            continue
        via = str(link.get("via") or "")
        phenomenon = records.get(via)
        if not isinstance(phenomenon, Mapping):
            continue
        symbols = {d.symbol for d in declarations(phenomenon)}
        if any(
            token in symbols or token == via or token.startswith(f"{via}.")
            for factor in factors
            for token in _factor_tokens(factor)
        ):
            continue
        found.append(
            finding(
                rules.COMPLETENESS_UNLINKED_EXPLANANS,
                f"the question draws its explanans from {via} through {link.get('question')},"
                " and no explanans factor of the answer names that phenomenon",
                "aim_block",
                "explanation",
                "factors",
            )
        )
    return found


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


def quantity_symbols(target: Mapping[str, Any]) -> set[str]:
    """Return the symbols of the variables and the parameters of a target system.

    >>> sorted(quantity_symbols({"variables": [{"symbol": "u"}], "parameters": [{"symbol": "Re"}],
    ...                          "index_sets": [{"symbol": "t"}]}))
    ['Re', 'u']
    """
    return {
        e["symbol"]
        for block in ("variables", "parameters")
        for e in target.get(block) or []
        if isinstance(e, Mapping) and isinstance(e.get("symbol"), str)
    }


def misstated_limit(question: Mapping[str, Any], quantities: Iterable[str]) -> list[Finding]:
    """Return the domain limit of a question when it is no relation ``q -> v`` whose left side is
    a variable or a parameter of the target system.

    A limit states the value that one quantity of the target approaches, as ``Re -> infinity``, and
    the question then concerns the limit system. A left side that names an index set, an operator
    or an expression names no quantity that can approach a value. A text that the grammar does not
    cover is reported by the resolution check, so it is not reported here.

    >>> question = {"subject": {"domain": {"limit": {"expression": "Re -> infinity"}}}}
    >>> misstated_limit(question, {"Re"})
    []
    >>> [f.text for f in misstated_limit(question, {"U"})]
    ['subject.domain.limit.expression: Re is no variable or parameter of the target']
    >>> question["subject"]["domain"]["limit"]["expression"] = "Re > 1000"
    >>> [f.text for f in misstated_limit(question, {"Re"})]
    ['subject.domain.limit.expression: Re > 1000 states no limit q -> v']
    """
    text = at(question, "subject.domain.limit.expression")
    tree = parse_expression(text)
    if tree is None:
        return []
    where = "subject.domain.limit.expression"
    place = ("subject", "domain", "limit", "expression")
    if tree[0] != "cmp" or tree[1] != "->":
        message = f"{where}: {str(text).strip()} states no limit q -> v"
    elif tree[2][0] != "sym":
        message = f"{where}: the left side of the limit is no symbol"
    elif tree[2][1] not in set(quantities):
        message = f"{where}: {tree[2][1]} is no variable or parameter of the target"
    else:
        return []
    return [finding(rules.COMPLETENESS_MISSTATED_LIMIT, message, *place)]


def malformed_restrictions(question: Mapping[str, Any], variables: Iterable[str]) -> list[Finding]:
    """Return every domain restriction that does not say what it holds, or holds it wrongly.

    A restriction names one quantity and the set it is held to, or it names none and carries the
    expression it holds under; carrying both says the same thing twice and carrying neither says
    nothing. An entry naming no quantity needs a name, since nothing else identifies it. How a
    quantity is held — clamped, initial, stationary, without an event — applies to something that
    varies, so an entry naming a fixed parameter states no such kind. A parameter that the course
    of the phenomenon lists as varying changes along that course, so it can be held like a variable.
    A quantity held without an event names that event, and an entry of another kind names none.

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
        if (entry.get("restriction") == "without-event") != bool(entry.get("event")):
            found.append(
                finding(
                    rules.COMPLETENESS_EXCLUDED_EVENT,
                    f"restrictions.{label}: "
                    + (
                        "the restriction without-event names no excluded event"
                        if entry.get("restriction") == "without-event"
                        else "names an event although its restriction is not without-event"
                    ),
                    *where,
                    "event",
                )
            )
    return found
