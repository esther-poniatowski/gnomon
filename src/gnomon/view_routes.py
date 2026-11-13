"""Primary generated view for each named completion target."""

from __future__ import annotations

from collections.abc import Mapping
from dataclasses import dataclass
from types import MappingProxyType


@dataclass(frozen=True)
class ViewRoute:
    """One generated view and the research task that it supports."""

    view: str
    purpose: str


_ROUTES: Mapping[str, ViewRoute] = MappingProxyType(
    {
        "problem-posed": ViewRoute(
            "problem-state",
            "inspect each problem's demand, obstacles, and closure state",
        ),
        "question-typed": ViewRoute(
            "next-act",
            "inspect the question's open conditions and the acts that can address them",
        ),
        "subject-identified": ViewRoute(
            "next-act",
            "inspect the conditions that remain open after the subject is identified",
        ),
        "subject-specified": ViewRoute(
            "next-act",
            "inspect the remaining open conditions and the acts that are ready",
        ),
        "candidate-proposed": ViewRoute(
            "exposure",
            "inspect the candidate's revisable units and their dependencies",
        ),
        "candidate-assessed": ViewRoute(
            "problem-state",
            "inspect whether each problem's demand is met and whether it may close",
        ),
    }
)


def view_routes() -> Mapping[str, ViewRoute]:
    """Return the ordered routes from completion targets to primary views."""
    return _ROUTES


def view_route(scope: str) -> ViewRoute:
    """Return the primary view route of ``scope``.

    Raises
    ------
    ValueError
        If ``scope`` is not a named completion target.
    """
    try:
        return _ROUTES[scope]
    except KeyError as error:
        choices = ", ".join(_ROUTES)
        raise ValueError(f"unknown view scope {scope!r}; choose one of {choices}") from error
