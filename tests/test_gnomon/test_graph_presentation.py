"""Presentation defaults of the operational graph."""

from pathlib import Path

import pytest

from gnomon.graph_presentation import load_graph_presentation


def test_categories_keep_the_common_form_while_product_kinds_use_distinct_markers() -> None:
    registry = load_graph_presentation()

    problem = registry.node("product", "problem")
    question = registry.node("product", "question")
    answer = registry.node("product", "answer")
    assessment = registry.node("product", "assessment")

    assert {item.shape for item in (problem, question, answer, assessment)} == {"rectangle"}
    assert len({item.marker for item in (problem, question, answer, assessment)}) == 4
    assert {item.kind_title for item in (problem, question, answer, assessment)} == {
        "Problem",
        "Question",
        "Answer",
        "Assessment",
    }


def test_an_unregistered_kind_takes_its_category_fallback() -> None:
    registry = load_graph_presentation()

    presentation = registry.node("activity", "custom-analysis")

    assert presentation.category_title == "Research activity"
    assert presentation.shape == "capsule"
    assert presentation.marker == "⚙"
    assert presentation.kind_title == "custom analysis"


def test_edge_kinds_declare_readable_titles_and_filter_layers() -> None:
    registry = load_graph_presentation()

    assert registry.edge("addresses").title == "addressed by"
    assert registry.edge("addresses").layer == "inquiry"
    assert registry.edge("takes").title == "input"
    assert registry.edge("takes").layer == "provenance"
    assert registry.edge("assembly-citation").title == "citation"
    assert registry.edge("assembly-citation").layer == "citation"


def test_the_portable_contract_is_versioned_and_declares_compatible_layouts() -> None:
    registry = load_graph_presentation()

    contract = registry.contract()

    assert contract["profile"] == "gnomon-operational"
    assert contract["version"] == 3
    assert contract["layouts"] == {
        "recommended": "layered-directed",
        "compatible": ["layered-directed", "force-directed", "compact-network"],
    }
    assert next(item for item in contract["node_kinds"] if item["id"] == "problem") == {
        "id": "problem",
        "category": "product",
        "title": "Problem",
        "icon": "circle-alert",
        "marker": "!",
        "style": "problem",
    }
    assert next(item for item in contract["edge_kinds"] if item["id"] == "takes") == {
        "id": "takes",
        "title": "input",
        "layer": "provenance",
        "style": "input",
    }


def test_an_unsafe_style_token_is_rejected(tmp_path: Path) -> None:
    registry = tmp_path / "graph-presentation.yml"
    registry.write_text(
        """
profile: {id: test-profile, version: 1}
layouts: {recommended: layered-directed, compatible: [layered-directed]}
categories:
  product: {title: Research product, shape: rectangle, marker: P, style: product}
  activity: {title: Research activity, shape: capsule, marker: A, style: activity}
  source: {title: External source, shape: dashed, marker: S, style: source}
node_kinds:
  problem: {category: product, title: Problem, icon: circle-alert, marker: '!', style: 'bad style'}
edge_kinds: {}
""".lstrip(),
        encoding="utf-8",
    )

    with pytest.raises(
        ValueError,
        match=r"problem\.style is not a safe presentation token: 'bad style'",
    ):
        load_graph_presentation(registry)


def test_the_recommended_layout_must_be_compatible(tmp_path: Path) -> None:
    registry = tmp_path / "graph-presentation.yml"
    registry.write_text(
        """
profile: {id: test-profile, version: 1}
layouts: {recommended: layered-directed, compatible: [force-directed]}
categories:
  product: {title: Research product, shape: rectangle, marker: P, style: product}
  activity: {title: Research activity, shape: capsule, marker: A, style: activity}
  source: {title: External source, shape: dashed, marker: S, style: source}
node_kinds: {}
edge_kinds: {}
""".lstrip(),
        encoding="utf-8",
    )

    with pytest.raises(
        ValueError,
        match=r"layouts\.recommended must occur in layouts\.compatible",
    ):
        load_graph_presentation(registry)
