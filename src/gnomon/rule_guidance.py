"""Load the canonical repair guidance of the published finding rules."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path, PurePosixPath
from typing import Any, Iterable, Mapping

import yaml

RULE_GUIDANCE_PATH = Path(__file__).parent / "data" / "rule-guidance.yml"
"""The package-data registry that supplies guidance to the finding catalogue."""

_FIELDS = frozenset({"repair_condition", "documentation_target"})


@dataclass(frozen=True)
class RuleGuidance:
    """The state that repairs one rule and the documentation that owns that state."""

    repair_condition: str
    documentation_target: str


def _text(entry: Mapping[str, Any], field: str, identifier: str) -> str:
    """Return one required, non-empty text field of a guidance entry."""
    value = entry.get(field)
    if not isinstance(value, str) or not value.strip():
        raise ValueError(f"rule guidance {identifier!r} has no non-empty {field}")
    return value.strip()


def _target(value: str, identifier: str) -> str:
    """Return a repository-relative Markdown target, optionally followed by a fragment."""
    path_text, _, _fragment = value.partition("#")
    path = PurePosixPath(path_text)
    if path.is_absolute() or ".." in path.parts or path.suffix != ".md":
        raise ValueError(f"rule guidance {identifier!r} has no repository-relative Markdown target")
    return value


def load_rule_guidance(source: Path = RULE_GUIDANCE_PATH) -> dict[str, RuleGuidance]:
    """Return the validated repair guidance, keyed by finding-rule identifier."""
    document = yaml.safe_load(source.read_text(encoding="utf-8")) or {}
    if not isinstance(document, Mapping) or set(document) != {"rules"}:
        raise ValueError("rule guidance must contain exactly one mapping named 'rules'")
    entries = document["rules"]
    if not isinstance(entries, Mapping):
        raise ValueError("the 'rules' value of rule guidance must be a mapping")

    found: dict[str, RuleGuidance] = {}
    for identifier, raw_entry in entries.items():
        if not isinstance(identifier, str) or not isinstance(raw_entry, Mapping):
            raise ValueError("each rule-guidance entry must map an identifier to fields")
        if set(raw_entry) != _FIELDS:
            raise ValueError(f"rule guidance {identifier!r} must contain exactly {sorted(_FIELDS)}")
        repair = _text(raw_entry, "repair_condition", identifier)
        target = _target(_text(raw_entry, "documentation_target", identifier), identifier)
        found[identifier] = RuleGuidance(repair, target)
    return found


def validate_guidance_coverage(
    identifiers: Iterable[str], guidance: Mapping[str, RuleGuidance]
) -> None:
    """Require the guidance keys to equal the published rule identifiers."""
    expected = set(identifiers)
    actual = set(guidance)
    missing = sorted(expected - actual)
    unknown = sorted(actual - expected)
    if missing or unknown:
        raise ValueError(f"rule-guidance coverage differs: missing={missing}, unknown={unknown}")
