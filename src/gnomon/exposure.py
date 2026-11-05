"""
The exposure of an answer to revision, computed by walking its dependencies back to their sources.

The exposure rule and the exposure of a derivation fix the content of the report: a conclusion is
exposed through every revisable unit on which it rests, directly or through the units that it rests
on in turn. This module walks that dependence from each answer:

- a ground or a premise naming a law reaches the law, which exposes the answer by its warrant
  ``posited``, ``fitted`` or ``measured``, and which a warrant ``derived`` passes on to its descent;
- the descent of a derived law is the derivation that records the law as a consequence, walked back
  from that consequence, or the published origin of the law when no derivation records it;
- a consequence of a derivation rests on the moves and the segments upstream of the object stating
  it, on the posits and the premises among their inputs, on the models on which the derivation runs,
  and on the derivations that it uses;
- a presupposition of a claim reaches the statement that holds it, or exposes the answer while no
  statement holds it, and a relation ``presupposes`` to another answer reaches that answer.

The walk fails closed: a unit whose state the record does not state, such as a warrant that names
no error, counts as exposed, so a record never lowers its exposure by omitting a field.

Classes
-------
Exposure
    One unit that exposes an answer, with its kind, its reason and the path that reaches it.

Functions
---------
combined_error
    Return the class of error of a consequence of a derivation, and the moves that set it.
answer_exposure
    Return the units that expose one answer.
exposure_rows
    Return the units that expose each answer of a set of records.
"""

from __future__ import annotations

from dataclasses import dataclass
from functools import cache
from pathlib import Path
from typing import Any, Iterator, Mapping

import yaml

from .derivations import recorded_descents, upstream
from .identifiers import split_reference
from .vocabulary import identifiers, upstream_of, visible_records

Records = Mapping[str, Mapping[str, Any]]

#: The registry of the rules of a derivation, which declares the tests confirming a posit.
REGISTRY = Path(__file__).parent / "data" / "registries" / "derivations.yml"

#: The blocks whose entries are quantities that a condition may define, by their path in a record.
QUANTITY_PATHS: tuple[tuple[str, ...], ...] = (
    ("variables",),
    ("parameters",),
    ("observables",),
    ("manifestations", "features"),
)

#: The warrants of a law that expose a conclusion resting on it.
REVISABLE_WARRANTS = frozenset({"posited", "fitted", "measured"})


@dataclass(frozen=True)
class Exposure:
    """One unit that exposes an answer: its reference, its kind, the reason of the exposure, and the
    record through which the walk reaches it."""

    unit: str
    kind: str
    reason: str
    via: str

    def row(self, answer: str) -> dict[str, str]:
        """Return the row of the view of exposure for an answer."""
        return {
            "answer": answer,
            "unit": self.unit,
            "kind": self.kind,
            "reason": self.reason,
            "via": self.via,
        }


@cache
def _confirming() -> tuple[frozenset[str], str | None]:
    """Return the tests that confirm a posit and the standard of a confirming computation."""
    registry: dict[str, Any] = yaml.safe_load(REGISTRY.read_text(encoding="utf-8")) or {}
    return frozenset(registry.get("confirming_tests") or []), registry.get("confirming_computation")


@cache
def _error_order() -> tuple[str, ...]:
    """Return the classes of error of a warrant, from the most to the least favourable."""
    registry: dict[str, Any] = yaml.safe_load(REGISTRY.read_text(encoding="utf-8")) or {}
    return tuple(str(e) for e in registry.get("error_order") or [])


def combined_error(record: Mapping[str, Any], consequence: str) -> tuple[str, list[str]]:
    """Return the class of error that a consequence of a derivation carries, the least favourable
    among the moves upstream of it, and those of its moves whose warrant is not exact, within whose
    regimes the consequence holds. A warrant that states no error counts as the least favourable.

    >>> derivation = {"moves": [{"id": "a", "inputs": ["p"], "outputs": ["x"],
    ...                          "warrant": {"error": "controlled"}},
    ...                         {"id": "b", "inputs": ["x"], "outputs": ["y"],
    ...                          "warrant": {"error": "exact"}}],
    ...               "consequences": [{"id": "c", "from": "y"}]}
    >>> combined_error(derivation, "c")
    ('controlled', ['a'])
    """
    order = _error_order()
    stated = _by_id(record, "consequences").get(consequence) or {}
    producers, _ = upstream(record, _names(stated.get("from")))
    worst, inexact = 0, []
    for ident, move in sorted(_by_id(record, "moves").items()):
        if ident not in producers:
            continue
        error = _mapping(move.get("warrant")).get("error")
        rank = order.index(error) if error in order else len(order)
        if rank:
            inexact.append(ident)
        worst = max(worst, rank)
    return (order[worst] if worst < len(order) else "not stated"), inexact


def _entries(record: Mapping[str, Any], name: str) -> list[Mapping[str, Any]]:
    """Return the entries of a list of a record that are mappings."""
    found = record.get(name)
    return [item for item in found if isinstance(item, Mapping)] if isinstance(found, list) else []


def _nested(record: Mapping[str, Any], path: tuple[str, ...]) -> list[Mapping[str, Any]]:
    """Return the entries reached by a path of lists in a record, such as the features of each
    manifestation."""
    level: list[Mapping[str, Any]] = [record]
    for key in path:
        level = [entry for parent in level for entry in _entries(parent, key)]
    return level


def _names(value: Any) -> list[str]:
    """Return the identifiers that a field holds: one for a string, one per entry for a list."""
    values = value if isinstance(value, list) else [value]
    return [str(v) for v in values if isinstance(v, str) and v.strip()]


def _by_id(record: Mapping[str, Any], name: str) -> dict[str, Mapping[str, Any]]:
    """Return the entries of a list of a record, keyed by their identifier."""
    return {str(e["id"]): e for e in _entries(record, name) if e.get("id")}


def _mapping(value: Any) -> Mapping[str, Any]:
    """Return ``value`` when it is a mapping, and an empty mapping otherwise."""
    return value if isinstance(value, Mapping) else {}


def _posit_state(posit: Mapping[str, Any], refuted: bool) -> str | None:
    """Return the reason for which a posit exposes a consequence resting on it, or None when a
    confirming test supports it and neither a refuting test nor a counterexample refutes it."""
    if refuted or any(t.get("verdict") == "refutes" for t in _entries(posit, "tests")):
        return "refuted"
    confirming, certified = _confirming()
    confirmed = any(
        t.get("verdict") == "supports"
        and (
            t.get("kind") in confirming
            or (t.get("kind") == "computation" and t.get("standard") == certified)
        )
        for t in _entries(posit, "tests")
    )
    return None if confirmed else "not confirmed"


class _Walk:
    """The walk of the dependence of one answer, which records each unit once."""

    def __init__(self, records: Records) -> None:
        self.records = records
        self.found: dict[tuple[str, str], Exposure] = {}
        self.visited: set[str] = set()
        self.descents = recorded_descents(records.values())

    def expose(self, unit: str, kind: str, reason: str, via: str) -> None:
        """Record one exposing unit, keeping the first path that reaches it."""
        self.found.setdefault((unit, reason), Exposure(unit, kind, reason, via))

    def _law(self, reference: str) -> Mapping[str, Any] | None:
        """Return the law that a reference names, or None when it names no law."""
        split = split_reference(reference)
        if split is None:
            return None
        owner, symbol = split
        record = self.records.get(owner) or {}
        return next((law for law in _entries(record, "laws") if law.get("symbol") == symbol), None)

    def reference(self, reference: str, via: str) -> None:
        """Walk a reference to a law, an answer, a derivation or one of its consequences."""
        if reference in self.visited:
            return
        self.visited.add(reference)
        target = self.records.get(reference)
        if target is not None:
            kind = target.get("type")
            if kind == "answer":
                self.answer(reference, f"answer {reference}")
            elif kind == "derivation":
                self.derivation(reference, None)
            return
        split = split_reference(reference)
        if split is not None and self._unit(reference, split, via):
            return
        law = self._law(reference)
        if law is not None:
            self.law(reference, law, via)
        elif split is not None:
            owner, ident = split
            for operation in _entries(self.records.get(owner) or {}, "operations"):
                if operation.get("id") == ident:
                    self.operation(owner, operation, via)

    def _unit(self, reference: str, split: tuple[str, str], via: str) -> bool:
        """Walk a unit of a derivation or an assumption of a model, and tell whether the reference
        names one."""
        owner_record = self.records.get(split[0]) or {}
        if owner_record.get("type") == "derivation":
            posits = _by_id(owner_record, "posits")
            if split[1] in posits:
                refuted = split[1] in {
                    str(r.get("target")) for r in _entries(owner_record, "refutations")
                }
                state = _posit_state(posits[split[1]], refuted)
                if state:
                    self.expose(reference, "posit", state, via)
            else:
                self.derivation(split[0], {split[1]})
            return True
        assumptions = _by_id(owner_record, "assumptions")
        if split[1] in assumptions:
            entry = assumptions[split[1]]
            motive = entry.get("motive") or "unclassified"
            removable = entry.get("removable") or "unknown"
            self.expose(reference, "assumption", f"{motive} assumption, removable {removable}", via)
            return True
        return False

    def operation(self, model: str, operation: Mapping[str, Any], via: str) -> None:
        """Expose an operation of a model whose error is not exact or is not stated."""
        error = operation.get("error")
        if error != "exact" and operation.get("id"):
            reason = f"{error} operation" if error else "operation error not stated"
            self.expose(f"{model}.{operation['id']}", "operation", reason, via)

    def _conditioned(self, owner: str) -> dict[str, tuple[str, Mapping[str, Any]]]:
        """Return the quantities defined by a condition that the expressions of a record may name,
        each with the record that declares it: the record itself, the records that it sees, and
        the target system that it is stated against."""
        record = self.records.get(owner) or {}
        seen = [record, *visible_records(record, self.records), upstream_of(record, self.records)]
        found: dict[str, tuple[str, Mapping[str, Any]]] = {}
        for other in seen:
            for path in QUANTITY_PATHS:
                for entry in _nested(other, path):
                    if entry.get("condition") and isinstance(entry.get("symbol"), str):
                        found.setdefault(entry["symbol"], (str(other.get("id")), entry))
        return found

    def existence(self, text: Any, owner: str, via: str) -> None:
        """Walk the existence that the condition of each quantity named by an expression
        presupposes: to the statement that holds it, or expose it while it stays undischarged."""
        if not isinstance(text, str) or not text.strip():
            return
        quantities = self._conditioned(owner)
        for name in sorted(identifiers(text) & set(quantities)):
            declared, entry = quantities[name]
            holder = entry.get("held_by")
            if isinstance(holder, str) and holder.strip():
                self.reference(holder, f"existence of {declared}.{name}")
                continue
            unique = " and uniqueness" if entry.get("selects") == "unique" else ""
            self.expose(f"{declared}.{name}", "existence", f"existence{unique} not discharged", via)

    def law(self, reference: str, law: Mapping[str, Any], via: str) -> None:
        """Walk a law: a revisable warrant exposes, a derived law passes on to its descent, and the
        quantities that it names pass on the existence that their conditions presuppose."""
        split = split_reference(reference)
        if split is not None:
            self.existence(law.get("expression"), split[0], via)
        for required in _names(law.get("requires")):
            self.reference(required, f"law {reference}")
        warrant = str(law.get("warrant") or "")
        if warrant in REVISABLE_WARRANTS:
            self.expose(reference, "law", warrant, via)
        elif warrant == "derived" and reference in self.descents:
            name, consequence = self.descents[reference]
            self.derivation(name, {consequence})
        elif warrant == "derived" and law.get("origin"):
            self.expose(reference, "law", "descent in its origin", via)
        elif warrant == "derived":
            self.expose(reference, "law", "descent not recorded", via)
        elif not warrant:
            self.expose(reference, "law", "warrant not stated", via)

    def derivation(self, name: str, consequences: set[str] | None) -> None:
        """Walk a derivation back from some of its consequences, or from all of them."""
        record = self.records.get(name)
        if not isinstance(record, Mapping):
            return
        via = f"derivation {name}"
        stated = _by_id(record, "consequences")
        chosen = set(stated) if consequences is None else consequences & set(stated)
        refuted = {str(r.get("target")) for r in _entries(record, "refutations") if r.get("target")}
        self._consequences(name, record, chosen, refuted)
        targets = {str(stated[c].get("from")) for c in chosen if stated[c].get("from")}
        needed = self._units(name, record, targets, refuted)
        for premise in sorted(n for n in needed if "." in n):
            self.reference(premise, via)
        for model in _names(record.get("runs_on")):
            for operation in _entries(self.records.get(model) or {}, "operations"):
                self.operation(model, operation, via)
        for used in _names(record.get("uses")):
            if used not in self.visited:
                self.visited.add(used)
                self.derivation(used, None)

    def _consequences(
        self, name: str, record: Mapping[str, Any], chosen: set[str], refuted: set[str]
    ) -> None:
        """Expose the consequences of a derivation that a counterexample refutes, and those whose
        moves carry an error that is not exact."""
        via = f"derivation {name}"
        for ident in sorted(chosen & refuted):
            self.expose(f"{name}.{ident}", "consequence", "refuted", via)
        for ident in sorted(chosen):
            error, inexact = combined_error(record, ident)
            if inexact:
                reason = f"{error} error, within the regimes of {', '.join(inexact)}"
                self.expose(f"{name}.{ident}", "consequence", reason, via)

    def _units(
        self, name: str, record: Mapping[str, Any], targets: set[str], refuted: set[str]
    ) -> set[str]:
        """Expose the moves and the posits of a derivation upstream of some objects, and return
        every input that those objects rest on."""
        via = f"derivation {name}"
        producers, needed = upstream(record, targets)
        moves = _by_id(record, "moves")
        for ident in sorted(producers & set(moves)):
            error = _mapping(moves[ident].get("warrant")).get("error")
            if error != "exact":
                reason = f"{error} warrant" if error else "warrant error not stated"
                self.expose(f"{name}.{ident}", "move", reason, via)
        for ident, posit in sorted(_by_id(record, "posits").items()):
            state = _posit_state(posit, ident in refuted) if ident in needed else None
            if state:
                self.expose(f"{name}.{ident}", "posit", state, via)
        return needed

    def answer(self, name: str, via: str) -> None:
        """Walk an answer: its grounds, the derivations of its route and of the obligations that
        its assessments settle, its presuppositions, and the existence that the quantities of its
        claim presuppose."""
        record = self.records.get(name) or {}
        self.obligations(name)
        for ground in _entries(record, "grounds"):
            if isinstance(ground.get("record"), str):
                self.reference(str(ground["record"]), via)
        route = record.get("route")
        for cited in _names(route.get("derivations") if isinstance(route, Mapping) else None):
            self.reference(cited, via)
        claim = record.get("claim")
        claim = claim if isinstance(claim, Mapping) else {}
        self.existence(claim.get("expression"), name, "claim")
        for entry in _entries(claim, "presuppositions"):
            self.presupposition(name, entry)
        for relation in _entries(record, "relations"):
            if relation.get("relation") == "presupposes" and isinstance(
                relation.get("answer"), str
            ):
                self.reference(str(relation["answer"]), f"answer {relation['answer']}")

    def obligations(self, answer: str) -> None:
        """Walk the derivations that settle the proof obligations of the assessments of an
        answer; an obligation not yet passed supports nothing yet."""
        for ident, assessment in sorted(self.records.items()):
            if assessment.get("type") != "assessment" or assessment.get("assesses") != answer:
                continue
            for obligation in _entries(assessment, "obligations"):
                derivation = obligation.get("derivation")
                if obligation.get("verdict") == "pass" and isinstance(derivation, str):
                    self.reference(derivation, f"assessment {ident}")

    def presupposition(self, answer: str, entry: Mapping[str, Any]) -> None:
        """Walk a presupposition: to the statement that holds it when one is named, and otherwise
        expose the answer to it while it stays undischarged."""
        holder = entry.get("held_by")
        if isinstance(holder, str) and holder.strip():
            self.reference(holder, f"presupposition {entry.get('id')}")
        else:
            unit = f"{answer}.claim.presuppositions.{entry.get('id') or '?'}"
            self.expose(unit, "presupposition", "not discharged", "claim")


def answer_exposure(records: Records, answer: str) -> list[Exposure]:
    """Return the units that expose one answer, in the order in which the walk reaches them."""
    walk = _Walk(records)
    walk.visited.add(answer)
    walk.answer(answer, "direct")
    return list(walk.found.values())


def exposure_rows(records: Records) -> Iterator[dict[str, str]]:
    """Yield one row per unit exposing each answer of a set of records."""
    for name in sorted(n for n, r in records.items() if r.get("type") == "answer"):
        for found in answer_exposure(records, name):
            yield found.row(name)
