"""
The export of a project: its research units and the relations between them, in the contract
``ekthesis:export@1`` that ``ekthesis`` publishes.

The export is generated from the records and never edited. Its units are declared per record kind
in the registry ``data/registries/export.yml``: each record of a declared kind, and each unit of a
declared list inside it. Its relations are the edges of the records whose declaration in the
relation registry names a class of the contract, read through :func:`gnomon.relations.edges`. A
relation is exported only when both of its ends, or all of its members, are exported units; the
others are returned as dropped, so that the command reports them.

The export holds no date, no revision and no absolute path, so two runs on unchanged records write
the same bytes. The decision on the research export states each rule.

See Also
--------
gnomon.relations : the edges of a record, and their declarations.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from functools import lru_cache
from pathlib import Path
from typing import Any, Mapping

import yaml

from .completeness.paths import at
from .relations import Edge, edges

Records = Mapping[str, Mapping[str, Any]]

#: The registry declaring the units that the export publishes.
EXPORT_REGISTRY = Path(__file__).parent / "data" / "registries" / "export.yml"

#: The command that generates an export, named in the export itself.
GENERATED_BY = "gnomon export"


@lru_cache(maxsize=2)
def load_export_registry(source: Path | None = None) -> Mapping[str, Any]:
    """Return the registry of the exported units."""
    loaded = yaml.safe_load((source or EXPORT_REGISTRY).read_text(encoding="utf-8")) or {}
    return loaded if isinstance(loaded, Mapping) else {}


def repository_identifier(directory: Path) -> str | None:
    """Return the identifier of the repository that holds a directory, read from ``repository.id``
    in the nearest ``repository.yml`` of the directory or of one of its parents."""
    for folder in (directory.resolve(), *directory.resolve().parents):
        manifest = folder / "repository.yml"
        if manifest.is_file():
            loaded = yaml.safe_load(manifest.read_text(encoding="utf-8")) or {}
            ident = at(loaded, "repository.id") if isinstance(loaded, Mapping) else None
            return str(ident) if ident else None
    return None


def _items(record: Mapping[str, Any], path: str) -> list[Mapping[str, Any]]:
    """Return the mappings of the list at a path of a record."""
    value = at(record, path)
    return (
        [item for item in value or [] if isinstance(item, Mapping)]
        if isinstance(value, list)
        else []
    )


def _superseded(records: Records) -> dict[str, list[str]]:
    """Return, for each answer that another answer revises, the answers that revise it."""
    found: dict[str, set[str]] = {}
    for ident, record in records.items():
        for edge in edges(record):
            if edge.relation == "revises":
                found.setdefault(edge.target, set()).add(ident)
    return {target: sorted(by) for target, by in found.items()}


def _unit(
    ident: str, record: str, unit: str, kind: str, source: Mapping[str, Any]
) -> dict[str, Any]:
    """Return one unit of the export, its identity followed by its source fields."""
    return {"id": ident, "record": record, "unit": unit, "kind": kind, **source}


def _record_units(
    ident: str, record: Mapping[str, Any], superseded: list[str]
) -> list[dict[str, Any]]:
    """Return the unit of a record of an exported kind, and the units of the declared lists of a
    record of any kind."""
    registry = load_export_registry()
    kind = str(record.get("type"))
    declared = (registry.get("records") or {}).get(kind)
    found = []
    if isinstance(declared, Mapping):
        own: dict[str, Any] = {
            "record_kind": kind,
            "statement": str(at(record, str(declared["statement"])) or ""),
            "status": str(record.get("status") or ""),
        }
        if kind == "question" and record.get("version") is not None:
            own["version"] = str(record["version"])
        own["superseded_by"] = superseded
        found.append(_unit(ident, ident, "", str(declared["kind"]), own))
    for spec in (registry.get("units") or {}).get(kind) or []:
        found += _list_units(ident, record, spec)
    return found


def _list_units(
    ident: str, record: Mapping[str, Any], spec: Mapping[str, Any]
) -> list[dict[str, Any]]:
    """Return the units of one declared list of a record, each named by the key of its item."""
    via = spec.get("via")
    lookup = {str(i.get("id")): i for i in _items(record, via["list"])} if via else {}
    found = []
    for item in _items(record, str(spec["list"])):
        name = item.get(spec["key"])
        if not name:
            continue
        source = lookup.get(str(item.get(via["key"]))) or {} if via else item
        inner = {
            "record_kind": str(record.get("type")),
            "statement": str(source.get(spec["statement"]) or ""),
            "status": "",
        }
        found.append(_unit(f"{ident}.{name}", ident, str(name), str(spec["kind"]), inner))
    return found


def export_units(records: Records) -> list[dict[str, Any]]:
    """Return the exported units of a set of records, sorted by identifier."""
    superseded = _superseded(records)
    units = [
        unit
        for ident in sorted(records)
        for unit in _record_units(ident, records[ident], superseded.get(ident, []))
    ]
    return sorted(units, key=lambda unit: str(unit["id"]))


def _holding_item(record: Mapping[str, Any], edge: Edge) -> Mapping[str, Any]:
    """Return the entry of an edge, or the item of a list that holds the field of the edge."""
    if edge.entry:
        return edge.entry
    node: Any = record
    for key in edge.where[:-1]:
        node = node[key] if isinstance(node, (Mapping, list)) else None
        if node is None:
            return {}
    return node if isinstance(node, Mapping) else {}


@dataclass
class ExportedRelations:
    """The relations of an export, and those dropped because an end is not exported."""

    relations: list[dict[str, Any]] = field(default_factory=list)
    dropped: list[str] = field(default_factory=list)


def _relation(edge: Edge, record: Mapping[str, Any]) -> dict[str, Any] | None:
    """Return the relation of the contract that an edge states, or None when it maps onto none."""
    declared = edge.declared
    mapping = declared.get("export")
    item = _holding_item(record, edge)
    use = str(item.get(declared["export_use"]) or "") if declared.get("export_use") else ""
    klass = mapping.get(use) if isinstance(mapping, Mapping) else mapping
    if not klass:
        return None
    row: dict[str, Any] = {"id": "", "class": str(klass)}
    if declared.get("export_form"):
        row["form"] = str(declared["export_form"])
    if edge.members:
        members = sorted({edge.holder, *edge.members})
        row["id"] = f"{edge.relation}:{','.join(members)}"
        row["members"] = members
    else:
        source, target = edge.holder, edge.target
        if declared.get("reversed"):
            source, target = target, source
        if declared.get("symmetric"):
            source, target = sorted((source, target))
        in_item = not edge.entry and any(isinstance(key, int) for key in edge.where)
        own = item.get("id") if in_item else None
        row["id"] = f"{edge.holder}.{own}" if own else f"{edge.relation}:{source}->{target}"
        row["source"], row["target"] = source, target
    if declared.get("symmetric") or declared.get("arity") == "set":
        row["symmetric"] = True
    row["relation"] = edge.relation
    if use:
        row["use"] = use
    return row


def _sort_key(row: Mapping[str, Any]) -> tuple[str, ...]:
    """Return the key that orders the relations: class, first end, second end, name, identifier."""
    first = row["members"][0] if "members" in row else row["source"]
    return (row["class"], first, str(row.get("target", "")), row["relation"], row["id"])


def export_relations(records: Records, units: set[str]) -> ExportedRelations:
    """Return the relations between exported units, each once, and the identifiers of the relations
    dropped because an end is not an exported unit."""
    rows: dict[str, dict[str, Any]] = {}
    dropped: set[str] = set()
    for ident in sorted(records):
        for edge in edges(records[ident]):
            row = _relation(edge, records[ident])
            if row is None:
                continue
            ends = row.get("members") or [row["source"], row["target"]]
            if all(end in units for end in ends):
                rows.setdefault(row["id"], row)
            else:
                dropped.add(row["id"])
    return ExportedRelations(sorted(rows.values(), key=_sort_key), sorted(dropped - set(rows)))


def build_export(
    records: Records, repository: str, findings_overridden: bool = False
) -> tuple[dict[str, Any], list[str]]:
    """Return the export of a set of records and the relations that it drops.

    >>> records = {"quest.a.q": {"id": "quest.a.q", "type": "question", "statement": "why?",
    ...                          "version": "1", "status": "posed"},
    ...            "ans.a.x": {"id": "ans.a.x", "type": "answer", "answers": "quest.a.q",
    ...                        "claim": {"reading": "because"}, "status": "accepted"}}
    >>> export, dropped = build_export(records, "demo")
    >>> [(r["class"], r["source"], r["target"]) for r in export["relations"]], dropped
    ([('solutionhood', 'quest.a.q', 'ans.a.x')], [])
    """
    units = export_units(records)
    related = export_relations(records, {str(unit["id"]) for unit in units})
    export = {
        "_schema": str(load_export_registry().get("contract")),
        "id": f"export.{repository}",
        "type": "export",
        "source": {"repository": repository, "tool": "gnomon"},
        "generated_by": GENERATED_BY,
        "findings_overridden": findings_overridden,
        "units": units,
        "relations": related.relations,
    }
    return export, related.dropped


def render_export(export: Mapping[str, Any]) -> str:
    """Return the text of an export file, as the command writes it."""
    return f"# Generated by `{GENERATED_BY}`. Edit the records, not this file.\n" + yaml.safe_dump(
        dict(export), sort_keys=False, allow_unicode=True, width=100
    )
