# External interfaces

> [!INFO] Tier and axis
> **Tier 1 (framework-level desiderata) — interface axis.** This file fixes how the framework relates to systems outside its own machinery: version-control, the human author, the toolchain, source-format conventions. Each commitment is framework-wide — it binds every aspect of the system rather than fixing how layers compose. They cannot be overridden by architectural or aspect-specific decisions.

---

## Git delegation ^t1-git-delegation

The framework does not maintain its own version-history machinery. Git is the version record; the file at HEAD is the current state; references between objects resolve at HEAD and are not commit-pinned. The framework covers only **in-state semantics at HEAD**.

This commitment binds every history-related decision: the revision aspect ([revision and feedback semantics](vendor/gnomon/docs/design/2-architecture/validity-revision#^t2-revision-feedback)) records in-state revision events but not version history; the status aspect ([epistemic status as a maturity record](vendor/gnomon/docs/design/2-architecture/object-kinds#^t2-epistemic-status)) excludes supersession from the maturity vocabulary; the archival aspect ([archival](vendor/gnomon/docs/design/2-architecture/validity-revision#^t2-archival)) moves files within the source tree rather than maintaining a parallel history store.

*Bearing axes:* operational quality, structural integrity.

*Source:* ratified from the Tier-1 proposal block of the deleted construction log.

---

## No run-time inference engine ^t1-no-runtime-inference

Warrant defeat appears only through author edits. The framework has no run-time inference engine that re-evaluates warrants without an edit. Defeasibility and revision share **one mechanism**, parameterized by the rule that makes warrant kinds sensitive to upstream changes.

This commitment binds every decision about how reasoning is evaluated: the defeasibility aspect ([warrant-kind annotation on support relations](vendor/gnomon/docs/design/2-architecture/validity-revision#^t2-warrant-annotation)) records warrant kinds on edges so that the system can parameterize propagation, but edits rather than inference trigger propagation; the revision aspect ([revision and feedback semantics](vendor/gnomon/docs/design/2-architecture/validity-revision#^t2-revision-feedback)) records all changes as events driven by the author; the mechanism for flagging dependents ([dependent flagging](vendor/gnomon/docs/design/2-architecture/validity-revision#^t2-dependent-flagging)) computes from the registry but emits diagnostics for the author rather than mutating dependents automatically. Without this commitment, the framework would have to commit to a substantially different layer: a run-time prover or argument engine.

*Bearing axes:* operational quality, epistemic quality.

*Source:* ratified from the Tier-1 proposal block of the deleted construction log.
