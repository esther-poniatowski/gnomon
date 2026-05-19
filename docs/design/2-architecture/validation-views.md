# Validation rules and view profiles

> [!INFO] Tier and scope
> **Tier 2 (architectural).** This file holds the commitments and decisions about how validation is organized — where rules live, where implementations live — and where view profiles belong. Both concerns share a placement question: which layer is the home for which artifact?
>
> Theme-local criterion bearing on this file: [layer replaceability](layering#^t2-layering-replaceability) — validator implementations must be replaceable without revising the rules. Framework-level criteria bearing on this theme: [read-side automation](../1-framework/cost-ergonomics#^t1-read-side-automation) and [write-side automation](../1-framework/cost-ergonomics#^t1-write-side-automation) — the mechanizability the validators realise — and [activity separation](../1-framework/research-activities-workflows#^t1-activity-access-rights).

---

## Decisions

### Validator and view-profile placement ^t2-validator-placement

> [!QUESTION] Where do validation rules, validator implementations, and view profiles belong?

Validation rules and validator implementations are separated into different layers.

- **Validation rules belong to the schema layer** (the *what*: invariants any object, relation, or assembly must satisfy). The schema declares what counts as well-formed. This satisfies [write-side automation](../1-framework/cost-ergonomics#^t1-write-side-automation): validation is mechanizable without human judgment.
- **Validator implementations belong to the tooling layer** (the *how*: executable code that reads sources, evaluates schema-declared rules, and emits diagnostics). Tooling is replaceable without revising the rules.
- **View profiles belong to view specifications**, not the schema layer, because they govern rendering rather than admissible meaning.

> [!important] Generalization to assemblies
> Validation rules must cover both canonical objects and assemblies (per [locus of justificatory annotations](vendor/gnomon/docs/design/2-architecture/reasoning-structure#^t2-reasoning-annotation-attachment), [assemblies relative to a target](vendor/gnomon/docs/design/2-architecture/reasoning-structure#^t2-target-relative-assemblies)). Their structural commitments differ:
>
> - canonical objects obey tighter, kind-specific schemas (required fields, fixed slots, closed enums);
> - assemblies obey looser structural rules (e.g., a sequence of citation records each carrying strategic and explanatory annotations, with no a priori fixed number of epistemic moves).
>
> [promotion of assembly-local records](vendor/gnomon/docs/design/2-architecture/reasoning-structure#^t2-assembly-record-promotion) fixes what an assembly may contain; the schema layer must declare:
>
> - the closed set of admissible assembly-local record kinds,
> - whether each kind can be promoted,
> - the admission-test predicates on which the build evaluates promotion candidacy.
>
> Validators flag promotion candidates per [t2-build-vs-mutation](vendor/gnomon/docs/design/2-architecture/layering#^t2-build-vs-mutation); they do not move records. The exact field set within each kind depends on [t2-reasoning-annotation-fields](vendor/gnomon/docs/design/2-architecture/reasoning-structure#^t2-reasoning-annotation-fields).

### Validation placement ^t2-validation-placement

> [!QUESTION] Is structural validation mechanical and schema-driven, or does it require human judgment?

**Mechanical and schema-driven** for structural well-formedness — required-field checks, edge typing, warrant presence, DAG acyclicity within snapshots, discharge accounting. Motivational adequacy, explanatory relevance, and teleological usefulness can be audited by rules or heuristics, but their full assessment may still require human judgment. The placement is set by [t2-validator-placement](#^t2-validator-placement); that this validation is mechanizable without human judgment follows from [write-side automation](../1-framework/cost-ergonomics#^t1-write-side-automation).

---

## Open questions

### Catalogue of structural validators ^t2-validator-catalogue

> [!QUESTION] What is the closed set of structural validators the system provides, and which is mechanical versus heuristic?

[Validation placement](#^t2-validation-placement) settles that structural validation is mechanical and schema-driven, and [validator and view-profile placement](#^t2-validator-placement) settles which layer hosts the rules and which hosts the implementations. Neither enumerates *which* validators exist. The mechanical-validation criterion gave an example list — required-field checks, edge typing, warrant presence, DAG acyclicity within snapshots, discharge accounting — but an example list is not a closed catalogue.

A resolved catalogue states, for each validator, the rule it enforces, the schema or graph structure it reads, the diagnostic it emits, and whether it is a hard mechanical check or a heuristic warning.

Candidate entries gathered from across the design:

| Layer                        | Mechanism                                                                                                               | Failure mode addressed                                                                                                                                                                          |
| ---------------------------- | ----------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Schema enforcement**       | Checks required-field and field-typing per kind                                                                         | Field name drift, missing required fields, type errors ([field-typing discipline](object-kinds#^t2-field-typing))                                                                               |
| **?**                        | Checks relation-edge typing, vocabulary closure                                                                         | ([build-error policy](relations-graph#^t2-relation-storage-locus)) ==TODO: appropriate ref?==                                                                                                   |
| **Uniqueness checks**        | Ensures ID and path uniqueness                                                                                          | Duplicate entries                                                                                                                                                                               |
| **Referential integrity**    | Checks cross-registry ID resolution, dangling-reference                                                                 | Dangling dependency IDs, references to non-existent notes                                                                                                                                       |
| **Graph integrity**          | Detects cycle on proof-dependency edges                                                                                 | Circular dependencies introduced silently ([snapshot acyclicity](relations-graph#^t2-snapshot-dag-property), [no circular reasoning](../1-framework/reasoning-integrity.md#^t1-vl-no-circular)) |
| **?**                        | Checks assumption-discharge accounting                                                                                  | Silent incompleteness ([reasoning-integrity](../1-framework/reasoning-integrity.md#^t1-vl-no-silent))                                                                                           |
| **Status fairness**          | Checks the epistemic force is proportional to support (e.g. warrant presence and warrant-completeness on support edges) | Arbitrary status attribution                                                                                                                                                                    |
| **Unknown objects**          | Identify terms that appear to introduce new concepts not present in the registry (heuristic: `:=` definitions)          | Drift of the canonical conceptual corpus                                                                                                                                                        |
| **Archival integrity**       | Ensures archived records are well-formed with revision-object pairing                                                   | ([t2-archival](validity-revision#^t2-archival))                                                                                                                                                 |
| **Terminology enforcement**  | Lints prose against the canonical terminology                                                                           | Naming drift across notes ([t1-canonical-terminology](../1-framework/modular-content-organization#^t1-canonical-terminology))                                                                   |
| **Interpretive-hazards**     | Flags phrasings that match heuristic patterns                                                                           | Unintended teleological reading ([below](#^t2-interpretive-hazard-lint))                                                                                                                        |
| **Aid for human validation** | Provides a filtered- diff-based review of specific aspects (e.g. fields, object types...)                               | Semantic errors that pass structural checks                                                                                                                                                     |

Resolution must state whether the catalogue is closed, and how it partitions into mechanical checks and heuristic warnings per [t2-validation-placement](#^t2-validation-placement).

Bearing criteria: [t1-read-side-automation](../1-framework/cost-ergonomics#^t1-read-side-automation), [t1-write-side-automation](../1-framework/cost-ergonomics#^t1-write-side-automation), [t1-validation-externality](../1-framework/research-activities-workflows#^t1-validation-externality).

==TODO: Open another decision for *other tooling tasks* such as visualization, querying...==

### Interpretive-hazard lint rules ^t2-interpretive-hazard-lint

> [!QUESTION] Should the validator carry author-time lint rules that flag phrasing patterns posing a known interpretive hazard?

The worked-example suite (example 34) surfaces a fragment carrying teleological-looking phrasing — "the abstractions useful for the task" — that reads as a hazard without being an error: the phrasing risks an unintended teleological reading. This is not a content kind and not a domain claim; it is an **author-time lint rule** — a heuristic check that flags a span for an interpretive risk and emits a warning, leaving the fragment unrewritten. It belongs with the mechanical-and-heuristic validation governed by [t2-validation-placement](#^t2-validation-placement): structural checks are mechanical, but a hazard lint is a heuristic warning, closer to the "audited by rules or heuristics" tier than to a hard schema check. Re-homed here from the dissolved metalinguistic-content candidate at [fleeting-ideas](vendor/gnomon/docs/design/_fleeting-ideas#^fleeting-metalinguistic-content); the open question is the rule vocabulary — which phrasing patterns warrant a hazard flag, and whether the catalogue is closed.

==TODO: Maybe generalize to user-defined patterns instead of hard-coded debatable heuristics?==
