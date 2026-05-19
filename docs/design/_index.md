# Design Documentation — Methods

Reference documents for the gnomon epistemic framework. These files describe the rationale, structure, and specification of the research organization system. They inform the design of the governance content in the [runtime data directory](vendor/gnomon/src/gnomon/data) but are not loaded at runtime.

For the project's goal and the failure modes that motivate the architecture, see [project overview](vendor/gnomon/docs/project-overview). The present document organizes the design itself.

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
| [Tier 1 index](vendor/gnomon/docs/design/1-framework/_index)       | Desiderata for the whole framework organized by axis                                                                    | `^t1-*` |
| [Tier 2 index](vendor/gnomon/docs/design/2-architecture/_index)    | Per-theme criteria, commitments, and decisions                                                                          | `^t2-*` |
| [Tier 3 index](vendor/gnomon/docs/design/3-aspect-specific/_index) | Criteria, commitments, and open questions for each aspect                                                               | `^t3-*` |

## Other design documents

Many initial proposals are backed up in the `_backup/` folder, and some have been migrated to the main design documentation. The following documents are relevant to the design but not yet integrated into the tiered structure:

- [Layered model](_backup/architecture-1-layered-model.md)
- [Rendering and views](_backup/rendering/rendering-and-views.md)
- [Workflows](_backup/workflow-for-users.md)
- [Object types ontology](vendor/gnomon/docs/object-types-ontology/_index)
- [Argument bundles](_backup/arguments-reasoning/argument-bundles.md)
- Criteria files: [criteria taxonomy backup](_backup/object-types-ontology/taxo-criteria-ontology.md).
- The [reference frameworks](vendor/gnomon/docs/references-methods/overview-formal-frameworks) ground several criteria.
