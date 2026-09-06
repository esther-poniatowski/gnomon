---
tags:
  - table
index: "[Design documentation](_index.md)"
aliases:
  - Terminology alias table
---
# Terminology alias table

> [!INFO] Status
> Sibling to [classification table](_classification-table) and [refactor handoff](_handoff-refactor). Records eight alias clusters detected after Step A.2's six adversarial-audit passes. Each cluster names the same underlying object or field under multiple labels across the active design and the backup files. Step C migration consults this table before minting any new anchor and consolidates `^bk-` D's that turn out to share a referent.

---

## How to read this table

Each cluster row records:

- **Canonical term**: the label used in the active design (or, when the active design is silent, the label chosen by the project for forward use).
- **Surface variants**: every label encountered in source files (active or backup) that denotes the same referent.
- **Sources**: the files that use each variant.
- **Affected anchors**: the `^t<n>-` and `^bk-` anchors in [classification table](_classification-table) that name the same referent.
- **Resolution**: how the redundancy collapses during Step C migration — which anchor survives, which folds, which is reframed.

Anchors marked **(canonical)** are the survivors; anchors marked **(folds into X)** collapse against the canonical anchor during Step C; anchors marked **(grain-distinct)** describe the same referent at a different grain and survive as refinements of the canonical anchor.

---

## Cluster 1 — Assembly ≈ Argument bundle ≈ Argument graph ≈ Work unit ^cluster-assembly

A *target-relative selected configuration of canonical objects that records a path of justification toward an answer*.

| Variant | Sources |
| --- | --- |
| **assembly** / **assemblies** | Active design (canonical, 72 hits across `2-architecture/`, `3-aspect-specific/`) |
| **argument bundle** | `_backup/architecture-1-layered-model.md`, `_backup/arguments-reasoning/argument-bundles.md` |
| **argument graph** | `_backup/architecture-C.md` (macro level), `_backup/arguments-reasoning/argument-bundles.md` (Proposal G) |
| **work unit** / **WorkUnit** | `_backup/architecture-2-spec.md`, `_backup/architecture-2-audit.md` |
| **reasoning unit** | `_backup/architecture-1-layered-model.md` |

**Affected anchors**:

- `^t2-target-relative-assemblies` (active D — Keep) **(canonical)**
- `^bk-bundle-component-taxonomy` **(grain-distinct)** — refines the canonical anchor with seven sub-kinds (argument bundle / question-decomposition tree / minimal answer subgraph / answer object / issue bundle / alternative-route bundle / session-task bundle). The "argument bundle" sub-kind is the same as the canonical assembly; the other six are sub-shapes within the same object kind.
- `^bk-argument-graph-fields` **(folds into `^bk-bundle-fields`)** — the macro-level field schema is one ratified candidate answer to the bundle-fields open D, not a separate object kind.
- `^bk-work-unit` **(grain-distinct)** — the work unit is the assembly viewed as Goal + OperationGraph + Result; survives as a sub-shape under the bundle-component taxonomy (between the canonical assembly and the operation graph it carries).

**Resolution**: `^t2-target-relative-assemblies` survives as the canonical object-kind anchor. `^bk-bundle-component-taxonomy` refines it with seven sub-kinds. `^bk-argument-graph-fields` becomes Proposal C-macro under `^bk-bundle-fields`. `^bk-work-unit` is reframed as the work-unit sub-shape under the component taxonomy with its own field set (Goal + OperationGraph + Result).

## Cluster 2 — Operation schema ≈ Atomic act ≈ Primitive operation ≈ Operation type ^cluster-operation

A *fixed-signature primitive unit of computational/epistemic work*.

| Variant | Sources |
| --- | --- |
| **operation schema** | Active design (canonical), `_backup/architecture-2-spec.md`, `_backup/reasoning.md` |
| **operation application** | `_backup/architecture-2-spec.md` (the *invocation* of a schema on bound operands) |
| **primitive operation** / **primitive schema** | `_backup/reasoning.md`, `_backup/architecture-2-audit.md` |
| **atomic act** / **atomic epistemic act** | `_backup/arguments-reasoning/derivation-proof-encoding-E.md` |
| **operation type** | `_backup/architecture-2-spec.md` |

**Affected anchors**:

- `^t2-closed-operational-core` (now R after pass 2 reclassification) — the closed-library *mechanism*.
- `^t2-operation-primitiveness` (active open D) **(canonical for closure question)** — the four-alternative closure-justification question.
- `^bk-operation-schema-fields` **(canonical for declaration grain)** — the eight-field signature.
- `^bk-operation-application-binding` **(grain-distinct from declaration)** — the role-indexed binding rule for *invocation*.
- `^bk-primitive-library-init` **(canonical for library-content question)** — the 10–15-schema initial library across four families.
- `^bk-atomic-act-grain` **(folds into `^bk-primitive-library-init`)** — the 12-act inventory from BK/derivation-proof-E is one analytic-computational sub-family of the primitive library, not a separate grain decision.

**Resolution**: declaration question lives at `^bk-operation-schema-fields`; invocation question at `^bk-operation-application-binding`; closure question at `^t2-operation-primitiveness`; library-content question at `^bk-primitive-library-init`. `^bk-atomic-act-grain` collapses into the library-content question — the inspectable-composable-unit requirement is a property of every entry in the primitive library, not an autonomous grain decision.

## Cluster 3 — Motivation ≈ Generative rationale ≈ Strategic role ≈ Why-this-move ≈ Strategic objective ^cluster-motivation

The *recorded research judgment explaining why a step is the chosen one*.

| Variant | Sources |
| --- | --- |
| **motivation** | Active design (canonical, 33 hits) |
| **generative rationale** / **generative_rationale** | `_backup/architecture-2-spec.md` |
| **strategic role** / **strategic_role** | `_backup/arguments-reasoning/argument-bundles.md` (Proposal 2) |
| **strategic objective** | `_backup/architecture-2-spec.md` |
| **strategic function** | `_backup/arguments-reasoning/derivation-proof-encoding-C.md` |
| **why_this_move** | `_backup/arguments-reasoning/derivation-proof-encoding-G.md` |
| **preferred alternative** | Active `^t2-reasoning-annotation-fields` (one of five fields after the `^t1-non-arbitrary` M-split) |
| **diagnosed insufficiency** | `_backup/architecture-2-spec.md` (the *gap* dimension of motivation) |

**Affected anchors**:

- `^t2-reasoning-annotation-fields` (active D — Keep) **(canonical)** — five strategic-annotation fields: target / move / principle / gap / preferred alternative.
- `^bk-three-axis-annotation` **(grain-distinct)** — splits motivation across operative-property and strategic-function axes; refines the *move* and *preferred alternative* fields of the canonical D.
- `^bk-planning-schema-fields` **(grain-distinct, planning grain)** — five fields at the planning-step grain (local epistemic state / diagnosed insufficiency / strategic objective / generative rationale / epistemic gain). "Diagnosed insufficiency" aliases "gap"; "strategic objective" aliases "move"; "generative rationale" aliases "principle".
- `^bk-question-to-goal-mapping` **(grain-distinct, inquiry grain)** — the planning judgment that selects a goal given a question; one occurrence of motivation at the topmost grain.
- `^bk-forward-productivity` **(grain-distinct, forward-direction prong)** — the third prong of the local-intelligibility criterion; complements the "preferred alternative" (contrastive prong) and "principle" (achievement prong) of the canonical D.

**Resolution**: `^t2-reasoning-annotation-fields` is the canonical home for the motivational field set. The other anchors describe the same field at different grains (planning-grain, inquiry-grain, axis-refinement, forward-direction prong). Step C consolidates by recording each anchor as a refinement or grain-shift of the canonical D, not as an independent field.

## Cluster 4 — Gap ≈ Obstacle ≈ Diagnosed insufficiency ≈ Deficiency ≈ Local goal ^cluster-gap

The *recorded statement of what is missing or what blocks immediate progress*.

| Variant | Sources |
| --- | --- |
| **gap** / **gap_closed** | Active design (canonical), `_backup/arguments-reasoning/argument-bundles.md` (Proposal 2) |
| **obstacle** | `_backup/arguments-reasoning/derivation-proof-encoding-G.md` (proof-state field), `_backup/architecture-C.md` (validator referent) |
| **diagnosed insufficiency** | `_backup/architecture-2-spec.md` (planning-schema field) |
| **deficiency** | Active `_index.md` and several backup files |
| **local goal** | `_backup/arguments-reasoning/argument-bundles.md` (Proposal 2) |

**Affected anchors**:

- *gap* field of `^t2-reasoning-annotation-fields` (active, after the `^t1-non-arbitrary` M-split) **(canonical)**.
- *diagnosed insufficiency* field of `^bk-planning-schema-fields` **(folds into the canonical gap field at planning grain)**.
- *obstacle* field of `^bk-proof-state-fields` **(grain-distinct, proof-state encoding)** — same field, conditional on the state-transition encoding alternative being adopted.
- `^bk-obstacle-typology` **(canonical for the gap-vocabulary question)** — the 8-kind typology of obstacle/gap values; applies to whichever encoding hosts the field.

**Resolution**: the gap field has one canonical home (`^t2-reasoning-annotation-fields`), with grain-distinct refinements at the planning grain (`^bk-planning-schema-fields`) and the proof-state grain (`^bk-proof-state-fields`). The 8-kind typology is the candidate enum body for the gap field across all grains, not a separate anchor per grain.

## Cluster 5 — Epistemic gain ≈ Conceptual effect ≈ Step contribution ≈ Cognitive gain ≈ Gain kind ^cluster-gain

The *recorded statement of what becomes available after a step*.

| Variant | Sources |
| --- | --- |
| **epistemic gain** | `_backup/architecture-2-spec.md`, `_backup/criteria-framework.md` (retired) |
| **gain_kind** / **gain kind** | Active `^t3-gain-kind-enum` (canonical) |
| **conceptual effect** | `_backup/criteria-framework.md` (retired), `_backup/arguments-reasoning/argument-bundles.md` (Proposal 2) |
| **step contribution** | `_classification-table.md` cross-cutting note (BK-minted from criteria-framework, retired) |
| **cognitive gain** | `_backup/criteria-framework.md` (retired) |
| **forward productivity** | `_backup/arguments-reasoning/derivation-proof-encoding-G.md` |

**Affected anchors**:

- `^t3-gain-kind-enum` (active open D) **(canonical)** — the closed enum of gain values.
- `^t3-step-contribution-enum` (BK D minted from the retired criteria-framework backup) **(folds into `^t3-gain-kind-enum`)** — the cross-cutting note at line 472 of [classification table](_classification-table) explicitly says these "describe the same step from dual angles". Merger pre-decided.
- `^bk-forward-productivity` **(folds into `^t3-gain-kind-enum`)** — the forward-direction prong of the local-intelligibility criterion is the same field as gain-kind, named under a different label. Merger.
- *epistemic gain* field of `^bk-planning-schema-fields` **(folds into the canonical gain field at planning grain)**.
- *conceptual effect* field of Proposal 2 under `^bk-bundle-fields` **(folds into the canonical gain field at per-step grain)**.

**Resolution**: the gain field has one canonical home (`^t3-gain-kind-enum`), with grain-distinct uses at planning, per-step, and forward-direction grains. Four anchors (`^t3-step-contribution-enum`, `^bk-forward-productivity`, planning's epistemic-gain field, Proposal 2's conceptual-effect field) collapse on resolution.

## Cluster 6 — Subquestion ≈ Sub-goal ≈ Subgoal ≈ Question decomposition ^cluster-subq

A *child node in the question-decomposition tree*.

| Variant | Sources |
| --- | --- |
| **subquestion** | Active design (canonical, 28 hits), `_backup/workflow-for-users.md` |
| **sub-goal** / **subgoal** | `_backup/arguments-reasoning/derivation-proof-encoding-G.md`, `_backup/architecture-2-spec.md` |
| **branch** | `_backup/criteria-framework.md` (retired) |
| **question decomposition** / **question-decomposition tree** | `_backup/arguments-reasoning/argument-bundles.md`, `^bk-bundle-component-taxonomy` |

**Affected anchors**:

- *question-decomposition tree* sub-kind of `^bk-bundle-component-taxonomy` **(canonical)**.
- `^t3-inquiry-format` (rename target of `^t3-minimal-answer-subgraph`) **(grain-distinct)** — the inquiry's answer is the minimal subgraph rooted at the target question; the decomposition-tree sub-kind is the structural support of that answer.
- `^bk-subquestion-forms` **(folds into the question-decomposition-tree sub-kind)** — the 9-prong subquestion typology is the candidate enum body for *what kind of subquestion* a child node carries, not a separate decision.
- *sub_goal* field of `^bk-argument-segment-fields` **(folds into the canonical decomposition-tree pointer)**.

**Resolution**: the question-decomposition tree has one canonical home (the sub-kind in `^bk-bundle-component-taxonomy`). `^bk-subquestion-forms` becomes a candidate enum body for the sub-kind; `^bk-argument-segment-fields`'s `sub_goal` field is the per-segment pointer into the tree.

## Cluster 7 — Registry ≈ Index ≈ Catalogue ≈ Store ^cluster-registry

A *derived addressable lookup structure*.

| Variant | Sources |
| --- | --- |
| **registry** | Active design (canonical), all backup files |
| **index** | Active design (canonical for read-side projections), backup files |
| **catalogue** / **catalog** | Active `^t3-registry-component-taxonomy` (canonical realisation of the catalogue concept). |
| **store** | Active `^t3-registry-component-taxonomy` (canonical realisation of the store concept). |

**Affected anchors**:

- `^t3-registry-component-taxonomy` (active D, eleven-component inventory) **(canonical)** — executed from the former `^bk-registry-component-taxonomy` plan.
- `^t3-registry-scope-per-scale` (active open question) **(grain-distinct)** — workspace / project / module strata, orthogonal to the component partition. Executed as an open question from the former `^bk-registry-scale-layering` plan.
- `^t3-dependency-graph-first-class` (R after the queryability split) **(folds into `^t3-registry-component-taxonomy`'s dependency-graph component)** — same object, different label.
- `^t3-dependency-graph-artifact` (active open question) — the maintenance-policy refinement of the dependency-graph component.
- The former `^bk-terminology-enforcement` (validator-policy) **(grain-distinct, still pending)** — the *terminology-index* component of the taxonomy is the underlying registry that the linter consumes; the linter realisation remains to be drafted at the validation work.
- `^t3-open-questions-index` (active D) **(refinement)** — per-component schema under the umbrella taxonomy. Executed from the former `^bk-open-questions-registry` plan.
- `^t3-terminology-index-schema` (active D) **(refinement)** — per-component schema for the terminology-index component.
- The former `^bk-dependencies-registry` **(superseded)** — its content is fully covered by the canonical object store, the dependency-graph component, and the reverse-dependency-index component of `^t3-registry-component-taxonomy`.

**Resolution**: the eleven-component taxonomy is the canonical decomposition; the brought-forward execution has lifted the BK plans into active `^t3-*` anchors. Step C collapses any remaining individual-component aliases against the taxonomy.

## Cluster 8 — Validator rule ≈ Validator check ≈ Audit defect ≈ Integrity invariant ^cluster-validator

A *well-formedness check enforced at validation time*.

| Variant | Sources |
| --- | --- |
| **validation rule** / **validator rule** | Active `^t2-validator-placement` (canonical), backup files |
| **integrity invariant** / **invariant** | `_backup/architecture-C.md`, `_backup/schema-fields-base.md` |
| **audit defect** | `_backup/arguments-reasoning/derivation-proof-encoding-G.md` |
| **integrity check** | Active `^t3-registry-component-taxonomy` (the integrity-report-structures component of the catalogue). |

**Affected anchors**:

- `^t2-validator-placement` (active D — Keep) **(canonical for placement question)**.
- `^t2-validation-mechanizability` (rename target of `^t2-validation-placement`) **(canonical for mechanical-vs-judgment question)**.
- `^bk-audit-defects` **(canonical for the defect taxonomy)** — six-defect enum: blind_step / hidden_obstacle / spurious_move / teleological_gap / untyped_transition / state_ambiguity.
- `^bk-schema-enforcement-policy`, `^bk-teleological-closure-rule`, `^bk-kernel-ratio-rule`, `^bk-validation-gating`, `^bk-separability-test`, `^bk-progress-non-rhetoric-rule`, `^bk-inter-object-invariants`, `^bk-source-credibility-annotation`, `^bk-weakest-link-query`, `^bk-explanation-summarisation`, `^bk-cross-argument-extraction` **(rules that detect specific defects)** — each rule corresponds to one or more defect kinds in `^bk-audit-defects`. Step C records the mapping; the rules survive as enforcement specifications, the defect taxonomy as the umbrella.

**Resolution**: the defect taxonomy `^bk-audit-defects` is the umbrella. Each individual rule survives as an enforcement specification; Step C records, per rule, which defect(s) it detects. Mappings:

- `blind_step` ← detected by `^bk-three-axis-annotation` + `^bk-separability-test` (jointly enforce that warrant + operative + strategic are non-collapsible)
- `hidden_obstacle` ← detected by `^bk-progress-non-rhetoric-rule` (every progress entry has a typed obstacle reference)
- `spurious_move` ← detected by `^bk-kernel-ratio-rule` (kernel-flag ratio bounded)
- `teleological_gap` ← detected by `^bk-teleological-closure-rule` (every segment resolves a registered obstacle)
- `untyped_transition` ← detected by `^bk-schema-enforcement-policy` (`additionalProperties: false` + enum-typed move kind)
- `state_ambiguity` ← detected by `^bk-validation-gating` (hard-gate prevents writes that would leave state under-specified)

---

## Step C usage

Before minting any new anchor in Step C, run a literal-substring search against this table's *Variant* column for every term in the anchor's source paragraph. If the term appears, the new anchor is a candidate alias; consult the *Resolution* row to decide whether to fold, refine, or mint.

Maintenance: when Step C migration discovers a new alias not listed here, add a row. When a cluster's resolution changes, update the *Resolution* row in place.
