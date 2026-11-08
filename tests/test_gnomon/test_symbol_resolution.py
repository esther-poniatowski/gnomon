"""Resolution of every symbol an inquiry record declares and every reference it makes.

A record declares each quantity under a ``symbol`` unique within that record, and names a
quantity by that symbol rather than by its name in words. The collecting logic lives in
``gnomon.vocabulary``; these tests exercise it on planted records and against the framework note.
The worked inquiries are checked in ``test_check.py``, through the context that ``gnomon check``
assembles.

The check is lexical. Identifiers are extracted from a formula without parsing its binders, so a
declared signature is not verified against the definition that would compute the signature. An
entry that names no declared set introduces an index local to its own quantity.
"""

from __future__ import annotations

import re
from pathlib import Path
from typing import Any, Mapping

import pytest
import yaml

from gnomon.completeness import (
    admitted_values,
    always_required,
    contradictory_accuracy,
    inadmissible_values,
    requirements_by_aim,
    requirements_by_commitment,
    undecided_boundaries,
    unjustified_explanans_bound,
    unmet_by_aim,
    unmet_commitment,
    unmet_general,
    unrealized_link,
    unstated_standing,
)
from gnomon.findings import texts
from gnomon.vocabulary import (
    RECORD_KINDS,
    arities,
    canonical_operators,
    corrupted_notation,
    declarations,
    doubly_defined,
    interaction_graph,
    load_problem,
    local_operators,
    malformed_relations,
    misattributed_appeals,
    mismatched_arity,
    misnamed_variant,
    misplaced_sharing,
    misrouted_interactions,
    mistyped_symbols,
    overreaching_declarations,
    overreaching_entries,
    render_yaml,
    split_expressions,
    unborne_variants,
    unfixed_parameters,
    unordered_interactions,
    unowned_quantities,
    unresolved,
    unselected_conditions,
    unused_declarations,
    upstream_of,
    vacuous_shared,
)

from .paths import EXAMPLES, ROOT

CANONICAL = canonical_operators()


def records() -> list[tuple[str, Mapping[str, Any]]]:
    """Return every instantiated case record, by its path relative to the repository."""
    if not EXAMPLES.is_dir():
        return []
    found = []
    for path in sorted(EXAMPLES.glob("*/*.yml")):
        loaded = yaml.safe_load(path.read_text(encoding="utf-8"))
        if isinstance(loaded, Mapping) and loaded.get("type") in RECORD_KINDS:
            found.append((str(path.relative_to(ROOT)), loaded))
    return found


CASES = records()
IDS = [name for name, _ in CASES] or ["no-fixture"]

#: Every fixture record of a checked kind, keyed by identifier.
BY_ID: dict[str, Mapping[str, Any]] = {str(r["id"]): r for _, r in CASES if "id" in r}


PROBLEMS = sorted(p for p in EXAMPLES.glob("*/") if p.is_dir()) if EXAMPLES.is_dir() else []


def test_a_yaml_keyword_used_as_a_symbol_is_reported() -> None:
    """``on`` is a YAML 1.1 boolean, so an unquoted symbol drawn from that set is not a string."""
    record = yaml.safe_load(
        "type: target-system\noperators:\n  - symbol: on\n    name: restriction\n"
    )
    assert record["operators"][0]["symbol"] is True
    assert texts(mistyped_symbols(record)) == ["operators: True is bool, not a symbol"]
    quoted = yaml.safe_load(
        'type: target-system\noperators:\n  - symbol: "on"\n    name: restriction\n'
    )
    assert mistyped_symbols(quoted) == []


def test_a_reference_to_a_missing_record_or_unit_is_reported() -> None:
    from gnomon.vocabulary import dangling_references

    records = {"mod.a.m": {"type": "model", "laws": [{"symbol": "onset"}]}}
    record = {
        "id": "ans.a.b",
        "route": {"runs_on": ["mod.a.m", "mod.a.x"]},
        "grounds": [{"record": "mod.a.m.drift"}],
    }
    assert texts(dangling_references(record, records)) == [
        "route.runs_on.1: no record carries the identifier mod.a.x; did you mean mod.a.m?",
        "grounds.0.record: mod.a.m declares no unit drift",
    ]


@pytest.mark.skipif(not PROBLEMS, reason="the expressivity fixtures are absent")
@pytest.mark.parametrize("directory", PROBLEMS, ids=[p.name for p in PROBLEMS] or ["none"])
def test_every_declared_operator_is_used_by_its_own_problem(directory: Path) -> None:
    """An operator a problem declares belongs to that problem, so a stale entry is reported."""
    problem = load_problem(directory)
    text = " ".join(path.read_text(encoding="utf-8") for path in directory.glob("*.yml"))
    unused = [
        op for op in problem.local if len(re.findall(rf"\b{re.escape(op)}(?:\b|_\{{)", text)) <= 1
    ]
    assert not unused, f"{directory.name}: declares {unused} without using them"


def test_a_factor_appeals_to_a_declared_external_system() -> None:
    """An answer may explain by the environment, and names which part of it it draws on."""
    target: dict[str, Any] = {
        "type": "target-system",
        "external_systems": [{"symbol": "decoder", "name": "the system reading the outputs"}],
        "variables": [{"symbol": "y", "of": "decoder", "signature": []}],
    }
    systems = {e["symbol"] for e in target["external_systems"]}
    answer: dict[str, Any] = {
        "type": "answer",
        "aim_block": {
            "explanation": {
                "factors": [
                    {"holds": "a linear decoder reads the outputs", "appeals_to": ["decoder"]}
                ]
            }
        },
    }
    assert misattributed_appeals(answer, systems) == []
    answer["aim_block"]["explanation"]["factors"][0]["appeals_to"] = ["y"]
    assert texts(misattributed_appeals(answer, systems)) == [
        "aim_block.explanation.factors.appeals_to: y is no external system of the target"
    ]


def test_an_answer_accounts_for_the_members_it_rests_on() -> None:
    """An answer resting on a quantity only some members carry accounts for those members.

    No answer record exists in the fixtures, so the rule is exercised here.
    """
    marked = {"R": "resource_explicit", "rho": "resource_explicit"}
    answer: dict[str, Any] = {
        "type": "answer",
        "laws": [{"symbol": "turnover", "expression": "diff(R, t) = G(N, R, rho)"}],
    }
    assert texts(overreaching_entries(answer, marked)) == [
        "laws.turnover: R is carried only by the resource_explicit variant",
        "laws.turnover: rho is carried only by the resource_explicit variant",
    ]
    answer["variant"] = "resource_explicit"
    assert overreaching_entries(answer, marked) == []
    answer["variant"] = "direct"
    assert len(overreaching_entries(answer, marked)) == 2
    del answer["variant"]
    answer["laws"][0]["variant"] = "resource_explicit"
    assert overreaching_entries(answer, marked) == []


def test_a_record_accounts_for_a_variant_the_target_declares() -> None:
    """A record naming a variant that does not exist would mark every entry of itself."""
    declared = {"resource_explicit", "direct"}
    assert misnamed_variant({"type": "answer", "variant": "direct"}, declared) == []
    assert misnamed_variant({"type": "answer"}, declared) == []
    assert texts(misnamed_variant({"type": "answer", "variant": "absent"}, declared)) == [
        "variant -> absent"
    ]
    nested = {
        "laws": [{"variant": "direct"}, {"variant": "absent"}],
        "c": {"d": [{"variant": "gone"}]},
    }
    assert texts(misnamed_variant(nested, declared)) == [
        "laws.variant -> absent",
        "c.d.variant -> gone",
    ]


def test_a_variant_named_in_prose_is_still_unborne() -> None:
    """The name of a variant recurs in its own prose, so the count is of what carries it."""
    record: dict[str, Any] = {
        "type": "target-system",
        "variants": [
            {
                "symbol": "lattice",
                "name": "lattice realization",
                "differentiation": "position runs over the sites of a lattice",
            }
        ],
        "variables": [{"symbol": "u", "variant": "continuum"}],
    }
    assert texts(unborne_variants(record)) == [
        "variants.lattice: no declaration or law carries it, and its maturity admits no gap"
    ]
    record["maturity"] = {"variants.lattice": "open"}
    assert unborne_variants(record) == []
    del record["maturity"]
    background = {
        "type": "background",
        "organization": [{"symbol": "coupling", "variant": "lattice"}],
    }
    assert (
        unborne_variants(record, [background]) == []
    )  # a relation carries a variant as a declaration does
    background["type"] = "phenomenon"
    assert len(unborne_variants(record, [background])) == 1  # only a block that declares counts


@pytest.mark.skipif(not CASES, reason="the expressivity fixtures are absent")
@pytest.mark.parametrize("case", CASES or [("", {})], ids=IDS)
def test_the_record_generates_a_directed_interaction_graph(
    case: tuple[str, Mapping[str, Any]],
) -> None:
    """Every edge the record states resolves to declared nodes and declared carriers."""
    name, record = case
    upstream = upstream_of(record, BY_ID)
    declared = {entry.symbol for entry in declarations(record) + declarations(upstream)}
    relations = {
        entry.get("symbol")
        for entry in record.get("organization") or []
        if isinstance(entry, Mapping)
    }
    kinds = {
        entry.get("symbol")
        for source in (record, upstream)
        for block in ("constituents", "index_sets")
        for entry in source.get(block) or []
        if isinstance(entry, Mapping)
    }
    for edge in interaction_graph(record, upstream):
        assert edge["edge"] in relations, f"{name}: {edge['edge']} is no relation of the record"
        for endpoint in edge["sources"] + [edge["reach"]]:
            assert endpoint in kinds, f"{name}: {endpoint} is no constituent kind or index set"
        for carrier in edge["through"]:
            assert carrier in declared, f"{name}: {carrier} is not declared"
        assert edge["tuples"], f"{name}: the edge {edge['edge']} names no ordered tuples"


#: A target with one constituent kind, whose quantity ``u`` joins two members and ``z`` indexes one.
PAIRED_TARGET: dict[str, Any] = {
    "type": "target-system",
    "constituents": [{"symbol": "sub"}],
    "variables": [
        {"symbol": "u", "signature": ["sub", "sub", "t"]},
        {"symbol": "z", "signature": ["sub", "t"]},
    ],
}


def test_an_influence_without_an_ordered_product_of_declared_kinds_is_reported() -> None:
    """The order of the tuples gives the direction of an influence, so each place is a declared
    kind."""
    record = {
        "type": "background",
        "organization": [
            {"symbol": "coupling", "relates": "prod(sub, sub)"},
            {"symbol": "loose", "relates": "Aij"},
            {"symbol": "stray", "relates": "prod(sub, pop)"},
            {"symbol": "order", "among": ["a", "b"]},
        ],
    }
    assert texts(unordered_interactions(record, PAIRED_TARGET)) == [
        "organization.loose: the relation names no ordered product of declared kinds",
        "organization.stray: the relation names no ordered product of declared kinds",
    ]
    # the kinds stand in the target, so a relation read without it names no declared kind
    assert (
        len(
            unordered_interactions(
                {"type": "background", "organization": record["organization"][:1]}
            )
        )
        == 1
    )


def test_an_interaction_whose_laws_name_no_quantity_of_both_endpoints_is_reported() -> None:
    """A law naming only a quantity of one member states a property of it, not an influence."""

    def background(expression: str) -> dict[str, Any]:
        return {
            "type": "background",
            "laws": [{"symbol": "transmit", "expression": expression}],
            "organization": [
                {"symbol": "coupling", "relates": "prod(sub, sub)", "realized_by": ["transmit"]}
            ],
        }

    assert misrouted_interactions(background("u = emit(z)"), PAIRED_TARGET) == []
    assert texts(misrouted_interactions(background("z = emit(z)"), PAIRED_TARGET)) == [
        "organization.coupling: the laws stating it name no quantity indexed by every one of"
        " ['sub', 'sub']"
    ]


def test_an_unmarked_entry_naming_a_symbol_of_one_variant_is_reported() -> None:
    """An entry without a variant holds of every member, so it cannot name what one variant alone
    carries."""
    target = {
        "type": "target-system",
        "variants": [{"symbol": "lattice"}],
        "constituents": [{"symbol": "cell"}, {"symbol": "site", "variant": "lattice"}],
        "variables": [{"symbol": "u"}, {"symbol": "w", "variant": "lattice"}],
        "laws": [
            {"symbol": "flow", "expression": "d_t(u) = -w"},
            {"symbol": "local", "expression": "d_t(w) = u", "variant": "lattice"},
        ],
        "external_systems": [{"symbol": "env", "shares": ["w"]}],
    }
    assert texts(overreaching_declarations(target)) == [
        "laws.flow: w is carried only by the lattice variant",
        "external_systems.env: w is carried only by the lattice variant",
    ]
    # a background reaches the variants of its target through the laws and the relations it states
    background = {
        "type": "background",
        "laws": [{"symbol": "drag", "expression": "d_t(u) = -w"}],
        "organization": [
            {"symbol": "link", "relates": "prod(site, site)"},
            {"symbol": "bulk", "relates": "prod(cell, cell)"},
        ],
    }
    assert texts(overreaching_declarations(background, target)) == [
        "laws.drag: w is carried only by the lattice variant",
        "organization.link: site is carried only by the lattice variant",
    ]


def test_a_call_passing_other_than_the_arity_of_its_operator_is_reported() -> None:
    """An operator whose signature lists its sets takes one argument per set; an open signature
    states none."""
    record = {
        "type": "target-system",
        "operators": [
            {"symbol": "ft", "signature": ["reals"]},
            {"symbol": "lift", "signature": "reals"},
        ],
        "laws": [{"symbol": "y", "expression": "y = ft(u, v) + ft(u) + lift(u, v)"}],
    }
    taken = arities(record)
    assert taken["ft"] == (1, False) and "lift" not in taken
    assert taken["interval"] == (2, False) and taken["enum"] == (1, True)
    assert texts(mismatched_arity(record, taken)) == [
        "laws.expression: ft takes 1 arguments and is passed 2"
    ]


def test_a_stated_arity_is_checked_and_a_variadic_operator_takes_more() -> None:
    """An operator that states its arity rather than a signature is checked too, and the last
    argument of a variadic operator repeats."""
    record = {
        "type": "target-system",
        "index_sets": [
            {"symbol": "t", "extent": "interval(reals)"},
            {"symbol": "s", "extent": "prod(reals, reals, reals)"},
            {"symbol": "k", "extent": "interval_of(reals)"},
        ],
    }
    assert texts(mismatched_arity(record, arities(record))) == [
        "index_sets.extent: interval takes 2 arguments and is passed 1"
    ]


def test_a_quantity_that_no_other_field_mentions_is_reported(tmp_path: Path) -> None:
    """Only a quantity meant to be reached is reported, and a generated symbol table does not reach
    it."""
    (tmp_path / "target-system.yml").write_text(
        yaml.safe_dump(
            {
                "id": "system.demo",
                "type": "target-system",
                "variables": [{"name": "used", "symbol": "u"}, {"name": "stray", "symbol": "w"}],
                "laws": [{"symbol": "decay", "expression": "d_t(u) = -u"}],
            }
        ),
        encoding="utf-8",
    )
    (tmp_path / "phenomenon.yml").write_text(
        yaml.safe_dump(
            {
                "id": "phen.demo.decay",
                "type": "phenomenon",
                "observables": [{"name": "terminal", "symbol": "obs"}],
            }
        ),
        encoding="utf-8",
    )
    (tmp_path / "vocabulary.yml").write_text(
        yaml.safe_dump(
            {
                "id": "vocab.demo",
                "type": "vocabulary",
                "symbols": [{"symbol": "w", "expression": "w"}],
                "variables": [{"symbol": "ghost"}],
            }
        ),
        encoding="utf-8",
    )
    found = unused_declarations(tmp_path)
    assert [(ident, f.text) for ident, f in found] == [
        ("system.demo", "variables.w: declared and never used")
    ]
    assert "ghost" not in load_problem(tmp_path).notations


def test_a_quantity_named_only_in_prose_is_reported(tmp_path: Path) -> None:
    """A prose field is opaque, so a symbol that only a name or a reading repeats is unused, and a
    dotted reference from another record is a use."""
    (tmp_path / "target-system.yml").write_text(
        yaml.safe_dump(
            {
                "id": "system.demo",
                "type": "target-system",
                "variables": [
                    {"name": "the variable w", "symbol": "w", "reading": "w decays"},
                    {"name": "the variable v", "symbol": "v"},
                ],
            }
        ),
        encoding="utf-8",
    )
    (tmp_path / "phenomenon.yml").write_text(
        yaml.safe_dump(
            {
                "id": "phen.demo.decay",
                "type": "phenomenon",
                "target_system": "system.demo",
                "data": [{"name": "record of v", "measures": "system.demo.v"}],
            }
        ),
        encoding="utf-8",
    )
    found = unused_declarations(tmp_path)
    assert [(ident, f.text) for ident, f in found] == [
        ("system.demo", "variables.w: declared and never used")
    ]


def test_a_shared_variable_naming_a_set_is_reported() -> None:
    """A set does not cross a boundary, so sharing one is reported."""
    record = {
        "type": "target-system",
        "index_sets": [{"symbol": "x"}],
        "variables": [{"symbol": "s"}],
        "external_systems": [{"name": "environment", "shares": ["s", "x"]}],
    }
    assert texts(misplaced_sharing(record)) == [
        "external_systems.shares: x is no declared quantity"
    ]


def test_a_parameter_running_along_an_interval_is_reported() -> None:
    """A parameter is held fixed, so a quantity indexed by an ordered continuum is exogenous."""
    record = {
        "type": "target-system",
        "index_sets": [
            {"symbol": "t", "structure": "evolution"},
            {"symbol": "i", "structure": "discrete-set"},
        ],
        "parameters": [{"symbol": "f", "signature": ["t"]}, {"symbol": "w", "signature": ["i"]}],
    }
    assert texts(unfixed_parameters(record)) == ["parameters.f: held fixed yet indexed by ['t']"]


def test_shared_without_a_signature_is_reported() -> None:
    record = {
        "type": "target-system",
        "parameters": [
            {"symbol": "nu", "signature": [], "shared": True},
            {"symbol": "w", "signature": ["i"], "shared": True},
        ],
    }
    assert texts(vacuous_shared(record)) == ["parameters.nu: shared without a signature"]


def test_a_quantity_carrying_both_an_expression_and_a_condition_is_reported() -> None:
    """One builds the quantity and cannot be false; the other presupposes that a value exists."""
    record = {
        "type": "phenomenon",
        "observables": [
            {"symbol": "a", "expression": "min_{i}( N(i) )", "condition": "d_t(N) = 0"},
            {"symbol": "b", "condition": "d_t(N) = 0"},
        ],
    }
    assert texts(doubly_defined(record)) == ["observables.a: both an expression and a condition"]


def test_a_quantity_owned_by_no_declared_system_is_reported() -> None:
    """A quantity characterizes the target unless it names an external system that exists."""
    record = {
        "type": "target-system",
        "external_systems": [{"symbol": "bath", "name": "heat bath"}],
        "parameters": [
            {"symbol": "T", "of": "bath"},
            {"symbol": "g", "of": "furnace"},
            {"symbol": "nu"},
        ],
    }
    assert texts(unowned_quantities(record)) == ["parameters.g: no external system named furnace"]


def test_a_condition_without_a_selection_rule_is_reported() -> None:
    """A condition may hold of several values, so the record says which one it denotes."""
    record = {
        "type": "phenomenon",
        "observables": [
            {"symbol": "a", "condition": "d_t(N) = 0"},
            {"symbol": "b", "condition": "d_t(N) = 0", "selects": "any"},
        ],
    }
    assert texts(unselected_conditions(record)) == [
        "observables.a: a condition without a selection rule"
    ]


REQUIRED = requirements_by_aim()


REQUIRED_BY_COMMITMENT = requirements_by_commitment()


def produced_for(aim: str, kind: str) -> set[str]:
    """Return the paths of ``kind`` that ``aim`` produces, with the record prefix stripped."""
    entry = REQUIRED.get(aim) or {}
    return {p.split(".", 1)[1] for p in entry.get("to_produce", []) if p.startswith(f"{kind}.")}


def test_a_design_carries_what_its_kind_requires() -> None:
    """An experiment or a simulation run states its protocol; a method needs none."""
    from gnomon.completeness import requirements_by_value, unmet_by_value

    table = requirements_by_value()
    design = yaml.safe_load(
        (EXAMPLES / "active-matter-phase-exploration" / "design.yml").read_text()
    )
    assert unmet_by_value(design, table) == []
    bare = {key: value for key, value in design.items() if key != "protocol"}
    assert texts(unmet_by_value(bare, table)) == ["kind simulation-run requires: protocol"]
    assert unmet_by_value({**bare, "kind": "method"}, table) == []


def test_a_record_lacking_what_its_commitment_requires_is_reported() -> None:
    """The levels are cumulative, so a specified record also carries what identification needs."""
    phenomenon = {
        "type": "phenomenon",
        "commitment": "identified",
        "statement": "A behavior.",
        "identification": {"description": "the behavior", "pointers": []},
    }
    assert unmet_commitment(phenomenon, REQUIRED_BY_COMMITMENT) == []
    phenomenon["commitment"] = "specified"
    assert texts(unmet_commitment(phenomenon, REQUIRED_BY_COMMITMENT)) == [
        "commitment specified requires: category",
        "commitment specified requires: course",
        "commitment specified requires: occurrence",
        "commitment specified requires: manifestations",
        "commitment specified requires: evidential_status",
    ]
    del phenomenon["identification"]
    phenomenon["commitment"] = "identified"
    assert texts(unmet_commitment(phenomenon, REQUIRED_BY_COMMITMENT)) == [
        "commitment identified requires: identification"
    ]
    target = {
        "type": "target-system",
        "commitment": "specified",
        "target_type": "particular",
        "reference_class": {"name": "a basin"},
        "identification": {"description": "the basin"},
    }
    assert texts(unmet_commitment(target, REQUIRED_BY_COMMITMENT)) == [
        "commitment specified requires: variables"
    ]


def test_a_record_stating_no_commitment_is_reported() -> None:
    assert texts(
        unmet_general({"type": "phenomenon", "commitment": None}, always_required("phenomenon"))
    ) == ["always required: commitment"]


def test_an_empty_value_leaves_a_required_specification_unfilled() -> None:
    """Null, an empty string and an empty block are unfilled; `open` is an ordinary value now."""
    paths = ["statement", "category", "manifestations"]
    record: dict[str, Any] = {
        "type": "phenomenon",
        "statement": None,
        "category": "",
        "manifestations": [],
    }
    assert texts(unmet_general(record, paths)) == [
        "always required: statement",
        "always required: category",
        "always required: manifestations",
    ]
    record.update(statement="open", category="regularity", manifestations=[{"form": "value"}])
    assert unmet_general(record, paths) == []


def test_a_path_that_the_aim_produces_may_stay_empty() -> None:
    """The registry, not the record, says whether an empty field is a gap or a product."""
    record = {"type": "phenomenon", "statement": None, "category": None}
    assert texts(unmet_general(record, ["statement", "category"], {"statement"})) == [
        "always required: category"
    ]
    produced = produced_for("exploration", "phenomenon")
    assert {"statement", "category", "occurrence", "evidential_status"} <= produced
    assert produced_for("explanation", "phenomenon") == set()


def test_an_empty_boundary_is_reported_and_an_empty_list_is_not() -> None:
    """An empty value leaves the boundary undecided; `[]` states that it imposes nothing."""
    record = {
        "external_systems": [
            {"symbol": "bath", "constrains": None},
            {"symbol": "decoder", "constrains": []},
        ]
    }
    assert texts(undecided_boundaries(record)) == [
        "external_systems.bath: constrains is empty, so the boundary is named without being decided"
    ]


def test_a_stated_axis_without_justification_is_reported() -> None:
    """An empty bound takes the default; a stated axis needs a justification or an open maturity."""
    empty = {"task": {"admissible_explanans": {"compositional": None, "substrate": None}}}
    assert unjustified_explanans_bound(empty) == []
    assert unjustified_explanans_bound({"task": {}}) == []
    bounded = {"task": {"admissible_explanans": {"compositional": ["sub"], "substrate": None}}}
    assert len(unjustified_explanans_bound(bounded)) == 1
    whole: dict[str, Any] = {
        "task": {"admissible_explanans": {"compositional": [], "substrate": None}}
    }
    assert unjustified_explanans_bound(whole) == unjustified_explanans_bound(bounded)
    substrate = {
        "task": {"admissible_explanans": {"compositional": None, "substrate": "independent"}}
    }
    assert len(unjustified_explanans_bound(substrate)) == 1
    reason = "the forecast names each part"
    justified = {
        "task": {"admissible_explanans": {"compositional": ["sub"], "justification": reason}}
    }
    assert unjustified_explanans_bound(justified) == []
    unsettled = dict(bounded, maturity={"task.admissible_explanans": "open"})
    assert unjustified_explanans_bound(unsettled) == []


def test_a_question_asking_for_a_link_needs_the_mapping() -> None:
    """Neither description answers how a role is realized, so the answer states the mapping."""
    question = {"task": {"admissible_explanans": {"substrate": "mapping"}}}
    assert texts(unrealized_link(question, {})) == [
        "the question asks for a link, and the answer maps no quantity onto its realization"
    ]
    assert (
        unrealized_link({"task": {"admissible_explanans": {"substrate": "independent"}}}, {}) == []
    )
    half = {"claim": {"realizations": [{"id": "gate", "realizes": "role"}]}}
    assert texts(unrealized_link(question, half)) == [
        "claim.realizations[0] names what it realizes without saying by what"
    ]
    whole = {"claim": {"realizations": [{"id": "gate", "realizes": "role", "by": "g * (v - e)"}]}}
    assert unrealized_link(question, whole) == []


def test_a_relation_of_the_organization_says_what_its_ends_are() -> None:
    """A relation runs between parts or between laws, and nothing carries a law-ended one."""
    record = {
        "type": "target-system",
        "laws": [{"symbol": "draw"}, {"symbol": "update"}],
        "organization": [{"symbol": "precedes", "among": ["draw", "update"]}],
    }
    assert malformed_relations(record) == []
    record["organization"] = [
        {"symbol": "both", "relates": "prod(a, b)", "among": ["draw", "update"]}
    ]
    assert texts(malformed_relations(record)) == [
        "organization.both: a relation runs between parts or between laws, and this one names both"
    ]
    record["organization"] = [{"symbol": "neither"}]
    assert texts(malformed_relations(record)) == [
        "organization.neither: a relation runs between parts or between laws, and this one names"
        " neither"
    ]
    record["organization"] = [{"symbol": "lone", "among": ["draw"]}]
    assert texts(malformed_relations(record)) == [
        "organization.lone: a relation among laws orders two or more of them"
    ]
    record["organization"] = [{"symbol": "stray", "among": ["draw", "absent"]}]
    assert texts(malformed_relations(record)) == [
        "organization.stray: absent is no law of the record"
    ]


def test_a_virtue_weighed_without_a_standing_is_reported() -> None:
    """A virtue with no standing leaves the product test unable to say what it applies."""
    question = {
        "virtues": [
            {"virtue": "economy", "standing": "preferred"},
            {"virtue": "tractability"},
            {"justification": "an entry that never named its virtue"},
        ]
    }
    assert texts(unstated_standing(question)) == [
        "virtues[1].standing is unstated for tractability",
        "virtues[2].standing is unstated for an unnamed virtue",
    ]
    assert unstated_standing({}) == []


def test_a_match_listed_under_an_inapplicable_accuracy_is_reported() -> None:
    """Whether an answer is matched against a measurement is a consistency between fields."""
    question = {
        "task": {
            "required_accuracy": {
                "standard": "not-applicable",
                "outputs_to_match": [{"model_output": "an exponent"}],
                "structures_to_match": [],
            }
        }
    }
    assert texts(contradictory_accuracy(question)) == [
        "task.required_accuracy.outputs_to_match is listed although accuracy does not apply"
    ]
    question["task"]["required_accuracy"]["standard"] = "numeric-bound"
    assert contradictory_accuracy(question) == []


def test_a_tolerance_stated_under_a_standard_that_fixes_its_own_is_reported() -> None:
    """The standard order-of-magnitude fixes its metric and bound, so a stated tolerance contradicts
    it."""
    entry = {
        "target": "an exponent",
        "tolerance": {"metric": "abs(answer - target)", "bound": "0.1"},
    }
    question = {
        "task": {
            "required_accuracy": {"standard": "order-of-magnitude", "outputs_to_match": [entry]}
        }
    }
    assert texts(contradictory_accuracy(question)) == [
        "task.required_accuracy.outputs_to_match: a tolerance is stated although the standard"
        " order-of-magnitude admits none"
    ]
    question["task"]["required_accuracy"]["standard"] = "numeric-bound"
    assert contradictory_accuracy(question) == []


def test_the_requirement_table_is_read_from_the_registry() -> None:
    assert REQUIRED["exploration"]["required"] == ["phenomenon.detection_criterion"]
    assert REQUIRED["explanation"]["required"] == ["question.task.requested_relation"]
    assert REQUIRED["description"] == {"required": [], "to_produce": []}
    assert "phenomenon.category" in REQUIRED["exploration"]["to_produce"]
    assert REQUIRED["prediction"]["to_produce"] == []
    assert REQUIRED_BY_COMMITMENT["identified"]["target-system"] == [
        "target_type",
        "identification",
        "reference_class",
    ]
    assert always_required("background") == ["describes", "laws", "closure"]


def test_a_registry_naming_an_unknown_level_is_reported(tmp_path: Path) -> None:
    source = tmp_path / "requirements.yml"
    source.write_text(
        "by_commitment:\n  sketched:\n    phenomenon: [statement]\n", encoding="utf-8"
    )
    with pytest.raises(ValueError, match="unknown levels of commitment"):
        requirements_by_commitment(source)


def test_an_inquiry_leaving_a_required_specification_open_is_reported() -> None:
    """A prediction compares an output against a measurement, so it fixes what must match."""
    question = {
        "task": {"epistemic_aim": "prediction", "required_accuracy": {"outputs_to_match": []}}
    }
    records: dict[str, dict[str, Any]] = {
        "question": question,
        "phenomenon": {"manifestations": []},
    }
    assert texts(unmet_by_aim(question, records, REQUIRED)) == [
        "prediction requires phenomenon.manifestations",
        "prediction requires question.task.required_accuracy.outputs_to_match",
    ]


def test_a_value_outside_its_vocabulary_is_reported() -> None:
    """A value outside a closed field's vocabulary passed every check before the registry existed.

    ``no-such-role`` is a deliberate sentinel rather than a typo awaiting correction: replacing it
    with an admitted value would leave the check unable to fail.
    """
    admitted = admitted_values("background")
    record: dict[str, Any] = {
        "type": "background",
        "laws": [{"role": "no-such-role"}, {"role": "state-constraint"}],
    }
    assert texts(inadmissible_values(record, admitted)) == [
        "laws.role: no-such-role is not admitted; the admitted values are admissibility,"
        " distribution, evolution, input-output, measurement, state-constraint"
    ]
    record["laws"][0]["role"] = "open"  # no longer a sentinel: an ordinary value, and not this one
    assert texts(inadmissible_values(record, admitted)) == [
        "laws.role: open is not admitted; the admitted values are admissibility, distribution,"
        " evolution, input-output, measurement, state-constraint"
    ]
    record["laws"][0]["role"] = None  # an empty field holds no value, so no vocabulary bears on it
    assert inadmissible_values(record, admitted) == []


def test_a_record_field_is_read_apart_from_a_field_of_the_same_name() -> None:
    """A record field and an entry field may share a name, under separate vocabularies.

    The rule is stated against a vocabulary written here: a collision of names must not let one
    lookup answer for the other.
    """
    admitted = {
        "status": frozenset({"draft"}),
        "terms.status": frozenset({"load-bearing"}),
    }
    record = {"status": "no-such-state", "terms": [{"status": "no-such-status"}]}
    assert texts(inadmissible_values(record, admitted)) == [
        "status: no-such-state is not admitted; the admitted values are draft",
        "terms.status: no-such-status is not admitted; the admitted values are load-bearing",
    ]


def test_two_fields_of_one_block_that_share_a_name_take_the_vocabulary_of_their_own_path() -> None:
    """In an answer, the kind of an explanatory factor is closed, and a varied factor holds a
    symbol.

    Both fields are named ``factor`` inside the block ``aim_block``, so a lookup by block and name
    would check the symbol against the kinds of a factor.
    """
    admitted = admitted_values("answer")
    assert "aim_block.explanation.factors.factor" in admitted
    assert "aim_block.exploration.space.varied.factor" not in admitted
    record = {
        "type": "answer",
        "aim_block": {
            "exploration": {"space": {"varied": [{"factor": "g", "range": "[0, 2]"}]}},
            "explanation": {"factors": [{"factor": "no-such-kind"}, {"factor": "condition"}]},
        },
    }
    assert texts(inadmissible_values(record, admitted)) == [
        "aim_block.explanation.factors.factor: no-such-kind is not admitted; the admitted values"
        " are condition, law-property, organization, structural-property",
    ]


def test_an_expression_split_on_its_commas_is_reported() -> None:
    """An unquoted expression inside a bracketed list splits into plausible fragments.

    The record below is what ``signature: [maps(prod(a, b), reals)]`` parses to.
    """
    record = {
        "type": "target-system",
        "operators": [{"symbol": "f", "signature": ["maps(prod(a", "b)", "reals)"]}],
    }
    assert texts(split_expressions(record)) == [
        "operators.signature: 'maps(prod(a' is a fragment of a split expression",
        "operators.signature: 'b)' is a fragment of a split expression",
        "operators.signature: 'reals)' is a fragment of a split expression",
    ]


def test_a_latex_form_in_double_quotes_is_reported() -> None:
    """A double-quoted scalar reads the backslash of a LaTeX command as an escape."""
    damaged = yaml.safe_load('parameters:\n  - symbol: nu\n    notation: "\\nu"\n')
    damaged["type"] = "target-system"
    assert texts(corrupted_notation(damaged)) == [
        "parameters.nu: the notation holds a control character"
    ]
    intact = yaml.safe_load("parameters:\n  - symbol: nu\n    notation: '\\nu'\n")
    intact["type"] = "target-system"
    assert corrupted_notation(intact) == []


def test_a_condition_of_the_phenomenon_is_checked() -> None:
    """A precipitating condition is an expression, so an undeclared symbol in it is reported."""
    record = {
        "type": "phenomenon",
        "observables": [{"symbol": "Y", "signature": []}],
        "conditions_and_byproducts": {
            "precipitating": [{"expression": "Y > no_such_symbol"}],
            "inhibiting": [],
        },
    }
    assert texts(unresolved(record, CANONICAL)) == [
        "conditions_and_byproducts.precipitating.expression -> no_such_symbol"
    ]


def test_the_canonical_vocabulary_comes_from_the_registry() -> None:
    """The framework set is read from package data, so no check depends on a document."""
    assert {"mean", "min", "max", "sum", "dist"} <= CANONICAL  # binders
    assert {"implies", "depends_on"} <= CANONICAL  # relations
    assert "far_field" not in CANONICAL  # a problem declares its own
    assert "Ltrain" not in CANONICAL  # a quantity is not an operator


def test_a_registry_declaring_no_operator_is_reported(tmp_path: Path) -> None:
    """Reading fails loudly when the registry carries no operator."""
    empty = tmp_path / "operators.yml"
    empty.write_text(
        "id: registry.operators\ntype: operator-registry\noperators: []\n", encoding="utf-8"
    )
    with pytest.raises(ValueError, match="declares no operator"):
        canonical_operators(empty)


def test_a_formula_naming_an_undeclared_symbol_is_reported() -> None:
    """The breakage prose names carried: a forcing term used by a law but declared nowhere."""
    record = {
        "type": "target-system",
        "index_sets": [{"symbol": "x"}],
        "variables": [{"symbol": "u", "signature": ["x"]}],
        "parameters": [{"symbol": "nu", "values": "pos(reals)"}],
        "laws": [{"expression": "diff(u, x) = nu * lap(u) + f", "signature": ["x"]}],
        "operators": [{"symbol": "lap", "name": "the Laplacian"}],
    }
    assert texts(unresolved(record, CANONICAL)) == ["laws.expression -> f"]


def test_a_binder_ranges_over_a_declared_index_set() -> None:
    """A binder index names a declared index set, with or without a restriction, or a fresh name
    introduced over a declared index set; any other index is reported."""
    record = {
        "type": "target-system",
        "index_sets": [{"symbol": "x"}, {"symbol": "t"}],
        "variables": [{"symbol": "u", "signature": ["x", "t"]}],
        "parameters": [{"symbol": "T"}],
        "laws": [
            {"expression": "sum_{zz}( u ) = 0"},
            {"expression": "max_{t <= T}( mean_{x}( u(x, t) ) ) = 0"},
            {"expression": "mean_{x1 in x, x2 in x}( u(x1, t) * u(x2, t) ) = 0"},
        ],
    }
    assert texts(unresolved(record, CANONICAL)) == ["laws.expression -> zz"]


def test_prose_left_in_a_value_set_is_reported() -> None:
    """A value set is an expression, so a description left there is no expression of the grammar,
    reported once rather than word by word."""
    record = {
        "type": "target-system",
        "parameters": [{"symbol": "nu", "values": "admissible body-force families"}],
    }
    found = unresolved(record, CANONICAL)
    assert texts(found) == [
        "parameters.values: admissible body-force families is no expression of the grammar"
        ", which docs/specification/expressions.md states"
    ]
    assert [f.rule.id for f in found] == ["vocabulary/unparsed-expression"]


def test_prose_in_a_nested_feature_value_set_is_reported() -> None:
    """A value set is checked wherever it occurs, including inside a manifestation feature."""
    record = {
        "type": "phenomenon",
        "manifestations": [{"features": [{"symbol": "a", "values": "prose left here"}]}],
    }
    assert texts(unresolved(record, CANONICAL)) == [
        "manifestations.features.values: prose left here is no expression of the grammar"
        ", which docs/specification/expressions.md states"
    ]


def test_a_set_expression_resolves() -> None:
    """The set constructors are canonical, so a well-formed value set reports nothing."""
    record = {
        "type": "target-system",
        "index_sets": [{"symbol": "x", "extent": "interval(reals)"}],
        "parameters": [{"symbol": "nu", "values": "maps(x, vectors(reals, 3))"}],
    }
    assert unresolved(record, CANONICAL) == []


def test_an_operator_the_record_does_not_declare_is_reported() -> None:
    """An operator outside the canonical set resolves only where the record declares it."""
    record: dict[str, Any] = {
        "type": "phenomenon",
        "observables": [
            {"symbol": "a", "expression": "max( re( far_field(J) ) )", "signature": []}
        ],
    }
    assert texts(unresolved(record, CANONICAL)) == [
        "observables.expression -> J",
        "observables.expression -> far_field; an operator is declared in the operator record of"
        " the problem",
    ]
    record["operators"] = [{"symbol": "far_field", "name": "the far-field limit of a profile"}]
    assert texts(unresolved(record, CANONICAL)) == ["observables.expression -> J"]


def test_a_reference_to_an_undeclared_set_is_reported() -> None:
    """Every signature entry names a declared set, so an undeclared index is reported too."""
    record = {
        "type": "target-system",
        "index_sets": [{"symbol": "x"}],
        "variables": [{"symbol": "u", "signature": ["x", "undeclared_index"]}],
        "laws": [{"expression": "u = u", "signature": ["y"]}],
    }
    assert texts(unresolved(record, CANONICAL)) == [
        "variables.signature -> undeclared_index",
        "laws.signature -> y",
    ]


def test_local_operators_are_read_from_the_record() -> None:
    record = {"operators": [{"symbol": "ft", "name": "Fourier transform"}]}
    assert local_operators(record) == {"ft": "Fourier transform"}


@pytest.mark.skipif(not PROBLEMS, reason="the expressivity fixtures are absent")
def test_a_problem_stores_its_vocabulary_as_a_record() -> None:
    problem = load_problem(PROBLEMS[0])
    data = yaml.safe_load(render_yaml(problem))
    assert data["type"] == "vocabulary"
    assert {e["symbol"] for e in data["symbols"]} == {d.symbol for d in problem.declarations}
    assert set(data["operators"]["canonical"]) == set(problem.canonical)


def test_an_empty_formula_is_skipped_and_open_is_an_unresolved_identifier() -> None:
    """With no sentinel left, `open` in an expression is a word that resolves to no declaration."""
    record = {
        "type": "target-system",
        "parameters": [{"symbol": "nu", "values": None}, {"symbol": "mu", "values": "open"}],
    }
    assert texts(unresolved(record, CANONICAL)) == ["parameters.values -> open"]
