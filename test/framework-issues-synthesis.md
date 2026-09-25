---
tags: []
index: "[Theoretical modeling tests](test/_index.md)"
aliases:
  - Framework issue synthesis
---
# Framework issue synthesis

Across the five trials, the forms capture the basic structure of an inquiry. However, their typed fields lose distinctions when a project contains nested variation or composite outputs.

> [!TIP] Promotion rule
> Amend the shared schema only when the same typed distinction recurs across cases or when splitting a record would alter the admissible answers.

## Global changes

Each global change belongs in the artifacts that all cases share, because prose inside one case record cannot preserve the distinction at stake.

| Issue | Cases | Proposed change | Acceptance test |
| --- | --- | --- | --- |
| **Target variants.** One flat record cannot give structurally different class members their own schemas. | Active matter · Tipping cascades · Microbial coexistence | Add an optional `variants[]` discriminated union. Each variant owns one complete member schema. Common declarations remain at the target root. | A selected variant yields one complete target schema without conditional prose. |
| **Formal roles.** Three kinds of formal object take a wrong role: index domains are treated as constituents, internal relations as external interfaces, and forward maps as coexistence laws. | Turbulence · Tipping cascades · Delayed generalization | Separate mathematical domains and internal relations from constituents and external interfaces. Add `input-output` to the law functions. | Every formal object has the correct typed role. |
| **Observable construction.** Prose values record how each observable is constructed. | All five cases | Give each explanandum variable a structured derivation and repeatable records of its axes. Add an optional protocol for observing events over time, including censoring. | Declared inputs reconstruct every derived quantity. Formulas and qualifications no longer occupy `name` or `values`. |
| **Instance scope and uncertainty.** The scalar scope field conflates two questions: how instances vary, and how claims quantify or average over that variation. | Delayed generalization · Turbulence · Tipping cascades · Microbial coexistence | Replace scalar `scope_over_instances` with repeatable scope axes. Each axis records the source of its variation and its statistical role, so the axes make explicit how each claim quantifies over or conditions on instances. | Each scope form remains distinct and readable by software. |
| **Varied factors with unknown effects.** The `modulating` category treats as known the effect that the research sets out to determine. | Active matter · Tipping cascades | Add `varied_factors[]` records that identify the varied object and define how the inquiry samples or compares its values. Keep the effect optional. | An exploratory record names each varied factor without asserting the result that the inquiry seeks. |
| **Task obligations and accuracy.** One modal and accuracy block cannot encode the direction of implication in a theorem or fidelity targets that differ across outputs. | Active matter · Turbulence · Tipping cascades · Microbial coexistence | Make `required_accuracy` nullable and move accuracy into each match. Represent each requested implication as an ordered antecedent and consequent. | Each target has its own fidelity test. Necessary and sufficient claims can be assessed independently. |
| **Scoped virtues.** A virtue token names neither the property that must persist nor the variation that tests the conclusion. | Delayed generalization · Turbulence · Microbial coexistence | Replace virtue tokens with objects. Each virtue object names the conclusion that it qualifies and the declared variations across which that claim is tested. | Two assessors apply a virtue to the same declared object and scope. |
| **Provenance.** Only evidence for the phenomenon has a source slot. | Active matter · Tipping cascades | Add optional source identifiers to technical entries and a bibliography for the record. Keep `phenomenon.data` restricted to evidence for the phenomenon. | A reviewer can trace each commitment without reconstructing its origin from surrounding prose. |

## Local edits

A local edit fixes the scope of one case or supplies an author choice that the case lacks. Each local edit is to be completed without expanding the shared schema.

| Case | Local edit |
| --- | --- |
| **Active matter** | Split results for finite systems and the thermodynamic limit into linked questions. Split lattice and continuum targets unless one answer must quantify across both. Fix the sampled controls and spatial extent. |
| **Delayed generalization** | Fix the evaluation protocol and the admissible training class. |
| **Turbulence** | Name the forcing and boundary families. Split structural relations from the numerical values of the exponents until each value can be assigned its own accuracy. |
| **Tipping cascades** | Fix the target membership and the rule that matches warming trajectories. Complete the forecast contract with its temporal scope and evaluation criteria. |
| **Microbial coexistence** | Split necessary and sufficient claims under the current template. Narrow or separate the model families, then fix the resource supply. |

No local edit supplies an unknown scientific result: such a result remains `open`, and the schema must represent its status without supplying its value.

## Disposition

The designer ratified reorienting the records toward a modeling language. In that language, every declared quantity carries a symbol. Each formula is an expression over those symbols. Most of the proposed changes are absorbed or reduced by that reorientation. The reorientation addresses several rows at once, because they report one defect as it surfaces in different places: a field typed as a token or a prose string where the record required a construction.

Each change carries its disposition in [the review state of every candidate and the implementation sequence](framework-corrections-handoff.md). The rows of this note keep their diagnosis and their acceptance test, whereas the handoff alone tracks implementation.
