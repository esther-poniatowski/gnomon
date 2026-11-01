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

from collections import Counter
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Iterable, Mapping

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
    """

    types: frozenset[str]
    least: int = 1
    most: int | None = 1

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


def _load(path: Path) -> dict[str, Any]:
    return yaml.safe_load(path.read_text(encoding="utf-8")) or {}


def slot(entry: Any) -> Slot:
    """Return the slot that one input entry of the registry declares.

    A bare type takes one record. A mapping names one type under ``type`` or alternatives under
    ``types``, and qualifies the number with ``several`` (two or more) or ``count`` (exactly that
    many); a ``role`` leaves the type unchanged.

    >>> slot("problem")
    Slot(types=frozenset({'problem'}), least=1, most=1)
    >>> slot({"type": "model", "several": True, "role": "family"}).admits(3)
    True
    >>> slot({"type": "model", "count": 2}).admits(1)
    False
    >>> sorted(slot({"types": ["hypothesis", "model"]}).types)
    ['hypothesis', 'model']
    """
    if isinstance(entry, str):
        return Slot(frozenset({entry}))
    declared = entry.get("types") or [entry.get("type")]
    types = frozenset(str(name) for name in declared)
    if entry.get("several"):
        return Slot(types, least=2, most=None)
    count = int(entry.get("count", 1))
    return Slot(types, least=count, most=count)


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


def has_placeholder(question: Mapping[str, Any]) -> bool:
    """Return whether some subject slot of a question holds a placeholder rather than a record."""
    subject = question.get("subject") or {}
    return any(isinstance(subject.get(slot), Mapping) for slot in ("target_system", "phenomenon"))


def holds(record: Mapping[str, Any], entry: Mapping[str, Any]) -> bool:
    """Return whether ``record``, in its present state, holds a product of the type of ``entry``.

    The kind of the record must be listed, and its state must satisfy the ``when`` mapping: the
    level of commitment, the slots of a question, or the status.

    >>> holds({"type": "question", "subject": {"phenomenon": {"placeholder": "observable"}}},
    ...       {"record": ["question"], "when": {"slots": "placeholder"}})
    True
    >>> holds({"type": "target-system", "commitment": "specified"},
    ...       {"record": ["target-system"], "when": {"commitment": ["identified"]}})
    False
    """
    kinds = entry.get("record")
    if not isinstance(kinds, list) or record.get("type") not in kinds:
        return False
    when = entry.get("when") or {}
    if "commitment" in when and record.get("commitment") not in when["commitment"]:
        return False
    if "status" in when and record.get("status") not in when["status"]:
        return False
    if "slots" in when and has_placeholder(record) != (when["slots"] == "placeholder"):
        return False
    return True


def record_types(record: Mapping[str, Any], types: Mapping[str, Mapping[str, Any]]) -> list[str]:
    """Return every product type that ``record`` holds in its present state, in registry order."""
    return [name for name, entry in types.items() if holds(record, entry)]


def _closed(field: str, source: Path | None = None) -> frozenset[str]:
    itinerary = (_load(source or VOCABULARY_REGISTRY).get("vocabularies") or {}).get("itinerary") or {}
    return frozenset(entry["value"] for entry in itinerary.get(field) or [])


def malformed_registry(
    acts: Mapping[str, Activity], types: Mapping[str, Any], modes: Iterable[str]
) -> list[Finding]:
    """Return every activity that names a type, a mode or a norm the registries do not admit.

    The itinerary check trusts the activity registry, so the registry is itself checked: every input
    and output names a product type, every mode is admitted, and every norm is the named test
    of its own activity. Each finding concerns the registry file, under its list ``activities``
    keyed by activity.
    """
    admitted = set(modes)
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
        if act.mode not in admitted:
            found.append(
                finding(rules.REGISTRY_UNADMITTED_MODE, f"{act.id}: {act.mode} is no admitted mode",
                        *entry, "mode")
            )
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
) -> list[Finding]:
    """Return every step of the itinerary that the registries or the records contradict.

    The five conditions of the itinerary check, stated in the overview of the activity taxonomy, apply:

    - every step names a registered activity;
    - the input types of a step fill the inputs of its activity, in number as well as in type, and
      its output type is the output of that activity;
    - each input reference names a record that holds the input type in its present state, or a step
      producing that type; a type held outside the records takes any pointer;
    - the references between steps form an acyclic graph;
    - every verdict is admitted.

    Four checks of the record fields complete them: the itinerary addresses a problem or a question; no
    two steps share an identifier; an output reference, once given, names a record that holds the
    output type; the norm of a step is the test of its activity, and a stated mode is its mode.

    Parameters
    ----------
    itinerary : mapping
        One filled itinerary record.
    records : mapping
        The records of the problem, keyed by identifier.
    acts, types : mapping, optional
        The two registries, read from package data when omitted.
    """
    acts = activities() if acts is None else acts
    types = product_types() if types is None else types
    verdicts, modes = _closed("steps.verdict"), _closed("steps.mode")
    steps = [
        (index, step) for index, step in enumerate(itinerary.get("steps") or []) if isinstance(step, Mapping)
    ]
    by_id = {str(step.get("id")): step for _, step in steps}
    found: list[Finding] = []

    target = itinerary.get("addresses")
    if (records.get(target) or {}).get("type") not in ("problem", "question"):
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
            producer = by_id.get(str(ref))
            if producer is not None:
                edges[name].add(str(ref))
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
        output = step.get("output") if isinstance(step.get("output"), Mapping) else {}
        made = output.get("type")
        if made != act.output:
            found.append(
                finding(rules.ITINERARY_MISTYPED_OUTPUT,
                        f"{where}: {act.id} produces {act.output}, and the step states {made}",
                        *at, "output", "type")
            )
        product = output.get("ref")
        if isinstance(product, str) and product in records:
            if not holds(records[product], types.get(str(made)) or {}):
                found.append(
                    finding(rules.ITINERARY_MISTYPED_OUTPUT_RECORD,
                            f"{where}: {product} holds {_held(records[product], types)}, not {made}",
                            *at, "output", "ref")
                )
        norm = step.get("norm") if isinstance(step.get("norm"), Mapping) else {}
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


def _held(record: Mapping[str, Any], types: Mapping[str, Mapping[str, Any]]) -> str:
    """Name the types that a record holds in its present state, for a message."""
    return " or ".join(record_types(record, types)) or f"no product type, as a {record.get('type')} record"


def _describe(held: Slot) -> str:
    if held.most is None:
        return f"{held.least} or more inputs"
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
