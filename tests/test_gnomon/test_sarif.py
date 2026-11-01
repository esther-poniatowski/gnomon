"""The SARIF log of the checks, in the findings profile of Elenchos.

The first tests build a log from findings and check each object that the profile requires or
excludes: one run of the driver ``gnomon`` listing every rule, one invocation, and per result its
rule, its level, its message, one physical location and one logical location. The last tests run
the command ``gnomon itinerary`` on a problem written in a temporary folder.
"""

from __future__ import annotations

import json
from pathlib import Path, PurePosixPath
from typing import Any

import pytest
import yaml
from typer.testing import CliRunner

from gnomon import __version__
from gnomon.cli import app
from gnomon.findings import ITINERARY_CYCLE, ITINERARY_UNADDRESSED, REGISTRY_FOREIGN_NORM, RULES, Finding
from gnomon.sarif import Located, sarif_log

CYCLE = Finding(ITINERARY_CYCLE, ("steps",), "steps: a -> b -> a forms a cycle", "a -> b -> a")
UNADDRESSED = Finding(ITINERARY_UNADDRESSED, ("addresses",), "addresses: x is no problem or question record")
FILE = PurePosixPath("problems/demo/itinerary.yml")


def run_of(log: dict[str, Any]) -> dict[str, Any]:
    assert log["version"] == "2.1.0" and len(log["runs"]) == 1
    return log["runs"][0]


def test_a_complete_run_lists_every_rule_and_declares_its_success() -> None:
    run = run_of(sarif_log([], "1.2.3"))
    driver = run["tool"]["driver"]
    assert (driver["name"], driver["version"]) == ("gnomon", "1.2.3")
    assert [rule["id"] for rule in driver["rules"]] == [rule.id for rule in RULES]
    assert all(
        rule["shortDescription"]["text"] and rule["defaultConfiguration"] == {"level": "error"}
        for rule in driver["rules"]
    )
    assert run["invocations"] == [{"executionSuccessful": True}]
    assert run["columnKind"] == "unicodeCodePoints"
    assert run["results"] == []


def test_a_failed_run_declares_an_error_notification() -> None:
    run = run_of(sarif_log([Located(UNADDRESSED, FILE, "itin.demo")], "1.2.3", stopped="a file was unreadable"))
    assert run["invocations"] == [{
        "executionSuccessful": False,
        "toolExecutionNotifications": [{"level": "error", "message": {"text": "a file was unreadable"}}],
    }]
    assert len(run["results"]) == 1


def test_a_result_holds_its_rule_message_and_two_locations() -> None:
    run = run_of(sarif_log([Located(CYCLE, FILE, "itin.demo"), Located(UNADDRESSED, FILE, "itin.demo")], "1"))
    cycle, unaddressed = run["results"]
    assert cycle == {
        "ruleId": "itinerary/cycle",
        "level": "error",
        "message": {"text": "steps: a -> b -> a forms a cycle"},
        "locations": [{
            "physicalLocation": {
                "artifactLocation": {"uri": "problems/demo/itinerary.yml", "uriBaseId": "SRCROOT"}
            },
            "logicalLocations": [{"name": "id:itin.demo#/steps"}],
        }],
        "partialFingerprints": {"discriminator/v1": "a -> b -> a"},
    }
    assert "partialFingerprints" not in unaddressed
    assert unaddressed["locations"][0]["logicalLocations"] == [{"name": "id:itin.demo#/addresses"}]
    for result in run["results"]:
        assert not {"suppressions", "fingerprints", "baselineState"} & set(result)
        assert "region" not in result["locations"][0]["physicalLocation"]


def test_the_whole_record_takes_the_resource_alone() -> None:
    whole = Finding(ITINERARY_UNADDRESSED, (), "the record")
    result = run_of(sarif_log([Located(whole, FILE, "itin.demo")], "1"))["results"][0]
    assert result["locations"][0]["logicalLocations"] == [{"name": "id:itin.demo"}]


def test_the_resource_and_the_uri_are_escaped() -> None:
    """``%`` and ``#`` are escaped in the resource; the URI is percent-encoded."""
    located = Located(CYCLE, PurePosixPath("odd dir/it#1.yml"), "itin.50%#a")
    result = run_of(sarif_log([located], "1"))["results"][0]
    location = result["locations"][0]
    assert location["logicalLocations"] == [{"name": "id:itin.50%25%23a#/steps"}]
    assert location["physicalLocation"]["artifactLocation"]["uri"] == "odd%20dir/it%231.yml"


def test_a_file_holding_no_record_is_named_by_its_path() -> None:
    norm = Finding(REGISTRY_FOREIGN_NORM, ("activities",), "x: its norm", "derivation/norm")
    located = Located(norm, PurePosixPath("src/gnomon/data/registries/activities.yml"))
    result = run_of(sarif_log([located], "1"))["results"][0]
    assert result["locations"][0]["logicalLocations"] == [
        {"name": "path:src/gnomon/data/registries/activities.yml#/activities"}
    ]


@pytest.mark.parametrize("path", ["/abs/itinerary.yml", "../outside.yml"])
def test_a_path_outside_the_repository_is_refused(path: str) -> None:
    with pytest.raises(ValueError, match="repository-relative"):
        Located(CYCLE, PurePosixPath(path), "itin.demo")


# --- The command ----------------------------------------------------------------------------------

RECORDS: dict[str, dict[str, Any]] = {
    "problem.yml": {"id": "prob.demo", "type": "problem"},
    "model.yml": {"id": "mod.demo", "type": "model"},
    "itinerary.yml": {
        "id": "itin.demo",
        "type": "itinerary",
        "addresses": "prob.demo",
        "steps": [
            {"id": "derive", "activity": "derivation", "inputs": [{"type": "model", "ref": "mod.demo"}],
             "output": {"type": "consequence"}, "norm": {"test": "norm.derivation", "verdict": "pending"},
             "mode": "deductive"},
            {"id": "guess", "activity": "intuition", "inputs": [], "output": {"type": "consequence"},
             "norm": {"test": "norm.intuition", "verdict": "pending"}},
        ],
    },
}
LINES = [
    "itin.demo: steps.guess: intuition is no registered activity",
    "1 itineraries checked, 1 problems found",
]


@pytest.fixture
def problem(tmp_path: Path) -> Path:
    """Write the records of one problem under ``tmp_path/problems/demo``."""
    folder = tmp_path / "problems" / "demo"
    folder.mkdir(parents=True)
    for name, record in RECORDS.items():
        (folder / name).write_text(yaml.safe_dump(record, sort_keys=False), encoding="utf-8")
    return folder


def test_the_text_output_prints_one_line_per_problem(problem: Path) -> None:
    result = CliRunner().invoke(app, ["itinerary", str(problem)])
    assert result.exit_code == 1
    assert result.stdout.splitlines() == LINES


def test_the_command_writes_a_log_and_keeps_its_text_output(problem: Path, tmp_path: Path) -> None:
    output = tmp_path / "logs" / "nested" / "gnomon.sarif"
    result = CliRunner().invoke(
        app, ["itinerary", str(problem), "--format", "sarif", "--output", str(output), "--root", str(tmp_path)]
    )
    assert result.exit_code == 1
    assert result.stdout.splitlines() == LINES
    run = run_of(json.loads(output.read_text(encoding="utf-8")))
    assert run["tool"]["driver"]["version"] == __version__
    assert run["invocations"] == [{"executionSuccessful": True}]
    (found,) = run["results"]
    assert found["ruleId"] == "itinerary/unknown-activity"
    assert found["message"]["text"] == "steps.guess: intuition is no registered activity"
    location = found["locations"][0]
    assert location["physicalLocation"]["artifactLocation"] == {
        "uri": "problems/demo/itinerary.yml", "uriBaseId": "SRCROOT"
    }
    assert location["logicalLocations"] == [{"name": "id:itin.demo#/steps"}]
    assert found["partialFingerprints"] == {"discriminator/v1": "guess/activity"}


def test_without_output_the_log_takes_standard_output(problem: Path, tmp_path: Path) -> None:
    result = CliRunner().invoke(app, ["itinerary", str(problem), "--format", "sarif", "--root", str(tmp_path)])
    assert result.exit_code == 1
    assert len(run_of(json.loads(result.stdout))["results"]) == 1
    assert result.stderr.splitlines() == LINES


def test_an_unreadable_record_declares_a_failed_run(problem: Path, tmp_path: Path) -> None:
    (problem / "broken.yml").write_text("id: [unclosed\n", encoding="utf-8")
    output = tmp_path / "gnomon.sarif"
    result = CliRunner().invoke(
        app, ["itinerary", str(problem), "--format", "sarif", "--output", str(output), "--root", str(tmp_path)]
    )
    assert result.exit_code == 1
    (invocation,) = run_of(json.loads(output.read_text(encoding="utf-8")))["invocations"]
    assert invocation["executionSuccessful"] is False
    assert invocation["toolExecutionNotifications"][0]["level"] == "error"
    assert "broken.yml" in result.stderr


def test_a_folder_outside_the_root_is_refused(problem: Path, tmp_path: Path) -> None:
    result = CliRunner().invoke(
        app, ["itinerary", str(problem), "--format", "sarif", "--root", str(tmp_path / "elsewhere")]
    )
    assert result.exit_code == 1
    assert "outside the root" in result.stderr


def test_an_output_requires_the_sarif_format(problem: Path, tmp_path: Path) -> None:
    result = CliRunner().invoke(app, ["itinerary", str(problem), "--output", str(tmp_path / "x.sarif")])
    assert result.exit_code == 2
