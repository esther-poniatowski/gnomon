"""
The symbol table of a problem: the declarations collected from its records, those that nothing
reaches, and the vocabulary record of the problem, a YAML view bound to the schema
``gnomon:view.vocabulary@1`` that a renderer displays as the other views.
"""

from __future__ import annotations

import re
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Mapping

import yaml

from .. import findings as rules
from ..findings import Finding, Key, finding
from ..latex import declared_notations, symbol_form
from .declarations import Declaration, declarations
from .interactions import interaction_graph
from .layout import upstream_of
from .operators import canonical_operators, local_operators


@dataclass
class Problem:
    """The vocabulary of one problem, collected from the records filled for it.

    Attributes
    ----------
    name : str
        The directory holding the records.
    declarations : list of Declaration
        Every symbol the problem declares, in record then block order.
    canonical : frozenset of str
        The operators the framework supplies.
    local : dict
        The operators the problem declares, each mapped to its name.
    interactions : list of dict
        The directed interaction graph its target system states, one entry per edge.
    notations : dict
        The LaTeX notation that each declared symbol states, empty when it states none.
    """

    name: str
    declarations: list[Declaration] = field(default_factory=list)
    canonical: frozenset[str] = frozenset()
    local: dict[str, str] = field(default_factory=dict)
    interactions: list[dict[str, Any]] = field(default_factory=list)
    notations: dict[str, str] = field(default_factory=dict)

    @property
    def operators(self) -> frozenset[str]:
        """Every operator the formulas of this problem may use."""
        return self.canonical | frozenset(self.local)

    def collisions(self) -> dict[str, list[str]]:
        """Return each symbol declared by more than one record, with those records.

        A symbol is unique within a record, so a repetition across records is admitted. It is
        reported because the same letter then denotes two quantities the author must keep apart.
        """
        by_symbol: dict[str, list[str]] = {}
        for entry in self.declarations:
            by_symbol.setdefault(entry.symbol, []).append(entry.record)
        return {s: r for s, r in by_symbol.items() if len(set(r)) > 1}


#: Blocks whose declarations exist to be reached by another field. A manifestation, a source of
#: variation, an observable or a feature is terminal: it states the phenomenon rather than
#: serving it.
REACHED: frozenset[str] = frozenset({"constituents", "index_sets", "variables", "parameters"})


def unused_declarations(directory: Path, registry: Path | None = None) -> list[tuple[str, Finding]]:
    """Return every quantity the problem declares that no other field of it mentions.

    The declarations span the records of the problem, so each finding comes with the identifier of
    the record that declares the quantity.

    A declaration that nothing reaches is either a stray specification or the trace of a law the
    record never wrote, and the two are told apart by reading. The count is lexical, as the
    operator check is: a symbol occurring once occurs only at its own declaration.

    Only the blocks of :data:`REACHED` are reported. A manifestation or an observable is terminal
    by design, since a question reaches it from outside the problem or nothing reaches it at all.
    """
    sources = [p for p in sorted(directory.glob("*.yml")) if p.name != "vocabulary.yml"]
    text = " ".join(p.read_text(encoding="utf-8") for p in sources)
    found = []
    for declaration in load_problem(directory, registry).declarations:
        if declaration.block not in REACHED:
            continue
        symbol = re.escape(declaration.symbol)
        if len(re.findall(rf"(?<![\w.]){symbol}(?![\w])", text)) <= 1:
            found.append(
                (
                    declaration.record,
                    finding(
                        rules.VOCABULARY_UNUSED_DECLARATION,
                        f"{declaration.block}.{declaration.symbol}: declared and never used",
                        declaration.block,
                        Key(declaration.symbol),
                    ),
                )
            )
    return found


def load_problem(directory: Path, registry: Path | None = None) -> Problem:
    """Collect the vocabulary of the problem whose records fill ``directory``."""
    problem = Problem(name=directory.name, canonical=canonical_operators(registry))
    loaded = [
        yaml.safe_load(path.read_text(encoding="utf-8")) for path in sorted(directory.glob("*.yml"))
    ]
    records = [record for record in loaded if isinstance(record, Mapping)]
    by_id = {str(record["id"]): record for record in records if "id" in record}
    problem.notations = declared_notations(r for r in records if r.get("type") != "operators")
    for record in records:
        problem.declarations.extend(declarations(record))
        problem.local.update(local_operators(record))
        problem.interactions.extend(interaction_graph(record, upstream_of(record, by_id)))
    return problem


def as_data(problem: Problem) -> dict[str, Any]:
    """Return the vocabulary of a problem in the record form it is stored in."""
    return {
        "_schema": "gnomon:view.vocabulary@1",
        "id": f"vocab.{problem.name}",
        "type": "vocabulary",
        "title": f"Vocabulary of {problem.name}",
        "problem": problem.name,
        "generated_by": "gnomon vocabulary",
        "symbols": [
            {
                "symbol": entry.symbol,
                "declared_in": entry.record,
                "block": entry.block,
                "signature": list(entry.signature),
                "name": entry.name,
                "latex": symbol_form(entry.symbol, problem.notations),
            }
            for entry in sorted(problem.declarations, key=lambda d: (d.record, d.block, d.symbol))
        ],
        "reused_across_records": {
            s: sorted(set(r)) for s, r in sorted(problem.collisions().items())
        },
        "operators": {
            "canonical": sorted(problem.canonical),
            "declared": dict(sorted(problem.local.items())),
        },
        "interactions": problem.interactions,
    }


def render_yaml(problem: Problem) -> str:
    """Return the vocabulary as the YAML the command writes."""
    header = (
        "# Generated by `gnomon vocabulary` from the filled records. Edit a record, not this"
        " file.\n"
        "# A symbol is unique within its record, so the same letter may return under another"
        " record.\n"
    )
    return header + yaml.safe_dump(as_data(problem), sort_keys=False, allow_unicode=True, width=100)
