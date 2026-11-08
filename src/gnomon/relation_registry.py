"""
The registry of relations between research units, read as data.

The registry declares the relations written as entries of a list of a record, whose tokens are the
closed values of that list, and the relations that a record states by a field of its own. This
module only reads the registry, so the readers of vocabularies can merge its tokens without
depending on the graph of relations, which :mod:`gnomon.relations` builds.

Functions
---------
load_relation_registry
    Return the registry of relations.
relation_vocabularies
    Return, per record kind, the tokens of each list of relations with their glosses.
"""

from __future__ import annotations

from functools import lru_cache
from pathlib import Path
from typing import Any, Mapping

import yaml

#: The registry declaring the relations between research units.
RELATION_REGISTRY = Path(__file__).parent / "data" / "registries" / "relations.yml"


@lru_cache(maxsize=4)
def _read(path: Path) -> Mapping[str, Any]:
    """Read a registry file once, and return its content as a mapping."""
    loaded = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    return loaded if isinstance(loaded, Mapping) else {}


def load_relation_registry(source: Path | None = None) -> Mapping[str, Any]:
    """Return the registry of relations."""
    return _read(source or RELATION_REGISTRY)


def relation_vocabularies(
    source: Path | None = None,
) -> dict[str, dict[str, list[tuple[str, str]]]]:
    """Return, per record kind, the tokens of each list of relations with their glosses, keyed by
    the name of the vocabulary that the base schema binds.

    >>> vocabularies = relation_vocabularies()
    >>> [token for token, _ in vocabularies["question"]["links.relation"]][:2]
    ['subquestion-of', 'explanans-from']
    """
    found: dict[str, dict[str, list[tuple[str, str]]]] = {}
    for kind, family in (load_relation_registry(source).get("entries") or {}).items():
        relations = family.get("relations") or {}
        found.setdefault(str(kind), {})[str(family.get("vocabulary"))] = [
            (str(token), str((declared or {}).get("name") or ""))
            for token, declared in relations.items()
        ]
    return found
