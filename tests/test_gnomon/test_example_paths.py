"""Presence of the worked examples that the fixture-driven tests read.

The tests of symbol resolution, inquiry records and itineraries skip when they find no example
folder. A wrong location would therefore turn them into skips rather than failures. This test
fails instead.
"""

from __future__ import annotations

from .paths import EXAMPLES, EXPECTED_CASES


def test_every_worked_example_folder_is_present() -> None:
    """The examples folder exists and holds the folder of each expected inquiry."""
    assert EXAMPLES.is_dir(), f"the examples folder is missing: {EXAMPLES}"
    missing = [name for name in EXPECTED_CASES if not (EXAMPLES / name).is_dir()]
    assert not missing, f"example folders missing under {EXAMPLES}: {missing}"
