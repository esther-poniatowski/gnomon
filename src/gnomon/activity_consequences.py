"""Operative consequences derived from the activity and product-type registries."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Iterable, Mapping

from .itineraries import EXTERNAL, TO_CREATE, Activity, Slot, activities, product_types


@dataclass(frozen=True)
class ActivityConsequence:
    """The typed inputs and output locations of one epistemic activity.

    Attributes
    ----------
    required_inputs : tuple of str
        The required input slots, including cardinality and admitted attitudes.
    output_type : str
        The product type yielded when the norm of the activity passes.
    produces_in : tuple of str
        The records or fields that can hold the output, including incomplete coverage.
    """

    required_inputs: tuple[str, ...]
    output_type: str
    produces_in: tuple[str, ...]


def _input_requirement(held: Slot) -> str:
    """Return one required input slot as a compact label."""
    types = " | ".join(sorted(held.types))
    if held.attitudes:
        types += f" ({' | '.join(sorted(held.attitudes))})"
    if held.most is None:
        return f"at least {held.least} × {types}"  # noqa: RUF001 - multiplication symbol
    if held.least == held.most == 1:
        return types
    return f"{held.least} × {types}"  # noqa: RUF001 - multiplication symbol


def _output_locations(entry: Mapping[str, Any]) -> tuple[str, ...]:
    """Return the records or fields that the registry assigns to one product type."""
    records = entry.get("record")
    if records == TO_CREATE:
        return ("not represented by a record yet",)
    if records == EXTERNAL:
        return ("external pointer",)
    if not isinstance(records, list):
        return ("no registered record or field",)

    fields = entry.get("fields")
    prefix = "partial: " if entry.get("status") == "partial" else ""
    locations: list[str] = []
    for kind in records:
        paths = fields.get(kind, []) if isinstance(fields, Mapping) else fields or []
        if paths:
            locations.extend(f"{prefix}{kind}.{path}" for path in paths)
        else:
            locations.append(f"{prefix}{kind} record")
    return tuple(locations)


def activity_consequences(
    activity_types: Mapping[str, Activity] | None = None,
    products: Mapping[str, Mapping[str, Any]] | None = None,
) -> dict[str, ActivityConsequence]:
    """Return the operative consequence of every registered activity.

    Parameters
    ----------
    activity_types : mapping, optional
        Activities keyed by identifier. The package registry is read when omitted.
    products : mapping, optional
        Product types keyed by identifier. The package registry is read when omitted.
    """
    activity_types = activities() if activity_types is None else activity_types
    products = product_types() if products is None else products
    return {
        name: ActivityConsequence(
            required_inputs=tuple(
                _input_requirement(held) for held in activity.inputs if held.least > 0
            ),
            output_type=activity.output,
            produces_in=_output_locations(products.get(activity.output) or {}),
        )
        for name, activity in activity_types.items()
    }


def activities_unblocked_by(
    output_type: str,
    waiting: Iterable[tuple[str, tuple[str, ...]]],
    *,
    excluding: str | None = None,
) -> tuple[str, ...]:
    """Return waiting activities whose missing slot admits ``output_type``.

    The result states a possible direct dependency. The producing activity must still pass its
    norm, and another product of the same type may satisfy the slot instead.
    """
    found: dict[str, None] = {}
    for activity, missing in waiting:
        if activity != excluding and any(
            output_type in requirement.split(" | ") for requirement in missing
        ):
            found.setdefault(activity, None)
    return tuple(found)
