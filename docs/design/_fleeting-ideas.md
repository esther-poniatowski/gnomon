---
tags:
  - ideas
index: "[Design documentation](_index.md)"
aliases:
  - Fleeting ideas
---
# Fleeting ideas

Staging area for new ideas pending triage. Items move out to their final destination once classified. The triage policy in the [main handoff](_handoff) governs decisions: each idea feeds an existing TODO, a Tier-2 open decision, a Tier-3 stub, or none.

This document is organised by **bearing decision** — the open question or criterion each candidate feeds — not by the review that surfaced it. Provenance is recorded in the [triage log](#^fleeting-triage-log) at the end. A candidate may bear on more than one decision; it is filed under its primary bearing and cross-linked from the others.

Concrete expressivity test cases that stress-test the design live in the companion document [worked-examples](_worked-examples); this document holds only the candidate solutions and the principled rejections.

---

## Candidates

Staged proposals, grouped by the decision each bears on. Each candidate is re-evaluated when its bearing decision comes up for resolution. The [paradigm catalogue](#^fleeting-paradigm-catalogue) preamble below states the cross-cutting principle that governs every candidate drawn from a programming language or formalism.

### On candidate scope ^fleeting-paradigm-catalogue

Many candidates below are drawn from expressive programming languages and formalisms. They are not mutually exclusive: the framework may adopt one paradigm for one decision (type classes for subtype discipline) and another for a different decision (multiple dispatch for operation primitiveness). The triage admits only candidates that solve a problem the framework has already committed to. Paradigm features that conflict with ratified state are recorded in the [principled rejections](#^fleeting-rejections) log, not silently inherited — most often because they require runtime inference, which [t1-no-runtime-inference](1-framework/framework-foundations#^t1-no-runtime-inference) forecloses.

> [!important] Two levels of "object" — do not conflate them
> "Object-oriented" enters this design at two distinct levels, and a candidate, criterion, or commitment lives at exactly one of them. Confusing the two is a recurring hazard — for example, applying a framework-level commitment such as the OOP-exclusion in [t2-subtype-discipline](2-architecture/object-kinds#^t2-subtype-discipline) to a content-level taxonomy, or vice versa.
>
> - **Level 1 — the framework's representation language.** The framework *is built out of* epistemic objects (`Claim`, `Definition`, `Proof`, …) inspired by OOP: they have kinds, fields, an admission test, a common abstract base. Candidates and commitments at this level: [Python-inspired OOP](#^fleeting-python-oop), [type classes / traits](#^fleeting-type-classes), [t2-subtype-discipline](2-architecture/object-kinds#^t2-subtype-discipline), [t2-common-abstract-base](2-architecture/object-kinds#^t2-common-abstract-base), the object-kinds theme. "Object" here means *an epistemic record the framework stores*.
> - **Level 2 — what the epistemic content speaks about.** A statement, proposition, or idea is *about* concepts, systems, and relations that can themselves be read as objects — a network is a system, a feedforward network a subtype, a flow of information a property. Candidates at this level: the [concept-type taxonomy](3-aspect-specific/ontology#^t3-concept-type-taxonomy) (system / subtype / property / process), [concept-as-class vs. concept-as-object metamodeling](#^fleeting-concept-metamodeling). "Object" here means *a referent the stored content describes*.
>
> A level-1 epistemic object (a `Definition` record) and a level-2 object (the `network` the definition is about) are categorically different. A framework-level subtype decision governs how `Definition` relates to `Claim`; a content-level subtype taxonomy governs how the *concept* "feedforward network" relates to the *concept* "network". The same word "subtype" applies at both levels and means different things.

---

### Bearing on subtype discipline and inheritance

These candidates feed the reopen on [t2-subtype-discipline](2-architecture/object-kinds#^t2-subtype-discipline) — the former standalone `^t2-no-inheritance` constraint was folded into that open question as the rejection rationale for the OOP-inheritance alternative. The re-ratification weighs five alternatives — tagged unions, schema refinement, hybrid, OOP inheritance, type classes / traits.

#### Python-inspired OOP for epistemic objects ^fleeting-python-oop

**Source.** Python's class-based OOP with attributes, methods, inheritance, instances, typing annotations, dataclasses, enums, duck typing, logical operators on propositional content, lambdas, containers.

**Bears on.**

- [t2-subtype-discipline](2-architecture/object-kinds#^t2-subtype-discipline) — admits OOP inheritance as a candidate primitive for subtypes of epistemic objects. **Triggers reopen** (recorded at that open question as a `[!missing] Reopen pending` callout).
- [t2-operation-primitiveness](2-architecture/operations-and-modes#^t2-operation-primitiveness) — admits binding operations as object methods as a candidate, alongside the existing four (definitional fiat / proof of termination / schema calculus / open library). See the operation-primitiveness group below.
- [t2-partial-formalization-profiles](2-architecture/granularity#^t2-partial-formalization-profiles) — duck typing and forward references route here: a draft profile admits them; a strict profile does not.
- [t2-layering-source-of-truth](2-architecture/layering) — class vs. instance mirrors schema/meta vs. canonical-layer; already implicit, not a new commitment.

**Six gaps for propositional knowledge** (folded in, not separately filed). Python primitives leave the following gaps that any adopting framework would need to extend:

- **Quantification** (∀, ∃) over open domains; Python's `all()`/`any()` operate only over iterables.
- **Modal operators** — necessity, possibility, "under conditions C", "in regime R". Needed because [valid licensing](1-framework/reasoning-integrity#^t1-valid-licensing) commits to monotonic and defeasible warrants. The worked-example suite sharpens this gap at the statement grain — hypothetical and counterfactual statement modality — filed separately as [statement modality](#^fleeting-statement-modality).
- **Epistemic attitudes** as propositional operators (X is known / conjectured / established), distinct from object-level status.
- **Approximate / partial / conditional equality** — "approximately equal", "up to a constant", "in the limit".
- **Reference vs. mention** — explicit discipline for talking *about* claims, definitions, terms.
- **Provenance and warrant attachment** on every proposition.

A concrete candidate solution to the propositional-content representation gap is [algebraic data types for formula syntax](#^fleeting-propositional-adt).

**Out-of-scope features.** Runtime evaluation of logical operators, lambdas, match, identity — see the [rejections log](#^fleeting-rejections). The framework may borrow Python's *syntax* for propositional content but not its *evaluation semantics*.

#### Type classes and traits (Haskell, Scala, Rust) ^fleeting-type-classes

**Source.** Haskell type classes (a type *supports an algebraic interface*, distinct from inheritance); Scala traits (typed mixins with composition); Rust traits (object-safe interfaces). One structural idea: an interface is satisfied by a type without the satisfying type being a subtype of the interface.

**Bears on.**

- [t2-subtype-discipline](2-architecture/object-kinds#^t2-subtype-discipline) — admits type classes / traits as a fifth alternative, alongside tagged unions, schema refinement, hybrid, and OOP inheritance.
- [t2-common-abstract-base](2-architecture/object-kinds#^t2-common-abstract-base) — traits are the typed implementation of the interface-contract pattern the `EpistemicObject` base already adopts. A candidate refinement of the abstract-base interface is the [uniform navigation protocol](#^fleeting-uniform-protocol).
- [t2-subtype-discipline](2-architecture/object-kinds#^t2-subtype-discipline) — **counterweight to the Python reopen**. Type classes give polymorphism without subtype substitutability: the same epistemic kind can simultaneously satisfy multiple algebraic interfaces without committing to a single inheritance line.

**Capability-interface candidates** surfaced by expert review. Each is an orthogonal capability a kind may or may not satisfy:

| Trait candidate | A kind satisfies it when it | Example bearer |
| --- | --- | --- |
| `Justifiable` | carries justifications | claim, theorem |
| `Formalizable` | maps to a formal object | textual claim |
| `SourceBacked` | traces to external sources | claim, definition |
| `Refutable` | admits counterexamples or defeaters | claim, argument |
| `Revisable` | participates in revision operations | most content kinds |
| `Composable` | composes with same-kind objects under a law | warrant, operation |
| `Substitutable` | admits substitution of sub-terms | formula, definition |
| `Normalizable` | has a canonical reduced form | formula, expression |
| `Visualizable` | exposes a rendering view | most content kinds |
| `Comparable` | admits comparison under a criterion | concept, result |
| `Versioned` | carries version lineage | every canonical object |

**Forward dependency.** Scala's deeper type-system features — higher-kinded types, variance, path-dependent types, abstract type members — are relevant only if the framework's schema-language deferral (main handoff "not in scope" section) is lifted. Noted; not filed now.

> [!note] Reinforcement, not a candidate
> The semantic-inclusion hierarchy (which categories necessarily include which) is distinct from the implementation-inheritance hierarchy (which fields and methods are inherited). This *reinforces* the OOP-exclusion rationale in [t2-subtype-discipline](2-architecture/object-kinds#^t2-subtype-discipline): semantic subtyping is authored as subtype relations, independent of any code inheritance. Recorded as support for the existing commitment, not as a new candidate.

---

### Bearing on operation primitiveness

These candidates feed [t2-operation-primitiveness](2-architecture/operations-and-modes#^t2-operation-primitiveness). The decision weighs the original four alternatives (definitional fiat / proof of termination / schema calculus / open library) plus the three below, plus the [Python-method](#^fleeting-python-oop) candidate.

#### Multiple dispatch (CLOS, Julia) ^fleeting-multiple-dispatch

**Source.** Common Lisp Object System (CLOS) and Julia. Operations are not owned by a single class; methods are attached to generic functions and selected on the tuple of types of all arguments.

**Bears on.** [t2-operation-primitiveness](2-architecture/operations-and-modes#^t2-operation-primitiveness) — admits multiple dispatch as a candidate alongside Python-style methods. Multiple dispatch matches the existing "operations are first-class schemas" stance better than the Python-method candidate, which binds operations to a single object.

**Domain-fit argument.** Operations on mathematical and epistemic tuples are not naturally owned by either argument. Concrete relation candidates surfaced by expert review:

| Operation | Dispatch participants | Why no single owner |
| --- | --- | --- |
| `supports(argument, claim)` | argument kind, claim kind | support depends on both kinds |
| `contradicts(statement, statement)` | two statement kinds | contradiction is relational, often symmetric |
| `instantiates(example, concept)` | example structure, concept kind | depends on both |
| `formalizes(textual_claim, formal_object)` | informal and formal representation | depends on both representations |
| `translates(object, target_language)` | source object, target formalism | depends on both |
| `equivalent(x, y, criterion)` | two objects plus a criterion | equivalence is criterion-relative |
| `applies(theorem, model, assumptions)` | theorem, model, assumption set | applicability is conditional on all three |
| `proves(proof, proposition, formal_system)` | proof, proposition, system | provability is system-relative |
| `task_relevant(representation, task, equivalence)` | representation, task, equivalence | relevance is task- and criterion-relative |

Resolving a [linking phrase](#^fleeting-relation-formalization) to a relation type by the kinds of its endpoints is itself a multiple-dispatch operation.

**Out-of-scope features.** The CLOS Metaobject Protocol — see the [rejections log](#^fleeting-rejections).

#### Term rewriting systems ^fleeting-term-rewriting

**Source.** Term rewriting systems. A rewrite rule has the form `l → r`: a left-hand pattern is replaced by a right-hand expression, producing an explicit transformation trace.

**Bears on.** [t2-operation-primitiveness](2-architecture/operations-and-modes#^t2-operation-primitiveness) — admits rewrite rules as a candidate sub-class of content-transforming operations, alongside Python-style methods and multiple dispatch. A rewrite produces a trace recording source, target, rule, and justification.

**Application range.** Formula normalisation, definition expansion, theorem application, notation translation, conceptual refinement, argument compression, proof transformation. The trace requirement aligns with [manipulable reasoning](1-framework/reasoning-integrity#^t1-manipulable-reasoning): transformations become explicit and inspectable, and reversible when the rule is invertible.

**Boundary.** A rewrite *records* an authored transformation; it is not *evaluated at runtime* to derive new content. The framework stores the rule and the trace; an author applies the rule. This keeps rewriting compatible with [t1-no-runtime-inference](1-framework/framework-foundations#^t1-no-runtime-inference).

**Explanatory non-neutrality** ([a derivation changes representation language](_worked-examples.md#^example-derivation-with-a-hidden-change-of-representation-language)). A rewrite can be *formally meaning-preserving yet explanatorily non-neutral* — rewriting the network function as a sum over paths makes some distributed effects look local, but only because locality has been relocated from units to paths, not discovered. The trace must therefore record more than source, target, rule, and justification: it must record the *explanatory shift* the rewrite induces — what the new representation makes appear local, simple, or salient that the old one did not. Without this, a rewrite silently changes what reads as explanatory while presenting itself as a neutral restatement.

#### Idea-improvement move vocabulary ^fleeting-move-vocabulary

**Source.** Knowledge Building theory. A fine-grained vocabulary of content-transforming moves: clarify (reduce ambiguity), distinguish (split conflated notions), generalize, specialize, operationalize, formalize, weaken (reduce excessive commitment), strengthen (add conditions or support), integrate (combine ideas), problematize (expose a hidden assumption or limitation). Two further move types: rise-above (synthesise a higher-level formulation from partial ideas) and metadiscourse (reasoning about the state of the inquiry itself).

**Bears on.** [t2-operation-primitiveness](2-architecture/operations-and-modes#^t2-operation-primitiveness) and the reasoning-fields theme, as candidate operation vocabulary. Distinct from the seven-activity taxonomy at [t1-activity-coverage](1-framework/expressive-depth#^t1-activity-coverage), which classifies *activities*; this is a finer vocabulary of *moves* within content production and revision. The *revisionary* family of the [linking-phrase taxonomy](#^fleeting-relation-formalization) overlaps this vocabulary — the relation grain and the move grain must be reconciled rather than both filed independently. The scholarly-discourse caveat applies: published-discourse ontologies describe finished discourse and must be extended with exploratory moves of exactly this kind.

> [!note] Re-typing is not one move — the three phenomena are routed separately
> Several worked examples surface a move that changes an object's *kind*. An earlier draft proposed a single `re-type` move covering all three; an adversarial audit found this fuses along the wrong seam — the three have three different authoring workflows and three existing homes, so no unifying move should be minted.
>
> - **Modelling-choice re-typing** ([a derivation changes viewpoint](_worked-examples.md#^example-derivation-whose-conclusion-is-a-changed-viewpoint), [context changes object type](_worked-examples.md#^example-claim-where-context-changes-the-type-of-the-object)) — treating a context variable as an instruction rather than an input feature. Already governed as a branch point by the ratified [rationale and rejected-alternative record](3-aspect-specific/arguments-reasoning#^t3-d-rationale-record): recorded as a branch with siblings. No new mechanism needed.
> - **Critique-driven re-typing** ([criticism creates a new object](_worked-examples.md#^example-claim-that-creates-a-new-object-by-criticism)) — a critique re-types the inquiry's *target object*, "an acceptable criterion" becoming "a family of tests". This is an undercutter whose payload is an object re-typing; routed to [what an attack edge targets](3-aspect-specific/arguments-reasoning#^t3-attack-target) as a structured-undercutter variant.
> - **Process-trajectory re-typing** ([temporal evolution changes conceptual status](_worked-examples.md#^example-claim-with-temporal-evolution-and-conceptual-instability)) — an object's kind changes along a *modelled process trajectory* (context shifting from auxiliary feature to organizing principle over training). This is a temporal fact about the phenomenon, distinct from authored revision tracked by [t1-revision-accountability](1-framework/research-activities-workflows#^t1-revision-accountability). It needs a *time-indexed object* whose kind can differ at trajectory points — an object-kinds-theme concern, recorded against the deferred [object taxonomy](../TODO), not a move.

---

### Bearing on the relation vocabulary and storage

These candidates feed [t2-typed-relation-vocabulary](2-architecture/relations-graph#^t2-typed-relation-vocabulary) and [t2-relation-storage-locus](2-architecture/relations-graph#^t2-relation-storage-locus). The reified-relation convergence note at the end of this group ties several of them together.

#### Typed-relation discipline ^fleeting-typed-relation-discipline

**Source.** Description Logics, restricted to its static modelling discipline (the runtime-reasoner features are rejected — see the [rejections log](#^fleeting-rejections)). Three static schema disciplines for relations, all checkable at author time:

- **Domain/range constraints.** Each relation declares an admissible source kind and target kind — `proves: Proof → MathematicalStatement`, `defines: Definition → Concept`, `supports: Argument → Claim`, `cites: EpistemicObject → Source`. Sharpens the closed typed relation vocabulary.
- **Declared structural-property metadata.** A relation carries metadata declaring whether it is transitive, symmetric, or has a named inverse — `dependsOn` is transitive, `proves` has inverse `isProvedBy`, `attacks` is *not* symmetric (directed).
- **Role reification / n-ary relations.** When a relation needs provenance, strength, or status, it becomes a first-class object (`SupportRelation` carrying supporter, supported, strength, context, source) rather than a bare binary edge.

**Bears on.** [t2-typed-relation-vocabulary](2-architecture/relations-graph#^t2-typed-relation-vocabulary) (domain/range and structural-property metadata) and [t2-relation-storage-locus](2-architecture/relations-graph#^t2-relation-storage-locus) (role reification). **Flag.** Whether declared transitivity is *materialised into a computed closure* is a separate decision: materialisation at read time would trip [t1-no-runtime-inference](1-framework/framework-foundations#^t1-no-runtime-inference). The metadata declaration is safe; the closure computation is not.

#### Named-graph / source-qualified assertions ^fleeting-named-graphs

**Source.** RDF named graphs. Every assertion is qualified by a source and context, so the same `(subject, predicate, object)` edge can hold in one source's frame and fail in another's. The relation itself becomes an epistemic object carrying source, context, and confidence.

**Bears on.** [t2-relation-storage-locus](2-architecture/relations-graph#^t2-relation-storage-locus) (the current edge model is single-context) and the open [t2-layer-feedback](2-architecture/layering#^t2-layer-feedback) question. A structural alternative the framework has not yet considered: edges qualified by an assertion frame rather than asserted absolutely.

#### Progressive relation formalization ^fleeting-relation-formalization

**Source.** Concept-map practice. Relations admit a maturity progression: an edge is a human-readable meaning-bearing phrase before it hardens into a controlled type. This is the relation-grain analogue of [t1-partial-formalization](1-framework/expressive-depth#^t1-partial-formalization), which currently covers content maturity but not edge maturity.

**Normalization ladder.** A relation may rest at any of six maturity levels, and different relations in the same corpus may rest at different levels:

| Level | Form | Example |
| --- | --- | --- |
| 0 | prose only | "this reminds me of the invariance issue" |
| 1 | explicit linking phrase | "linear decodability is weaker than causal contribution" |
| 2 | relation family | `comparative_strength` |
| 3 | controlled relation type | `weaker_than` |
| 4 | ontology-aligned relation | `skos:broader`, `cito:extends` — optional, exposition-facing rung |
| 5 | formal predicate | `WeakerCriterion(c1, c2)` |

Forcing level 5 too early distorts inquiry; staying permanently at level 0 reproduces prose drift. Level 4 is exposition-flavoured and optional; levels 0–3 and 5 are framework-internal.

**Linking phrase as an object.** A linking phrase is not stored as a bare string. It is an intermediate semantic unit — neither prose nor formal predicate — carrying declared metadata: a surface form, a relation family, a polarity, a modality, a directionality, a context-sensitivity rating, and a set of candidate formalizations. A phrase-bearing edge is therefore a reified relation (see the convergence note below).

**Linking-phrase family taxonomy.** A candidate classification of linking phrases by **epistemic function** — which satisfies [functional separation of concerns](1-framework/framework-foundations#^t1-functional-separation) (classify by function, not grammatical form):

| Family | Example linking phrases | Function |
| --- | --- | --- |
| definitional | "is defined as", "means", "is a kind of" | concept stabilization |
| contrastive | "differs from", "should not be conflated with" | distinction construction |
| evidential | "supports", "is evidence for", "motivates" | support relation |
| critical | "challenges", "undermines", "is insufficient for" | objection or limitation |
| explanatory | "explains", "accounts for", "is caused by" | explanatory structure |
| methodological | "is measured by", "is operationalized by" | method-theory bridge |
| dependency | "depends on", "requires", "presupposes" | background commitment |
| derivational | "follows from", "is derived from", "generalizes" | reasoning trajectory |
| analogical | "is analogous to", "transfers from" | cross-domain transfer |
| contextual | "holds under", "relative to", "assuming" | scope restriction |
| rhetorical | "introduces", "summarizes", "motivates" | discourse organization |
| revisionary | "refines", "weakens", "splits into" | inquiry development |

The taxonomy stays open: new linking phrases are admissible, but each should eventually map to one or more controlled families.

> [!warning] Overlap to resolve, not to file as independent
> Two overlaps must be surfaced for whoever resolves the relation vocabulary. (a) The twelve families overlap the relation-vocabulary *contents*, which are deferred to [the project TODO](../TODO); this taxonomy is candidate input to that deferred decision, not a parallel vocabulary. (b) The *revisionary* family (refines, weakens, splits-into) overlaps the [idea-improvement move vocabulary](#^fleeting-move-vocabulary); the relation grain and the move grain must be reconciled rather than both filed as independent vocabularies.

**Endpoint-dependent phrase resolution.** The same linking phrase resolves to different relation types depending on the kinds of *both* endpoints: "is a stronger version of" maps to logical implication between two theorems, to specialization between two concepts, and to warrant-strengthening between two arguments. Resolving a phrase to a type is therefore itself a multiple-dispatch operation — this connects the entry to [multiple dispatch](#^fleeting-multiple-dispatch).

**Carries a tension** with the ratified closed-and-typed relation vocabulary at [t2-typed-relation-vocabulary](2-architecture/relations-graph#^t2-typed-relation-vocabulary). A `[!missing]` tension callout is placed at that decision. Resolution must state whether a draft profile admits free linking phrases later resolved to declared types, or whether closure holds at every maturity level.

> [!note] Scholarly-discourse ontologies — out of architectural scope
> An expert review surveyed scholarly-discourse ontologies (SWAN, SALT, CiTO, DoCO, DEO). These are vocabularies for annotating finished documents, and the framework treats exposition as a secondary derived artifact rather than a primary design concern (per [t1-activity-access-rights](1-framework/research-activities-workflows#^t1-activity-access-rights)). They are downstream of the exposition-is-derived deferral — not rejected by principle, but not filed as candidates. Three recurring generalized points turn out to restate ratified state: "the same content plays different roles in different contexts" (DoCO/DEO) restates the role separation in [t1-recoverable-reasoning](1-framework/reasoning-integrity#^t1-justification-levels) and converges with [Context as a first-class object](#^fleeting-context-object); "discourse is about what is said, not validated fact" (SWAN) restates [t2-epistemic-status](2-architecture/object-kinds#^t2-epistemic-status) and [t1-partial-formalization](1-framework/expressive-depth#^t1-partial-formalization). The one keepable residue — a set of custom relation families (conceptual, argumentative, evidential, methodological, derivational, inquiry-dynamic, discourse-rhetorical) — is candidate input to the deferred relation vocabulary, with the same overlap caveats as the phrase-family taxonomy above. Citation-intent typing is filed separately below.

#### Citation-intent vocabulary ^fleeting-citation-intent

**Source.** The CiTO citation-typing ontology. Typing `cites` edges by intent. The framework has a `cites` relation but no intent typing — whether a citation extends, disputes, uses-method-from, or corroborates the cited work.

**Bears on.** [t2-typed-relation-vocabulary](2-architecture/relations-graph#^t2-typed-relation-vocabulary) and the literature-facing themes.

#### Convergence — the reified relation object ^fleeting-edge-scope

A reified relation carrying source, target, phrase, relation type, context, provenance, and status is the common object behind four separately filed proposals: [role reification](#^fleeting-typed-relation-discipline), [source-qualified named graphs](#^fleeting-named-graphs), [Context as a first-class object](#^fleeting-context-object), and the [linking-phrase object](#^fleeting-relation-formalization). These four describe one object by different routes and should be resolved together.

An earlier draft filed two further "edge-level scope indices" as a separate candidate; an adversarial audit found they are not an independent construct but **two field specifications on the reified edge** — once an edge is reified into an object with context and status fields, the two indices are simply those fields. They are folded in here:

- **Bounded-scope field.** An edge may hold only within an explicit boundary, with a stated failure condition outside it — an analogy useful only insofar as both terms share intrinsic directions of transformation and misleading once that assumption lapses ([an analogy has restricted scope](_worked-examples.md#^example-argument-whose-premise-is-an-analogy-with-restricted-scope)); a model that isolates a structure a phenomenon *may* instantiate under some conditions, pending a future mapping ([a model has an ambiguous relation to a phenomenon](_worked-examples.md#^example-ambiguous-relation-between-model-and-phenomenon)). This is a *context field with a failure condition* on the reified edge — the relation-grain counterpart of the applicability conditions already carried by [reasoning schemes](3-aspect-specific/arguments-reasoning#^t3-reasoning-schemes).
- **Edge-local status field.** A hedge may scope to a single inferential link inside a statement, not to the whole statement or its objects — "plausible, though not yet demonstrated" attaching to one observation-to-mechanism link ([a statement mixes epistemic statuses](_worked-examples.md#^example-mixed-epistemic-status-within-a-single-statement)). This is the *status field* on the reified edge: the per-kind status enums at [t2-epistemic-status](2-architecture/object-kinds#^t2-epistemic-status) attach status to an *object*, but a reified edge carries its own status, so a statement can be part-asserted, part-hedged.

The rejected edge-strength / adequacy grade is not duplicated here: the only worked example behind it, [definition by refusal of inadequate operationalizations](_worked-examples.md#^example-definition-by-refusal-of-inadequate-operationalizations), concerns a *rejected definitional criterion*, which the multi-rejection negative-definition template at [t3-definition-normal-form](3-aspect-specific/ontology#^t3-definition-normal-form) records as the rejection's adequacy grade.

**Bears on** [t2-typed-relation-vocabulary](2-architecture/relations-graph#^t2-typed-relation-vocabulary) and [t2-relation-storage-locus](2-architecture/relations-graph#^t2-relation-storage-locus): the reified edge, with its context, status, bounded-scope, and edge-local-status fields, is the resolution locus for all of these.

---

### Bearing on object kinds and the taxonomy

These candidates feed the object-kinds theme, [t2-common-abstract-base](2-architecture/object-kinds#^t2-common-abstract-base), the Tier-3 [ontology theme](3-aspect-specific/ontology), and the deferred [object taxonomy](../TODO).

#### Policy and criterion fields on content kinds ^fleeting-policy-fields

Content kinds may carry explicit policy and criterion fields rather than treating concepts as passive labels. Candidate fields not already covered by a ratified decision:

- `IdentityCriterion` — decides whether two objects count as the same concept.
- `EquivalenceCriterion` — decides whether two formulations are equivalent under a chosen standard.
- `RefinementPolicy` — controls admissible specialisation of a concept.
- `FormalizationPolicy` — determines how an informal claim maps to a formal object.

**Bears on** the [object-kind field design](3-aspect-specific/ontology) (Tier-3 ontology stub). Fields the expert listed that are *already covered* — `RevisionPolicy` (revision-vocabulary theme), `JustificationPolicy` (warrant-vocabulary theme), `ViewPolicy` (rendering-views theme) — are not refiled. The Metaobject-Protocol framing the expert attached to these fields is rejected; see the [rejections log](#^fleeting-rejections). The fields themselves are static schema declarations and do not require a runtime-modifiable object system.

#### Uniform navigation protocol on the abstract base ^fleeting-uniform-protocol

Every kind exposes a uniform read-side protocol: `describe`, `dependencies`, `justifications`, `counterparts`, `history`, `views`. A concept, theorem, proof, and argument all support comparable inspection even when their internal structures differ.

**Bears on** [t2-common-abstract-base](2-architecture/object-kinds#^t2-common-abstract-base): the abstract base could declare more interface methods than identity, kind, status, and outgoing edges. This is a structural commitment about the read-side interface; it is distinct from Smalltalk's runtime message-passing (rejected — see the [rejections log](#^fleeting-rejections)).

#### Concept-as-class vs. concept-as-object metamodeling ^fleeting-concept-metamodeling

A concept must be representable both as a category (a class of things) and as a manipulable epistemic object (carrying a definition, history, sources, variants, critiques). "Representation" is simultaneously a class and an object *about* that class. The proposed discipline keeps the two explicit — a `ConceptObject` that `denotesClass` a category — rather than conflating them.

**Bears on** the object-kinds theme. Sharpens the [concept-type taxonomy](3-aspect-specific/ontology#^t3-concept-type-taxonomy) Tier-3 open question with a use/mention-style distinction between the concept-object and the class it denotes.

#### Candidate kind-set for the object taxonomy ^fleeting-kind-set

A concrete candidate set of object kinds for the deferred [object taxonomy](../TODO): Question, Idea, Claim, Argument, Warrant, Assumption, Distinction, Derivation, Example, Counterexample, Criterion, Perspective, Source, Move.

Most of these correspond to kinds the framework already anticipates. Four are novel relative to anything currently filed:

- **Idea** — pre-formal candidate content, addressable and citable before it has the typed structure of a `Claim`. Research ideas need stable identity before full formal semantics. Bears on [t1-partial-formalization](1-framework/expressive-depth#^t1-partial-formalization) and the [object-kind admission test](2-architecture/object-kinds#^t2-object-kind-admission): is a pre-formal `Idea` a distinct kind, or an early-maturity `Claim`?
- **Distinction** — a conceptual split, as a first-class object, that prevents conflation of two notions.
- **Perspective** — an interpretive frame relative to which content is stated.
- **Move** — an inquiry operation reified as an object.

**Bears on** the deferred object taxonomy. Connects to the [concept-type taxonomy](3-aspect-specific/ontology#^t3-concept-type-taxonomy) and the [epistemic-gap subtypes](3-aspect-specific/ontology#^t3-epistemic-gap-subtypes) already filed.

The `Example` kind carries two distinct roles, surfaced by [a boundary case as concept probe](_worked-examples.md#^example-boundary-case-as-concept-probe). An *illustrative* example instantiates a concept or claim to aid understanding. A *probe* example is used deliberately to force a `Distinction` explicit or to test where its boundary lies — its function is diagnostic, not illustrative. The kind-set should mark the role, since the two are validated and consumed differently: a probe example is admissible even when it instantiates nothing, because its purpose is to stress a distinction.

#### Option-under-criteria content sub-structure ^fleeting-qoc-substructure

**Source.** QOC design rationale. Whether research *content* — not only design decisions — can carry an explicit Question / Option / Criterion sub-structure, where a question opens candidate options assessed against named criteria. The framework's `Question` kind currently decomposes into sub-questions; it has no explicit option-compared-under-criteria sub-structure. The framework's own Tier-2 deliberation already uses QOC form (a `[!QUESTION]` callout with alternatives weighed against bearing criteria); the open question is whether research content should be representable the same way.

**Bears on** the reasoning-structure and object-kinds themes. Minor candidate.

#### Granularity-relative object identity ^fleeting-object-scope

**Source.** [A conceptual move that changes granularity](_worked-examples.md#^example-conceptual-move-that-changes-granularity). An earlier draft paired this with an explanation-level index under "object-level scope indices"; an adversarial audit found the explanation-level index is a *context index on a claim*, not an object-decomposition concern, and it has been folded into [Context as a first-class object](#^fleeting-context-object). The genuine residue — the one item that bears on object decomposition — is below.

What counts as one object depends on the analysis grain: one representation at the layer level may decompose into several task-specific sub-representations once the computation is analysed along paths rather than units, as [a conceptual move that changes granularity](_worked-examples.md#^example-conceptual-move-that-changes-granularity) shows. Neither decomposition is privileged. The framework needs a way to relate the same content's decompositions across granularities — a `Perspective`-indexed family of decompositions — rather than assuming one canonical object set.

**Bears on** [t1-typed-object-decomposition](1-framework/framework-foundations#^t1-typed-object-decomposition): this is a genuine tension with the criterion's commitment to a structured set of typed objects, recorded as a `[!missing]` callout there. The criterion does not say the object set is unique.

#### Non-assertive statement categories ^fleeting-non-assertive-statements

**Source.** [Strategic non-definition](_worked-examples.md#^example-research-move-involving-strategic-non-definition), [mixed epistemic status](_worked-examples.md#^example-mixed-epistemic-status-within-a-single-statement), [a derivation that changes representation language](_worked-examples.md#^example-derivation-with-a-hidden-change-of-representation-language), and [ambiguity preservation](_worked-examples.md#^example-statement-whose-role-is-to-preserve-ambiguity). The framework's content kinds assume a statement *asserts* domain content. Several examples carry statements whose function is not assertion.

- **Inquiry-steering content.** A statement may be a directive about the research process — defer this definition, settle that constraint first, keep this term plural for now — not a claim about the domain ([strategic non-definition](_worked-examples.md#^example-research-move-involving-strategic-non-definition), [ambiguity preservation](_worked-examples.md#^example-statement-whose-role-is-to-preserve-ambiguity)). The [move vocabulary](#^fleeting-move-vocabulary)'s `metadiscourse` move names the act of producing such a statement; inquiry-steering content needs to be a recognised statement category so it is not validated as a domain claim.
- **Cautionary / warning content.** A statement may be a warning — that a concept is dangerous, that a rewrite relocates rather than discovers locality — cautionary rather than assertive ([a concept has a failure mode](_worked-examples.md#^example-statement-whose-content-is-a-failure-mode-of-a-concept), [a derivation changes representation language](_worked-examples.md#^example-derivation-with-a-hidden-change-of-representation-language)).

**Bears on** the object-kinds theme and the [candidate kind-set](#^fleeting-kind-set): non-assertive statements need a category (or a per-statement assertive/non-assertive marker) so validation does not treat a process directive or a warning as a domain claim. [Time-bounded ambiguity preservation](_worked-examples.md#^example-statement-whose-role-is-to-preserve-ambiguity) is inquiry-steering content with a temporal scope.

#### Meta-conceptual content ^fleeting-metalinguistic-content

**Source.** [A conceptual distinction revises its target concept](_worked-examples.md#^example-conceptual-distinction-that-also-revises-the-target-concept), [a research question embeds a critique](_worked-examples.md#^example-research-question-embedded-in-a-critique), [definition by refusal of inadequate operationalizations](_worked-examples.md#^example-definition-by-refusal-of-inadequate-operationalizations), and [a derivation changes viewpoint](_worked-examples.md#^example-derivation-whose-conclusion-is-a-changed-viewpoint). An earlier draft of this candidate bundled four unlike items under "metalinguistic content"; an adversarial audit found the convergence false — a validator treats each of the four differently — and the bundle is dissolved. Two items left for other homes (see the note below); the coherent residue is content stated *one level up from the research domain*, about concepts rather than their referents.

- **Meta-conceptual statement.** A statement may be *about the criteria for applying a concept*, not about the concept's referent — "the distinction between information being present and information being used changes what should count as representation", as [a conceptual distinction revises its target concept](_worked-examples.md#^example-conceptual-distinction-that-also-revises-the-target-concept) shows. Such a statement operates one level up from domain content: its object is the concept's application conditions. *Effect:* the framework marks this level so a meta-conceptual statement is **not** run through domain-claim validation — it has no domain truth value to check.
- **Metaphor as a diagnosable object.** A conceptual metaphor — "container model", "shadow" — can be a named object that an argument targets, diagnoses, or uses ([a research question embeds a critique](_worked-examples.md#^example-research-question-embedded-in-a-critique), [definition by refusal of inadequate operationalizations](_worked-examples.md#^example-definition-by-refusal-of-inadequate-operationalizations)); a term may also occupy a *hybrid register*, simultaneously metaphorical and technical ([a derivation changes viewpoint](_worked-examples.md#^example-derivation-whose-conclusion-is-a-changed-viewpoint)). **Thin item:** this is two worked examples wide and proposes no mechanism (no stored field, no author-time check). Retained as a flagged sub-item; whoever takes up this candidate should either build it a mechanism or drop it.

**Bears on** the object-kinds theme.

> [!note] Two items moved out of this candidate
> The dissolved bundle's other two items have been re-homed. **Usage-norm content** (a statement asserting how a community uses a term, as in [a claim whose force depends on disciplinary perspective](_worked-examples.md#^example-claim-whose-force-depends-on-disciplinary-perspective)) is a first-order, checkable claim with a truth value and a source; it folds into the lexical-term level of the [definition-normal-form](3-aspect-specific/ontology#^t3-definition-normal-form) five-level term/concept separation. **Hazard-flagged fragment** (teleological-looking phrasing flagged for an interpretive risk, as in [a research constraint](_worked-examples.md#^example-statement-whose-main-content-is-a-research-constraint)) is not content at all but a *linter rule*; it belongs in the validation-views theme as an author-time lint warning, not as a content kind.

#### Content about sources ^fleeting-source-facing-content

The [source-sensitive claim with interpretive uncertainty](_worked-examples.md#^example-source-sensitive-claim-with-interpretive-uncertainty) and the [critique of a hidden assumption in a literature tradition](_worked-examples.md#^example-critique-of-a-hidden-assumption-in-a-literature-tradition) raise two source-facing items. An adversarial audit found they belong in two different places, not one candidate.

- **Source-interpretation content** ([a source-sensitive claim has interpretive uncertainty](_worked-examples.md#^example-source-sensitive-claim-with-interpretive-uncertainty)) — a hedged claim about what an author means. This is exposition-adjacent: the framework treats literature-facing work as a derived artifact per [t1-activity-access-rights](1-framework/research-activities-workflows#^t1-activity-access-rights), and interpreting a source is literature-facing. It is **deferred, not a live candidate** — recorded as a pointer for whoever resolves the literature-facing theme, alongside [citation-intent](#^fleeting-citation-intent). No mechanism is filed now.
- **Tradition-level diffuse source** ([a literature tradition carries a hidden assumption](_worked-examples.md#^example-critique-of-a-hidden-assumption-in-a-literature-tradition)) — a critique targeting an inference pattern attributed to "much of the literature", a diffuse, uncitable aggregate distinct from the identifiable `Source` kind. This is **in architectural scope**: the critique itself lives on the canonical layer, and the diffuse aggregate needs a representation the `Source` kind does not provide. It bears directly on the object-kinds theme (a tradition or literature-pattern object alongside `Source`) and on [t2-typed-relation-vocabulary](2-architecture/relations-graph#^t2-typed-relation-vocabulary) (a critique edge whose target is a diffuse source). Filed against those themes, not bundled with the deferred source-interpretation item.

**Bears on** the object-kinds theme and [t2-typed-relation-vocabulary](2-architecture/relations-graph#^t2-typed-relation-vocabulary) (tradition-level diffuse source); the literature-facing theme (source-interpretation, deferred).

---

### Bearing on status and partial formalization

#### Four-way detection-status distinction with explicit closure ^fleeting-proof-status

Any *detection claim* admits four distinct values that the framework must not conflate. The originating case is proof status — whether a statement has a proof:

- **No stored result** — nothing has been asserted; no claim is made about whether a result exists.
- **Known absence** — an explicitly closed search context records that no result exists.
- **Disproved** — a counterexample or contradiction is established.
- **Undecided** — a tracked epistemic status.

The framework is a closed-world authored store, so the open-world framing the source assumes is moot; the substantive contribution is the four-way distinction and the *explicit-closure* mechanism (a closed context records that a search terminated without result).

**Generalisation beyond proofs** ([absence used as evidence](_worked-examples.md#^example-statement-using-absence-as-evidence)). The same four-way distinction is needed for *any* detection claim, not only proofs. The absence of a clean context axis in a representation does not establish that context is absent — it may show only that no axis-shaped marker was detected, while context acts by deforming the whole space. Conflating "no marker found" with "marker established absent" is a false-negative inference the four-way distinction blocks: a detection claim must record which of the four statuses holds, and "no stored result" must never be read as "known absence".

**Bears on** the status-vocabulary theme and on [valid licensing](1-framework/reasoning-integrity#^t1-valid-licensing): the distinction between "no result asserted" and "absence established" is exactly what silent-incompleteness detection turns on.

---

### Bearing on arguments and reasoning

These candidates feed the [arguments-reasoning theme](3-aspect-specific/arguments-reasoning). Two contributions from the same review were substantial enough to file directly there as open questions: [t3-reasoning-schemes](3-aspect-specific/arguments-reasoning#^t3-reasoning-schemes) and [t3-attack-target](3-aspect-specific/arguments-reasoning#^t3-attack-target).

#### Algebraic data types for propositional content ^fleeting-propositional-adt

Propositional and formula content is represented as recursive algebraic data types (`And`, `Or`, `Not`, `Atom`, `Implies`), not as free-form strings or prose. The grammar `φ ::= p | ¬φ | φ∧φ | φ∨φ | φ→φ` is more robust than string representations and supports structural pattern matching.

**Bears on** [t1-rich-prose-expressivity](1-framework/expressive-depth#^t1-rich-prose-expressivity) and the reasoning-fields and arguments-reasoning themes. A candidate solution to the propositional-content representation gap among the six propositional-knowledge gaps in [Python-inspired OOP](#^fleeting-python-oop).

#### Grammars for reasoning-assembly fields ^fleeting-reasoning-field-grammars

**Source.** The formal-expression criterion [t1-formal-expression](1-framework/framework-foundations#^t1-formal-expression) forecloses prose defaults in any semantic field. [The reasoning-fields theme](3-aspect-specific/reasoning-fields.md) currently proposes prose defaults for several reasoning-assembly cells: strategic rationale at citation sites, explanatory gain after contributions, route selection, deficiency addressed, rejected-alternative records. Each of these is a semantic field — operations and validators read them — and so each requires a grammar rather than free prose.

**Open question.** What grammar does each reasoning-assembly cell take?

- **Strategic rationale.** Candidate shapes: a controlled vocabulary of move-types crossed with a typed reference to the deficiency the move addresses; a structured record (`{move_type, target_deficiency_ref, expected_gain_kind}`); a grammar over the operation library's signatures.
- **Explanatory gain.** Candidates: a typed reference to the state property that was previously absent and is now present (e.g. a reference to a newly licensed claim, a discharged assumption, a closed sub-goal); a structured delta record over the snapshot.
- **Route selected and rejected alternatives.** Candidates: typed references to candidate operations or sub-arguments from a registry; structured `{candidate_ref, rejection_reason_kind}` records with rejection-reason kinds drawn from a closed vocabulary.
- **Deficiency addressed.** Candidate: a typed reference into a gap/question registry; the same gap-subtype vocabulary as [t3-epistemic-gap-subtypes](3-aspect-specific/registries-indexes#^t3-epistemic-gap-subtypes).

**Bears on** [t1-formal-expression](1-framework/framework-foundations#^t1-formal-expression) (the criterion that forces the question open), [t2-field-typing](2-architecture/object-kinds#^t2-field-typing) (the meta-schema discipline that will host the partition), the entirety of [the reasoning-fields theme](3-aspect-specific/reasoning-fields.md), and [t2-x5](1-framework/_tensions#^t2-x5) (the tension that pays the authoring cost these grammars impose). Until grammars are chosen, the prose defaults in the reasoning-fields theme are inconsistent with the framework-tier commitment.

#### Statement modality — hypothetical and counterfactual content ^fleeting-statement-modality

**Source.** [An undercutting condition hidden inside an example](_worked-examples.md#^example-argument-with-an-undercutting-condition-hidden-inside-an-example), [a research question embedded in a critique](_worked-examples.md#^example-research-question-embedded-in-a-critique), and [implicit dependency on counterfactuals](_worked-examples.md#^example-statement-with-implicit-dependency-on-counterfactuals). The framework's content kinds and warrant model assume a statement *asserts*. Two statement modalities the framework has no native construct for:

- **Hypothetical statement.** A whole statement may be conditional — "if such evidence held, it would mean Z" — asserting no fact ([an argument hides an undercutting condition](_worked-examples.md#^example-argument-with-an-undercutting-condition-hidden-inside-an-example), [a research question embeds a critique](_worked-examples.md#^example-research-question-embedded-in-a-critique)). The framework can mark a *warrant* as defeasible, but it cannot currently mark a *statement* as hypothetical, so a hypothetical statement risks being read as an assertion. A per-statement hypothetical marker is needed.
- **Counterfactual content.** A claim about what the computation *would have been* under an unrealized intervention — "the feature contributes to the task" unpacks as a claim about the computation without it ([a statement depends on counterfactuals](_worked-examples.md#^example-statement-with-implicit-dependency-on-counterfactuals)). A counterfactual is neither an asserted claim nor a defeasible warrant; it is a claim about an unrealized condition, and it is meaningful only relative to an *admissible intervention family*. This is sharper than mere possibility.

**Bears on** the propositional-content concern and the reasoning-fields theme. The propositional-content gaps were first collected under [Python-inspired OOP](#^fleeting-python-oop)'s six-gaps list because that entry happened to host the list; statement modality is filed here as its own candidate since it concerns statement-level modality, not Python OOP. Counterfactual content connects to [the intervention-admissibility concern](_worked-examples.md#^example-statement-introducing-a-comparative-adequacy-criterion) and to the constitutive definition-validation entanglement recorded at [t3-definition-normal-form](3-aspect-specific/ontology#^t3-definition-normal-form).

#### Proof-assistant model for proof objects ^fleeting-proof-model

Proofs are structured objects, not prose fields attached to propositions. A proof carries steps, assumptions, dependencies on mathematical objects, and a checker. A proposition may carry several proof objects and several countermodels. The elaboration/checking split — a semi-formal statement is elaborated into a formal object, then a smaller trusted checker validates it — is the central borrowed distinction.

**Bears on** the [arguments-reasoning theme](3-aspect-specific/arguments-reasoning) (proof structure is currently a Tier-3 stub), [t2-operation-primitiveness](2-architecture/operations-and-modes#^t2-operation-primitiveness) (tactics as goal-to-subgoal operations), and the open `^t3-assumption-discharge-mechanism` decision (assumptions as proof context). Borrowed concepts: context (active assumptions, definitions, notation), term, tactic, goal state, kernel, elaborator, dependency graph.

#### Argumentation-graph semantics ^fleeting-argumentation-graph

**Source.** Dung-style abstract and structured argumentation. An argument graph carries arguments plus typed attack, support, and defeat edges. Acceptance semantics — grounded, preferred, stable, admissible — classify arguments as accepted, rejected, or undecided.

**Bears on** the [arguments-reasoning theme](3-aspect-specific/arguments-reasoning).

**Authored edge types.** Beyond attack, support, and defeat, the worked-example suite requires a fourth authored edge: a **competing-explanation edge**. When two explanations are offered for one observation — a separability that is causal *or* epiphenomenal ([an explanatory gap rather than a claim](_worked-examples.md#^example-statement-that-introduces-an-explanatory-gap-rather-than-a-claim)); a gating mechanism *or* a decoding-basis change ([mixed epistemic status](_worked-examples.md#^example-mixed-epistemic-status-within-a-single-statement)); context acting as a separable axis *or* as a global deformation ([absence used as evidence](_worked-examples.md#^example-statement-using-absence-as-evidence)); decodability read as representation *or* as redundant statistical alignment ([an undercutting condition hidden inside an example](_worked-examples.md#^example-argument-with-an-undercutting-condition-hidden-inside-an-example)) — neither attacks, supports, nor defeats the other; they *compete* as accounts of the same target. The competing-explanation edge records that two objects are rival explanations of one observation, an authored relation distinct from attack.

**Carve-out.** The *authored* attack/support/defeat/competing-explanation edges are admissible and fit the closed relation vocabulary at [t2-typed-relation-vocabulary](2-architecture/relations-graph#^t2-typed-relation-vocabulary). The *computation* of acceptance status under a semantics requires runtime evaluation of the graph and conflicts with [t1-no-runtime-inference](1-framework/framework-foundations#^t1-no-runtime-inference) — see the [rejections log](#^fleeting-rejections). Only the authored-edge subset is a live candidate.

#### Legitimate mutual constraint vs. vicious circularity ^fleeting-mutual-constraint

**Source.** [Conceptual dependence between two definitions](_worked-examples.md#^example-conceptual-dependence-between-two-definitions) and [ambiguous explanatory priority](_worked-examples.md#^example-ambiguous-explanatory-priority). [valid licensing](1-framework/reasoning-integrity#^t1-valid-licensing) forbids a justification chain that returns to itself. Two examples show structures that *look* circular but are not vicious justification cycles, and the framework must distinguish them.

- **Co-definition.** Two definitions can be mutually dependent — "task variable" cannot be fixed independently of "task", because what counts as a variable depends on which distinctions the task makes relevant, as [conceptual dependence between definitions](_worked-examples.md#^example-conceptual-dependence-between-two-definitions) shows. The genus-differentia normal form at [t3-definition-normal-form](3-aspect-specific/ontology#^t3-definition-normal-form) authors one definiendum against forward-reference placeholders; mutually dependent definitions must be *co-authored* — neither is a stable placeholder for the other. The framework needs a co-definition construct: a cluster of definitions admitted together, the mutual constraint recorded and marked legitimate.
- **Co-determination.** Two objects can each explain an aspect of the other — the task explains the geometry, the geometry explains which aspects of the task are effectively treated as relevant, as [ambiguous explanatory priority](_worked-examples.md#^example-ambiguous-explanatory-priority) shows. A simple directed `explains` edge is insufficient; the framework needs a co-determination relation. A precise `Distinction` (here task vs. effective task) often dissolves the apparent circularity by separating the endpoints, so the two edges no longer share both ends.

**Bears on** [valid licensing](1-framework/reasoning-integrity#^t1-valid-licensing): the criterion must distinguish a vicious justification cycle from a legitimate mutual constraint between definitions or between explanatory relations. A `[!missing]` tension callout is placed at that criterion. Also bears on [t3-definition-normal-form](3-aspect-specific/ontology#^t3-definition-normal-form) (the co-definition construct) and [t2-typed-relation-vocabulary](2-architecture/relations-graph#^t2-typed-relation-vocabulary) (the co-determination relation).

> [!note] Method-result circularity is filed elsewhere
> [Method-result circularity](_worked-examples.md#^example-statement-where-a-method-produces-the-object-it-measures) — a method partly constructing the object it then measures — superficially shares the word "circular" but is neither a mutual constraint nor a justification cycle: nothing in the recorded chain returns to itself. It is a structured undercutter, filed at [what an attack edge targets](3-aspect-specific/arguments-reasoning#^t3-attack-target).

---

### Bearing on validation and workflow

#### Context-local disjointness as author-time validation ^fleeting-disjointness-validation

Disjointness declarations — `Conjecture ⊓ Theorem ⊑ ⊥`, `AcceptedClaim ⊓ RejectedClaim ⊑ ⊥` — as author-time validation rules, not runtime inference. The key qualification: contradiction in a research corpus is sometimes epistemically meaningful, so inconsistency must be **scoped to a context** (project, source, belief state), never imposed globally. The proposed form is a localised `InconsistentWithin(x, context)` rather than global collapse.

**Bears on** the validation-views theme (disjointness as a validation rule) and the open [t2-layer-feedback](2-architecture/layering#^t2-layer-feedback) question (how a localised inconsistency propagates).

#### Ownership and borrowing (Rust) ^fleeting-ownership-borrowing

**Source.** Rust's ownership-and-borrowing model: compile-time invariants on which agent holds the right to read or write a value, with explicit move and borrow semantics.

**Bears on** **TODO 3 on [t1-activity-access-rights](1-framework/research-activities-workflows#^t1-activity-access-rights)** — candidate formalism for the per-activity read/write rights the TODO calls for. Rust-style ownership specifies which activity *owns* each artefact, which activities may *borrow* it for reading, and how write rights transfer. A cross-reference pointer is placed at the TODO site.

---

### Bearing on revision

#### AGM revision-operation vocabulary ^fleeting-agm-vocabulary

Belief-revision operations as candidate vocabulary: expansion (add without resolving conflict), revision (add while preserving consistency), contraction (remove a commitment), consolidation (restore consistency after contradiction), merge (combine epistemic states).

**Bears on** the revision-vocabulary theme (Tier-3). The `EpistemicTransition` object the source proposes — before-state, operation, after-state, rationale — is *already the ratified position*: transitions are authored edits with provenance per [t1-revision-accountability](1-framework/research-activities-workflows#^t1-revision-accountability). Only the operation vocabulary is a new candidate; the transition architecture is restatement.

---

### Cross-cutting convergences

Two convergences span multiple candidates. Whoever resolves any one member should resolve the cluster together.

- **The reified relation object.** [Role reification](#^fleeting-typed-relation-discipline), [source-qualified named graphs](#^fleeting-named-graphs), [Context as a first-class object](#^fleeting-context-object), and the [linking-phrase object](#^fleeting-relation-formalization) all describe one object — a relation reified to carry phrase, type, context, provenance, status — by different routes.
- **Context-relativity of content.** [Source-qualified named graphs](#^fleeting-named-graphs), [ontology modularity](#^fleeting-ontology-modularity), and [Context as a first-class object](#^fleeting-context-object) all reach, by different routes, the position that content is asserted relative to a context rather than absolutely.

#### Context as a first-class object ^fleeting-context-object

A `Context` bundles a domain, its assumptions, its active definitions, and its standards; every assertion is stated relative to a context. This is the most explicit form of the context-relativity convergence above.

A **Marr-style explanation level** is one such context. A claim may hold at the computational level and a different, apparently conflicting claim hold at the algorithmic level — an invariant decision rule realised through equivariant intermediate representations, as [a claim whose truth depends on the level of explanation](_worked-examples.md#^example-a-claim-whose-truth-depends-on-the-level-of-explanation) shows. Folded in here from a former object-scope candidate: an explanation level is a *context index on a claim*, not an object-decomposition concern. Its operative effect is on **validation**: a contradiction-detection validator must read two claims' explanation-level indices before firing, so that level-relative claims at different Marr levels are not reported as a contradiction. An `implements` relation between levels records how a lower-level claim realises a higher-level one. This bears on the validation-views theme (the contradiction check) and [t2-layer-feedback](2-architecture/layering#^t2-layer-feedback); it is distinct from the five-level *justification* model at [t1-recoverable-reasoning](1-framework/reasoning-integrity#^t1-justification-levels), which stratifies a move's justification, not the claim's content.

**Bears on** [t2-layer-feedback](2-architecture/layering#^t2-layer-feedback), the relations-graph theme, the object-kinds theme, and the validation-views theme (the explanation-level contradiction-suppression check).

#### Ontology modularity vs. global canonical terminology ^fleeting-ontology-modularity

Per-project, per-paper, per-domain ontology modules, each carrying its own axioms, imports, profile, and context. The motivating fact: different projects use incompatible concept systems — "representation" carries different definitions in neuroscience, deep-learning theory, and philosophy of mind — and a single global ontology forces premature reconciliation.

**Bears on** the Tier-3 ontology theme. **Carries a real tension** with the ratified [t1-canonical-terminology](1-framework/modular-content-organization#^t1-canonical-terminology): if terminology is module-scoped, canonicity holds *within a module*, not across the corpus. A `[!missing]` tension callout is placed at that criterion. Resolution must state whether canonicity is global or module-local and how cross-module aliasing is linked.

---

### External citations the framework owes ^fleeting-citations-owed

Established frameworks that are external precedents for ratified criteria. These are citations the criteria files should carry, not new candidates. When a criterion file is next edited on independent grounds, the citation can be integrated as backing:

- **IBIS** (issue / position / argument inquiry graph) and **QOC** (question / option / criteria) — precedents for [served goal](1-framework/reasoning-integrity#^t1-served-goal) (analytical decomposition into a question network).
- **Toulmin model** (claim / grounds / warrant / backing / qualifier / rebuttal) — precedent for [t1-recoverable-reasoning](1-framework/reasoning-integrity#^t1-justification-levels) (the five-level justification structure). File 2 of the source-cleanup already owes a Toulmin citation; the cleanup handoff records it as a flagged item.
- **W3C PROV** (entity / activity / agent provenance) — precedent for [t1-revision-accountability](1-framework/research-activities-workflows#^t1-revision-accountability) and [t1-activity-coverage](1-framework/expressive-depth#^t1-activity-coverage).
- **Knowledge Building theory** and **semantic wikis** (ideas as improvable objects; prose plus typed annotation; gradual formalization) — precedents for [t1-partial-formalization](1-framework/expressive-depth#^t1-partial-formalization) and [t1-rich-prose-expressivity](1-framework/expressive-depth#^t1-rich-prose-expressivity).
- **Frame semantics, typed feature structures, Abstract Meaning Representation, semantic-annotation systems** — precedents for the statement-normalization machinery at [t3-definition-normal-form](3-aspect-specific/ontology#^t3-definition-normal-form).

---

## Principled rejections ^fleeting-rejections

Proposals declined during triage, each recorded with the principle that excludes it. Future re-imports of the same idea should consult this log first. A rejection here is by architectural principle, not by chronology: the proposal is excluded because a ratified commitment forecloses it, not because it arrived late.

| Rejected proposal | Source | Excluding principle |
| --- | --- | --- |
| Smalltalk message passing as a runtime computation model | language assessment | [t1-no-runtime-inference](1-framework/framework-foundations#^t1-no-runtime-inference) — the framework records authored content; it does not evaluate messages at runtime. The uniform-protocol idea is kept separately ([uniform navigation protocol](#^fleeting-uniform-protocol)); only the runtime-evaluation framing is rejected. |
| Self / JavaScript prototype-based OOP | language assessment | [t2-layering-source-of-truth](2-architecture/layering) — removing the class layer collapses the schema/meta vs. canonical-instance split. |
| CLOS Metaobject Protocol — runtime-modifiable object system | language assessment, DL review | [t1-no-runtime-inference](1-framework/framework-foundations#^t1-no-runtime-inference) and [functional separation of concerns](1-framework/framework-foundations#^t1-functional-separation) — the meta-schema is fixed; defeasibility manifests through author edits, not runtime customisation of inheritance, slot access, or dispatch. |
| Prolog backward chaining as an inference layer | paradigm survey | [t1-no-runtime-inference](1-framework/framework-foundations#^t1-no-runtime-inference) — Prolog's strength is runtime derivation of new facts. The framework's query layer is retrieval and navigation only, per [t1-relational-queryability](1-framework/modular-content-organization#^t1-relational-queryability). The relation names Prolog would query are already authored edges per [t2-typed-relation-vocabulary](2-architecture/relations-graph#^t2-typed-relation-vocabulary). |
| Argumentation acceptance-semantics computation (grounded / preferred / stable / admissible) | paradigm survey | [t1-no-runtime-inference](1-framework/framework-foundations#^t1-no-runtime-inference) — computing acceptance status requires runtime evaluation of the argument graph. The authored attack/support/defeat edges are kept ([argumentation-graph semantics](#^fleeting-argumentation-graph)); only the semantic computation is rejected. |
| DL automatic classification — a reasoner infers an object's kind from its properties | DL review | [t1-no-runtime-inference](1-framework/framework-foundations#^t1-no-runtime-inference) — intensional class definitions evaluated by a runtime reasoner. The framework's kind tags are authored, not inferred. The kind taxonomy is in scope for the deferred [object taxonomy](../TODO) as *authored* kinds. |
| DL defined classes as cognitive operators — reasoner-materialised dynamic categories | DL review | [t1-no-runtime-inference](1-framework/framework-foundations#^t1-no-runtime-inference) — the DL mechanism materialises class membership at runtime. The underlying use case (derived conceptual lenses such as FragileTheorem, UnresolvedObjection) routes instead to derived view specifications computed by the build, per [t1-relational-queryability](1-framework/modular-content-organization#^t1-relational-queryability) and the validation-views theme. |
| OWL profiles as expressivity stratification | DL review | Downstream of the rejected runtime reasoner. With no reasoner, there is no expressivity/performance tradeoff to stratify. Not applicable. |
| DL reasoner as a service — HermiT / ELK / Pellet backends | DL review | [t1-no-runtime-inference](1-framework/framework-foundations#^t1-no-runtime-inference) — the most explicit runtime-reasoner proposal. Every task (consistency, satisfiability, subsumption, classification, instance retrieval, entailment) is runtime inference. |
| DL justification-based explanations — minimal axiom sets entailing a conclusion | DL review | [t1-no-runtime-inference](1-framework/framework-foundations#^t1-no-runtime-inference) — DL justifications explain reasoner-inferred facts. The framework's explanation of why reasoning advances is *authored*, via the five-level model at [t1-recoverable-reasoning](1-framework/reasoning-integrity#^t1-justification-levels) and warrant attachment. The need is already met by ratified machinery. |
| DL-inference half of the DL-vs-SHACL split | DL review | [t1-no-runtime-inference](1-framework/framework-foundations#^t1-no-runtime-inference) — the inference questions (what follows, is this satisfiable, which individuals belong to a class) require a reasoner. The SHACL half — closed-world structural validation — is *not* rejected: it restates the ratified author-time validation model at [t1-write-side-automation](1-framework/cost-ergonomics#^t1-write-side-automation) and the validation-views theme. |
| DL controlled semantic extension — reasoner-materialised compositional complex classes | DL review | [t1-no-runtime-inference](1-framework/framework-foundations#^t1-no-runtime-inference) for the DL mechanism. The failure mode the section names — naive OOP subclass explosion — is *already guarded against* by the OOP-exclusion in [t2-subtype-discipline](2-architecture/object-kinds#^t2-subtype-discipline) (tagged unions, not subclass trees) and [object-kind set smallness](2-architecture/object-kinds#^t2-ontology-small). |
| DL TBox/ABox/RBox separation as a new layer | DL review | Restates ratified state — the TBox/ABox split is the schema/meta vs. instance distinction at [t2-layering-source-of-truth](2-architecture/layering); RBox role axioms map onto the relation-vocabulary theme. Nothing new to file. |
| DL-inspired reasoner-based framework components — OntologyManager, ReasonerService, ExplanationService | DL review | Implementation-level component sketch built entirely around the rejected runtime reasoner. Wrong architectural level. |
| Ranked DL borrowings summary table | DL review | Summary restatement; most top-ranked items are the rejected runtime-reasoner services. Filing it would duplicate substance and import the runtime assumption as if ratified — forbidden by the no-reformulation rule. |
| Five-layer content taxonomy (conceptual / argumentative / mathematical / epistemic / cognitive) as a layering architecture | DL review | [t2-layering-source-of-truth](2-architecture/layering) — the framework's layering is settled and cuts by source-of-truth role, not by content domain. The expert's cut is a content taxonomy; as such it overlaps the deferred [object taxonomy](../TODO) and is not a layering alternative. |
| Categorical / functional transformation pipelines as a new architectural commitment | paradigm survey | Redundant with the staged operation-primitiveness candidates, not with ratified state — [t2-operation-primitiveness](2-architecture/operations-and-modes#^t2-operation-primitiveness) is an *open* question, so nothing is "already committed" there. The pipeline's typed inputs/outputs, assumptions, failure modes, and provenance duplicate what the operation-schema candidates in that group already propose; the `>>` pipeline syntax is implementation sugar. Rejected as redundant with staged candidates, not by ratified principle. |
| Description Logics as the ontological backbone | DL review | Restates the deferred schema-validation-language state (main handoff "not in scope" section). Not a new commitment; compatible with the deferral but adds nothing to file. |
| Four-layer object/relation/query/view database split | DL review | Restates ratified state — canonical store, [t2-relation-storage-locus](2-architecture/relations-graph#^t2-relation-storage-locus), [t1-relational-queryability](1-framework/modular-content-organization#^t1-relational-queryability), and the rendering-views theme already implement this split. |
| Rust frozen-dataclass / revision-produces-new-object discipline as a new proposal | statement-normalization review | Restates ratified state — [t1-revision-accountability](1-framework/research-activities-workflows#^t1-revision-accountability) and [no version history](1-framework/framework-foundations#^t1-no-version-history) already commit to revision as an authored edit creating a new state. The Rust ownership formalism is kept separately as [ownership and borrowing](#^fleeting-ownership-borrowing). |
| Hybrid-architecture summary table, concrete code sketch, priority ranking | paradigm survey | Summary and implementation-level restatements of content filed under the individual candidates. Filing them would duplicate substance — forbidden by the no-reformulation rule. Specific field proposals within the code sketch are captured in [policy and criterion fields](#^fleeting-policy-fields). |
| Scholarly-discourse ontologies (SWAN, SALT, CiTO, DoCO, DEO) as a *document-annotation* architecture | inquiry review, DL review | What is rejected is narrower than "exposition is derived": it is the use of these ontologies to *annotate finished documents* — a derived-artifact concern deferred per [t1-activity-access-rights](1-framework/research-activities-workflows#^t1-activity-access-rights). The principle does **not** exclude canonical content whose *referent* is a source: [source interpretation](_worked-examples.md#^example-source-sensitive-claim-with-interpretive-uncertainty) and [tradition-level critique](_worked-examples.md#^example-critique-of-a-hidden-assumption-in-a-literature-tradition) show source-facing content authored on the canonical layer and in scope, kept at [content about sources](#^fleeting-source-facing-content). Citation-intent typing is likewise kept ([citation-intent vocabulary](#^fleeting-citation-intent)). Only the document-segmentation / discourse-annotation use of these vocabularies is out of scope. |
| RO-Crate / Research Objects packaging | inquiry review | Serialization and interchange concern, downstream of the architecture. The main handoff defers tooling and serialization formats. Recorded as out of architectural scope. |

---

## Triage log ^fleeting-triage-log

Provenance of the candidates above, one line per review. The log preserves the audit trail; the candidates themselves are organised by bearing decision, not by review.

- **Language-paradigm assessment** → candidates: [Python OOP](#^fleeting-python-oop), [type classes / traits](#^fleeting-type-classes), [multiple dispatch](#^fleeting-multiple-dispatch), [term rewriting](#^fleeting-term-rewriting), [ownership and borrowing](#^fleeting-ownership-borrowing). Rejections: Smalltalk message passing, prototype OOP, CLOS Metaobject Protocol.
- **Exhaustive paradigm survey** → candidates: [policy and criterion fields](#^fleeting-policy-fields), [uniform navigation protocol](#^fleeting-uniform-protocol), [propositional ADTs](#^fleeting-propositional-adt), [proof-assistant model](#^fleeting-proof-model), [argumentation-graph semantics](#^fleeting-argumentation-graph), [named graphs](#^fleeting-named-graphs), [AGM vocabulary](#^fleeting-agm-vocabulary). Rejections: Prolog backward chaining, acceptance-semantics computation, categorical pipelines, the hybrid-architecture summary.
- **Description-Logic review** → candidates: [typed-relation discipline](#^fleeting-typed-relation-discipline), [context-local disjointness](#^fleeting-disjointness-validation), [four-way proof-status](#^fleeting-proof-status), [ontology modularity](#^fleeting-ontology-modularity), [concept metamodeling](#^fleeting-concept-metamodeling). Rejections: DL automatic classification, defined-class materialisation, OWL profiles, reasoner-as-service, justification computation, the DL-inference half of the DL/SHACL split, complex-class materialisation, TBox/ABox-as-layer, reasoner components, the ranked-borrowings table, the five-layer content taxonomy, DL-as-backbone, the four-layer database split.
- **Semi-formal inquiry-frameworks review** → candidates: [idea-improvement move vocabulary](#^fleeting-move-vocabulary), [progressive relation formalization](#^fleeting-relation-formalization), [candidate kind-set](#^fleeting-kind-set), [citation-intent vocabulary](#^fleeting-citation-intent), [Context as a first-class object](#^fleeting-context-object), [QOC content sub-structure](#^fleeting-qoc-substructure); citations-owed list. Filed directly to the arguments-reasoning theme: `^t3-reasoning-schemes`, `^t3-attack-target`. Rejections: scholarly-discourse ontologies as an architecture, RO-Crate packaging.
- **Linking-phrase and scholarly-ontology detail** → enriched [progressive relation formalization](#^fleeting-relation-formalization) with the normalization ladder, the linking-phrase object, and the family taxonomy. Scholarly-discourse ontologies recorded as out of architectural scope.
- **Statement-normalization review** (worked example) → the [genus-differentia definition](_worked-examples.md#^example-genus-differentia); definition-structure refinements folded into `^t3-definition-normal-form`; the undischarged-commitment cluster filed as `^t3-undischarged-commitments`.
- **Worked-example suite** (40 adversarial examples in [worked-examples](_worked-examples)) → resolved in eight batches and propagated, then revised across three adversarial-audit passes. Current state of the candidates the suite produced: [non-assertive statement categories](#^fleeting-non-assertive-statements), [legitimate mutual constraint](#^fleeting-mutual-constraint) (co-definition + co-determination), [statement modality](#^fleeting-statement-modality), [granularity-relative object identity](#^fleeting-object-scope), [meta-conceptual content](#^fleeting-metalinguistic-content), and [content about sources](#^fleeting-source-facing-content) (tradition-level residue in scope; source-interpretation deferred). Enrichments: [the move vocabulary](#^fleeting-move-vocabulary), [term rewriting](#^fleeting-term-rewriting) (explanatory non-neutrality), [the candidate kind-set](#^fleeting-kind-set) (`Example` probe role), [the four-way detection-status distinction](#^fleeting-proof-status), `^t3-definition-normal-form` (negative-definition template; the candidate-set + resolution-policy fields, the re-cut of the former ambiguity-status enum), the reified-relation convergence at [fleeting-ideas](#^fleeting-edge-scope) (absorbing the former edge-scope indices), [t3-attack-target](3-aspect-specific/arguments-reasoning#^t3-attack-target) (question-framing attack, method-result circularity, critique-driven re-typing). The first audit fixed phantom anchors and relabelled coverage-inflated verdicts. The deepest audit pass (rationale depth) re-cut five candidates: the ambiguity-status enum into candidate-set + resolution-policy fields plus a separate defect claim; `^fleeting-metalinguistic-content` dissolved (usage-norm → ontology lexical level; hazard-flag → validation-views linter rule [t2-interpretive-hazard-lint](2-architecture/validation-views#^t2-interpretive-hazard-lint); meta-conceptual + metaphor kept); edge-scope folded into the reified-relation convergence; object-scope`s explanation-level folded into [Context as a first-class object](#^fleeting-context-object); the unifying re-type move dissolved into three existing homes; source-facing-content reduced to a deferral pointer plus the tradition-level residue. `[!missing]` callouts stand on [t1-canonical-terminology](1-framework/modular-content-organization#^t1-canonical-terminology), [functional separation of concerns](1-framework/framework-foundations#^t1-functional-separation), [t1-typed-object-decomposition](1-framework/framework-foundations#^t1-typed-object-decomposition), and [valid licensing](1-framework/reasoning-integrity#^t1-valid-licensing).
- **Standalone triage decisions.** Concept-type taxonomy (system / subtype / property / process) → [concept-type taxonomy](3-aspect-specific/ontology#^t3-concept-type-taxonomy). Question-as-epistemic-gap hypothesis → split between the deepening note at [t2-question-vs-goal](2-architecture/object-kinds#^t2-question-vs-goal) and the [epistemic-gap subtypes](3-aspect-specific/ontology#^t3-epistemic-gap-subtypes) open question.
