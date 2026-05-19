# Layering and source-of-truth

> [!INFO] Tier and scope
> **Tier 2 (architectural).** This file holds the commitments and decisions that fix the architecture's stratification: which layers exist, which is the source of truth, how they relate, and what operations may write to which layer.
>
> This file opens with a `## Criteria` section holding the theme-local criterion [layer replaceability](#^t2-layering-replaceability); the strict-direction question is the open question [layer-feedback policy](#^t2-layer-feedback). Framework-level criteria bearing on this theme: [activity separation](../1-framework/research-activities-workflows#^t1-activity-access-rights) and [single source of truth](../1-framework/research-activities-workflows#^t1-single-source-of-truth).

---

## Criteria

### Layer replaceability ^t2-layering-replaceability

Each layer must be replaceable without redefining the others. Replacing the rendering layer must not require touching the canonical objects; if it does, the layering is leaking. Replaceability is the test for whether a layer boundary is principled or merely convenient.

A layer that duplicates another's content cannot be replaced cleanly, so this criterion is a consequence of [non-redundancy](../1-framework/modular-content-organization#^t1-non-redundancy): a leaking layer is a form of cross-layer redundancy. It bears on the layer-feedback decision and on every per-theme commitment that introduces a layer.

## Decisions

### Meta vs. instance distinction ^t2-meta-instance-distinction

> [!QUESTION] Does the architecture distinguish a constitutive vocabulary (admissible types, relations, contracts, validators) from the instance content that conforms to it?

**Yes.** A schema/meta level fixes the admissible object types, relation types, field contracts, and validation invariants. An instance level stores objects conforming to the schema. Schema and instances are separately versioned and separately edited.

### Canonical layer as source of truth ^t2-canonical-source-of-truth

> [!QUESTION] Where is the primary epistemic content stored, and what guarantees its primacy?

**In a canonical layer of stable, addressable epistemic objects.** The exact taxonomy is deferred to [the project TODO](vendor/gnomon/docs/TODO). Each canonical object carries a stable identifier; no content lives only in a rendered artifact; no artifact may be edited as a substitute for editing its canonical source. Object kinds are admitted under [t2-object-kind-admission](vendor/gnomon/docs/design/2-architecture/object-kinds#^t2-object-kind-admission).

### Object-centric, not document-centric ^t2-object-centric

> [!QUESTION] Is the primary unit of representation a typed object or a text document?

**A typed object with a stable identifier.** Documents are derived assemblies of objects, not primary stores.

### Derived artifacts ^t2-derived-artifacts

> [!QUESTION] May rendered artifacts (notes, summaries, presentations, dashboards) be edited directly, or are they always compiled outputs?

**Always compiled outputs.** Manual edits in rendered artifacts are forbidden. Artifacts are produced from canonical objects via declarative selection and rendering rules.

### View specifications ^t2-view-specifications

> [!QUESTION] What mediates between canonical content and rendered artifacts?

**A view-specification layer.** It holds note manifests, audience profiles, and rendering templates. View specs are stable, versioned, declarative, and contain no substantive epistemic content.

### Build vs. mutation ^t2-build-vs-mutation

> [!QUESTION] Which operations may write to the source tree, and under what conditions?

The architecture separates two classes of operation:

- **Build / read operations** (parsing, validation, registry derivation, stale-mark computation, query execution) are read-only on source files. They may produce derived artifacts, indexes, and diagnostics, but they do not move, create, rename, or delete source files.
- **Mutating operations** (creating, archiving, revising, renaming, deleting) are performed only by the author — by hand or via dedicated maintenance commands explicitly invoked for the purpose. A read operation that silently mutates the source tree is forbidden.

When a mutating action is logically required as a follow-up to an event the build detects, the build emits a diagnostic naming the required action; it does not perform it. This yields a general **rule/implementation split**: the *kinds* of mutating action are declared by the schema; the *execution* is author-driven. Build steps are idempotent and side-effect-free on the source tree.

This commitment cross-cuts every theme but is recorded here because it is fundamentally about the source-tree boundary.

### Argument-aware indexes ^t2-registries-arguments

> [!QUESTION] May registries and indexes reference assembly structures relative to a target, or are they restricted to canonical object structures?

**They may reference assemblies.** Indexes that track arguments are derived from assemblies and exposed in the registry/index layer for querying. This makes argument graphs queryable and navigable without making the registry layer the source of reasoning content that belongs to a target; canonical objects, assemblies, and derived query structures remain separated.

> [!important] Implication for [t2-layer-feedback](#^t2-layer-feedback)
> Argument-aware indexes are inconsistent with a strictly one-way layer ordering Meta → Canonical → Graph → Bundles. The layer-feedback decision must therefore admit revision-edge feedback or revise the layer ordering so indexes sit above bundles.

---

## Open questions

### Layer-feedback policy ^t2-layer-feedback

> [!QUESTION] Is the dependency direction across layers strictly one-way, or are upward edges admitted under controlled conditions?

Alternatives:

- **Strict one-way** — Meta → Canonical → Graph → Bundles → Views → Artifacts. Inconsistent with [t2-registries-arguments](#^t2-registries-arguments) above.
- **One-way for content, with revision edges as a second edge class** permitted across layers.
- **Bidirectional reasoning edges, one-way persistence edges** (mixed).

Bearing criteria: [layer replaceability](#^t2-layering-replaceability), [revision accountability](../1-framework/research-activities-workflows#^t1-revision-accountability).

The strict-one-way alternative is closed by [t2-registries-arguments](#^t2-registries-arguments). The remaining two alternatives are open.
