"""
Identifiers of records and of their units, in the dotted form that the decision on dotted
identifiers fixes.

A record identifier opens on a prefix that names its record type, and the prefix fixes how many
dot-separated segments the identifier holds. One further segment names a unit of the record: the
symbol of a declared element, or the identifier of a unit without a symbol, such as a step of an
itinerary. A resolver therefore splits a reference from its prefix alone.

See Also
--------
gnomon.vocabulary : the resolution of the symbols that a reference names.
"""

from __future__ import annotations

#: The number of segments of a record identifier, keyed by the prefix that names its record type.
RECORD_SEGMENTS: dict[str, int] = {
    "system": 2,
    "ops": 2,
    "vocab": 2,
    "prob": 3,
    "concept": 3,
    "design": 3,
    "derivation": 3,
    "quest": 3,
    "phen": 3,
    "bg": 3,
    "mod": 3,
    "bind": 3,
    "key": 3,
    "ans": 3,
    "assess": 3,
    "itin": 3,
}


def split_reference(text: str) -> tuple[str, str] | None:
    """Return the record identifier and the unit that a reference names, or None when it names none.

    >>> split_reference("phen.grokking.delay.tgen")
    ('phen.grokking.delay', 'tgen')
    >>> split_reference("system.turbulence.u")
    ('system.turbulence', 'u')
    >>> split_reference("phen.grokking.delay") is None
    True
    >>> split_reference("tgen") is None
    True
    """
    parts = text.split(".")
    count = RECORD_SEGMENTS.get(parts[0])
    if count is None or len(parts) != count + 1 or not all(parts):
        return None
    return ".".join(parts[:count]), parts[count]
