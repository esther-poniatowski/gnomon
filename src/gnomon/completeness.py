"""
What a filled inquiry must carry, read from the registry that declares it.

The requirements that govern a record are declared in two registries rather than restated here:

- the values a closed field admits, listed per record kind in ``data/vocabularies.yml``;
- the general ones, listed per record kind under ``always`` in ``data/requirements.yml``;
- the ones a level of commitment imposes on a target system or a phenomenon, under
  ``by_commitment``;
- the ones an epistemic aim adds, and the general ones the inquiry produces, under ``by_aim``. An
  inquiry that produces a phenomenon cannot be asked to state that phenomenon in advance, so
  those paths may stay empty.

An empty value means that a field is not filled. Whether an empty field is a gap or a value that
the inquiry will produce is read from the registry, never from the record.

A third kind is neither: a consistency between fields, such as an accuracy marked inapplicable
while outputs are listed for matching. No aim decides those, so each is its own check.

The specification notes document the same requirements and are checked against the registry, so no
check here reads a document.

See Also
--------
data/requirements.yml : the registry these functions read.
"""

from __future__ import annotations

from pathlib import Path
from typing import Any, Iterable, Mapping

import yaml

DATA = Path(__file__).parent / "data"

#: The registry declaring what a filled inquiry must carry.
REQUIREMENT_REGISTRY = DATA / "requirements.yml"

#: The registry declaring the values each closed field admits.
VOCABULARY_REGISTRY = DATA / "vocabularies.yml"

#: The levels of commitment of a target system or a phenomenon, weakest first.
COMMITMENT_LEVELS: tuple[str, ...] = ("identified", "specified")

#: The subject slots of a question, each with the record kind its identifier names.
SUBJECT_SLOTS: Mapping[str, str] = {"target_system": "target-system", "phenomenon": "phenomenon"}

#: The subject slots of a question, each with the one placeholder type it admits.
SLOT_PLACEHOLDERS: Mapping[str, str] = {"target_system": "system", "phenomenon": "phenomenon"}

def is_empty(value: Any) -> bool:
    """Return whether ``value`` leaves its field unfilled: absent, null, or an empty string.

    An empty list or mapping is a value: it states that the block holds no entry.

    >>> [is_empty(v) for v in (None, "", "  ", [], "open")]
    [True, True, True, False, False]
    """
    return value is None or (isinstance(value, str) and not value.strip())


def is_unfilled(value: Any) -> bool:
    """Return whether a required specification is unfilled: empty, or an empty list or mapping."""
    return is_empty(value) or value in ([], {})


def _registry(source: Path | None) -> dict[str, Any]:
    return yaml.safe_load((source or REQUIREMENT_REGISTRY).read_text(encoding="utf-8")) or {}


def requirements_by_aim(source: Path | None = None) -> dict[str, dict[str, list]]:
    """Return, per epistemic aim, the paths its inquiry fixes and the ones it produces.

    Raises
    ------
    ValueError
        If the registry declares no aim.
    """
    by_aim = _registry(source).get("by_aim") or {}
    if not by_aim:
        raise ValueError(f"{(source or REQUIREMENT_REGISTRY).name} declares no aim")
    return {
        aim: {
            "required": [e["path"] for e in (entry.get("required") or [])],
            "to_produce": list(entry.get("to_produce") or []),
        }
        for aim, entry in by_aim.items()
    }


def always_required(kind: str, source: Path | None = None) -> list[str]:
    """Return the specifications every record of ``kind`` carries, whatever the inquiry."""
    return list((_registry(source).get("always") or {}).get(kind) or [])


def record_kinds(source: Path | None = None) -> list[str]:
    """Return every record kind the registry states a general requirement for."""
    return sorted((_registry(source).get("always") or {}))


def requirements_by_commitment(source: Path | None = None) -> dict[str, dict[str, list[str]]]:
    """Return, per level of commitment, the specifications each record kind carries at that level.

    Raises
    ------
    ValueError
        If the registry names a level outside :data:`COMMITMENT_LEVELS`.
    """
    table = _registry(source).get("by_commitment") or {}
    unknown = set(table) - set(COMMITMENT_LEVELS)
    if unknown:
        raise ValueError(f"unknown levels of commitment: {sorted(unknown)}")
    return {level: {kind: list(paths or []) for kind, paths in (table.get(level) or {}).items()}
            for level in COMMITMENT_LEVELS}


def commitment_requirements(
    kind: str, level: str, table: Mapping[str, Mapping[str, list[str]]]
) -> list[str]:
    """Return what a record of ``kind`` carries at ``level``, the weaker levels included.

    >>> table = {"identified": {"phenomenon": ["statement"]}, "specified": {"phenomenon": ["course"]}}
    >>> commitment_requirements("phenomenon", "specified", table)
    ['statement', 'course']
    """
    if level not in COMMITMENT_LEVELS:
        return []
    paths: list[str] = []
    for weaker in COMMITMENT_LEVELS[: COMMITMENT_LEVELS.index(level) + 1]:
        paths += list((table.get(weaker) or {}).get(kind) or [])
    return paths


def at(record: Mapping[str, Any], path: str) -> Any:
    """Return the value a dotted path names, or None when the path does not resolve.

    A step written ``key[]`` traverses the list it names and collects what the rest of the path
    reaches in each entry, so one path states a requirement bearing on every entry of a block.

    >>> at({"virtues": [{"virtue": "generality"}, {"virtue": "economy"}]}, "virtues[].virtue")
    ['generality', 'economy']
    """
    head, marker, tail = path.partition("[].")
    node: Any = record
    for key in head.split("."):
        if not isinstance(node, Mapping):
            return None
        node = node.get(key)
    if not marker:
        return node
    if not isinstance(node, list):
        return None
    return [at(entry, tail) for entry in node if isinstance(entry, Mapping)]


def unmet_general(
    record: Mapping[str, Any],
    paths: list[str],
    produced: frozenset[str] | set[str] = frozenset(),
    label: str = "always required",
) -> list[str]:
    """Return every required specification the record leaves unfilled.

    A specification is unfilled when it is absent, null, an empty string, or an empty list or
    mapping. The aim of the inquiry may produce a required specification, so the caller passes the
    paths that aim produces: those may stay unfilled, since the inquiry supplies their values.
    """
    return [
        f"{label}: {path}"
        for path in paths
        if path not in produced and is_unfilled(at(record, path))
    ]


def unmet_commitment(
    record: Mapping[str, Any],
    table: Mapping[str, Mapping[str, list[str]]],
    produced: frozenset[str] | set[str] = frozenset(),
) -> list[str]:
    """Return every specification that the level of commitment of the record requires and it lacks.

    A record at ``identified`` fixes its referent; a record at ``specified`` also writes the
    declarations that make it checkable. A record stating no admitted level is reported by the
    general requirement on ``commitment`` and by the vocabulary, so it is not reported here.
    """
    level = record.get("commitment")
    paths = commitment_requirements(str(record.get("type")), str(level), table)
    return unmet_general(record, paths, produced, label=f"commitment {level} requires")


def occurrence_by_category(source: Path | None = None) -> dict[str, list[str]]:
    """Return, per phenomenon category, the occurrence classes that the category admits."""
    table = _registry(source).get("occurrence_by_category") or {}
    return {str(category): list(classes or []) for category, classes in table.items()}


def mismatched_occurrence(
    phenomenon: Mapping[str, Any], table: Mapping[str, list[str]]
) -> list[str]:
    """Return the occurrence class that the category of the phenomenon does not admit.

    A particular occurrence is one token of a state, a process or an event. A structural property
    holds at each point of the course, as a state does. A regularity relates occurrences without
    being one, and a capacity is a disposition, so neither takes an occurrence class. An empty
    field leaves the pair unfilled, and nothing is reported.

    >>> table = {"regularity": ["not-applicable"], "particular-occurrence": ["state", "process", "event"]}
    >>> mismatched_occurrence({"category": "regularity", "occurrence": "event"}, table)
    ['occurrence: event is no occurrence class of a regularity, which admits not-applicable']
    """
    category, occurrence = phenomenon.get("category"), phenomenon.get("occurrence")
    if not isinstance(category, str) or not isinstance(occurrence, str):
        return []
    if is_empty(category) or is_empty(occurrence) or category not in table:
        return []
    admitted = table[category]
    if occurrence in admitted:
        return []
    return [f"occurrence: {occurrence} is no occurrence class of a {category}, which admits {' or '.join(admitted)}"]


def placeholder_types(source: Path | None = None) -> frozenset[str]:
    """Return the types a placeholder of a question slot may take, as the vocabulary lists them."""
    return admitted_values("question", source).get("subject.placeholder", frozenset())


def unresolved_slots(
    question: Mapping[str, Any],
    records: Mapping[str, Mapping[str, Any]],
    types: Iterable[str],
) -> list[str]:
    """Return every subject slot that holds neither an identified record nor a typed placeholder.

    A slot of a question schema awaits an item of a type from a closed list, described in words,
    and the type fits the slot: the target-system slot awaits a system, and the phenomenon slot a
    phenomenon. A slot of a question names a record that fixes its referent, so the record exists, has the kind
    the slot expects, and carries an identification. Both checks are decidable, and the stronger
    level, a record whose declarations resolve, is checked by the resolution of its symbols.

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
        value, where = subject.get(slot), f"subject.{slot}"
        if isinstance(value, Mapping):
            awaited = value.get("placeholder")
            if awaited not in admitted:
                found.append(f"{where}: the placeholder type {awaited!r} is not admitted")
            elif awaited != SLOT_PLACEHOLDERS[slot]:
                found.append(f"{where}: the placeholder type {awaited!r} does not fit the slot, which awaits {SLOT_PLACEHOLDERS[slot]!r}")
            if not value.get("description"):
                found.append(f"{where}: the placeholder carries no description")
            continue
        if not isinstance(value, str) or is_empty(value):
            found.append(f"{where}: holds neither a record identifier nor a placeholder")
            continue
        record = records.get(value)
        if record is None:
            found.append(f"{where}: no record carries the identifier {value}")
        elif record.get("type") != kind:
            found.append(f"{where}: {value} is a {record.get('type')} record, not a {kind} record")
        elif not (record.get("identification") or {}).get("description"):
            found.append(f"{where}: {value} carries no identification, so its referent is not fixed")
    return found


def unresolved_question_references(
    question: Mapping[str, Any], records: Mapping[str, Mapping[str, Any]]
) -> list[str]:
    """Return every problem, linked question and background that a question names and that is missing.

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
        found.append(f"addresses: {addressed} is no problem record")
    for index, link in enumerate(question.get("links") or []):
        if not isinstance(link, Mapping):
            continue
        other, via = link.get("question"), link.get("via")
        if kind_of(other) != "question":
            found.append(f"links[{index}]: {other} is no question record")
        elif other == question.get("id"):
            found.append(f"links[{index}]: a question is linked to itself")
        if via is not None and kind_of(via) is None:
            found.append(f"links[{index}]: no record carries the identifier {via}")
    subject = question.get("subject") or {}
    target = subject.get("target_system")
    for name in subject.get("background") or []:
        if kind_of(name) != "background":
            found.append(f"subject.background: {name} is no background record")
        elif isinstance(target, str) and records[name].get("describes") != target:
            found.append(f"subject.background: {name} describes another target than {target}")
    return found


def unstated_function_sense(question: Mapping[str, Any]) -> list[str]:
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
    return ["task.function_sense: a functional relation is requested without its sense of function"]


def malformed_credence(assessment: Mapping[str, Any]) -> list[str]:
    """Return the credence that is no degree of belief, or that states no basis.

    A credence is a number between zero and one; a value outside that interval is no probability,
    and a value without its basis cannot be revised when the evidence changes.
    """
    credence = assessment.get("credence")
    if credence is None:
        return []
    if not isinstance(credence, Mapping):
        return ["credence: holds neither a value nor a basis"]
    found = []
    value = credence.get("value")
    if isinstance(value, bool) or not isinstance(value, (int, float)) or not 0 <= value <= 1:
        found.append(f"credence.value: {value!r} is no number between 0 and 1")
    if not credence.get("basis"):
        found.append("credence.basis: the value states no basis")
    return found


def disposition(assessment: Mapping[str, Any], erotetic_relation: str | None = None) -> str:
    """Return the disposition of an assessment, read from its admissibility and warrant verdicts.

    An answer satisfies its question only when it is admissible and warranted, so one failed test
    decides the disposition. Without a failure, a pending verdict withholds it. A corrective answer
    shows that a presupposition of its question is false, so it cannot satisfy that question: the
    disposition that would be ``satisfied`` is ``corrective`` instead.

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
    """
    tests = assessment.get("tests") or {}
    verdicts = [
        (entry or {}).get("verdict")
        for level in ("admissibility", "warrant")
        for entry in (tests.get(level) or {}).values()
    ]
    if "fail" in verdicts:
        return "not-satisfied"
    if any(verdict not in ("pass", "not-applicable") for verdict in verdicts):
        return "withheld"
    return "corrective" if erotetic_relation == "corrective" else "satisfied"


def unmet_by_aim(
    question: Mapping[str, Any],
    records: Mapping[str, Mapping[str, Any]],
    required: Mapping[str, dict[str, list]],
) -> list[str]:
    """Return every specification the aim of this question requires and the records leave open.

    Parameters
    ----------
    question : mapping
        One filled question record.
    records : mapping
        The records its paths reach, keyed by the prefix that names them: ``question``,
        ``phenomenon`` and ``target-system``.
    required : mapping
        The table the registry declares.

    Notes
    -----
    An aim fixes what an answer must deliver, so it requires a specification to be filled and
    never a value that specification takes. Which value is right is a judgement of the inquiry,
    and a rule that reaches inside a field belongs to a consistency check between fields.
    """
    aim = at(question, "task.epistemic_aim")
    missing = []
    for path in (required.get(str(aim)) or {}).get("required", []):
        prefix, _, rest = path.partition(".")
        if is_unfilled(at(records.get(prefix, {}), rest)):
            missing.append(f"{aim} requires {path}")
    return missing


def contradictory_accuracy(question: Mapping[str, Any]) -> list[str]:
    """Return the matches a question lists while declaring that accuracy does not apply.

    No aim decides whether an answer is matched against a measurement: an inquiry over a formal
    model class may match measured exponents, and one seeking a theorem may match nothing. The
    rule is therefore a consistency between fields rather than a requirement of an aim.
    """
    accuracy = at(question, "task.required_accuracy") or {}
    if accuracy.get("standard") != "not-applicable":
        return []
    return [
        f"task.required_accuracy.{key} is listed although accuracy does not apply"
        for key in ("outputs_to_match", "structures_to_match")
        if accuracy.get(key)
    ]


def unrealized_link(question: Mapping[str, Any], answer: Mapping[str, Any]) -> list[str]:
    """Return the link a question asks for and the answer does not supply.

    A question may bound the explanans to substrate-specific variables, to substrate-independent
    ones, or to the link between them. The third is not a third kind of variable: it obliges the
    answer to give both descriptions and the mapping that carries one onto the other, since a
    question about how a role is realized is answered by neither description alone. The two
    descriptions are declared in the ordinary blocks; the mapping is what the answer would
    otherwise leave to a reader to reconstruct.
    """
    if at(question, "task.admissible_explanans.substrate") != "mapping":
        return []
    realizations = answer.get("realizations") or []
    if not realizations:
        return ["the question asks for a link, and the answer maps no quantity onto its realization"]
    return [
        f"realizations[{index}] names what it realizes without saying by what"
        for index, entry in enumerate(realizations)
        if isinstance(entry, Mapping) and not (entry.get("realizes") and entry.get("by"))
    ]


def unjustified_explanans_bound(question: Mapping[str, Any]) -> list[str]:
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
    return ["task.admissible_explanans states an axis, and no justification says why the answer is bound to it"]


def unstated_standing(question: Mapping[str, Any]) -> list[str]:
    """Return every virtue the question weighs without saying what failing it costs.

    A virtue bears on an answer in one of two ways, and which one is not derivable from the virtue
    itself: constitutive of the product, so that an answer lacking it is inadmissible however
    accurate, or preferred, so that it ranks answers that are already admissible. No aim decides
    this either, since an inquiry may hold an account to intelligibility whatever product it seeks
    and another may treat the same virtue as a tie-breaker. The question therefore states it, and
    an entry that does not leaves the product test unable to say what it applies.
    """
    return [
        f"virtues[{index}].standing is unstated for {entry.get('virtue') or 'an unnamed virtue'}"
        for index, entry in enumerate(question.get("virtues") or [])
        if isinstance(entry, Mapping) and not entry.get("standing")
    ]


def malformed_restrictions(
    question: Mapping[str, Any], variables: Iterable[str]
) -> list[str]:
    """Return every domain restriction that does not say what it holds, or holds it wrongly.

    A restriction names one quantity and the set it is held to, or it names none and carries the
    expression it holds under; carrying both says the same thing twice and carrying neither says
    nothing. An entry naming no quantity needs a name, since nothing else identifies it. How a
    quantity is held — clamped, initial, stationary, without an event — applies to something that
    varies, so an entry naming a parameter states no such kind: a parameter is already fixed.

    Parameters
    ----------
    question : mapping
        One filled question record.
    variables : iterable of str
        The symbols its target system declares as variables rather than as parameters.
    """
    varying = set(variables)
    found = []
    for entry in at(question, "subject.domain.restrictions") or []:
        if not isinstance(entry, Mapping):
            continue
        held = entry.get("of")
        symbol = held.rsplit("#", 1)[-1] if isinstance(held, str) else None
        label = entry.get("name") or held or "an entry"
        carried = [key for key in ("values", "expression") if entry.get(key) is not None]
        if len(carried) != 1:
            found.append(f"restrictions.{label}: carries {len(carried)} of values and expression")
        if not held and not entry.get("name"):
            found.append("restrictions: an entry names neither a quantity nor itself")
        if entry.get("restriction") and symbol not in varying:
            found.append(
                f"restrictions.{label}: states how it is held although it names no variable"
            )
    return found


def undecided_boundaries(record: Mapping[str, Any]) -> list[str]:
    """Return every external system whose constraint is neither written nor declared absent.

    An external system either imposes something on the variables it shares, written as
    expressions, or imposes nothing beyond their declared value sets, written as an empty list
    ``[]``. An empty value says neither. A boundary that was never written then reads exactly like
    one that imposes nothing, so the quantities a constraint would have named are never missed: an
    overshoot diagnostic, a measurement coverage. Where a constraint is a genuine scientific
    unknown, the record says so with a ``maturity`` entry rather than by leaving the field empty.
    """
    return [
        f"external_systems.{entry.get('symbol')}: constrains is empty, so the boundary is named"
        " without being decided"
        for entry in record.get("external_systems") or []
        if isinstance(entry, Mapping) and is_empty(entry.get("constrains"))
    ]


def admitted_values(kind: str, source: Path | None = None) -> dict[str, frozenset[str]]:
    """Return, per field of ``kind``, the values it admits.

    A key names the block enclosing the field and the field itself, so ``terms.type`` is the
    type of a term and ``.status`` is the status of the record. An empty field holds no value, so
    no vocabulary bears on it.
    """
    registry = yaml.safe_load((source or VOCABULARY_REGISTRY).read_text(encoding="utf-8")) or {}
    fields = (registry.get("vocabularies") or {}).get(kind) or {}
    return {
        name: frozenset(entry["value"] for entry in values)
        for name, values in fields.items()
    }


def inadmissible_values(record: Mapping[str, Any], admitted: Mapping[str, frozenset[str]]) -> list[str]:
    """Return every closed field of the record holding a value its vocabulary does not admit."""
    found: list[str] = []

    def visit(node: Any, block: str) -> None:
        if isinstance(node, Mapping):
            for key, value in node.items():
                vocabulary = admitted.get(f"{block}.{key}")
                if vocabulary is not None:
                    for item in value if isinstance(value, list) else [value]:
                        if isinstance(item, str) and item not in vocabulary:
                            found.append(f"{block or 'record'}.{key}: {item} is not admitted")
                if isinstance(value, (Mapping, list)):
                    visit(value, block or key)
        elif isinstance(node, list):
            for item in node:
                visit(item, block)

    for key, value in record.items():
        vocabulary = admitted.get(f".{key}")
        if vocabulary is not None:
            for item in value if isinstance(value, list) else [value]:
                if isinstance(item, str) and item not in vocabulary:
                    found.append(f"record.{key}: {item} is not admitted")
        if isinstance(value, (Mapping, list)):
            visit(value, key)
    return found
