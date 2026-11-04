"""
The paths of the registries, the reading of a record by the path of a field, and the test that
tells an empty field from a filled one.

An empty value means that a field is not filled. Whether an empty field is a gap or a value that
the inquiry will produce is read from the requirement registry, never from the record.
"""

from __future__ import annotations

from pathlib import Path
from typing import Any, Mapping

from ..findings import Segment

DATA = Path(__file__).resolve().parent.parent / "data"


#: The registry declaring what a filled inquiry must carry.
REQUIREMENT_REGISTRY = DATA / "requirements.yml"


#: The registry declaring the values each closed field admits.
VOCABULARY_REGISTRY = DATA / "vocabularies.yml"


def is_empty(value: Any) -> bool:
    """Return whether ``value`` leaves its field unfilled: absent, null, or an empty string.

    An empty list or mapping is a value: it states that the block holds no entry.

    >>> [is_empty(v) for v in (None, "", "  ", [], "open")]
    [True, True, True, False, False]
    """
    return value is None or (isinstance(value, str) and not value.strip())


def is_unfilled(value: Any) -> bool:
    """Return whether a required specification is unfilled.

    A value is unfilled when it is empty, and a list or a mapping when every value that it holds is
    unfilled, so that a required block whose fields are all empty fails its requirement as a missing
    block does.

    >>> [is_unfilled(v) for v in (None, [], {}, {"a": None, "b": [""]}, [{"a": ""}], {"a": "x"}, 0)]
    [True, True, True, True, True, False, False]
    """
    if isinstance(value, Mapping):
        return all(is_unfilled(item) for item in value.values())
    if isinstance(value, list):
        return all(is_unfilled(item) for item in value)
    return is_empty(value)


def at(record: Mapping[str, Any], path: str) -> Any:
    """Return the value a dotted path names, or None when the path does not resolve.

    A step written ``key[]`` traverses the list it names and collects what the rest of the path
    reaches in each entry, so one path states a requirement bearing on every entry of a block.

    >>> at({"virtues": [{"virtue": "generality"}, {"virtue": "economy"}]}, "virtues[].virtue")
    ['generality', 'economy']
    """
    head, marker, tail = path.partition("[].")
    node: Any = record
    for key in head.split("."):
        if not isinstance(node, Mapping):
            return None
        node = node.get(key)
    if not marker:
        return node
    if not isinstance(node, list):
        return None
    return [at(entry, tail) for entry in node if isinstance(entry, Mapping)]


def path_segments(path: str) -> tuple[tuple[Segment, ...], str | None]:
    """Return the keys of a dotted path up to its first traversed list, and the rest of the path.

    A path written ``key[]`` names a field of every entry of a list, so its locus is the list and
    the field it names inside each entry is returned apart, or None when the path traverses none.

    >>> path_segments("task.required_accuracy")
    (('task', 'required_accuracy'), None)
    >>> path_segments("factors[].target_status")
    (('factors',), 'target_status')
    """
    head, marker, tail = path.partition("[].")
    return tuple(head.split(".")), (tail if marker else None)
