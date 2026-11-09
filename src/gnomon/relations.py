"""
The graph of relations between research units, its checks, and the transmission of a revision.

The relation registry declares each relation (:mod:`gnomon.relation_registry`). This module reads
the edges that a record states: the entries of its lists of relations, the fields that the registry
names, and every other reference in a field of an identifier or of an expression, which transmits a
revision as a constitutive dependence. A reference in prose is no edge.

Functions
---------
edges
    Return the edges that a record states.
relation_findings
    Return the defects of the relations that one record states.
workspace_relation_findings
    Return the relations stated twice and the cycles across the records.
flagged_dependents
    Return the records that a revision of one record flags, each with the reason.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from functools import lru_cache
from itertools import pairwise
from typing import Any, Mapping

from . import findings as rules
from .findings import Entry, Finding, finding
from .identifiers import split_reference
from .itineraries import cycles
from .relation_registry import load_relation_registry
from .schemas import kinds, load_base
from .vocabulary.declarations import references

Records = Mapping[str, Mapping[str, Any]]

#: The kinds of a field whose references are prose, which transmit no revision.
PROSE_KINDS = frozenset({"markdown-line", "markdown"})

#: The declaration of a reference that no relation names: a constitutive dependence.
DEFAULT = {"flags": "source", "warrant": "non-inferential"}

#: The keys of an entry that state the relation and its ends, beyond its attributes.
ENDS = frozenset({"relation", "target", "members"})


@dataclass(frozen=True)
class Edge:
    """One relation that a record states, from the record that holds it to one other end."""

    holder: str
    relation: str
    target: str
    declared: Mapping[str, Any]
    where: tuple[Any, ...]
    entry: Mapping[str, Any] = field(default_factory=dict)
    members: tuple[str, ...] = ()


def owner(ident: str, records: Records) -> str | None:
    """Return the record that an identifier names, itself or the record holding the unit."""
    if ident in records:
        return ident
    split = split_reference(ident)
    return split[0] if split is not None and split[0] in records else None


def _pattern(path: tuple[Any, ...]) -> str:
    """Return a path with each list index written ``[]``, as the registry names a field."""
    text = ""
    for key in path:
        text += "[]" if isinstance(key, int) else (f".{key}" if text else str(key))
    return text


def _bare(pattern: str) -> str:
    return pattern.removesuffix("[]")


@lru_cache(maxsize=32)
def field_kinds(kind: str) -> Mapping[str, str]:
    """Return the kind of each field of a record type, keyed by its pattern."""
    found: dict[str, str] = {}

    def walk(node: Any, path: str) -> None:
        if not isinstance(node, Mapping):
            return
        if path and isinstance(node.get("x-kind"), str):
            found[path] = node["x-kind"]
        for key, value in (node.get("properties") or {}).items():
            walk(value, f"{path}.{key}" if path else str(key))
        if isinstance(node.get("items"), Mapping):
            walk(node["items"], f"{path}[]")

    if kind in kinds():
        walk(load_base(kind), "")
    return found


def _entry_edges(record: Mapping[str, Any], ident: str, family: Mapping[str, Any]) -> list[Edge]:
    """Return the edges of the entries of a list of relations: one per target, or per member."""
    found = []
    list_key, target_key = str(family.get("list")), str(family.get("target_key") or "target")
    declared_relations = family.get("relations") or {}
    for index, entry in enumerate(record.get(list_key) or []):
        if not isinstance(entry, Mapping):
            continue
        declared = declared_relations.get(str(entry.get("relation"))) or _undeclared(family)
        where = (list_key, Entry(index, entry))
        if declared.get("arity") == "set":
            members = tuple(str(m) for m in entry.get("members") or [] if isinstance(m, str))
            found += [
                Edge(ident, str(entry["relation"]), m, declared, where, entry, members)
                for m in members
            ]
        elif isinstance(entry.get(target_key), str):
            relation = str(entry.get("relation") or "link")
            found.append(Edge(ident, relation, entry[target_key], declared, where, entry))
    return found


def _undeclared(family: Mapping[str, Any]) -> Mapping[str, Any]:
    """Return the declaration of an entry whose relation is missing or unknown: its end may take
    any kind that a relation of its list admits, and it transmits nothing."""
    kinds_admitted = sorted(
        {
            kind
            for declared in (family.get("relations") or {}).values()
            for kind in declared.get("targets") or []
        }
    )
    return {"targets": kinds_admitted, "flags": "none"}


def edges(record: Mapping[str, Any]) -> list[Edge]:
    """Return the edges that a record states.

    >>> answer = {"id": "ans.a.x", "type": "answer", "answers": "quest.a.q",
    ...           "relations": [{"relation": "incompatible-with", "members": ["ans.a.y"]}],
    ...           "claim": {"reading": "unlike ans.a.z, the delay grows"}}
    >>> [(e.relation, e.target) for e in edges(answer)]
    [('incompatible-with', 'ans.a.y'), ('answers', 'quest.a.q')]
    """
    registry = load_relation_registry()
    kind, ident = str(record.get("type")), str(record.get("id"))
    family = (registry.get("entries") or {}).get(kind) or {}
    found = _entry_edges(record, ident, family) if family else []
    lists = {str(family.get("list"))} if family else set()
    declared_fields = {
        _bare(path): (path, declared)
        for path, declared in ((registry.get("fields") or {}).get(kind) or {}).items()
    }
    field_kind = field_kinds(kind)
    for path, text in references(record):
        if not path or path[0] in lists or path == ("id",):
            continue
        pattern = _pattern(path)
        named = declared_fields.get(_bare(pattern))
        if named is not None:
            found.append(Edge(ident, named[0], text, named[1], path))
            continue
        kind_of_field = field_kind.get(pattern) or field_kind.get(_bare(pattern))
        if kind_of_field not in PROSE_KINDS:
            found.append(Edge(ident, "reference", text, DEFAULT, path))
    return found


def _family(kind: str) -> Mapping[str, Any]:
    return (load_relation_registry().get("entries") or {}).get(kind) or {}


def _attribute_findings(record: Mapping[str, Any], family: Mapping[str, Any]) -> list[Finding]:
    """Return each entry that lacks an end or an attribute, or carries one not admitted."""
    found = []
    list_key = str(family.get("list"))
    target_key = str(family.get("target_key") or "target")
    modes = load_relation_registry().get("warrant_classes") or {}
    for index, entry in enumerate(record.get(list_key) or []):
        if not isinstance(entry, Mapping):
            continue
        if entry.get("relation") in (None, ""):
            found.append(
                finding(
                    rules.RELATION_MISPLACED_ATTRIBUTE,
                    f"{list_key}[{index}]: the entry names no relation",
                    list_key,
                    Entry(index, entry),
                )
            )
            continue
        declared = (family.get("relations") or {}).get(str(entry.get("relation")))
        if declared is None:
            continue
        admitted = set(declared.get("attributes") or []) | {target_key, "relation"}
        if declared.get("arity") == "set":
            admitted = (admitted - {target_key}) | {"members"}
        stated = {key for key, value in entry.items() if value not in (None, [], "")}
        missing = [key for key in declared.get("required") or [] if key not in stated]
        missing += [
            end
            for end in (["members"] if declared.get("arity") == "set" else [target_key])
            if end not in stated
        ]
        extra = sorted(stated - admitted)
        kind_of_warrant = (
            (entry.get("warrant") or {}) if isinstance(entry.get("warrant"), Mapping) else {}
        )
        if kind_of_warrant.get("kind") is not None and kind_of_warrant.get("kind") not in modes:
            extra.append(f"warrant kind {kind_of_warrant.get('kind')}")
        if missing or extra:
            parts = ([f"lacks {', '.join(missing)}"] if missing else []) + (
                [f"admits no {', '.join(extra)}"] if extra else []
            )
            found.append(
                finding(
                    rules.RELATION_MISPLACED_ATTRIBUTE,
                    f"{list_key}[{index}]: {entry.get('relation')} {' and '.join(parts)}",
                    list_key,
                    Entry(index, entry),
                )
            )
    return found


def relation_findings(record: Mapping[str, Any], records: Records) -> list[Finding]:
    """Return the defects of the relations that one record states: an attribute that its relation
    does not admit or lacks, an end or an attribute naming a record of a kind that the relation
    does not admit, and a relation of the record to itself.

    >>> records = {"ans.a.x": {"type": "answer"}, "quest.a.q": {"type": "question"}}
    >>> answer = {"id": "ans.a.x", "type": "answer",
    ...           "relations": [{"relation": "supports", "target": "quest.a.q"}]}
    >>> [f.rule.id for f in relation_findings(answer, records)]
    ['relation/mistyped-end']
    """
    kind, ident = str(record.get("type")), str(record.get("id"))
    family = _family(kind)
    found = _attribute_findings(record, family) if family else []
    for edge in edges(record):
        found += _attribute_kinds(edge, records)
        other = owner(edge.target, records)
        if other is None:
            continue
        if edge.relation != "reference" and (
            edge.target == ident or (bool(edge.entry) and other == ident)
        ):
            found.append(
                finding(
                    rules.RELATION_SELF,
                    f"{edge.relation}: the record is related to itself through {edge.target}",
                    *edge.where,
                )
            )
            continue
        targets = edge.declared.get("targets")
        if targets and records[other].get("type") not in targets:
            found.append(
                finding(
                    rules.RELATION_MISTYPED_END,
                    f"{edge.relation}: {edge.target} is a {records[other].get('type')}, not a"
                    f" {' or a '.join(targets)}",
                    *edge.where,
                )
            )
    return found


def _attribute_kinds(edge: Edge, records: Records) -> list[Finding]:
    """Return each attribute of an entry that names a record of a kind it does not admit."""
    found = []
    for key, admitted in (edge.declared.get("attribute_targets") or {}).items():
        named = edge.entry.get(key)
        other = owner(named, records) if isinstance(named, str) else None
        if other is not None and records[other].get("type") not in admitted:
            found.append(
                finding(
                    rules.RELATION_MISTYPED_END,
                    f"{edge.relation}: {key} {named} is a {records[other].get('type')}, not a"
                    f" {' or a '.join(admitted)}",
                    *edge.where,
                    key,
                )
            )
    return found


def _restated(records: Records) -> list[tuple[str, Finding]]:
    """Return each symmetric or set relation stated a second time, or covering a stated set."""
    stated: dict[tuple[str, frozenset[str]], str] = {}
    found = []
    for ident in sorted(records):
        for edge in edges(records[ident]):
            declared = edge.declared
            if not (declared.get("arity") == "set" or declared.get("symmetric")):
                continue
            ends = frozenset({ident, *edge.members} if edge.members else {ident, edge.target})
            key = (edge.relation, ends)
            if stated.get(key) == ident:
                continue
            if key in stated:
                text = f"{edge.relation}: already stated by {stated[key]}"
                found.append((ident, finding(rules.RELATION_RESTATED, text, *edge.where)))
                continue
            covered = [
                holder
                for (relation, other), holder in stated.items()
                if relation == edge.relation and (other < ends or ends < other)
            ]
            if covered:
                text = (
                    f"{edge.relation}: its set overlaps the set stated by {covered[0]}, so one"
                    " of them is not minimal"
                )
                found.append((ident, finding(rules.RELATION_RESTATED, text, *edge.where)))
            stated.setdefault(key, ident)
    return found


@dataclass
class _Graphs:
    """The graphs of the relations whose cycles are forbidden or judged, keyed by graph."""

    nodes: dict[str, dict[str, set[str]]] = field(default_factory=dict)
    policies: dict[str, str] = field(default_factory=dict)
    crossed: dict[tuple[str, str, str], str] = field(default_factory=dict)
    where: dict[tuple[str, str], tuple[Any, ...]] = field(default_factory=dict)


def _graphs(records: Records) -> _Graphs:
    """Return the graphs of the relations whose policy forbids or judges cycles, each edge running
    from the dependent end to the end on which it depends."""
    found = _Graphs()
    for ident in sorted(records):
        for edge in edges(records[ident]):
            policy = edge.declared.get("cycles")
            other = owner(edge.target, records)
            if policy not in ("forbidden", "judged") or other is None or other == ident:
                continue
            graph = str(edge.declared.get("graph") or edge.relation)
            dependent, dependence = ident, other
            if edge.declared.get("dependent") == "target":
                dependent, dependence = other, ident
            found.nodes.setdefault(graph, {}).setdefault(dependent, set()).add(dependence)
            found.policies[graph] = str(policy)
            found.crossed.setdefault((graph, dependent, dependence), edge.relation)
            found.where.setdefault((graph, ident), edge.where)
    return found


def _cycles(records: Records) -> list[tuple[str, Finding]]:
    """Return a cycle of each graph whose policy forbids or judges cycles.

    A relation that declares a graph, such as the graph of claims, joins the other relations of
    that graph, so a cycle passing through several of them is found; a relation that declares
    none forms a graph of its own. Each cycle names the relations that it crosses.
    """
    graphs = _graphs(records)
    found = []
    for graph, nodes in sorted(graphs.nodes.items()):
        for cycle in _first_cycles(nodes):
            relations = sorted(
                {
                    graphs.crossed[(graph, a, b)]
                    for a, b in pairwise(cycle)
                    if (graph, a, b) in graphs.crossed
                }
            )
            forbidden = graphs.policies[graph] == "forbidden"
            rule = rules.RELATION_CYCLE if forbidden else rules.RELATION_JUDGED_CYCLE
            text = f"{graph}: {' -> '.join(cycle)}, through {', '.join(relations)}"
            holder = next((n for n in cycle if (graph, n) in graphs.where), cycle[0])
            found.append((holder, finding(rule, text, *graphs.where.get((graph, holder), ()))))
    return found


def _first_cycles(graph: Mapping[str, set[str]]) -> list[list[str]]:
    """Return the cycles of a graph, one per set of nodes, as the search of an itinerary finds.

    >>> _first_cycles({"a": {"b"}, "b": {"a"}, "c": {"a"}})
    [['a', 'b', 'a']]
    """
    found, seen = [], []
    for cycle in cycles(graph):
        nodes = frozenset(cycle)
        if nodes not in seen:
            seen.append(nodes)
            found.append(cycle)
    return found


def _restated_grounds(records: Records) -> list[tuple[str, Finding]]:
    """Return each relation ``supports`` whose target already names the supporting answer, or a
    unit of it, as a ground: the two entries state one dependence twice."""
    found = []
    for ident in sorted(records):
        for edge in edges(records[ident]):
            if edge.relation != "supports":
                continue
            target = records.get(edge.target) or {}
            grounds = [g for g in target.get("grounds") or [] if isinstance(g, Mapping)]
            if any(_reaches(str(g.get("record") or ""), ident) for g in grounds):
                text = f"supports: {edge.target} already names {ident} as a ground"
                found.append((ident, finding(rules.RELATION_RESTATED_GROUND, text, *edge.where)))
    return found


def workspace_relation_findings(records: Records) -> list[tuple[str, Finding]]:
    """Return the relations stated twice, the supports that restate a ground, and the cycles across
    the records, each with the identifier of the record where it is reported."""
    return _restated(records) + _restated_grounds(records) + _cycles(records)


EXACT = frozenset({"exact"})


def _dependent_class(record: Mapping[str, Any]) -> str:
    """Return the warrant class of a dependent whose relation leaves the warrant to it.

    An answer formally proven and a model derived by exact operations alone rest deductively on
    what they cite; every other dependent rests defeasibly.
    """
    if record.get("type") == "answer" and record.get("support") == "formally-proven":
        return "monotonic"
    if record.get("type") == "model" and record.get("derives_from"):
        operations = [op for op in record.get("operations") or [] if isinstance(op, Mapping)]
        if operations and all(op.get("error") in EXACT for op in operations):
            return "monotonic"
    return "defeasible"


def _class_of(edge: Edge, dependent: Mapping[str, Any]) -> str:
    """Return the warrant class of an edge toward the dependent that it may flag."""
    classes = load_relation_registry().get("warrant_classes") or {}
    if edge.declared.get("flags") == "entry":
        return "entry"
    warrant = edge.declared.get("warrant")
    if warrant == "entry":
        stated = edge.entry.get("warrant")
        kind = stated.get("kind") if isinstance(stated, Mapping) else None
        warrant = kind if kind in classes else "dependent"
    if warrant == "dependent":
        return _dependent_class(dependent)
    return str(classes.get(str(warrant), "defeasible"))


def _reaches(text: str, revised: str) -> bool:
    """Return whether an end names the revised record or unit, a unit inside it, or the record
    that holds it."""
    return text == revised or text.startswith(f"{revised}.") or revised.startswith(f"{text}.")


def flagged_dependents(revised: str, kind: str, records: Records) -> dict[str, str]:
    """Return the records that a revision of one record flags, each with the reason of the flag.

    >>> records = {"bg.a.b": {"id": "bg.a.b", "type": "background"},
    ...            "ans.a.x": {"id": "ans.a.x", "type": "answer", "support": "formally-proven",
    ...                        "grounds": [{"record": "bg.a.b.law"}]}}
    >>> flagged_dependents("bg.a.b", "scope-narrowing", records)
    {'ans.a.x': 'grounds[].record (monotonic)'}
    >>> flagged_dependents("bg.a.b", "reorientation", records)
    {}
    """
    transmits = load_relation_registry().get("transmits") or {}
    found: dict[str, str] = {}
    for ident in sorted(records):
        record = records[ident]
        if record.get("type") == "itinerary":
            continue
        for edge in edges(record):
            flags = edge.declared.get("flags")
            if flags in ("source", "entry") and ident != revised and _reaches(edge.target, revised):
                dependent = ident
            elif flags == "target" and _reaches(ident, revised):
                dependent = owner(edge.target, records) or ""
            else:
                continue
            if not dependent or _reaches(dependent, revised) or dependent not in records:
                continue
            klass = _class_of(edge, records[dependent])
            if kind in (transmits.get(klass) or []) and dependent not in found:
                found[dependent] = f"{edge.relation} ({klass})"
    return found


def declared_paths() -> list[tuple[str, str]]:
    """Return each field path that the registry names, with its record kind."""
    fields = load_relation_registry().get("fields") or {}
    return [(str(kind), str(path)) for kind, paths in fields.items() for path in (paths or {})]
