"""
The symbols that a record declares, the units that an identifier names, and the checks of the
references between records.
"""

from __future__ import annotations

import re
from dataclasses import dataclass
from typing import Any, Mapping

from .. import findings as rules
from ..findings import Finding, finding
from ..identifiers import RECORD_SEGMENTS, split_reference
from .layout import DECLARING, entries


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
    for entry in entries(record, "observables"):
        pointer = entry.get("reference")
        named = split_reference(pointer) if isinstance(pointer, str) else None
        if named is not None:
            source, symbol = named
            found.append(Declaration(symbol, "", "referenced", source))
    if record.get("type") == "question":
        contrast = (record.get("subject") or {}).get("contrast") or {}
        for foil in contrast.get("foil_set") or [] if isinstance(contrast, Mapping) else []:
            if isinstance(foil, Mapping) and isinstance(foil.get("symbol"), str):
                found.append(
                    Declaration(foil["symbol"], str(foil.get("name") or ""), "foil_set", identifier)
                )
    for entry in entries(record, "manifestations"):
        for feature in entries(entry, "features"):
            symbol = feature.get("symbol")
            if isinstance(symbol, str):
                found.append(
                    Declaration(
                        symbol,
                        str(feature.get("name") or ""),
                        "manifestations.features",
                        identifier,
                    )
                )
    return found


#: The blocks whose entries are units named by an `id` rather than by a symbol, per record type,
#: as the decision on dotted identifiers admits: a reference names such a unit by that `id`.
ID_UNITS: Mapping[str, tuple[str, ...]] = {
    "model": ("operations", "assumptions"),
    "answer": ("grounds", "abstractions"),
    "design": ("steps", "rules"),
    "derivation": ("objects", "posits", "moves", "interpretations", "segments", "consequences"),
    "binding": ("feature_pairs", "condition_pairs"),
}


def units(record: Mapping[str, Any]) -> list[str]:
    """Return the names by which a reference may reach a unit of the record: its symbols and the ids
    of its units.

    >>> units({"type": "model", "laws": [{"symbol": "onset"}],
    ...        "operations": [{"id": "drop-noise"}]})
    ['onset', 'drop-noise']
    """
    names = [entry.symbol for entry in declarations(record)]
    names += [
        str(entry["id"])
        for block in ID_UNITS.get(str(record.get("type", "")), ())
        for entry in entries(record, block)
        if entry.get("id")
    ]
    return names


#: A dotted token opening on the prefix of a record kind, wherever it stands in a string.
REFERENCE_TOKEN = re.compile(rf"(?<![\w.-])(?:{'|'.join(RECORD_SEGMENTS)})\.[\w.-]*\w")


def references(record: Mapping[str, Any]) -> list[tuple[tuple[str | int, ...], str]]:
    """Return every dotted reference that the record makes, with the path of the field holding it.

    The identifier of a record or of a unit is its declaration, not a reference, so the fields
    ``id`` are skipped.

    >>> references({"id": "ans.a.b", "route": {"runs_on": ["mod.a.m"]}})
    [(('route', 'runs_on', 0), 'mod.a.m')]
    """
    found: list[tuple[tuple[str | int, ...], str]] = []

    def walk(node: Any, path: tuple[str | int, ...]) -> None:
        if isinstance(node, Mapping):
            for key, value in node.items():
                if key != "id":
                    walk(value, (*path, str(key)))
        elif isinstance(node, list):
            for index, item in enumerate(node):
                walk(item, (*path, index))
        elif isinstance(node, str):
            found.extend((path, text) for text in REFERENCE_TOKEN.findall(node))

    walk(record, ())
    return found


def dangling_references(
    record: Mapping[str, Any], records: Mapping[str, Mapping[str, Any]]
) -> list[Finding]:
    """Return every reference to a record or to a unit that the records of the workspace do not
    declare.

    A reference has the segments that the prefix of its kind fixes, to reach a whole record, or one
    more, to reach a unit: a symbol, or the identifier of a unit such as an operation or a pair. A
    step of an itinerary is a unit that the itinerary check resolves, so it is left to that check,
    and a placeholder of a template, such as ``quest.TOPIC.NAME``, names no record yet.

    >>> records = {"mod.a.m": {"type": "model", "laws": [{"symbol": "onset"}]}}
    >>> [f.text for f in dangling_references({"record": "mod.a.m.onset", "other": "mod.a.x"},
    ...                                      records)]
    ['other: no record carries the identifier mod.a.x']
    """
    found = []
    for path, text in references(record):
        parts = text.split(".")
        count = RECORD_SEGMENTS[parts[0]]
        if any(part.isupper() for part in parts[1:count]):
            continue
        where = ".".join(str(segment) for segment in path)
        if len(parts) == count:
            if text not in records:
                found.append(
                    finding(
                        rules.VOCABULARY_UNKNOWN_RECORD,
                        f"{where}: no record carries the identifier {text}",
                        *path,
                        value=text,
                    )
                )
            continue
        split = split_reference(text)
        if split is None or parts[0] == "itin":
            continue
        owner, unit = split
        if owner not in records:
            found.append(
                finding(
                    rules.VOCABULARY_UNKNOWN_RECORD,
                    f"{where}: no record carries the identifier {owner}",
                    *path,
                    value=text,
                )
            )
        elif unit not in units(records[owner]):
            found.append(
                finding(
                    rules.VOCABULARY_UNKNOWN_UNIT,
                    f"{where}: {owner} declares no unit {unit}",
                    *path,
                    value=text,
                )
            )
    return found


def repeated_symbols(record: Mapping[str, Any]) -> list[Finding]:
    """Return every symbol that the record declares more than once.

    >>> record = {"type": "target-system", "variables": [{"symbol": "x"}],
    ...           "parameters": [{"symbol": "x"}]}
    >>> [f.text for f in repeated_symbols(record)]
    ['x: declared more than once']
    """
    seen = [entry.symbol for entry in declarations(record)]
    return [
        finding(
            rules.VOCABULARY_REPEATED_SYMBOL, f"{symbol}: declared more than once", value=symbol
        )
        for symbol in sorted({s for s in seen if seen.count(s) > 1})
    ]
