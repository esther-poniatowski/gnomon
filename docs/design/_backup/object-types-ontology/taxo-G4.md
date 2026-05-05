# Ontological Design for an Epistemic Object Framework - G4

The correct axis for a typed reasoning graph is to center the ontology on **epistemic role** rather than on surface linguistic form. Each primitive must capture a major organizational pole of theoretical inquiry.

The principal defect in proposed ontologies is **misfactoring**. Several kinds may be compressed into attributes (e.g. in `CLAIM`) or broad formulations (e.g. in `MODEL`), but they differ too strongly in **epistemic function**, **dependency profile**, and **graph behavior** to remain transparent under that compression. The result is that some central reasoning structures become artificially flattened. The ontology is **not optimally expressive**, because it suppresses a small number of distinctions that materially improve intelligibility.

The main recommendation is therefore **not** to expand indiscriminately, but to refactor around a more explicit separation between:

- **semantic objects**
- **truth-apt commitments**
- **inferential objects**
- **representational structures**
- **procedural schemas**
- **epistemic prompts**
- **framework-level organizing commitments**


# 2. Necessity Analysis of Each Primitive

## CONCEPT

`CONCEPT` is necessary.

A concept is not merely a proposition missing a truth value. It has a different epistemic role. It supplies **semantic circumscription**, **applicability boundaries**, and often the very **space of admissible questions and claims**. In a reasoning graph, concepts are not only content-bearing nodes; they are often **classification anchors**, **contrast loci**, and **dependency sources** for definitions, distinctions, and theoretical reinterpretations.

Elimination into `CLAIM` would damage intelligibility in at least three ways:

- semantic grounding would be forced into truth-apt form

- conceptual revision would become indistinguishable from propositional revision

- boundary work between neighboring concepts would become opaque


This primitive is irreducible under the understandability criterion.

## CLAIM

`CLAIM` is necessary, but currently overburdened.

Truth-aptness is an essential ontological divide. Assertions, hypotheses, conjectures, evaluative commitments, and explanatory theses all participate in evidential support, conflict, revision, and justification in ways that concepts and methods do not.

However, the current `CLAIM` type is **too promiscuous**. It absorbs items whose graph behavior differs markedly:

- theorem

- axiom

- definition

- interpretation

- comparative judgment

- instantiative statement


Logical reducibility does not settle the issue. The question is whether one broad `CLAIM` node preserves structural visibility. In many routine cases it does. In high-level theoretical work, often it does not.

Thus the primitive is necessary, but the current compression policy within it is only partially acceptable.

## ARGUMENT

`ARGUMENT` is necessary.

The central reason is that inferential structure is not recoverable transparently from claims and relations alone unless the graph adopts very rich edge semantics. Even then, the inferential act itself remains diffused. A typed reasoning system needs explicit objects for:

- premise bundles

- warrants

- defeaters

- inference mode

- local strategy


Without `ARGUMENT`, the graph can represent dependency, but not **reason-giving structure**. That is a critical loss.

The primitive is irreducible.

## QUESTION

`QUESTION` is necessary.

This is not merely a missing-answer placeholder. In research reasoning, questions organize inquiry, decompose epistemic gaps, constrain admissible answers, and define relevance. A question has a different directionality from a claim: it opens a search space rather than closes one.

Reduction to a `METHOD` plus unresolved `CLAIM` set would obscure:

- what is unknown

- what would count as resolution

- why certain subclaims are introduced


This primitive is irreducible.

## MODEL

`MODEL` is necessary, but its scope is currently too heterogeneous.

The proposed characterization is broadly correct: a model is a representational structure used to organize, simulate, classify, or idealize a domain rather than directly assert propositions of it.

However, the inclusion of both **mathematical/causal/computational models** and **taxonomic/classificatory structures** under one primitive risks hiding a major internal divide. Some models are primarily **generative or structural surrogates**; some are primarily **organizational partitions**. The graph roles differ.

That said, total elimination of `MODEL` into `CLAIM` plus `CONCEPT` would be disastrous. It would erase the distinction between:

- asserting facts about a system

- constructing a structure through which the system is represented


`MODEL` is therefore necessary, though likely in need of internal factoring or subtype elevation.

## METHOD

`METHOD` is necessary.

A method is not an argument token. It is not even always inferential in the narrow sense. It is a **normative or procedural schema** governing how inquiry, proof search, diagnosis, decomposition, or evaluation is to proceed.

Elimination into `ARGUMENT` would conflate:

- one actual inferential move

- a reusable procedure for generating or validating such moves


Elimination into `FRAME` would be too coarse. Methods are often local and operational; frames are background-structural.

This primitive is irreducible.

---

# Previously Eliminated Types

## Example

Compression into `CLAIM` or `MODEL` is tolerable only if examplehood is represented explicitly as a **role-bearing subtype or relation pattern**. Examples are not trivial instances. They function as **epistemic access devices**, often mediating between concept and claim. Pure attribute compression is acceptable only if the system preserves their pedagogical and justificatory roles.

## Counterexample

Compression into `CLAIM` is damaging unless counterexample status is explicit and first-class in graph behavior. A counterexample is not merely a false-instance claim. It is a **targeted defeater** of a universal, modal, or classificatory commitment. Its role is structurally distinctive. This should at minimum be a stable subtype of `CLAIM` or a dedicated objection-pattern composite.

## Analogy

Compression into warrant type inside `ARGUMENT` is insufficient. Analogy often functions not only as a warrant, but as a **mapping structure** between domains. That mapping has internal articulation. Therefore, analogy should not be a primitive, but it does require more than a bare argument attribute. It should be represented as a structured subtype or auxiliary object linked to `ARGUMENT`.

## Mechanism

Compression into `MODEL` is often acceptable, but only for mature mechanistic accounts. In many contexts, “mechanism” behaves partly as explanatory claim, partly as organized model, partly as answer to a how-question. The compression is acceptable only if explanatory relation structure is rich. Otherwise, mechanistic explanation becomes too opaque.

## Distinction

This should not be a primitive. It is best treated as a structured relation or composite pattern between `CONCEPT`s and sometimes `CLAIM`s. Primitive elevation would over-objectify what is often a relational epistemic act.

## Interpretation

Compression into `CLAIM` is often too weak. Interpretations are truth-apt in some contexts, but they also mediate between model, concept, and evidence. A generic claim label obscures that mediating role. A subtype family under `CLAIM`, or a relation-rich composite, is preferable.

## Theorem

Compression into `CLAIM` is acceptable **only if** theoremhood carries explicit inferential certification and proof linkage. Otherwise the difference between theorem, hypothesis, and speculative claim becomes too flat.

## Axiom

Compression into `CLAIM` is questionable. An axiom is not merely a proposition with a role tag. It has a special dependency direction: it is introduced as a basis within a formal frame. It is closer to a **framework-grounding commitment** than to an ordinary claim. Compression is possible, but only at some cost.

## Conjecture

Compression into `CLAIM` is acceptable. The epistemic role is important, but the structural behavior remains close enough to claimhood.

## Objection

Compression into `ARGUMENT` or `CLAIM` alone is damaging. An objection is a dialectical attack with a target and a mode of defeat. It is best treated as a structured subtype or relation-bearing argument pattern, not a primitive.

## Motivation

Compression into `CLAIM` is poor. Motivation is typically neither descriptive truth-apt content nor method. It often functions as a **rationale for inquiry choice**, model choice, or decomposition choice. Primitive elevation may be too much, but reducing it to claimhood hides strategy. This is a warning sign that a framework-level or rationale-level representational family may be missing.

## Norm

Compression into `METHOD` or `FRAME` is context-dependent. Local operational norms belong with method. Global standards of admissibility and evaluation belong with frame. No separate primitive is needed.

## Taxonomy

Compression into `MODEL` is acceptable if taxonomies are treated as a distinct subtype family. Compression into `CONCEPT` or `CLAIM` would be poor.

---

# Boundaries

## Definition

- Correct assignment: `CLAIM` linked constitutively to `CONCEPT`
- Nearest competing assignment: `CONCEPT`
- Boundary stability: only moderately stable

A definition both **introduces semantic determination** and **asserts a constitutive equivalence or criterion**. The current resolution is workable, but definitional nodes are hybrid enough that ordinary claim treatment can obscure their concept-fixing role.

## Theorem

- Correct assignment: `CLAIM`
- Nearest competing assignment: `ARGUMENT`
- Boundary stability: stable if proof linkage is explicit

The theorem is the proposition proved, not the proof. Stable.

## Proof strategy

- Correct assignment: `METHOD`
- Nearest competing assignment: `ARGUMENT`
- Boundary stability: moderately stable

A specific proof execution is an argument. A reusable strategy is a method. The distinction is sound.

## Causal explanation

- Correct assignment: usually `ARGUMENT` supported by `MODEL`, sometimes explanatory `CLAIM`
- Nearest competing assignment: `MODEL`
- Boundary stability: unstable in current ontology

This is one of the proposal’s weak points. Explanations are not always merely arguments, nor merely models. They often integrate both. The current ontology can encode them, but not always transparently.

## Analogy

- Correct assignment: structured `ARGUMENT` plus mapping structure
- Nearest competing assignment: `MODEL`
- Boundary stability: unstable in current ontology

The instability comes from the lack of an explicit representational mapping object.

## Counterexample

- Correct assignment: `CLAIM` with explicit defeater role, or objection-pattern
- Nearest competing assignment: `ARGUMENT`
- Boundary stability: moderately unstable

The node itself may be a claim, but its graph function is dialectical.

## Taxonomy

- Correct assignment: `MODEL`
- Nearest competing assignment: `CONCEPT`
- Boundary stability: fairly stable

## Research heuristic

- Correct assignment: `METHOD`
- Nearest competing assignment: `FRAME`
- Boundary stability: stable if local, unstable if paradigmatic

## Objection

- Correct assignment: `ARGUMENT`
- Nearest competing assignment: `CLAIM`
- Boundary stability: stable if target relation is explicit

## Paradigm or framework

- Correct assignment: missing meta-level type, best called `FRAME`
- Nearest competing assignment: composite of `MODEL`, `CONCEPT`, `METHOD`, `CLAIM`
- Boundary stability: unstable under current ontology

This is the most important failure.

---

# Sufficiency

The ontology covers much of the declared reasoning space, but not all of it with equal transparency.

**Adequately covered**:

- formal derivation
- question decomposition
- heuristic reasoning
- much of conceptual clarification
- much of comparative analysis
- basic model-based reasoning

**Partially but imperfectly covered**:

- mechanistic explanation
- analogy
- interpretive reasoning
- objection and dialectical evaluation
- framework-level reasoning
- rationale or motivation-sensitive planning

> [!FAIL]
> The central sufficiency problem is that the ontology is better at representing **content units** than **orientation structures**. 
> 

Theoretical research is not only a sequence of claims and arguments. It is also guided by:

- background commitments
- standards of admissibility
- preferred explanatory ideals
- problem-framing lenses
- strategic motivations for certain decompositions

Those are not noise. They are often what makes a reasoning path intelligible. Therefore, full sufficiency is **not yet achieved**.

---

# 6. Assessment of FRAME or Other Missing Meta-Level Types

A missing primitive is indeed present, and `FRAME` is the correct general direction.

However, it should not be defined vaguely as an all-purpose worldview container. It should be defined sharply as:

## FRAME

A structured background configuration that fixes some combination of:

- ontological commitments

- admissible object types

- methodological norms

- evaluative standards

- explanatory ideals

- default distinctions

- privileged questions or problem-formulations


Why primitive status is justified:

- elimination into a bundle of nodes loses the fact that these elements operate as a **coherent conditioning background**

- many arguments, questions, and methods are intelligible only relative to such a background

- framework shifts are central events in philosophy and theoretical science


A frame is not merely a collection. It has a distinctive epistemic role: it **conditions the space of acceptable reasoning moves**.

This primitive is necessary for framework-level reasoning and paradigm comparison.

A second possible candidate would be `RATIONALE` or `MOTIVATION`, but primitive elevation is less clearly justified. Much of that material can be handled by `QUESTION`, `METHOD`, and `FRAME` together.

---

# 7. Alternative Ontologies and Comparative Evaluation

## 7.2 More articulated ontology

`CONCEPT`, `DEFINITION`, `CLAIM`, `THEOREM`, `AXIOM`, `QUESTION`, `ARGUMENT`, `OBJECTION`, `MODEL`, `METHOD`, `FRAME`, `EXAMPLE`

### Assessment

- Understandability: locally strong

- Expressive adequacy: very high

- Boundary purity: mixed

- Operational usefulness: high but risks fragmentation


This ontology is too articulated for a primitive layer. Several distinctions are useful, but better handled as subtypes.

## 7.3 Differently factored ontology

`CONCEPT`, `THESIS`, `QUESTION`, `ARGUMENT`, `REPRESENTATION`, `PROCEDURE`, `FRAME`

Where:

- `THESIS` replaces broad claim

- `REPRESENTATION` covers model, taxonomy, analogy-mapping structures

- `PROCEDURE` covers method and heuristic schema


### Assessment

- Understandability: strong

- Expressive adequacy: strong

- Boundary purity: better than current proposal

- Operational usefulness: strong


This is superior to the current proposal in one respect: it explicitly separates **representational structures** from propositional commitments while giving enough room to framework-level structure. However, replacing `CLAIM` by `THESIS` may be too narrow if atomic truth-apt statements are important in the graph.

---

# 8. Final Recommended Ontology

The best decomposition is not the original six, and not a highly expanded list. The strongest candidate is a **seven-primitive ontology**:

## Primitive layer

1. **CONCEPT**  
Semantic circumscription and applicability structure

2. **CLAIM**  
Truth-apt commitment

3. **QUESTION**  
Structured epistemic gap

4. **ARGUMENT**  
Inferential structure linking reasons to conclusion

5. **MODEL**  
Representational structure organizing a target domain

6. **METHOD**  
Procedural or normative schema for inquiry or inference

7. **FRAME**  
Coherent background configuration conditioning admissible reasoning


## Required subtype families or structured composites

These should not all be primitives, but they must be explicitly supported:

- under `CLAIM`: theorem, conjecture, hypothesis, interpretation, definition, counterexample-instance
- under `ARGUMENT`: proof, objection, explanation, analogical argument
- under `MODEL`: taxonomy, causal model, mathematical model, computational model
- under `METHOD`: proof strategy, research heuristic, evaluation protocol


## Relation families

The ontology will remain insufficient unless these relations are first-class:

- `grounds` / `supports` / `rebuts`
- `defines`
- `instantiates`
- `models`
- `interprets`
- `presupposes`
- `decomposes-into`
- `operates-within-frame`
- `motivates`
- `analogically-maps-to`

This recommended ontology is more expressive than the original while remaining compact.

---

# Remaining Unresolved Risks

- **Hybrid objects remain unavoidable**: Definitions, explanations, interpretations, and mechanistic accounts are genuinely cross-cutting. No ontology will remove all mixed cases. The aim should be **controlled hybridity**, not impossible purity.

- **Overreliance on attributes may reintroduce opacity**: Even with seven primitives, excessive attribute compression can silently collapse important differences. Subtype policy matters almost as much as primitive choice.

- **Relation design is as important as node design**: A node ontology with weak relation semantics will still yield poor structural intelligibility. This proposal’s final success depends heavily on relation families.

- **FRAME can become a junk drawer**: Unless defined narrowly, `FRAME` risks absorbing everything background-like. That would destroy its usefulness. It must be reserved for coherent background configurations that condition admissibility, relevance, and evaluation.

- **Token/type ambiguity must be controlled**: Several tensions arise because token-level reasoning events and type-level reusable structures are mixed. This is especially acute for argument, method, analogy, and model. The implementation must enforce this distinction clearly.
