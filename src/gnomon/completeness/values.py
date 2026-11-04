"""
The closed vocabularies of the record kinds, read from the vocabulary registry, and the check of
the values that a closed field admits.
"""

from __future__ import annotations

from pathlib import Path
from typing import Any, Mapping

import yaml

from .. import findings as rules
from ..findings import Entry, Finding, Place, finding
from ..schemas import kinds, load_base, vocabulary_paths
from .paths import VOCABULARY_REGISTRY


def placeholder_types(source: Path | None = None) -> frozenset[str]:
    """Return the types a placeholder of a question slot may take, as the vocabulary lists them."""
    return vocabularies("question", source).get("subject.placeholder", frozenset())


def result_aims(source: Path | None = None) -> dict[str, frozenset[str]]:
    """Return, per type of result of a problem, the aims of the questions that may serve it."""
    registry = yaml.safe_load((source or VOCABULARY_REGISTRY).read_text(encoding="utf-8")) or {}
    types = ((registry.get("vocabularies") or {}).get("problem") or {}).get(".result_type") or []
    return {str(entry["value"]): frozenset(entry.get("admits") or []) for entry in types}


def vocabularies(kind: str, source: Path | None = None) -> dict[str, frozenset[str]]:
    """Return, per vocabulary of ``kind`` in the registry, the values it admits, keyed as the
    registry keys it."""
    registry = yaml.safe_load((source or VOCABULARY_REGISTRY).read_text(encoding="utf-8")) or {}
    fields = (registry.get("vocabularies") or {}).get(kind) or {}
    return {name: frozenset(entry["value"] for entry in values) for name, values in fields.items()}


def admitted_values(kind: str, source: Path | None = None) -> dict[str, frozenset[str]]:
    """Return, per closed field of ``kind``, the values it admits, keyed by the path of the field.

    The base schema of the record type binds each closed field to its vocabulary, so the path of
    a field selects its vocabulary, never the name of the vocabulary: in an answer, the field
    ``aim_block.explanation.factors.factor`` takes the kinds of a factor, whereas
    ``aim_block.exploration.space.varied.factor``, which holds a symbol, takes none. A record type
    without a base schema reads each vocabulary of the record level as the field of its name. An
    empty field holds no value, so no vocabulary bears on it.
    """
    values = vocabularies(kind, source)
    if kind in kinds():
        return {
            path: values[key]
            for path, key in vocabulary_paths(load_base(kind)).items()
            if key in values
        }
    return {key[1:]: admitted for key, admitted in values.items() if key.startswith(".")}


def inadmissible_values(
    record: Mapping[str, Any], admitted: Mapping[str, frozenset[str]]
) -> list[Finding]:
    """Return every closed field of the record holding a value its vocabulary does not admit.

    ``admitted`` is keyed by the path of each closed field, an entry of a list adding no segment,
    as :func:`admitted_values` returns it. The message names that path; the finding lies at the
    full path of the field, and at the item of a field holding a list.
    """
    found: list[Finding] = []

    def report(label: str, key: str, value: Any, vocabulary: frozenset[str], where: Place) -> None:
        items = list(enumerate(value)) if isinstance(value, list) else [(None, value)]
        for index, item in items:
            if isinstance(item, str) and item not in vocabulary:
                place = (*where, key) if index is None else (*where, key, index)
                found.append(
                    finding(
                        rules.COMPLETENESS_INADMISSIBLE_VALUE,
                        f"{label}: {item} is not admitted",
                        *place,
                    )
                )

    def visit(node: Any, path: tuple[str, ...], where: Place) -> None:
        if isinstance(node, Mapping):
            for key, value in node.items():
                field_path = ".".join((*path, str(key)))
                vocabulary = admitted.get(field_path)
                if vocabulary is not None:
                    report(field_path, str(key), value, vocabulary, where)
                if isinstance(value, (Mapping, list)):
                    visit(value, (*path, str(key)), (*where, key))
        elif isinstance(node, list):
            for index, item in enumerate(node):
                visit(item, path, (*where, Entry(index, item)))

    visit(record, (), ())
    return found
