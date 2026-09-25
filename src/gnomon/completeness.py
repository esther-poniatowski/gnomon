"""
What a filled inquiry must carry, read from the registry that declares it.

Two kinds of requirement govern a record, and both are declared in ``data/requirements.yml``
rather than restated here:

- the values a closed field admits, listed per record kind under ``vocabularies``;
- the general ones, listed per record kind under ``always``;
- the ones an epistemic aim adds, and the general ones it relaxes, under ``by_aim``. An inquiry
  that produces a phenomenon cannot be asked to state that phenomenon in advance.

A third kind is neither: a consistency between fields, such as an accuracy marked inapplicable
while outputs are listed for matching. No aim decides those, so each is its own check.

The method notes document the same requirements and are checked against the registry, so no
check here reads a document.

See Also
--------
data/requirements.yml : the registry these functions read.
"""

from __future__ import annotations

from pathlib import Path
from typing import Any, Mapping

import yaml

DATA = Path(__file__).parent / "data"

#: The registry declaring what a filled inquiry must carry.
REQUIREMENT_REGISTRY = DATA / "requirements.yml"

#: The registry declaring the values each closed field admits.
VOCABULARY_REGISTRY = DATA / "vocabularies.yml"


def _registry(source: Path | None) -> dict[str, Any]:
    return yaml.safe_load((source or REQUIREMENT_REGISTRY).read_text(encoding="utf-8")) or {}


def requirements_by_aim(source: Path | None = None) -> dict[str, dict[str, list]]:
    """Return, per epistemic aim, the paths its inquiry fixes and the ones it may leave open.

    Raises
    ------
    ValueError
        If the registry declares no aim.
    """
    by_aim = _registry(source).get("by_aim") or {}
    if not by_aim:
        raise ValueError(f"{(source or REQUIREMENT_REGISTRY).name} declares no aim")
    return {
        aim: {
            "required": [e["path"] for e in (entry.get("required") or [])],
            "open": list(entry.get("open") or []),
        }
        for aim, entry in by_aim.items()
    }


def always_required(kind: str, source: Path | None = None) -> list[str]:
    """Return the specifications every record of ``kind`` carries, whatever the inquiry."""
    return list((_registry(source).get("always") or {}).get(kind) or [])


def record_kinds(source: Path | None = None) -> list[str]:
    """Return every record kind the registry states a general requirement for."""
    return sorted((_registry(source).get("always") or {}))


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


def unmet_general(
    record: Mapping[str, Any], paths: list[str], relaxed: frozenset[str] | set[str] = frozenset()
) -> list[str]:
    """Return every always-required specification the record leaves open without licence.

    An aim may admit open a specification that the registry requires always, so the caller
    passes the paths that aim relaxes.
    """
    missing = []
    for path in paths:
        if path in relaxed:
            continue
        if at(record, path) in (None, [], {}, "open"):
            missing.append(f"always required: {path}")
    return missing


def unmet_by_aim(
    question: Mapping[str, Any],
    records: Mapping[str, Mapping[str, Any]],
    required: Mapping[str, dict[str, list]],
) -> list[str]:
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
    An aim fixes what an answer must deliver, so it requires a specification to be filled and
    never a value that specification takes. Which value is right is a judgement of the inquiry,
    and a rule that reaches inside a field belongs to a consistency check between fields.
    """
    aim = at(question, "task.epistemic_aim")
    missing = []
    for path in (required.get(str(aim)) or {}).get("required", []):
        prefix, _, rest = path.partition(".")
        if at(records.get(prefix, {}), rest) in (None, [], {}, "open"):
            missing.append(f"{aim} requires {path}")
    return missing


def contradictory_accuracy(question: Mapping[str, Any]) -> list[str]:
    """Return the matches a question lists while declaring that accuracy does not apply.

    No aim decides whether an answer is matched against a measurement: an inquiry over a formal
    model class may match measured exponents, and one seeking a theorem may match nothing. The
    rule is therefore a consistency between fields rather than a requirement of an aim.
    """
    accuracy = at(question, "task.required_accuracy") or {}
    if accuracy.get("standard") != "not-applicable":
        return []
    return [
        f"task.required_accuracy.{key} is listed although accuracy does not apply"
        for key in ("outputs_to_match", "structures_to_match")
        if accuracy.get(key)
    ]


def unrealized_link(question: Mapping[str, Any], answer: Mapping[str, Any]) -> list[str]:
    """Return the link a question asks for and the answer does not supply.

    A question may bound the explanans to substrate-specific variables, to substrate-independent
    ones, or to the link between them. The third is not a third kind of variable: it obliges the
    answer to give both descriptions and the mapping that carries one onto the other, since a
    question about how a role is realized is answered by neither description alone. The two
    descriptions are declared in the ordinary blocks; the mapping is what the answer would
    otherwise leave to a reader to reconstruct.
    """
    if at(question, "task.admissible_explanans.substrate") != "mapping":
        return []
    realizations = answer.get("realizations") or []
    if not realizations:
        return ["the question asks for a link, and the answer maps no quantity onto its realization"]
    return [
        f"realizations[{index}] names what it realizes without saying by what"
        for index, entry in enumerate(realizations)
        if isinstance(entry, Mapping) and not (entry.get("realizes") and entry.get("by"))
    ]


def undeclared_explanans_bound(question: Mapping[str, Any]) -> list[str]:
    """Return the question that bounds the explanans by nothing without saying which silence it is.

    A question may leave the answer free to explain at any level, and a question may not yet know
    which level its analysis will need. Both are written by leaving the bound empty, and the two
    read alike while meaning opposite things: the first is a finished decision, the second is work
    not done. The record separates them by carrying a justification for the decision, or by marking
    the field open in its maturity, which is what a maturity marker is for.
    """
    bound = at(question, "task.admissible_explanans") or {}
    if bound.get("compositional") is not None or bound.get("substrate") is not None:
        return []
    if bound.get("justification"):
        return []
    if (question.get("maturity") or {}).get("task.admissible_explanans"):
        return []
    return [
        "task.admissible_explanans bounds the answer by nothing, and neither a justification"
        " nor a maturity marker says whether that is a decision or unfinished work"
    ]


def unstated_standing(question: Mapping[str, Any]) -> list[str]:
    """Return every virtue the question weighs without saying what failing it costs.

    A virtue bears on an answer in one of two ways, and which one is not derivable from the virtue
    itself: constitutive of the product, so that an answer lacking it is inadmissible however
    accurate, or preferred, so that it ranks answers that are already admissible. No aim decides
    this either, since an inquiry may hold an account to intelligibility whatever product it seeks
    and another may treat the same virtue as a tie-breaker. The question therefore states it, and
    an entry that does not leaves the product test unable to say what it applies.
    """
    return [
        f"virtues[{index}].standing is unstated for {entry.get('virtue') or 'an unnamed virtue'}"
        for index, entry in enumerate(question.get("virtues") or [])
        if isinstance(entry, Mapping) and not entry.get("standing")
    ]


def malformed_restrictions(
    question: Mapping[str, Any], variables: Iterable[str]
) -> list[str]:
    """Return every domain restriction that does not say what it holds, or holds it wrongly.

    A restriction names one quantity and the set it is held to, or it names none and carries the
    expression it holds under; carrying both says the same thing twice and carrying neither says
    nothing. An entry naming no quantity needs a name, since nothing else identifies it. How a
    quantity is held — clamped, initial, stationary, without an event — applies to something that
    varies, so an entry naming a parameter states no such kind: a parameter is already fixed.

    Parameters
    ----------
    question : mapping
        One filled question record.
    variables : iterable of str
        The symbols its target system declares as variables rather than as parameters.
    """
    varying = set(variables)
    found = []
    for entry in at(question, "subject.domain.restrictions") or []:
        if not isinstance(entry, Mapping):
            continue
        held = entry.get("of")
        symbol = held.rsplit("#", 1)[-1] if isinstance(held, str) else None
        label = entry.get("name") or held or "an entry"
        carried = [key for key in ("values", "expression") if entry.get(key) is not None]
        if len(carried) != 1:
            found.append(f"restrictions.{label}: carries {len(carried)} of values and expression")
        if not held and not entry.get("name"):
            found.append("restrictions: an entry names neither a quantity nor itself")
        if entry.get("restriction") and symbol not in varying:
            found.append(
                f"restrictions.{label}: states how it is held although it names no variable"
            )
    return found


def undecided_boundaries(record: Mapping[str, Any]) -> list[str]:
    """Return every external system whose constraint is neither written nor declared absent.

    An external system either imposes something on the variables it shares, written as
    expressions, or imposes nothing beyond their declared value sets, written as an empty list.
    ``open`` says neither. A boundary that was never written then reads exactly like one that
    imposes nothing, so the quantities a constraint would have named are never missed: an
    overshoot diagnostic, a measurement coverage. Where a constraint is a genuine scientific
    unknown, the record says so with a ``maturity`` entry rather than by leaving the field open.
    """
    return [
        f"external_systems.{entry.get('symbol')}: constrains is open, so the boundary is named"
        " without being decided"
        for entry in record.get("external_systems") or []
        if isinstance(entry, Mapping) and entry.get("constrains") == "open"
    ]


def admitted_values(kind: str, source: Path | None = None) -> dict[str, frozenset[str]]:
    """Return, per field of ``kind``, the values it admits.

    A key names the block enclosing the field and the field itself, so ``terms.type`` is the
    type of a term and ``.status`` is the status of the record. Every closed field also admits
    ``open``, absent from the registry.
    """
    registry = yaml.safe_load((source or VOCABULARY_REGISTRY).read_text(encoding="utf-8")) or {}
    fields = (registry.get("vocabularies") or {}).get(kind) or {}
    return {
        name: frozenset({entry["value"] for entry in values} | {"open"})
        for name, values in fields.items()
    }


def inadmissible_values(record: Mapping[str, Any], admitted: Mapping[str, frozenset[str]]) -> list[str]:
    """Return every closed field of the record holding a value its vocabulary does not admit."""
    found: list[str] = []

    def visit(node: Any, block: str) -> None:
        if isinstance(node, Mapping):
            for key, value in node.items():
                vocabulary = admitted.get(f"{block}.{key}")
                if vocabulary is not None:
                    for item in value if isinstance(value, list) else [value]:
                        if isinstance(item, str) and item not in vocabulary:
                            found.append(f"{block or 'record'}.{key}: {item} is not admitted")
                if isinstance(value, (Mapping, list)):
                    visit(value, block or key)
        elif isinstance(node, list):
            for item in node:
                visit(item, block)

    for key, value in record.items():
        vocabulary = admitted.get(f".{key}")
        if vocabulary is not None:
            for item in value if isinstance(value, list) else [value]:
                if isinstance(item, str) and item not in vocabulary:
                    found.append(f"record.{key}: {item} is not admitted")
        if isinstance(value, (Mapping, list)):
            visit(value, key)
    return found
