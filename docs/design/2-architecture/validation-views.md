# Validation rules and view profiles

> [!INFO] Tier and scope
> **Tier 2 (architectural).** This file holds the commitments and decisions about how validation is organized — where rules live, where implementations live — and where view profiles belong. Both concerns share a placement question: which layer is the home for which artifact?
>
> Cross-cutting Tier-2 criteria that constrain decisions in this file: see [Architectural constraints](vendor/gnomon/docs/design/2-architecture/constraints), in particular [t2-mechanical-validation](vendor/gnomon/docs/design/2-architecture/constraints#^t2-mechanical-validation), [t2-separation-of-concerns](vendor/gnomon/docs/design/2-architecture/constraints#^t2-separation-of-concerns), [t2-layer-replaceability](vendor/gnomon/docs/design/2-architecture/constraints#^t2-layer-replaceability), [t1-dual-usability](vendor/gnomon/docs/design/1-framework/operational-quality#^t1-dual-usability).

---

## Decisions

### Validator and view-profile placement ^t2-validator-placement

> [!QUESTION] Where do validation rules, validator implementations, and view profiles belong?

Validation rules and validator implementations are separated into different layers.

- **Validation rules belong to the schema layer** (the *what*: invariants any object, relation, or assembly must satisfy). The schema declares what counts as well-formed. This satisfies [t2-mechanical-validation](vendor/gnomon/docs/design/2-architecture/constraints#^t2-mechanical-validation).
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

**Mechanical and schema-driven** for structural well-formedness — required-field checks, edge typing, warrant presence, DAG acyclicity within snapshots, discharge accounting. Motivational adequacy, explanatory relevance, and teleological usefulness can be audited by rules or heuristics, but their full assessment may still require human judgment. The placement is set by [t2-validator-placement](#^t2-validator-placement); the criterion that this validation is mechanical is recorded at [t2-mechanical-validation](vendor/gnomon/docs/design/2-architecture/constraints#^t2-mechanical-validation).

---

## Open questions

### Interpretive-hazard lint rules ^t2-interpretive-hazard-lint

> [!QUESTION] Should the validator carry author-time lint rules that flag phrasing patterns posing a known interpretive hazard?

The worked-example suite (example 34) surfaces a fragment carrying teleological-looking phrasing — "the abstractions useful for the task" — that reads as a hazard without being an error: the phrasing risks an unintended teleological reading. This is not a content kind and not a domain claim; it is an **author-time lint rule** — a heuristic check that flags a span for an interpretive risk and emits a warning, leaving the fragment unrewritten. It belongs with the mechanical-and-heuristic validation governed by [t2-validation-placement](#^t2-validation-placement): structural checks are mechanical, but a hazard lint is a heuristic warning, closer to the "audited by rules or heuristics" tier than to a hard schema check. Re-homed here from the dissolved metalinguistic-content candidate at [_fleeting-ideas](vendor/gnomon/docs/design/_fleeting-ideas#^fleeting-metalinguistic-content); the open question is the rule vocabulary — which phrasing patterns warrant a hazard flag, and whether the catalogue is closed.
