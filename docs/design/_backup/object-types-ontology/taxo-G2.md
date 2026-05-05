# Ontological Design for an Epistemic Object Framework - G2

# Eight-type ontology ontology

A strictly superior decomposition should be **smaller where separations are weak** and **larger where a genuine missing structure exists**. This ontology improves the proposal in two ways:

- **more minimal** because it collapses Problem, Distinction, and Interpretation
- **more expressive** because it adds Method, which fills a genuine structural gap

The principal architectural lesson is the following: the ontology should privilege **content-bearing reusable structures** over discourse labels, but it must not confuse **search-guiding practical rationality** with mere annotation.

| Type                     | Role                                                                                                                                                                                                                                                      |
| ------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **CONCEPT**              | semantic/intensional object                                                                                                                                                                                                                               |
| **CLAIM**                | truth-apt content, including descriptive, comparative, normative, definitional, interpretive, and rationale claims                                                                                                                                        |
| **ARGUMENT**             | reified inferential support/attack structure                                                                                                                                                                                                              |
| **QUESTION**             | erotetic gap, including constructive and procedural subkinds                                                                                                                                                                                              |
| **MECHANISM**            | explanatory productive organization model                                                                                                                                                                                                                 |
| **ANALOGY**              | structured cross-domain mapping                                                                                                                                                                                                                           |
| **EXAMPLE**              | case object or case description deployed relative to targets                                                                                                                                                                                              |
| **METHOD**               | reusable procedural or strategic schema for constructing, testing, comparing, or solving                                                                                                                                                                  |
| **RATIONALE** (optional) | epistemic justification for asking, decomposing, prioritizing, idealizing, or pursuing<br>(only if the framework aims not only to store knowledge but also to store **research navigation and strategy justification** - otherwise a Claim kind suffices) |

# Necessity

A strict irreducibility audit yields the following:

|Type|Verdict|Decision|
|---|--:|---|
|Concept|Irreducible|Keep|
|Claim|Irreducible|Keep|
|Argument|Irreducible|Keep|
|Question|Irreducible|Keep|
|Problem|Reducible to Question + fields|Collapse|
|Mechanism|Irreducible|Keep|
|Analogy|Irreducible|Keep|
|Example|Irreducible|Keep|
|Distinction|Reducible to structured comparative Claim|Collapse|
|Interpretation|Reducible in current form|Collapse or narrow radically|

So the ten-type proposal fails strict minimality. A more defensible core has **seven** stable types.

## Concept

**Verdict:** irreducible

A concept is not truth-apt and does not merely name a string label. Its function is to determine **what counts as an instance**, what falls inside or outside the extension, what inferential commitments attach to its use, and under what scope conditions the term is licensed. That content is not recoverable from Claim alone without conflation between:

- asserting that something is the case
- fixing the meaning of terms used in assertions

A definitional claim such as “A group is an associative magma with identity and inverses” is truth-apt as a metalinguistic statement, but the **conceptual object** “group” is the semantic anchor reused by many claims, examples, distinctions, and questions. If Concept is collapsed into Claim, either each concept becomes a bundle of definitional claims without a unifying intensional locus, or one claim is arbitrarily privileged as the “real” concept. Both distort the role of concepts in reasoning.

## Claim

**Verdict:** irreducible

Truth-apt assertoric content requires a generic home independent of proof status, source, certainty, or modality. The collapse of theorem, conjecture, axiom, empirical regularity, and hypothesis into Claim is sound at the type level because these differ primarily by **epistemic status and justification regime**, not by basic ontological shape.

The only caveat is that not all claims are propositionally homogeneous. Normative claims, causal claims, classificatory claims, existential claims, and definitional claims support different downstream operations. That does not require subtype proliferation, but it does require a well-typed `claim_kind` or `logical_form` attribute.

## Argument

**Verdict:** irreducible

An argument is not equivalent to a set of claims plus edges. The crucial irreducible content is the **warranted inferential act**:

- which claims play premise roles
- which inferential rule or pattern licenses the move
- whether the move is deductive, abductive, analogical, causal, dialectical, and so on
- what hidden assumptions or defeaters govern its force

If encoded only as dependency edges among claims, the system loses the distinction between:

- semantic dependence
- evidential support
- inferential derivation
- rhetorical adjacency

Moreover, one conclusion may admit many arguments with different warrants. That plurality requires argument objects as first-class reifiable entities.

## Question

**Verdict:** irreducible

A question is not reducible to a claim with unknown truth value. The semantics of inquiry is different from the semantics of assertion. Questions carry:

- answerhood conditions
- presuppositions
- decomposition structure
- admissible forms of completion
- control of search space

A why-question, what-is question, comparison question, and procedure question do not differ merely by content labels; they induce different reasoning obligations and object-introduction permissions.

## Problem

**Verdict:** not strictly irreducible. **Do not keep as a separate core type.**

The proposed distinction between Question and Problem is real at the pragmatic level, but weak at the ontological level. A problem, as described, is a **question with additional structure**:

- target artifact or target state
- success criteria
- constraints
- admissible operations
- known unknown boundary

This is substantial, but it does not justify a separate type if the framework already has Question plus explicit answer schemas and solution criteria. “Construct an example of a non-normal subgroup of index 2” and “Find parameters satisfying constraints C” are not ontologically alien to erotetic objects; they are **directive or constructive question subkinds**.

The decisive test is whether a Problem can appear in all roles a Question can: be decomposed, carry presuppositions, generate subquestions, receive candidate answers, be closed by satisfaction conditions. The answer is yes. The extra structure is field-level, not type-level.

**Collapse:** `Problem -> Question(problem_mode=True, success_criteria, constraints, target_artifact_kind)`

## Mechanism

**Verdict:** irreducible, with an important qualification

The defense offered is correct in substance: a mechanism is not merely an argument, because its primary content is **organized productive structure**, not inferential force. A mechanistic explanation contains:

- parts or entities
- activities/interactions
- organization
- temporal or functional ordering
- mapping from organization to explanandum

An argument may support the claim that such a mechanism exists or is adequate, but the mechanism itself is a model-like structured object. It can be compared, refined, simulated, and transferred independently of any one argument.

However, the current description oscillates between **mechanism as world structure** and **mechanism as explanatory representation**. That boundary must be fixed. The correct choice for this ontology is the second: a Mechanism object should represent a **structured explanatory model** of productive organization.

## Analogy

**Verdict:** irreducible

The proposed justification is strong. An analogy is not only an argument pattern. The mapping itself has reusable content:

- source structure
- target structure
- correspondence relation
- transferable predicates or relations
- scope limits
- known disanalogies

The same analogy may support many arguments, motivate conjectures, guide examples, or expose conceptual structure. If analogy is collapsed into Argument, that reusable mapping becomes buried inside warrants or prose fields.

## Example

**Verdict:** irreducible, but narrowly so.

An example is a concrete or at least more determinate case used relative to some target object. It is not merely a claim because its epistemic role depends on **exhibiting** an instance, pattern, failure, or boundary. The same mathematical structure may function as:

- an instance of a concept
- a witness for an existential claim
- a counterexample to a universal claim
- an illustration of a subtle distinction
- a boundary case probing a definition

This object is reusable and queryable independently of the surrounding argument. Systems for theoretical work benefit from retrieving all examples of a concept, all counterexamples to a claim, or all edge cases linked to a distinction.

The narrowness matters because some examples are fully extensional objects, while others are partially narrated constructions. The schema must therefore support both **object-level instance description** and **role-relative deployment**.

## Distinction

**Verdict:** not strictly irreducible. **Do not keep as a separate core type.**

The defense is insufficient. A distinction does carry content, but that content is recoverable from a structured relation among concepts or claims plus a criterion field. In fact, the essential structure of a distinction is relational:

- two or more targets
- contrast dimension
- point of non-equivalence
- common source of conflation
- consequences of confusion

This does not require a full object type unless distinctions themselves become higher-order objects that must accumulate history, objections, examples, and refinements. Even then, reification can be achieved as a **typed comparative analysis claim** or a specialized relational object. But the proposal has already committed to not making relations first-class object types. Under that commitment, the cleanest move is not “Distinction as object,” but either:

1. allow **reified typed relations** in a limited family, or
2. encode distinction as a **Claim/Analysis object** with structured fields

Because the framework already includes Claim, the second option is sufficient. For instance:

- claim_kind = `distinction`
- targets = [concept_a, concept_b]
- contrast_basis = ...
- non-interchangeability = ...
- conflation_conditions = ...

Nothing structurally essential is lost. The alleged irreducibility over “two concept nodes plus an edge” is true, but that is a weak target. The real comparison is not against an untyped edge; it is against **Claim with structured comparative schema**.

**Collapse:** `Distinction -> Claim(claim_kind="distinction" or "comparative-analysis", structured_targets, contrast_basis, conflation_conditions)`

## Interpretation

**Verdict:** not strictly irreducible in the proposed form. Given the ontology as proposed, the cleaner choice is collapse.

The current definition combines two different things:

1. **semantic assignment** from a formal structure to a domain
2. **representational application** of a formalism within a model or theory

Both can be encoded without a separate type if Claim and Concept are sufficiently typed. “Under interpretation I, symbol R denotes physical resistance” is a claim about a mapping. A model-theoretic interpretation is a structured assignment object, but then the right abstraction is not “Interpretation” in the broad philosophical sense; it is **semantic map / model assignment**.

The decisive issue is whether Interpretation is truth-apt. In practice, most interpretations in theoretical work are indeed evaluable:

- apt or inapt
- faithful or distorting
- conservative or excessive
- admissible under explicit criteria or not

If the object is evaluable and supports constraints on symbol-domain correspondences, then it is not outside Claim. If the objection is that “assignment is not assertion,” the response is that the ontology already allows non-primitive structured fields inside a claim object.

The only case where Interpretation deserves a separate type is if semantic mappings are pervasive, reusable, and independently transformed by operations such as restriction, extension, composition, or transport. In many theoretical frameworks that is true. But then “Interpretation” should be defined much more narrowly as a **mapping object** with domain, codomain, assignment rules, and admissibility conditions. The current broad formulation is too semantically diffuse.

**Collapse:** 

- Option 1: `Interpretation -> Claim(claim_kind="interpretive-assignment", mapping_schema=...)`
- Option 2: Of mappings are globally central, replace it with a narrower type `SEMANTIC_MAP`

# Sufficiency

The set is **not fully sufficient** as stated. The most serious missing piece is **Method/Procedure**. A secondary but still important deficiency is the under-representation of **epistemic rationale / heuristic guidance**. Principles and typologies can likely be absorbed by a richer Claim schema.

## Gap 1 — Method / Procedure / Strategy

**Needed type:** `METHOD` or `PROCEDURE`

The proposal includes `answer_type = procedure` on Question, but that does not solve the representational problem. A method is not merely the answer to a question. It is a reusable structured object containing:

- ordered or partially ordered steps
- entry conditions
- stopping conditions
- admissible transformations
- expected outputs
- failure modes
- sometimes branching logic

This matters in research frameworks because local reasoning often contains procedural knowledge: how to test a conjecture class, how to normalize a definition, how to compare mechanisms, how to construct counterexamples. Storing such content as prose in claims or arguments makes it non-queryable and non-composable.

## Gap 2 — Motivation / Heuristic / Rationale-for-pursuit

Treating motivation as annotation is too weak. Not every motivational object is fluff. In serious inquiry, there are epistemically operative objects such as:

- why a question matters
- why a decomposition is licensed
- why a proof strategy is promising
- why one model idealization is acceptable
- what obstacle makes a problem nontrivial

These are not always claims about the domain. They often function as **search-guiding rationales**. If buried in annotations, the framework cannot track strategy-level dependencies.

The crucial distinction is between mere editorial motivation and **epistemic rationale**. The latter has enough structure to warrant representation. It may be implemented as a typed Claim if truth-apt, but often it is a mixed practical-epistemic object.

A separate core type is not mandatory if Claim is widened with `claim_kind = rationale / significance / heuristic-guidance`. But under the current proposal, where Motivation is denied object status altogether, sufficiency fails.

**Minimal repair:** allow a structured `RATIONALE` subtype under Claim, or introduce `RATIONALE` as a separate type if practical guidance is central.

## Gap 3 — Principle / Criterion / Rule

The ontology has Concept and Claim, but it lacks a stable home for objects such as:

- parsimony criterion
- adequacy condition 
- explanatory norm
- admissibility rule
- interpretation constraint
- model selection principle

These are not ordinary descriptive claims in use. They are **normative evaluative operators** that govern acceptance, comparison, and design. They can be encoded as claims, but only if Claim is explicitly allowed to carry a deontic or normative mode and downstream operations know how to use it.

This is not necessarily a new type, but it is a sufficiency hazard unless the Claim schema explicitly supports **criteria/principles as first-class claim kinds**.

## Gap 4 — Taxonomy / Partition / Typology

The framework includes Concept and Distinction, but not the structured operation of partitioning a space into exhaustive or non-exhaustive cases. Theoretical reasoning often depends on:

- exhaustive case splits
- typologies
- mutually exclusive partitions
- layered taxonomies

These could be encoded as a network of concepts and claims, but that loses the unified structure “this is a partition of domain D under criterion C.” Since the proposal values reusable structural objects, the absence is noticeable.

This gap is weaker than Method. It can plausibly be repaired by a structured Claim kind rather than a new type.

---
# Boundaries

The most unstable boundaries are:

- Question / Problem
- Distinction / Claim / Concept
- Interpretation / Claim / Analogy / Concept

Those instabilities are not minor implementation issues; they indicate over-fragmentation around weakly separable functions.

## Concept vs Claim

The boundary is unstable around definitions, identity conditions, and classificatory statements.

Examples:

- “A prime number is an integer greater than 1 with exactly two positive divisors”
- “Memory consolidation is the post-encoding stabilization of trace structure”
- “Attention is not selection but gain modulation”

These can be encoded as:

- Concept content
- definitional Claim
- sometimes Distinction

A principled criterion is needed to avoid ontological drift:

- **Concept** stores the semantic object being delimited
- **Claim** stores any assertive sentence about the concept, including definitional formulations
- one or more claims may serve as definitional anchors for a concept, but are not identical to it

## Question vs Problem

This boundary is explicitly unstable, which is one reason Problem should collapse. Any constructive problem can be phrased erotetically, and any question with constraints begins to resemble a problem. No sharp ontological decision criterion exists here beyond pragmatic presentation.

## Argument vs Mechanism

A mechanism often appears embedded in an explanatory argument. For example:

- premises: components behave in ways A, B, C
- conclusion: the phenomenon arises by mechanism M

But M may also be the central content. The boundary criterion should be:

- **Argument** = inferential support structure
- **Mechanism** = represented productive organization

Without that distinction, mechanism narratives will be inconsistently encoded as either arguments or mechanism objects.

## Analogy vs Argument

Analogical reasoning creates strong instability:

- the mapping itself belongs to Analogy
- the inferential use of that mapping belongs to Argument

Many texts blur both. The criterion must be:

- if the content primarily answers “what corresponds to what, under what structural preservation and breakdown conditions?” then Analogy
- if it answers “how does this support conclusion C from premises P?” then Argument

## Example vs Claim

A witness example can be represented either as:

- a concrete object record
- an existential claim
- a miniature argument

For purity, Example should be reserved for **case objects or case descriptions** deployed relative to another target. The supporting existential claim remains separate.

## Distinction vs Concept

This instability is another reason to collapse Distinction. Many distinctions are simply sharpened concept boundaries, while others are comparative claims about non-equivalence. Without a sharp criterion, the framework will encode similar content inconsistently.

## Interpretation vs Concept / Claim / Analogy

Interpretation sits on a three-way fault line:

- as semantic grounding, it resembles Concept
- as mapping assertion, it resembles Claim
- as cross-domain correspondence, it resembles Analogy

This instability is not accidental; it indicates that the type is insufficiently purified. In its present form it should not survive as a core primitive.

---
# Collapse decisions

## Theorem / Axiom / Conjecture into Claim

**Verdict:** sound and largely lossless

These differ by epistemic status, justificatory position, and acceptance mode, not by deep structural form. A theorem, conjecture, and axiom are all truth-apt propositions. The critical condition is that the Claim schema must include at least:

- status
- modality
- justification status
- proof/derivation links
- provenance

If those fields exist, no separate types are needed.

## Counterexample into Example

**Verdict:** conditionally sound

A counterexample is indeed a role of an example relative to a claim. Structurally, the important content is:

- target claim refuted
- mode of refutation
- whether it defeats universality, implication, equivalence, necessity, sufficiency, and so on

If Example supports typed roles and target links, no separate Counterexample type is needed.

However, a mere `role = counterexample` field is too thin. The refutational logic must be explicit. Otherwise the framework cannot distinguish:

- example inconsistent with a universal claim
- example exposing non-equivalence
- example showing criterion insufficiency
- example defeating a proof step rather than the conclusion

So the collapse is sound only with richer relational structure.

## Objection into Claim + dependency edge

**Verdict:** mostly sound

An objection is a claim playing a dialectical role relative to an argument, claim, or mechanism. That role can be modeled by:

- claim content
- target object
- objection relation type
- attack locus: premise, warrant, inference pattern, scope condition, evidential basis, ambiguity, counterexample, underdetermination

No separate object type is necessary. What matters is that objections be typed by **attack mode**. Otherwise the framework loses the reason why the objection matters.

## Motivation into annotation field

**Verdict:** unsound

This is the weakest collapse decision. Purely editorial motivation can indeed remain annotation, but many motivational elements are structurally important:

- why a question is worth asking
- why a decomposition is necessary
- why an assumption is introduced
- why one formalization is preferable
- why an analogy is epistemically promising

Such items guide inquiry and constrain object introduction. If hidden in annotations, they cannot participate in the explicit epistemic architecture the framework claims to enforce.

A better treatment is:

- either represent serious motivations as `Claim(kind="rationale" | "significance" | "heuristic")`
- or add a separate `RATIONALE` type if search-guiding discourse is central

## Definition into Claim serving as Concept.definition

**Verdict:** broadly sound, but only with a bidirectional discipline

A definition sentence is truth-apt as a metalinguistic or stipulative act, so Claim is an acceptable host. But a concept cannot be reduced to its definition string because concepts often have:

- multiple equivalent definitions
- intensional decompositions
- historical variants
- canonical vs operational criteria
- scope notes and exclusions

So the correct arrangement is:

- Concept as primary semantic object
- one or more Claims linked as definitional formulations
- one designated canonical definition if needed

This collapse is sound only if Concept remains distinct.

