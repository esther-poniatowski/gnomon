---
tags:
  - gaps
project: gnomon
aliases:
  - Known gaps
---
# Known architectural gaps

The following are demanded by the reference frameworks and by the internal audits but are not yet operationalized. They are blocking gaps for Phase 1 of the operational route and must be filled before aspect-specific decisions are frozen.

Each gap names the framework-level criterion it leaves unmet and the architectural decision that addresses it. A gap is not a framework desideratum; it is a tracking entry for un-operationalized work, resolved when its addressing decision is settled.

---

- **G1 — Partial formalization policy** ([t1-partial-formalization](../1-framework/expressive-depth#^t1-partial-formalization)). What exactly is mandatory vs. optional at each note type and each formalization profile? Currently undefined; addressed at [t2-partial-formalization-profiles](granularity#^t2-partial-formalization-profiles) (open).
- **G2 — Revision propagation semantics** ([t1-revision-accountability](../1-framework/research-activities-workflows#^t1-revision-accountability)). When an upstream object is revised, what exactly happens to downstream bundles, arguments, and rendered notes? Settled at [t2-revision-feedback](validity-revision#^t2-revision-feedback) and its sub-questions.
- **G3 — Validity regime interface** ([valid licensing](../1-framework/reasoning-integrity#^t1-valid-licensing), warrant-composition facet). How do monotonic and non-monotonic regions of the reasoning graph interoperate at their boundary? Settled at [t2-warrant-annotation](validity-revision#^t2-warrant-annotation) together with [t2-propagation](validity-revision#^t2-propagation).
- **G4 — Closed operational core termination** ([t1-no-infinite-regress](../1-framework/expressive-depth#^t1-no-infinite-regress)). The current treatment asserts primitivity without deriving it. Addressed at [t2-operation-primitiveness](operations-and-modes#^t2-operation-primitiveness) (open).
- **G5 — Representation-vs-generation bifurcation** ([inquiry content and progression](../1-framework/framework-foundations#^t1-inquiry-content-and-progression), the static-vs-dynamic axis). Several documents oscillate between the two modes. A clean separation with distinct guarantees is missing; addressed at [t2-representation-vs-generation](operations-and-modes#^t2-representation-vs-generation) and [t2-partial-formalization-profiles](granularity#^t2-partial-formalization-profiles) (open).
