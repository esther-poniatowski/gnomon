"""
The stage of an itinerary, computed from its steps and from the record that it addresses.

An itinerary records the acts of one course of inquiry, and the status of the problem or the
question that it addresses records how that course ends. The stage of the course follows from
both, so no field of the itinerary records it: the view ``itinerary-progress`` reports it.

See Also
--------
docs/epistemology/processes/activities/epistemic-activities.md : the stages of an itinerary.
"""

from __future__ import annotations

from typing import Any, Mapping

#: The statuses of an addressed problem or question at which its course has reached an outcome
#: other than abandonment.
CONCLUDING_STATUSES = frozenset({"solved", "dissolved", "answered"})

#: The judged verdicts of a norm; ``pending`` is the verdict of a norm not yet judged, whereas an
#: ``inconclusive`` norm was judged without being met or failed.
JUDGED_VERDICTS = frozenset({"pass", "fail", "inconclusive"})

#: The stages of an itinerary, in the order of its course.
STAGES = ("planned", "in-progress", "concluded", "abandoned")


def _block(step: Mapping[str, Any], key: str) -> Mapping[str, Any]:
    """Return the block of a step under a key, or an empty mapping when the key holds none."""
    value = step.get(key)
    return value if isinstance(value, Mapping) else {}


def _judged(step: Mapping[str, Any]) -> bool:
    """Return whether the norm of a step has a judged verdict."""
    return _block(step, "norm").get("verdict") in JUDGED_VERDICTS


def _carried_out(step: Mapping[str, Any]) -> bool:
    """Return whether the act of a step was carried out: its output names a record, or its norm
    has a judged verdict."""
    return bool(_block(step, "output").get("ref")) or _judged(step)


def itinerary_stage(itinerary: Mapping[str, Any], records: Mapping[str, Mapping[str, Any]]) -> str:
    """Return the stage of an itinerary, computed from its steps and from the record it addresses.

    The itinerary is ``abandoned`` when the addressed problem or question is abandoned, and
    ``concluded`` when that record has reached another outcome and the norm of every act carried
    out has been judged. Otherwise it is ``in-progress`` once one act has been carried out, and
    ``planned`` before. A step taken by no act, such as the alternative of a branch, does not
    prevent the conclusion.

    >>> steps = [{"id": "a", "output": {"ref": "ans.x"}, "norm": {"verdict": "pass"}},
    ...          {"id": "b", "norm": {"verdict": "pending"}}]
    >>> itinerary_stage({"addresses": "prob.x", "steps": steps}, {"prob.x": {"status": "solved"}})
    'concluded'
    >>> itinerary_stage({"addresses": "prob.x", "steps": steps}, {"prob.x": {"status": "posed"}})
    'in-progress'
    >>> itinerary_stage({"addresses": "prob.x", "steps": steps[1:]}, {})
    'planned'
    """
    addressed = records.get(str(itinerary.get("addresses")))
    status = addressed.get("status") if isinstance(addressed, Mapping) else None
    if status == "abandoned":
        return "abandoned"
    acts = [s for s in itinerary.get("steps") or [] if isinstance(s, Mapping) and _carried_out(s)]
    if status in CONCLUDING_STATUSES and all(_judged(s) for s in acts):
        return "concluded"
    return "in-progress" if acts else "planned"
