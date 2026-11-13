"""Registration of an existing Gnomon record in its inquiry index.

The record supplies its published contract. The template index supplies the stage, link label and
purpose of the entry. Thus, callers can request registration without reproducing Gnomon's index
order or Markdown conventions.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Any

import yaml

from .scaffold import register_file
from .schemas import published_contracts, record_kinds


@dataclass(frozen=True)
class RegistrationPlan:
    """Index update bound to the record and index bytes observed during planning."""

    record: Path
    index: Path
    kind: str
    state: str
    text: str
    expected_record: bytes
    expected_index: bytes


def _mapping(content: bytes, path: Path) -> dict[str, Any]:
    """Parse one record mapping and give malformed input an actionable error."""
    try:
        value = yaml.safe_load(content.decode("utf-8"))
    except (UnicodeDecodeError, yaml.YAMLError) as error:
        raise ValueError(f"record is not valid UTF-8 YAML: {path}: {error}") from error
    if not isinstance(value, dict):
        raise ValueError(f"record must hold one YAML mapping: {path}")
    return value


def _record_kind(record: dict[str, Any]) -> str:
    """Return the template kind fixed by the record's published Gnomon contract."""
    binding = record.get("_schema")
    contract = published_contracts().get(str(binding))
    if contract is None:
        raise ValueError(f"record does not name a published Gnomon contract: {binding!r}")
    properties = contract.get("properties")
    type_schema = properties.get("type") if isinstance(properties, dict) else None
    record_type = type_schema.get("const") if isinstance(type_schema, dict) else None
    kind = record_kinds().get(str(record_type))
    if kind is None:
        raise ValueError(f"contract {binding!r} has no indexable Gnomon record kind")
    return kind


def plan_registration(record: Path, index: Path | None = None) -> RegistrationPlan:
    """Plan the registration of ``record`` in its sibling inquiry index.

    The record must be a direct child of the index folder. The index must already exist, because
    its prose and existing entries are authored state that this command preserves.
    """
    record = record.resolve()
    if record.suffix not in {".yml", ".yaml"} or not record.is_file():
        raise ValueError(f"record is not an existing .yml or .yaml file: {record}")
    index = (index or record.parent / "_index.md").resolve()
    if index.parent != record.parent:
        raise ValueError("record and inquiry index must be in the same folder")
    if not index.is_file():
        raise ValueError(f"inquiry index does not exist: {index}")

    record_bytes = record.read_bytes()
    index_bytes = index.read_bytes()
    kind = _record_kind(_mapping(record_bytes, record))
    try:
        current = index_bytes.decode("utf-8")
    except UnicodeDecodeError as error:
        raise ValueError(f"inquiry index is not valid UTF-8: {index}") from error
    updated = register_file(current, kind, record.name)
    state = "kept" if updated == current else "updated"
    return RegistrationPlan(
        record,
        index,
        kind,
        state,
        updated,
        record_bytes,
        index_bytes,
    )


def apply_registration(plan: RegistrationPlan) -> RegistrationPlan:
    """Apply a plan only while both observed inputs remain byte-for-byte current."""
    if plan.record.read_bytes() != plan.expected_record:
        raise ValueError(f"record changed after registration was planned: {plan.record}")
    if plan.index.read_bytes() != plan.expected_index:
        raise ValueError(f"inquiry index changed after registration was planned: {plan.index}")
    if plan.state == "updated":
        plan.index.write_text(plan.text, encoding="utf-8")
    return plan


def register_record(record: Path, index: Path | None = None) -> RegistrationPlan:
    """Register one existing record and return whether its inquiry index changed."""
    return apply_registration(plan_registration(record, index))
