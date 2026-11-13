"""Coverage of a generated view selected for one completion target."""

from __future__ import annotations

from collections.abc import Mapping, Sequence
from typing import TypedDict

from .scope_classification import FutureWork


class AuthoredRecord(TypedDict):
    """One started authored record read while generating a view."""

    record: str
    kind: str


class LaterRecordKind(TypedDict):
    """One absent record kind required after the selected completion target."""

    due_scope: str
    kind: str
    expected_file: str


class ViewCoverage(TypedDict):
    """The present inputs and later record kinds of a selected view."""

    scope: str
    authored_records: list[AuthoredRecord]
    later_record_kinds: list[LaterRecordKind]


def attach_view_coverage(view: Mapping[str, object], coverage: ViewCoverage) -> dict[str, object]:
    """Insert ``coverage`` after the shared view header."""
    selected: dict[str, object] = {}
    for key, value in view.items():
        selected[key] = value
        if key == "source_state":
            selected["coverage"] = coverage
    if "coverage" not in selected:
        raise ValueError("a generated view must carry source_state before coverage")
    return selected


def view_coverage(
    scope: str,
    records: Mapping[str, Mapping[str, object]],
    future_work: Sequence[FutureWork],
) -> ViewCoverage:
    """Return the authored records read now and absent record kinds due later."""
    authored_records: list[AuthoredRecord] = [
        {"record": identifier, "kind": str(record.get("type") or "")}
        for identifier, record in sorted(records.items())
    ]
    seen: set[tuple[str, str, str]] = set()
    later_record_kinds: list[LaterRecordKind] = []
    for item in future_work:
        identity = (item.due_scope, item.kind, item.file.as_posix())
        if item.record is not None or identity in seen:
            continue
        seen.add(identity)
        later_record_kinds.append(
            {
                "due_scope": item.due_scope,
                "kind": item.kind,
                "expected_file": item.file.as_posix(),
            }
        )
    return {
        "scope": scope,
        "authored_records": authored_records,
        "later_record_kinds": later_record_kinds,
    }
