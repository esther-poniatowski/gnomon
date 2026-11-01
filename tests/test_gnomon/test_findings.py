"""Findings of the checks: the catalogue of rules, the locus of each finding, and its discriminator.

A finding lies at the JSON Pointer of the field it concerns. An entry of a keyed list is located by
the pointer of the list and named by its identifier in the discriminator, so reordering the list
keeps its identity; an entry of an unkeyed list keeps its index. These tests plant one defect per
case and read the locus and the discriminator of the finding it yields.
"""

from __future__ import annotations

import copy
from typing import Any

import pytest

from gnomon.completeness import inadmissible_values, malformed_restrictions, unstated_standing
from gnomon.findings import RULE_ID, RULES, Rule, pointer
from gnomon.itineraries import activities, itinerary_problems, malformed_registry, product_types
from gnomon.vocabulary import doubly_defined, misnamed_variant, unresolved

from .test_itineraries import ITINERARY, RECORDS


def places(found: list[Any]) -> list[tuple[str, str]]:
    """Return the locus and the discriminator of each finding."""
    return [(f.locus, f.discriminator) for f in found]


@pytest.mark.parametrize(
    ("path", "expected"),
    [
        ((), ""),
        (("",), "/"),
        (("a/b",), "/a~1b"),
        (("c~1d",), "/c~01d"),
        (("~/",), "/~0~1"),
        (("relations", 2, "target"), "/relations/2/target"),
    ],
)
def test_a_field_path_converts_to_a_json_pointer(path: tuple[str | int, ...], expected: str) -> None:
    """``~`` is escaped before ``/``, so that ``/`` never becomes ``~01``."""
    assert pointer(path) == expected


def test_the_catalogue_holds_one_well_formed_rule_per_identifier() -> None:
    identifiers = [rule.id for rule in RULES]
    assert len(identifiers) == len(set(identifiers))
    assert all(RULE_ID.fullmatch(identifier) for identifier in identifiers)
    assert all(rule.description.strip() for rule in RULES)
    with pytest.raises(ValueError, match="malformed rule identifier"):
        Rule("Itinerary/Cycle", "an uppercase identifier")


def test_an_entry_of_a_keyed_list_is_named_by_its_identifier() -> None:
    """Reordering the list keeps each identity; the identifier opens the discriminator."""
    record = {
        "type": "target-system",
        "variables": [
            {"symbol": "a", "expression": "x", "condition": "y"},
            {"symbol": "b", "expression": "x", "condition": "y"},
        ],
    }
    found = doubly_defined(record)
    assert places(found) == [("/variables", "a"), ("/variables", "b")]
    record["variables"].reverse()
    assert sorted(places(doubly_defined(record))) == sorted(places(found))


def test_an_entry_without_identifier_keeps_its_index() -> None:
    record = {"type": "target-system", "variables": [{"symbol": "a"}, {"expression": "x", "condition": "y"}]}
    assert places(doubly_defined(record)) == [("/variables/1", "")]


def test_an_identifier_is_escaped_in_the_discriminator() -> None:
    record = {"type": "target-system", "variables": [{"symbol": "a/b~c", "expression": "x", "condition": "y"}]}
    assert places(doubly_defined(record)) == [("/variables", "a~1b~0c")]


def test_an_entry_of_an_unkeyed_list_keeps_its_index() -> None:
    question = {"virtues": [{"virtue": "economy", "standing": "preferred"}, {"virtue": "tractability"}]}
    assert places(unstated_standing(question)) == [("/virtues/1/standing", "")]


def test_a_step_is_named_by_its_identifier_wherever_it_stands() -> None:
    itinerary = copy.deepcopy(ITINERARY)
    itinerary["steps"][1]["activity"] = "intuition"
    assert places(itinerary_problems(itinerary, RECORDS)) == [("/steps", "derive/activity")]
    itinerary["steps"].reverse()
    assert places(itinerary_problems(itinerary, RECORDS)) == [("/steps", "derive/activity")]


def test_a_cycle_and_a_repeated_step_are_discriminated_by_their_content() -> None:
    itinerary = copy.deepcopy(ITINERARY)
    itinerary["steps"].append(copy.deepcopy(itinerary["steps"][0]))
    itinerary["steps"][2]["inputs"].append({"type": "data", "ref": "observe"})
    found = places(itinerary_problems(itinerary, RECORDS))
    assert ("/steps", "pose") in found
    assert ("/steps", "design -> observe -> design") in found


def test_a_closed_field_lies_at_its_full_path() -> None:
    """The message names the top-level block and the field alone; the locus keeps every level."""
    admitted = {"laws.role": frozenset({"evolution"}), ".status": frozenset({"draft"})}
    record = {"status": "wrong", "laws": [{"symbol": "f", "inner": {"role": "bad"}},
                                          {"inner": {"role": ["evolution", "worse"]}}]}
    found = inadmissible_values(record, admitted)
    assert [f.text for f in found] == [
        "record.status: wrong is not admitted",
        "laws.role: bad is not admitted",
        "laws.role: worse is not admitted",
    ]
    assert places(found) == [("/status", ""), ("/laws", "f/inner/role"), ("/laws/1/inner/role/1", "")]


def test_a_restriction_lies_under_the_domain_of_the_subject() -> None:
    question = {"subject": {"domain": {"restrictions": [
        {"name": "clamped flux", "values": "x", "expression": "y"},
        {"restriction": "clamped"},
    ]}}}
    found = malformed_restrictions(question, set())
    assert places(found) == [
        ("/subject/domain/restrictions", "clamped flux"),
        ("/subject/domain/restrictions/1", ""),
        ("/subject/domain/restrictions/1", ""),
        ("/subject/domain/restrictions/1/restriction", ""),
    ]


def test_an_unresolved_symbol_lies_at_its_field_or_its_expression() -> None:
    """A reference lies at its item; a formula identifier is discriminated by its name."""
    record = {
        "type": "target-system",
        "laws": [{"symbol": "g", "expression": "u + f", "signature": ["t", "s"]}],
        "course": {"varies": ["w"]},
    }
    found = unresolved(record, set())
    assert [f.text for f in found] == [
        "laws.signature -> t",
        "laws.signature -> s",
        "course.varies[] -> w",
        "laws.expression -> f",
        "laws.expression -> u",
    ]
    assert places(found) == [
        ("/laws", "g/signature/0"),
        ("/laws", "g/signature/1"),
        ("/course/varies/0", ""),
        ("/laws", "g/expression/f"),
        ("/laws", "g/expression/u"),
    ]


def test_a_misnamed_variant_lies_at_its_mark() -> None:
    nested = {"laws": [{"symbol": "f", "variant": "absent"}], "c": {"d": [{"variant": "gone"}]}}
    found = misnamed_variant(nested, {"direct"})
    assert [f.text for f in found] == ["laws.variant -> absent", "c.d.variant -> gone"]
    assert places(found) == [("/laws", "f/variant"), ("/c/d/0/variant", "")]


def test_a_finding_on_the_registry_names_the_activity() -> None:
    act = activities()["derivation"]
    broken = {"derivation": type(act)(**{**act.__dict__, "output": "theorem", "mode": "intuitive"})}
    found = malformed_registry(broken, product_types(), ["deductive"])
    assert places(found) == [("/activities", "derivation/output/theorem"), ("/activities", "derivation/mode")]
