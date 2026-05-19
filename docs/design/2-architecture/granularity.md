# Granularity and partial formalization

> [!INFO] Tier and scope
> **Tier 2 (architectural).** This file holds the commitments and decisions about how reasoning is stratified into units of varying granularity, and about how formalization scales — which fields and validators are mandatory at each profile, and what guarantees degrade under relaxation.
>
> Theme-local criterion bearing on this file: [object-kind set smallness](object-kinds#^t2-ontology-small). Framework-level criteria bearing on this theme: [activity coverage](../1-framework/expressive-depth#^t1-activity-coverage) and [t1-partial-formalization](../1-framework/expressive-depth#^t1-partial-formalization). See also tension [X2](../1-framework/_tensions#^t2-x2).

---

## Open questions

### Reasoning-record storage ^t2-reasoning-record-storage

> [!QUESTION] Where are reasoning records stored — as a dedicated layer above structural graphs, as two synchronized layers (planning and execution), as fields on canonical objects, or as a snapshot-and-delta dynamic layer?

Alternatives:

- **Dedicated layer above structural graphs** ("Inquiry and arguments" layer 3).
- **Two dedicated layers, planning and execution**, with two synchronized graphs.
- **Snapshot-and-delta dynamic layer** with bundles inside it.

The fields-on-canonical-objects alternative is closed by [t2-reasoning-annotation-attachment](vendor/gnomon/docs/design/2-architecture/reasoning-structure#^t2-reasoning-annotation-attachment): strategic and explanatory justification cannot live on canonical objects under the placement rule, so reasoning records cannot be canonical-object annotations.

Bearing criteria: [t1-intelligibility](../1-framework/reasoning-integrity#^t1-justification-levels), [non-redundancy](../1-framework/modular-content-organization#^t1-non-redundancy), [t1-feasibility](../1-framework/cost-ergonomics#^t1-system-scale), [revision accountability](../1-framework/research-activities-workflows#^t1-revision-accountability).

### Granularity strata for reasoning ^t2-granularity-strata

> [!QUESTION] At what granularities are reasoning units distinguished?

Alternatives:

- **Three strata** — micro (Inference Node) / meso (Argument Segment) / macro (Argument Graph).
- **Four strata** — Goal / Planning Schema / Work Unit / Operation Application.
- **Two strata only** — bundle (target-relative selection) / canonical objects.
- **Mixed** — `ReasoningBundle` containing `WorkUnit`s containing `OperationApplication`s, plus `StateDelta`s.

Bearing criteria: [object-kind set smallness](object-kinds#^t2-ontology-small), [t1-reasoning-types-coverage](../1-framework/expressive-depth#^t1-reasoning-types-coverage), [t1-activity-coverage](../1-framework/expressive-depth#^t1-activity-coverage).

### Partial-formalization profiles ^t2-partial-formalization-profiles

> [!QUESTION] Which fields and which validators are mandatory at each formalization profile, and which are optional?

A **formalization profile** is a named tuple `(mandatory_field_set, validator_set, guarantee_set)` declared per object kind and per assembly kind, where:

- `mandatory_field_set` selects, from the field set per locus × content-kind cell fixed by [t2-reasoning-annotation-fields](vendor/gnomon/docs/design/2-architecture/reasoning-structure#^t2-reasoning-annotation-fields), which optional fields become mandatory at this profile;
- `validator_set` selects, from the validators declared by [t2-validator-placement](vendor/gnomon/docs/design/2-architecture/validation-views#^t2-validator-placement), which must pass for a record to satisfy the profile;
- `guarantee_set` declares which formal guarantees the profile delivers and which degrade under relaxation to a lower profile.

Records advertise the profile they claim; validators check the claim. The profile vocabulary is closed at design time. The architecture commits to *that* profiles have this shape; the named profiles, their contents, and their degradation chain are aspect-specific (Tier 3).

Bearing criteria: [t1-partial-formalization](../1-framework/expressive-depth#^t1-partial-formalization), [t1-feasibility](../1-framework/cost-ergonomics#^t1-system-scale), tension [X2](../1-framework/_tensions#^t2-x2).
