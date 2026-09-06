---
tags:
  - tensions
index: "[Framework-level criteria](_index.md)"
aliases:
  - Irreducible tensions
---
# Irreducible tensions between framework criteria

Five tensions hold between the framework-level criteria. They cannot be dissolved by better design; each must be recorded at every design decision it touches, so that the chosen tradeoff is explicit and auditable.

Each tension names two opposing framework-level criteria and the resolution pattern that the architecture adopts to live with the tension rather than remove it. The tension anchors keep their `^t2-x*` names until the migration step explicitly redirects them.

---

## X1 — Expressivity vs. non-arbitrariness ^t2-x1

[t1-expressivity](expressive-depth#^t1-reasoning-types-coverage) demands support for reasoning patterns not anticipated by the schema inventory. [t1-non-arbitrary](reasoning-integrity#^t1-served-goal) demands that operations be schema-governed. Either the schema inventory is closed (and expressivity is bounded) or it is open (and non-arbitrariness is nominal).

*Resolution pattern*: adopt a schema calculus — a small set of primitive schema constructors from which schemas for domains are derived. This bounds the schema space structurally while admitting new schemas under principled construction. Settled at [t2-operation-primitiveness](../2-architecture/operations-and-modes#^t2-operation-primitiveness) (open) and instantiated in [Operation schemas](../3-aspect-specific/operation-schemas).

## X2 — Formalization depth vs. usability ^t2-x2

[t1-intelligibility](reasoning-integrity#^t1-justification-levels) demands that every step carry licensing, strategic, and explanatory justification. [t1-partial-formalization](expressive-depth#^t1-partial-formalization) and [t1-feasibility](cost-ergonomics#^t1-system-scale) demand that the annotation burden not exceed what researchers tolerate. These are in irreducible tension for moderately complex proofs and informal arguments.

*Resolution pattern*: each profile partitions fields into mandatory and optional sets, with named guarantees that weaken when the profile loosens. Selected at [t2-reasoning-annotation-fields](../2-architecture/reasoning-structure#^t2-reasoning-annotation-fields) and instantiated in [Reasoning-annotation field set](../3-aspect-specific/reasoning-fields). Profile contents deferred to [t2-partial-formalization-profiles](../2-architecture/granularity#^t2-partial-formalization-profiles).

## X3 — Narrow ontology vs. coverage completeness ^t2-x3

[Object-kind set smallness](../2-architecture/object-kinds#^t2-ontology-small) demands few object kinds. [t1-activity-coverage](expressive-depth#^t1-activity-coverage) and [t1-reasoning-types-coverage](expressive-depth#^t1-reasoning-types-coverage) demand that the ontology span every epistemic move and every reasoning kind.

*Resolution pattern*: the operational five-condition test at [object-kind admission](../2-architecture/object-kinds#^t2-object-kind-admission) is the discriminator. A candidate is admitted as a kind only if it passes all five; otherwise it becomes a field, status, relation, or annotation.

## X4 — Acyclicity vs. revision ^t2-x4

Reasoning snapshots must be DAGs ([snapshot acyclicity](../2-architecture/relations-graph#^t2-snapshot-dag-property), discharge accounting). Research reasoning is inherently cyclic (revision, retraction, goal reformulation). The representations must support both.

*Resolution pattern*: the framework distinguishes snapshot slices (DAG-valid) from revision history (cyclic edges allowed, with temporal stamps). A snapshot is a temporal cross-section; revisions move the system from one snapshot to another. Recorded at [t2-revision-feedback](../2-architecture/validity-revision#^t2-revision-feedback).

## X5 — Formal expression vs. authoring cost ^t2-x5

[t1-formal-expression](framework-foundations#^t1-formal-expression) requires every semantic field to be grammar-bound — no prose stand-ins anywhere the framework reads. [t1-feasibility](cost-ergonomics#^t1-system-scale) demands that authoring stay within the cost a researcher tolerates. Writing a grammatical value for a strategic rationale, a route-selection record, or an explanatory gain is heavier than writing a sentence; for in-progress thinking, the cost of formalizing on the fly may exceed the cost of recording the move at all.

This is distinct from [X2](#^t2-x2): X2 trades **how many aspects** carry annotations (breadth) against burden; X5 trades **how grammatical each present annotation must be** (depth-per-aspect) against burden, given that the formal-expression criterion forecloses sub-formal compromise on any semantic field.

*Resolution pattern*: split the field surface into two disjoint classes per the formal-expression criterion. Semantic fields are grammar-bound without compromise; the carve-out for cost relief is the explicit class of **unessential fields** (TODO, FIX, remark, comment) that the framework stores but does not read. The authoring-cost pressure is absorbed by (a) the partial-formalization carve-out at [t1-partial-formalization](expressive-depth#^t1-partial-formalization) — annotations may be *absent* — and (b) the unessential-fields carve-out, where prose remains permitted because nothing depends on it. The cost of *supplying* a grammatical semantic value is not relieved; it is paid. Recorded at [t2-field-typing](../2-architecture/object-kinds#^t2-field-typing); reasoning-field grammars are staged as an open question in [the fleeting-ideas catalogue](../_fleeting-ideas.md).
