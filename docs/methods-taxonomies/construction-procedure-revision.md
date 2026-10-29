---
tags:
  - tasks
index: "[Methods for taxonomies](docs/methods-taxonomies/_index.md)"
aliases:
  - Construction procedure revision ledger
---
# Construction procedure revision

## Task state

- [ ] **Phase 1 — global scope contract:** implemented and awaiting review in the [feature-system scope contract](construction-procedure.md#^scope-output-boundary) and [planned taxonomy-layer routes](taxonomy-extension-plan.md).
- [ ] **Phase 2 — formal contracts:** pending approval of Phase 1; specify the assumptions and guarantees of each formal operation.
- [ ] **Phase 3 — algorithms and examples:** blocked by Phase 2; correct each procedure and its complexity statement, then update the worked examples.
- [ ] **Phase 4 — final consistency pass:** blocked by Phases 2 and 3; reconcile terminology and navigation, then close the remaining review markers.

## Active constraints

- The [feature-system output boundary](construction-procedure.md#^scope-output-boundary) stops before taxa; the separate [taxonomy-layer route comparison](taxonomy-extension-plan.md) owns the taxonomic layer.
- The [applicability boundary](construction-procedure.md#^applicability-guarantees) restricts formal guarantees to finite, crisp analyzed tables and requires a documented missing-observation policy.
- The [dependency contract](construction-procedure.md#^def-dependency-languages) separates functional dependencies in the many-valued table from positive Horn implications in the scaled context.
- An `==FIX:...==` marker remains until the user approves its correction.

## Open questions

- Does the Phase 1 wording express the three intended boundaries?
- Which [proposed taxonomy-layer route](taxonomy-extension-plan.md) should govern the later taxonomy layer?

## Provenance

- The current file state is authoritative for every later edit.
- The formal boundaries draw on the [original Rough Set formulation](https://link.springer.com/article/10.1007/BF01001956) and the standard [Formal Concept Analysis treatment](https://link.springer.com/book/10.1007/978-3-642-59830-2).
- No delegated agent contributed to Phase 1.

## Decision log

- **2026-09-10:** Retain the narrower feature-system objective and plan the taxonomy layer separately.
- **2026-09-10:** Restrict formal guarantees to finite, crisp tables with documented handling of missing observations.
- **2026-09-10:** Type dependencies by representation: functional dependence in the many-valued table and positive Horn implication in the scaled FCA context.
