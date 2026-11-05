"""
The values that a started record still holds from its template.

A template writes a placeholder in each field, such as ``SYMBOL`` or ``"NAME OF THE LAW"``, and a
researcher replaces the placeholders of the fields that the inquiry fills and deletes the others.
A record whose identifier is filled is checked, so a placeholder left in it would otherwise be
read as content: a symbol declared twice, an expression outside the grammar, a route that the
question never named. Every command therefore reads a started record without its leftovers, and
the check reports each leftover once, with its repair.

A leftover is a string that some template writes as a placeholder, or a mapping, such as an entry
of a list, that equals the template at its place and still holds a placeholder: a block left as
the template wrote it. A placeholder is recognized by exact equality with a string of a template,
so a symbol in capitals, such as ``DGMT``, is never taken for one.

Functions
---------
placeholder_values
    Return the strings that the templates write as placeholders.
strip_leftovers
    Return a record without its leftovers, and one finding per leftover.
"""

from __future__ import annotations

import re
from functools import cache
from typing import Any, Mapping

import yaml

from . import findings as rules
from .findings import Entry, Finding, finding
from .schemas import TEMPLATES, record_kinds

#: An uppercase word, which marks a string of a template as a placeholder.
UPPERCASE_WORD = re.compile(r"[A-Z]{2,}")


def _leaves(node: Any) -> list[str]:
    """Return the string leaves of a parsed template, the keys of its mappings included, since a
    template may write a placeholder as a key, as ``FIELD.PATH`` in ``maturity``."""
    if isinstance(node, Mapping):
        keys = [key for key in node if isinstance(key, str)]
        return keys + [leaf for value in node.values() for leaf in _leaves(value)]
    if isinstance(node, list):
        return [leaf for value in node for leaf in _leaves(value)]
    return [node] if isinstance(node, str) else []


@cache
def _template(kind: str) -> Any:
    """Return the parsed template of a record kind."""
    return yaml.safe_load((TEMPLATES / f"{kind}.yml").read_text(encoding="utf-8"))


@cache
def placeholder_values() -> frozenset[str]:
    """Return the strings that the templates write as placeholders: those holding an uppercase
    word, as ``SYMBOL``, ``NAME OF THE LAW`` or ``quest.TOPIC.NAME``.

    >>> {"SYMBOL", "quest.TOPIC.NAME"} <= placeholder_values()
    True
    >>> "provisional" in placeholder_values()
    False
    """
    return frozenset(
        leaf
        for kind in record_kinds().values()
        for leaf in _leaves(_template(kind))
        if UPPERCASE_WORD.search(leaf)
    )


def _holds_placeholder(node: Any) -> bool:
    """Return whether a value holds a placeholder at any depth."""
    return any(leaf in placeholder_values() for leaf in _leaves(node))


def _label(path: tuple[Any, ...]) -> str:
    """Return the path of a value as the messages print it: keys joined by dots, entries indexed."""
    text = ""
    for part in path:
        if isinstance(part, Entry):
            text += f"[{part.index}]"
        elif isinstance(part, int):
            text += f"[{part}]"
        else:
            text += f".{part}" if text else str(part)
    return text


class _Stripper:
    """The walk of a record against its template, collecting the leftovers."""

    def __init__(self) -> None:
        self.found: list[Finding] = []

    def report(self, path: tuple[Any, ...], text: str, value: str) -> None:
        self.found.append(
            finding(
                rules.COMPLETENESS_TEMPLATE_LEFTOVER, f"{_label(path)}: {text}", *path, value=value
            )
        )

    def untouched(self, node: Any, template: Any) -> bool:
        """Return whether a mapping is a block of the template left as the template wrote it."""
        return isinstance(node, Mapping) and node == template and _holds_placeholder(node)

    def value(self, node: Any, template: Any, path: tuple[Any, ...]) -> Any:
        """Return a value without its leftovers, reporting each of them."""
        if isinstance(node, str) and node in placeholder_values():
            self.report(path, f"still holds the template value {node}; fill it or delete it", node)
            return None
        if isinstance(node, Mapping):
            given = template if isinstance(template, Mapping) else {}
            kept_items: dict[Any, Any] = {}
            for key, item in node.items():
                if isinstance(key, str) and key in placeholder_values():
                    self.report((*path, key), "is the template key; fill it or delete it", key)
                else:
                    kept_items[key] = self.value(item, given.get(key), (*path, key))
            return kept_items
        if isinstance(node, list):
            entry = template[0] if isinstance(template, list) and template else None
            kept: list[Any] = []
            for index, item in enumerate(node):
                place = (*path, Entry(index, item) if isinstance(item, Mapping) else index)
                if self.untouched(item, entry):
                    self.report(
                        place, "is the template entry left untouched; fill it or delete it", "entry"
                    )
                elif isinstance(item, str) and item in placeholder_values():
                    self.report(
                        place,
                        f"still holds the template value {item}; fill it or delete" " it",
                        item,
                    )
                else:
                    kept.append(self.value(item, entry, place))
            return kept
        return node


def strip_leftovers(record: Mapping[str, Any]) -> tuple[dict[str, Any], list[Finding]]:
    """Return a record without its leftovers, and one finding per leftover.

    A block of the template left untouched is removed whole and reported once; a placeholder left
    in a filled block becomes an empty value. A record of a kind without a template is returned as
    it stands.

    >>> record = {"type": "background", "id": "bg.a.b",
    ...           "laws": [{"name": "decay", "symbol": "SYMBOL"}]}
    >>> cleaned, found = strip_leftovers(record)
    >>> cleaned["laws"]
    [{'name': 'decay', 'symbol': None}]
    >>> print(found[0].text)
    laws[0].symbol: still holds the template value SYMBOL; fill it or delete it
    """
    kind = record_kinds().get(str(record.get("type")))
    if kind is None:
        return dict(record), []
    template = _template(kind)
    walk = _Stripper()
    cleaned: dict[str, Any] = {}
    for key, value in record.items():
        given = template.get(key) if isinstance(template, Mapping) else None
        if walk.untouched(value, given):
            walk.report(
                (key,), "is the template block left untouched; fill it or delete it", "block"
            )
            continue
        cleaned[key] = walk.value(value, given, (key,))
    return cleaned, walk.found
