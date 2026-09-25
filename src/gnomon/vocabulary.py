"""
Symbols and operators of an inquiry, collected from the records that declare them.

Three vocabularies meet in a filled inquiry, and they differ by who writes them and how far
they reach:

- the fields and their option lists, fixed by the framework and written by the designer;
- the symbols of one problem (constituents, index sets, variables, parameters, observables),
  written by the author of that problem and scoped to its records;
- the operators, whose canonical part the framework supplies and whose remainder each problem
  declares for its own formulas.

This module owns the second and third. It collects the symbols a problem declares, resolves the
operators available to each of its records, and renders the table an author consults before
choosing a new symbol.

See Also
--------
data/operators.yml : the operator vocabulary the framework supplies.
"""

from __future__ import annotations

import re
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Iterable, Mapping, Sequence

import yaml

DATA = Path(__file__).parent / "data"

#: The registry declaring the operators the framework supplies.
OPERATOR_REGISTRY = DATA / "operators.yml"

#: Blocks whose entries declare a symbol, per record kind.
DECLARING: Mapping[str, tuple[str, ...]] = {
    "target-system": (
        "variants",
        "constituents",
        "index_sets",
        "variables",
        "parameters",
        "laws",
        "organization",
        "external_systems",
    ),
    "phenomenon": ("index_sets", "explanandum_variables", "manifestations", "scope_over_instances"),
}

#: The record kinds the checkers read. A kind declaring no symbol still carries expressions, so
#: this set is wider than the keys of :data:`DECLARING`.
RECORD_KINDS: frozenset[str] = frozenset({"target-system", "phenomenon", "operators", "question"})

#: Fields holding an expression, as (block, key).
FORMULA: tuple[tuple[str, str], ...] = (
    ("variables", "expression"),
    ("variables", "condition"),
    ("parameters", "expression"),
    ("parameters", "condition"),
    ("laws", "expression"),
    ("explanandum_variables", "expression"),
    ("explanandum_variables", "condition"),
    ("manifestations", "expression"),
    ("detection_criterion", "expression"),
    ("constituents", "extent"),
    ("index_sets", "extent"),
    ("operators", "values"),
    ("operators", "signature"),
    ("variables", "values"),
    ("external_systems", "class"),
    ("organization", "relates"),
    ("realizations", "by"),
    ("explanans", "holds"),
    ("proof_obligations", "antecedent"),
    ("proof_obligations", "consequent"),
    ("parameters", "values"),
    ("explanandum_variables", "values"),
)

#: Expression fields inside a mapping carried by a list entry, as (block, mapping, key).
WITHIN_ENTRY: tuple[tuple[str, str, str], ...] = (
    ("explanandum_variables", "event", "origin"),
    ("explanandum_variables", "event", "horizon"),
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
    "task.required_accuracy.outputs_to_match[].tolerance.metric",
    "task.required_accuracy.outputs_to_match[].tolerance.bound",
    "task.proof_obligations[].antecedent[]",
    "task.proof_obligations[].consequent[]",
)

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
    ("explanans", "bears_on"),
    ("explanans", "through"),
    ("explanans", "separates"),
    ("explanans", "appeals_to"),
    ("organization", "realized_by"),
    ("organization", "among"),
    ("realizations", "realizes"),
    ("realizations", "variant"),
    ("explanandum_variables", "signature"),
    ("scope_over_instances", "over"),
    ("scope_over_instances", "conditional_on"),
    ("detection_criterion", "across"),
    ("detection_criterion", "limited_by"),
)
@dataclass(frozen=True)
class Declaration:
    """One symbol a record declares, with what the author needs in order to reuse or avoid it.

    Attributes
    ----------
    symbol : str
        The identifier, unique within its record.
    name : str
        The name in words.
    block : str
        The block that declares the symbol, and so the kind of object the symbol names.
    record : str
        The identifier of the declaring record.
    signature : tuple of str
        The indices the quantity takes, empty for a scalar or for a set.
    """

    symbol: str
    name: str
    block: str
    record: str
    signature: tuple[str, ...] = ()
@dataclass
class Problem:
    """The vocabulary of one problem, collected from the records filled for it.

    Attributes
    ----------
    name : str
        The directory holding the records.
    declarations : list of Declaration
        Every symbol the problem declares, in record then block order.
    canonical : frozenset of str
        The operators the framework supplies.
    local : dict
        The operators the problem declares, each mapped to its name.
    interactions : list of dict
        The directed interaction graph its target system states, one entry per edge.
    """

    name: str
    declarations: list[Declaration] = field(default_factory=list)
    canonical: frozenset[str] = frozenset()
    local: dict[str, str] = field(default_factory=dict)
    interactions: list[dict[str, Any]] = field(default_factory=list)

    @property
    def operators(self) -> frozenset[str]:
        """Every operator the formulas of this problem may use."""
        return self.canonical | frozenset(self.local)

    def collisions(self) -> dict[str, list[str]]:
        """Return each symbol declared by more than one record, with those records.

        A symbol is unique within a record, so a repetition across records is admitted. It is
        reported because the same letter then denotes two quantities the author must keep apart.
        """
        by_symbol: dict[str, list[str]] = {}
        for entry in self.declarations:
            by_symbol.setdefault(entry.symbol, []).append(entry.record)
        return {s: r for s, r in by_symbol.items() if len(set(r)) > 1}
def entries(record: Mapping[str, Any], block: str) -> list[Mapping[str, Any]]:
    """Return the entries of ``block``, or none when the record has no such block."""
    value = record.get(block)
    return [e for e in value if isinstance(e, Mapping)] if isinstance(value, list) else []
def canonical_operators(source: Path | None = None) -> frozenset[str]:
    """Return the operator vocabulary the framework supplies.

    The registry beside this module owns the vocabulary, so extending the framework means editing
    one data file. The method note documents the same set and is checked against it, and no
    check reads that note.

    Raises
    ------
    ValueError
        If the registry declares no operator.
    """
    registry = yaml.safe_load((source or OPERATOR_REGISTRY).read_text(encoding="utf-8")) or {}
    found = frozenset(
        entry["symbol"]
        for entry in registry.get("operators") or []
        if isinstance(entry.get("symbol"), str)
    )
    if not found:
        raise ValueError(f"{(source or OPERATOR_REGISTRY).name} declares no operator")
    return found
def mistyped_symbols(record: Mapping[str, Any]) -> list[str]:
    """Return every ``symbol`` entry that YAML did not resolve to a string.

    YAML 1.1 reads ``on``, ``off``, ``yes``, ``no``, ``y``, ``n``, ``true`` and ``false`` as
    booleans, and ``null`` and ``~`` as nothing, so an unquoted symbol drawn from that set
    silently becomes a value of another type. Reporting it prevents a declaration from
    disappearing without a diagnostic.
    """
    blocks = (*DECLARING.get(str(record.get("type", "")), ()), "operators")
    found = []
    for block in blocks:
        for entry in entries(record, block):
            if "symbol" in entry and not isinstance(entry["symbol"], str):
                found.append(f"{block}: {entry['symbol']!r} is {type(entry['symbol']).__name__}, not a symbol")
    return found
def split_expressions(record: Mapping[str, Any]) -> list[str]:
    """Return every expression a serializer split into fragments.

    An unquoted expression inside a bracketed list splits on its commas, so the record holds
    plausible fragments rather than one value. A fragment is reported by its unbalanced
    parentheses.
    """
    found = []
    for block, key in (*FORMULA, *REFERENCE):
        for entry in entries(record, block):
            value = entry.get(key)
            for item in value if isinstance(value, list) else []:
                if isinstance(item, str) and item.count("(") != item.count(")"):
                    found.append(f"{block}.{key}: {item!r} is a fragment of a split expression")
    return found
def corrupted_notation(record: Mapping[str, Any]) -> list[str]:
    """Return every notation a serializer damaged by reading a backslash as an escape.

    A double-quoted YAML scalar processes ``\\n``, ``\\t`` and their kin, so a LaTeX form such as
    ``\\nu`` arrives as a newline followed by a letter. A control character in a notation is the
    trace of that reading.
    """
    found = []
    for block in ("constituents", "index_sets", "variables",
                  "parameters", "explanandum_variables", "operators", "terms"):
        for entry in entries(record, block):
            form = entry.get("notation")
            if isinstance(form, str) and any(c in form for c in "\n\t\r\x0b\x0c\x08\x07"):
                found.append(f"{block}.{entry.get('symbol')}: the notation holds a control character")
    return found
def misplaced_sharing(record: Mapping[str, Any]) -> list[str]:
    """Return every shared variable that names something other than a quantity.

    A variable crosses the boundary of the system, so it is one the record declares as a state
    variable, an exogenous variable or a parameter. A constituent kind and an index set are sets,
    and a set does not cross a boundary. The direction of the exchange is read from the declaring
    block rather than declared again.
    """
    quantities = {
        e["symbol"]
        for block in ("variables", "parameters")
        for e in entries(record, block)
        if isinstance(e.get("symbol"), str)
    }
    found = []
    for entry in entries(record, "external_systems"):
        for name in entry.get("shares") or []:
            if isinstance(name, str) and name not in quantities:
                found.append(f"external_systems.shares: {name} is no declared quantity")
    return found
def unfixed_parameters(record: Mapping[str, Any]) -> list[str]:
    """Return every parameter whose signature runs along an interval index.

    A parameter is held fixed while the phenomenon unfolds, so a quantity indexed by an ordered
    continuum varies during the dynamics and is an exogenous variable instead.
    """
    running = {
        e["symbol"]
        for e in entries(record, "index_sets")
        if isinstance(e.get("symbol"), str) and e.get("structure") == "interval"
    }
    found = []
    for entry in entries(record, "parameters"):
        along = [s for s in entry.get("signature") or [] if s in running]
        if along:
            found.append(f"parameters.{entry.get('symbol')}: held fixed yet indexed by {along}")
    return found
def doubly_defined(record: Mapping[str, Any]) -> list[str]:
    """Return every quantity carrying both an expression and a condition.

    An expression builds the quantity and cannot be false; a condition states what it satisfies
    and presupposes that such a value exists. Carrying both would define the quantity twice.
    """
    found = []
    for block in ("variables", "parameters", "explanandum_variables"):
        for entry in entries(record, block):
            if entry.get("expression") and entry.get("condition"):
                found.append(f"{block}.{entry.get('symbol')}: both an expression and a condition")
    return found
def unowned_quantities(record: Mapping[str, Any]) -> list[str]:
    """Return every quantity naming an owner that the record declares no external system for.

    A quantity characterizes the target system unless it names an external system as its owner,
    so an owner that resolves to nothing leaves the quantity attached to no system at all.
    """
    systems = {
        e["symbol"] for e in entries(record, "external_systems") if isinstance(e.get("symbol"), str)
    }
    found = []
    for block in ("variables", "parameters"):
        for entry in entries(record, block):
            owner = entry.get("of")
            if isinstance(owner, str) and owner not in systems:
                found.append(f"{block}.{entry.get('symbol')}: no external system named {owner}")
    return found
def unselected_conditions(record: Mapping[str, Any]) -> list[str]:
    """Return every quantity fixed by a condition without saying which value it denotes.

    A condition may hold of several values, so the record states whether exactly one is
    presupposed, whether the claim holds of any of them, or whether the quantity is the set.
    """
    found = []
    for block in ("variables", "parameters", "explanandum_variables"):
        for entry in entries(record, block):
            if entry.get("condition") and entry.get("selects") not in ("unique", "any", "all"):
                found.append(f"{block}.{entry.get('symbol')}: a condition without a selection rule")
    for entry in entries(record, "manifestations"):
        for feature in entries(entry, "features"):
            if feature.get("condition") and feature.get("selects") not in ("unique", "any", "all"):
                found.append(
                    f"manifestations.features.{feature.get('symbol')}: a condition without a selection rule"
                )
    return found
def vacuous_shared(record: Mapping[str, Any]) -> list[str]:
    """Return every quantity that marks ``shared`` while taking no signature.

    ``shared`` asserts that one value holds across every tuple of the signature, so a quantity
    with no signature has nothing to hold it across and the field states nothing.
    """
    found = []
    for block in ("variables", "parameters"):
        for entry in entries(record, block):
            if "shared" in entry and not (entry.get("signature") or []):
                found.append(f"{block}.{entry.get('symbol')}: shared without a signature")
    return found
def declarations(record: Mapping[str, Any]) -> list[Declaration]:
    """Return every symbol the record declares, in block order."""
    found: list[Declaration] = []
    identifier = str(record.get("id", ""))
    for block in DECLARING.get(str(record.get("type", "")), ()):
        for entry in entries(record, block):
            symbol = entry.get("symbol")
            if isinstance(symbol, str):
                signature = entry.get("signature") or []
                found.append(
                    Declaration(
                        symbol=symbol,
                        name=str(entry.get("name") or entry.get("over") or ""),
                        block=block,
                        record=identifier,
                        signature=tuple(s for s in signature if isinstance(s, str)),
                    )
                )
    for entry in entries(record, "explanandum_variables"):
        pointer = entry.get("reference")
        if isinstance(pointer, str) and "#" in pointer:
            source, symbol = pointer.split("#", 1)
            found.append(Declaration(symbol, "", "referenced", source))
    for entry in entries(record, "manifestations"):
        for feature in entries(entry, "features"):
            symbol = feature.get("symbol")
            if isinstance(symbol, str):
                found.append(
                    Declaration(symbol, str(feature.get("name") or ""), "manifestations.features", identifier)
                )
    return found
def local_operators(record: Mapping[str, Any]) -> dict[str, str]:
    """Return the operators the record declares for its own formulas, each with its name."""
    return {
        str(e["symbol"]): str(e.get("name") or "")
        for e in entries(record, "operators")
        if isinstance(e.get("symbol"), str)
    }
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
def formulas(record: Mapping[str, Any]) -> list[tuple[str, str, frozenset[str]]]:
    """Return every expression the record holds, with where it sits and its type variables."""
    checked: list[tuple[str, Mapping[str, Any], str]] = [
        (f"{block}.{key}", entry, key) for block, key in FORMULA for entry in entries(record, block)
    ]
    checked += [
        (f"{outer}.{inner}.{key}", feature, key)
        for outer, inner, key in NESTED_FORMULA
        for entry in entries(record, outer)
        for feature in entries(entry, inner)
    ]
    for block, mapping, key in WITHIN_ENTRY:
        for entry in entries(record, block):
            held = entry.get(mapping)
            if isinstance(held, Mapping):
                checked.append((f"{block}.{mapping}.{key}", held, key))
    for mapping, inner, key in WITHIN_MAPPING:
        holder = record.get(mapping)
        if isinstance(holder, Mapping):
            checked += [(f"{mapping}.{inner}.{key}", e, key) for e in entries(holder, inner)]
    reached: list[tuple[str, str, frozenset[str]]] = [
        (where, text, generic(entry))
        for where, entry, key in checked
        for text in (lambda v: v if isinstance(v, list) else [v])(entry.get(key))
        if isinstance(text, str) and text != "open"
    ]
    reached += [
        (path, text, frozenset())
        for path in PATH_FORMULA
        for text in along(record, path)
        if text != "open"
    ]
    return reached


def calls(text: str) -> list[tuple[str, int]]:
    """Return each call an expression makes, with the number of arguments it passes.

    A binder carries the indices it consumes between its name and its arguments, and those are
    not arguments: ``mean_{x, t}( u )`` calls ``mean`` with one.

    >>> calls("div(u) = 0")
    [('div', 1)]
    >>> calls("mean_{x, t}( u(a, x) * 2 )")
    [('mean', 1), ('u', 2)]
    """
    found: list[tuple[str, int]] = []
    for match in re.finditer(r"([A-Za-z_]\w*)(_\{[^}]*\})?\s*\(", text):
        depth, argument, empty = 1, 1, True
        for character in text[match.end():]:
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


def mismatched_arity(record: Mapping[str, Any], arities: Mapping[str, int]) -> list[str]:
    """Return every call passing a number of arguments its operator does not take.

    An operator states what it takes, so a call that passes more or fewer is reported. Only an
    operator whose signature is a list of sets is checked: one left open states no arity, and a
    quantity applied to its own indices is not an operator call at all.
    """
    found = []
    for where, text, _ in formulas(record):
        for name, passed in calls(text):
            expected = arities.get(name)
            if expected is not None and passed != expected:
                found.append(f"{where}: {name} takes {expected} arguments and is passed {passed}")
    return found


def arities(*records: Mapping[str, Any], source: Path | None = None) -> dict[str, int]:
    """Return the number of arguments each operator takes, where its signature says."""
    registry = yaml.safe_load((source or OPERATOR_REGISTRY).read_text(encoding="utf-8"))
    found = {}
    for entry in list(registry.get("operators") or []) + [
        e for record in records for e in entries(record, "operators")
    ]:
        signature = entry.get("signature")
        if isinstance(signature, list) and all(isinstance(s, str) for s in signature):
            found[str(entry.get("symbol"))] = len(signature)
    return found


def unresolved(
    record: Mapping[str, Any],
    operators: Iterable[str],
    external: Iterable[str] = (),
) -> list[str]:
    """Return every reference and formula identifier of the record that resolves to nothing.

    Parameters
    ----------
    record : mapping
        One filled inquiry record.
    operators : iterable of str
        The operators available to this record: the canonical set and its own declarations.
    external : iterable of str
        Symbols declared by a record this one references, such as the target system of a
        phenomenon.
    """
    available = frozenset(operators)
    known = (
        {entry.symbol for entry in declarations(record)}
        | set(external)
        | set(local_operators(record))
    )
    problems: list[str] = []
    for block, key in REFERENCE:
        for entry in entries(record, block):
            value = entry.get(key)
            for name in value if isinstance(value, list) else [value]:
                if isinstance(name, str) and "#" not in name and name not in known:
                    problems.append(f"{block}.{key} -> {name}")
    for outer, inner, key in NESTED_REFERENCE:
        for entry in entries(record, outer):
            for nested in entries(entry, inner):
                value = nested.get(key)
                for name in value if isinstance(value, list) else [value]:
                    if isinstance(name, str) and "#" not in name and name not in known:
                        problems.append(f"{outer}.{inner}.{key} -> {name}")
    for where, text, variables in formulas(record):
        reachable = known | bound(text) | available | variables
        if where.startswith("task.required_accuracy.outputs_to_match[].tolerance"):
            reachable |= TOLERANCE_NAMES
        problems += [
            f"{where} -> {name}" for name in sorted(identifiers(text)) if name not in reachable
        ]
    return problems
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
    found: list[Any] = [node]
    for step in path.split("."):
        key, listed = (step[:-2], True) if step.endswith("[]") else (step, False)
        nxt: list[Any] = []
        for held in found:
            value = held.get(key) if isinstance(held, Mapping) else None
            if listed and isinstance(value, list):
                nxt.extend(value)
            elif not listed and value is not None:
                nxt.append(value)
        found = nxt
    return [held for held in found if isinstance(held, str)]
def declared_variants(record: Mapping[str, Any]) -> frozenset[str]:
    """Return the shapes a member of the reference class may take, which only a target declares."""
    return frozenset(
        entry["symbol"] for entry in entries(record, "variants") if isinstance(entry.get("symbol"), str)
    )


def variant_symbols(record: Mapping[str, Any]) -> dict[str, str]:
    """Return every symbol only some members carry, mapped to the variant that carries it."""
    found: dict[str, str] = {}
    for block in DECLARING.get(str(record.get("type", "")), ()):
        for entry in entries(record, block):
            symbol, variant = entry.get("symbol"), entry.get("variant")
            if isinstance(symbol, str) and isinstance(variant, str):
                found[symbol] = variant
    return found
def overreaching_declarations(record: Mapping[str, Any]) -> list[str]:
    """Return every entry of the target asserting of all members what only some of them can bear.

    An entry left unmarked asserts something of every member of the reference class. When it names
    a symbol that only one variant declares, it is not false of the other members but unreadable
    for them: the quantity it governs does not exist there. A law names its quantities in its
    expression, a relation of the organization names the parts it runs between and the laws that
    realize it, and an external system names what it shares, so each reaches the class the same
    way.
    """
    variants = variant_symbols(record)
    found = []
    for block, keys in (
        ("laws", ("expression",)),
        ("organization", ("relates", "among", "realized_by")),
        ("external_systems", ("shares",)),
    ):
        for entry in entries(record, block):
            if entry.get("variant"):
                continue
            for key in keys:
                value = entry.get(key)
                for text in value if isinstance(value, list) else [value]:
                    if not isinstance(text, str):
                        continue
                    for name in sorted(identifiers(text)):
                        if name in variants:
                            found.append(
                                f"{block}.{entry.get('name') or entry.get('symbol')}: {name} is"
                                f" carried only by the {variants[name]} variant"
                            )
    return found
#: Fields of an entry holding an expression or a reference, so a symbol in them is load-bearing.
FORMAL_KEYS: frozenset[str] = frozenset(
    {
        "expression", "condition", "values", "extent", "signature", "observed", "effect",
        "over", "across", "conditional_on", "selects_on", "origin", "horizon", "influence",
        "constrains", "shares", "relates", "among",
    }
)


def misattributed_appeals(record: Mapping[str, Any], systems: Iterable[str]) -> list[str]:
    """Return every explanans appealing to something that is not an external system.

    An answer may explain the phenomenon by the environment rather than by the target alone: by
    the structure of the inputs, or by the class of system that reads the outputs. Naming that
    environment is what makes the appeal checkable, so it resolves to an external system the
    target declares. A quantity that system owns is reached as a term, under its own symbol.
    """
    declared = set(systems)
    return [
        f"explanans.appeals_to: {name} is no external system of the target"
        for entry in entries(record, "explanans")
        for name in entry.get("appeals_to") or []
        if isinstance(name, str) and name not in declared
    ]


def unborne_variants(record: Mapping[str, Any]) -> list[str]:
    """Return every variant the record declares and no declaration or law carries.

    A variant is one shape a member may take, written as a partition of the record's own
    declarations, so one that nothing carries names an alternative the record cannot generate:
    the other members stay describable and this one has no schema at all. A record may admit the
    gap by marking the variant open in its maturity, which is what turns that marker from an
    assertion nothing reads into a licence the check consults.

    The count is structural rather than lexical. The name of a variant recurs in its own prose
    and in the marker admitting it, so counting occurrences would find an empty variant reached.
    """
    borne: dict[str, int] = {}
    for block in DECLARING.get(str(record.get("type", "")), ()):
        for entry in entries(record, block):
            carried = entry.get("variant")
            if isinstance(carried, str):
                borne[carried] = borne.get(carried, 0) + 1
    admitted = record.get("maturity") or {}
    found = []
    for variant in entries(record, "variants"):
        symbol = str(variant.get("symbol"))
        if borne.get(symbol) or admitted.get(f"variants.{symbol}") == "open":
            continue
        found.append(
            f"variants.{symbol}: no declaration or law carries it, and its maturity admits no gap"
        )
    return found


def misnamed_variant(record: Mapping[str, Any], variants: Iterable[str]) -> list[str]:
    """Return every variant the record names that the target does not declare.

    A variant is not one symbol among the others: an entry marked by a symbol that names no
    variant claims to hold of a part of the class that does not exist, and an unmarked entry
    claims to hold of all of it, so the mark is read as true wherever it is read at all. The walk
    reaches every position a mark may take, since a block gaining one is not to gain a hole.
    """
    declared = set(variants)

    def walk(node: Any, where: str) -> list[str]:
        if isinstance(node, Mapping):
            found = [
                f"{where}variant -> {node['variant']}"
                if isinstance(node.get("variant"), str) and node["variant"] not in declared
                else ""
            ]
            for key, value in node.items():
                found += walk(value, f"{where}{key}.")
            return [problem for problem in found if problem]
        if isinstance(node, list):
            return [p for item in node for p in walk(item, where)]
        return []

    return walk(record, "")


def overreaching_entries(record: Mapping[str, Any], marked: Mapping[str, str]) -> list[str]:
    """Return every entry asserting of all members what only some of them can bear.

    ``marked`` maps each symbol that only some members carry to the variant carrying it, as the
    target system states it. Neither a phenomenon nor an answer declares a variant of its own, so
    the fact reaches them from the record they are about: an entry naming such a symbol holds of
    that variant and says so, or it ranges over members for which its claim cannot be read at all.

    An answer may name the variant it accounts for once, on the record, and every entry of it
    inherits that; a part of it narrower still names its own.
    """
    found: list[str] = []
    default = record.get("variant")

    def scan(where: str, entry: Mapping[str, Any]) -> None:
        variant = entry.get("variant") or default
        for key, value in entry.items():
            if key not in FORMAL_KEYS:
                continue
            for text in value if isinstance(value, list) else [value]:
                if not isinstance(text, str):
                    continue
                for symbol in sorted(identifiers(text)):
                    if symbol in marked and variant != marked[symbol]:
                        found.append(
                            f"{where}.{entry.get('name') or entry.get('symbol')}: {symbol} is"
                            f" carried only by the {marked[symbol]} variant"
                        )

    for block in ("explanandum_variables", "manifestations", "scope_over_instances",
                  "detection_criterion", "constituents", "index_sets", "variables",
                  "parameters", "laws", "organization", "realizations", "explanans"):
        for entry in entries(record, block):
            scan(block, entry)
    holder = record.get("conditions_and_byproducts")
    if isinstance(holder, Mapping):
        for kind in ("precipitating", "inhibiting", "modulating", "nonstandard", "byproducts"):
            for entry in entries(holder, kind):
                scan(f"conditions_and_byproducts.{kind}", entry)
    return found


def interaction_graph(record: Mapping[str, Any]) -> list[dict[str, Any]]:
    """Return the directed interaction graph the record states, one entry per relation.

    An edge is an entry of the organization: the ordered tuples the relation runs along, the reach
    last and every source before it, and the laws that state it. A tuple of three or more carries a
    joint relation, which no pair of endpoints could state. What the relation passes through is read
    from the expressions of the laws realizing it, being the quantities indexed by every place, so
    neither the endpoints nor the carriers are written a second time.

    The nodes are constituent kinds and index sets, not identified members: which tuples are joined
    is fixed by a parameter of a member model, which the record does not value, so the relation says
    where the edges of one member are to be read from.

    >>> record = {"type": "target-system",
    ...           "variables": [{"symbol": "u", "signature": ["sub", "sub", "t"]}],
    ...           "laws": [{"symbol": "transmit", "expression": "u = emit(z)"}],
    ...           "organization": [{"symbol": "coupling", "relates": "prod(sub, sub)",
    ...                             "realized_by": ["transmit"]}]}
    >>> interaction_graph(record)
    [{'edge': 'coupling', 'sources': ['sub'], 'reach': 'sub', 'through': ['u'], 'tuples': 'prod(sub, sub)'}]
    """
    signatures = {d.symbol: d.signature for d in declarations(record)}
    stated = {
        str(law.get("symbol")): law.get("expression")
        for law in entries(record, "laws")
        if isinstance(law.get("expression"), str)
    }
    graph = []
    for relation in entries(record, "organization"):
        places = influence_places(str(relation.get("relates") or ""))
        text = " ".join(
            stated.get(str(name), "") for name in relation.get("realized_by") or []
        )
        carriers = [
            name
            for name in sorted(identifiers(text))
            if places and joins(list(signatures.get(name, ())), places)
        ]
        graph.append(
            {
                "edge": relation.get("symbol"),
                "sources": places[:-1],
                "reach": places[-1] if places else None,
                "through": carriers,
                "tuples": relation.get("relates"),
            }
        )
    return graph


def influence_places(influence: str) -> list[str]:
    """Return the places an influence runs along, the reach last.

    >>> influence_places("subset(prod(sub, sub), Aij)")
    ['sub', 'sub']
    >>> influence_places("prod(pop, pop, pop)")
    ['pop', 'pop', 'pop']
    """
    found = re.search(r"prod\(([^()]*)\)", influence)
    if not found:
        return []
    places = [part.strip() for part in found.group(1).split(",")]
    return places if len(places) > 1 and all(re.fullmatch(r"[A-Za-z_]\w*", p) for p in places) else []


def unordered_interactions(record: Mapping[str, Any]) -> list[str]:
    """Return every influence that names no ordered product of declared kinds.

    The direction of an influence is the order of the tuples it runs along, so a tuple set that
    is not a product of two or more declared kinds leaves the edge without a reach.
    """
    kinds = {
        entry.get("symbol")
        for block in ("constituents", "index_sets")
        for entry in entries(record, block)
    }
    found = []
    for relation in entries(record, "organization"):
        if relation.get("among"):
            continue                       # its ends are laws, and malformed_relations checks those
        places = influence_places(str(relation.get("relates") or ""))
        if not places or any(place not in kinds for place in places):
            found.append(
                f"organization.{relation.get('symbol')}:"
                " the relation names no ordered product of declared kinds"
            )
    return found


def malformed_relations(record: Mapping[str, Any]) -> list[str]:
    """Return every relation of the organization that does not say what its ends are.

    A relation runs between parts or between laws, never both. Between parts it names the tuples
    it runs along, one per pair of members, and the laws realizing it supply what it carries.
    Between laws it names the laws themselves, in order, with the reach last: two activities may
    stand in an order that no quantity carries, as when one runs only after another has completed
    and no index of the model relates their clocks. Where a shared index already fixes the order,
    the expressions carry it and the relation would restate them, which is why the corpus states
    none.
    """
    laws = {law.get("symbol") for law in entries(record, "laws")}
    found = []
    for relation in entries(record, "organization"):
        where = f"organization.{relation.get('symbol')}"
        relates, among = relation.get("relates"), relation.get("among")
        if bool(relates) == bool(among):
            found.append(
                f"{where}: a relation runs between parts or between laws, and this one names"
                f" {'both' if relates else 'neither'}"
            )
            continue
        if not among:
            continue
        if not isinstance(among, list) or len(among) < 2:
            found.append(f"{where}: a relation among laws orders two or more of them")
            continue
        for name in among:
            if name not in laws:
                found.append(f"{where}: {name} is no law of the record")
    return found


def joins(signature: list[str], endpoints: Sequence[Any]) -> bool:
    """Return whether the signature carries every endpoint, counting a repeated kind twice."""
    remaining = list(signature)
    for endpoint in endpoints:
        if not isinstance(endpoint, str):
            return False
        if endpoint not in remaining:
            return False
        remaining.remove(endpoint)
    return True
def misrouted_interactions(record: Mapping[str, Any]) -> list[str]:
    """Return every interaction whose law names no quantity indexed by both its endpoints.

    An influence from one part to another is carried by something the ordered pair shares, so the
    law asserting it names a quantity taking both endpoints in its signature. A law naming only
    quantities of the source states a property of the source, not an influence on anything.
    """
    return [
        f"organization.{edge['edge']}: the laws stating it name no quantity indexed by"
        f" every one of {edge['sources'] + [edge['reach']]}"
        for edge in interaction_graph(record)
        if not edge["through"]
    ]
#: Blocks whose declarations exist to be reached by another field. A manifestation, a source of
#: variation, an observable or a feature is terminal: it states the phenomenon rather than serving it.
REACHED: frozenset[str] = frozenset(
    {"constituents", "index_sets", "variables", "parameters"}
)
def unused_declarations(directory: Path, registry: Path | None = None) -> list[str]:
    """Return every quantity the problem declares that no other field of it mentions.

    A declaration that nothing reaches is either a stray specification or the trace of a law the
    record never wrote, and the two are told apart by reading. The count is lexical, as the
    operator check is: a symbol occurring once occurs only at its own declaration.

    Only the blocks of :data:`REACHED` are reported. A manifestation or an observable is terminal
    by design, since a question reaches it from outside the problem or nothing reaches it at all.
    """
    sources = [p for p in sorted(directory.glob("*.yml")) if p.name != "vocabulary.yml"]
    text = " ".join(p.read_text(encoding="utf-8") for p in sources)
    found = []
    for declaration in load_problem(directory, registry).declarations:
        if declaration.block not in REACHED:
            continue
        symbol = re.escape(declaration.symbol)
        if len(re.findall(rf"(?<![\w.]){symbol}(?![\w])", text)) <= 1:
            found.append(f"{declaration.block}.{declaration.symbol}: declared and never used")
    return found
def load_problem(directory: Path, registry: Path | None = None) -> Problem:
    """Collect the vocabulary of the problem whose records fill ``directory``."""
    problem = Problem(name=directory.name, canonical=canonical_operators(registry))
    for path in sorted(directory.glob("*.yml")):
        record = yaml.safe_load(path.read_text(encoding="utf-8"))
        if not isinstance(record, Mapping):
            continue
        problem.declarations.extend(declarations(record))
        problem.local.update(local_operators(record))
        problem.interactions.extend(interaction_graph(record))
    return problem
def as_data(problem: Problem) -> dict[str, Any]:
    """Return the vocabulary of a problem in the record form it is stored in."""
    return {
        "id": f"vocab.{problem.name}",
        "type": "vocabulary",
        "problem": problem.name,
        "generated_by": "gnomon vocabulary",
        "symbols": [
            {
                "symbol": entry.symbol,
                "declared_in": entry.record,
                "block": entry.block,
                "signature": list(entry.signature),
                "name": entry.name,
            }
            for entry in sorted(problem.declarations, key=lambda d: (d.record, d.block, d.symbol))
        ],
        "reused_across_records": {s: sorted(set(r)) for s, r in sorted(problem.collisions().items())},
        "operators": {
            "canonical": sorted(problem.canonical),
            "declared": dict(sorted(problem.local.items())),
        },
        "interactions": problem.interactions,
    }
def render_yaml(problem: Problem) -> str:
    """Return the vocabulary as the YAML the command writes."""
    header = (
        "# Generated by `gnomon vocabulary` from the filled records. Edit a record, not this file.\n"
        "# A symbol is unique within its record, so the same letter may return under another record.\n"
    )
    return header + yaml.safe_dump(as_data(problem), sort_keys=False, allow_unicode=True, width=100)
def render_markdown(problem: Problem, index_path: str = "_index.md") -> str:
    """Return the table an author reads, built from the same record.

    Parameters
    ----------
    problem : Problem
        The vocabulary of one problem.
    index_path : str
        Target of the frontmatter ``index`` link: the index of the folder holding the problem,
        written from the root of the workspace, since notes link their parent index from there.

    Returns
    -------
    str
        The Markdown page, frontmatter included.
    """
    data = as_data(problem)
    lines = [
        "---",
        "tags:",
        "  - generated",
        f'index: "[{problem.name}]({index_path})"',
        "---",
        f"# Vocabulary of {problem.name}",
        "",
        "Built by `gnomon vocabulary --markdown` from `vocabulary.yml`. Edit a record, not this file.",
        "",
        "## Symbols",
        "",
        "| Symbol | Declared in | Block | Signature | Gloss |",
        "| --- | --- | --- | --- | --- |",
    ]
    for entry in data["symbols"]:
        signature = ", ".join(entry["signature"]) or "—"
        lines.append(
            f"| `{entry['symbol']}` | {entry['declared_in']} | {entry['block'].replace('_', ' ')} "
            f"| {signature} | {entry['name']} |"
        )
    if data["reused_across_records"]:
        lines += ["", "## Symbols reused across records", ""]
        lines += [
            f"- `{s}` denotes a distinct quantity in {', '.join(r)}."
            for s, r in data["reused_across_records"].items()
        ]
    if data["interactions"]:
        lines += [
            "",
            "## Directed interactions",
            "",
            "The nodes are kinds, not identified members: which tuples are joined is fixed by a parameter"
            " of a member model, and the last column says where to read it from. A tuple of three or"
            " more carries a joint influence, which no pair of endpoints could state.",
            "",
            "| Sources | Edge | Reach | Through | Ordered tuples |",
            "| --- | --- | --- | --- | --- |",
        ]
        for edge in data["interactions"]:
            through = ", ".join(f"`{c}`" for c in edge["through"]) or "—"
            sources = " · ".join(f"`{c}`" for c in edge["sources"]) or "—"
            lines.append(
                f"| {sources} | `{edge['edge']}` | `{edge['reach']}` | {through} | `{edge['tuples']}` |"
            )
    lines += ["", "## Operators", ""]
    lines += [f"- Canonical: {', '.join(f'`{o}`' for o in data['operators']['canonical'])}."]
    declared = data["operators"]["declared"]
    lines += [
        f"- Declared by this problem: {', '.join(f'`{o}` ({g})' for o, g in declared.items())}."
        if declared else "- This problem declares no operator of its own."
    ]
    return "\n".join(lines) + "\n"
