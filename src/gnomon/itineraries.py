"""
Itineraries of inquiry, checked against the registries of epistemic activities and product types.

An itinerary lists activity instances, its steps. Each step names a registered activity, the products
that it takes and the product that it produces, each typed by the registry of product types, and
the verdict of the norm that judges it. Two registries in package data declare what a step may
state, so no check here reads a document:

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

#: The record kind whose status is an attitude, the only kind that an ``attitude`` qualifier restricts.
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
class Activity:
    """One epistemic activity, as the registry declares it."""

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
    many), and ``optional`` lets the step omit the input; a ``role`` leaves the type unchanged. An ``attitude``, one value or a list, restricts the
    attitudes under which a referenced answer holds the type, since the attitude of a claim is an
    attribute of the claim, not a type.

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
    attitudes = frozenset([attitude] if isinstance(attitude, str) else (str(value) for value in attitude))
    if entry.get("several"):
        return Slot(types, least=0 if entry.get("optional") else 2, most=None, attitudes=attitudes)
    count = int(entry.get("count", 1))
    return Slot(types, least=0 if entry.get("optional") else count, most=count, attitudes=attitudes)


def required_attitudes(act: Activity, kind: str) -> frozenset[str]:
    """Return the attitudes under which a record must hold ``kind`` to enter ``act``; empty when any serves.

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
    """Return, per product type, the record kinds that hold it; a type that no record holds maps to none.

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
    ...                                "verdict": {"class": "evaluative", "record": ["assessment"]}}))
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
    """Return ``question`` once every subject slot names a record and the request is fixed, else ``schema``.

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


def _closed(field: str, source: Path | None = None, kind: str = "itinerary") -> frozenset[str]:
    vocabulary = (_load(source or VOCABULARY_REGISTRY).get("vocabularies") or {}).get(kind) or {}
    return frozenset(entry["value"] for entry in vocabulary.get(field) or [])


def malformed_registry(
    acts: Mapping[str, Activity],
    types: Mapping[str, Any],
    modes: Iterable[str],
    attitudes: Iterable[str] | None = None,
) -> list[Finding]:
    """Return every activity that names a type, a mode, an attitude or a norm the registries do not admit.

    The itinerary check trusts the activity registry, so the registry is itself checked: every input
    and output names a product type, every attitude that qualifies an input is an attitude of an
    answer, every mode is admitted, and every norm is the named test of its own activity. Each
    finding concerns the registry file, under its list ``activities`` keyed by activity.
    """
    admitted = set(modes)
    held_as = set(_closed(".status", kind=ATTITUDE_HOLDER) if attitudes is None else attitudes)
    found = []
    for act in acts.values():
        entry = ("activities", Key(act.id))
        named = [(t, (*entry, "inputs", index)) for index, s in enumerate(act.inputs) for t in s.types]
        for kind, where in [*named, (act.output, (*entry, "output"))]:
            if kind not in types:
                found.append(
                    finding(rules.REGISTRY_UNKNOWN_PRODUCT_TYPE, f"{act.id}: {kind} is no product type",
                            *where, value=kind)
                )
        found += [
            finding(rules.REGISTRY_UNADMITTED_ATTITUDE, f"{act.id}: {value} is no attitude of an answer",
                    *entry, "inputs", index, value=value)
            for index, held in enumerate(act.inputs) for value in sorted(held.attitudes - held_as)
        ]
        if act.mode not in admitted:
            found.append(
                finding(rules.REGISTRY_UNADMITTED_MODE, f"{act.id}: {act.mode} is no admitted mode",
                        *entry, "mode")
            )
        holders = type_holders(types).get(act.output, frozenset())
        for name, values in act.output_values.items():
            vocabulary = set().union(*(_closed(f".{name}", kind=holder) for holder in holders))
            found += [
                finding(rules.REGISTRY_UNKNOWN_OUTPUT_VALUE,
                        f"{act.id}: {value} is no {name} of a {act.output}", *entry, "output_values",
                        name, value=value)
                for value in values if value not in vocabulary
            ]
        if act.norm != f"norm.{act.id}":
            found.append(
                finding(rules.REGISTRY_FOREIGN_NORM,
                        f"{act.id}: its norm {act.norm} is not the test norm.{act.id}", *entry, "norm")
            )
    return found


def itinerary_problems(
    itinerary: Mapping[str, Any],
    records: Mapping[str, Mapping[str, Any]],
    acts: Mapping[str, Activity] | None = None,
    types: Mapping[str, Any] | None = None,
    states: Callable[[str, str], Mapping[str, Any] | None] | None = None,
) -> list[Finding]:
    """Return every step of the itinerary that the registries or the records contradict.

    The five conditions of the itinerary check, stated in the overview of the activity taxonomy, apply:

    - every step names a registered activity;
    - the input types of a step fill the inputs of its activity, in number as well as in type, and
      its output type is the output of that activity;
    - each input reference names a record that holds the input type in its present state, or at
      the revision that the input names by ``as_of``, under an attitude that its slot admits, or a step producing that type, named in full by the identifier
      of the itinerary followed by its own; a type held outside the records takes any pointer;
    - the references between steps form an acyclic graph;
    - every verdict is admitted, and a verdict ``pass`` or ``fail`` states its evidence and its date.

    Five checks of the record fields complete them: the itinerary addresses a problem or a question; no
    two steps share an identifier; an output reference, once given, names a record that holds the
    output type; the norm of a step is the test of its activity, and a stated mode is its mode; the
    rationale of a step serves a question or a problem, and names a condition when it serves a question.

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
    types = product_types() if types is None else types
    verdicts, modes, acts_on = _closed("steps.verdict"), _closed("steps.mode"), _closed("steps.acts_on")
    steps = [
        (index, step) for index, step in enumerate(itinerary.get("steps") or []) if isinstance(step, Mapping)
    ]
    by_id = {str(step.get("id")): step for _, step in steps}
    own = f"{itinerary.get('id')}."
    found: list[Finding] = []

    target = itinerary.get("addresses")
    if (records.get(str(target)) or {}).get("type") not in ("problem", "question"):
        found.append(
            finding(rules.ITINERARY_UNADDRESSED, f"addresses: {target} is no problem or question record",
                    "addresses")
        )

    repeated = [name for name, count in Counter(str(s.get("id")) for _, s in steps).items() if count > 1]
    found += [
        finding(rules.ITINERARY_REPEATED_STEP, f"steps: the identifier {name} names several steps",
                "steps", value=name)
        for name in repeated
    ]

    edges: dict[str, set[str]] = {name: set() for name in by_id}
    for position, step in steps:
        name = str(step.get("id"))
        where = f"steps.{name}"
        at = ("steps", Entry(position, step))
        act = acts.get(str(step.get("activity")))
        if act is None:
            found.append(
                finding(rules.ITINERARY_UNKNOWN_ACTIVITY,
                        f"{where}: {step.get('activity')} is no registered activity", *at, "activity")
            )
            continue
        inputs = [(i, item) for i, item in enumerate(step.get("inputs") or []) if isinstance(item, Mapping)]
        counts = Counter(str(item.get("type")) for _, item in inputs)
        for index, held in enumerate(act.inputs):
            filled = sum(counts[t] for t in held.types)
            if not held.admits(filled):
                found.append(
                    finding(
                        rules.ITINERARY_UNFILLED_INPUT,
                        f"{where}: {act.id} takes {_describe(held)} of {' or '.join(sorted(held.types))},"
                        f" and the step gives {filled}",
                        *at, "inputs", value="|".join(sorted(held.types)),
                    )
                )
        accepted = {t for held in act.inputs for t in held.types}
        found += [
            finding(rules.ITINERARY_UNACCEPTED_INPUT, f"{where}: {act.id} takes no input of type {kind}",
                    *at, "inputs", value=kind)
            for kind in sorted(counts) if kind not in accepted
        ]
        for index, item in inputs:
            given = (*at, "inputs", index)
            kind, ref = str(item.get("type")), item.get("ref")
            local = str(ref)[len(own):] if isinstance(ref, str) and ref.startswith(own) else None
            if local is not None and (producer := by_id.get(local)) is not None:
                edges[name].add(local)
                made = (producer.get("output") or {}).get("type")
                if made != kind:
                    found.append(
                        finding(rules.ITINERARY_MISTYPED_STEP_INPUT,
                                f"{where}: the step {ref} produces {made}, not {kind}", *given)
                    )
                continue
            entry = types.get(kind) or {}
            if entry.get("record") == EXTERNAL:
                continue
            if entry.get("record") == TO_CREATE:
                found.append(
                    finding(rules.ITINERARY_INPUT_WITHOUT_PRODUCER,
                            f"{where}: no record holds a {kind}, so its input names a step, and {ref} is none",
                            *given)
                )
                continue
            record = records.get(ref) if isinstance(ref, str) else None
            revision = item.get("as_of")
            if isinstance(ref, str) and isinstance(revision, str) and revision:
                record = states(ref, revision) if states is not None else None
                if record is None:
                    found.append(
                        finding(rules.ITINERARY_UNREADABLE_STATE,
                                f"{where}: {ref} cannot be read at the revision {revision}", *given, "as_of")
                    )
                    continue
            if record is None:
                found.append(
                    finding(rules.ITINERARY_UNRESOLVED_INPUT, f"{where}: {ref} is neither a step nor a record",
                            *given)
                )
            elif not holds(record, entry):
                found.append(
                    finding(rules.ITINERARY_MISTYPED_RECORD_INPUT,
                            f"{where}: {ref} holds {_held(record, types)}, not {kind}", *given)
                )
            elif (
                record.get("type") == ATTITUDE_HOLDER
                and (attitudes := required_attitudes(act, kind))
                and record.get("status") not in attitudes
            ):
                found.append(
                    finding(rules.ITINERARY_UNADMITTED_ATTITUDE,
                            f"{where}: {ref} is {record.get('status')}, and {act.id} takes a {kind}"
                            f" held as {' or '.join(sorted(attitudes))}", *given)
                )
        output = _block(step, "output") or {}
        made = output.get("type")
        if made != act.output:
            found.append(
                finding(rules.ITINERARY_MISTYPED_OUTPUT,
                        f"{where}: {act.id} produces {act.output}, and the step states {made}",
                        *at, "output", "type")
            )
        product = output.get("ref")
        if made == "knowledge-state-change" and isinstance(product, str) and product in records:
            before = output.get("before")
            earlier = states(product, before) if states is not None and isinstance(before, str) and before else None
            if earlier is None:
                found.append(finding(rules.ITINERARY_UNCHANGED_STATE,
                                     f"{where}: the change of {product} names no readable revision before it",
                                     *at, "output", "before"))
            elif earlier.get("status") == records[product].get("status"):
                found.append(finding(rules.ITINERARY_UNCHANGED_STATE,
                                     f"{where}: the status of {product} is {earlier.get('status')} before and after the step",
                                     *at, "output", "before"))
        if isinstance(product, str) and product in records:
            if not holds(records[product], types.get(str(made)) or {}):
                found.append(
                    finding(rules.ITINERARY_MISTYPED_OUTPUT_RECORD,
                            f"{where}: {product} holds {_held(records[product], types)}, not {made}",
                            *at, "output", "ref")
                )
            for name, admitted in act.output_values.items():
                value = records[product].get(name)
                if isinstance(value, str) and value and value not in admitted:
                    found.append(
                        finding(rules.ITINERARY_UNADMITTED_OUTPUT_VALUE,
                                f"{where}: {product} has the {name} {value}, and {act.id} produces"
                                f" a {act.output} of the {name} {' or '.join(admitted)}",
                                *at, "output", "ref")
                    )
        norm = _block(step, "norm") or {}
        if norm.get("test") != act.norm:
            found.append(
                finding(rules.ITINERARY_FOREIGN_NORM,
                        f"{where}: the norm of {act.id} is {act.norm}, and the step names {norm.get('test')}",
                        *at, "norm", "test")
            )
        if norm.get("verdict") not in verdicts:
            found.append(
                finding(rules.ITINERARY_UNKNOWN_VERDICT, f"{where}: {norm.get('verdict')!r} is no verdict",
                        *at, "norm", "verdict")
            )
        elif norm.get("verdict") != "pending":
            judged = norm.get("judged")
            if not isinstance(norm.get("evidence"), str) or not norm["evidence"].strip():
                found.append(
                    finding(rules.ITINERARY_UNJUSTIFIED_VERDICT,
                            f"{where}: the verdict {norm.get('verdict')} states no evidence", *at, "norm", "evidence")
                )
            if not DATE.fullmatch(str(judged)):
                found.append(
                    finding(rules.ITINERARY_UNJUSTIFIED_VERDICT,
                            f"{where}: the verdict {norm.get('verdict')} states no date of judgment, written YYYY-MM-DD",
                            *at, "norm", "judged")
                )
        rationale = _block(step, "rationale") or {}
        served = (records.get(str(rationale.get("serves"))) or {}).get("type")
        if served not in ("question", "problem"):
            found.append(
                finding(rules.ITINERARY_UNSERVED,
                        f"{where}: the rationale serves {rationale.get('serves')}, which is no question or problem record",
                        *at, "rationale", "serves")
            )
        elif served == "question" and rationale.get("acts_on") not in acts_on:
            found.append(
                finding(rules.ITINERARY_UNSERVED,
                        f"{where}: the rationale serves a question and names no condition or act among"
                        f" {', '.join(sorted(acts_on))}", *at, "rationale", "acts_on")
            )
        branch = _block(step, "branch")
        if branch is not None:
            other = by_id.get(str(branch.get("otherwise")))
            made_other = ((other or {}).get("output") or {}).get("type")
            if not isinstance(branch.get("condition"), str) or not branch["condition"].strip():
                found.append(finding(rules.ITINERARY_MALFORMED_CONSTRUCTOR,
                                     f"{where}: the branch states no condition", *at, "branch", "condition"))
            if other is None or made_other != act.output:
                found.append(finding(rules.ITINERARY_MALFORMED_CONSTRUCTOR,
                                     f"{where}: the branch names no step that produces {act.output} otherwise",
                                     *at, "branch", "otherwise"))
        iterate = _block(step, "iterate")
        if iterate is not None:
            if not isinstance(iterate.get("until"), str) or not iterate["until"].strip():
                found.append(finding(rules.ITINERARY_MALFORMED_CONSTRUCTOR,
                                     f"{where}: the iteration states no criterion of termination", *at, "iterate", "until"))
            if act.output not in {t for held in act.inputs for t in held.types}:
                found.append(finding(rules.ITINERARY_MALFORMED_CONSTRUCTOR,
                                     f"{where}: {act.id} takes no input of its output type {act.output}, so it cannot repeat on it",
                                     *at, "iterate"))
        mode = step.get("mode")
        if mode is not None and (mode not in modes or mode != act.mode):
            found.append(
                finding(rules.ITINERARY_MISMATCHED_MODE,
                        f"{where}: {act.id} proceeds by {act.mode} inference, and the step states {mode}",
                        *at, "mode")
            )
    found += [
        finding(rules.ITINERARY_CYCLE, f"steps: {' -> '.join(cycle)} forms a cycle", "steps",
                value=" -> ".join(cycle))
        for cycle in cycles(edges)
    ]
    return found


def _block(record: Mapping[str, Any], key: str) -> Mapping[str, Any] | None:
    """Return the block that a record holds under a key, or None when the key holds no mapping."""
    value = record.get(key)
    return value if isinstance(value, Mapping) else None


def _held(record: Mapping[str, Any], types: Mapping[str, Mapping[str, Any]]) -> str:
    """Name the types that a record holds in its present state, for a message."""
    return " or ".join(record_types(record, types)) or f"no product type, as a {record.get('type')} record"


def _describe(held: Slot) -> str:
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
                found.append(path[path.index(nxt):] + [nxt] if nxt in path else [node, nxt])
            elif nxt in edges and state.get(nxt) is None:
                visit(nxt, path + [nxt])
        state[node] = 2

    for node in sorted(edges):
        if state.get(node) is None:
            visit(node, [node])
    return found
