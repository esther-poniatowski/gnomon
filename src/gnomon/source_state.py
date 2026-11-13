"""Deterministic identifiers of the authored records behind a generated view.

Functions
---------
source_state
    Return the SHA-256 identifier of a record mapping in canonical JSON form.
"""

from __future__ import annotations

import base64
import datetime
import hashlib
import json
import math
from collections.abc import Mapping
from typing import Any


def _sort_key(value: Any) -> str:
    """Return the stable ordering key of one canonical value."""
    return json.dumps(value, ensure_ascii=False, separators=(",", ":"))


# Each branch preserves one distinct runtime type produced by safe YAML loading.
# pylint: disable=too-many-return-statements,too-many-branches
def _canonical(value: Any) -> list[Any]:
    """Return a typed canonical representation of a value produced by safe YAML loading."""
    if value is None:
        return ["null"]
    if isinstance(value, bool):
        return ["bool", value]
    if isinstance(value, int):
        return ["int", str(value)]
    if isinstance(value, float):
        if math.isnan(value):
            encoded = "nan"
        elif math.isinf(value):
            encoded = "+inf" if value > 0 else "-inf"
        else:
            encoded = value.hex()
        return ["float", encoded]
    if isinstance(value, str):
        return ["str", value]
    if isinstance(value, bytes):
        return ["bytes", base64.b64encode(value).decode("ascii")]
    if isinstance(value, datetime.datetime):
        return ["datetime", value.isoformat()]
    if isinstance(value, datetime.date):
        return ["date", value.isoformat()]
    if isinstance(value, Mapping):
        pairs = [[_canonical(key), _canonical(item)] for key, item in value.items()]
        return [
            "mapping",
            sorted(pairs, key=lambda pair: (_sort_key(pair[0]), _sort_key(pair[1]))),
        ]
    if isinstance(value, list):
        return ["list", [_canonical(item) for item in value]]
    if isinstance(value, tuple):
        return ["tuple", [_canonical(item) for item in value]]
    if isinstance(value, (set, frozenset)):
        items = [_canonical(item) for item in value]
        return ["set", sorted(items, key=_sort_key)]
    raise TypeError(f"{type(value).__name__} is not a supported safe-YAML value")


# pylint: enable=too-many-return-statements,too-many-branches


def source_state(records: Mapping[str, Mapping[str, Any]]) -> str:
    """Return a deterministic identifier of the complete authored-record mapping.

    Each safe-YAML value receives a typed representation. Mapping keys and set entries are sorted,
    so filesystem order and YAML order do not affect the identifier. Types remain distinct: a
    parsed date differs from the same characters written as quoted text, and non-finite numbers,
    binary values and sets remain hashable while the contract checker reports them.

    Parameters
    ----------
    records : mapping
        Authored records keyed by their identifiers, after generated records and template
        leftovers have been removed.

    Returns
    -------
    str
        ``sha256:`` followed by the lowercase hexadecimal digest of the canonical mapping.

    Raises
    ------
    TypeError
        If a value does not belong to the data model produced by safe YAML loading.

    Examples
    --------
    >>> first = {"prob.a": {"status": "posed", "type": "problem"}}
    >>> second = {"prob.a": {"type": "problem", "status": "posed"}}
    >>> source_state(first) == source_state(second)
    True
    """
    canonical = json.dumps(
        _canonical(records),
        ensure_ascii=False,
        separators=(",", ":"),
    ).encode("utf-8")
    return f"sha256:{hashlib.sha256(canonical).hexdigest()}"
