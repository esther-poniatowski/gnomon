"""Locations that the test modules read: the repository root and the worked examples.

The worked examples are the filled records of seven inquiries, one folder per inquiry. Several
test modules parametrize over these folders and skip when none is found, so the location is fixed
here once, and ``test_example_paths.py`` fails when it does not hold the expected folders.
"""

from __future__ import annotations

from pathlib import Path

#: Root of the repository.
ROOT = Path(__file__).resolve().parents[2]

#: Folder of the worked examples, one subfolder per inquiry.
EXAMPLES = ROOT / "examples"

#: The inquiries whose folders must exist under ``EXAMPLES``.
EXPECTED_CASES = (
    "active-matter-phase-exploration",
    "earth-system-tipping-cascades",
    "grokking-delayed-generalization",
    "microbial-stable-coexistence",
    "neural-tangent-kernel-model-knowledge",
    "swift-hohenberg-localized-states",
    "turbulence-anomalous-scaling",
)
