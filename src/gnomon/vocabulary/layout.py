"""
Where a record holds its declarations, its formulas and its references, and the functions that
walk them.
"""

from __future__ import annotations

import re
from typing import Any, Mapping

from ..findings import Entry, Place
from ..identifiers import split_reference

#: Blocks whose entries declare a symbol, per record kind. A background record declares its laws
#: and relations over the quantities of the target system that it describes.
DECLARING: Mapping[str, tuple[str, ...]] = {
    "target-system": (
        "variants",
        "constituents",
        "index_sets",
        "variables",
        "parameters",
        "external_systems",
    ),
    "background": ("laws", "organization"),
    "phenomenon": ("index_sets", "observables", "manifestations", "scope_over_instances"),
    "model": ("constituents", "index_sets", "variables", "parameters", "laws", "organization"),
    "derivation": ("slots",),
}


#: The record kinds the checkers read. A kind declaring no symbol still carries expressions, so
#: this set is wider than the keys of :data:`DECLARING`.
RECORD_KINDS: frozenset[str] = frozenset(
    {
        "target-system",
        "background",
        "phenomenon",
        "operators",
        "question",
        "model",
        "answer",
        "binding",
        "derivation",
    }
)


#: The field through which a record of each kind names the target system it is stated against.
UPSTREAM_FIELD: Mapping[str, str] = {
    "background": "describes",
    "phenomenon": "target_system",
    "operators": "target_system",
}


#: Fields holding an expression, as (block, key).
FORMULA: tuple[tuple[str, str], ...] = (
    ("variables", "expression"),
    ("variables", "condition"),
    ("parameters", "expression"),
    ("parameters", "condition"),
    ("laws", "expression"),
    ("laws", "range"),
    ("observables", "expression"),
    ("observables", "condition"),
    ("manifestations", "expression"),
    ("detection_criterion", "expression"),
    ("constituents", "extent"),
    ("index_sets", "extent"),
    ("operators", "values"),
    ("operators", "signature"),
    ("variables", "values"),
    ("external_systems", "class"),
    ("organization", "relates"),
    ("proof_obligations", "antecedent"),
    ("proof_obligations", "consequent"),
    ("parameters", "values"),
    ("observables", "values"),
)


#: Expression fields inside a mapping carried by a list entry, as (block, mapping, key).
WITHIN_ENTRY: tuple[tuple[str, str, str], ...] = (
    ("observables", "event", "origin"),
    ("observables", "event", "horizon"),
)


#: Expression fields inside a mapping that holds lists, as (mapping, list, key).
WITHIN_MAPPING: tuple[tuple[str, str, str], ...] = (
    ("conditions_and_byproducts", "precipitating", "expression"),
    ("conditions_and_byproducts", "inhibiting", "expression"),
    ("conditions_and_byproducts", "modulating", "expression"),
    ("conditions_and_byproducts", "modulating", "effect"),
    ("conditions_and_byproducts", "nonstandard", "expression"),
    ("conditions_and_byproducts", "byproducts", "expression"),
    ("reference_class", "selection_criteria", "expression"),
)


#: Expression fields nested one level deeper, as (block, inner block, key).
NESTED_FORMULA: tuple[tuple[str, str, str], ...] = (
    ("manifestations", "features", "values"),
    ("manifestations", "features", "condition"),
    ("external_systems", "constrains", "expression"),
)


#: Reference fields nested one level deeper, as (block, inner block, key).
NESTED_REFERENCE: tuple[tuple[str, str, str], ...] = (
    ("external_systems", "constrains", "signature"),
)


#: Expression fields named by a dotted path, with ``[]`` wherever a list is traversed. A question
#: nests its expressions too deeply for the block-and-key form above.
PATH_FORMULA: tuple[str, ...] = (
    "subject.contrast.foil_set[].expression[]",
    "subject.domain.restrictions[].values",
    "subject.domain.restrictions[].expression",
    "subject.domain.limit.expression",
    "course.grain",
    "task.required_accuracy.outputs_to_match[].tolerance.metric",
    "task.required_accuracy.outputs_to_match[].tolerance.bound",
    "task.proof_obligations[].antecedent[]",
    "task.proof_obligations[].consequent[]",
)


#: Reference fields named by a dotted path, as :data:`PATH_FORMULA` names expressions.
PATH_REFERENCE: tuple[str, ...] = (
    "course.index",
    "course.varies[]",
)


#: Expression and reference fields of one record type alone, named by dotted paths, as
#: (record type, paths): an answer nests its expressions under its claim and its aim blocks, and
#: another type may use the same key, such as `domain`, with other symbols.
TYPE_PATH_FORMULA: Mapping[str, tuple[str, ...]] = {
    "answer": (
        "claim.expression",
        "claim.presuppositions[].expression",
        "claim.realizations[].by",
        "domain",
        "uncertainty[].expression",
        "aim_block.description.values[].value",
        "aim_block.exploration.space.varied[].range",
        "aim_block.exploration.criterion.expression",
        "aim_block.exploration.classes[].pattern",
        "aim_block.prediction.outputs[].condition",
        "aim_block.prediction.outputs[].value",
        "aim_block.explanation.factors[].holds",
        "aim_block.explanation.factors[].under",
        "aim_block.modal_knowledge.property",
    ),
    "model": ("operations[].regime", "operations[].bound"),
    "derivation": ("objects[].expression",),
    "binding": (
        "feature_pairs[].exemplified",
        "condition_pairs[].model_condition",
        "condition_pairs[].target_condition",
        "domain[].region",
        "structural_discrepancy[].expression",
    ),
}


TYPE_PATH_REFERENCE: Mapping[str, tuple[str, ...]] = {
    "answer": (
        "claim.realizations[].realizes",
        "uncertainty[].of",
        "aim_block.exploration.space.observables[]",
        "aim_block.exploration.space.varied[].factor",
        "aim_block.explanation.factors[].bears_on[]",
        "aim_block.explanation.factors[].through[]",
        "aim_block.explanation.factors[].produces",
        "aim_block.explanation.factors[].separates[]",
        "aim_block.explanation.factors[].appeals_to[]",
    ),
    "model": ("operations[].yields[]",),
}


#: Names a tolerance may use where every other field names a declared symbol: the candidate's
#: value and the observable it reproduces, as the epistemic-task note fixes them.
TOLERANCE_NAMES: frozenset[str] = frozenset({"answer", "target"})


#: Fields holding a reference to a declared symbol, as (block, key).
REFERENCE: tuple[tuple[str, str], ...] = (
    ("variables", "signature"),
    ("parameters", "signature"),
    ("laws", "signature"),
    ("interface", "variable"),
    ("external_systems", "shares"),
    ("organization", "realized_by"),
    ("organization", "among"),
    ("observables", "signature"),
    ("scope_over_instances", "over"),
    ("scope_over_instances", "conditional_on"),
    ("detection_criterion", "across"),
    ("detection_criterion", "limited_by"),
)


def entries(record: Mapping[str, Any], block: str) -> list[Mapping[str, Any]]:
    """Return the entries of ``block``, or none when the record has no such block."""
    return [entry for _, entry in indexed(record, block)]


def indexed(record: Mapping[str, Any], block: str) -> list[tuple[int, Mapping[str, Any]]]:
    """Return the entries of ``block`` with their index in the list, as :func:`entries` selects
    them."""
    value = record.get(block)
    return (
        [(i, e) for i, e in enumerate(value) if isinstance(e, Mapping)]
        if isinstance(value, list)
        else []
    )


def items_of(value: Any) -> list[tuple[int | None, Any]]:
    """Return the items of a field, each with its index, or the value alone with no index.

    >>> items_of(["a", "b"]), items_of("c")
    ([(0, 'a'), (1, 'b')], [(None, 'c')])
    """
    return list(enumerate(value)) if isinstance(value, list) else [(None, value)]


def at_item(place: Place, index: int | None) -> Place:
    """Return the path of one item of a field: the field itself, or the item at ``index``."""
    return place if index is None else (*place, index)


def identifiers(text: str) -> set[str]:
    """Return the identifiers occurring in an expression.

    A binder is written ``op_{indices}``, so its token carries a trailing underscore that is
    stripped before the operator vocabulary is consulted.

    Quoted text is a literal, such as the member names of an enumeration, so it is removed
    before the identifiers are read.

    >>> sorted(identifiers("mean_{x}( u(x) )"))
    ['mean', 'u', 'x']
    >>> sorted(identifiers('enum("A", "B")'))
    ['enum']
    """
    without_literals = re.sub(r"'[^']*'|\"[^\"]*\"", " ", text)
    found = {token.rstrip("_") for token in re.findall(r"[A-Za-z_][A-Za-z_0-9]*", without_literals)}
    return {token for token in found if token}


def bound(text: str) -> set[str]:
    """Return the indices a binder of the expression introduces.

    >>> sorted(bound("mean_{x, t}( u )"))
    ['t', 'x']
    """
    found: set[str] = set()
    for group in re.findall(r"[A-Za-z_][A-Za-z_0-9]*_\{([^}]*)\}", text):
        found |= {name.strip() for name in group.split(",") if name.strip()}
    return found


def formulas(record: Mapping[str, Any]) -> list[tuple[str, Place, str, frozenset[str]]]:
    """Return every expression the record holds, with where it sits, its path and its type
    variables.

    ``where`` names the field as the messages print it; the path reaches the expression itself,
    including its index when the field holds a list of expressions.
    """
    checked: list[tuple[str, Place, Mapping[str, Any], str]] = [
        (f"{block}.{key}", (block, Entry(i, entry)), entry, key)
        for block, key in FORMULA
        for i, entry in indexed(record, block)
    ]
    checked += [
        (f"{outer}.{inner}.{key}", (outer, Entry(i, entry), inner, Entry(j, feature)), feature, key)
        for outer, inner, key in NESTED_FORMULA
        for i, entry in indexed(record, outer)
        for j, feature in indexed(entry, inner)
    ]
    for block, mapping, key in WITHIN_ENTRY:
        for i, entry in indexed(record, block):
            held = entry.get(mapping)
            if isinstance(held, Mapping):
                checked.append(
                    (f"{block}.{mapping}.{key}", (block, Entry(i, entry), mapping), held, key)
                )
    for mapping, inner, key in WITHIN_MAPPING:
        holder = record.get(mapping)
        if isinstance(holder, Mapping):
            checked += [
                (f"{mapping}.{inner}.{key}", (mapping, inner, Entry(i, e)), e, key)
                for i, e in indexed(holder, inner)
            ]
    reached: list[tuple[str, Place, str, frozenset[str]]] = [
        (where, at_item((*place, key), index), text, generic(entry))
        for where, place, entry, key in checked
        for index, text in items_of(entry.get(key))
        if isinstance(text, str) and text.strip()
    ]
    reached += [
        (path, place, text, frozenset())
        for path in (*PATH_FORMULA, *TYPE_PATH_FORMULA.get(str(record.get("type", "")), ()))
        for place, text in reach(record, path)
        if text.strip()
    ]
    return reached


def calls(text: str) -> list[tuple[str, int]]:
    """Return each call an expression makes, with the number of arguments it passes.

    A binder carries the indices it consumes between its name and its arguments, and those are
    not arguments: ``mean_{x, t}( u )`` calls ``mean`` with one.

    >>> calls("div(u, x) = 0")
    [('div', 2)]
    >>> calls("mean_{x, t}( u(a, x) * 2 )")
    [('mean', 1), ('u', 2)]
    """
    found: list[tuple[str, int]] = []
    for match in re.finditer(r"([A-Za-z_]\w*)(_\{[^}]*\})?\s*\(", text):
        depth, argument, empty = 1, 1, True
        for character in text[match.end() :]:
            if character == "(":
                depth += 1
            elif character == ")":
                depth -= 1
                if depth == 0:
                    break
            elif character == "," and depth == 1:
                argument += 1
            if not character.isspace():
                empty = False
        found.append((match.group(1), 0 if empty else argument))
    return found


def generic(entry: Mapping[str, Any]) -> frozenset[str]:
    """Return the type variables an operator is generic in, which its own types may name.

    An operator is usually general where the quantities it acts on are particular: an adjoint
    acts on maps of any set to itself, so its signature names a variable rather than one problem's
    state space. The variable is declared on the operator and reaches its signature and its values.
    """
    held = entry.get("for_any")
    return frozenset(name for name in held or () if isinstance(name, str))


def along(node: Any, path: str) -> list[str]:
    """Return every string the dotted ``path`` reaches, traversing a list wherever it reads ``[]``.

    >>> along({"a": [{"b": "x"}, {"b": "y"}]}, "a[].b")
    ['x', 'y']
    """
    return [text for _, text in reach(node, path)]


def reach(node: Any, path: str) -> list[tuple[Place, str]]:
    """Return every string the dotted ``path`` reaches, each with the field path that reaches it.

    >>> from gnomon.findings import VOCABULARY_UNRESOLVED, finding
    >>> [(finding(VOCABULARY_UNRESOLVED, text, *place).locus, text)
    ...  for place, text in reach({"a": [{"b": "x"}, {"b": "y"}]}, "a[].b")]
    [('/a/0/b', 'x'), ('/a/1/b', 'y')]
    """
    found: list[tuple[Place, Any]] = [((), node)]
    for step in path.split("."):
        key, listed = (step[:-2], True) if step.endswith("[]") else (step, False)
        nxt: list[tuple[Place, Any]] = []
        for place, held in found:
            value = held.get(key) if isinstance(held, Mapping) else None
            if listed and isinstance(value, list):
                nxt.extend(((*place, key, Entry(i, item)), item) for i, item in enumerate(value))
            elif not listed and value is not None:
                nxt.append(((*place, key), value))
        found = nxt
    return [(place, held) for place, held in found if isinstance(held, str)]


def upstream_of(
    record: Mapping[str, Any], records: Mapping[str, Mapping[str, Any]]
) -> Mapping[str, Any]:
    """Return the target system that ``record`` is stated against, or an empty mapping.

    >>> upstream_of({"type": "background", "describes": "system.a"},
    ...             {"system.a": {"id": "system.a"}})
    {'id': 'system.a'}
    """
    field_name = UPSTREAM_FIELD.get(str(record.get("type", "")))
    identifier = record.get(field_name) if field_name else None
    return records.get(identifier, {}) if isinstance(identifier, str) else {}


def visible_records(
    record: Mapping[str, Any], records: Mapping[str, Mapping[str, Any]]
) -> list[Mapping[str, Any]]:
    """Return the records whose symbols the bare identifiers of an answer or a model may name.

    An answer sees the records on which its route runs, and the question that it answers with the
    target system, the phenomenon and the backgrounds of that question; a model sees its parents
    and its background; a binding sees its model, its phenomenon and the target system of that
    phenomenon; a derivation sees the records that hold its premises, the record that it serves and
    the derivations whose consequences it uses. Any other record sees none through this function.

    >>> records = {"quest.a.b": {"subject": {"phenomenon": "phen.a.b"}},
    ...            "phen.a.b": {"id": "phen.a.b"}}
    >>> [r.get("id") for r in visible_records({"type": "answer", "answers": "quest.a.b"}, records)]
    [None, 'phen.a.b']
    """
    kind = record.get("type")
    names: list[Any] = []
    if kind == "answer":
        question = records.get(str(record.get("answers")), {})
        stated = question.get("subject")
        subject: Mapping[str, Any] = stated if isinstance(stated, Mapping) else {}
        names = [
            *((record.get("route") or {}).get("runs_on") or []),
            record.get("answers"),
            subject.get("target_system"),
            subject.get("phenomenon"),
            *(subject.get("background") or []),
        ]
    elif kind == "model":
        names = [*(record.get("derives_from") or []), record.get("background")]
    elif kind == "derivation":
        served = str(record.get("serves") or "")
        split = split_reference(served)
        names = [
            *(record.get("runs_on") or []),
            split[0] if split else served,
            *(record.get("uses") or []),
        ]
    elif kind == "binding":
        stated = record.get("target")
        target: Mapping[str, Any] = stated if isinstance(stated, Mapping) else {}
        phenomenon = records.get(str(target.get("phenomenon")), {})
        names = [record.get("model"), target.get("phenomenon"), phenomenon.get("target_system")]
    found = [
        records[name]
        for name in dict.fromkeys(n for n in names if isinstance(n, str))
        if name in records
    ]
    return found + [
        parent
        for model in found
        if model.get("type") == "model"
        for parent in visible_records(model, records)
        if parent not in found
    ]
