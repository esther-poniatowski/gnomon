"""Consequences of epistemic activities exposed to next-act guidance."""

from gnomon.activity_consequences import activities_unblocked_by, activity_consequences


def test_activity_consequences_name_required_inputs_and_output_locations() -> None:
    """The registries determine the fields shown before a researcher selects an act."""
    consequences = activity_consequences()

    assert consequences["explication"].required_inputs == ("concept | problem",)
    assert consequences["explication"].output_type == "concept"
    assert consequences["explication"].produces_in == ("concept record",)
    assert consequences["operationalization"].produces_in == (
        "partial: target-system.variables[].scale",
        "partial: target-system.variables[].expression",
    )
    assert consequences["reduction"].required_inputs == ("2 × model",)  # noqa: RUF001
    assert consequences["reduction"].produces_in == ("not represented by a record yet",)


def test_an_output_names_only_waiting_activities_that_admit_its_type() -> None:
    """A possible downstream act is derived from its missing slot, without ranking it."""
    waiting = (
        ("explication", ("concept | problem",)),
        ("operationalization", ("concept",)),
        ("formalization", ("model | target-claim",)),
        ("derivation", ("admitted-laws",)),
    )

    assert activities_unblocked_by("concept", waiting) == (
        "explication",
        "operationalization",
    )
    assert activities_unblocked_by("concept", waiting, excluding="explication") == (
        "operationalization",
    )
    assert activities_unblocked_by("target-claim", waiting) == ("formalization",)
    assert not activities_unblocked_by("verdict", waiting)
