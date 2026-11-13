"""Validated presentation defaults for graphs published by Gnomon."""

from __future__ import annotations

import re
from collections.abc import Callable, Mapping
from dataclasses import dataclass
from pathlib import Path
from types import MappingProxyType
from typing import TypedDict

import yaml

GRAPH_PRESENTATION_REGISTRY = (
    Path(__file__).parent / "data" / "registries" / "graph-presentation.yml"
)

_TOKEN = re.compile(r"^[a-z][a-z0-9-]*$")
_REQUIRED_CATEGORIES = frozenset({"product", "activity", "source"})


@dataclass(frozen=True)
class CategoryPresentation:
    """Presentation shared by every node of one graph category."""

    title: str
    shape: str
    marker: str
    style: str


@dataclass(frozen=True)
class KindPresentation:
    """Presentation that distinguishes one semantic node kind within its category."""

    category: str
    title: str
    icon: str
    marker: str
    style: str


@dataclass(frozen=True)
class EdgePresentation:
    """Presentation shared by every edge of one semantic relation kind."""

    title: str
    layer: str
    style: str


@dataclass(frozen=True)
class NodePresentation:
    """Effective presentation of one node after its category and kind are combined."""

    category_title: str
    shape: str
    marker: str
    category_style: str
    kind_title: str
    icon: str
    kind_style: str


@dataclass(frozen=True)
class ProfileMetadata:
    """Identity and layout compatibility of one presentation profile."""

    identifier: str
    version: int
    recommended_layout: str
    compatible_layouts: tuple[str, ...]


class CategoryContract(TypedDict):
    """Portable presentation of one graph category."""

    # The portable profile contract names this field ``id``.
    # pylint: disable-next=disallowed-name
    id: str
    title: str
    shape: str
    marker: str
    style: str


class NodeKindContract(TypedDict):
    """Portable presentation of one registered node kind."""

    # The portable profile contract names this field ``id``.
    # pylint: disable-next=disallowed-name
    id: str
    category: str
    title: str
    icon: str
    marker: str
    style: str


class EdgeKindContract(TypedDict):
    """Portable presentation of one registered edge kind."""

    # The portable profile contract names this field ``id``.
    # pylint: disable-next=disallowed-name
    id: str
    title: str
    layer: str
    style: str


class LayoutContract(TypedDict):
    """Portable layout recommendation and compatibility declaration."""

    recommended: str
    compatible: list[str]


class GraphPresentationContract(TypedDict):
    """Self-contained presentation profile published with one graph."""

    profile: str
    version: int
    layouts: LayoutContract
    categories: list[CategoryContract]
    node_kinds: list[NodeKindContract]
    edge_kinds: list[EdgeKindContract]


@dataclass(frozen=True)
class GraphPresentation:
    """Validated category, node-kind, and edge-kind presentation registries."""

    profile: str
    version: int
    recommended_layout: str
    compatible_layouts: tuple[str, ...]
    categories: Mapping[str, CategoryPresentation]
    node_kinds: Mapping[str, KindPresentation]
    edge_kinds: Mapping[str, EdgePresentation]

    def node(self, category: str, kind: str) -> NodePresentation:
        """Return the effective presentation of ``kind`` in ``category``.

        Raises
        ------
        ValueError
            If the graph names an unregistered category.
        """
        try:
            shared = self.categories[category]
        except KeyError as error:
            raise ValueError(f"unregistered graph category: {category}") from error
        specific = self.node_kinds.get(kind)
        return NodePresentation(
            category_title=shared.title,
            shape=shared.shape,
            marker=specific.marker if specific is not None else shared.marker,
            category_style=shared.style,
            kind_title=(specific.title if specific is not None else kind.replace("-", " ")),
            icon=specific.icon if specific is not None else "",
            kind_style=specific.style if specific is not None else "",
        )

    def edge(self, kind: str) -> EdgePresentation:
        """Return the presentation registered for one edge kind.

        Raises
        ------
        ValueError
            If the graph names an unregistered edge kind.
        """
        try:
            return self.edge_kinds[kind]
        except KeyError as error:
            raise ValueError(f"unregistered graph edge kind: {kind}") from error

    def contract(self) -> GraphPresentationContract:
        """Return the portable profile embedded once in each generated graph."""
        return {
            "profile": self.profile,
            "version": self.version,
            "layouts": {
                "recommended": self.recommended_layout,
                "compatible": list(self.compatible_layouts),
            },
            "categories": [
                {
                    "id": identifier,
                    "title": entry.title,
                    "shape": entry.shape,
                    "marker": entry.marker,
                    "style": entry.style,
                }
                for identifier, entry in self.categories.items()
            ],
            "node_kinds": [
                {
                    "id": identifier,
                    "category": entry.category,
                    "title": entry.title,
                    "icon": entry.icon,
                    "marker": entry.marker,
                    "style": entry.style,
                }
                for identifier, entry in self.node_kinds.items()
            ],
            "edge_kinds": [
                {
                    "id": identifier,
                    "title": entry.title,
                    "layer": entry.layer,
                    "style": entry.style,
                }
                for identifier, entry in self.edge_kinds.items()
            ],
        }


def load_graph_presentation(source: Path | None = None) -> GraphPresentation:
    """Load and validate the graph-presentation registry from package data or ``source``.

    Parameters
    ----------
    source
        Registry path. Package data is read when omitted.

    Returns
    -------
    GraphPresentation
        Immutable mappings of the validated presentation entries.

    Raises
    ------
    TypeError
        If the registry or one of its entries is not a mapping.
    ValueError
        If the registry has an invalid structure or unsafe identifier.
    """
    path = source or GRAPH_PRESENTATION_REGISTRY
    document = yaml.safe_load(path.read_text(encoding="utf-8"))
    root = _mapping(document, "graph presentation registry")
    metadata = _profile_metadata(root)
    categories = _entries(
        root,
        "categories",
        lambda name, entry: CategoryPresentation(
            title=_text(entry, "title", name),
            shape=_token(entry, "shape", name),
            marker=_text(entry, "marker", name),
            style=_token(entry, "style", name),
        ),
    )
    missing = sorted(_REQUIRED_CATEGORIES - categories.keys())
    if missing:
        raise ValueError("graph presentation registry lacks categories: " + ", ".join(missing))
    node_kinds = _entries(
        root,
        "node_kinds",
        lambda name, entry: KindPresentation(
            category=_token(entry, "category", name),
            title=_text(entry, "title", name),
            icon=_token(entry, "icon", name),
            marker=_text(entry, "marker", name),
            style=_token(entry, "style", name),
        ),
    )
    for name, entry in node_kinds.items():
        if entry.category not in categories:
            raise ValueError(
                f"node_kinds.{name}.category names an unregistered category: " f"{entry.category}"
            )
    edge_kinds = _entries(
        root,
        "edge_kinds",
        lambda name, entry: EdgePresentation(
            title=_text(entry, "title", name),
            layer=_token(entry, "layer", name),
            style=_token(entry, "style", name),
        ),
    )
    return GraphPresentation(
        metadata.identifier,
        metadata.version,
        metadata.recommended_layout,
        metadata.compatible_layouts,
        MappingProxyType(categories),
        MappingProxyType(node_kinds),
        MappingProxyType(edge_kinds),
    )


def _profile_metadata(root: Mapping[object, object]) -> ProfileMetadata:
    """Return the validated identity and layouts of one profile."""
    profile = _mapping(root.get("profile"), "profile")
    layouts = _mapping(root.get("layouts"), "layouts")
    recommended = _safe_text(layouts, "recommended", "layouts")
    compatible = _token_sequence(layouts, "compatible", "layouts")
    if recommended not in compatible:
        raise ValueError("layouts.recommended must occur in layouts.compatible")
    return ProfileMetadata(
        identifier=_safe_text(profile, "id", "profile"),
        version=_positive_integer(profile, "version", "profile"),
        recommended_layout=recommended,
        compatible_layouts=compatible,
    )


def _entries[Entry](
    root: Mapping[object, object],
    key: str,
    build: Callable[[str, Mapping[object, object]], Entry],
) -> dict[str, Entry]:
    """Return one validated mapping of named registry entries."""
    raw = _mapping(root.get(key), key)
    entries: dict[str, Entry] = {}
    for untyped_name, untyped_entry in raw.items():
        if not isinstance(untyped_name, str) or _TOKEN.fullmatch(untyped_name) is None:
            raise ValueError(f"{key} contains an unsafe identifier: {untyped_name!r}")
        entries[untyped_name] = build(
            untyped_name, _mapping(untyped_entry, f"{key}.{untyped_name}")
        )
    return entries


def _mapping(value: object, place: str) -> Mapping[object, object]:
    """Return ``value`` as a mapping, or report its registry location."""
    if not isinstance(value, Mapping):
        raise TypeError(f"{place} must be a mapping")
    return value


def _text(entry: Mapping[object, object], key: str, name: str) -> str:
    """Return one required non-empty text value of an entry."""
    value = entry.get(key)
    if not isinstance(value, str) or not value.strip():
        raise ValueError(f"{name}.{key} must be non-empty text")
    return value


def _token(entry: Mapping[object, object], key: str, name: str) -> str:
    """Return one safe presentation token of an entry."""
    value = _text(entry, key, name)
    if _TOKEN.fullmatch(value) is None:
        raise ValueError(f"{name}.{key} is not a safe presentation token: {value!r}")
    return value


def _safe_text(entry: Mapping[object, object], key: str, name: str) -> str:
    """Return one required text value constrained to a safe identifier."""
    return _token(entry, key, name)


def _positive_integer(entry: Mapping[object, object], key: str, name: str) -> int:
    """Return one required positive integer value of an entry."""
    value = entry.get(key)
    if not isinstance(value, int) or isinstance(value, bool) or value < 1:
        raise ValueError(f"{name}.{key} must be a positive integer")
    return value


def _token_sequence(entry: Mapping[object, object], key: str, name: str) -> tuple[str, ...]:
    """Return one non-empty sequence of distinct safe presentation tokens."""
    value = entry.get(key)
    if not isinstance(value, list) or not value:
        raise ValueError(f"{name}.{key} must be a non-empty list")
    tokens: list[str] = []
    for item in value:
        if not isinstance(item, str) or _TOKEN.fullmatch(item) is None:
            raise ValueError(f"{name}.{key} contains an unsafe presentation token: {item!r}")
        if item in tokens:
            raise ValueError(f"{name}.{key} contains a duplicate token: {item}")
        tokens.append(item)
    return tuple(tokens)
