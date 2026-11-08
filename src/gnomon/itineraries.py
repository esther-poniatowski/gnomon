"""
Itineraries of inquiry, checked against the registries of epistemic activities and product types.

An itinerary lists activity instances, its steps. Each step names a registered activity, the
products that it takes and the product that it produces, each typed by the registry of product
types, and the verdict of the norm that judges it. Two registries in package data declare what a
step may state, so no check here reads a document:

- ``registries/activities.yml``: per activity, its family, its input and output types, its norm,
  its mode and its context;
- ``registries/product-types.yml``: per product type, the record kinds that hold it, and the
  state in which a record of such a kind holds it.

The check is decidable. It compares types and identifiers, and never judges whether a norm is met:
the verdict records that judgement.

See Also
--------
data/registries/activities.yml : the activities a step may instantiate.
data/registries/product-types.yml : the types its inputs and output take.
"""

from __future__ import annotations

import difflib
import re
from collections import Counter
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Callable, Iterable, Mapping

import yaml

from . import findings as rules
from .findings import Entry, Finding, Key, finding

DATA = Path(__file__).parent / "data"

#: The registry declaring the epistemic activities.
ACTIVITY_REGISTRY = DATA / "registries" / "activities.yml"

#: The registry declaring the types of epistemic product.
PRODUCT_TYPE_REGISTRY = DATA / "registries" / "product-types.yml"

#: The registry declaring the values each closed field admits, including the verdicts and modes.
VOCABULARY_REGISTRY = DATA / "vocabularies.yml"

#: The value of ``record`` for a type held outside the records, reached by a pointer.
EXTERNAL = "external pointer"

#: The value of ``record`` for a type that no record kind holds yet.
TO_CREATE = "to-create"

#: The record kind whose status is an attitude, the only kind that an ``attitude`` qualifier
#: restricts.
ATTITUDE_HOLDER = "answer"


@dataclass(frozen=True)
class Slot:
    """One input that an activity takes.

    Attributes
    ----------
    types : frozenset of str
        The product types the input may take; more than one when the activity admits any of them.
    least : int
        The fewest inputs that fill the slot.
    most : int or None
        The most inputs that fill the slot, or None when it takes any number from ``least``.
    attitudes : frozenset of str
        The attitudes under which a referenced answer may hold the type; empty when any serves.
    """

    types: frozenset[str]
    least: int = 1
    most: int | None = 1
    attitudes: frozenset[str] = frozenset()

    def admits(self, count: int) -> bool:
        """Return whether ``count`` inputs fill the slot."""
        return count >= self.least and (self.most is None or count <= self.most)


@dataclass(frozen=True)
# pylint: disable-next=too-many-instance-attributes  # one attribute per key of an entry
class Activity:
    """One epistemic activity, as the registry declares it."""

    # pylint: disable-next=disallowed-name  # the field mirrors the key `id` of an entry
    id: str
    family: str
    inputs: tuple[Slot, ...]
    output: str
    norm: str
    mode: str
    context: str
    output_values: Mapping[str, tuple[str, ...]] = field(default_factory=dict)


#: The form of the date of a judgment: YYYY-MM-DD.
DATE = re.compile(r"\d{4}-\d{2}-\d{2}")


def _load(path: Path) -> dict[str, Any]:
    return yaml.safe_load(path.read_text(encoding="utf-8")) or {}


def slot(entry: Any) -> Slot:
    """Return the slot that one input entry of the registry declares.

    A bare type takes one record. A mapping names one type under ``type`` or alternatives under
    ``types``, and qualifies the number with ``several`` (two or more) or ``count`` (exactly that
    many), and ``optional`` lets the step omit the input; a ``role`` leaves the type unchanged. An
    ``attitude``, one value or a list, restricts the attitudes under which a referenced answer holds
    the type, since the attitude of a claim is an attribute of the claim, not a type.

    >>> slot("problem")
    Slot(types=frozenset({'problem'}), least=1, most=1, attitudes=frozenset())
    >>> slot({"type": "model", "several": True, "role": "family"}).admits(3)
    True
    >>> slot({"type": "model", "count": 2}).admits(1)
    False
    >>> sorted(slot({"types": ["target-claim", "model"]}).types)
    ['model', 'target-claim']
    >>> sorted(slot({"type": "target-claim", "attitude": "hypothesized"}).attitudes)
    ['hypothesized']
    >>> slot({"type": "model", "optional": True}).admits(0)
    True
    """
    if isinstance(entry, str):
        return Slot(frozenset({entry}))
    declared = entry.get("types") or [entry.get("type")]
    types = frozenset(str(name) for name in declared)
    attitude = entry.get("attitude") or []
    attitudes = frozenset(
        [attitude] if isinstance(attitude, str) else (str(value) for value in attitude)
    )
    if entry.get("several"):
        return Slot(types, least=0 if entry.get("optional") else 2, most=None, attitudes=attitudes)
    count = int(entry.get("count", 1))
    return Slot(types, least=0 if entry.get("optional") else count, most=count, attitudes=attitudes)


def required_attitudes(act: Activity, kind: str) -> frozenset[str]:
    """Return the attitudes under which a record must hold ``kind`` to enter ``act``; empty when any
    serves.

    An input of one type may fill several slots of an activity, so the attitudes of those slots are
    united, and a slot that names no attitude admits every attitude.
    """
    held = [entry for entry in act.inputs if kind in entry.types]
    if not held or any(not entry.attitudes for entry in held):
        return frozenset()
    return frozenset().union(*(entry.attitudes for entry in held))


def activities(source: Path | None = None) -> dict[str, Activity]:
    """Return every registered activity, keyed by identifier.

    Raises
    ------
    ValueError
        If the registry declares no activity.
    """
    registry = _load(source or ACTIVITY_REGISTRY)
    found = {
        str(entry["id"]): Activity(
            id=str(entry["id"]),
            family=str(entry.get("family")),
            inputs=tuple(slot(item) for item in entry.get("inputs") or []),
            output=str(entry.get("output")),
            norm=str(entry.get("norm")),
            mode=str(entry.get("mode")),
            context=str(entry.get("context")),
            output_values={
                str(name): tuple(str(value) for value in values or [])
                for name, values in (entry.get("output_values") or {}).items()
            },
        )
        for entry in registry.get("activities") or []
    }
    if not found:
        raise ValueError(f"{(source or ACTIVITY_REGISTRY).name} declares no activity")
    return found


def product_types(source: Path | None = None) -> dict[str, Mapping[str, Any]]:
    """Return every product type with its entry: the record kinds that hold it and their state."""
    registry = _load(source or PRODUCT_TYPE_REGISTRY)
    return {str(entry["id"]): entry for entry in registry.get("product_types") or []}


def type_classes(types: Mapping[str, Mapping[str, Any]] | None = None) -> dict[str, str]:
    """Return the class of each product type, as the inventory of epistemic objects sorts it."""
    types = product_types() if types is None else types
    return {name: str(entry.get("class")) for name, entry in types.items()}


def type_holders(types: Mapping[str, Mapping[str, Any]] | None = None) -> dict[str, frozenset[str]]:
    """Return, per product type, the record kinds that hold it; a type that no record holds maps to
    none.

    >>> type_holders({"model": {"record": ["model"]}, "design": {"record": "to-create"}})
    {'model': frozenset({'model'}), 'design': frozenset()}
    """
    types = product_types() if types is None else types
    return {
        name: frozenset(entry["record"]) if isinstance(entry.get("record"), list) else frozenset()
        for name, entry in types.items()
    }


def construct_record_kinds(types: Mapping[str, Mapping[str, Any]] | None = None) -> frozenset[str]:
    """Return the record kinds that hold a product of a construct type.

    >>> sorted(construct_record_kinds({"model": {"class": "construct", "record": ["model"]},
    ...                                "design": {"class": "construct", "record": "to-create"},
    ...                                "verdict": {"class": "evaluative",
    ...                                            "record": ["assessment"]}}))
    ['model']
    """
    types = product_types() if types is None else types
    return frozenset(
        kind
        for entry in types.values()
        if entry.get("class") == "construct" and isinstance(entry.get("record"), list)
        for kind in entry["record"]
    )


def has_placeholder(question: Mapping[str, Any]) -> bool:
    """Return whether some subject slot of a question holds a placeholder rather than a record."""
    subject = question.get("subject") or {}
    return any(isinstance(subject.get(slot), Mapping) for slot in ("target_system", "phenomenon"))


def question_form(question: Mapping[str, Any]) -> str:
    """Return ``question`` once every subject slot names a record and the request is fixed, else
    ``schema``.

    >>> question_form({"subject": {"phenomenon": "phen.a"}, "request": "one"})
    'question'
    >>> question_form({"subject": {"phenomenon": "phen.a"}})
    'schema'
    """
    return "question" if not has_placeholder(question) and question.get("request") else "schema"


def holds(record: Mapping[str, Any], entry: Mapping[str, Any]) -> bool:
    """Return whether ``record``, in its present state, holds a product of the type of ``entry``.

    The kind of the record must be listed, its state must satisfy the ``when`` mapping (the level
    of commitment, the form of a question, or the status), and, when the entry names the fields
    that hold the type, one of them must be filled.

    >>> holds({"type": "question", "subject": {"phenomenon": {"placeholder": "phenomenon"}}},
    ...       {"record": ["question"], "when": {"form": "schema"}})
    True
    >>> holds({"type": "target-system", "commitment": "specified"},
    ...       {"record": ["target-system"], "when": {"commitment": ["identified"]}})
    False
    >>> entry = {"record": ["model"], "fields": {"model": ["laws[].warrant=derived"]}}
    >>> holds({"type": "model", "laws": [{"warrant": "posited"}]}, entry)
    False
    >>> holds({"type": "model", "laws": [{"warrant": "posited"}, {"warrant": "derived"}]}, entry)
    True
    """
    kinds = entry.get("record")
    if not isinstance(kinds, list) or record.get("type") not in kinds:
        return False
    when = entry.get("when") or {}
    if "commitment" in when and record.get("commitment") not in when["commitment"]:
        return False
    if "status" in when and record.get("status") not in when["status"]:
        return False
    if "form" in when and question_form(record) != when["form"]:
        return False
    fields = entry.get("fields")
    paths = fields.get(str(record.get("type")), []) if isinstance(fields, Mapping) else fields or []
    return not paths or any(filled(record, path) for path in paths)


def filled(record: Mapping[str, Any], path: str) -> bool:
    """Return whether a field path of the registry of product types holds content in ``record``.

    A segment ending in ``[]`` ranges over the items of a list, and a final ``=value`` requires that
    value.

    >>> filled({"laws": [{"warrant": "derived"}]}, "laws[].warrant=derived")
    True
    >>> filled({"aim_block": {"explanation": {}}}, "aim_block.explanation"), filled({}, "data")
    (False, False)
    """
    path, _, value = path.partition("=")
    nodes: list[Any] = [record]
    for segment in path.split("."):
        name, many = (segment[:-2], True) if segment.endswith("[]") else (segment, False)
        nodes = [node.get(name) for node in nodes if isinstance(node, Mapping)]
        if many:
            nodes = [item for node in nodes if isinstance(node, list) for item in node]
    if value:
        return any(node == value for node in nodes)
    return any(node not in (None, "", [], {}) for node in nodes)


def record_types(record: Mapping[str, Any], types: Mapping[str, Mapping[str, Any]]) -> list[str]:
    """Return every product type that ``record`` holds in its present state, in registry order."""
    return [name for name, entry in types.items() if holds(record, entry)]


def _closed(name: str, source: Path | None = None, kind: str = "itinerary") -> frozenset[str]:
    """Return the values that the vocabulary registry admits for the field ``name`` of ``kind``."""
    vocabulary = (_load(source or VOCABULARY_REGISTRY).get("vocabularies") or {}).get(kind) or {}
    return frozenset(entry["value"] for entry in vocabulary.get(name) or [])


def _unknown_output_values(
    act: Activity, types: Mapping[str, Any], entry: tuple[str, Key]
) -> list[Finding]:
    """Return each output value of an activity that the kinds holding its output do not admit."""
    holders = type_holders(types).get(act.output, frozenset())
    found = []
    for name, values in act.output_values.items():
        vocabulary = set().union(*(_closed(f".{name}", kind=holder) for holder in holders))
        found += [
            finding(
                rules.REGISTRY_UNKNOWN_OUTPUT_VALUE,
                f"{act.id}: {value} is no {name} of a {act.output}",
                *entry,
                "output_values",
                name,
                value=value,
            )
            for value in values
            if value not in vocabulary
        ]
    return found


def _malformed_activity(
    act: Activity, types: Mapping[str, Any], admitted: set[str], held_as: set[str]
) -> list[Finding]:
    """Return what one activity of the registry names that the other registries do not admit."""
    entry = ("activities", Key(act.id))
    named = [(t, (*entry, "inputs", index)) for index, s in enumerate(act.inputs) for t in s.types]
    found = [
        finding(
            rules.REGISTRY_UNKNOWN_PRODUCT_TYPE,
            f"{act.id}: {kind} is no product type",
            *where,
            value=kind,
        )
        for kind, where in [*named, (act.output, (*entry, "output"))]
        if kind not in types
    ]
    found += [
        finding(
            rules.REGISTRY_UNADMITTED_ATTITUDE,
            f"{act.id}: {value} is no attitude of an answer",
            *entry,
            "inputs",
            index,
            value=value,
        )
        for index, held in enumerate(act.inputs)
        for value in sorted(held.attitudes - held_as)
    ]
    if act.mode not in admitted:
        text = f"{act.id}: {act.mode} is no admitted mode"
        found.append(finding(rules.REGISTRY_UNADMITTED_MODE, text, *entry, "mode"))
    found += _unknown_output_values(act, types, entry)
    if act.norm != f"norm.{act.id}":
        text = f"{act.id}: its norm {act.norm} is not the test norm.{act.id}"
        found.append(finding(rules.REGISTRY_FOREIGN_NORM, text, *entry, "norm"))
    return found


def malformed_registry(
    acts: Mapping[str, Activity],
    types: Mapping[str, Any],
    modes: Iterable[str],
    attitudes: Iterable[str] | None = None,
) -> list[Finding]:
    """Return every activity that names a type, a mode, an attitude or a norm the registries do not
    admit.

    The itinerary check trusts the activity registry, so the registry is itself checked: every input
    and output names a product type, every attitude that qualifies an input is an attitude of an
    answer, every mode is admitted, and every norm is the named test of its own activity. Each
    finding concerns the registry file, under its list ``activities`` keyed by activity.
    """
    admitted = set(modes)
    held_as = set(_closed(".status", kind=ATTITUDE_HOLDER) if attitudes is None else attitudes)
    return [f for act in acts.values() for f in _malformed_activity(act, types, admitted, held_as)]


@dataclass(frozen=True)
class _Itinerary:
    """What every check of a step of one itinerary reads.

    Attributes
    ----------
    records : mapping
        The records of the problem, keyed by identifier.
    types : mapping
        The registry of product types.
    states : callable or None
        A reader of a record at a revision, or None when no history is available.
    by_id : mapping
        The steps of the itinerary, keyed by identifier.
    own : str
        The prefix that names a step of this itinerary in full: its identifier and a dot.
    closed : mapping
        The admitted values of the closed fields ``verdict``, ``mode`` and ``acts_on`` of a step.
    """

    records: Mapping[str, Mapping[str, Any]]
    types: Mapping[str, Any]
    states: Callable[[str, str], Mapping[str, Any] | None] | None
    by_id: Mapping[str, Mapping[str, Any]]
    own: str
    closed: Mapping[str, frozenset[str]]


@dataclass(frozen=True)
class _Step:
    """One step of an itinerary whose activity is registered, with the itinerary that holds it."""

    itinerary: _Itinerary
    position: int
    step: Mapping[str, Any]
    act: Activity

    @property
    def name(self) -> str:
        """The identifier of the step."""
        return str(self.step.get("id"))

    @property
    def where(self) -> str:
        """The path of the step, which opens each message."""
        return f"steps.{self.name}"

    @property
    def at(self) -> tuple[str, Entry]:
        """The field path of the step, which places each finding."""
        return ("steps", Entry(self.position, self.step))


def _unaddressed(
    itinerary: Mapping[str, Any], records: Mapping[str, Mapping[str, Any]]
) -> list[Finding]:
    """Report an itinerary that addresses no problem record and no question record."""
    target = itinerary.get("addresses")
    if (records.get(str(target)) or {}).get("type") in ("problem", "question"):
        return []
    return [
        finding(
            rules.ITINERARY_UNADDRESSED,
            f"addresses: {target} is no problem or question record",
            "addresses",
        )
    ]


def _repeated_steps(steps: list[tuple[int, Mapping[str, Any]]]) -> list[Finding]:
    """Report each identifier that names several steps."""
    counts = Counter(str(s.get("id")) for _, s in steps)
    return [
        finding(
            rules.ITINERARY_REPEATED_STEP,
            f"steps: the identifier {name} names several steps",
            "steps",
            value=name,
        )
        for name, count in counts.items()
        if count > 1
    ]


def _inputs_of(step: Mapping[str, Any]) -> list[tuple[int, Mapping[str, Any]]]:
    """Return the inputs of a step that are mappings, each with its position."""
    return [
        (i, item) for i, item in enumerate(step.get("inputs") or []) if isinstance(item, Mapping)
    ]


def _input_counts(s: _Step) -> list[Finding]:
    """Report an input slot that the step fills in the wrong number, and an input type not taken."""
    act, found = s.act, []
    counts = Counter(str(item.get("type")) for _, item in _inputs_of(s.step))
    for held in act.inputs:
        supplied = sum(counts[t] for t in held.types)
        if not held.admits(supplied):
            found.append(
                finding(
                    rules.ITINERARY_UNFILLED_INPUT,
                    f"{s.where}: {act.id} takes {_describe(held)} of"
                    f" {' or '.join(sorted(held.types))},"
                    f" and the step gives {supplied}",
                    *s.at,
                    "inputs",
                    value="|".join(sorted(held.types)),
                )
            )
    accepted = {t for held in act.inputs for t in held.types}
    found += [
        finding(
            rules.ITINERARY_UNACCEPTED_INPUT,
            f"{s.where}: {act.id} takes no input of type {kind}",
            *s.at,
            "inputs",
            value=kind,
        )
        for kind in sorted(counts)
        if kind not in accepted
    ]
    return found


def _step_input(s: _Step, index: int, item: Mapping[str, Any]) -> tuple[list[Finding], str | None]:
    """Check one input that names a step of the itinerary; return its findings and the step named.

    The step named is None when the input names no step of this itinerary, and the input is then
    read as a reference to a record.
    """
    ref, own = item.get("ref"), s.itinerary.own
    local = str(ref)[len(own) :] if isinstance(ref, str) and ref.startswith(own) else None
    producer = s.itinerary.by_id.get(local) if local is not None else None
    if local is None or producer is None:
        return [], None
    kind = str(item.get("type"))
    made = (producer.get("output") or {}).get("type")
    if made == kind:
        return [], local
    text = f"{s.where}: the step {ref} produces {made}, not {kind}"
    return [finding(rules.ITINERARY_MISTYPED_STEP_INPUT, text, *s.at, "inputs", index)], local


def _resolved_input(
    s: _Step, index: int, item: Mapping[str, Any]
) -> tuple[Mapping[str, Any] | None, list[Finding]]:
    """Return the record that an input names, at its revision when it names one, or the finding."""
    given = (*s.at, "inputs", index)
    ref, revision = item.get("ref"), item.get("as_of")
    record = s.itinerary.records.get(ref) if isinstance(ref, str) else None
    if isinstance(ref, str) and isinstance(revision, str) and revision:
        states = s.itinerary.states
        record = states(ref, revision) if states is not None else None
        if record is None:
            unavailable = getattr(states, "unavailable", None)
            if callable(unavailable) and unavailable(ref, revision):
                text = (
                    f"{s.where}: the revision {revision} is absent from this clone, which lacks the"
                    f" full history, so {ref} is not read at it"
                )
                rule = rules.ITINERARY_UNAVAILABLE_HISTORY
            else:
                text = f"{s.where}: {ref} cannot be read at the revision {revision}"
                rule = rules.ITINERARY_UNREADABLE_STATE
            return None, [finding(rule, text, *given, "as_of")]
    if record is None:
        own = s.itinerary.own
        if isinstance(ref, str) and ref in s.itinerary.by_id:
            text = (
                f"{s.where}: {ref} names a step of this itinerary without its itinerary; write it"
                f" in full, as {own}{ref}"
            )
        elif isinstance(ref, str) and "." not in ref:
            text = (
                f"{s.where}: {ref} is neither a step nor a record; a step is named in full, as"
                f" {own}<step>"
            )
        else:
            text = f"{s.where}: {ref} is neither a step nor a record"
        return None, [finding(rules.ITINERARY_UNRESOLVED_INPUT, text, *given)]
    return record, []


def _held_input(
    s: _Step, index: int, item: Mapping[str, Any], record: Mapping[str, Any]
) -> list[Finding]:
    """Check that a record named by an input holds its type, under an attitude its slot admits."""
    given = (*s.at, "inputs", index)
    kind, ref = str(item.get("type")), item.get("ref")
    if not holds(record, s.itinerary.types.get(kind) or {}):
        text = f"{s.where}: {ref} holds {_held(record, s.itinerary.types)}, not {kind}"
        return [finding(rules.ITINERARY_MISTYPED_RECORD_INPUT, text, *given)]
    attitudes = (
        required_attitudes(s.act, kind) if record.get("type") == ATTITUDE_HOLDER else frozenset()
    )
    if attitudes and record.get("status") not in attitudes:
        text = (
            f"{s.where}: {ref} is {record.get('status')}, and {s.act.id} takes a {kind}"
            f" held as {' or '.join(sorted(attitudes))}"
        )
        return [finding(rules.ITINERARY_UNADMITTED_ATTITUDE, text, *given)]
    return []


def _record_input(s: _Step, index: int, item: Mapping[str, Any]) -> list[Finding]:
    """Check one input that names a record: its state, its type and the attitude that it holds."""
    kind, ref = str(item.get("type")), item.get("ref")
    held_by = (s.itinerary.types.get(kind) or {}).get("record")
    if held_by == EXTERNAL:
        return []
    if held_by == TO_CREATE:
        text = f"{s.where}: no record holds a {kind}, so its input names a step, and {ref} is none"
        return [finding(rules.ITINERARY_INPUT_WITHOUT_PRODUCER, text, *s.at, "inputs", index)]
    record, failure = _resolved_input(s, index, item)
    return failure if record is None else _held_input(s, index, item, record)


def _input_references(s: _Step) -> tuple[list[Finding], set[str]]:
    """Check each input reference of a step; return the findings and the steps that it names."""
    found: list[Finding] = []
    named: set[str] = set()
    for index, item in _inputs_of(s.step):
        step_found, local = _step_input(s, index, item)
        if local is not None:
            found += step_found
            named.add(local)
        else:
            found += _record_input(s, index, item)
    return found, named


def _state_change(s: _Step, product: str) -> list[Finding]:
    """Report a change of knowledge state whose record shows no change from its earlier revision."""
    output = _block(s.step, "output") or {}
    before, states = output.get("before"), s.itinerary.states
    earlier = (
        states(product, before)
        if states is not None and isinstance(before, str) and before
        else None
    )
    if earlier is None:
        text = f"{s.where}: the change of {product} names no readable revision before it"
    elif earlier.get("status") == s.itinerary.records[product].get("status"):
        text = (
            f"{s.where}: the status of {product} is {earlier.get('status')} before and"
            " after the step"
        )
    else:
        return []
    return [finding(rules.ITINERARY_UNCHANGED_STATE, text, *s.at, "output", "before")]


def _output_record(s: _Step, product: str, made: Any) -> list[Finding]:
    """Report an output record that does not hold the output type, or holds a value not admitted."""
    record, act, types = s.itinerary.records[product], s.act, s.itinerary.types
    found = []
    if not holds(record, types.get(str(made)) or {}):
        text = f"{s.where}: {product} holds {_held(record, types)}, not {made}"
        found.append(finding(rules.ITINERARY_MISTYPED_OUTPUT_RECORD, text, *s.at, "output", "ref"))
    for name, admitted in act.output_values.items():
        value = record.get(name)
        if isinstance(value, str) and value and value not in admitted:
            text = (
                f"{s.where}: {product} has the {name} {value}, and {act.id} produces"
                f" a {act.output} of the {name} {' or '.join(admitted)}"
            )
            found.append(
                finding(rules.ITINERARY_UNADMITTED_OUTPUT_VALUE, text, *s.at, "output", "ref")
            )
    return found


def _output(s: _Step) -> list[Finding]:
    """Check the output of a step: its type, the record that it names, and a change of state."""
    output = _block(s.step, "output") or {}
    made, product = output.get("type"), output.get("ref")
    found = []
    if made != s.act.output:
        text = f"{s.where}: {s.act.id} produces {s.act.output}, and the step states {made}"
        found.append(finding(rules.ITINERARY_MISTYPED_OUTPUT, text, *s.at, "output", "type"))
    if not isinstance(product, str) or product not in s.itinerary.records:
        return found
    if made == "knowledge-state-change":
        found += _state_change(s, product)
    return found + _output_record(s, product, made)


def _norm(s: _Step) -> list[Finding]:
    """Check the norm of a step: its test, its verdict, and the evidence and date of a verdict."""
    norm = _block(s.step, "norm") or {}
    verdict, found = norm.get("verdict"), []
    if norm.get("test") != s.act.norm:
        text = (
            f"{s.where}: the norm of {s.act.id} is {s.act.norm}, and the step names"
            f" {norm.get('test')}"
        )
        found.append(finding(rules.ITINERARY_FOREIGN_NORM, text, *s.at, "norm", "test"))
    if verdict not in s.itinerary.closed["verdict"]:
        text = f"{s.where}: {verdict!r} is no verdict"
        return [*found, finding(rules.ITINERARY_UNKNOWN_VERDICT, text, *s.at, "norm", "verdict")]
    if verdict == "pending":
        return found
    evidence = norm.get("evidence")
    if not isinstance(evidence, str) or not evidence.strip():
        text = f"{s.where}: the verdict {verdict} states no evidence"
        found.append(finding(rules.ITINERARY_UNJUSTIFIED_VERDICT, text, *s.at, "norm", "evidence"))
    if not DATE.fullmatch(str(norm.get("judged"))):
        text = f"{s.where}: the verdict {verdict} states no date of judgment, written YYYY-MM-DD"
        found.append(finding(rules.ITINERARY_UNJUSTIFIED_VERDICT, text, *s.at, "norm", "judged"))
    return found


def _rationale(s: _Step) -> list[Finding]:
    """Check that the rationale of a step serves a question or a problem, and names a condition."""
    rationale = _block(s.step, "rationale") or {}
    served = (s.itinerary.records.get(str(rationale.get("serves"))) or {}).get("type")
    acts_on = s.itinerary.closed["acts_on"]
    if served not in ("question", "problem"):
        text = (
            f"{s.where}: the rationale serves {rationale.get('serves')}, which is no question"
            " or problem record"
        )
        return [finding(rules.ITINERARY_UNSERVED, text, *s.at, "rationale", "serves")]
    if served == "question" and rationale.get("acts_on") not in acts_on:
        text = (
            f"{s.where}: the rationale serves a question and names no condition or act among"
            f" {', '.join(sorted(acts_on))}"
        )
        return [finding(rules.ITINERARY_UNSERVED, text, *s.at, "rationale", "acts_on")]
    return []


def _stated(block: Mapping[str, Any], key: str) -> bool:
    """Return whether a block states a non-blank text under ``key``."""
    value = block.get(key)
    return isinstance(value, str) and bool(value.strip())


def _constructors(s: _Step) -> list[Finding]:
    """Check the branch and the iteration of a step, which construct the order of the steps."""
    act, found = s.act, []
    branch = _block(s.step, "branch")
    if branch is not None:
        other = s.itinerary.by_id.get(str(branch.get("otherwise")))
        if not _stated(branch, "condition"):
            text = f"{s.where}: the branch states no condition"
            found.append(
                finding(rules.ITINERARY_MALFORMED_CONSTRUCTOR, text, *s.at, "branch", "condition")
            )
        if other is None or ((other.get("output") or {}).get("type")) != act.output:
            text = f"{s.where}: the branch names no step that produces {act.output} otherwise"
            found.append(
                finding(rules.ITINERARY_MALFORMED_CONSTRUCTOR, text, *s.at, "branch", "otherwise")
            )
    iterate = _block(s.step, "iterate")
    if iterate is not None:
        if not _stated(iterate, "until"):
            text = f"{s.where}: the iteration states no criterion of termination"
            found.append(
                finding(rules.ITINERARY_MALFORMED_CONSTRUCTOR, text, *s.at, "iterate", "until")
            )
        if act.output not in {t for held in act.inputs for t in held.types}:
            text = (
                f"{s.where}: {act.id} takes no input of its output type {act.output}, so it"
                " cannot repeat on it"
            )
            found.append(finding(rules.ITINERARY_MALFORMED_CONSTRUCTOR, text, *s.at, "iterate"))
    return found


def _mode(s: _Step) -> list[Finding]:
    """Report a stated mode that is not admitted or is not the mode of the activity."""
    mode = s.step.get("mode")
    if mode is None or (mode in s.itinerary.closed["mode"] and mode == s.act.mode):
        return []
    text = f"{s.where}: {s.act.id} proceeds by {s.act.mode} inference, and the step states {mode}"
    return [finding(rules.ITINERARY_MISMATCHED_MODE, text, *s.at, "mode")]


def _derivation(s: _Step) -> list[Finding]:
    """Report a passed step of the activity derivation that names no derivation record, and a
    derivation that records none of its consequences in the output record of the step."""
    named = s.step.get("derivation")
    norm = s.step.get("norm")
    verdict = norm.get("verdict") if isinstance(norm, Mapping) else None
    if not isinstance(named, str) or not named:
        if s.act.id == "derivation" and verdict == "pass":
            text = f"{s.where}: the step passes its norm and names no derivation record"
            return [finding(rules.ITINERARY_UNRECORDED_DERIVATION, text, *s.at)]
        return []
    derivation = s.itinerary.records.get(named)
    output = s.step.get("output")
    made = output.get("ref") if isinstance(output, Mapping) else None
    if not isinstance(derivation, Mapping) or not isinstance(made, str) or made.startswith("itin."):
        return []
    recorded = [
        str(c.get("record"))
        for c in derivation.get("consequences") or []
        if isinstance(c, Mapping) and c.get("record")
    ]
    if any(r == made or r.startswith(made + ".") for r in recorded):
        return []
    text = f"{s.where}: {named} records none of its consequences in {made}, the output of the step"
    return [finding(rules.ITINERARY_FOREIGN_DERIVATION, text, *s.at, "derivation", value=named)]


def _question_version(s: _Step) -> list[Finding]:
    """Check that a step revising a question reads it at an earlier version than the present one.

    A revision of a question raises its version, so the state that the step read, at the revision
    named by ``as_of``, holds an earlier version than the question holds now.
    """
    revised = str((_block(s.step, "revises") or {}).get("record") or "")
    if s.act.id != "question-revision" and not revised.startswith("quest."):
        return []
    states, found = s.itinerary.states, []
    for index, item in _inputs_of(s.step):
        ref, revision = item.get("ref"), item.get("as_of")
        present = s.itinerary.records.get(str(ref))
        if item.get("type") != "question" or states is None or not revision or present is None:
            continue
        earlier = states(str(ref), str(revision))
        if earlier is not None and str(earlier.get("version")) == str(present.get("version")):
            text = (
                f"{s.where}: {ref} holds version {present.get('version')} both at {revision} and"
                " now, so the revision raised no version"
            )
            found.append(
                finding(
                    rules.ITINERARY_UNVERSIONED_QUESTION_REVISION,
                    text,
                    *s.at,
                    "inputs",
                    index,
                    "as_of",
                )
            )
    return found


#: The checks of a step whose activity is registered, in the order of their reports.
STEP_CHECKS: tuple[Callable[[_Step], list[Finding]], ...] = (
    _output,
    _derivation,
    _norm,
    _rationale,
    _constructors,
    _mode,
    _question_version,
)


def _step_findings(
    context: _Itinerary, position: int, step: Mapping[str, Any], acts: Mapping[str, Activity]
) -> tuple[list[Finding], set[str]]:
    """Check one step; return its findings and the steps that its inputs name."""
    act = acts.get(str(step.get("activity")))
    if act is None:
        close = difflib.get_close_matches(str(step.get("activity")), list(acts), n=3)
        hint = f"did you mean {' or '.join(close)}? " if close else ""
        text = (
            f"steps.{step.get('id')}: {step.get('activity')} is no registered activity; {hint}the"
            " activities are listed in src/gnomon/data/registries/activities.yml"
        )
        place = ("steps", Entry(position, step), "activity")
        return [finding(rules.ITINERARY_UNKNOWN_ACTIVITY, text, *place)], set()
    s = _Step(context, position, step, act)
    referenced, named = _input_references(s)
    found = _input_counts(s) + referenced
    for check in STEP_CHECKS:
        found += check(s)
    return found, named


def itinerary_problems(
    itinerary: Mapping[str, Any],
    records: Mapping[str, Mapping[str, Any]],
    acts: Mapping[str, Activity] | None = None,
    types: Mapping[str, Any] | None = None,
    states: Callable[[str, str], Mapping[str, Any] | None] | None = None,
) -> list[Finding]:
    """Return every step of the itinerary that the registries or the records contradict.

    The five conditions of the itinerary check, stated in the overview of the activity taxonomy,
    apply:

    - every step names a registered activity;
    - the input types of a step fill the inputs of its activity, in number as well as in type, and
      its output type is the output of that activity;
    - each input reference names a record that holds the input type in its present state, or at
      the revision that the input names by ``as_of``, under an attitude that its slot admits, or a
      step producing that type, named in full by the identifier of the itinerary followed by its
      own; a type held outside the records takes any pointer;
    - the references between steps form an acyclic graph;
    - every verdict is admitted, and a verdict ``pass`` or ``fail`` states its evidence and its
      date.

    Five checks of the record fields complete them: the itinerary addresses a problem or a question;
    no two steps share an identifier; an output reference, once given, names a record that holds the
    output type; the norm of a step is the test of its activity, and a stated mode is its mode; the
    rationale of a step serves a question or a problem, and names a condition when it serves a
    question. A step that names a derivation finds one of its consequences in its output record,
    and a passed step of the activity derivation names its derivation.

    Parameters
    ----------
    itinerary : mapping
        One filled itinerary record.
    records : mapping
        The records of the problem, keyed by identifier.
    acts, types : mapping, optional
        The two registries, read from package data when omitted.
    states : callable, optional
        A reader of a record at a revision, as :func:`gnomon.history.git_states` returns; without
        it, an input named ``as_of`` a revision is reported as unreadable.
    """
    acts = activities() if acts is None else acts
    steps = [
        (index, step)
        for index, step in enumerate(itinerary.get("steps") or [])
        if isinstance(step, Mapping)
    ]
    context = _Itinerary(
        records=records,
        types=product_types() if types is None else types,
        states=states,
        by_id={str(step.get("id")): step for _, step in steps},
        own=f"{itinerary.get('id')}.",
        closed={name: _closed(f"steps.{name}") for name in ("verdict", "mode", "acts_on")},
    )
    found = _unaddressed(itinerary, records) + _repeated_steps(steps)
    edges: dict[str, set[str]] = {name: set() for name in context.by_id}
    for position, step in steps:
        step_found, named = _step_findings(context, position, step, acts)
        found += step_found
        edges[str(step.get("id"))] |= named
    found += [
        finding(
            rules.ITINERARY_CYCLE,
            f"steps: {' -> '.join(cycle)} forms a cycle",
            "steps",
            value=" -> ".join(cycle),
        )
        for cycle in cycles(edges)
    ]
    return found


def _block(record: Mapping[str, Any], key: str) -> Mapping[str, Any] | None:
    """Return the block that a record holds under a key, or None when the key holds no mapping."""
    value = record.get(key)
    return value if isinstance(value, Mapping) else None


def _held(record: Mapping[str, Any], types: Mapping[str, Mapping[str, Any]]) -> str:
    """Name the types that a record holds in its present state, for a message."""
    return (
        " or ".join(record_types(record, types))
        or f"no product type, as a {record.get('type')} record"
    )


def _describe(held: Slot) -> str:
    """Return the number of inputs that a slot takes, in words."""
    if held.most is None:
        return f"{held.least} or more inputs"
    if held.least == 0:
        return "at most one input" if held.most == 1 else f"at most {held.most} inputs"
    return "one input" if held.least == held.most == 1 else f"{held.least} inputs"


def cycles(edges: Mapping[str, set[str]]) -> list[list[str]]:
    """Return the cycles that a depth-first search meets in the dependency graph of the steps.

    ``edges`` maps each step to the steps whose outputs it takes.

    >>> cycles({"a": {"b"}, "b": {"a"}, "c": set()})
    [['a', 'b', 'a']]
    >>> cycles({"a": {"a"}})
    [['a', 'a']]
    """
    state: dict[str, int] = {}
    found: list[list[str]] = []

    def visit(node: str, path: list[str]) -> None:
        state[node] = 1
        for nxt in sorted(edges.get(node, ())):
            if state.get(nxt) == 1:
                found.append([*path[path.index(nxt) :], nxt] if nxt in path else [node, nxt])
            elif nxt in edges and state.get(nxt) is None:
                visit(nxt, [*path, nxt])
        state[node] = 2

    for node in sorted(edges):
        if state.get(node) is None:
            visit(node, [node])
    return found
