"""
The requirements that a record carries, read from the requirement registry, and the checks of
the specifications that a record leaves unfilled.

The registry lists the general requirements of each record kind, those of a level of commitment,
those of a value of a closed field, those of the presence of a field, and those of an epistemic
aim, with the paths that the inquiry produces and may therefore leave empty.
"""

from __future__ import annotations

from pathlib import Path
from typing import Any, Mapping

import yaml

from .. import findings as rules
from ..findings import Entry, Finding, Rule, finding
from .paths import REQUIREMENT_REGISTRY, at, is_unfilled, path_segments

#: The levels of commitment of a target system or a phenomenon, weakest first.
COMMITMENT_LEVELS: tuple[str, ...] = ("identified", "specified")


def read_requirements(source: Path | None) -> dict[str, Any]:
    return yaml.safe_load((source or REQUIREMENT_REGISTRY).read_text(encoding="utf-8")) or {}


def requirements_by_aim(source: Path | None = None) -> dict[str, dict[str, list[str]]]:
    """Return, per epistemic aim, the paths its inquiry fixes and the ones it produces.

    Raises
    ------
    ValueError
        If the registry declares no aim.
    """
    by_aim = read_requirements(source).get("by_aim") or {}
    if not by_aim:
        raise ValueError(f"{(source or REQUIREMENT_REGISTRY).name} declares no aim")
    return {
        aim: {
            "required": [e["path"] for e in (entry.get("required") or [])],
            "to_produce": list(entry.get("to_produce") or []),
        }
        for aim, entry in by_aim.items()
    }


def always_required(kind: str, source: Path | None = None) -> list[str]:
    """Return the specifications every record of ``kind`` carries, whatever the inquiry."""
    return list((read_requirements(source).get("always") or {}).get(kind) or [])


def block_requirements(source: Path | None = None) -> dict[str, list[str]]:
    """Return, per path of an aim block of an answer, the specifications that the block carries,
    relative to it."""
    return {
        str(block): list(paths or [])
        for block, paths in (read_requirements(source).get("by_block") or {}).items()
    }


def record_kinds(source: Path | None = None) -> list[str]:
    """Return every record kind the registry states a general requirement for."""
    return sorted(read_requirements(source).get("always") or {})


def requirements_by_commitment(source: Path | None = None) -> dict[str, dict[str, list[str]]]:
    """Return, per level of commitment, the specifications each record kind carries at that level.

    Raises
    ------
    ValueError
        If the registry names a level outside :data:`COMMITMENT_LEVELS`.
    """
    table = read_requirements(source).get("by_commitment") or {}
    unknown = set(table) - set(COMMITMENT_LEVELS)
    if unknown:
        raise ValueError(f"unknown levels of commitment: {sorted(unknown)}")
    return {
        level: {kind: list(paths or []) for kind, paths in (table.get(level) or {}).items()}
        for level in COMMITMENT_LEVELS
    }


def commitment_requirements(
    kind: str, level: str, table: Mapping[str, Mapping[str, list[str]]]
) -> list[str]:
    """Return what a record of ``kind`` carries at ``level``, the weaker levels included.

    >>> table = {"identified": {"phenomenon": ["statement"]},
    ...          "specified": {"phenomenon": ["course"]}}
    >>> commitment_requirements("phenomenon", "specified", table)
    ['statement', 'course']
    """
    if level not in COMMITMENT_LEVELS:
        return []
    paths: list[str] = []
    for weaker in COMMITMENT_LEVELS[: COMMITMENT_LEVELS.index(level) + 1]:
        paths += list((table.get(weaker) or {}).get(kind) or [])
    return paths


def unmet_general(
    record: Mapping[str, Any],
    paths: list[str],
    produced: frozenset[str] | set[str] = frozenset(),
    label: str = "always required",
    rule: Rule = rules.COMPLETENESS_UNMET_REQUIREMENT,
) -> list[Finding]:
    """Return every required specification the record leaves unfilled.

    A specification is unfilled when it is absent, null, an empty string, or an empty list or
    mapping. A path written ``key[].field`` bears on every entry of the list, so each entry leaving
    the field unfilled is reported, and a list with no entry imposes nothing. The aim of the inquiry
    may produce a required specification, so the caller passes the paths that aim produces: those
    may stay unfilled, since the inquiry supplies their values. Each finding of ``rule`` lies at the
    unfilled path.

    >>> record = {"moves": [{"id": "a", "kind": "solve"}, {"id": "b"}]}
    >>> [f.text for f in unmet_general(record, ["moves[].kind"])]
    ['always required: moves[].kind']
    >>> unmet_general({"moves": []}, ["moves[].kind"])
    []
    """
    found = []
    for path in paths:
        if path in produced:
            continue
        keys, field = path_segments(path)
        if field is None:
            if is_unfilled(at(record, path)):
                found.append(finding(rule, f"{label}: {path}", *keys))
            continue
        entries = at(record, ".".join(str(k) for k in keys))
        for i, entry in enumerate(entries if isinstance(entries, list) else []):
            if isinstance(entry, Mapping) and is_unfilled(at(entry, field)):
                found.append(
                    finding(rule, f"{label}: {path}", *keys, Entry(i, entry), *field.split("."))
                )
    return found


def unmet_commitment(
    record: Mapping[str, Any],
    table: Mapping[str, Mapping[str, list[str]]],
    produced: frozenset[str] | set[str] = frozenset(),
) -> list[Finding]:
    """Return every specification that the level of commitment of the record requires and it lacks.

    A record at ``identified`` fixes its referent; a record at ``specified`` also writes the
    declarations that make it checkable. A record stating no admitted level is reported by the
    general requirement on ``commitment`` and by the vocabulary, so it is not reported here.
    """
    level = record.get("commitment")
    paths = commitment_requirements(str(record.get("type")), str(level), table)
    return unmet_general(
        record,
        paths,
        produced,
        label=f"commitment {level} requires",
        rule=rules.COMPLETENESS_UNMET_COMMITMENT,
    )


def requirements_by_presence(
    source: Path | None = None,
) -> dict[str, dict[str, dict[str, list[str]]]]:
    """Return, per record kind and field, the specifications that the presence and the absence of
    the field impose."""
    table = read_requirements(source).get("by_presence") or {}
    return {
        str(kind): {
            str(field): {
                state: list((cases or {}).get(state) or []) for state in ("present", "absent")
            }
            for field, cases in (fields or {}).items()
        }
        for kind, fields in table.items()
    }


def unmet_by_presence(
    record: Mapping[str, Any], table: Mapping[str, Mapping[str, Mapping[str, list[str]]]]
) -> list[Finding]:
    """Return every specification that the presence or the absence of a field requires and the
    record lacks.

    >>> table = {"model": {"derives_from": {"present": ["operations"], "absent": ["laws"]}}}
    >>> [f.text for f in unmet_by_presence({"type": "model"}, table)]
    ['derives_from absent requires: laws']
    >>> [f.text for f in unmet_by_presence({"type": "model", "derives_from": ["system.a"]}, table)]
    ['derives_from present requires: operations']
    """
    found: list[Finding] = []
    for field, cases in (table.get(str(record.get("type"))) or {}).items():
        state = "absent" if is_unfilled(record.get(field)) else "present"
        found += unmet_general(record, cases.get(state, []), label=f"{field} {state} requires")
    return found


def requirements_by_value(source: Path | None = None) -> dict[str, dict[str, dict[str, list[str]]]]:
    """Return, per record kind, field and value, the specifications that the value imposes."""
    table = read_requirements(source).get("by_value") or {}
    return {
        str(kind): {
            str(field): {str(value): list(paths or []) for value, paths in (values or {}).items()}
            for field, values in (fields or {}).items()
        }
        for kind, fields in table.items()
    }


def unmet_by_value(
    record: Mapping[str, Any],
    table: Mapping[str, Mapping[str, Mapping[str, list[str]]]],
    produced: frozenset[str] | set[str] = frozenset(),
) -> list[Finding]:
    """Return every specification that the value of a field of the record requires and it lacks.

    >>> table = {"design": {"kind": {"experiment": ["protocol"]}}}
    >>> [f.text for f in unmet_by_value({"type": "design", "kind": "experiment"}, table)]
    ['kind experiment requires: protocol']
    >>> unmet_by_value({"type": "design", "kind": "method"}, table)
    []
    """
    found: list[Finding] = []
    for field, values in (table.get(str(record.get("type"))) or {}).items():
        value = record.get(field)
        if isinstance(value, str) and value in values:
            found += unmet_general(
                record,
                values[value],
                produced,
                label=f"{field} {value} requires",
                rule=rules.COMPLETENESS_UNMET_BY_VALUE,
            )
    return found


def unmet_by_aim(
    question: Mapping[str, Any],
    records: Mapping[str, Mapping[str, Any]],
    required: Mapping[str, dict[str, list[str]]],
) -> list[Finding]:
    """Return every specification the aim of this question requires and the records leave open.

    Parameters
    ----------
    question : mapping
        One filled question record.
    records : mapping
        The records its paths reach, keyed by the prefix that names them: ``question``,
        ``phenomenon`` and ``target-system``.
    required : mapping
        The table the registry declares.

    Notes
    -----
    Each finding concerns the question, whose aim imposes the requirement: it lies at
    ``task.epistemic_aim``, with the required path as discriminator, whichever record that path
    reaches.

    An aim fixes what an answer must deliver, so it requires a specification to be filled and
    never a value that specification takes. Which value is right is a judgement of the inquiry,
    and a rule that reaches inside a field belongs to a consistency check between fields.
    """
    aim = at(question, "task.epistemic_aim")
    missing = []
    for path in (required.get(str(aim)) or {}).get("required", []):
        prefix, _, rest = path.partition(".")
        if is_unfilled(at(records.get(prefix, {}), rest)):
            missing.append(
                finding(
                    rules.COMPLETENESS_UNMET_AIM,
                    f"{aim} requires {path}",
                    "task",
                    "epistemic_aim",
                    value=path,
                )
            )
    return missing
