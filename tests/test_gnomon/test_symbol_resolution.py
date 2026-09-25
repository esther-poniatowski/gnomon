"""Resolution of every symbol an inquiry record declares and every reference it makes.

A record declares each quantity under a ``symbol`` unique within that record, and names a
quantity by that symbol rather than by its name in words. The collecting logic lives in
``gnomon.vocabulary``; these tests exercise it against the framework note and the filled records.

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
    inadmissible_values,
    malformed_restrictions,
    contradictory_accuracy,
    record_kinds,
    requirements_by_aim,
    unmet_by_aim,
    undecided_boundaries,
    undeclared_explanans_bound,
    unrealized_link,
    unstated_standing,
    unmet_general,
)

from gnomon.vocabulary import (
    RECORD_KINDS,
    canonical_operators,
    declarations,
    doubly_defined,
    load_problem,
    local_operators,
    corrupted_notation,
    misplaced_sharing,
    split_expressions,
    unfixed_parameters,
    interaction_graph,
    declared_variants,
    malformed_relations,
    misattributed_appeals,
    misnamed_variant,
    misrouted_interactions,
    arities,
    mismatched_arity,
    unordered_interactions,
    unborne_variants,
    overreaching_entries,
    overreaching_declarations,
    variant_symbols,
    unselected_conditions,
    unused_declarations,
    unowned_quantities,
    mistyped_symbols,
    vacuous_shared,
    render_markdown,
    render_yaml,
    unresolved,
)

ROOT = Path(__file__).resolve().parents[2]
FIXTURES = ROOT / "test"
CANONICAL = canonical_operators()


def records() -> list[tuple[str, Mapping[str, Any]]]:
    """Return every instantiated case record, by its path relative to the repository."""
    if not FIXTURES.is_dir():
        return []
    found = []
    for path in sorted(FIXTURES.glob("*/*.yml")):
        loaded = yaml.safe_load(path.read_text(encoding="utf-8"))
        if isinstance(loaded, Mapping) and loaded.get("type") in RECORD_KINDS:
            found.append((str(path.relative_to(ROOT)), loaded))
    return found


def symbols_of(record: Mapping[str, Any]) -> list[str]:
    """Return the symbols the record declares, repetitions kept."""
    return [entry.symbol for entry in declarations(record)]


CASES = records()
IDS = [name for name, _ in CASES] or ["no-fixture"]


def problem_of(name: str) -> str:
    """Return the directory whose records make up one problem."""
    return str(Path(name).parent)


#: Per problem, the operators every one of its records may use, and every symbol they declare.
PROBLEM_OPERATORS: dict[str, set[str]] = {}
PROBLEM_SYMBOLS: dict[str, list[str]] = {}
for _name, _record in CASES:
    PROBLEM_OPERATORS.setdefault(problem_of(_name), set()).update(local_operators(_record))
    PROBLEM_SYMBOLS.setdefault(problem_of(_name), []).extend(symbols_of(_record))
PROBLEMS = sorted(p for p in FIXTURES.glob("*/") if p.is_dir()) if FIXTURES.is_dir() else []


@pytest.mark.skipif(not CASES, reason="the expressivity fixtures are absent")
@pytest.mark.parametrize("case", CASES or [("", {})], ids=IDS)
def test_every_symbol_resolved_to_a_string(case: tuple[str, Mapping[str, Any]]) -> None:
    name, record = case
    assert not mistyped_symbols(record), f"{name}: {mistyped_symbols(record)}"


def test_a_yaml_keyword_used_as_a_symbol_is_reported() -> None:
    """``on`` is a YAML 1.1 boolean, so an unquoted symbol drawn from that set is not a string."""
    record = yaml.safe_load("type: target-system\noperators:\n  - symbol: on\n    name: restriction\n")
    assert record["operators"][0]["symbol"] is True
    assert mistyped_symbols(record) == ["operators: True is bool, not a symbol"]
    quoted = yaml.safe_load('type: target-system\noperators:\n  - symbol: "on"\n    name: restriction\n')
    assert mistyped_symbols(quoted) == []


@pytest.mark.skipif(not CASES, reason="the expressivity fixtures are absent")
@pytest.mark.parametrize("case", CASES or [("", {})], ids=IDS)
def test_no_symbol_is_declared_twice(case: tuple[str, Mapping[str, Any]]) -> None:
    name, record = case
    found = symbols_of(record)
    repeated = sorted({s for s in found if found.count(s) > 1})
    assert not repeated, f"{name}: {repeated} declared more than once"


@pytest.mark.skipif(not CASES, reason="the expressivity fixtures are absent")
@pytest.mark.parametrize("case", CASES or [("", {})], ids=IDS)
def test_every_reference_and_formula_identifier_resolves(case: tuple[str, Mapping[str, Any]]) -> None:
    name, record = case
    targets = {r["id"]: r for _, r in CASES if r.get("type") == "target-system"}
    upstream = targets.get(record.get("target_system", ""), {})
    # an operator is typed over the sets of its whole problem, so it reads against all of them
    # an operator and a question are both read against the whole problem: the first is typed over
    # whatever set declares it, the second reaches the target and the phenomenon alike
    external = (
        PROBLEM_SYMBOLS[problem_of(name)]
        if record.get("type") in ("operators", "question")
        else symbols_of(upstream)
    )
    inherited = CANONICAL | frozenset(PROBLEM_OPERATORS[problem_of(name)])
    problems = unresolved(record, inherited, external)
    assert not problems, f"{name}: {problems}"


def external_references() -> list[tuple[str, str]]:
    """Return every ``record-id#symbol`` reference of the fixture tree, with the file making it."""
    found: list[tuple[str, str]] = []
    if not FIXTURES.is_dir():
        return found
    for path in sorted(FIXTURES.glob("*/*.yml")):
        for text in re.findall(r"[A-Za-z][\w.-]*#\w+", path.read_text(encoding="utf-8")):
            found.append((str(path.relative_to(ROOT)), text))
    return sorted(set(found))


EXTERNAL = external_references()


@pytest.mark.skipif(not EXTERNAL, reason="no cross-record reference is made")
@pytest.mark.parametrize("reference", EXTERNAL, ids=[f"{n}:{r}" for n, r in EXTERNAL] or ["none"])
def test_every_cross_record_reference_resolves(reference: tuple[str, str]) -> None:
    name, text = reference
    record_id, symbol = text.split("#", 1)
    by_id = {r["id"]: r for _, r in CASES if "id" in r}
    assert record_id in by_id, f"{name}: no record carries the identifier {record_id}"
    assert symbol in symbols_of(by_id[record_id]), f"{name}: {record_id} declares no symbol {symbol}"


@pytest.mark.skipif(not PROBLEMS, reason="the expressivity fixtures are absent")
@pytest.mark.parametrize("directory", PROBLEMS, ids=[p.name for p in PROBLEMS] or ["none"])
def test_every_declared_operator_is_used_by_its_own_problem(directory: Path) -> None:
    """An operator a problem declares belongs to that problem, so a stale entry is reported."""
    problem = load_problem(directory)
    text = " ".join(path.read_text(encoding="utf-8") for path in directory.glob("*.yml"))
    unused = [op for op in problem.local if len(re.findall(rf"\b{re.escape(op)}(?:\b|_\{{)", text)) <= 1]
    assert not unused, f"{directory.name}: declares {unused} without using them"


@pytest.mark.skipif(not PROBLEMS, reason="the expressivity fixtures are absent")
@pytest.mark.parametrize("directory", PROBLEMS, ids=[p.name for p in PROBLEMS] or ["none"])
def test_every_declared_quantity_is_reached_by_its_own_problem(directory: Path) -> None:
    """A quantity nothing reaches is a stray declaration, or a law the record never wrote."""
    unused = unused_declarations(directory)
    assert not unused, f"{directory.name}: {unused}"


@pytest.mark.skipif(not CASES, reason="the expressivity fixtures are absent")
@pytest.mark.parametrize("case", CASES or [("", {})], ids=IDS)
def test_every_restriction_says_what_it_holds(case: tuple[str, Mapping[str, Any]]) -> None:
    """A restriction holds one quantity to a set, or states the expression it holds under."""
    name, record = case
    if record.get("type") != "question":
        return
    targets = {r["id"]: r for _, r in CASES if r.get("type") == "target-system"}
    upstream = targets.get(record.get("subject", {}).get("target_system", ""), {})
    varying = {
        entry.get("symbol")
        for entry in upstream.get("variables") or []
        if isinstance(entry, Mapping)
    }
    malformed = malformed_restrictions(record, varying)
    assert not malformed, f"{name}: {malformed}"


@pytest.mark.skipif(not CASES, reason="the expressivity fixtures are absent")
@pytest.mark.parametrize("case", CASES or [("", {})], ids=IDS)
def test_every_external_system_decides_what_it_imposes(case: tuple[str, Mapping[str, Any]]) -> None:
    """A boundary left open reads like one that imposes nothing, so the field is never open."""
    name, record = case
    undecided = undecided_boundaries(record)
    assert not undecided, f"{name}: {undecided}"


@pytest.mark.skipif(not CASES, reason="the expressivity fixtures are absent")
@pytest.mark.parametrize("case", CASES or [("", {})], ids=IDS)
def test_every_interaction_runs_along_ordered_pairs(case: tuple[str, Mapping[str, Any]]) -> None:
    """The direction of an influence is the order of its pairs, so the pairs name two kinds."""
    name, record = case
    unordered = unordered_interactions(record)
    assert not unordered, f"{name}: {unordered}"


@pytest.mark.skipif(not CASES, reason="the expressivity fixtures are absent")
@pytest.mark.parametrize("case", CASES or [("", {})], ids=IDS)
def test_no_entry_ranges_beyond_the_members_that_bear_it(
    case: tuple[str, Mapping[str, Any]],
) -> None:
    """Only a target declares variants, so which members carry a symbol reaches a record upstream.

    An answer reaches its target through its question, and a phenomenon names it directly; the
    records of one problem share one target, so the problem locates it for either kind.
    """
    name, record = case
    if record.get("type") not in ("phenomenon", "answer"):
        return
    overreaching = overreaching_entries(record, variant_symbols(PROBLEM_TARGETS[problem_of(name)]))
    assert not overreaching, f"{name}: {overreaching}"


@pytest.mark.skipif(not CASES, reason="the expressivity fixtures are absent")
@pytest.mark.parametrize("case", CASES or [("", {})], ids=IDS)
def test_every_variant_mark_names_a_variant_the_target_declares(
    case: tuple[str, Mapping[str, Any]],
) -> None:
    """Only a target declares the variants, and every record of its problem marks against them."""
    name, record = case
    misnamed = misnamed_variant(record, declared_variants(PROBLEM_TARGETS[problem_of(name)]))
    assert not misnamed, f"{name}: {misnamed}"


#: Per problem, the target system its other records declare their quantities against.
PROBLEM_TARGETS: dict[str, Mapping[str, Any]] = {
    problem_of(name): record for name, record in CASES if record.get("type") == "target-system"
}


#: Per problem, the number of arguments each operator it may use takes.
PROBLEM_ARITIES: dict[str, dict[str, int]] = {
    problem_of(name): arities(*[r for n, r in CASES if problem_of(n) == problem_of(name)])
    for name, _ in CASES
}


@pytest.mark.skipif(not CASES, reason="the expressivity fixtures are absent")
@pytest.mark.parametrize("case", CASES or [("", {})], ids=IDS)
def test_every_call_passes_what_its_operator_takes(case: tuple[str, Mapping[str, Any]]) -> None:
    """An operator states what it takes, so a call passing more or fewer is reported."""
    name, record = case
    mismatched = mismatched_arity(record, PROBLEM_ARITIES[problem_of(name)])
    assert not mismatched, f"{name}: {mismatched}"


@pytest.mark.skipif(not CASES, reason="the expressivity fixtures are absent")
@pytest.mark.parametrize("case", CASES or [("", {})], ids=IDS)
def test_every_variant_is_carried_or_admitted_open(case: tuple[str, Mapping[str, Any]]) -> None:
    """A variant nothing carries names a member the record cannot generate, unless it says so."""
    name, record = case
    unborne = unborne_variants(record)
    assert not unborne, f"{name}: {unborne}"


def test_an_explanans_appeals_to_a_declared_external_system() -> None:
    """An answer may explain by the environment, and names which part of it it draws on."""
    target = {
        "type": "target-system",
        "external_systems": [{"symbol": "decoder", "name": "the system reading the outputs"}],
        "variables": [{"symbol": "y", "of": "decoder", "signature": []}],
    }
    systems = {e["symbol"] for e in target["external_systems"]}
    answer = {
        "type": "answer",
        "explanans": [{"claim": "a linear decoder reads the outputs", "appeals_to": ["decoder"]}],
    }
    assert misattributed_appeals(answer, systems) == []
    answer["explanans"][0]["appeals_to"] = ["y"]
    assert misattributed_appeals(answer, systems) == [
        "explanans.appeals_to: y is no external system of the target"
    ]


def test_an_answer_accounts_for_the_members_it_rests_on() -> None:
    """An answer resting on a quantity only some members carry accounts for those members.

    No answer record exists in the fixtures, so the rule is exercised here.
    """
    marked = {"R": "resource_explicit", "rho": "resource_explicit"}
    answer = {
        "type": "answer",
        "laws": [{"symbol": "turnover", "expression": "diff(R, t) = G(N, R, rho)"}],
    }
    assert overreaching_entries(answer, marked) == [
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
    assert misnamed_variant({"type": "answer", "variant": "absent"}, declared) == ["variant -> absent"]
    nested = {"laws": [{"variant": "direct"}, {"variant": "absent"}], "c": {"d": [{"variant": "gone"}]}}
    assert misnamed_variant(nested, declared) == ["laws.variant -> absent", "c.d.variant -> gone"]


def test_a_variant_named_in_prose_is_still_unborne() -> None:
    """The name of a variant recurs in its own prose, so the count is of what carries it."""
    record = {
        "type": "target-system",
        "variants": [{"symbol": "lattice", "name": "lattice realization",
                      "differentiation": "position runs over the sites of a lattice"}],
        "variables": [{"symbol": "u", "variant": "continuum"}],
    }
    assert unborne_variants(record) == [
        "variants.lattice: no declaration or law carries it, and its maturity admits no gap"
    ]
    record["maturity"] = {"variants.lattice": "open"}
    assert unborne_variants(record) == []
    del record["maturity"]
    record["organization"] = [{"symbol": "coupling", "variant": "lattice"}]
    assert unborne_variants(record) == []   # a relation carries a variant as a declaration does


@pytest.mark.skipif(not CASES, reason="the expressivity fixtures are absent")
@pytest.mark.parametrize("case", CASES or [("", {})], ids=IDS)
def test_no_declaration_asserts_of_all_members_what_only_some_carry(
    case: tuple[str, Mapping[str, Any]],
) -> None:
    """An entry left unmarked holds of every member, so it names no symbol of one variant alone.

    A law reaches the class through its expression, a relation of the organization through the
    parts it runs between and the laws realizing it, an external system through what it shares.
    """
    name, record = case
    overreaching = overreaching_declarations(record)
    assert not overreaching, f"{name}: {overreaching}"


@pytest.mark.skipif(not CASES, reason="the expressivity fixtures are absent")
@pytest.mark.parametrize("case", CASES or [("", {})], ids=IDS)
def test_every_interaction_passes_through_a_shared_quantity(
    case: tuple[str, Mapping[str, Any]],
) -> None:
    """A quantity indexed by one endpoint alone cannot carry an influence between two."""
    name, record = case
    misrouted = misrouted_interactions(record)
    assert not misrouted, f"{name}: {misrouted}"


@pytest.mark.skipif(not CASES, reason="the expressivity fixtures are absent")
@pytest.mark.parametrize("case", CASES or [("", {})], ids=IDS)
def test_the_record_generates_a_directed_interaction_graph(
    case: tuple[str, Mapping[str, Any]],
) -> None:
    """Every edge the record states resolves to declared nodes and declared carriers."""
    name, record = case
    declared = {entry.symbol for entry in declarations(record)}
    relations = {
        entry.get("symbol") for entry in record.get("organization") or [] if isinstance(entry, Mapping)
    }
    kinds = {
        entry.get("symbol")
        for block in ("constituents", "index_sets")
        for entry in record.get(block) or []
        if isinstance(entry, Mapping)
    }
    for edge in interaction_graph(record):
        assert edge["edge"] in relations, f"{name}: {edge['edge']} is no relation of the record"
        for endpoint in edge["sources"] + [edge["reach"]]:
            assert endpoint in kinds, f"{name}: {endpoint} is no constituent kind or index set"
        for carrier in edge["through"]:
            assert carrier in declared, f"{name}: {carrier} is not declared"
        assert edge["tuples"], f"{name}: the edge {edge['edge']} names no ordered tuples"


@pytest.mark.skipif(not CASES, reason="the expressivity fixtures are absent")
@pytest.mark.parametrize("case", CASES or [("", {})], ids=IDS)
def test_every_shared_variable_is_a_quantity(case: tuple[str, Mapping[str, Any]]) -> None:
    name, record = case
    assert not misplaced_sharing(record), f"{name}: {misplaced_sharing(record)}"


@pytest.mark.skipif(not CASES, reason="the expressivity fixtures are absent")
@pytest.mark.parametrize("case", CASES or [("", {})], ids=IDS)
def test_no_quantity_marks_shared_without_a_signature(case: tuple[str, Mapping[str, Any]]) -> None:
    name, record = case
    assert not vacuous_shared(record), f"{name}: {vacuous_shared(record)}"


def test_a_shared_variable_naming_a_set_is_reported() -> None:
    """A set does not cross a boundary, so sharing one is reported."""
    record = {
        "type": "target-system",
        "index_sets": [{"symbol": "x"}],
        "variables": [{"symbol": "s"}],
        "external_systems": [{"name": "environment", "shares": ["s", "x"]}],
    }
    assert misplaced_sharing(record) == ["external_systems.shares: x is no declared quantity"]


def test_a_parameter_running_along_an_interval_is_reported() -> None:
    """A parameter is held fixed, so a quantity indexed by an ordered continuum is exogenous."""
    record = {
        "type": "target-system",
        "index_sets": [{"symbol": "t", "structure": "interval"}, {"symbol": "i", "structure": "discrete-set"}],
        "parameters": [{"symbol": "f", "signature": ["t"]}, {"symbol": "w", "signature": ["i"]}],
    }
    assert unfixed_parameters(record) == ["parameters.f: held fixed yet indexed by ['t']"]


def test_shared_without_a_signature_is_reported() -> None:
    record = {
        "type": "target-system",
        "parameters": [{"symbol": "nu", "signature": [], "shared": True},
                       {"symbol": "w", "signature": ["i"], "shared": True}],
    }
    assert vacuous_shared(record) == ["parameters.nu: shared without a signature"]


@pytest.mark.skipif(not CASES, reason="the expressivity fixtures are absent")
@pytest.mark.parametrize("case", CASES or [("", {})], ids=IDS)
def test_no_parameter_runs_along_an_interval(case: tuple[str, Mapping[str, Any]]) -> None:
    name, record = case
    assert not unfixed_parameters(record), f"{name}: {unfixed_parameters(record)}"


@pytest.mark.skipif(not CASES, reason="the expressivity fixtures are absent")
@pytest.mark.parametrize("case", CASES or [("", {})], ids=IDS)
def test_no_quantity_is_both_built_and_conditioned(case: tuple[str, Mapping[str, Any]]) -> None:
    name, record = case
    assert not doubly_defined(record), f"{name}: {doubly_defined(record)}"


def test_a_quantity_carrying_both_an_expression_and_a_condition_is_reported() -> None:
    """One builds the quantity and cannot be false; the other presupposes that a value exists."""
    record = {
        "type": "phenomenon",
        "explanandum_variables": [
            {"symbol": "a", "expression": "min_{i}( N(i) )", "condition": "d_t(N) = 0"},
            {"symbol": "b", "condition": "d_t(N) = 0"},
        ],
    }
    assert doubly_defined(record) == ["explanandum_variables.a: both an expression and a condition"]


@pytest.mark.skipif(not CASES, reason="the expressivity fixtures are absent")
@pytest.mark.parametrize("case", CASES or [("", {})], ids=IDS)
def test_every_owner_resolves_to_an_external_system(case: tuple[str, Mapping[str, Any]]) -> None:
    name, record = case
    assert not unowned_quantities(record), f"{name}: {unowned_quantities(record)}"


def test_a_quantity_owned_by_no_declared_system_is_reported() -> None:
    """A quantity characterizes the target unless it names an external system that exists."""
    record = {
        "type": "target-system",
        "external_systems": [{"symbol": "bath", "name": "heat bath"}],
        "parameters": [{"symbol": "T", "of": "bath"}, {"symbol": "g", "of": "furnace"},
                       {"symbol": "nu"}],
    }
    assert unowned_quantities(record) == ["parameters.g: no external system named furnace"]


@pytest.mark.skipif(not CASES, reason="the expressivity fixtures are absent")
@pytest.mark.parametrize("case", CASES or [("", {})], ids=IDS)
def test_every_condition_states_which_value_it_denotes(case: tuple[str, Mapping[str, Any]]) -> None:
    name, record = case
    assert not unselected_conditions(record), f"{name}: {unselected_conditions(record)}"


def test_a_condition_without_a_selection_rule_is_reported() -> None:
    """A condition may hold of several values, so the record says which one it denotes."""
    record = {
        "type": "phenomenon",
        "explanandum_variables": [
            {"symbol": "a", "condition": "d_t(N) = 0"},
            {"symbol": "b", "condition": "d_t(N) = 0", "selects": "any"},
        ],
    }
    assert unselected_conditions(record) == ["explanandum_variables.a: a condition without a selection rule"]


REQUIRED = requirements_by_aim()
QUESTIONS = sorted(FIXTURES.glob("*/question.yml")) if FIXTURES.is_dir() else []


def records_of(directory: Path) -> dict[str, Any]:
    kinds = {"question": "question.yml", "phenomenon": "phenomenon.yml", "target-system": "target-system.yml"}
    return {
        prefix: yaml.safe_load((directory / name).read_text(encoding="utf-8"))
        for prefix, name in kinds.items()
        if (directory / name).is_file()
    }


@pytest.mark.skipif(not QUESTIONS, reason="the expressivity fixtures are absent")
@pytest.mark.parametrize("path", QUESTIONS, ids=[p.parent.name for p in QUESTIONS] or ["none"])
def test_each_inquiry_fixes_what_its_aim_requires(path: Path) -> None:
    records = records_of(path.parent)
    missing = unmet_by_aim(records["question"], records, REQUIRED)
    assert not missing, f"{path.parent.name}: {missing}"


def relaxed_for(aim: str, kind: str) -> set[str]:
    """Return the paths of ``kind`` that ``aim`` admits open, with the record prefix stripped."""
    entry = REQUIRED.get(aim) or {}
    return {p.split(".", 1)[1] for p in entry.get("open", []) if p.startswith(f"{kind}.")}


@pytest.mark.skipif(not QUESTIONS, reason="the expressivity fixtures are absent")
@pytest.mark.parametrize("path", QUESTIONS, ids=[p.parent.name for p in QUESTIONS] or ["none"])
def test_each_record_carries_what_the_notes_require_always(path: Path) -> None:
    records = records_of(path.parent)
    aim = str(((records["question"].get("task") or {}).get("epistemic_aim")))
    missing = []
    for kind in record_kinds():
        record = records.get(kind)
        if record is None:
            continue
        missing += [
            f"{kind}: {m}"
            for m in unmet_general(record, always_required(kind), relaxed_for(aim, kind))
        ]
    assert not missing, f"{path.parent.name} ({aim}): {missing}"


def test_an_aim_relaxes_only_what_the_note_lets_it_relax() -> None:
    """A record leaving an always-required specification open needs its aim to admit it."""
    record = {"type": "phenomenon", "statement": "open",
              "category": "regularity", "manifestations": [{}], "evidential_status": "established"}
    paths = always_required("phenomenon")
    assert unmet_general(record, paths) == ["always required: statement"]
    assert unmet_general(record, paths, {"statement"}) == []


@pytest.mark.skipif(not QUESTIONS, reason="the expressivity fixtures are absent")
@pytest.mark.parametrize("path", QUESTIONS, ids=[p.parent.name for p in QUESTIONS] or ["none"])
def test_every_question_says_which_silence_its_explanans_bound_is(path: Path) -> None:
    """An unbounded explanans is a decision or unfinished work, and the two read alike."""
    question = yaml.safe_load(path.read_text(encoding="utf-8"))
    assert not undeclared_explanans_bound(question), f"{path.parent.name}"


def test_an_unbounded_explanans_with_no_declaration_is_reported() -> None:
    """A justification records the decision; a maturity marker records the work not done."""
    bare = {"task": {"admissible_explanans": {"compositional": None, "substrate": None}}}
    assert len(undeclared_explanans_bound(bare)) == 1
    assert undeclared_explanans_bound({"task": {}}) == [undeclared_explanans_bound(bare)[0]]
    decided = {"task": {"admissible_explanans": {"justification": "no explanans is requested"}}}
    assert undeclared_explanans_bound(decided) == []
    unsettled = dict(bare, maturity={"task.admissible_explanans": "open"})
    assert undeclared_explanans_bound(unsettled) == []
    bounded = {"task": {"admissible_explanans": {"compositional": ["sub"], "substrate": None}}}
    assert undeclared_explanans_bound(bounded) == []


def test_a_question_asking_for_a_link_needs_the_mapping() -> None:
    """Neither description answers how a role is realized, so the answer states the mapping."""
    question = {"task": {"admissible_explanans": {"substrate": "mapping"}}}
    assert unrealized_link(question, {}) == [
        "the question asks for a link, and the answer maps no quantity onto its realization"
    ]
    assert unrealized_link({"task": {"admissible_explanans": {"substrate": "independent"}}}, {}) == []
    half = {"realizations": [{"symbol": "gate", "realizes": "role"}]}
    assert unrealized_link(question, half) == ["realizations[0] names what it realizes without saying by what"]
    whole = {"realizations": [{"symbol": "gate", "realizes": "role", "by": "g * (v - e)"}]}
    assert unrealized_link(question, whole) == []


def test_a_relation_of_the_organization_says_what_its_ends_are() -> None:
    """A relation runs between parts or between laws, and nothing carries a law-ended one."""
    record = {"type": "target-system", "laws": [{"symbol": "draw"}, {"symbol": "update"}],
              "organization": [{"symbol": "precedes", "among": ["draw", "update"]}]}
    assert malformed_relations(record) == []
    record["organization"] = [{"symbol": "both", "relates": "prod(a, b)", "among": ["draw", "update"]}]
    assert malformed_relations(record) == [
        "organization.both: a relation runs between parts or between laws, and this one names both"
    ]
    record["organization"] = [{"symbol": "neither"}]
    assert malformed_relations(record) == [
        "organization.neither: a relation runs between parts or between laws, and this one names neither"
    ]
    record["organization"] = [{"symbol": "lone", "among": ["draw"]}]
    assert malformed_relations(record) == ["organization.lone: a relation among laws orders two or more of them"]
    record["organization"] = [{"symbol": "stray", "among": ["draw", "absent"]}]
    assert malformed_relations(record) == ["organization.stray: absent is no law of the record"]


@pytest.mark.skipif(not CASES, reason="the expressivity fixtures are absent")
@pytest.mark.parametrize("case", CASES or [("", {})], ids=IDS)
def test_every_relation_of_the_organization_is_well_formed(
    case: tuple[str, Mapping[str, Any]],
) -> None:
    """Every record declaring an organization says, per relation, what its ends are."""
    name, record = case
    assert not malformed_relations(record), f"{name}: {malformed_relations(record)}"


@pytest.mark.skipif(not QUESTIONS, reason="the expressivity fixtures are absent")
@pytest.mark.parametrize("path", QUESTIONS, ids=[p.parent.name for p in QUESTIONS] or ["none"])
def test_every_virtue_a_question_weighs_states_its_standing(path: Path) -> None:
    """Which tier applies a virtue is not derivable from the virtue, so the question says."""
    question = yaml.safe_load(path.read_text(encoding="utf-8"))
    assert not unstated_standing(question), f"{path.parent.name}: {unstated_standing(question)}"


def test_a_virtue_weighed_without_a_standing_is_reported() -> None:
    """A virtue with no standing leaves the product test unable to say what it applies."""
    question = {"virtues": [{"virtue": "economy", "standing": "preferred"},
                            {"virtue": "tractability"},
                            {"justification": "an entry that never named its virtue"}]}
    assert unstated_standing(question) == [
        "virtues[1].standing is unstated for tractability",
        "virtues[2].standing is unstated for an unnamed virtue",
    ]
    assert unstated_standing({}) == []


@pytest.mark.skipif(not QUESTIONS, reason="the expressivity fixtures are absent")
@pytest.mark.parametrize("path", QUESTIONS, ids=[p.parent.name for p in QUESTIONS] or ["none"])
def test_no_question_lists_a_match_while_excluding_accuracy(path: Path) -> None:
    question = yaml.safe_load(path.read_text(encoding="utf-8"))
    assert not contradictory_accuracy(question), f"{path.parent.name}: {contradictory_accuracy(question)}"


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
    assert contradictory_accuracy(question) == [
        "task.required_accuracy.outputs_to_match is listed although accuracy does not apply"
    ]
    question["task"]["required_accuracy"]["standard"] = "numeric-bound"
    assert contradictory_accuracy(question) == []


def test_the_requirement_table_is_read_from_the_registry() -> None:
    assert REQUIRED["exploration"]["required"] == ["phenomenon.detection_criterion"]
    assert "question.subject.contrast.foil_set" in REQUIRED["explanation"]["required"]
    assert REQUIRED["description"] == {"required": [], "open": []}
    assert "phenomenon.category" in REQUIRED["exploration"]["open"]
    assert REQUIRED["prediction"]["open"] == []


def test_an_inquiry_leaving_a_required_specification_open_is_reported() -> None:
    """A prediction compares an output against a measurement, so it fixes what must match."""
    question = {"task": {"epistemic_aim": "prediction", "required_accuracy": {"outputs_to_match": []}}}
    records = {"question": question, "phenomenon": {"manifestations": []}}
    assert unmet_by_aim(question, records, REQUIRED) == [
        "prediction requires phenomenon.manifestations",
        "prediction requires question.task.required_accuracy.outputs_to_match",
    ]


@pytest.mark.skipif(not CASES, reason="the expressivity fixtures are absent")
@pytest.mark.parametrize("case", CASES or [("", {})], ids=IDS)
def test_every_closed_field_holds_an_admitted_value(case: tuple[str, Mapping[str, Any]]) -> None:
    name, record = case
    bad = inadmissible_values(record, admitted_values(str(record.get("type"))))
    assert not bad, f"{name}: {bad}"


def test_a_value_outside_its_vocabulary_is_reported() -> None:
    """A value outside a closed field's vocabulary passed every check before the registry existed.

    ``no-such-role`` is a deliberate sentinel rather than a typo awaiting correction: replacing it
    with an admitted value would leave the check unable to fail.
    """
    admitted = admitted_values("target-system")
    record = {"type": "target-system", "laws": [{"role": "no-such-role"}, {"role": "state-constraint"}]}
    assert inadmissible_values(record, admitted) == ["laws.role: no-such-role is not admitted"]


def test_a_record_field_is_read_apart_from_a_field_of_the_same_name() -> None:
    """A record field and an entry field may share a name, under separate vocabularies.

    No field of the current templates collides, the last one having gone when the answer stopped
    calling its quantities terms, so the rule is stated against a vocabulary written here: a
    collision must not let one lookup answer for the other.
    """
    admitted = {
        ".status": frozenset({"draft"}),
        "terms.status": frozenset({"load-bearing"}),
    }
    record = {"status": "no-such-state", "terms": [{"status": "no-such-status"}]}
    assert inadmissible_values(record, admitted) == [
        "record.status: no-such-state is not admitted",
        "terms.status: no-such-status is not admitted",
    ]


@pytest.mark.skipif(not CASES, reason="the expressivity fixtures are absent")
@pytest.mark.parametrize("case", CASES or [("", {})], ids=IDS)
def test_no_expression_was_split_by_the_serializer(case: tuple[str, Mapping[str, Any]]) -> None:
    name, record = case
    assert not split_expressions(record), f"{name}: {split_expressions(record)}"


def test_an_expression_split_on_its_commas_is_reported() -> None:
    """An unquoted expression inside a bracketed list splits into plausible fragments.

    The record below is what ``signature: [maps(prod(a, b), reals)]`` parses to.
    """
    record = {
        "type": "target-system",
        "operators": [{"symbol": "f", "signature": ["maps(prod(a", "b)", "reals)"]}],
    }
    assert split_expressions(record) == [
        "operators.signature: 'maps(prod(a' is a fragment of a split expression",
        "operators.signature: 'b)' is a fragment of a split expression",
        "operators.signature: 'reals)' is a fragment of a split expression",
    ]


@pytest.mark.skipif(not CASES, reason="the expressivity fixtures are absent")
@pytest.mark.parametrize("case", CASES or [("", {})], ids=IDS)
def test_no_notation_was_damaged_by_the_serializer(case: tuple[str, Mapping[str, Any]]) -> None:
    name, record = case
    assert not corrupted_notation(record), f"{name}: {corrupted_notation(record)}"


def test_a_latex_form_in_double_quotes_is_reported() -> None:
    """A double-quoted scalar reads the backslash of a LaTeX command as an escape."""
    damaged = yaml.safe_load('parameters:\n  - symbol: nu\n    notation: "\\nu"\n')
    damaged["type"] = "target-system"
    assert corrupted_notation(damaged) == ["parameters.nu: the notation holds a control character"]
    intact = yaml.safe_load("parameters:\n  - symbol: nu\n    notation: '\\nu'\n")
    intact["type"] = "target-system"
    assert corrupted_notation(intact) == []


def test_a_condition_of_the_phenomenon_is_checked() -> None:
    """A precipitating condition is an expression, so an undeclared symbol in it is reported."""
    record = {
        "type": "phenomenon",
        "explanandum_variables": [{"symbol": "Y", "signature": []}],
        "conditions_and_byproducts": {
            "precipitating": [{"expression": "Y > no_such_symbol"}],
            "inhibiting": [],
        },
    }
    assert unresolved(record, CANONICAL) == [
        "conditions_and_byproducts.precipitating.expression -> no_such_symbol"
    ]


def test_the_canonical_vocabulary_comes_from_the_registry() -> None:
    """The framework set is read from package data, so no check depends on a document."""
    assert {"mean", "min", "max", "sum", "dist"} <= CANONICAL      # binders
    assert {"implies", "depends_on"} <= CANONICAL                  # relations
    assert "far_field" not in CANONICAL                            # a problem declares its own
    assert "Ltrain" not in CANONICAL                               # a quantity is not an operator


def test_a_registry_declaring_no_operator_is_reported(tmp_path: Path) -> None:
    """Reading fails loudly when the registry carries no operator."""
    empty = tmp_path / "operators.yml"
    empty.write_text("id: registry.operators\ntype: operator-registry\noperators: []\n", encoding="utf-8")
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
    assert unresolved(record, CANONICAL) == ["laws.expression -> f"]


def test_prose_left_in_a_value_set_is_reported() -> None:
    """A value set is an expression, so a description left there resolves to nothing."""
    record = {
        "type": "target-system",
        "parameters": [{"symbol": "nu", "values": "admissible body-force families"}],
    }
    assert unresolved(record, CANONICAL) == [
        "parameters.values -> admissible",
        "parameters.values -> body",
        "parameters.values -> families",
        "parameters.values -> force",
    ]


def test_prose_in_a_nested_feature_value_set_is_reported() -> None:
    """A value set is checked wherever it occurs, including inside a manifestation feature."""
    record = {
        "type": "phenomenon",
        "manifestations": [{"features": [{"symbol": "a", "values": "prose left here"}]}],
    }
    assert unresolved(record, CANONICAL) == [
        "manifestations.features.values -> here",
        "manifestations.features.values -> left",
        "manifestations.features.values -> prose",
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
        "explanandum_variables": [
            {"symbol": "a", "expression": "max( re( far_field(J) ) )", "signature": []}
        ],
    }
    assert unresolved(record, CANONICAL) == [
        "explanandum_variables.expression -> J",
        "explanandum_variables.expression -> far_field",
    ]
    record["operators"] = [{"symbol": "far_field", "name": "the far-field limit of a profile"}]
    assert unresolved(record, CANONICAL) == ["explanandum_variables.expression -> J"]


def test_a_reference_to_an_undeclared_set_is_reported() -> None:
    """Every signature entry names a declared set, so an undeclared index is reported too."""
    record = {
        "type": "target-system",
        "index_sets": [{"symbol": "x"}],
        "variables": [{"symbol": "u", "signature": ["x", "undeclared_index"]}],
        "laws": [{"expression": "u = u", "signature": ["y"]}],
    }
    assert unresolved(record, CANONICAL) == [
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


def test_the_markdown_view_is_built_from_that_record() -> None:
    problem = load_problem(PROBLEMS[0])
    page = render_markdown(problem)
    assert page.startswith("---")
    assert "## Symbols" in page and "## Operators" in page
    assert all(f"`{entry.symbol}`" in page for entry in problem.declarations)
