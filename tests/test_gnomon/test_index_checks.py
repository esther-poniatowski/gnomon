"""The number of arguments of a quantity, and the operators written as binders.

A quantity is applied to its indices, or to the arguments of its value map; any other number of
arguments is reported, unless the record leaves the values of the quantity open. An operator
written ``op_{indices}(...)`` binds those indices, so its kind must be binder, in the registry or
in the operator record of the problem. Each rule is shown on a defect planted in a copy of a worked
inquiry.
"""

from __future__ import annotations

import shutil
from pathlib import Path

from gnomon.check import check_workspace, load_workspace

from .paths import EXAMPLES


def _rules(tmp_path: Path, case: str, name: str, old: str, new: str) -> list[str]:
    """Return the rule and the text of each finding of a copy of a worked inquiry, changed once."""
    folder = tmp_path / case
    shutil.copytree(EXAMPLES / case, folder)
    path = folder / name
    text = path.read_text(encoding="utf-8")
    assert old in text, f"{name}: the text to replace is absent: {old}"
    path.write_text(text.replace(old, new, 1), encoding="utf-8")
    return [
        f"{x.finding.rule.id} {x.finding.text}" for x in check_workspace(load_workspace(tmp_path))
    ]


def test_a_quantity_applied_to_too_few_indices_is_reported(tmp_path: Path) -> None:
    found = _rules(
        tmp_path, "grokking-delayed-generalization", "background.yml", "theta(coord, 0)", "theta(0)"
    )
    assert any(
        t.startswith("vocabulary/mismatched-indices") and "theta is applied to 1 arguments" in t
        for t in found
    ), found


def test_an_operator_of_another_kind_written_as_a_binder_is_reported(tmp_path: Path) -> None:
    found = _rules(
        tmp_path,
        "grokking-delayed-generalization",
        "phenomenon.yml",
        "min_{step}( Ltrain <= eps_fit )",
        "abs_{step}( Ltrain )",
    )
    assert any(
        "vocabulary/misused-binder" in t and "abs binds the indices step" in t for t in found
    )


def test_a_problem_operator_binds_only_once_declared_a_binder(tmp_path: Path) -> None:
    found = _rules(
        tmp_path, "earth-system-tipping-cascades", "operators.yml", "    kind: binder\n", ""
    )
    assert any("vocabulary/misused-binder" in t and "sequence binds" in t for t in found)
