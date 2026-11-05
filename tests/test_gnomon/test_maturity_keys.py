"""The keys of the block `maturity`: each is the path of a field that the schema of its record
declares, through an entry named by its symbol or its identifier where the path picks one entry.

Each form of a key is shown on a planted record, and a misspelled key is planted in a copy of a
worked inquiry.
"""

from __future__ import annotations

import shutil
from pathlib import Path

from gnomon.check import check_workspace, load_workspace
from gnomon.completeness import misplaced_maturity
from gnomon.findings import texts

from .paths import EXAMPLES


def _phenomenon(**maturity: str) -> dict[str, object]:
    return {
        "type": "phenomenon",
        "observables": [{"symbol": "Z", "values": None}],
        "manifestations": [],
        "maturity": {key.replace("__", "."): value for key, value in maturity.items()},
    }


def test_a_key_names_a_field_an_entry_or_a_field_of_every_entry() -> None:
    record = _phenomenon(category="open", observables__Z__values="open", observables__values="open")
    assert not misplaced_maturity(record)


def test_a_field_of_a_list_without_entries_is_named_by_its_schema() -> None:
    assert not misplaced_maturity(_phenomenon(manifestations__form="open"))


def test_a_key_naming_no_field_or_no_entry_is_reported() -> None:
    record = _phenomenon(observables__W__values="open", categry="open")
    assert texts(misplaced_maturity(record)) == [
        "maturity.observables.W.values: names no field of the record",
        "maturity.categry: names no field of the record",
    ]


def test_a_misspelled_key_is_reported_in_a_worked_inquiry(tmp_path: Path) -> None:
    case = "earth-system-tipping-cascades"
    shutil.copytree(EXAMPLES / case, tmp_path / case)
    path = tmp_path / case / "phenomenon.yml"
    text = path.read_text(encoding="utf-8")
    assert "  observables.Z.values: open" in text
    path.write_text(text.replace("  observables.Z.values: open", "  observables.Z.value: open"))
    rules = {x.finding.rule.id for x in check_workspace(load_workspace(tmp_path))}
    assert "completeness/misplaced-maturity" in rules
