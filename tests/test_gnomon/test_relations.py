"""The relation registry, the checks of the relations that records state, and the transmission of a
revision along each edge.

Each rule is shown on a planted defect; the worked inquiries report none, as the check of the
examples shows.
"""

from __future__ import annotations

from typing import Any

from gnomon.completeness import admitted_values, inadmissible_values
from gnomon.relations import (
    declared_paths,
    flagged_dependents,
    relation_findings,
    workspace_relation_findings,
)
from gnomon.schemas import load_base

ANSWERS: dict[str, dict[str, Any]] = {
    f"ans.a.{name}": {"id": f"ans.a.{name}", "type": "answer", "answers": "quest.a.q"}
    for name in ("x", "y", "z")
}
RECORDS: dict[str, dict[str, Any]] = {
    **ANSWERS,
    "quest.a.q": {"id": "quest.a.q", "type": "question"},
}


def _with(ident: str, *relations: dict[str, Any]) -> dict[str, dict[str, Any]]:
    return {**RECORDS, ident: {**RECORDS[ident], "relations": list(relations)}}


def _rules(records: dict[str, dict[str, Any]], ident: str) -> list[str]:
    return [f.rule.id for f in relation_findings(records[ident], records)]


def _schema_paths(node: Any, path: str = "") -> set[str]:
    found = {path} if path else set()
    if isinstance(node, dict):
        for key, value in (node.get("properties") or {}).items():
            found |= _schema_paths(value, f"{path}.{key}" if path else key)
        if isinstance(node.get("items"), dict):
            found |= _schema_paths(node["items"], f"{path}[]")
    return found


def test_every_field_that_the_registry_names_exists_in_its_base_schema() -> None:
    for kind, path in declared_paths():
        schema = load_base(kind)
        paths = _schema_paths(schema)
        assert path in paths or f"{path}[]" in paths, f"{kind}: {path}"


def test_the_relation_tokens_are_the_closed_values_of_their_lists() -> None:
    admitted = admitted_values("answer")
    good = {"relations": [{"relation": "incompatible-with", "members": ["ans.a.y"]}]}
    bad = {"relations": [{"relation": "rebuts", "target": "ans.a.y"}]}
    assert inadmissible_values(good, admitted) == []
    assert [f.rule.id for f in inadmissible_values(bad, admitted)] == [
        "completeness/inadmissible-value"
    ]


def test_an_end_of_a_wrong_kind_and_a_relation_to_itself_are_reported() -> None:
    wrong = _with("ans.a.x", {"relation": "supports", "target": "quest.a.q"})
    assert _rules(wrong, "ans.a.x") == ["relation/mistyped-end"]
    itself = _with("ans.a.x", {"relation": "supports", "target": "ans.a.x"})
    assert _rules(itself, "ans.a.x") == ["relation/self"]


def test_a_missing_or_an_unadmitted_attribute_is_reported() -> None:
    no_respect = _with("ans.a.x", {"relation": "contrasts-with", "target": "ans.a.y"})
    assert _rules(no_respect, "ans.a.x") == ["relation/misplaced-attribute"]
    stray = _with("ans.a.x", {"relation": "revises", "target": "ans.a.y", "respect": ["f"]})
    assert _rules(stray, "ans.a.x") == ["relation/misplaced-attribute"]
    bad_mode = _with(
        "ans.a.x", {"relation": "supports", "target": "ans.a.y", "warrant": {"kind": "hunch"}}
    )
    assert _rules(bad_mode, "ans.a.x") == ["relation/misplaced-attribute"]
    good = _with(
        "ans.a.x",
        {"relation": "contrasts-with", "target": "ans.a.y", "respect": ["f"]},
        {"relation": "supports", "target": "ans.a.z", "warrant": {"kind": "abductive"}},
    )
    assert _rules(good, "ans.a.x") == []


def test_a_set_stated_twice_or_not_minimal_is_reported() -> None:
    records = {
        **RECORDS,
        "ans.a.x": {
            **RECORDS["ans.a.x"],
            "relations": [{"relation": "incompatible-with", "members": ["ans.a.y"]}],
        },
        "ans.a.y": {
            **RECORDS["ans.a.y"],
            "relations": [{"relation": "incompatible-with", "members": ["ans.a.x"]}],
        },
    }
    assert [f.rule.id for _, f in workspace_relation_findings(records)] == ["relation/restated"]
    wider = {
        **records,
        "ans.a.y": {
            **RECORDS["ans.a.y"],
            "relations": [{"relation": "incompatible-with", "members": ["ans.a.x", "ans.a.z"]}],
        },
    }
    assert [f.rule.id for _, f in workspace_relation_findings(wider)] == ["relation/restated"]


def test_a_forbidden_cycle_is_an_error_and_a_judged_one_a_warning() -> None:
    def cycle(relation: str) -> dict[str, dict[str, Any]]:
        return {
            **RECORDS,
            "ans.a.x": {
                **RECORDS["ans.a.x"],
                "relations": [{"relation": relation, "target": "ans.a.y"}],
            },
            "ans.a.y": {
                **RECORDS["ans.a.y"],
                "relations": [{"relation": relation, "target": "ans.a.x"}],
            },
        }

    assert [f.rule.id for _, f in workspace_relation_findings(cycle("revises"))] == [
        "relation/cycle"
    ]
    found = [f for _, f in workspace_relation_findings(cycle("supports"))]
    assert [(f.rule.id, f.rule.level) for f in found] == [("relation/judged-cycle", "warning")]


def test_an_answer_rests_constitutively_on_its_question() -> None:
    """A proven answer is not flagged by a reorientation of its grounds, but by one of its
    question."""
    records: dict[str, dict[str, Any]] = {
        "quest.a.q": {"id": "quest.a.q", "type": "question"},
        "bg.a.b": {"id": "bg.a.b", "type": "background"},
        "ans.a.x": {
            "id": "ans.a.x",
            "type": "answer",
            "answers": "quest.a.q",
            "support": "formally-proven",
            "grounds": [{"record": "bg.a.b.law"}],
        },
    }
    assert flagged_dependents("bg.a.b", "reorientation", records) == {}
    assert flagged_dependents("quest.a.q", "reorientation", records) == {
        "ans.a.x": "answers (constitutive)"
    }


def test_a_reference_in_prose_transmits_no_revision() -> None:
    records: dict[str, dict[str, Any]] = {
        "ans.a.y": {"id": "ans.a.y", "type": "answer"},
        "ans.a.x": {"id": "ans.a.x", "type": "answer", "claim": {"reading": "unlike ans.a.y"}},
    }
    assert flagged_dependents("ans.a.y", "retraction", records) == {}


def test_a_support_flags_the_supported_answer_by_the_warrant_of_its_entry() -> None:
    records = _with(
        "ans.a.x", {"relation": "supports", "target": "ans.a.y", "warrant": {"kind": "deductive"}}
    )
    assert flagged_dependents("ans.a.x", "reorientation", records) == {}
    assert flagged_dependents("ans.a.x", "scope-narrowing", records) == {
        "ans.a.y": "supports (monotonic)"
    }


def test_a_revision_of_one_law_flags_the_answers_that_rest_on_it() -> None:
    """A law superseded by a step is named by its dotted identifier, and its dependents are
    flagged."""
    from gnomon.propagation import revisions

    records: dict[str, dict[str, Any]] = {
        "bg.a.b": {"id": "bg.a.b", "type": "background"},
        "ans.a.x": {"id": "ans.a.x", "type": "answer", "grounds": [{"record": "bg.a.b.law"}]},
        "itin.a.i": {
            "id": "itin.a.i",
            "type": "itinerary",
            "steps": [{"id": "s", "revises": {"record": "bg.a.b.law", "kind": "retraction"}}],
        },
    }
    (revision,) = revisions(records)
    assert revision.flagged == ("ans.a.x",)


def test_a_revision_of_one_law_flags_a_record_that_admits_its_whole_background() -> None:
    records: dict[str, dict[str, Any]] = {
        "bg.a.b": {"id": "bg.a.b", "type": "background"},
        "mod.a.m": {"id": "mod.a.m", "type": "model", "background": "bg.a.b"},
    }
    assert flagged_dependents("bg.a.b.law", "retraction", records) == {
        "mod.a.m": "background (defeasible)"
    }


def test_the_links_of_a_question_are_checked_as_relations() -> None:
    """A link names a question, never itself, states its relation, and passes through a record of
    the kind that its relation admits."""
    records: dict[str, dict[str, Any]] = {
        "quest.a.p": {"id": "quest.a.p", "type": "question"},
        "phen.a.g": {"id": "phen.a.g", "type": "phenomenon"},
        "prob.a.p": {"id": "prob.a.p", "type": "problem"},
    }

    def rules(*links: dict[str, Any], addresses: str = "prob.a.p") -> list[str]:
        question = {
            "id": "quest.a.q",
            "type": "question",
            "addresses": addresses,
            "links": list(links),
        }
        return [f.rule.id for f in relation_findings(question, {**records, "quest.a.q": question})]

    link = {"question": "quest.a.p", "relation": "explanans-from", "via": "phen.a.g"}
    assert rules(link) == []
    assert rules({**link, "question": "phen.a.g"}) == ["relation/mistyped-end"]
    assert rules({**link, "question": "quest.a.q"}) == ["relation/self"]
    assert rules({**link, "via": "prob.a.p"}) == ["relation/mistyped-end"]
    assert rules({"question": "phen.a.g"}) == [
        "relation/misplaced-attribute",
        "relation/mistyped-end",
    ]
    assert rules(link, addresses="quest.a.p") == ["relation/mistyped-end"]


def test_a_cycle_through_several_relations_of_one_graph_is_found() -> None:
    """An answer supports another and rests on a model whose law requires the supported answer:
    one cycle of the graph of claims, through three relations. Each edge runs from the dependent
    end, so the supported answer depends on the supporting one."""
    records: dict[str, dict[str, Any]] = {
        "ans.a.x": {
            "id": "ans.a.x",
            "type": "answer",
            "relations": [{"relation": "supports", "target": "ans.a.y"}],
            "grounds": [{"record": "mod.a.m.law"}],
        },
        "ans.a.y": {"id": "ans.a.y", "type": "answer"},
        "mod.a.m": {
            "id": "mod.a.m",
            "type": "model",
            "laws": [{"symbol": "law", "requires": ["ans.a.y"]}],
        },
    }
    found = [f for _, f in workspace_relation_findings(records)]
    assert [f.rule.id for f in found] == ["relation/judged-cycle"]
    assert found[0].text == (
        "claims: ans.a.x -> mod.a.m -> ans.a.y -> ans.a.x, through grounds[].record,"
        " laws[].requires, supports"
    )


def test_the_relations_of_one_graph_share_a_policy_of_cycles() -> None:
    from gnomon.relation_registry import load_relation_registry

    registry = load_relation_registry()
    declared = [
        relation
        for family in (registry.get("entries") or {}).values()
        for relation in (family.get("relations") or {}).values()
    ] + [
        relation
        for fields in (registry.get("fields") or {}).values()
        for relation in fields.values()
    ]
    policies: dict[str, set[str]] = {}
    for relation in declared:
        if relation.get("graph"):
            policies.setdefault(relation["graph"], set()).add(relation.get("cycles"))
    assert policies and all(len(found) == 1 for found in policies.values()), policies


def test_a_support_that_restates_a_ground_is_a_warning() -> None:
    records = {
        **RECORDS,
        "ans.a.x": {
            **RECORDS["ans.a.x"],
            "relations": [{"relation": "supports", "target": "ans.a.y"}],
        },
    }
    assert workspace_relation_findings(records) == []
    records["ans.a.y"] = {
        **RECORDS["ans.a.y"],
        "grounds": [{"id": "part", "role": "warrant", "record": "ans.a.x"}],
    }
    found = [f for _, f in workspace_relation_findings(records)]
    assert [(f.rule.id, f.rule.level) for f in found] == [("relation/restated-ground", "warning")]
