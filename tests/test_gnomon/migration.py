"""The worked answers that keep the form of the former answer, until the goal `model-design` migrates them."""

from __future__ import annotations

from typing import Any, Mapping

import pytest

#: The keys of the former answer, which held its model; the worked answers keep them until the
#: pilot of the goal `model-design` migrates them to model records, as the task list states.
FORMER_ANSWER_KEYS = frozenset(
    {"statement", "constituents", "index_sets", "variables", "parameters", "laws", "organization",
     "realizations", "idealizations", "explanans"}
)

#: The mark of a check that a record of the former answer cannot pass before its migration.
AWAITING_MIGRATION = pytest.mark.xfail(
    strict=True, reason="the answer awaits its migration under the goal `model-design`"
)


def awaiting_migration(record: Mapping[str, Any]) -> bool:
    """Whether a worked answer still holds the keys of the former answer."""
    return record.get("type") == "answer" and bool(FORMER_ANSWER_KEYS & set(record))
