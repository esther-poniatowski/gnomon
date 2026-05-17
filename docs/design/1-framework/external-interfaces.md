---
tags:
  - criteria
index: "[[_index|Framework-level criteria]]"
aliases:
  - External interfaces (criteria)
---
# External interfaces — Framework-level criteria

These criteria fix what the framework delegates to systems outside its own machinery, rather than reimplementing internally.

## Git delegation ^t1-git-delegation

The framework does *not* maintain its own version-history machinery. Git is the version record. The framework covers only **in-state semantics**: each file at HEAD is the current state; references between objects resolve at HEAD and are not pinned to any commit. 

**Failure mode prevented.** A framework that maintains its own version-history layer alongside Git creates two competing records of the same corpus. References, supersession, and queries about current state can then disagree depending on which record a reader consults. Pinning every reference to a commit would create the opposite failure: the active corpus would fragment into historical snapshots, and HEAD would no longer serve as the shared state of the inquiry.

**Upstream dependencies.**

- None (root for external interfaces): the framework boundary with the surrounding version-control system.

**Downstream consequences.**

- [Revision and feedback semantics](vendor/gnomon/docs/design/2-architecture/validity-revision#^t2-revision-feedback) (decision in the validity-revision theme): revision objects record in-state revision events, not version history.
- [Archival](vendor/gnomon/docs/design/2-architecture/validity-revision#^t2-archival) (decision in the validity-revision theme): outdated objects move within the source tree rather than into a parallel history store.
- [Epistemic status as a maturity record](vendor/gnomon/docs/design/2-architecture/object-kinds#^t2-epistemic-status) (decision in the object-kinds theme): supersession is excluded from the maturity vocabulary; status records the object's standing at HEAD.

## No run-time inference engine ^t1-no-runtime-inference

The framework has no run-time inference engine that evaluates warrant conditions or defeat conditions. Argument validity is determined by authored objects and revision events rather than by an automated reasoner.

Defeasibility and revision share **one mechanism**, parameterized by the rule that makes warrant kinds sensitive to upstream changes.

**Failure mode prevented.** A framework with a run-time prover or argument engine can change what is warranted without any authored change to the corpus, inducing a hidden evaluation layer rather than a traceable revision process. Although automated inference and validation might be an extension of the framework, this is not currently a desired feature, and it would be a significant departure from the current design.

**Upstream dependencies.**

- [Valid licensing](reasoning-integrity#^t1-valid-licensing) (cross-group parent criterion in *Reasoning integrity*): warrant kinds and defeat conditions must be recorded explicitly.
- [Revision accountability](research-activities-workflows#^t1-revision-accountability) (cross-group parent criterion in *Research activities and workflows*): upstream changes must reach dependents through traceable revision events.

**Downstream consequences.**

- [Warrant-kind annotation on support relations](vendor/gnomon/docs/design/2-architecture/validity-revision#^t2-warrant-annotation) (decision in the validity-revision theme): support edges record warrant kinds so that propagation can be parameterized without run-time warrant evaluation.
- [Revision and feedback semantics](vendor/gnomon/docs/design/2-architecture/validity-revision#^t2-revision-feedback) (decision in the validity-revision theme): all changes that affect warrants are revision events driven by the author.
- [Dependent flagging](vendor/gnomon/docs/design/2-architecture/validity-revision#^t2-dependent-flagging) (decision in the validity-revision theme): tooling computes stale marks from the registry and emits diagnostics for the author, rather than mutating dependents automatically.
- [Relational queryability](modular-content-organization#^t1-relational-queryability) (cross-group sub-criterion in *Modular content organization*): query tools retrieve authored and derived registry structure; they do not infer new warrants at run time.
