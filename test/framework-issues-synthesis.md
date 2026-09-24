---
tags: []
index: "[Theoretical modeling tests](_index.md)"
aliases:
  - Framework issue synthesis
---
# Framework issue synthesis

The five trials reveal one general pattern: the forms capture basic inquiry structure. Typed fields lose distinctions when a project contains nested variation or composite outputs.

> [!TIP] Promotion rule
> Change the shared schema only when the same typed distinction recurs across cases or when splitting a record would change the admissible answers.

## Global changes

Global changes belong in the shared framework artifacts because local prose cannot preserve the required distinctions.

| Issue | Cases | Proposed change | Acceptance test |
| --- | --- | --- | --- |
| **Target variants.** One flat record cannot give structurally different class members their own schemas. | Active matter · Earth-system cascades · Microbial coexistence | Add an optional `variants[]` discriminated union. Each variant owns one complete member schema. Common declarations remain at the target root. | A selected variant yields one complete target schema without conditional prose. |
| **Formal roles.** Index domains are treated as constituents. Internal relations are treated as external interfaces. Forward maps are treated as coexistence laws. | Turbulence · Earth-system cascades · Delayed generalization | Separate mathematical domains and internal relations from constituents and external interfaces. Add `input-output` to the law functions. | Every formal object has the correct typed role. |
| **Observable construction.** Values stored as prose absorb how observables are constructed. | All five cases | Give each explanandum variable a structured derivation and repeatable axis records. Add an optional protocol for observing events over time, including censoring. | Declared inputs reconstruct every derived quantity. Formulas and qualifications no longer occupy `name` or `values`. |
| **Instance scope and uncertainty.** The scalar scope field conflates how instances vary with how claims quantify or average over them. | Delayed generalization · Turbulence · Earth-system cascades · Microbial coexistence | Replace scalar `scope_over_instances` with repeatable scope axes. Each axis records its variation source and statistical role. Quantification and conditioning become explicit. | Each scope form remains distinct and readable by software. |
| **Varied factors with unknown effects.** The `modulating` category presupposes a known effect when the effect is the research target. | Active matter · Earth-system cascades | Add `varied_factors[]` records that identify the varied object and define how the inquiry samples or compares its values. Keep the effect optional. | Exploration records what varies without asserting the result sought by the inquiry. |
| **Task obligations and accuracy.** One modal and accuracy block cannot encode the implication direction of theorems or heterogeneous fidelity targets. | Active matter · Turbulence · Earth-system cascades · Microbial coexistence | Make `required_accuracy` nullable and move accuracy into each match. Represent each requested implication as an ordered antecedent and consequent. | Each target has its own fidelity test. Necessary and sufficient claims can be assessed independently. |
| **Scoped virtues.** A virtue token does not state what must persist or which variation tests the conclusion. | Delayed generalization · Turbulence · Microbial coexistence | Replace virtue tokens with objects. Each virtue names the conclusion it qualifies and defines how to test that conclusion across declared variations. | Two assessors apply a virtue to the same declared object and scope. |
| **Provenance.** Only evidence for the phenomenon has a source slot. | Active matter · Earth-system cascades | Add optional source identifiers to technical entries and a bibliography for the record. Keep `phenomenon.data` restricted to evidence for the phenomenon. | A reviewer can trace each commitment without reconstructing its origin from surrounding prose. |

## Local edits

Local edits fix case scope or missing author choices. They should be completed without expanding the shared schema.

| Case | Local edit |
| --- | --- |
| **Active matter** | Split results for finite systems and the thermodynamic limit into linked questions. Split lattice and continuum targets unless one answer must quantify across both. Fix the sampled controls and spatial extent. |
| **Delayed generalization** | Fix the evaluation protocol and the admissible training class. |
| **Turbulence** | Name the forcing and boundary families. Split structural relations from numerical exponent targets until accuracy can be assigned to each target. |
| **Earth-system cascades** | Fix the target membership and the rule that matches warming trajectories. Complete the forecast contract with its temporal scope and evaluation criteria. |
| **Microbial coexistence** | Split necessary and sufficient claims under the current template. Narrow or separate the model families, then fix the resource supply. |

Unknown scientific results remain `open`. The schema must represent their status without supplying their values.

## Disposition

The designer ratified a reorientation of the records toward a modeling language: every declared quantity carries a symbol, and every formula is an expression over declared symbols. That reorientation absorbs or reduces most of the rows above, because several of them reported one defect seen from different directions — a field typed as a token or a prose string where a construction was required.

[The review state of every candidate and the implementation sequence](framework-corrections-handoff.md) record the disposition. This file retains the diagnosis and the acceptance test behind each row; it does not track implementation.
