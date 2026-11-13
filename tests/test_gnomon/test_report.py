"""The stable structured issue contract of the YAML findings report."""

from pathlib import PurePosixPath

import yaml

from gnomon.check import FutureWork
from gnomon.findings import CONTRACT_VALIDATION, Finding, Rule
from gnomon.report import render_yaml_report
from gnomon.sarif import Located


def test_an_issue_carries_location_classification_and_guidance() -> None:
    rule = Rule(
        "test/broken-value",
        "A value is broken.",
        result_class=CONTRACT_VALIDATION,
        repair_condition="The value satisfies its declared type.",
        documentation_target="docs/specification/value.md",
    )
    located = Located(
        Finding(
            rule,
            ("value",),
            "value: expected an integer",
            controlled_by=("kind",),
        ),
        PurePosixPath("problems/demo/problem.yml"),
        "prob.demo",
    )

    document = yaml.safe_load(render_yaml_report([located], "demo", 1))

    assert document["files"] == [
        {
            "file": "problems/demo/problem.yml",
            "findings": [
                {
                    "record": "prob.demo",
                    "rule": "test/broken-value",
                    "level": "error",
                    "locus": "/value",
                    "result_class": CONTRACT_VALIDATION,
                    "message": "value: expected an integer",
                    "repair_condition": "The value satisfies its declared type.",
                    "documentation_target": "docs/specification/value.md",
                    "source_file": "problems/demo/problem.yml",
                    "record_identifier": "prob.demo",
                    "field_path": "/value",
                    "severity": "error",
                    "explanation": "value: expected an integer",
                    "controlled_by": "/kind",
                }
            ],
        }
    ]


def test_missing_optional_guidance_is_explicit() -> None:
    rule = Rule("test/broken-value", "A value is broken.")
    located = Located(Finding(rule, (), "the record is invalid"), PurePosixPath("problem.yml"))

    issue = yaml.safe_load(render_yaml_report([located], "demo", 1))["files"][0]["findings"][0]

    assert issue["repair_condition"] is None
    assert issue["documentation_target"] is None


def test_a_scoped_report_separates_future_work_from_findings() -> None:
    future = FutureWork(
        "candidate-proposed",
        PurePosixPath("problems/demo/answer.yml"),
        "ans.demo.candidate",
        "answer",
        "/claim",
        "claim: answer requires claim",
    )

    report = yaml.safe_load(
        render_yaml_report([], "demo", 1, scope="question-typed", future_work=[future])
    )

    assert report["findings"] == 0
    assert report["future"] == 1
    assert report["future_work"] == [
        {
            "due_scope": "candidate-proposed",
            "source_file": "problems/demo/answer.yml",
            "record_identifier": "ans.demo.candidate",
            "record_kind": "answer",
            "field_path": "/claim",
            "result_class": "computed inquiry diagnosis",
            "message": "claim: answer requires claim",
        }
    ]
