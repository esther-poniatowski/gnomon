---
tags:
  - criteria
index: "[[_index|Framework-level criteria]]"
aliases:
  - Research activities and workflows (criteria)
---
# Research activities and workflows — Framework-level criteria

## Revision accountability ^t1-revision-accountability

Any aspect of the content can be revised (e.g. correcting a failing argument, weakening an assumption, reformulating a goal). The framework **accounts for revision as a process**: each revision must be traceable to its origin and propagable to every dependent step. Two requirements follow:

- **Dependency tracking** — every step that consumes upstream content carries a reference to that content, so that a revision upstream can locate every step it affects.
- **Correction propagation** — once a revision occurs, the framework provides the path along which the correction reaches each affected step, rather than leaving the reconciliation implicit.

**Failure mode prevented.** A framework where revisions are silent overwrites — without recording what was revised, why, or which steps depend on the revised content — breaks the inferential record. Downstream steps continue to rest on premises that no longer hold; readers cannot reconstruct the trajectory that produced the final form.

**Upstream dependencies.**

- [Inquiry content and progression](framework-foundations#^t1-inquiry-content-and-progression) (cross-group parent criterion in *Framework foundation*): research reasoning advances by revision; an adequate framework must account for the revision process, not only its terminal states.

**Downstream consequences.**

- Revision-recording mechanism (decision in the validity-revision theme): the chosen way to record what was revised, when, and why.
- Dependency-tracking mechanism (decision in the validity-revision theme): the chosen way to attach upstream references to each step.
- Propagation mechanism (decision in the validity-revision theme): the chosen way to convey a correction from the revised step to its dependents.
- [Valid licensing](reasoning-integrity#^t1-valid-licensing) (cross-group tension per `^t2-x4`): the revision record is itself cyclic (a step can be revised in light of its own consequences), whereas the no-circular-reasoning facet requires the snapshot graph to remain acyclic; the resolution is the snapshot-vs-history slicing.
- [Staleness gating](#^t1-staleness-gating) (peer sub-criterion): once dependencies are tracked and corrections propagate, gating dependent activity on unresolved revisions becomes enforceable.

## Activity access rights ^t1-activity-access-rights

Distinct [supported activities](expressive-depth#^t1-activity-coverage) are characterized by specific **access rights** over the framework's artefacts:

- **Read rights** — an activity may consume only the artefacts it is granted read access to.
- **Write rights** — each activity has a defined set of editable artefacts, and within each artefact a defined scope for edits (e.g. specific fields).

> [!warning]
> The framework does not require activities to occupy *disjoint* artefacts — activities legitimately interact, and revision in particular edits the artefacts that content production authored.

> [!note] Criterion scope
> This mechanism that implements per-activity read/write rights is a downstream decision. A candidate formalism is [Rust's ownership-and-borrowing model](_fleeting-ideas#^fleeting-ownership-borrowing), it specifies which activity *owns* each artefact, which activities may *borrow* it for reading, and how write rights transfer.

**Failure mode prevented.** When an activity may write outside any declared scope, every operation can silently modify an artefact another activity depends on. The two activities then drift, and authoritative status across artefacts becomes indeterminate.

**Upstream dependencies.**

- [Activity coverage](expressive-depth#^t1-activity-coverage) (cross-group parent criterion in *Expressive depth*): the taxonomy of activities is fixed; this criterion assigns each activity its read and write rights.
- [Inquiry content and progression](framework-foundations#^t1-inquiry-content-and-progression) (cross-group ancestor criterion in *Framework foundation*): per-activity access rights are the structural specialisation of capturing the dynamic dimension as distinct, disciplined authoring activities.

**Downstream consequences.**

- Layer inventory and per-layer functional roles (decisions in the layering theme): the chosen partition of the system into write loci with defined editable scopes.
- Per-activity read/write-rights mechanism (open decision in the layering theme): the chosen formalism for assigning and enforcing access rights — the staged ownership/borrowing candidate is one input.
- [Single source of truth](#^t1-single-source-of-truth) (peer sub-criterion): the access-rights regime presupposes that each piece of content has one owning locus to assign rights against.
- [Non-redundancy](modular-content-organization#^t1-non-redundancy) (cross-group sub-criterion in *Modular content organization*): once each activity writes only within its declared scope, non-redundancy is enforceable across the system.

## Single source of truth ^t1-single-source-of-truth

Each piece of content has **one canonical locus** that owns it; every other artefact that presents the same content **derives from** that locus rather than asserting it independently.

Consequence:

- Canonical content (e.g. definitions, claims, proofs, relations...) is the only *authoritative* source; and remains *agnostic to the audience or purpose* of any particular rendering.
- Expository views (e.g. an academic submission, a formal report, a pedagogical presentation...) must select, reformulate, or re-render that source for an audience. It must not assert claims or relations absent from the canonical source. Exposition holds read rights over canonical content and write rights only over its own rendered artefacts.

**Failure mode prevented.** When an expository view, or any derived artefact, asserts new contents, the reasoning become unstable: several representations of the inquiry evolves in parallel and drift apart. In a specific exposition, the main message dilutes in prose, becomes untractable, and is subject to formatting constraints.

**Upstream dependencies.**

- [Activity access rights](#^t1-activity-access-rights) (peer sub-criterion): the access-rights regime needs one owning locus per content to assign rights against; single source of truth supplies it.
- [Inquiry content and progression](framework-foundations#^t1-inquiry-content-and-progression) (cross-group ancestor criterion in *Framework foundation*): a single canonical locus is what makes the recorded state a usable reference.

**Downstream consequences.**

- Single-source-of-truth mechanism (decision in the layering theme): which locus owns each piece of content as its canonical source.
- Audience-independent stability (sub-criterion): expository renderings remain stable as canonical content evolves, because they derive from one canonical source.
- [Non-redundancy](modular-content-organization#^t1-non-redundancy) (cross-group sub-criterion in *Modular content organization*): a single canonical locus per content is the precondition for stating each piece of content exactly once.

## Staleness gating ^t1-staleness-gating

The framework **gates dependent activity** — drafting, citation, downstream derivation — on the resolution of upstream revision staleness. Authors cannot proceed past unresolved upstream changes without explicit override.

**Failure mode prevented.** Drafting on top of a stale dependency silently produces work that rests on a withdrawn premise. Without a gate, the author discovers the conflict only at validation time, by which point the downstream work needs rewriting.

**Upstream dependencies.**

- None (root): a workflow commitment imposed independently of other criteria.

**Downstream consequences.**

- Drafting-gate mechanism (decision in the validity-revision theme): the chosen way to block dependent activity until upstream resolution.

## Validation externality ^t1-validation-externality

**Validation is performed by a process distinct from authoring.** Self-validation — whatever produced the content also certifying that the content is well-formed — does not substitute for the verdict of an external validator. The validator's output is authoritative; authoring corrections made before the validator runs do not stand in for it.

**Failure mode prevented.** When the producer is also the certifier, the producer's blind spots become the validation's blind spots: any error the producer cannot recognise passes undetected, and the validation signal collapses into the authoring signal. Externality breaks this collapse by routing the verdict through a process that does not share the authoring loop's assumptions.

**Upstream dependencies.**

- [Write-side automation](cost-ergonomics#^t1-write-side-automation) (cross-group parent criterion in *Cost and Ergonomics*): externality presupposes that validators are mechanizable.

**Downstream consequences.**

- Validation-architecture mechanism (decision in the validation-views theme): the chosen organisation of the external validators.
- Validation-gating mechanism (decision in the validation-views theme): the chosen policy for what a validator failure does.
- [Canonical terminology](modular-content-organization#^t1-canonical-terminology) (peer sub-criterion): the canonicity check is one externalised validator.