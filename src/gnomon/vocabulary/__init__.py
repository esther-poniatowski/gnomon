"""
Symbols and operators of an inquiry, collected from the records that declare them.

Three vocabularies meet in a filled inquiry, and they differ by who writes them and how far
they reach:

- the fields and their option lists, fixed by the framework and written by the designer;
- the symbols of one problem (constituents, index sets, variables, parameters, observables),
  written by the author of that problem and scoped to its records;
- the operators, whose canonical part the framework supplies and whose remainder each problem
  declares for its own formulas.

This module owns the second and third. It collects the symbols a problem declares, resolves the
operators available to each of its records, and renders the table an author consults before
choosing a new symbol.

Modules
-------
layout
    Locate the declarations, the formulas and the references of a record, and walk them.
declarations
    Collect the symbols and the units that a record declares, and check its references.
operators
    Collect the operators that a formula may call, and check the arity of each call.
structure
    Check the declarations of a record that read no other record.
resolution
    Resolve the identifiers of a record against the symbols and operators it can see.
signatures
    Check the signature of a defined quantity against the indices its definition leaves free.
coordinates
    Check the coordinates of a derivative against the argument that it differentiates.
variants
    Check the entries that reach beyond the variants that bear them.
interactions
    Read the organization of a record as a directed graph, and check its relations.
table
    Build and render the symbol table of a problem, and find the declarations unused.

See Also
--------
data/operators.yml : the operator vocabulary the framework supplies.
"""

from __future__ import annotations

from .declarations import (
    ID_UNITS,
    REFERENCE_TOKEN,
    Declaration,
    dangling_references,
    declarations,
    references,
    repeated_symbols,
    units,
)
from .interactions import (
    influence_places,
    interaction_graph,
    joins,
    malformed_relations,
    misrouted_interactions,
    unordered_interactions,
)
from .layout import (
    DECLARING,
    FORMULA,
    NESTED_FORMULA,
    NESTED_REFERENCE,
    PATH_FORMULA,
    PATH_REFERENCE,
    RECORD_KINDS,
    REFERENCE,
    TOLERANCE_NAMES,
    TYPE_PATH_FORMULA,
    TYPE_PATH_REFERENCE,
    UPSTREAM_FIELD,
    WITHIN_ENTRY,
    WITHIN_MAPPING,
    along,
    calls,
    entries,
    formulas,
    generic,
    identifiers,
    indexed,
    items_of,
    reach,
    upstream_of,
    visible_records,
)
from .operators import (
    DATA,
    OPERATOR_REGISTRY,
    arities,
    canonical_operators,
    local_operators,
    mismatched_arity,
    operator_arity,
)
from .resolution import (
    misattributed_appeals,
    retired_in_use,
    unresolved,
    unresolved_names,
)
from .signatures import QUANTITY_BLOCKS, contradicted_signatures, free_indices
from .structure import (
    corrupted_notation,
    doubly_defined,
    misplaced_sharing,
    mistyped_symbols,
    split_expressions,
    unfixed_parameters,
    unowned_quantities,
    unselected_conditions,
    vacuous_shared,
)
from .table import (
    REACHED,
    Problem,
    as_data,
    load_problem,
    render_yaml,
    unused_declarations,
)
from .variants import (
    FORMAL_KEYS,
    declared_variants,
    misnamed_variant,
    overreaching_declarations,
    overreaching_entries,
    unborne_variants,
    variant_symbols,
)

__all__ = [
    "DATA",
    "DECLARING",
    "FORMAL_KEYS",
    "FORMULA",
    "ID_UNITS",
    "NESTED_FORMULA",
    "NESTED_REFERENCE",
    "OPERATOR_REGISTRY",
    "PATH_FORMULA",
    "PATH_REFERENCE",
    "QUANTITY_BLOCKS",
    "REACHED",
    "RECORD_KINDS",
    "REFERENCE",
    "REFERENCE_TOKEN",
    "TOLERANCE_NAMES",
    "TYPE_PATH_FORMULA",
    "TYPE_PATH_REFERENCE",
    "UPSTREAM_FIELD",
    "WITHIN_ENTRY",
    "WITHIN_MAPPING",
    "Declaration",
    "Problem",
    "along",
    "arities",
    "as_data",
    "calls",
    "canonical_operators",
    "contradicted_signatures",
    "corrupted_notation",
    "dangling_references",
    "declarations",
    "declared_variants",
    "doubly_defined",
    "entries",
    "formulas",
    "free_indices",
    "generic",
    "identifiers",
    "indexed",
    "influence_places",
    "interaction_graph",
    "items_of",
    "joins",
    "load_problem",
    "local_operators",
    "malformed_relations",
    "misattributed_appeals",
    "mismatched_arity",
    "misnamed_variant",
    "misplaced_sharing",
    "misrouted_interactions",
    "mistyped_symbols",
    "operator_arity",
    "overreaching_declarations",
    "overreaching_entries",
    "reach",
    "references",
    "render_yaml",
    "repeated_symbols",
    "retired_in_use",
    "split_expressions",
    "unborne_variants",
    "unfixed_parameters",
    "units",
    "unordered_interactions",
    "unowned_quantities",
    "unresolved",
    "unresolved_names",
    "unselected_conditions",
    "unused_declarations",
    "upstream_of",
    "vacuous_shared",
    "variant_symbols",
    "visible_records",
]
