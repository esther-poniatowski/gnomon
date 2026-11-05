"""
The symbol table of a problem: the declarations collected from its records, those that no
grammatical field reaches, and the vocabulary record of the problem, a YAML view bound to the schema
``gnomon:view.vocabulary@1`` that a renderer displays as the other views.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Iterable, Iterator, Mapping

import yaml

from .. import findings as rules
from ..findings import Finding, Key, finding
from ..identifiers import PLACEHOLDER_SEGMENT, split_reference
from ..latex import declared_notations, symbol_form
from ..leftovers import strip_leftovers
from .declarations import Declaration, declarations
from .interactions import interaction_graph
from .layout import (
    GENERATED_KINDS,
    PATH_REFERENCE,
    TYPE_PATH_REFERENCE,
    cited,
    formulas,
    identifiers,
    items_of,
    reach,
    upstream_of,
)
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


def problem_records(directory: Path) -> list[Mapping[str, Any]]:
    """Return the records that fill the problem of ``directory``, as the checks read them: the
    records of a generated kind, such as its table ``vocabulary.yml``, and the templates not yet
    started are left out, and a started record is read without its leftovers of the template."""
    loaded = [
        yaml.safe_load(path.read_text(encoding="utf-8")) for path in sorted(directory.glob("*.yml"))
    ]
    return [
        strip_leftovers(record)[0]
        for record in loaded
        if isinstance(record, Mapping)
        and record.get("type") not in GENERATED_KINDS
        and not PLACEHOLDER_SEGMENT.search(str(record.get("id", "")))
    ]


def _strings(node: Any) -> Iterator[str]:
    """Yield every string value that a record holds, at any depth."""
    if isinstance(node, str):
        yield node
    elif isinstance(node, Mapping):
        for value in node.values():
            yield from _strings(value)
    elif isinstance(node, list):
        for item in node:
            yield from _strings(item)


def symbol_uses(
    records: Iterable[Mapping[str, Any]],
) -> tuple[set[str], set[tuple[str, str]]]:
    """Return the symbols that the grammatical fields of the records name: the bare symbols of the
    expressions and of the reference fields, and each dotted identifier as its record and symbol.

    A prose field is opaque, so a symbol named only in a reading or a name counts as no use.

    >>> bare, dotted = symbol_uses([{"type": "phenomenon", "target_system": "system.a",
    ...     "observables": [{"symbol": "E", "name": "energy E", "signature": ["t"],
    ...                      "expression": "mean_{x}( u(x, t) )"}],
    ...     "data": [{"measures": "system.a.nu"}]}])
    >>> sorted(bare), sorted(dotted)
    (['mean', 't', 'u', 'x'], [('system.a', 'nu')])
    """
    bare: set[str] = set()
    dotted: set[tuple[str, str]] = set()
    for record in records:
        for _, _, text, _ in formulas(record):
            bare |= identifiers(text)
        for _, _, value in cited(record):
            bare |= {name for _, name in items_of(value) if isinstance(name, str)}
        for path in (*PATH_REFERENCE, *TYPE_PATH_REFERENCE.get(str(record.get("type", "")), ())):
            bare |= {name for _, name in reach(record, path)}
        dotted |= {named for text in _strings(record) if (named := split_reference(text))}
    return bare, dotted


def unused_declarations(directory: Path, registry: Path | None = None) -> list[tuple[str, Finding]]:
    """Return every quantity the problem declares that no grammatical field of it names.

    The declarations span the records of the problem, so each finding comes with the identifier of
    the record that declares the quantity.

    A declaration that nothing reaches is either a stray specification or the trace of a law the
    record never wrote, and the two are told apart by reading. A use is read from the fields that
    a grammar declares, as :func:`symbol_uses` collects them, since a prose field is opaque to
    every tool.

    Only the blocks of :data:`REACHED` are reported. A manifestation or an observable is terminal
    by design, since a question reaches it from outside the problem or nothing reaches it at all.
    """
    bare, dotted = symbol_uses(problem_records(directory))
    return [
        (
            declaration.record,
            finding(
                rules.VOCABULARY_UNUSED_DECLARATION,
                f"{declaration.block}.{declaration.symbol}: declared and never used",
                declaration.block,
                Key(declaration.symbol),
            ),
        )
        for declaration in load_problem(directory, registry).declarations
        if declaration.block in REACHED
        and declaration.symbol not in bare
        and (declaration.record, declaration.symbol) not in dotted
    ]


def load_problem(directory: Path, registry: Path | None = None) -> Problem:
    """Collect the vocabulary of the problem whose records fill ``directory``."""
    problem = Problem(name=directory.resolve().name, canonical=canonical_operators(registry))
    records = problem_records(directory)
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
