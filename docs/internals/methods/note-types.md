# Note types

> [!INFO] See also
> Part of the [agent instruction system](plan-agents-humain-generation.md). Related: [decision rules](../quality-criteria/decision-rules.md) — [formal contracts](formal-contracts.md) — [procedural workflows](procedural-workflows.md) — [workspace architecture](workspace-architecture.md).


Each note type is associated with two files in the workspace:
- a **note specification** in `governance/specs/` that defines the structural requirements (required sections), forbidden patterns, and type-specific audit criteria,
- a **contract template** in `governance/contracts/` that instantiates the [contract structure](formal-contracts.md#^contract-template) with type-specific fields (e.g., expected output format for problem notes, proof strategy for result notes).

## Main note types

| Note type               | Purpose                                                                  | Required sections                                                                                                        | Forbidden patterns                                                                                                                                                    |
| ----------------------- | ------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Problem note**        | Formulate a precise question and why it matters.                         | Atomic question, role in global argument, dependencies, expected output                                                  | Proofs, broad synthesis, extended derivations, literature surveys                                                                                                     |
| **Index note**          | Operational navigation within a module or project.                       | Scope, note categories, current frontier, main outputs                                                                   | Expository prose, proofs, derivations — only navigation and status                                                                                                    |
| **Entry-point note**    | Introduce a multi-step argument its inferential map.                     | Local subquestion, scope, roadmap, subcases                                                                              | Expository prose, proofs, derivations, extended background — only orientation and mapping                                                                             |
| **Result note**         | Establish a result and proof.                                            | Local objective, assumptions, target result, proof strategy, proof, operational interpretation                           | Cross-module synthesis, literature comparison of alternative frameworks, speculative extensions, free-form survey sections, new definitions not required by the proof |
| **Definition note**     | Stabilize one core concept or notation family.                           | Motivation (obstacle addressed), formal definition, immediate properties, boundary of applicability                      | Proofs of theorems using the definition (belong in result notes), extended applications, synthesis                                                                    |
| **Tool note**           | Develop a reusable mathematical device.                                  | Local problem, why a new tool is needed, construction, properties needed here, example of use, boundary of applicability | Theorems that use the tool (belong in result notes), cross-module synthesis, comparative surveys                                                                      |
| **Comparison note**     | Contrast approaches or formalisms relative to a precise criterion.       | Comparison criterion (fixed upfront), evaluation of each item on the same explicit axes                                  | New proofs, new constructions, free-form survey without fixed axes, advocacy for one approach without explicit criterion                                              |
| **Synthesis note**      | Integrate several prior results into a larger conclusion.                | Imported ingredients listed explicitly, combination argument, resulting insight                                          | New proofs of novel results (only combination of established results), new definitions, new tool constructions                                                        |
| **Frontier note**       | Record current open inferential gaps and their blocking dependencies.    | Each gap with: question, prerequisites, blocking reason, priority                                                        | Solutions, proofs, extended analysis — only gap identification                                                                                                        |
| **Assumption registry** | Centralize recurring assumptions used across multiple notes in a module. | Each assumption with: name, formal statement, notes that use it, role it plays                                           | Derivations, proofs, extended exposition, interpretive commentary                                                                                                     |
| **Notation table**      | Stabilize symbols and admissible variants for a module or project.       | Each symbol with: canonical form, meaning, forbidden variants, defining note                                             | Exposition beyond identification, proofs, derivations                                                                                                                 |

The [audit](../../governance/post-draft-audits.md) pass must verify that the
note's declared type matches its actual content — see [audit enforcement by
note type](../../governance/post-draft-audits.md#audit-enforcement-by-note-type).

## Index note specifications

The **index note** and **entry-point note** types serve navigation and orientation roles. Their specifications are more detailed than the table above because their content is structural rather than mathematical.

### Project overview index

The project index serves as the **entry point into the project reasoning architecture** (should not merely list files). It should answer: _How is this project decomposed, and where is the current frontier of work?_

Suggested structure:

- project purpose
- main question
- module list with local roles
- current frontier of open questions
- links to project-level syntheses
- links to cross-module notes
- links to foundational module outputs

### Module local index

The module index should act as the **operational local control panel**.

Suggested structure:

- module scope
- local subquestion
- note categories inside the module
- current active contracts
- local open questions
- main local outputs
- migration status of the module
- links to authoritative active notes
- warnings about superseded legacy notes
