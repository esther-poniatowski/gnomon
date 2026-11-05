"""
The form of record identifiers: the prefix of their type, the grammar of their segments, and the
topic that the records of one problem share.

A record identifier opens on the prefix of its type, followed by segments of lowercase words joined
by hyphens, as the decision on dotted identifiers states. Its first segment after the prefix is its
topic. A target system is named by its own topic, so a background or an operator record, which is
stated against one target system, takes the topic of that system. Every other record of a problem
takes the topic of the problem, so that the identifiers of one problem read as one family.

Functions
---------
malformed_identifier
    Return the finding of a record identifier that breaks the grammar of its type.
foreign_topics
    Return each record of a problem whose identifier carries another topic than it should.
"""

from __future__ import annotations

import re
from collections import Counter
from typing import Any, Mapping

from .. import findings as rules
from ..findings import Finding, finding
from ..identifiers import RECORD_SEGMENTS, identifier_pattern, topic

#: The field through which a record names the target system whose topic it takes.
TARGET_FIELD: Mapping[str, str] = {"background": "describes", "operators": "target_system"}


def malformed_identifier(record: Mapping[str, Any], prefixes: Mapping[str, str]) -> list[Finding]:
    """Return the finding of a record identifier that breaks the grammar of its type.

    >>> prefixes = {"question": "quest"}
    >>> malformed_identifier({"type": "question", "id": "quest.grokking.explain-delay"}, prefixes)
    []
    >>> [f.text for f in malformed_identifier({"type": "question", "id": "quest.a.b_c"}, prefixes)]
    ['id: quest.a.b_c is not quest followed by 2 segments of lowercase words joined by hyphens']
    >>> [f.text for f in malformed_identifier({"type": "question", "id": "phen.a.b"}, prefixes)]
    ['id: phen.a.b does not open on the prefix quest of the type question']
    """
    kind, identifier = record.get("type"), record.get("id")
    prefix = prefixes.get(str(kind))
    if prefix is None or prefix not in RECORD_SEGMENTS or not isinstance(identifier, str):
        return []
    if re.fullmatch(identifier_pattern(prefix), identifier):
        return []
    if identifier.split(".", 1)[0] != prefix:
        text = f"id: {identifier} does not open on the prefix {prefix} of the type {kind}"
    else:
        count = RECORD_SEGMENTS[prefix] - 1
        text = (
            f"id: {identifier} is not {prefix} followed by {count} segment"
            f"{'s' if count > 1 else ''} of lowercase words joined by hyphens"
        )
    return [finding(rules.VOCABULARY_MALFORMED_IDENTIFIER, text, "id", value=identifier)]


def _problem_topic(records: Mapping[str, Mapping[str, Any]]) -> str | None:
    """Return the topic of a problem: that of its problem record, else the topic that most of its
    records share, the first in alphabetical order on a tie."""
    for record in records.values():
        if record.get("type") == "problem" and (found := topic(str(record.get("id", "")))):
            return found
    counted = Counter(
        found
        for record in records.values()
        if record.get("type") not in ("target-system", *TARGET_FIELD)
        and (found := topic(str(record.get("id", ""))))
    )
    if not counted:
        return None
    most = max(counted.values())
    return min(name for name, count in counted.items() if count == most)


def foreign_topics(records: Mapping[str, Mapping[str, Any]]) -> list[tuple[str, Finding]]:
    """Return each record of a problem whose identifier carries another topic than it should.

    A background or an operator record takes the topic of the target system that it names; a
    target system keeps its own; every other record takes the topic of the problem.

    >>> records = {
    ...     "system.nets": {"type": "target-system", "id": "system.nets"},
    ...     "bg.nets.law": {"type": "background", "id": "bg.nets.law", "describes": "system.nets"},
    ...     "ops.other": {"type": "operators", "id": "ops.other", "target_system": "system.nets"},
    ...     "quest.delay.why": {"type": "question", "id": "quest.delay.why"},
    ...     "phen.delays.run": {"type": "phenomenon", "id": "phen.delays.run"},
    ...     "prob.delay.what": {"type": "problem", "id": "prob.delay.what"}}
    >>> [(i, f.text) for i, f in foreign_topics(records)]  # doctest: +NORMALIZE_WHITESPACE
    [('ops.other', 'id: the topic other differs from the topic nets of the target system
      system.nets'), ('phen.delays.run', 'id: the topic delays differs from the topic delay of
      the problem')]
    """
    expected = _problem_topic(records)
    found: list[tuple[str, Finding]] = []
    for ident in sorted(records):
        record = records[ident]
        kind = str(record.get("type"))
        own = topic(ident)
        if own is None or kind == "target-system":
            continue
        if kind in TARGET_FIELD:
            target = record.get(TARGET_FIELD[kind])
            wanted = topic(target) if isinstance(target, str) else None
            where = f"the target system {target}"
        else:
            wanted, where = expected, "the problem"
        if wanted is not None and own != wanted:
            text = f"id: the topic {own} differs from the topic {wanted} of {where}"
            found.append((ident, finding(rules.VOCABULARY_FOREIGN_TOPIC, text, "id", value=own)))
    return found
