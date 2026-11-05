"""
The checks of an answer and of a derived model: the operations of the model, the outputs bound to
the question, the pairs that place each factor of an explanation, and the presuppositions and the
interventions of a claim.
"""

from __future__ import annotations

from typing import Any, Mapping

from .. import findings as rules
from ..dimensions import parse_expression
from ..findings import Entry, Finding, finding, values_at
from ..findings import where as place_of
from ..identifiers import split_reference
from .paths import at, is_unfilled


def incomplete_operations(model: Mapping[str, Any]) -> list[Finding]:
    """Return every operation of a derived model that lacks a field required by its kind or its
    error.

    A controlled error states its bound, an approximation states its regime, and a singular limit
    states the order of its limits, as the note on derived models requires.

    >>> model = {"operations": [{"id": "near", "kind": "approximate", "error": "controlled"}]}
    >>> for f in incomplete_operations(model):
    ...     print(f.text)
    operations.near: a controlled error states its bound
    operations.near: an approximation states its regime
    """
    found: list[Finding] = []
    for index, entry in enumerate(model.get("operations") or []):
        if not isinstance(entry, Mapping):
            continue
        name = entry.get("id")
        required = [
            ("bound", entry.get("error") == "controlled", "a controlled error states its bound"),
            ("regime", entry.get("kind") == "approximate", "an approximation states its regime"),
            (
                "order",
                entry.get("kind") == "limit" and entry.get("error") == "singular",
                "a singular limit states the order of its limits",
            ),
        ]
        found += [
            finding(
                rules.COMPLETENESS_INCOMPLETE_OPERATION,
                f"operations.{name}: {message}",
                "operations",
                index,
                field,
            )
            for field, applies, message in required
            if applies and is_unfilled(entry.get(field))
        ]
    return found


def unclassified_operations(
    answer: Mapping[str, Any], records: Mapping[str, Mapping[str, Any]]
) -> list[Finding]:
    """Return every operation of a model on the route of the answer that no ground of the answer
    names.

    Only an answer classifies an assumption against its target, so each operation of a model on
    which its route runs is named by a ground, by the identifier of the operation or by a symbol
    that the operation yields: the removal of the noise as an idealization, a restriction as a
    condition, a posited law as a warrant.

    >>> model = {"id": "mod.a.b", "type": "model",
    ...          "operations": [{"id": "near", "yields": ["J"]}, {"id": "drop"}]}
    >>> answer = {"route": {"runs_on": ["mod.a.b"]}, "grounds": [{"record": "mod.a.b.J"}]}
    >>> [f.text for f in unclassified_operations(answer, {"mod.a.b": model})]
    ['operation drop of mod.a.b is named by no ground of the answer']
    """
    named = {
        str(ground.get("record"))
        for ground in answer.get("grounds") or []
        if isinstance(ground, Mapping)
    }
    found: list[Finding] = []
    for identifier in (answer.get("route") or {}).get("runs_on") or []:
        model = records.get(str(identifier)) or {}
        if model.get("type") != "model":
            continue
        for block, label in (("operations", "operation"), ("assumptions", "assumption")):
            for entry in model.get(block) or []:
                units = [entry.get("id"), *(entry.get("yields") or [])]
                if not any(f"{identifier}.{unit}" in named for unit in units if unit):
                    found.append(
                        finding(
                            rules.COMPLETENESS_UNCLASSIFIED_OPERATION,
                            f"{label} {entry.get('id')} of {identifier} is named by no ground of"
                            " the answer",
                            "grounds",
                        )
                    )
    return found


def unbound_outputs(
    answer: Mapping[str, Any], question: Mapping[str, Any], records: Mapping[str, Mapping[str, Any]]
) -> list[Finding]:
    """Return the missing binding of an answer on a model whose question names outputs to match.

    The comparison with the outputs runs through a binding, so a declared use does not replace it,
    even on a formal target, as the rule on a declared use states.

    >>> question = {"task": {"required_accuracy": {"outputs_to_match": [{"target": "phen.a.b.x"}]}}}
    >>> answer = {"route": {"runs_on": ["mod.a.b"]}, "use": {"value": "tool"}}
    >>> [f.text for f in unbound_outputs(answer, question, {"mod.a.b": {"type": "model"}})]
    ['the question names outputs to match, and the answer on a model cites no binding']
    """
    outputs = at(question, "task.required_accuracy.outputs_to_match") or []
    on_model = any(
        (records.get(str(r)) or {}).get("type") == "model"
        for r in (answer.get("route") or {}).get("runs_on") or []
    )
    if outputs and on_model and is_unfilled(answer.get("binding")):
        return [
            finding(
                rules.COMPLETENESS_UNBOUND_OUTPUTS,
                "the question names outputs to match, and the answer on a model cites no binding",
                "binding",
            )
        ]
    return []


#: The types of feature pair that each target status of a factor admits, when the route runs on a
#: model, as the status pairs of the answer specification
#: (docs/specification/answer.md#^status-pairs) state them; an alignment test keeps the two equal.
STATUS_PAIRS: Mapping[str, frozenset[str]] = {
    "denoting": frozenset({"quantity", "component"}),
    "coarse-graining": frozenset({"pattern", "regime"}),
    "limit-construct": frozenset({"invariance-class"}),
    "structural-constraint": frozenset({"invariance-class", "modal-profile"}),
}


def mismatched_status_pairs(
    answer: Mapping[str, Any], records: Mapping[str, Mapping[str, Any]]
) -> list[Finding]:
    """Return every factor whose pair does not carry its target status onto the target.

    When the route runs on a model, the binding carries each factor onto the target through a pair
    of the type that its status requires, and a limit construct cites, as a ground with the role
    `warrant`, the argued pair that places the target in the class of its limit. A route on the
    target needs no pair, since a factor stated over the symbols of the target denotes by
    declaration.

    >>> records = {"mod.a.m": {"type": "model"},
    ...            "bind.a.b": {"feature_pairs": [{"id": "p", "type": "quantity"}]}}
    >>> answer = {"route": {"runs_on": ["mod.a.m"]},
    ...           "aim_block": {"explanation": {"factors": [
    ...               {"id": "f", "target_status": "limit-construct", "pair": "bind.a.b.p"}]}}}
    >>> [f.text for f in mismatched_status_pairs(answer, records)]  # doctest: +NORMALIZE_WHITESPACE
    ['factors.f: the status limit-construct requires a pair of type invariance-class,
      and bind.a.b.p is of type quantity',
     'factors.f: no ground with the role warrant cites the pair bind.a.b.p that places the target
      in the class of the limit']
    """
    on_model = any(
        (records.get(str(r)) or {}).get("type") == "model"
        for r in (answer.get("route") or {}).get("runs_on") or []
    )
    if not on_model:
        return []
    warrants = {
        g.get("record")
        for g in answer.get("grounds") or []
        if isinstance(g, Mapping) and g.get("role") == "warrant"
    }
    found = []
    for index, factor in enumerate(at(answer, "aim_block.explanation.factors") or []):
        if not isinstance(factor, Mapping) or factor.get("target_status") not in STATUS_PAIRS:
            continue
        status, ref = factor["target_status"], factor.get("pair")
        admitted = STATUS_PAIRS[status]
        where = ("aim_block", "explanation", "factors", Entry(index, factor), "pair")
        name = factor.get("id") or index
        if not isinstance(ref, str):
            found.append(
                finding(
                    rules.COMPLETENESS_MISMATCHED_STATUS_PAIR,
                    f"factors.{name}: the status {status} requires a pair of type"
                    f" {' or '.join(sorted(admitted))}, and the factor names none",
                    *where,
                )
            )
            continue
        record, unit = split_reference(ref) or (ref, "")
        pair = next(
            (
                p
                for p in (records.get(record) or {}).get("feature_pairs") or []
                if isinstance(p, Mapping) and p.get("id") == unit
            ),
            None,
        )
        if pair is not None and pair.get("type") not in admitted:
            found.append(
                finding(
                    rules.COMPLETENESS_MISMATCHED_STATUS_PAIR,
                    f"factors.{name}: the status {status} requires a pair of type"
                    f" {' or '.join(sorted(admitted))}, and {ref} is of type {pair.get('type')}",
                    *where,
                )
            )
        if status == "limit-construct" and ref not in warrants:
            found.append(
                finding(
                    rules.COMPLETENESS_MISMATCHED_STATUS_PAIR,
                    f"factors.{name}: no ground with the role warrant cites the pair {ref}"
                    " that places the target in the class of the limit",
                    *where,
                )
            )
    return found


def _claim(answer: Mapping[str, Any]) -> Mapping[str, Any]:
    """Return the claim of an answer, or an empty mapping."""
    claim = answer.get("claim")
    return claim if isinstance(claim, Mapping) else {}


def _holds_statement(
    reference: str, answer: Mapping[str, Any], records: Mapping[str, Mapping[str, Any]]
) -> bool:
    """Tell whether a reference names a statement that can hold a presupposition: a law of a
    background or of a model, or a consequence of a derivation, other than the answer itself."""
    split = split_reference(reference)
    if split is None or split[0] == answer.get("id"):
        return False
    owner = records.get(split[0], {})
    if owner.get("type") in ("background", "model"):
        return any(
            isinstance(law, Mapping) and law.get("symbol") == split[1]
            for law in owner.get("laws") or []
        )
    if owner.get("type") == "derivation":
        return any(
            isinstance(c, Mapping) and c.get("id") == split[1]
            for c in owner.get("consequences") or []
        )
    return False


def _presuppositions(record: Mapping[str, Any]) -> list[tuple[int, Mapping[str, Any]]]:
    """Return the presuppositions that a question or the claim of an answer states, with their
    indices."""
    source = record.get("presuppositions") if record.get("type") == "question" else None
    entries = source if source is not None else _claim(record).get("presuppositions")
    return [(i, e) for i, e in enumerate(entries or []) if isinstance(e, Mapping)]


def misheld_presuppositions(
    answer: Mapping[str, Any], records: Mapping[str, Mapping[str, Any]]
) -> list[Finding]:
    """Return the presuppositions of a claim whose holder states no statement: neither a law of a
    background or a model nor a consequence of a derivation, or the answer itself. A presupposition
    that another answer holds is a relation ``presupposes`` to that answer.

    >>> held = [{"id": "p", "held_by": "ans.a.c"}]
    >>> answer = {"id": "ans.a.b", "claim": {"presuppositions": held}}
    >>> [f.text for f in misheld_presuppositions(answer, {})]
    ['claim.presuppositions.p.held_by: ans.a.c is no law and no consequence of a derivation']
    """
    found = []
    for index, entry in _presuppositions(answer):
        holder = entry.get("held_by")
        if not isinstance(holder, str) or not holder.strip():
            continue
        if _holds_statement(holder, answer, records):
            continue
        found.append(
            finding(
                rules.COMPLETENESS_MISHELD_PRESUPPOSITION,
                f"claim.presuppositions.{entry.get('id') or index}.held_by: {holder} is no law"
                " and no consequence of a derivation",
                "claim",
                "presuppositions",
                Entry(index, entry),
                "held_by",
                value=holder,
            )
        )
    return found


#: The blocks whose entries are quantities that a condition may define, by their path in a record.
CONDITIONED: tuple[tuple[str, ...], ...] = (
    ("variables",),
    ("parameters",),
    ("observables",),
    ("manifestations", "features"),
)


def misheld_existence(
    record: Mapping[str, Any], records: Mapping[str, Mapping[str, Any]]
) -> list[Finding]:
    """Return the quantities defined by a condition whose field ``held_by`` names no statement
    establishing a value that satisfies the condition: neither a law of a background or a model
    nor a consequence of a derivation.

    >>> record = {"id": "mod.a.b", "variables": [
    ...     {"symbol": "r", "condition": "r = min(S)", "held_by": "concept.a.b"}]}
    >>> [f.text for f in misheld_existence(record, {})]
    ['variables.r.held_by: concept.a.b is no law and no consequence of a derivation']
    """
    found = []
    for path in CONDITIONED:
        for locus, entries in values_at(record, path[:1]):
            for i, entry in enumerate(entries if isinstance(entries, list) else []):
                if not isinstance(entry, Mapping):
                    continue
                if len(path) > 1:
                    children = entry.get(path[1])
                    targets = [
                        ((*locus, Entry(i, entry), path[1], Entry(j, c)), c)
                        for j, c in enumerate(children if isinstance(children, list) else [])
                        if isinstance(c, Mapping)
                    ]
                else:
                    targets = [((*locus, Entry(i, entry)), entry)]
                for place, quantity in targets:
                    holder = quantity.get("held_by")
                    if not isinstance(holder, str) or not holder.strip():
                        continue
                    if _holds_statement(holder, record, records):
                        continue
                    found.append(
                        finding(
                            rules.COMPLETENESS_MISHELD_PRESUPPOSITION,
                            f"{place_of(place)}.held_by: {holder} is no law and no consequence of a"
                            " derivation",
                            *place,
                            "held_by",
                            value=holder,
                        )
                    )
    return found


def _same(left: Mapping[str, Any], right: Mapping[str, Any]) -> bool:
    """Tell whether two presuppositions state one commitment: expressions with the same tree, or
    the same reading when either is not formalized.

    >>> _same({"expression": "x > 0"}, {"expression": "x>0"})
    True
    """
    trees = parse_expression(left.get("expression")), parse_expression(right.get("expression"))
    if None not in trees:
        return trees[0] == trees[1]
    a, b = left.get("reading"), right.get("reading")
    return isinstance(a, str) and isinstance(b, str) and " ".join(a.split()) == " ".join(b.split())


def inherited_presuppositions(
    answer: Mapping[str, Any], question: Mapping[str, Any]
) -> list[Finding]:
    """Return the presuppositions of a claim that restate a presupposition of the question that the
    answer answers, since every direct answer of a question inherits its presuppositions.

    >>> question = {"type": "question", "presuppositions": [{"id": "q", "expression": "x > 0"}]}
    >>> answer = {"claim": {"presuppositions": [{"id": "p", "expression": "x > 0"}]}}
    >>> [f.text for f in inherited_presuppositions(answer, question)]
    ['claim.presuppositions.p: the question presupposes it already, as q']
    """
    asked = _presuppositions(question) if question.get("type") == "question" else []
    found = []
    for index, entry in _presuppositions(answer):
        twin = next((q for _, q in asked if _same(entry, q)), None)
        if twin is not None:
            found.append(
                finding(
                    rules.COMPLETENESS_INHERITED_PRESUPPOSITION,
                    f"claim.presuppositions.{entry.get('id') or index}: the question presupposes it"
                    f" already, as {twin.get('id')}",
                    "claim",
                    "presuppositions",
                    Entry(index, entry),
                )
            )
    return found


def _sets_intervention(reference: str, records: Mapping[str, Mapping[str, Any]]) -> bool:
    """Tell whether a reference names what an intervention sets: an experiment or a simulation run
    whose protocol states its intervention, or a parameter or a variable of a model."""
    design = records.get(reference)
    if design is not None:
        protocol = design.get("protocol")
        intervention = protocol.get("intervention") if isinstance(protocol, Mapping) else None
        return (
            design.get("type") == "design"
            and design.get("kind") in ("experiment", "simulation-run")
            and not is_unfilled(intervention)
        )
    split = split_reference(reference)
    if split is None:
        return False
    owner = records.get(split[0], {})
    return owner.get("type") == "model" and any(
        isinstance(q, Mapping) and q.get("symbol") == split[1]
        for block in ("parameters", "variables")
        for q in owner.get(block) or []
    )


def misdirected_interventions(
    answer: Mapping[str, Any], records: Mapping[str, Mapping[str, Any]]
) -> list[Finding]:
    """Return the interventions of a counterfactual claim that name neither an experiment or a
    simulation run stating an intervention nor a parameter or a variable of a model.

    >>> answer = {"claim": {"interventions": ["design.a.b"]}}
    >>> records = {"design.a.b": {"type": "design", "kind": "method"}}
    >>> for f in misdirected_interventions(answer, records):
    ...     print(f.text)  # doctest: +NORMALIZE_WHITESPACE
    claim.interventions: design.a.b sets no intervention: no experiment or simulation run stating
    one, and no quantity of a model
    """
    named = _claim(answer).get("interventions")
    found = []
    for index, reference in enumerate(named if isinstance(named, list) else []):
        if not isinstance(reference, str) or not reference.strip():
            continue
        if _sets_intervention(reference, records):
            continue
        found.append(
            finding(
                rules.COMPLETENESS_MISDIRECTED_INTERVENTIONS,
                f"claim.interventions: {reference} sets no intervention: no experiment or"
                " simulation run stating one, and no quantity of a model",
                "claim",
                "interventions",
                index,
                value=reference,
            )
        )
    return found
