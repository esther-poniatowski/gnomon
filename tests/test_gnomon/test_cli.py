"""Behavior of the root command-line interface."""

import platform

import pytest
from typer.testing import CliRunner

from gnomon import __version__
from gnomon.cli import app
from gnomon.findings import ITINERARY_UNAVAILABLE_HISTORY, RULES


def test_version_option_exits_without_a_subcommand() -> None:
    """The root version option reports the package version and succeeds."""
    result = CliRunner().invoke(app, ["--version"])

    assert result.exit_code == 0
    assert result.stdout == f"{__version__}\n"


def test_info_reports_the_package_and_platform_diagnostics() -> None:
    """The info command reports the installed and runtime versions."""
    result = CliRunner().invoke(app, ["info"])

    assert result.exit_code == 0
    assert result.stdout == (
        f"gnomon {__version__} | Platform: {platform.system()} "
        f"Python {platform.python_version()}\n"
    )


def test_no_arguments_still_show_the_root_help() -> None:
    """Enabling root options preserves the existing no-argument guidance."""
    result = CliRunner().invoke(app, [])

    assert result.exit_code == 2
    assert "Usage:" in result.stdout
    assert "--version" in result.stdout


def _fields(stdout: str) -> dict[str, str]:
    """Return the labelled lines of an explanation, keyed by their label."""
    return dict(line.split(": ", 1) for line in stdout.splitlines())


def test_explain_prints_the_catalogue_entry_of_a_known_rule() -> None:
    """A known rule prints its catalogue fields in a fixed order, identically on each run."""
    rule = ITINERARY_UNAVAILABLE_HISTORY
    first = CliRunner().invoke(app, ["explain", rule.id])
    second = CliRunner().invoke(app, ["explain", rule.id])

    assert first.exit_code == 0
    assert first.stderr == ""
    assert first.stdout == second.stdout
    assert first.stdout == (
        f"rule: {rule.id}\n"
        f"level: {rule.level}\n"
        f"meaning: {rule.description}\n"
        f"repair: {rule.repair_condition}\n"
        f"documentation: {rule.documentation_target}\n"
    )


def test_explain_prints_the_catalogue_target_of_every_rule() -> None:
    """Each published rule explains, and each printed field is the field of the catalogue."""
    for rule in RULES:
        result = CliRunner().invoke(app, ["explain", rule.id])

        assert result.exit_code == 0, rule.id
        assert _fields(result.stdout) == {
            "rule": rule.id,
            "level": rule.level,
            "meaning": rule.description,
            "repair": str(rule.repair_condition),
            "documentation": str(rule.documentation_target),
        }


def test_explain_rejects_an_unknown_rule_without_a_traceback() -> None:
    """An unknown identifier is named on standard error with the closest rule and the listing."""
    result = CliRunner().invoke(app, ["explain", "itinerary/cycl"])

    assert result.exit_code == 2
    assert isinstance(result.exception, SystemExit)
    assert result.stdout == ""
    assert result.stderr == (
        "unknown rule identifier: itinerary/cycl; did you mean itinerary/cycle?\n"
        "list the known identifiers with: gnomon explain --list\n"
    )


def test_explain_suggests_no_rule_far_from_every_identifier() -> None:
    """An identifier close to no rule receives the listing instruction alone."""
    result = CliRunner().invoke(app, ["explain", "no/such-rule"])

    assert result.exit_code == 2
    assert result.stderr.splitlines() == [
        "unknown rule identifier: no/such-rule",
        "list the known identifiers with: gnomon explain --list",
    ]


def test_explain_list_prints_every_identifier_in_sorted_order() -> None:
    """The listing holds each identifier of the catalogue once, sorted."""
    result = CliRunner().invoke(app, ["explain", "--list"])

    assert result.exit_code == 0
    assert result.stdout.splitlines() == sorted(rule.id for rule in RULES)


@pytest.mark.parametrize("arguments", [[], ["--list", "itinerary/cycle"]])
def test_explain_requires_exactly_one_of_an_identifier_and_the_listing(
    arguments: list[str],
) -> None:
    """Neither or both of an identifier and `--list` is a usage error."""
    result = CliRunner().invoke(app, ["explain", *arguments])

    assert result.exit_code == 2
    assert result.stdout == ""
    assert result.stderr == "give either one rule identifier or --list\n"
