# Validity regimes, warrant, and revision

> [!INFO] Tier and scope
> **Tier 2 (architectural).** This file holds the commitments and decisions about how the architecture distinguishes monotonic from defeasible support, and how it handles revision events that propagate to dependents. The two concerns are connected: warrant kind annotated on each support edge parameterizes how dependents respond to upstream revisions.
>
> Cross-cutting Tier-2 criteria that constrain decisions in this file: see [Architectural constraints](vendor/gnomon/docs/design/2-architecture/constraints), in particular [t2-defeasibility](vendor/gnomon/docs/design/2-architecture/constraints#^t2-defeasibility), [t2-revision-semantics](vendor/gnomon/docs/design/2-architecture/constraints#^t2-revision-semantics), [t2-multi-regime-reasoning](vendor/gnomon/docs/design/2-architecture/constraints#^t2-multi-regime-reasoning), [t2-snapshot-dag](vendor/gnomon/docs/design/2-architecture/constraints#^t2-snapshot-dag).
>
> Two framework-level commitments govern this theme: [t1-git-delegation](vendor/gnomon/docs/design/1-framework/external-interfaces#^t1-git-delegation) (versioning is delegated to git; this file covers only in-state semantics at HEAD) and [t1-no-runtime-inference](vendor/gnomon/docs/design/1-framework/external-interfaces#^t1-no-runtime-inference) (defeasibility and revision share one operational mechanism — author edits, not run-time inference).

---

## Decisions

### Warrant-kind annotation on support relations ^t2-warrant-annotation

> [!QUESTION] How does the architecture distinguish monotonic from defeasible support — what is annotated, and where?

**Warrant kind on each edge.** Warrant kind is drawn from a closed enum declared in the schema and recorded on the edge. This keeps each support relation independently auditable and supports reuse of canonical objects across contexts (consistent with [t1-modularity](../1-framework/modular-content-organization#^t1-reuse) and [t2-object-kind-admission](vendor/gnomon/docs/design/2-architecture/object-kinds#^t2-object-kind-admission)).

**Derived from edges, not stored in node.** Whether a node's conclusion is defeasible is a property of *how* it is supported, not of what it is: the warrant kinds of its incoming support edges are combined to determine the regime.

For enum entries and the combination rule, see [warrant vocabulary](vendor/gnomon/docs/design/3-aspect-specific/warrant-vocabulary). Whether the warrant enum inside assemblies coincides with the enum for canonical edges is open and depends on which fields [the reasoning note schema](vendor/gnomon/docs/design/3-aspect-specific/reasoning-fields) selects.

### Revision and feedback semantics ^t2-revision-feedback

> [!QUESTION] How does the architecture represent revision when content is changed, retracted, or reformulated, and how do those changes propagate to dependents?

The question decomposes into five sub-decisions: revision kinds, recording, archival, dependent flagging, propagation. Each is settled below.

The two related questions — warrant kind on edges (above) and revision propagation — interact: the warrant kind on each support edge controls how dependents respond to upstream revisions. Neither subsumes the other; they share the mechanism mandated by [t1-no-runtime-inference](vendor/gnomon/docs/design/1-framework/external-interfaces#^t1-no-runtime-inference).

#### Revision kinds ^t2-revision-kinds

> [!QUESTION] What classes of revision does the architecture recognize, and what default propagation priority does each carry?

**Closed enum with multiple tags allowed**, each kind carrying a default propagation priority. A single revision episode can mix kinds; the episode priority is the max over the default priorities of its tags ([t2-propagation](#^t2-propagation) refines this with warrant kind sensitivity).

The `rationale` field carries one or more tags for failure kinds from a closed enum, plus optional prose. These tags support queries across projects about patterns in failed routes.

Enum entries, priority table, and failure-kind enum: see [Revision vocabulary](vendor/gnomon/docs/design/3-aspect-specific/revision-vocabulary).

> [!note] Scope note
> Purely-considered routes (not pursued, not recorded as canonical objects) are out of scope. They are not retraction events: no other object depends on them. Such routes are recorded on a target object by ordinary target-local annotation (e.g., a `considered-route` content block).

#### Revision recording ^t2-revision-recording

> [!QUESTION] Where and how is a revision episode recorded?

**Revision objects.** Every revision episode is recorded as a revision object in a dedicated revisions directory while open or in progress (`revisions/{id}.md`). The revision object is the single source of truth for the episode and serves as the workbench for tracking progress. Dependents themselves are not annotated to track progress.

**Fields authorship.** The revision object contains three classes of fields:

- filled by the human reviewer at creation time,
- derived automatically from the revision object and the dependency graph, but finally specified by the human reviewer (allowing override) — possibly routed by a maintenance command after the computation,
- updated by the author as work progresses.

The derived metadata is a build-time cache: it changes whenever the dependency graph, the enum for revision kinds, or the warrant kinds on edges change.

**Manual creation.** The author decides whether a revision episode warrants recording. A typo edit does not require a revision object — only revisions the author judges substantive enough to warrant dependent re-examination.

Revision-object field set and authorship partition: see [Revision vocabulary](vendor/gnomon/docs/design/3-aspect-specific/revision-vocabulary).

**Derived metadata and the build/mutation separation.** The result of a build computation can be routed to revision-object fields by a specific command. This does not violate [t2-build-vs-mutation](vendor/gnomon/docs/design/2-architecture/layering#^t2-build-vs-mutation) or [t2-relation-storage-locus](vendor/gnomon/docs/design/2-architecture/relations-graph#^t2-relation-storage-locus): derived metadata lives in the build-output registry, not silently written into the source. The human reviewer remains free to write the derived metadata into the revision object or override it.

The dependency graph stays DAG-acyclic per [t2-snapshot-dag](vendor/gnomon/docs/design/2-architecture/constraints#^t2-snapshot-dag): revisions are recorded as objects in `revisions/`, not as edges.

#### Archival ^t2-archival

> [!QUESTION] What happens to objects that become inactive (retracted objects, resolved revision objects), and how are they distinguished from active content?

**Unified archive.** Outdated objects of every kind (retracted canonical objects and resolved revision objects) live under a single top-level `archive/` directory. The active set shows only outstanding work.

**Parallel trees.** The archive directory mirrors the active store: an archived item's relative path within `archive/` matches its prior path within the active store; only the top-level prefix changes.

- Retracted canonical objects move to `archive/{kind}/{id}.md`.
- Resolved revisions (`status: resolved`) move to `archive/revisions/{id}.md`.

**Author-driven archival.** Per [t2-build-vs-mutation](vendor/gnomon/docs/design/2-architecture/layering#^t2-build-vs-mutation), all moves are performed by the author once the relevant status change occurs.

**Validation.** A validator ensures moves are well-formed and that the corresponding revision-object pairing is present. It emits diagnostics naming the required action when the pairing is incomplete; it does not move files itself.

**Build policy.** The registry build can scan both the active store and `archive/` and produce the derived registry. Archived objects are tagged (e.g., `in_archive: true`).

Free consequences of the path-mirroring convention:

- **Browsability.** The archive is browsable with the same kind-directories and tooling as the active store.
- **ID stability.** An archived object's ID is unchanged; the archive prefix is a path change, not an identity change.
- **Provenance recoverability.** An archived object's prior location is its current archive location with the `archive/` prefix stripped.
- **Resolution.** The registry resolves any direct reference to an archived ID without error.
- **Visible archive marker.** Tooling that resolves a reference to an archived object surfaces the `in_archive` tag and the triggering revision, so consumers cannot accidentally treat an archived object as active.
- **Path-based filtering.** Default queries hide archived content via a path-based predicate; historical queries opt in by removing the predicate.

Retraction recipe and the validator diagnostic strings: see [Revision vocabulary](vendor/gnomon/docs/design/3-aspect-specific/revision-vocabulary).

#### Dependent flagging ^t2-dependent-flagging

> [!QUESTION] How are objects that depend on a revised upstream surfaced to the researcher?

**Registry index.** For each ID in the database, the registry associates a list of revision object IDs that mention it. Multiple concurrent revisions per dependent are supported, since each object may simultaneously be affected by several upstream revisions.

**Lightweight references.** The index holds references only, not duplicated content. The revision object remains the single source of truth for rationale, priority, and progress; the registry is the per-dependent index.

**Automated flagging.** Tooling reads each revision object in `revisions/`. For each object in the `dependents` field, it appends the ID of the revision object into the index entry for that dependent.

**Registry-derived property.** Stale-marks are centralized in the registry (per [t2-single-source-of-truth](vendor/gnomon/docs/design/2-architecture/constraints#^t2-single-source-of-truth)). Dependent source files are not automatically modified (per [t2-relation-storage-locus](vendor/gnomon/docs/design/2-architecture/relations-graph#^t2-relation-storage-locus)).

**Researcher autonomy.** The researcher decides per dependent whether it still holds without adjustment, needs adjustment, or needs retraction in turn.

> [!hint] Distinction from revision-episode dependent identification
> The flagging mechanism described here goes from a single dependent to (possibly multiple) revision episodes. The identification process in [t2-revision-recording](#^t2-revision-recording) goes the other direction: from a single revision episode to (possibly multiple) dependent objects. The two processes serve different views: the identification process gives the researcher all subsequent actions for one episode; the flagging mechanism gives the researcher all constraints on one object across episodes, supporting a globally-aware revision.

#### Upstream-change propagation ^t2-propagation

> [!QUESTION] When an upstream object is revised, how is the revision propagated to dependents?

The propagation rule decomposes into three parameters per dependent.

| Parameter        | Question                                                                    | Depends on                                                                                                          |
| ---------------- | --------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------- |
| **Transmission** | *Whether* an upstream revision transmits a stale-mark to a given dependent. | The **relation kind** of the edge from the upstream object to the dependent.                                        |
| **Sensitivity**  | *Which classes of upstream change* transmit through a given edge.           | The **warrant kind** on the support edge from the upstream to the dependent (per [t2-warrant-annotation](#^t2-warrant-annotation)). |
| **Priority**     | *How urgently* the dependent must be re-examined.                           | The **revision kind** of the upstream change (priority table at [t2-revision-kinds](#^t2-revision-kinds)) and the **warrant kind** of the dependent's edge. |

Transmission and sensitivity examples, and the provisional combination rule for priority: see [Revision vocabulary](vendor/gnomon/docs/design/3-aspect-specific/revision-vocabulary).

> [!missing] Open subsidiary questions
> - **Transmitting relation set** — which exact relation kinds transmit revision? Deferred to the relation-vocabulary decision in [the project TODO](vendor/gnomon/docs/TODO).
> - **Combination rule for priority** — exact rule combining `revision_kind` priority with `warrant_kind` sensitivity into the per-dependent priority; provisional formulation in [Revision vocabulary](vendor/gnomon/docs/design/3-aspect-specific/revision-vocabulary).
