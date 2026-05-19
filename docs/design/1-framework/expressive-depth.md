---
tags:
  - criteria
index: "[[_index|Framework-level criteria]]"
aliases:
  - Expressive depth (criteria)
---
# Expressive depth — Framework-level criteria

## Activity coverage ^t1-activity-coverage

The framework supports the **canonical set of activities** through which research advances:

- **Inquiry direction** — formulating, refining, and prioritising research questions.
- **Content production** — defining concepts, deriving results, constructing examples, formulating claims.
- **Justification** — supplying warrants, discharging assumptions, certifying soundness.
- **Critique** — surfacing errors, raising objections, identifying gaps.
- **Revision** — withdrawing, weakening, or reformulating prior content under new information.
- **Exposition** — rendering content for distinct audiences (formal, pedagogical, audit).
- **Navigation** — finding, comparing, cross-referencing across the corpus.

For every activity in this set, the framework must provide a **representation**, a library of **operations**, and a **workflow** that lets researchers perform the activity within the system.

**Failure mode prevented.** A framework that omits an activity forces that activity to occur *outside* the framework, where the framework cannot record its outcome or trace its dependencies. The activity then drifts away from the corpus.

**Upstream dependencies.**

- [Inquiry content and progression](framework-foundations#^t1-inquiry-content-and-progression) (parent criterion): the dynamic dimension is realised through these activities; coverage of the dynamic dimension requires coverage of the activities.

**Downstream consequences.**

- [Activity access rights](research-activities-workflows#^t1-activity-access-rights) (cross-group sub-criterion in *Research activities and workflows*): each activity in this taxonomy is assigned defined read and write rights.
- [Move coverage](object-kinds#^t2-move-coverage) (theme-local criterion): the operation library must span every activity in this taxonomy at the per-step grain.
- Workflow decisions in the workflows theme: each activity has a workflow specifying how the user performs it.

## Reasoning-types coverage ^t1-reasoning-types-coverage

The framework admits the **range of reasoning kinds** that research actually employs:

- mathematical / formal proofs (monotonic, rule-governed, deductive),
- informal theoretical reasoning (conceptual distinctions, reformulations),
- empirical arguments (evidence-based, defeasible, probabilistic),
- abductive and exploratory reasoning (hypothesis generation, serendipitous discovery),
- analogical reasoning (cross-domain transfer of structure).

**Failure mode prevented.** A framework that admits only classical deduction forces all reasoning modes into a single shape that distorts them, and thus silently excludes the bulk of research practice. Real research mixes reasoning kinds within a single inquiry.

**Upstream dependencies.**

- [Inquiry content and progression](framework-foundations#^t1-inquiry-content-and-progression) (parent criterion): without coverage across reasoning kinds the framework cannot capture genuine research.

**Downstream consequences.**

- [Valid licensing](reasoning-integrity#^t1-valid-licensing) (sub-criterion): its warrant-composition facet becomes pertinent only once warrants of different kinds coexist within a single chain.

## Rich content expressivity ^t1-rich-prose-expressivity

The framework's semantic fields admit **content shapes richer than short scalars**: mathematical formulas through math grammars, multi-step derivations through structured derivation records, diagrams through declarative diagram languages, and any other substantive content the corpus carries. Each such shape is met by a *formal* representation, not by a prose body. Unessential authoring loci (TODO, FIX, remark, comment) carry free prose, but that prose is framework-opaque and never substitutes for a semantic field.

**Failure mode prevented.** A representation that admits only short scalar values cannot host the substantive content of research; it either truncates it or scatters it across many opaque atoms. The opposite over-reach — admitting free prose as a substantive content shape — would reintroduce the failure modes of conventional note-taking inside fields the framework treats as semantic, masking ungrammatical content behind a typed surface.

**Upstream dependencies.**

- [Inquiry content and progression](framework-foundations#^t1-inquiry-content-and-progression) (parent criterion): research artefacts include rich mathematical and structural content; an adequate framework must host such content as first-class.
- [Formal expression of all content](framework-foundations#^t1-formal-expression) (peer sub-criterion of *Language-tooling integration*): the richness this criterion demands must be supplied by formal grammars, not by prose.

**Downstream consequences.**

- [Field-typing discipline](../2-architecture/object-kinds#^t2-field-typing) (decision): the admissible shapes for semantic fields include math grammars, structured-derivation records, and declarative diagram languages — never free-text bodies.
- [Object-kind admission test](../2-architecture/object-kinds#^t2-object-kind-admission) (decision): a candidate kind is admissible only when its canonical content has a grammar of suitable richness; prose canonical content is not admissible.
- Canonical-vs-exposition encoding (structural note): the canonical layer carries grammar-bound semantic content; the exposition layer renders that content for human readers and may carry prose around it.

## Partial formalization tolerance ^t1-partial-formalization

**The level of formalization is set per object**, not globally by the framework. Partiality applies to **which annotations are present**, never to the grammar of the annotations themselves: every annotation that is present is grammar-bound per [formal expression of all content](framework-foundations#^t1-formal-expression). Two facets:

- Contents (concept, claim, argument...) are admissible as legitimate intermediate items before their full formal characterization is available: a partially-specified content is a first-class participant in the framework, not a placeholder. The content fields that *are* recorded conform to their grammar; the fields that are not yet known are marked absent rather than filled with prose.
- For any individual object, some aspects (warrant, motivation, status, scope, …) may be left unannotated. The framework specifies, for each aspect, which annotations are mandatory, which are optional, and which formal guarantees no longer hold under relaxation. An unannotated aspect is recorded as *absent*; it is never approximated by a prose stand-in inside a semantic field.

**Failure mode prevented.** A uniform demand forces a binary choice: either every object is fully formalized (prohibitively heavy) or the framework offers no guarantees (unvalidatable). Neither is compatible with real research, which advances by gradually formalizing partially specified objects. The opposite over-reach — letting "partial" mean "filled with prose" — would silently smuggle ungrammatical content into semantic fields and forfeit the formal-expression commitment.

**Upstream dependencies.**

- [Inquiry content and progression](framework-foundations#^t1-inquiry-content-and-progression) (parent criterion): research operates on partially specified objects.
- [Formal expression of all content](framework-foundations#^t1-formal-expression) (peer sub-criterion of *Language-tooling integration*): partiality is *annotation absence*, not *sub-formal prose*; the two criteria together define the only admissible form of partial formalization.

**Downstream consequences.**

- Partial-formalization profile (open decision in the validity-revision theme): answers *which profiles are admissible* under this criterion.
- [Justification levels](reasoning-integrity#^t1-justification-levels) (tension per `^t2-x2`): deeper formalization improves the recoverability of reasoning at the cost of authoring overhead.
- [Apt strategy](reasoning-integrity#^t1-apt-strategy) (tension per `^t2-x2`): same tradeoff at the motivation grain — full annotation of every move's rationale and every sub-gap's admissibility conditions is heavy.

## Concrete analytical execution ^t1-concrete-execution

Reasoning chains encode **actual epistemic work**: step-by-step proofs, computations, comparisons, constructions, conceptual analyses. The precise operations and its operands are explicitly represented at the finest grain of the chain, not only at a higher level of abstraction.

**Failure mode prevented.** A skeleton of high-level dependencies and verb labels ("derive", "explain", "decompose", "eliminate"...) — without the underlying computation — has the surface appearance of a reasoning chain but carries no epistemic content. Such skeletons cannot be validated, transferred, or diagnosed.

**Upstream dependencies.**

- [Inquiry content and progression](framework-foundations#^t1-inquiry-content-and-progression) (cross-group parent criterion in *Framework foundation*): genuine reasoning is the actual epistemic work, not its label.

**Downstream consequences.**

- Five-row admissibility table — signature / conditions / semantics / success / license (decision in the operation-schemas theme): records the operands required for each primitive operation.
- "No opaque transformation" reasoning-quality clause (absorbed sub-claim): subsumed at the per-step grain.

## No infinite regress ^t1-no-infinite-regress

Describing a reasoning **terminates**, it does not lead to an open-ended demand for further primitives.

**Failure mode prevented.** A reasoning description that decomposes every step into sub-steps without a halting principle never terminates; the author cannot finish recording, and downstream tools cannot validate.

**Upstream dependencies.**

- [Concrete analytical execution](#^t1-concrete-execution) (parent criterion): execution is concrete only if the description bottoms out.

**Downstream consequences.**

- Closed-library mechanism (decision in the operation-schemas theme): one chosen answer — a different framework could satisfy this criterion by other means (e.g., a meta-rule reducing every operation to a fixed computational basis).
- [Operation-primitiveness](operations-and-modes#^t2-operation-primitiveness) (open decision): selects among four termination strategies — definitional fiat, well-foundedness derivation, schema calculus, open library.