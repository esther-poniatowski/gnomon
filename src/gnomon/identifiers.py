"""
Identifiers of records and of their units, in the dotted form that the decision on dotted
identifiers fixes.

A record identifier opens on a prefix that names its record type, and the prefix fixes how many
dot-separated segments the identifier holds. Each segment after the prefix is written in lowercase
letters and digits, its words joined by hyphens, and the first of them is the topic of the record.
One further segment names a unit of the record: the symbol of a declared element, or the identifier
of a unit without a symbol, such as a step of an itinerary. A resolver therefore splits a reference
from its prefix alone.

See Also
--------
gnomon.vocabulary : the resolution of the symbols that a reference names.
"""

from __future__ import annotations

import re

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


#: One segment of a record identifier after its prefix: lowercase words of letters and digits,
#: joined by hyphens.
SEGMENT = r"[a-z][a-z0-9]*(?:-[a-z0-9]+)*"

#: A segment still holding the placeholder of a template, such as ``TOPIC`` in ``quest.TOPIC.NAME``.
PLACEHOLDER_SEGMENT = re.compile(r"(?:^|\.)[A-Z][A-Z0-9_]*(?:\.|$)")


def identifier_pattern(prefix: str) -> str:
    """Return the pattern of a record identifier that opens on ``prefix``.

    >>> bool(re.fullmatch(identifier_pattern("quest"), "quest.grokking.explain-delay"))
    True
    >>> bool(re.fullmatch(identifier_pattern("quest"), "quest.grokking.explain_delay"))
    False
    """
    return f"^{re.escape(prefix)}" + rf"\.{SEGMENT}" * (RECORD_SEGMENTS[prefix] - 1) + "$"


def topic(identifier: str) -> str | None:
    """Return the topic of a record identifier: its segment after the prefix, or None.

    >>> topic("bg.delayed-generalization-networks.training-specification")
    'delayed-generalization-networks'
    """
    parts = identifier.split(".")
    return parts[1] if len(parts) > 1 and parts[0] in RECORD_SEGMENTS and parts[1] else None


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
