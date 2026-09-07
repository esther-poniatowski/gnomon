---
tags:
  - index
index: "[gnomon documentation](../_index.md)"
aliases:
  - Design documentation
---
# Design Documentation — Methods

Reference documents for the gnomon epistemic framework. These files describe the rationale, structure, and specification of the research organization system. They inform the design of the governance content in the [runtime data directory](../../src/gnomon/data) but are not loaded at runtime.

For the project's goal and the failure modes that motivate the architecture, see [project overview](../project-overview.md). The present document organizes the design itself.

## Tiers and axes

The design criteria, architectural commitments, and decisions for each aspect are organized along two orthogonal dimensions: 

- a **tier** (framework / architectural / aspect) 
- an **axis** (content / structural / epistemic / operational).

### Tiers

Every criterion in the project belongs to exactly one of the following tiers.

| Tier   | Name                      | Scope                                                                                        | Binding force                                                                                     |
| ------ | ------------------------- | -------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- |
| **T1** | Framework desiderata      | Properties of the system as a whole; not properties of any single component                  | Cannot be overridden. All design decisions are evaluated against these                            |
| **T2** | Architectural constraints | Properties of structural decisions (layers, data flow, composition)                          | Cannot be overridden by aspect-specific decisions. Apply wherever the architecture makes a choice |
| **T3** | Criteria for each aspect  | Properties local to one domain: ontology, fields, relations, arguments, rendering, workflows | Must trace to at least one Tier 1 or Tier 2 criterion. Live in domain documents                   |

Each tier follows the same logical structure (criteria → commitments/decisions), implemented per tier:

- **Tier 1:** criteria for the whole framework, organized by axis. Each axis file holds its criteria directly. No commitments or decisions yet at the framework level.
- **Tier 2:** architectural criteria, commitments, and decisions, all theme-local: each thematic file opens with an optional `## Criteria` section of well-formedness requirements binding that theme, followed by `## Decisions` and `## Open questions`, each opened by a `[!QUESTION]` callout naming the design question it answers. The former cross-cutting `constraints` file has been retired: every constraint it held was promoted to Tier 1 or moved to its theme-local home.
- **Tier 3:** criteria, commitments, and open questions for each theme all live within each thematic file.

### Axes

Every criterion evaluates a property along one of four axes. These axes are independent: scoring well on one does not entail scoring well on another.

| Axis                    | Question                                               | Typical criteria                                                          |
| ----------------------- | ------------------------------------------------------ | ------------------------------------------------------------------------- |
| **Content adequacy**    | Does the representation capture the right aspects?     | expressivity, coverage completeness, epistemic adequacy                   |
| **Structural quality**  | Is the architecture well-formed?                       | separation of concerns, single source of truth, narrow ontology           |
| **Epistemic quality**   | Does the representation support genuine understanding? | motivational non-triviality, teleological coherence, warrant transparency |
| **Operational quality** | Is the system usable, validatable, implementable?      | partial formalization tolerance, validation, scalability                  |

## Tier folders and organization

Each tier is developed its own sub-folder with an index file that organizes the criteria and decisions of that tier. The index files are the top-level entry points to the design documentation. They are linked from this file and from each other, so that every criterion and decision is traceable to its source in the overall design.

| Index                                                              | Folder organization                                                                                                     | Anchors |
| ------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------- | ------- |
| [Tier 1 index](1-framework/_index.md)       | Desiderata for the whole framework organized by axis                                                                    | `^t1-*` |
| [Tier 2 index](2-architecture/_index.md)    | Per-theme criteria, commitments, and decisions                                                                          | `^t2-*` |
| [Tier 3 index](3-aspect-specific/_index.md) | Criteria, commitments, and open questions for each aspect                                                               | `^t3-*` |

## Files in this folder

| Note | Content |
| --- | --- |
| [Design handoff](_handoff.md) | Project-level state for a new agent, and which focused handoff governs the work about to start. |
| [Design refactor handoff](_handoff-refactor.md) | State of the Step A–D refactor sequence. |
| [Source-file cleanup handoff](_handoff-cleanup.md) | State of Step A.4 alone: removing source bodies whose Tier-1 content has already moved into the framework criteria. |
| [Design classification table](_classification-table.md) | Each source entry under its current class tags, with the final state each tag produces. |
| [Migration table](_migration-table.md) | Where each migrated entry came from and where it now lives, with the anchor on each side. |
| [Terminology alias table](_alias-table.md) | Eight clusters of labels that denote one referent, each with the term retained for forward use. |
| [Worked examples](_worked-examples.md) | Statements the framework must be able to represent, each paired with the parts that handle it. |
| [Fleeting ideas](_fleeting-ideas.md) | Ideas awaiting triage, held until each one feeds a TODO entry, an open decision, a stub, or none. |

## Superseded proposals

[The earlier proposals, registered by group](_backup/_index.md), remain informational sources. Five are consulted for commitments that the tier files record without re-deriving:

- [the layered model](_backup/architecture-1-layered-model.md);
- [the rendering proposal](_backup/rendering/rendering-and-views.md);
- [the user workflow](_backup/workflow-for-users.md);
- [argument bundles](_backup/arguments-reasoning/argument-bundles.md);
- [the conditions a canonical object must satisfy](_backup/object-types-ontology/taxo-criteria-ontology.md).

Several criteria are grounded in [the formal reasoning domains](../methods-reasoning/formal-frameworks-overview.md).
