"""
Composition of the statement of a question from its fields.

The subject of a question fills a statement frame, whose interrogative the epistemic aim selects
and whose connective of contrast the locus of the foils selects, as the note on the subject of
inquiry states. A statement composed from the fields, read beside the statement authored, shows a
specification that the fields miss, or a remark of the authored statement that changes no answer.
The words of the frame are read from the registry of statements, so this module holds no wording.

A record named by a slot enters the statement by its title, whose first letter is lowered when the
rest of its first word is in lower case, since the titles of records are written in sentence case.
A slot left unfilled enters as its letter in brackets, such as ``[P]``, and a placeholder of a
question schema as its description in brackets, so that no slot is filled from outside the fields.

Classes
-------
Statement
    A composed statement, with the slots of the frame that the fields leave unfilled.

Functions
---------
load_statement_registry
    Return the registry of the words of the statement frame.
compose_statement
    Compose the statement of a question from its fields and from the records that they name.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Mapping, Sequence

import yaml

from .completeness import is_unfilled
from .identifiers import split_reference

#: The registry of the words of the statement frame, in the package data.
STATEMENT_REGISTRY = Path(__file__).parent / "data" / "registries" / "statements.yml"

Records = Mapping[str, Mapping[str, Any]]


@dataclass(frozen=True)
class Statement:
    """A statement composed from the fields of a question.

    Attributes
    ----------
    text : str
        The statement, with each unfilled slot written as its letter in brackets.
    gaps : tuple[str, ...]
        The slots of the frame that the fields leave unfilled, in the order of the frame.
    """

    text: str
    gaps: tuple[str, ...] = ()


def load_statement_registry(source: Path | None = None) -> dict[str, Any]:
    """Return the registry of the words of the statement frame."""
    return yaml.safe_load((source or STATEMENT_REGISTRY).read_text(encoding="utf-8")) or {}


def _sentence_case(title: str) -> str:
    """Lower the first letter of a title whose first word is otherwise in lower case.

    >>> [_sentence_case(t) for t in ("Delayed generalization", "NTK limit", "x")]
    ['delayed generalization', 'NTK limit', 'x']
    """
    word = title.split(" ", 1)[0]
    if len(word) > 1 and word[0].isupper() and word[1:] == word[1:].lower():
        return title[0].lower() + title[1:]
    return title


def _listed(items: Sequence[str], conjunction: str) -> str:
    """Join items as an enumeration in prose.

    >>> [_listed(x, "and") for x in (["a"], ["a", "b"], ["a", "b", "c"])]
    ['a', 'a and b', 'a, b and c']
    """
    if len(items) < 2:
        return "".join(items)
    return f"{', '.join(items[:-1])} {conjunction} {items[-1]}"


def _named(value: Any, records: Records) -> str | None:
    """Return the words of a slot that names a record, or None when the slot is unfilled."""
    if is_unfilled(value):
        return None
    if isinstance(value, Mapping):
        description = value.get("description")
        return f"[{description}]" if description else None
    record = records.get(str(value)) or {}
    title = record.get("title")
    return _sentence_case(str(title)) if title else str(value)


def _quantity(reference: str, records: Records) -> str:
    """Return the name that a record declares for the quantity of a reference, else its symbol."""
    split = split_reference(reference)
    if split is None:
        return reference
    holder, symbol = split
    for block in (records.get(holder) or {}).values():
        for entry in block if isinstance(block, list) else []:
            if isinstance(entry, Mapping) and entry.get("symbol") == symbol and entry.get("name"):
                return str(entry["name"])
    return symbol


def _restrictions(
    domain: Mapping[str, Any], records: Records, kinds: Mapping[str, str]
) -> list[str]:
    """Return the words of each restriction of a domain: its name, else the kind and the
    quantity."""
    words = []
    for entry in domain.get("restrictions") or []:
        if not isinstance(entry, Mapping) or is_unfilled(entry):
            continue
        if entry.get("name"):
            words.append(str(entry["name"]))
        elif entry.get("of"):
            phrase = kinds.get(str(entry.get("restriction") or "restricted"), "restricted {Q}")
            words.append(phrase.replace("{Q}", _quantity(str(entry["of"]), records)))
        elif entry.get("expression"):
            words.append(str(entry["expression"]))
    return words


@dataclass
class _Slots:
    """The slots of the frame that the fields leave unfilled, in the order of the frame."""

    gaps: list[str] = field(default_factory=list)

    def fill(self, letter: str, value: str | None) -> str:
        """Return the words of a slot, or its letter in brackets when it is unfilled."""
        if value is None:
            self.gaps.append(letter)
            return f"[{letter}]"
        return value


def _domain_clause(domain: Mapping[str, Any], records: Records, words: Mapping[str, Any]) -> str:
    """Return the clause of the restrictions and the limit of a domain, empty without them."""
    restrictions = _restrictions(domain, records, words.get("restriction_kinds") or {})
    limit = domain.get("limit")
    expression = limit.get("expression") if isinstance(limit, Mapping) else None
    clause = ""
    if restrictions:
        clause += " " + str(words.get("restrictions", "under {D}")).replace(
            "{D}", _listed(restrictions, "and")
        )
    if expression:
        clause += ", " + str(words.get("limit", "in the limit {L}")).replace("{L}", str(expression))
    return clause


def _interrogative_clause(
    question: Mapping[str, Any], records: Records, words: Mapping[str, Any], slots: _Slots
) -> str:
    """Return the interrogative that the aim selects, with the phenomenon or the explicandum."""
    subject, task = question.get("subject") or {}, question.get("task") or {}
    aim = task.get("epistemic_aim")
    interrogative = (words.get("interrogatives") or {}).get(aim)
    if interrogative is None:
        slots.gaps.append("aim")
        interrogative = "[interrogative] {P}"
    if aim == "explication":
        explicandum = task.get("explicandum")
        filled = None if is_unfilled(explicandum) else str(explicandum)
        return str(interrogative).replace("{E}", slots.fill("E", filled))
    return str(interrogative).replace(
        "{P}", slots.fill("P", _named(subject.get("phenomenon"), records))
    )


def _contrast_clause(contrast: Mapping[str, Any], words: Mapping[str, Any], slots: _Slots) -> str:
    """Return the connective that the locus selects, with the foils; empty for the locus `none`."""
    connective = (words.get("contrasts") or {}).get(contrast.get("locus"))
    if connective is None:
        return " rather than " + slots.fill("X", None)
    if not connective:
        return ""
    foils = [
        str(f["name"])
        for f in contrast.get("foil_set") or []
        if isinstance(f, Mapping) and f.get("name")
    ]
    foil_words = _listed(foils, "or") if foils else str(words.get("default_foils") or "")
    return " " + str(connective).replace("{X}", foil_words)


def compose_statement(
    question: Mapping[str, Any], records: Records, registry: Mapping[str, Any] | None = None
) -> Statement:
    """Compose the statement of a question from its fields and from the records that they name.

    >>> records = {"system.a": {"title": "Wide networks"}, "phen.a.b": {"title": "Lazy training"}}
    >>> question = {"subject": {"target_system": "system.a", "phenomenon": "phen.a.b",
    ...                         "contrast": {"locus": "other-outcome",
    ...                                      "foil_set": [{"name": "feature learning"}]},
    ...                         "domain": {"restrictions": [{"name": "fixed depth"}]}},
    ...             "task": {"epistemic_aim": "explanation"}}
    >>> compose_statement(question, records).text
    'In wide networks under fixed depth, what explains lazy training rather than feature learning?'
    >>> compose_statement({"task": {"epistemic_aim": "prediction"}}, {}).gaps
    ('S', 'P', 'X')
    """
    words = registry if registry is not None else load_statement_registry()
    subject = question.get("subject") or {}
    slots = _Slots()
    system = slots.fill("S", _named(subject.get("target_system"), records))
    text = str(words.get("system", "In {S}")).replace("{S}", system)
    text += _domain_clause(subject.get("domain") or {}, records, words)
    text += ", " + _interrogative_clause(question, records, words, slots)
    text += _contrast_clause(subject.get("contrast") or {}, words, slots)
    return Statement(text + "?", tuple(slots.gaps))
