# Operation schemas and reasoning modes

> [!INFO] Tier and scope
> **Tier 2 (architectural).** This file holds the commitments and decisions about the operational core — where operation schemas live, on what grounds the schema regress terminates, how representation and generation modes relate, and how planning synchronizes with execution.
>
> Cross-cutting Tier-2 criteria that constrain decisions in this file: see [Architectural constraints](vendor/gnomon/docs/design/2-architecture/constraints), in particular [t2-closed-operational-core](vendor/gnomon/docs/design/2-architecture/constraints#^t2-closed-operational-core), [t2-repr-vs-gen](vendor/gnomon/docs/design/2-architecture/constraints#^t2-repr-vs-gen), [t2-revision-semantics](vendor/gnomon/docs/design/2-architecture/constraints#^t2-revision-semantics), tension [X1](vendor/gnomon/docs/design/2-architecture/constraints#^t2-x1).

---

## Decisions

### Operation-schema placement ^t2-operation-schema-placement

> [!QUESTION] Where do operation schemas belong?

**In the meta-schema**, as part of the representational vocabulary or as schema declarations. They are not canonical epistemic content objects. They are versioned and validated like schema elements, referenced by operation applications, and reused across reasoning contexts.

> [!important] Implication
> The placement is the same under all primitiveness regimes ([t2-operation-primitiveness](#^t2-operation-primitiveness) below); only the contents differ. Per-alternative contents and constructor proposals: see [Operation schemas](vendor/gnomon/docs/design/3-aspect-specific/operation-schemas).

### Representation vs. generation ^t2-representation-vs-generation

> [!QUESTION] Does the architecture provide a representational language (post-hoc annotation of completed reasoning), a generative framework (operative during research), or both?

**Both, with explicit separation.** The architecture supports both representation mode (post-hoc annotation) and generation mode (operative guidance during research), with an explicit boundary between them.

> [!missing] Separation mechanism
> Which fields and validators are mandatory in each mode, and what degrades under partial specification, is deferred to [t2-partial-formalization-profiles](vendor/gnomon/docs/design/2-architecture/granularity#^t2-partial-formalization-profiles).

---

## Open questions

### Operation-schema primitiveness ^t2-operation-primitiveness

> [!QUESTION] Is there a closed library of primitive operation schemas, and on what grounds does the regress terminate?

Alternatives:

- **Definitional fiat** — closed library asserted, not derived.
- **Well-foundedness derivation** — closed library required, with reduction to a fixed computational basis or an explicit stratification proof.
- **Schema calculus** — a small set of primitive constructors from which domain schemas are derived (constructor proposals in [Operation schemas](vendor/gnomon/docs/design/3-aspect-specific/operation-schemas)).
- **Open library** — implicitly ruled out by all sources, recorded as a pole.

Bearing criteria: [t2-closed-operational-core](vendor/gnomon/docs/design/2-architecture/constraints#^t2-closed-operational-core), [t1-expressivity](vendor/gnomon/docs/design/1-framework/content-adequacy#^t1-expressivity), tension [X1](vendor/gnomon/docs/design/2-architecture/constraints#^t2-x1). Tension X1 favors deriving schemas from a small calculus.

### Synchronization between planning and execution ^t2-planning-execution-sync

> [!QUESTION] When execution produces a result, how does the planning side learn about it?

Alternatives:

- **Implicit** — the goal is marked satisfied by inspection of the dependency graph.
- **Explicit two-graph correspondence** — a functor or relation between planning and execution graphs (criticized as decoration without further structure).
- **`StateDelta` objects** emitted by work units update the snapshot, which contains both goals and content.
- **Single bidirectional reasoning graph** — no separate goal graph.

Bearing criteria: [t2-revision-semantics](vendor/gnomon/docs/design/2-architecture/constraints#^t2-revision-semantics), [t1-non-arbitrary](vendor/gnomon/docs/design/1-framework/content-adequacy#^t1-non-arbitrary).
