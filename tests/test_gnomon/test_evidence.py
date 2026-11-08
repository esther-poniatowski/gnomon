"""The evidential status of a phenomenon against the type of its target system.

A behavior obtained by derivation is ``derived`` when it is asserted of a model or of a target
without actual members, and ``predicted`` when it is asserted of a target with actual members,
since it then awaits detection. Each mismatch is shown on a defect planted in a copy of a worked
inquiry, and the unchanged inquiries report neither.
"""

from __future__ import annotations

import shutil
from pathlib import Path

from gnomon.check import check_workspace, load_workspace

from .paths import EXAMPLES

RULE = "completeness/mismatched-evidence"


def _rules(tmp_path: Path, case: str, old: str, new: str) -> list[str]:
    """Return the rule and the text of each finding of a copy of a worked inquiry whose
    phenomenon is changed once."""
    folder = tmp_path / case
    shutil.copytree(EXAMPLES / case, folder)
    path = folder / "phenomenon.yml"
    text = path.read_text(encoding="utf-8")
    assert old in text, f"the text to replace is absent: {old}"
    path.write_text(text.replace(old, new, 1), encoding="utf-8")
    return [
        f"{x.finding.rule.id} {x.finding.text}" for x in check_workspace(load_workspace(tmp_path))
    ]


def test_a_behavior_derived_for_an_empirical_target_is_reported_as_predicted(
    tmp_path: Path,
) -> None:
    found = _rules(
        tmp_path,
        "earth-system-tipping-cascades",
        "evidential_status: predicted",
        "evidential_status: derived",
    )
    assert [t for t in found if t.startswith(RULE)] == [
        f"{RULE} evidential_status: derived, whereas system.earth-tipping-subsystems is of"
        " type particular; a behavior derived for a target with actual members is predicted"
    ], found


def test_a_behavior_predicted_for_a_formal_target_is_reported_as_derived(tmp_path: Path) -> None:
    found = _rules(
        tmp_path,
        "swift-hohenberg-localized-states",
        "evidential_status: derived",
        "evidential_status: predicted",
    )
    assert any(
        t.startswith(RULE) and "a behavior derived for a target without actual members" in t
        for t in found
    ), found
