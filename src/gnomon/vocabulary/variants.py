"""
The variants of a target system, and the checks of the entries that reach beyond the members
that bear them.
"""

from __future__ import annotations

from typing import Any, Iterable, Mapping

from .. import findings as rules
from ..findings import Entry, Finding, Place, finding
from .layout import DECLARING, at_item, entries, identifiers, indexed, items_of


def declared_variants(record: Mapping[str, Any]) -> frozenset[str]:
    """Return the shapes a member of the reference class may take, which only a target declares."""
    return frozenset(
        entry["symbol"]
        for entry in entries(record, "variants")
        if isinstance(entry.get("symbol"), str)
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


def _entry_overreach(
    block: str,
    position: int,
    entry: Mapping[str, Any],
    keys: tuple[str, ...],
    variants: Mapping[str, str],
) -> list[Finding]:
    """Return a finding per symbol of one variant that an unmarked entry names under ``keys``."""
    label = f"{block}.{entry.get('name') or entry.get('symbol')}"
    return [
        finding(
            rules.VOCABULARY_OVERREACHING_ENTRY,
            f"{label}: {name} is carried only by the {variants[name]} variant",
            *at_item((block, Entry(position, entry), key), index),
            value=name,
        )
        for key in keys
        for index, text in items_of(entry.get(key))
        if isinstance(text, str)
        for name in sorted(identifiers(text))
        if name in variants
    ]


def overreaching_declarations(
    record: Mapping[str, Any], upstream: Mapping[str, Any] | None = None
) -> list[Finding]:
    """Return every entry of the target asserting of all members what only some of them can bear.

    An entry left unmarked asserts something of every member of the reference class. When it names
    a symbol that only one variant declares, it is not false of the other members but unreadable
    for them: the quantity it governs does not exist there. A law names its quantities in its
    expression, a relation of the organization names the parts it runs between and the laws that
    realize it, and an external system names what it shares, so each reaches the class the same
    way. A background record states laws over the quantities of its target, so the variants of
    that target, passed as ``upstream``, mark the symbols its entries may name.
    """
    variants = {**variant_symbols(upstream or {}), **variant_symbols(record)}
    found: list[Finding] = []
    for block, keys in (
        ("laws", ("expression",)),
        ("organization", ("relates", "among", "realized_by")),
        ("external_systems", ("shares",)),
    ):
        for position, entry in indexed(record, block):
            if not entry.get("variant"):
                found += _entry_overreach(block, position, entry, keys, variants)
    return found


#: Fields of an entry holding an expression or a reference, so a symbol in them is load-bearing.
FORMAL_KEYS: frozenset[str] = frozenset(
    {
        "expression",
        "condition",
        "values",
        "extent",
        "signature",
        "observed",
        "effect",
        "over",
        "across",
        "conditional_on",
        "selects_on",
        "origin",
        "horizon",
        "influence",
        "constrains",
        "shares",
        "relates",
        "among",
    }
)


def unborne_variants(
    record: Mapping[str, Any], carriers: Iterable[Mapping[str, Any]] = ()
) -> list[Finding]:
    """Return every variant the record declares and no declaration or law carries.

    A variant is one shape a member may take, written as a partition of the record's own
    declarations, so one that nothing carries names an alternative the record cannot generate:
    the other members stay describable and this one has no schema at all. A record may admit the
    gap by marking the variant open in its maturity, which is what turns that marker from an
    assertion nothing reads into a licence the check consults.

    The count is structural rather than lexical. The name of a variant recurs in its own prose
    and in the marker admitting it, so counting occurrences would find an empty variant reached.
    The laws and relations that carry a variant stand in the background records describing the
    target, passed as ``carriers``, so their marks count as the marks of the target do.
    """
    borne: dict[str, int] = {}
    for source in (record, *carriers):
        for block in DECLARING.get(str(source.get("type", "")), ()):
            for entry in entries(source, block):
                carried = entry.get("variant")
                if isinstance(carried, str):
                    borne[carried] = borne.get(carried, 0) + 1
    admitted = record.get("maturity") or {}
    found = []
    for index, variant in indexed(record, "variants"):
        symbol = str(variant.get("symbol"))
        if borne.get(symbol) or admitted.get(f"variants.{symbol}") == "open":
            continue
        found.append(
            finding(
                rules.VOCABULARY_UNBORNE_VARIANT,
                f"variants.{symbol}: no declaration or law carries it, and its maturity admits no"
                " gap",
                "variants",
                Entry(index, variant),
            )
        )
    return found


def misnamed_variant(record: Mapping[str, Any], variants: Iterable[str]) -> list[Finding]:
    """Return every variant the record names that the target does not declare.

    A variant is not one symbol among the others: an entry marked by a symbol that names no
    variant claims to hold of a part of the class that does not exist, and an unmarked entry
    claims to hold of all of it, so the mark is read as true wherever it is read at all. The walk
    reaches every position a mark may take, since a block gaining one is not to gain a hole. The
    message names the keys above the mark; the finding lies at the full path of the mark.
    """
    declared = set(variants)

    def walk(node: Any, where: str, place: Place) -> list[Finding]:
        if isinstance(node, Mapping):
            found = (
                [
                    finding(
                        rules.VOCABULARY_MISNAMED_VARIANT,
                        f"{where}variant -> {node['variant']}",
                        *place,
                        "variant",
                    )
                ]
                if isinstance(node.get("variant"), str) and node["variant"] not in declared
                else []
            )
            for key, value in node.items():
                found += walk(value, f"{where}{key}.", (*place, key))
            return found
        if isinstance(node, list):
            return [
                p
                for index, item in enumerate(node)
                for p in walk(item, where, (*place, Entry(index, item)))
            ]
        return []

    return walk(record, "", ())


def overreaching_entries(record: Mapping[str, Any], marked: Mapping[str, str]) -> list[Finding]:
    """Return every entry asserting of all members what only some of them can bear.

    ``marked`` maps each symbol that only some members carry to the variant carrying it, as the
    target system states it. Neither a phenomenon nor an answer declares a variant of its own, so
    the fact reaches them from the record they are about: an entry naming such a symbol holds of
    that variant and says so, or it ranges over members for which its claim cannot be read at all.

    An answer may name the variant it accounts for once, on the record, and every entry of it
    inherits that; a part of it narrower still names its own.
    """
    found: list[Finding] = []
    default = record.get("variant")

    def scan(where: str, place: Place, entry: Mapping[str, Any]) -> None:
        variant = entry.get("variant") or default
        for key, value in entry.items():
            if key not in FORMAL_KEYS:
                continue
            for index, text in items_of(value):
                if not isinstance(text, str):
                    continue
                for symbol in sorted(identifiers(text)):
                    if symbol in marked and variant != marked[symbol]:
                        found.append(
                            finding(
                                rules.VOCABULARY_OVERREACHING_ENTRY,
                                f"{where}.{entry.get('name') or entry.get('symbol')}: {symbol} is"
                                f" carried only by the {marked[symbol]} variant",
                                *at_item((*place, key), index),
                                value=symbol,
                            )
                        )

    for block in (
        "observables",
        "manifestations",
        "scope_over_instances",
        "detection_criterion",
        "constituents",
        "index_sets",
        "variables",
        "parameters",
        "laws",
        "organization",
    ):
        for index, entry in indexed(record, block):
            scan(block, (block, Entry(index, entry)), entry)
    holder = record.get("conditions_and_byproducts")
    if isinstance(holder, Mapping):
        for kind in ("precipitating", "inhibiting", "modulating", "nonstandard", "byproducts"):
            for index, entry in indexed(holder, kind):
                scan(
                    f"conditions_and_byproducts.{kind}",
                    ("conditions_and_byproducts", kind, Entry(index, entry)),
                    entry,
                )
    return found
