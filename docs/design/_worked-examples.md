# Worked examples

Concrete expressivity test cases and their resolutions. Each example states a statement the framework must be able to represent, then a brief resolution naming the framework parts that handle it.

Each example is a free-form statements for an expressive inquiry framework. These examples are intentionally adversarial: they stress-test the design, namely the boundary between prose, structured annotation, conceptual modelling, and formalization. They are not meant to be easily normalized into simple definition, support, contrast, or citation relations.

The general lessons each example yields are propagated to the relevant criteria, decisions, and open questions, rather than restated example-by-example in those parts.

> [!INFO] Propagation status
> Examples 1–40 are resolved, and the general lesson each one surfaced is propagated to its destination in [_fleeting-ideas](_fleeting-ideas) or the tier files. Each resolution below names the framework part — already ratified, or now a staged candidate — that covers each difficulty; each **General lesson** line names where that lesson landed. The [triage log](_fleeting-ideas#^fleeting-triage-log) summarises the suite’s propagation; the per-example destinations are the **General lesson** lines here.

---

## 0. Definition by genus and differentia ^example-genus-differentia

**Statement.** "A feedforward network is a network where the flow of information is unidirectional."

**Normalized roles.** The statement is a definition with four components:

- *definiendum* — the concept `feedforward network`, the term being defined.
- *genus* — `feedforward network` is a subtype of `network`.
- *differentia attribute* — the attribute `flow of information`, an attribute of the genus.
- *differentia value* — the value `unidirectional`, which the differentia attribute takes.

**Difficulty.** The differentia references `network` and `flow of information`, which the framework may not yet contain. Requiring the researcher to define every referenced term upstream produces infinite regress and overburdens authoring.

**Resolution.** The example draws on four framework parts, but two of them are open, not ratified: the typed-placeholder forward-reference mechanism — the actual anti-infinite-regress device — is the open sub-question at [t3-definition-normal-form](3-aspect-specific/ontology#^t3-definition-normal-form) (is a placeholder a kind, a status, or a kind-annotated reference?), and the draft-profile tolerance it relies on is the open [t2-partial-formalization-profiles](2-architecture/granularity#^t2-partial-formalization-profiles). The genus-differentia *normal form* is the one part with a defined structure; the forward-reference mechanism is named and motivated but unbuilt.

**Verdict.** Partially resolved. The normal-form skeleton is defined; the forward-reference mechanism rests on two stacked open questions and is not a closed combination. **Residue:** how a forward reference actually works — placeholder as kind vs. status vs. annotated reference — is unbuilt.

- The four-way role split matches the [concept-type taxonomy](3-aspect-specific/ontology#^t3-concept-type-taxonomy): `network` is a *system*, `feedforward network` a *subtype*, `flow of information` a *property*, `unidirectional` the *value* the property takes.
- The unintroduced terms `network` and `flow of information` are admitted as forward references under the draft profile of [t2-partial-formalization-profiles](2-architecture/granularity#^t2-partial-formalization-profiles); this is the anti-infinite-regress mechanism.
- For the roles to stay clear while the referents are undefined, each forward reference carries a *typed placeholder* — a kind tag (system, property) and an undefined status — and is promoted to a full definition later under the promotion rule, without rewriting referencing content. Whether such a placeholder is a distinct kind, a maturity state, or a kind-annotated reference is recorded as the open sub-question [normalized definition form](3-aspect-specific/ontology#^t3-definition-normal-form).
- Each component is an addressable typed object per [t1-typed-object-decomposition](_framework-criteria#^t1-typed-object-decomposition), with roles assigned by function per [t1-function-driven-typology](_framework-criteria#^t1-function-driven-typology).
- The genus link (`feedforward network` subtype-of `network`) and the differentia link are typed relations; their maturity is governed by [progressive relation formalization](_fleeting-ideas#^fleeting-relation-formalization).

**General lesson propagated.** The genus-differentia normal form and the typed-placeholder forward-reference mechanism are recorded as the open question [t3-definition-normal-form](3-aspect-specific/ontology#^t3-definition-normal-form) in the ontology theme. A second expert review of this example contributed further refinements: the definition-structure refinements (template registry, template-inferred hole kinds, typed ambiguity, stable cross-statement placeholders, lexical/concept separation, the three-operation split) are folded into that same open question; the undischarged-commitment refinements (presuppositions, commitment strengths, definitional force) are filed as [t3-undischarged-commitments](3-aspect-specific/arguments-reasoning#^t3-undischarged-commitments). All are kept general rather than tied to this example.

**Candidate normalization pipeline and object model.** The second review also proposed a concrete pipeline and object model for normalizing a statement. They are recorded here as a candidate, at implementation grain, for whoever resolves [t3-definition-normal-form](3-aspect-specific/ontology#^t3-definition-normal-form).

The pipeline runs without failing on unresolved references:

```text
raw statement
  -> span annotation
  -> template recognition
  -> role assignment
  -> provisional object creation
  -> presupposition extraction
  -> semantic graph construction
  -> optional ontology export
```

The intermediate semantic graph has term occurrences and provisional objects as nodes, and semantic roles as edges — an intermediate representation between prose and formal logic, distinct from both.

The candidate object model:

- `NormalizedStatement` — original text, statement type, span annotations, semantic-role bindings, introduced objects, unresolved references, presuppositions, candidate formalizations.
- `DefinitionStatement` (a `NormalizedStatement`) — definiendum, definition pattern, definitional force, genus, differentiae.
- `AttributeConstraint` — bearer, attribute, constraint relation, value, formalization status.
- `UnresolvedReference` — label, expected kind, introducing object, local semantic role, resolution status.
- `Presupposition` — content, source statement, role, status, priority.

---

## 1. Definitions with unstable genus and implicit criterion shift

> A feedforward network is not merely a network without recurrence, but a computational regime in which the relevant causal dependencies can be represented as an acyclic order, provided that feedback-like effects introduced by training, normalization, or external control are not counted as part of the forward computation.

| Difficulty              | Description                                                           |
| ----------------------- | --------------------------------------------------------------------- |
| unstable genus          | `feedforward network` shifts from object type to computational regime |
| negative definition     | “not merely” rejects an expected definition                           |
| hidden criterion        | recurrence is replaced by causal representability                     |
| boundary exclusion      | training, normalization, external control are excluded                |
| context-sensitive scope | “forward computation” is treated as a restricted temporal slice       |

**Resolution.** The genus-differentia normal form at [t3-definition-normal-form](3-aspect-specific/ontology#^t3-definition-normal-form) handles the structural skeleton, and three further difficulties are each now covered. The *negative definition* ("not merely a network without recurrence") is a definition stated by rejecting a competing definition; the negative-definition template row added to [t3-definition-normal-form](3-aspect-specific/ontology#^t3-definition-normal-form) now carries this, and the contrastive family of the [linking-phrase taxonomy](_fleeting-ideas#^fleeting-relation-formalization) carries the rejecting edge. The *unstable genus* (the definiendum's genus shifts from object kind to computational regime) is a typed-ambiguity case at the genus slot: the genus placeholder carries a *candidate-set field* per the re-cut at [t3-definition-normal-form](3-aspect-specific/ontology#^t3-definition-normal-form), a set of candidate kinds rather than one. The *boundary exclusion* (training, normalization, external control "not counted as part of the forward computation") is a scope qualifier — each exclusion is a presupposition the definition leans on, carried by the [undischarged-commitments](3-aspect-specific/arguments-reasoning#^t3-undischarged-commitments) machinery. The *hidden criterion shift* (recurrence replaced by causal representability) is **not** a definitional-force concern — definitional force is the necessary/sufficient/biconditional axis, not criterion replacement. A criterion shift is the *rejection of the old differentia criterion plus assertion of a new one*, so it routes to the rejected-definition slot of the negative-definition template at [t3-definition-normal-form](3-aspect-specific/ontology#^t3-definition-normal-form): the old criterion (recurrence) is the rejected definition, the new criterion (causal representability) the asserted one.

**Verdict.** Partially resolved. Negative definition and boundary exclusion are propagated; the unstable genus rests on the candidate-set/resolution-policy open question at `^t3-definition-normal-form` (residue); the criterion shift is now routed but the template does not yet specify a *silent-substitution* check — a criterion shift differs from an authored multi-rejection in being unannounced.

**General lesson** → propagated to [t3-definition-normal-form](3-aspect-specific/ontology#^t3-definition-normal-form). Negative or contrastive definitions — defining X by rejecting a competing definition of X — need a template-registry entry distinct from genus-differentia; the rejected definition is a first-class part of the normalized form, not noise. The negative-definition template row, generalised to multi-rejection, carries this. **Residue:** a *silent* criterion shift (the differentia criterion is swapped without the swap being announced) is a sharper case the multi-rejection template does not yet detect — recorded as an open refinement of that template.

---

## 2. Conceptual distinction that also revises the target concept

> The distinction between information being present in a representation and information being used by the system is not an additional refinement of representational analysis; it changes what should count as representation in the first place.

|Difficulty|Description|
|---|---|
|distinction-as-revision|the distinction modifies the concept it distinguishes|
|meta-conceptual move|the statement concerns the criteria for concept application|
|normative force|“should count” is not descriptive|
|target ambiguity|“representation” may mean data structure, neural state, or explanatory construct|

**Resolution.** A `Distinction` is a candidate object kind in the [kind-set](_fleeting-ideas#^fleeting-kind-set). *Distinction-as-revision* — this distinction does not merely sit beside `representation`, it changes the concept's application criteria — needs a *distinction-revises-criterion* edge, distinct from a plain relate-two-concepts edge. **This edge cannot be filed now.** Adding an edge type is a relation-vocabulary decision, and the relation vocabulary is explicitly deferred (main handoff: "the exact relation vocabulary deferred to the project TODO"). The difficulty is therefore not resolved — it is blocked on the deferred relation-vocabulary decision and recorded as a residue below. The *meta-conceptual move* (the statement concerns the criteria for applying a concept, not its referent) is the meta-conceptual-statement item of [content about language](_fleeting-ideas#^fleeting-metalinguistic-content). *Normative force* ("should count") is the definitional-force axis of [undischarged-commitments](3-aspect-specific/arguments-reasoning#^t3-undischarged-commitments) generalised from definitions to distinctions. *Target ambiguity* is the candidate-set field of the placeholder, per [t3-definition-normal-form](3-aspect-specific/ontology#^t3-definition-normal-form).

**Verdict.** Partially resolved. The meta-conceptual move is propagated; the *distinction-revises-criterion* edge is **blocked on the deferred relation vocabulary** and cannot be resolved without un-deferring it.

**General lesson** → propagated to [content about language](_fleeting-ideas#^fleeting-metalinguistic-content) (meta-conceptual statement). Statements *about the criteria for applying a concept* are metalinguistic content. **Residue:** a `Distinction` may revise the application criterion of the concept it distinguishes; the edge type this needs is a relation-vocabulary addition the framework currently forbids itself from making — recorded as an open dependency on the deferred relation vocabulary, not as a resolved item.

---

## 3. Argument with an undercutting condition hidden inside an example

> If a variable is linearly decodable from every hidden layer but ablating the subspace carrying it has no effect on the model’s behaviour, then the decodability result looks less like evidence of representation and more like evidence of redundant statistical alignment.

|Difficulty|Description|
|---|---|
|hypothetical evidence|no concrete empirical result is asserted|
|comparative reinterpretation|one evidential role is displaced by another|
|implicit undercutter|decodability is weakened as evidence|
|latent alternative explanation|“redundant statistical alignment” introduces a competing construct|
|modal softness|“looks less like” avoids strict entailment|

**Resolution.** The *implicit undercutter* is squarely the [t3-attack-target](3-aspect-specific/arguments-reasoning#^t3-attack-target) open question: the statement attacks the *inference* from decodability to representation, not the conclusion — an undercutter, not a rebuttal. The *latent alternative explanation* ("redundant statistical alignment") is a competing construct introduced as the undercutter's payload; the [argumentation-graph](_fleeting-ideas#^fleeting-argumentation-graph) authored-edge subset handles competing-explanation edges. *Hypothetical evidence* (the whole statement is conditional — "if X but Y, then Z") and *modal softness* ("looks less like" — not strict entailment) are both carried by the hypothetical-statement item of [statement modality](_fleeting-ideas#^fleeting-statement-modality). *Comparative reinterpretation* (one evidential role displaced by another) is a content-transforming move in the [move vocabulary](_fleeting-ideas#^fleeting-move-vocabulary).

**General lesson** → propagated to [statement modality](_fleeting-ideas#^fleeting-statement-modality). A statement may be entirely *conditional and hypothetical* — asserting no fact, only "if such evidence held, it would mean Z". A statement, not only a warrant, must be markable as hypothetical, so it is not read as an assertion; the statement-modality candidate records this.

---

## 4. Research question embedded in a critique

> The problem with asking whether a network “contains” a concept is that the question presupposes a container model of representation, whereas the more relevant issue may be whether the concept is stabilized across transformations that preserve the task.

|Difficulty|Description|
|---|---|
|question critique|the statement attacks the framing of a question|
|metaphor diagnosis|“container model” is a conceptual metaphor, not a formal claim|
|alternative inquiry|a replacement question is introduced|
|task-relative criterion|“preserve the task” is itself theoretically loaded|
|soft modality|“may be” marks tentative redirection|

**Resolution.** The *question critique* is an attack whose target is a `Question` object — specifically its presupposition ("contains" presupposes a container model). [t3-attack-target](3-aspect-specific/arguments-reasoning#^t3-attack-target) covers attacks on inferences; the extension to attacks on a question's *framing* is recorded against that open question, and connects to [undischarged-commitments](3-aspect-specific/arguments-reasoning#^t3-undischarged-commitments): the critique surfaces a presupposition the question carries. The *alternative inquiry* (a replacement question is introduced) is a question-to-question move — the [move vocabulary](_fleeting-ideas#^fleeting-move-vocabulary)'s `problematize` plus a reframing move, bearing on [goal-driven reasoning](_framework-criteria#^t1-goal-driven-reasoning) since it restructures the question network. *Metaphor diagnosis* ("container model" named as a metaphor, not a formal claim) is now carried by [meta-conceptual content](_fleeting-ideas#^fleeting-metalinguistic-content) (metaphor as a diagnosable object). *Soft modality* is the modal gap again.

**General lesson** → propagated to [t3-attack-target](3-aspect-specific/arguments-reasoning#^t3-attack-target) and [meta-conceptual content](_fleeting-ideas#^fleeting-metalinguistic-content). Two gaps. (a) A statement can *attack the framing or presupposition of a question*, not a claim or an inference — `^t3-attack-target` now records a third attack target, an attack on a `Question`'s framing, alongside rebuttal and undercutter. (b) A conceptual metaphor ("container model") can be a named, diagnosable object that an argument targets — recorded as metaphor-as-object in the metalinguistic-content candidate.

---

## 5. Definition by refusal of inadequate operationalizations

> Task-relevance cannot be identified with decodability, causal effect, or mutual information alone, because each captures a different shadow of the relation between a representation and a task.

|Difficulty|Description|
|---|---|
|negative triangulation|concept is defined by rejecting several approximations|
|metaphorical content|“shadow” is meaningful but non-literal|
|plural partial adequacy|rejected criteria are not simply false|
|missing positive definition|no direct criterion is supplied|
|relation reification|“relation between representation and task” becomes the true object|

**Resolution.** *Negative triangulation* extends the negative-definition gap from example 1: here the definition rejects *several* approximations at once (decodability, causal effect, mutual information), each rejected as partial rather than false. The multi-rejection negative-definition pattern added to [t3-definition-normal-form](3-aspect-specific/ontology#^t3-definition-normal-form) carries this, including the *plural partial adequacy* — that template records each rejection's adequacy grade, so a rejected criterion can be marked partially adequate rather than false. *Missing positive definition* is handled by [t1-partial-formalization](_framework-criteria#^t1-partial-formalization): a definition may rest at a stage where only the negative boundary is drawn. *Relation reification* ("the relation between representation and task" becomes the object) is the reified-relation convergence noted in [progressive relation formalization](_fleeting-ideas#^fleeting-relation-formalization). *Metaphorical content* ("shadow") is carried by the metaphor-as-object item of [meta-conceptual content](_fleeting-ideas#^fleeting-metalinguistic-content).

**General lesson** → propagated to [t3-definition-normal-form](3-aspect-specific/ontology#^t3-definition-normal-form). Negative definition generalises to multi-rejection — a definition stated by rejecting several partial approximations at once, now a template-registry row whose rejections each carry an adequacy grade (a rejected criterion can be partially adequate, not false).

---

## 6. Claim whose force depends on disciplinary perspective

> In neuroscience, calling a feature “represented” often means that it is recoverable from activity; in mechanistic interpretability, the same word is misleading unless the feature participates in the computation.

|Difficulty|Description|
|---|---|
|discipline-relative semantics|same term has different standards across fields|
|no global definition|neither use is declared universally correct|
|pragmatic evaluation|“misleading” is not a truth-functional predicate|
|implicit contrast|recoverability versus participation|
|sociolinguistic content|the statement describes scientific usage norms|

**Resolution.** *Discipline-relative semantics* and *no global definition* are the [ontology-modularity](_fleeting-ideas#^fleeting-ontology-modularity) candidate exactly: the same term ("represented") carries different definitions in neuroscience and mechanistic interpretability, and the framework must hold both without forcing a global canonical concept — the recorded tension with [t1-canonical-terminology](_framework-criteria#^t1-canonical-terminology). *Implicit contrast* (recoverability vs. participation) is a contrastive edge in the [linking-phrase taxonomy](_fleeting-ideas#^fleeting-relation-formalization). *Pragmatic evaluation* ("misleading" — not truth-functional) reinforces the modal/epistemic-attitude propositional gaps. *Sociolinguistic content* — the statement *describes a usage norm* rather than asserting a fact about the domain — is now carried by the usage-norm item of [meta-conceptual content](_fleeting-ideas#^fleeting-metalinguistic-content).

**General lesson** → propagated to [meta-conceptual content](_fleeting-ideas#^fleeting-metalinguistic-content). A statement may assert a *usage norm* — a fact about how a scientific community uses a term — rather than a fact about the research domain. This metalinguistic content is now a staged candidate; it converges with the lexical-term level of the [definition-normal-form](3-aspect-specific/ontology#^t3-definition-normal-form) five-level term/concept separation.

---

## 7. Derivation whose conclusion is a changed viewpoint

> Once the context variable is treated not as an input feature but as an instruction selecting a task, the apparent geometry of the representation should no longer be interpreted as encoding a larger stimulus space, but as implementing a family of conditional coordinate systems.

|Difficulty|Description|
|---|---|
|reclassification of object|context variable becomes instruction|
|interpretation shift|geometry receives a new explanatory role|
|negative and positive reading|one interpretation is rejected, another introduced|
|metaphorical-formal hybrid|“conditional coordinate systems” is both suggestive and technical|
|dependency on modelling choice|conclusion depends on how context is treated|

**Resolution.** *Reclassification of object* (the context variable is re-typed from input feature to instruction) and *dependency on modelling choice* (the whole conclusion is conditional on that re-typing) are the same phenomenon as example 19 — a modelling choice changes an object's kind. The re-typing here is a *modelling-choice re-typing*, governed as a branch point by the ratified [t3-no-hidden-branch-choice](3-aspect-specific/arguments-reasoning#^t3-no-hidden-branch-choice) (recorded as a branch with siblings); the conclusion that depends on it inherits a conditional commitment ([undischarged-commitments](3-aspect-specific/arguments-reasoning#^t3-undischarged-commitments)). An earlier draft routed this to a unifying `re-type` move; that move was dissolved by audit as fusing three distinct phenomena. *Interpretation shift* (geometry gets a new explanatory role) is a `Perspective`-change in the [kind-set](_fleeting-ideas#^fleeting-kind-set). *Negative and positive reading* is the reject-one/introduce-another structure of examples 1 and 5. *Metaphorical-formal hybrid* ("conditional coordinate systems" is both suggestive and technical) — a term occupying a metaphorical and a formal register at once — is the hybrid-register item of [meta-conceptual content](_fleeting-ideas#^fleeting-metalinguistic-content), distinct from metaphor-diagnosis (ex. 4) because here the metaphor is *used*, not diagnosed.

**General lesson** → propagated to [t3-no-hidden-branch-choice](3-aspect-specific/arguments-reasoning#^t3-no-hidden-branch-choice) and [metaphor as a diagnosable object](_fleeting-ideas#^fleeting-metalinguistic-content). Modelling-choice re-typing is a branch point governed by the ratified no-hidden-branch-choice criterion; conclusions reached after a re-typing carry a conditional commitment on it. A term may sit in a *hybrid register*, simultaneously metaphorical and technical — the metaphor-as-object item of the meta-conceptual-content candidate.

---

## 8. Argument where the warrant is methodological rather than propositional

> The reason to compare representational geometries across contexts is not that geometry is the final object of interest, but that geometry is the least arbitrary level at which global transformations can be made visible without committing to a particular decoder.

|Difficulty|Description|
|---|---|
|methodological justification|argues for an analysis strategy|
|non-finality|the chosen object is instrumental, not ultimate|
|comparative criterion|“least arbitrary” is a methodological value judgment|
|implicit alternatives|decoders are rejected without being enumerated|
|visualization role|“made visible” mixes cognition, method, and explanation|

**Resolution.** *Methodological justification* — the warrant is "do this analysis because it is the least arbitrary level", an argument *for an analysis strategy*, not for a propositional claim. The three-level justification model at [t1-reasoning-understandability](_framework-criteria#^t1-reasoning-understandability) (Licensing / Strategic / Explanatory) justifies *reasoning moves*; a justification for a *method choice* is a distinct argument target, recorded as a candidate methodological argument scheme against the [reasoning-schemes](3-aspect-specific/arguments-reasoning#^t3-reasoning-schemes) open question. *Non-finality* (the chosen object is instrumental) and *comparative criterion* ("least arbitrary" is a value judgment) are evaluative content — the [QOC option-under-criteria substructure](_fleeting-ideas#^fleeting-qoc-substructure) handles option-assessed-against-criterion, and "least arbitrary" is such a criterion. *Implicit alternatives* (decoders rejected without enumeration) is a forward-reference case: the rejected alternatives are referenced but undefined ([definition-normal-form](3-aspect-specific/ontology#^t3-definition-normal-form) placeholders). *Visualization role* ("made visible" mixing cognition, method, explanation) touches the Explanatory level of understandability.

**General lesson** → propagated to the [reasoning-schemes](3-aspect-specific/arguments-reasoning#^t3-reasoning-schemes) open question. A warrant may justify a *method or analysis-strategy choice* rather than a propositional inference; methodological justification is a distinct argument target — a candidate methodological argument scheme.

---

## 9. Statement that introduces an explanatory gap rather than a claim

> Even if two contexts produce separable manifolds, it remains unclear whether this separation is the mechanism by which the network solves the task or merely the geometric trace of some lower-level routing process.

|Difficulty|Description|
|---|---|
|uncertainty as content|the main object is an unresolved ambiguity|
|alternative explanations|mechanism versus trace|
|same observation, different roles|separability can be causal or epiphenomenal|
|hidden demand|asks for criteria distinguishing mechanism from trace|
|non-assertive structure|the statement advances inquiry by suspending commitment|

**Resolution.** This is the cleanest fit so far. *Uncertainty as content* and *non-assertive structure* — the statement's payload *is* an unresolved gap, not a claim — is exactly the [epistemic-gap](2-architecture/object-kinds#^t2-question-vs-goal) reading of the unified Question/Goal kind, and the gap is of the *missing-mechanism* subtype in [t3-epistemic-gap-subtypes](3-aspect-specific/ontology#^t3-epistemic-gap-subtypes). *Hidden demand* (the statement asks for criteria distinguishing mechanism from trace) is the gap's success condition under [goal-driven reasoning](_framework-criteria#^t1-goal-driven-reasoning). *Alternative explanations* (mechanism vs. trace) and *same observation, different roles* (separability is causal or epiphenomenal) are competing-explanation edges over one observation — the [argumentation-graph](_fleeting-ideas#^fleeting-argumentation-graph) authored-edge subset. **Resolved, pending ratification** — the gap-as-content reading is ratified (`^t2-question-vs-goal`), but the gap-subtype taxonomy is the open question `^t3-epistemic-gap-subtypes` and the competing-explanation edges are the staged argumentation-graph candidate. No new mechanism is needed; the covering parts must be ratified.

**General lesson** — none; no propagation. This example confirms that the epistemic-gap kind, the gap-subtype taxonomy, and competing-explanation edges together cover statements whose entire content is a suspended commitment.

---

## 10. Conceptual move that changes granularity

> What appears as one representation at the layer level may decompose into several task-specific sub-representations once the computation is analysed along paths rather than units.

|Difficulty|Description|
|---|---|
|scale dependence|representation depends on analysis granularity|
|perspective-dependent ontology|layer-level versus path-level entities|
|modal re-description|“may decompose” is exploratory|
|implicit methodological intervention|path analysis changes the ontology|
|object instability|“one representation” may not survive refinement|

**Resolution.** *Perspective-dependent ontology* (what counts as one representation depends on whether the analysis is layer-level or path-level) is a `Perspective` object from the [kind-set](_fleeting-ideas#^fleeting-kind-set): the same content yields different object decompositions under different analytical perspectives. *Scale dependence* and *object instability* ("one representation" may not survive refinement) are now filed as [granularity-relative object identity](_fleeting-ideas#^fleeting-object-scope), which carries the tension with [t1-typed-object-decomposition](_framework-criteria#^t1-typed-object-decomposition) (a `[!missing]` callout is placed there). *Implicit methodological intervention* (path analysis changes the ontology) is the method-object entanglement of example 26. *Modal re-description* ("may decompose") is the modal gap.

**General lesson** → propagated to [granularity-relative object identity](_fleeting-ideas#^fleeting-object-scope). Typed-object decomposition is not granularity-invariant: one object at a coarse grain may be several at a finer grain, and neither decomposition is privileged. The candidate proposes a `Perspective`-indexed family of decompositions; a `[!missing]` tension callout is placed on `^t1-typed-object-decomposition`.

---

## 11. Claim with locally scoped technical vocabulary

> In this project, “attention” should not mean a learned weighting mechanism in the transformer sense, but any context-dependent deformation of representational geometry that selectively increases task-relevant separability.

|Difficulty|Description|
|---|---|
|local stipulation|term meaning is project-specific|
|exclusion of standard meaning|transformer attention is explicitly rejected|
|functional redefinition|attention becomes a geometric operation|
|normative terminology|“should not mean” is a methodological stipulation|
|composite criterion|deformation, selectivity, task relevance, separability|

**Resolution.** *Local stipulation* (the term "attention" gets a project-specific meaning) is the [ontology-modularity](_fleeting-ideas#^fleeting-ontology-modularity) candidate at the per-project grain: a module-local definition overriding the standard one. *Exclusion of standard meaning* (transformer attention explicitly rejected) is a negative-definition component — the gap recurring from examples 1 and 5. *Functional redefinition* (attention becomes a geometric operation) is a [function-driven typology](_framework-criteria#^t1-function-driven-typology) move: the redefinition keys on function, not surface form. *Normative terminology* ("should not mean") is the definitional-force axis of [undischarged-commitments](3-aspect-specific/arguments-reasoning#^t3-undischarged-commitments). *Composite criterion* (the new definition stacks deformation + selectivity + task-relevance + separability) is a genus-differentia definition with a *conjunctive* differentia — the [definition-normal-form](3-aspect-specific/ontology#^t3-definition-normal-form) template registry, with each conjunct a forward-reference placeholder. **Resolved via staged candidates**, mostly by the ontology-modularity candidate (itself in tension with the ratified `^t1-canonical-terminology`) plus the negative-definition template; no new gap.

**General lesson** — none; no propagation. Confirms that ontology modularity (module-local term meaning) plus the negative-definition template row together cover project-specific stipulative redefinition. The conjunctive differentia is a template-registry variant already implied by `^t3-definition-normal-form`.

---

## 12. Argument whose premise is an analogy with restricted scope

> The analogy with eigenvectors is useful only insofar as both aim to identify intrinsic directions of transformation; it becomes misleading as soon as one forgets that neural representations need not be governed by a linear operator with stable invariant subspaces.

|Difficulty|Description|
|---|---|
|bounded analogy|analogy has explicit scope and failure condition|
|mixed support and warning|the analogy is both useful and dangerous|
|technical disanalogy|linear operators and neural representations differ structurally|
|condition on misuse|problem arises from a forgotten assumption|
|no simple relation|not just `analogous_to` or `not_analogous_to`|

**Resolution.** *Bounded analogy* and *no simple relation* — the analogy holds within an explicit scope and fails outside it, so it is neither `analogous_to` nor `not_analogous_to` — is the *bounded scope* index now filed at [the reified relation object](_fleeting-ideas#^fleeting-edge-scope): an edge that holds within a stated boundary with a failure condition outside it. The candidate notes this is the relation-grain counterpart of the [reasoning-schemes](3-aspect-specific/arguments-reasoning#^t3-reasoning-schemes) "applicability conditions" — an analogy is a reusable argument scheme with a failure boundary. *Mixed support and warning* (the analogy is both useful and dangerous in one statement) is mixed evidential status — example 23's territory. *Technical disanalogy* (linear operators vs. neural representations differ) is a contrastive edge. *Condition on misuse* (the problem arises from a *forgotten assumption*) is an [undischarged-commitment](3-aspect-specific/arguments-reasoning#^t3-undischarged-commitments) made explicit.

**General lesson** → propagated to [the reified relation object](_fleeting-ideas#^fleeting-edge-scope). A relation can hold *only within an explicit scope*, with a stated failure boundary outside it — a bounded edge, now the bounded-scope index of the edge-scope candidate. Converges with example 1's context-sensitive scope.

---

## 13. A claim whose truth depends on the level of explanation

> At the computational level, the task demands an invariant decision rule; at the algorithmic level, the network may implement this through equivariant intermediate representations rather than invariant ones.

|Difficulty|Description|
|---|---|
|multi-level structure|Marr-level distinction is essential|
|apparent contradiction|invariant task rule versus equivariant representations|
|explanatory compatibility|distinct claims coexist at different levels|
|modality|“may implement” is not categorical|
|relation between levels|implementation relation is central but implicit|

**Resolution.** *Multi-level structure* (the claim is stated at the computational level and the algorithmic level) and *explanatory compatibility* (two claims that look contradictory coexist because they sit at different levels) are the *explanation-level index* — a Marr level is a context index on a claim, now filed at [Context as a first-class object](_fleeting-ideas#^fleeting-context-object). Its operative effect is on validation: a contradiction-detection validator must read two claims` explanation-level indices before firing. The three-level justification model at [t1-reasoning-understandability](_framework-criteria#^t1-reasoning-understandability) is a different stratification (Licensing/Strategic/Explanatory of *one* move); Marr-style computational/algorithmic/implementation levels stratify *the claim itself*. *Apparent contradiction* (invariant rule vs. equivariant representations) is resolved by the level index — without it the two claims would read as inconsistent. *Relation between levels* (the `implements` relation between a computational rule and an algorithmic realisation) is recorded against that candidate. *Modality* is the modal gap.

**General lesson** → propagated to [Context as a first-class object](_fleeting-ideas#^fleeting-context-object). A claim may be true *at one explanation level* and a different, apparently conflicting claim true *at another* (Marr's computational / algorithmic / implementation levels). An explanation level is a context index on a claim; the candidate carries it and an `implements` relation between levels, and its effect is to stop a contradiction validator from firing on level-relative claims. Distinct from the three-level justification model.

---

## 14. Open-ended inquiry move disguised as a conclusion

> The failure of pairwise similarity measures is therefore not merely empirical; it suggests that the object being compared has been underspecified.

|Difficulty|Description|
|---|---|
|conclusion opens problem|result generates a new object-level question|
|empirical-to-conceptual shift|failure of method diagnoses underspecified object|
|hidden presupposition|comparison requires a defined object of comparison|
|non-deductive inference|“suggests” expresses abductive movement|
|underspecification target|unclear whether object is representation, geometry, context, or task|

**Resolution.** *Conclusion opens problem* (a result that generates a new question rather than closing one) is the progressive-problem-solving stance already in [goal-driven reasoning](_framework-criteria#^t1-goal-driven-reasoning) — a move can open a sub-question — and the new question is a [missing-mechanism or incomplete-characterisation gap](3-aspect-specific/ontology#^t3-epistemic-gap-subtypes). *Hidden presupposition* (comparison requires a defined object of comparison) is exactly [undischarged-commitments](3-aspect-specific/arguments-reasoning#^t3-undischarged-commitments): the method's failure surfaces a presupposition it leaned on. *Non-deductive inference* ("suggests" — abductive movement) is a warrant kind: [t1-mixed-monotonicity](_framework-criteria#^t1-mixed-monotonicity) governs monotonic vs. defeasible warrants, and `abductive` is already a ratified entry in the warrant-kind enum of the warrant-vocabulary theme, already classed as defeasible. *Empirical-to-conceptual shift* (a method failure diagnoses an underspecified *object*, not a wrong result) and *underspecification target* (unclear which object is underspecified) connect to the typed-ambiguity mechanism in the open question [t3-definition-normal-form](3-aspect-specific/ontology#^t3-definition-normal-form): the underspecified term carries a candidate set. **Resolved** — `^t1-mixed-monotonicity` and the abductive warrant entry are ratified; the underspecified-object reading rests on the typed-ambiguity open question.

**General lesson** — none; no propagation. A method failure can be diagnosed as the *object of study being underspecified* rather than the method being wrong — an empirical-to-conceptual diagnostic move; the framework's gap and undischarged-commitment machinery cover this. Abduction ("suggests") is already a ratified entry in the warrant-kind enum of the warrant-vocabulary theme, already classed as a defeasible warrant — nothing to record.

---

## 15. Source-sensitive claim with interpretive uncertainty

> Saxe et al. seem to treat learning dynamics as revealing the structure of the task through singular modes, but it is not obvious whether this should be read as a claim about representations themselves or about the input-output map implemented by the whole network.

|Difficulty|Description|
|---|---|
|uncertain attribution|“seem to treat” avoids direct citation commitment|
|interpretive ambiguity|two readings of a source are possible|
|source-sensitive meaning|claim concerns what an author means|
|theory-object ambiguity|representations versus global map|
|requires hermeneutic tracking|interpretation may later be revised|

**Resolution.** *Source-sensitive meaning* and *uncertain attribution* — the claim is about *what an author means*, hedged with "seem to treat" — is the source-interpretation item now filed at [content about sources](_fleeting-ideas#^fleeting-source-facing-content). [Citation-intent](_fleeting-ideas#^fleeting-citation-intent) types how the *citing* work uses the cited one; an *interpretation* of the cited work is a distinct, separately-filed content kind, exposition-adjacent (the framework treats literature-facing work as secondary per [t1-activity-separation](_framework-criteria#^t1-activity-separation)). *Interpretive ambiguity* (two readings of the source are possible) is a candidate-set field per [t3-definition-normal-form](3-aspect-specific/ontology#^t3-definition-normal-form) applied to a source-interpretation object. *Theory-object ambiguity* (representations vs. global map) is the same ambiguity at the object level. *Requires hermeneutic tracking* (the interpretation may later be revised) is [revision accountability](_framework-criteria#^t1-revision-accountability): an interpretation is revisable content with provenance.

**General lesson** → propagated to [content about sources](_fleeting-ideas#^fleeting-source-facing-content). An *interpretation of a source* — a hedged claim about what an author means — is a distinct content kind, revisable and about a source rather than the domain; it is exposition-adjacent and the candidate records it at the boundary of the exposition-is-derived deferral.

---

## 16. Claim involving partial formalization and residual intuition

> The covariance recursion gives a precise handle on how correlations propagate, but the sense in which this constitutes an explanation of representation formation remains partly metaphorical unless the relevant task variables are identified inside the recursion.

|Difficulty|Description|
|---|---|
|formal tool with interpretive gap|mathematics exists but explanatory status is unclear|
|partial adequacy|recursion is useful but insufficient|
|metaphor diagnosis|“explanation” may be only metaphorical|
|missing bridge|task variables must be identified in formal dynamics|
|layered evaluation|precision and understanding are separated|

**Resolution.** *Formal tool with interpretive gap* and *layered evaluation* — a result is mathematically precise yet its *explanatory* status is unclear — is the Licensing-vs-Explanatory split inside [t1-reasoning-understandability](_framework-criteria#^t1-reasoning-understandability): a step can be licensed (formally valid) without delivering the Explanatory-level gain. The example confirms that criterion's "formal validity is not understanding" thesis directly. *Partial adequacy* (the recursion is useful but insufficient) is the graded-adequacy axis surfaced at example 5. *Missing bridge* (task variables must be identified inside the formal dynamics for the recursion to count as explanation) is an [undischarged-commitment](3-aspect-specific/arguments-reasoning#^t3-undischarged-commitments) — a deferred obligation the formal result leans on — and a [partial-formalization](_framework-criteria#^t1-partial-formalization) state: the formalization is incomplete in a specific, nameable way. *Metaphor diagnosis* ("explanation" may be only metaphorical) is the metaphor gap from examples 4–5. **Covered** — the primary difficulty is handled by the ratified Licensing/Explanatory split in `^t1-reasoning-understandability`; the graded-adequacy and metaphor items are already surfaced (staged at the edge-scope and metalinguistic candidates) and add no new gap.

**General lesson** — none; no propagation. Confirms that the Licensing-vs-Explanatory distinction in `^t1-reasoning-understandability` already separates formal precision from explanatory adequacy. Reinforces the graded-adequacy axis (ex. 5, propagated to [the reified relation object](_fleeting-ideas#^fleeting-edge-scope)) and the metaphor item (ex. 4, propagated to [meta-conceptual content](_fleeting-ideas#^fleeting-metalinguistic-content)).

---

## 17. Statement with deferred object identity

> The same “representation” may be the activity vector, the subspace spanned by task-relevant variation, the equivalence class under readout-preserving transformations, or the causal role played in the computation.

|Difficulty|Description|
|---|---|
|term fragmentation|one term maps to multiple candidate objects|
|no chosen resolution|alternatives remain open|
|different ontological types|vector, subspace, equivalence class, causal role|
|formalization-sensitive identity|object identity depends on modelling choice|
|not merely ambiguity|each candidate may be scientifically legitimate|

**Resolution.** This is the candidate-set field of [t3-definition-normal-form](3-aspect-specific/ontology#^t3-definition-normal-form) in its purest form: one term ("representation") carries a candidate set of *four* referents. *Different ontological types* (activity vector, subspace, equivalence class, causal role are not the same kind of thing) means the candidate set is heterogeneous, spanning the [concept-type taxonomy](3-aspect-specific/ontology#^t3-concept-type-taxonomy) and the [kind-set](_fleeting-ideas#^fleeting-kind-set). *Formalization-sensitive identity* means the resolution policy is `will-resolve` only once a modelling choice is made — the same fork as examples 7 and 19. *Not merely ambiguity* (each candidate is scientifically legitimate) corresponds to the resolution policy being potentially `cannot-resolve` rather than `will-resolve`.

**Verdict.** Routed to an open question, not resolved. The candidate-set field and the concept-type taxonomy both sit in open questions (`^t3-definition-normal-form`, `^t3-concept-type-taxonomy`); this example contributes one clause to the first — that the candidate set may be heterogeneous in kind — and resolves nothing on its own.

**General lesson** → propagated to [t3-definition-normal-form](3-aspect-specific/ontology#^t3-definition-normal-form). One sharpening of typed ambiguity: a candidate set may contain candidates of *different object kinds* (a vector, a subspace, an equivalence class, a causal role), not just instances of one kind. The candidate-set field now records that it may be heterogeneous in kind.

---

## 18. Conceptual critique with implicit desiderata

> A metric that changes under arbitrary reparameterizations of the hidden layer may still be statistically informative, but it cannot serve as an intrinsic characterization of the network’s computation.

|Difficulty|Description|
|---|---|
|dual evaluation|statistically useful but theoretically inadequate|
|implicit desideratum|intrinsic characterization requires invariance|
|contrast between goals|information versus characterization|
|hidden formal property|reparameterization invariance is not spelled out|
|normative methodological claim|“cannot serve” depends on research aim|

**Resolution.** *Implicit desideratum* (intrinsic characterization requires reparameterization invariance) and *hidden formal property* (the invariance is not spelled out) are an [undischarged-commitment](3-aspect-specific/arguments-reasoning#^t3-undischarged-commitments): the critique leans on an unstated criterion. *Dual evaluation* (the metric is statistically useful but theoretically inadequate) is the graded/multi-axis evaluation seen at examples 5 and 16 — a thing can score well on one axis and fail another, and the [QOC option-under-criteria substructure](_fleeting-ideas#^fleeting-qoc-substructure) handles option-assessed-against-multiple-criteria. *Contrast between goals* (information vs. characterization) is a contrastive edge between two research aims. *Normative methodological claim* ("cannot serve" depends on the research aim) is definitional/methodological force, aim-relative — the same aim-relativity as example 25. **Resolved via open question and staged candidate** — the unstated-desideratum reading rests on the `^t3-undischarged-commitments` open question and the multi-criterion evaluation on the staged QOC-substructure candidate; no new gap.

**General lesson** — none; no propagation. Confirms that a critique often leans on an *unstated desideratum* (here, reparameterization invariance) which the undischarged-commitments machinery surfaces, and that an object can be evaluated against multiple criteria with divergent verdicts (QOC substructure). Reinforces aim-relativity (ex. 25).

---

## 19. Claim where context changes the type of the object

> When the cue is treated as a context, the representation is a family indexed by tasks; when the cue is treated as a stimulus, the representation is a single geometry over an enlarged input space.

|Difficulty|Description|
|---|---|
|modelling choice changes object type|family versus single geometry|
|same data, different ontology|cue receives different role|
|indexical structure|context induces task-indexed representation|
|no empirical difference necessarily|distinction may be conceptual|
|formalization fork|later analyses diverge from this choice|

**Resolution.** *Modelling choice changes object type* and *formalization fork* — treating the cue as context vs. as stimulus yields a task-indexed family vs. a single geometry, and later analyses diverge from the choice — is the same re-typing-as-move phenomenon as example 7, plus a new emphasis: the modelling choice is a *branch point* in the inquiry, and [t3-no-hidden-branch-choice](3-aspect-specific/arguments-reasoning#^t3-no-hidden-branch-choice) already requires branch choices to be explicit. So a re-typing modelling choice is a recordable branch, and the divergent downstream analyses are the branch's children. *Same data, different ontology* (the cue gets different roles, no empirical difference necessarily) is [typed ambiguity](3-aspect-specific/ontology#^t3-definition-normal-form) at the modelling grain. *Indexical structure* (context induces a task-indexed representation) is the [context-object](_fleeting-ideas#^fleeting-context-object) candidate. **Partially resolved** — the branch-point reading rests on the ratified `^t3-no-hidden-branch-choice`, but the context-as-object and typed-ambiguity parts are a staged candidate and an open question; confirms re-typing is a branch choice.

**General lesson** — none; no propagation. Confirms that a modelling/re-typing choice is a branch point governed by `^t3-no-hidden-branch-choice`, and that purely conceptual forks (no empirical difference) must still be recorded as explicit branches. Reinforces re-typing-as-move (ex. 7, propagated to the [move vocabulary](_fleeting-ideas#^fleeting-move-vocabulary)) and context-as-object.

---

## 20. Research move involving strategic non-definition

> It may be premature to define task-relevance directly; instead, the inquiry should first isolate the transformations under which any acceptable definition must remain invariant.

|Difficulty|Description|
|---|---|
|intentional deferral|definition is postponed deliberately|
|meta-criterion first|invariance constraints precede definition|
|inquiry strategy|statement directs research process|
|non-object-level content|concerns order of investigation|
|negative operationality|defines what not to do yet|

**Resolution.** *Intentional deferral* (the definition of task-relevance is deliberately postponed) is the [partial-formalization](_framework-criteria#^t1-partial-formalization) draft-profile stance made into an explicit *move*: the deferral is chosen, not incidental. *Meta-criterion first* (invariance constraints must be settled before the definition) is the [t3-definition-normal-form](3-aspect-specific/ontology#^t3-definition-normal-form) three-operation split — normalization/completion/validation — read as an *ordering*. *Inquiry strategy* and *non-object-level content* — the statement directs the research *process*, it is not a claim about the domain — is the inquiry-steering item now filed at [non-assertive statement categories](_fleeting-ideas#^fleeting-non-assertive-statements); the [move vocabulary](_fleeting-ideas#^fleeting-move-vocabulary)'s `metadiscourse` move names the act of producing such a statement. *Negative operationality* (defining what *not* to do yet) is the negative-definition pattern turned toward process.

**General lesson** → propagated to [non-assertive statement categories](_fleeting-ideas#^fleeting-non-assertive-statements). A statement may be *inquiry-steering* — its content is a directive about the research process, not a claim about the domain. The candidate records it as a statement category distinct from domain content, so it is not validated as a claim. Recurs at examples 31 and 40.

---

## 21. Boundary case as concept probe

> A neuron that carries task information only because it is correlated with another genuinely causal feature is precisely the kind of case that forces the difference between encoding and use to become explicit.

|Difficulty|Description|
|---|---|
|boundary case|example tests a conceptual distinction|
|indirect information|information arises through correlation|
|causal asymmetry|causal feature differs from correlated carrier|
|case-as-method|example is used to force clarification|
|latent classification problem|neuron may encode without being used|

**Resolution.** *Case-as-method* — a boundary case used deliberately to *force a conceptual distinction explicit* — is the worked-examples discipline itself, and at the framework grain it is an `Example`/`Counterexample` object from the [kind-set](_fleeting-ideas#^fleeting-kind-set) used as a *probe*: an example whose function is not to illustrate but to test a `Distinction`. *Boundary case* and *latent classification problem* (the neuron sits exactly on the encoding/use line) confirm the `Distinction` object (ex. 2) needs to be probeable by examples. *Indirect information* and *causal asymmetry* (information via correlation; the causal feature differs from the correlated carrier) is a counterfactual/causal-structure concern — example 37's territory, where contribution is defined counterfactually. **Resolved via staged candidate** — the `Example` and `Distinction` objects are both in the staged `^fleeting-kind-set` (`Distinction` is one of its explicitly novel kinds), and the probe role is a candidate enrichment of that candidate.

**General lesson** → propagated to the [candidate kind-set](_fleeting-ideas#^fleeting-kind-set). An `Example` object can serve a *probe* function — used to force a `Distinction` explicit or to test its boundary — distinct from an illustrative example. The probe role is recorded against the `Example` kind: a probe example is admissible even when it instantiates nothing, since its purpose is to stress a distinction.

---

## 22. Statement whose content is a failure mode of a concept

> The danger of “representation” is that it can name either the structure that explains the computation or merely the structure that an external observer can recover from the system.

|Difficulty|Description|
|---|---|
|concept pathology|statement diagnoses a problematic ambiguity|
|observer-relative content|one reading depends on external recovery|
|explanatory contrast|explanation versus recoverability|
|warning rather than claim|function is cautionary|
|non-standard object|“danger of a concept” is itself a research object|

**Resolution.** *Concept pathology* and *non-standard object* — the statement's content is "the concept `representation` is dangerous because it is ambiguous between two readings", and "the danger of a concept" is itself the object — is a **defect claim**: per the re-cut at [t3-definition-normal-form](3-aspect-specific/ontology#^t3-definition-normal-form), a defectively-ambiguous concept is not an ambiguity *status* but an authored claim that the concept ought to be repaired, a first-class object connecting to the [concept-as-class-vs-object metamodeling](_fleeting-ideas#^fleeting-concept-metamodeling) candidate. *Warning rather than claim* (the statement is cautionary, not assertive) is the cautionary-content item of [non-assertive statement categories](_fleeting-ideas#^fleeting-non-assertive-statements). *Observer-relative content* and *explanatory contrast* (one reading depends on external recovery, the other on participating in computation) is the recoverability-vs-use distinction, a `Distinction` object.

**Verdict.** Routed to open questions, not resolved. The defect claim is a recognised object but its mechanism — what an author stores beyond the claim, what the framework does when a concept is marked defective — is unspecified; it rests on the `^t3-definition-normal-form` open question and the staged concept-metamodeling candidate. **Residue:** the defect claim has a name and a home, no mechanism.

**General lesson** → propagated to [t3-definition-normal-form](3-aspect-specific/ontology#^t3-definition-normal-form) and [non-assertive statement categories](_fleeting-ideas#^fleeting-non-assertive-statements). A *diagnosed defect of a concept* is a **defect claim** — an authored claim that the concept ought to be repaired, distinct from the resolution policy of its candidate set. A *warning/cautionary* statement is non-assertive content, kin to inquiry-steering content (ex. 20).

---

## 23. Mixed epistemic status within a single statement

> It is plausible, though not yet demonstrated, that the context-dependent rotation observed in the hidden space reflects a learned gating mechanism rather than a mere change in decoding basis.

|Difficulty|Description|
|---|---|
|explicit uncertainty|plausible but undemonstrated|
|observation-to-mechanism inference|geometric observation suggests mechanism|
|competing explanation|gating mechanism versus decoding basis|
|evidential weakness|not yet demonstrated|
|modality is local|uncertainty applies to one inferential link, not all terms|

**Resolution.** *Explicit uncertainty* and *evidential weakness* ("plausible, though not yet demonstrated") are an [epistemic status](2-architecture/object-kinds#^t2-epistemic-status): the claim sits at a conjecture/plausible maturity level, which the per-kind status enums already carry. *Observation-to-mechanism inference* (a geometric observation suggests a mechanism) is a defeasible warrant under [t1-mixed-monotonicity](_framework-criteria#^t1-mixed-monotonicity) — abductive, like example 14. *Competing explanation* (gating mechanism vs. decoding basis) is a competing-explanation edge, the [argumentation-graph](_fleeting-ideas#^fleeting-argumentation-graph) authored subset. The genuinely sharp difficulty — *modality is local*, the uncertainty attaching to *one inferential link* rather than the whole statement — is the *edge-local epistemic status* index now filed at [the reified relation object](_fleeting-ideas#^fleeting-edge-scope).

**General lesson** → propagated to [the reified relation object](_fleeting-ideas#^fleeting-edge-scope). Epistemic status / uncertainty can scope to a *single inferential link inside a statement*, not to the whole statement or its objects — now the edge-local-status index of the edge-scope candidate, so a statement can be partly asserted and partly hedged.

---

## 24. Derivation with a hidden change of representation language

> Rewriting the network function as a sum over paths makes some distributed effects look local, but only because locality has been moved from units to paths.

|Difficulty|Description|
|---|---|
|representation-language shift|path expansion changes explanatory vocabulary|
|apparent simplification|distributed becomes local|
|hidden cost|locality is relocated, not discovered|
|meta-representational claim|concerns effect of formalism itself|
|conceptual caution|warns against reifying the new representation|

**Resolution.** *Representation-language shift* (rewriting the network function as a sum over paths changes the explanatory vocabulary) is a [term-rewriting](_fleeting-ideas#^fleeting-term-rewriting) operation. *Hidden cost* (locality is relocated from units to paths, not discovered) and *apparent simplification* are the *explanatory non-neutrality* of a rewrite — now recorded in the term-rewriting candidate: the rewrite is formally meaning-preserving yet changes what reads as explanatory, and the trace must record that shift. *Meta-representational claim* (the statement is about the effect of the formalism itself) is a level-shift: content about a representation choice, not about the domain. *Conceptual caution* (warns against reifying the new representation) is the cautionary-content item of [non-assertive statement categories](_fleeting-ideas#^fleeting-non-assertive-statements).

**General lesson** → propagated to [term rewriting](_fleeting-ideas#^fleeting-term-rewriting). A content-transforming rewrite can be *formally meaning-preserving yet explanatorily non-neutral* — it relocates what appears local or simple; the rewrite trace records the explanatory shift it induces, not only the formal substitution. Reinforces the meta-representational level-shift (ex. 13) and the cautionary category (ex. 23).

---

## 25. Statement introducing a comparative adequacy criterion

> A useful notion of task-relevance should reject both features that are merely decodable and features that are causally active only under interventions that destroy the computation being studied.

|Difficulty|Description|
|---|---|
|desideratum for definition|not a definition, but a constraint on one|
|two-sided exclusion|rejects two different false positives|
|intervention validity|some causal tests are methodologically invalid|
|dependence on “computation being studied”|target process must be fixed|
|normativity|“useful notion should reject” is evaluative|

**Resolution.** *Desideratum for definition* — the statement is not a definition but a *constraint on any acceptable definition* — is exactly the three-operation split at [t3-definition-normal-form](3-aspect-specific/ontology#^t3-definition-normal-form): a constraint feeds the validation operation, separate from the definition itself. It is also the meta-criterion-first move of example 20. *Two-sided exclusion* (rejects two distinct false positives — merely decodable features, and features causally active only under computation-destroying interventions) is the multi-rejection negative form from example 5, here applied to a *desideratum* rather than a definition. *Intervention validity* (some causal tests are methodologically invalid) and *dependence on the computation being studied* are counterfactual-admissibility concerns — example 37 territory, where a counterfactual is meaningful only relative to an admissible intervention family. *Normativity* ("a useful notion should reject") is aim-relative definitional force. **Resolved via open question and staged candidate** — the three-operation split (constraint-on-definition) is part of the `^t3-definition-normal-form` open question, and counterfactual admissibility rests on the staged [statement-modality](_fleeting-ideas#^fleeting-statement-modality) candidate; no new gap.

**General lesson** — none; no propagation. Confirms that a *constraint on an acceptable definition* is first-class content distinct from the definition, handled by the normalization/validation split, and that such constraints can themselves take a multi-rejection negative form. Reinforces counterfactual-intervention admissibility (ex. 37) and aim-relativity (ex. 19).

---

## 26. Statement where a method produces the object it measures

> A clustering analysis of representations may reveal task-relevant groups, but it may also impose the very discreteness that later appears as evidence for those groups.

|Difficulty|Description|
|---|---|
|method-object circularity|method may construct the observed object|
|epistemic contamination|evidence depends on analysis procedure|
|ambiguous outcome|reveal versus impose|
|reflexive critique|method affects interpretation of its result|
|no simple support/attack|same method is useful and suspect|

**Resolution.** *Method-object circularity* — a clustering analysis may *reveal* task-relevant groups or may *impose* the discreteness it then reports as evidence — is the *method-result circularity* pattern now recorded as a structured undercutter at [what an attack edge targets](3-aspect-specific/arguments-reasoning#^t3-attack-target): the method partly constructs its object, which is not a justification cycle but an undercutter whose ground is the method-object relation. *Epistemic contamination* (the evidence depends on the analysis procedure) and *reflexive critique* are that undercutting relation — the critique attacks the inference from clustering-result to task-groups by noting the method shaped the result. *Ambiguous outcome* (reveal vs. impose) is a competing-reading edge. *No simple support/attack* (the same method is both useful and suspect) is mixed evidential status (ex. 23).

**General lesson** → propagated to [what an attack edge targets](3-aspect-specific/arguments-reasoning#^t3-attack-target). Method-result circularity — a method partly constructing the object it then measures — is distinct from the justification-chain circularity `^t1-no-circular-reasoning` forbids and from mutual constraint; it is a structured undercutter whose ground is the method-object relation, recorded against the attack-target open question.

---

## 27. Claim with temporal evolution and conceptual instability

> Early in training, the network may encode context as an auxiliary feature; later, the same context may become the organizing principle of the representation space.

|Difficulty|Description|
|---|---|
|diachronic change|role changes over training|
|same object changes type|auxiliary feature becomes organizing principle|
|non-static relation|relation between context and representation evolves|
|developmental explanation|learning trajectory matters|
|vague transition|no precise boundary between stages|

**Resolution.** *Diachronic change* and *same object changes type* — over training, context shifts from an auxiliary feature to the organizing principle of the representation space — is the *process-time re-typing* variant now recorded in the re-typing-as-a-move enrichment of the [move vocabulary](_fleeting-ideas#^fleeting-move-vocabulary): the object's kind changes as a fact about the phenomenon over time, distinct from the modelling-choice re-typing of examples 7 and 19, and distinct from authored revision tracked by [revision accountability](_framework-criteria#^t1-revision-accountability). *Non-static relation* (the context-representation relation itself evolves) and *vague transition* (no precise stage boundary) compound this — the relation is time-indexed and the index is fuzzy.

**General lesson** → propagated to the [move vocabulary](_fleeting-ideas#^fleeting-move-vocabulary). An object's kind or role can change along a *modelled process trajectory* (e.g. over training) — a fact about the phenomenon, distinct from authored revision. The re-typing enrichment records the need for a time-indexed object whose kind can differ at different points of a trajectory, with fuzzy stage boundaries.

---

## 28. Statement using absence as evidence

> The absence of a clean context axis does not show that context is absent from the representation; it may show that context acts by deforming the whole space rather than occupying a separable direction.

|Difficulty|Description|
|---|---|
|negative evidence|absence of marker does not imply absence of phenomenon|
|alternative mode of presence|axis versus deformation|
|measurement critique|detectable form differs from actual form|
|implicit model of representation|separable direction versus global transformation|
|epistemic caution|prevents false negative inference|

**Resolution.** *Negative evidence* — the absence of a clean context axis does not establish that context is absent — is the [four-way detection-status distinction](_fleeting-ideas#^fleeting-proof-status), now generalised beyond proofs: "no marker found" must not be conflated with "known absence", exactly the *no stored result* vs. *known absence* distinction. *Alternative mode of presence* (context may act by deforming the whole space rather than occupying a separable axis) is a competing-explanation edge, the [argumentation-graph](_fleeting-ideas#^fleeting-argumentation-graph) authored-edge subset. *Measurement critique* (the detectable form differs from the actual form) is an [undercutter](3-aspect-specific/arguments-reasoning#^t3-attack-target): it attacks the inference from "no axis detected" to "no context", by denying the warrant that context must take a detectable axis form. *Epistemic caution* is the cautionary-content item of [non-assertive statement categories](_fleeting-ideas#^fleeting-non-assertive-statements).

**General lesson** → propagated to the [four-way detection-status distinction](_fleeting-ideas#^fleeting-proof-status). The four-way "no stored result / known absence / disproved / undecided" distinction generalises from proof status to *any detection claim*: absence of a detected marker must not collapse into established absence of the phenomenon. The candidate has been generalised accordingly.

---

## 29. Conceptual dependence between two definitions

> The definition of “task variable” cannot be fixed independently of the definition of “task,” because what counts as a variable depends on which distinctions the task itself makes relevant.

|Difficulty|Description|
|---|---|
|mutual dependence|definitions are not independent|
|relevance dependence|variables depend on task distinctions|
|anti-modular pressure|cannot define concepts one by one|
|circularity risk|task and task variable constrain each other|
|intensional relation|“makes relevant” is not a simple attribute|

**Resolution.** *Mutual dependence* and *circularity risk* — "task variable" cannot be defined independently of "task", and vice versa — is the *co-definition* item of [legitimate mutual constraint vs. vicious circularity](_fleeting-ideas#^fleeting-mutual-constraint), which carries the tension with [t1-no-circular-reasoning](_framework-criteria#^t1-no-circular-reasoning) (a `[!missing]` callout is placed there) and with the [definition-normal-form](3-aspect-specific/ontology#^t3-definition-normal-form). *Anti-modular pressure* (the concepts cannot be defined one at a time) is what that candidate's co-definition construct addresses — a cluster of definitions co-authored, neither a stable placeholder for the other. *Intensional relation* ("makes relevant" is not a simple attribute) is a relation the closed vocabulary does not yet carry.

**General lesson** → propagated to [legitimate mutual constraint vs. vicious circularity](_fleeting-ideas#^fleeting-mutual-constraint). Two definitions can be *mutually dependent* — co-defined, neither prior — which the genus-differentia normal form does not accommodate and which must be distinguished from vicious circularity. The candidate proposes a co-definition construct: a cluster of definitions admitted together, the mutual constraint recorded and marked legitimate.

---

## 30. Statement where a term is intentionally overloaded

> The word “geometry” is useful here precisely because it can refer at once to metric relations, transformation structure, and the visual intuition that makes changes in representation intelligible.

|Difficulty|Description|
|---|---|
|productive ambiguity|overload is not an error|
|multiple semantic layers|metric, transformation, visual intuition|
|intentional non-disambiguation|ambiguity has cognitive value|
|anti-normalization pressure|forced splitting may lose meaning|
|pragmatic justification|usefulness depends on cognitive role|

**Resolution.** This example directly tests the framework against its own discipline. *Productive ambiguity* and *intentional non-disambiguation* — "geometry" is *deliberately* left meaning metric relations, transformation structure, and visual intuition at once — is, under the re-cut at [t3-definition-normal-form](3-aspect-specific/ontology#^t3-definition-normal-form), a candidate set with resolution policy `will-not-resolve`: distinct from `will-resolve` (awaiting resolution) and from a defect claim (a diagnosed pathology, example 22). The `[!missing]` callouts on [t1-canonical-terminology](_framework-criteria#^t1-canonical-terminology) and [t1-stable-boundaries](_framework-criteria#^t1-stable-boundaries) record that a `will-not-resolve` term must not be flagged by the canonicity check. *Pragmatic justification* (the overload is justified by its cognitive role) is the recorded rationale a `will-not-resolve` policy carries.

**General lesson** → propagated to [t3-definition-normal-form](3-aspect-specific/ontology#^t3-definition-normal-form) (the resolution-policy field), with `[!missing]` callouts on two criteria. The callout on [t1-canonical-terminology](_framework-criteria#^t1-canonical-terminology) records a genuine tension — the automatic canonicity check would flag a `will-not-resolve` term as drift, and must exempt it. The callout on [t1-stable-boundaries](_framework-criteria#^t1-stable-boundaries) is a *scoping clarification*, not a tension — a `will-not-resolve` content concept is not a violation of that criterion, which governs framework-component boundaries rather than content concepts. A term can be *intentionally and productively ambiguous* — the `will-not-resolve` resolution policy, distinct from `will-resolve` and from a defect claim. Recurs at example 40.

---

## 31. Qualitative theoretical conjecture with no clean predicate form

> Perhaps what matters is not whether the network has learned a representation of the context, but whether the context has become a principle according to which other variables are organized.

|Difficulty|Description|
|---|---|
|exploratory conjecture|marked by “perhaps”|
|question transformation|shifts object from representation to organization principle|
|abstract relation|context organizes other variables|
|no direct predicate|difficult to formalize without distortion|
|conceptual reframing|advances inquiry by changing focus|

**Resolution.** *Exploratory conjecture* ("perhaps what matters is...") is a low-maturity [epistemic status](2-architecture/object-kinds#^t2-epistemic-status) and a draft-profile [partial-formalization](_framework-criteria#^t1-partial-formalization) statement. *Question transformation* and *conceptual reframing* — the statement shifts the inquiry's object from "representation of context" to "context as an organizing principle" — is a reframing move on the question network, governed by [goal-driven reasoning](_framework-criteria#^t1-goal-driven-reasoning) and the [move vocabulary](_fleeting-ideas#^fleeting-move-vocabulary)'s `problematize`/reframe. *No direct predicate* — the conjecture resists formalization without distortion — is the [partial-formalization](_framework-criteria#^t1-partial-formalization) draft profile combined with [t1-rich-prose-expressivity](_framework-criteria#^t1-rich-prose-expressivity): a statement may stay at the prose maturity level precisely because forcing a predicate would distort it. *Abstract relation* ("context organizes other variables") is an intensional relation, like example 29's "makes relevant". **Covered** — the primary parts are ratified (`^t2-epistemic-status`, `^t1-goal-driven-reasoning`, `^t1-partial-formalization`, `^t1-rich-prose-expressivity`); the per-profile draft-vs-strict distinction is the open question `^t2-partial-formalization-profiles`. No new gap.

**General lesson** — none; no propagation. Confirms that an exploratory conjecture resisting clean predicate form is a legitimate low-maturity, prose-level statement under `^t1-partial-formalization` and `^t1-rich-prose-expressivity`, and that reframing the inquiry's object is a move on the question network. Reinforces intensional relations (ex. 29).

---

## 32. Ambiguous explanatory priority

> The task may explain the geometry, but the learned geometry may also explain which aspects of the task the network effectively treats as relevant.

|Difficulty|Description|
|---|---|
|bidirectional explanation|task explains geometry and geometry explains effective task|
|circular-looking relation|explanatory dependency is not strictly linear|
|distinction between task and effective task|objective task differs from network-internal task|
|explanatory priority unresolved|no direction is privileged|
|requires co-determination model|simple cause/effect relation is insufficient|

**Resolution.** *Bidirectional explanation* and *circular-looking relation* — the task explains the geometry and the geometry explains which aspects of the task are effectively treated as relevant — is the relation-grain counterpart of example 29's mutually dependent definitions. It tensions with [t1-no-circular-reasoning](_framework-criteria#^t1-no-circular-reasoning): a bidirectional explanatory dependency is not a vicious justification cycle, but the framework must distinguish the two. *Requires co-determination model* makes the point explicit — a simple directed `explains` edge is insufficient; the framework needs a co-determination relation. *Distinction between task and effective task* (the objective task vs. the network-internal task) is a `Distinction` object, and it is what *breaks the apparent circularity*: the two `explains` edges have different endpoints once task and effective-task are separated, so it is not strictly circular. **Partially covered**; surfaces co-determination as a relation type and confirms a `Distinction` can dissolve apparent circularity.

**General lesson** → propagated to [legitimate mutual constraint vs. vicious circularity](_fleeting-ideas#^fleeting-mutual-constraint). Two objects can stand in a *co-determination* relation — each explains an aspect of the other — which is not a vicious cycle; it is the relation-grain sibling of co-definition (ex. 29), now the candidate's second sub-item. A precise `Distinction` (task vs. effective task) often dissolves the apparent circularity by separating the endpoints.

---

## 33. Meta-theoretical claim about formalization

> Formalizing representation as an equivalence class may solve the problem of arbitrary coordinates, but it also risks erasing the very implementation details that make the representation mechanistically informative.

|Difficulty|Description|
|---|---|
|formalization trade-off|gains invariance, loses implementation detail|
|evaluates representation choice|statement concerns modelling formalism|
|risk rather than fact|modal caution|
|competing desiderata|coordinate-free versus mechanistic|
|anti-single-object pressure|representation has incompatible useful aspects|

**Resolution.** *Evaluates representation choice* — the statement is about whether to formalize representation as an equivalence class, a claim about the *modelling formalism* itself — is a meta-formal level-shift, the same level as examples 13 and 24. *Formalization trade-off* and *competing desiderata* (invariance vs. mechanistic detail) are an option-against-criteria comparison — the [QOC substructure](_fleeting-ideas#^fleeting-qoc-substructure), here with a *formalization choice* as the option. *Anti-single-object pressure* (representation has incompatible useful aspects, so no single formalization captures it) is the `cannot-resolve` value of the resolution-policy field at [t3-definition-normal-form](3-aspect-specific/ontology#^t3-definition-normal-form): the candidate set's plurality is forced by the object and is permanent. *Risk rather than fact* ("may erase" — modal caution) is the modal gap plus the cautionary category.

**Verdict.** Routed to an open question, not resolved. The `cannot-resolve` resolution policy is the right home, but it is a value in the `^t3-definition-normal-form` open question, not ratified machinery; this example contributes the case that motivates that value.

**General lesson** → propagated to [t3-definition-normal-form](3-aspect-specific/ontology#^t3-definition-normal-form) (resolution-policy field). A candidate set may have resolution policy `cannot-resolve` — no single formalization can unify its aspects, the plurality forced by the object — distinct from `will-resolve` (ex. 17, awaiting resolution) and `will-not-resolve` (ex. 30, plural by an authored choice).

---

## 34. Statement whose main content is a research constraint

> Any account of hierarchical build-up must explain not only why deeper layers are more abstract, but why the particular abstractions that emerge are those useful for the task.

|Difficulty|Description|
|---|---|
|adequacy constraint|imposes burden on theories|
|rejects weak explanation|abstraction alone is insufficient|
|teleological-looking language|“useful for the task” requires care|
|emergence requirement|process of abstraction matters|
|comparative scope|applies to any acceptable account|

**Resolution.** *Adequacy constraint* and *comparative scope* — the statement imposes a burden that *any acceptable account* of hierarchical build-up must meet — is a constraint on a class of theories, the same shape as example 25's constraint-on-a-definition, generalised from definitions to *explanatory accounts*. It feeds the validation operation of [t3-definition-normal-form](3-aspect-specific/ontology#^t3-definition-normal-form) generalised, and it is a [criterion](_fleeting-ideas#^fleeting-kind-set) object — an explicit standard of adequacy. *Rejects weak explanation* (abstraction alone is insufficient) is the negative half of the constraint. *Teleological-looking language* ("useful for the task") is flagged content: it reads as teleological and needs care — this is a content-quality concern the framework should mark, kin to the metaphor-diagnosis gap (a fragment flagged for a specific interpretive hazard). *Emergence requirement* (the *process* of abstraction matters, not just the end state) is the dynamic dimension of [t1-inquiry-content-and-progression](_framework-criteria#^t1-inquiry-content-and-progression). **Resolved via staged candidate** — the `Criterion` object is one of the staged `^fleeting-kind-set` kinds, and the constraint-on-accounts is the generalisation of example 25's constraint-on-a-definition; the teleological-phrasing flag is filed at the metalinguistic-content candidate.

**General lesson** → propagated to [meta-conceptual content](_fleeting-ideas#^fleeting-metalinguistic-content) (hazard-flagged fragment). A constraint on a *class of acceptable accounts* is a `Criterion` object, the generalisation of example 25's constraint-on-a-definition — nothing new there. The one filed item: teleological-looking phrasing ("useful for the task") is a fragment that may warrant a flag for an interpretive hazard, now the hazard-flagged-fragment item of the metalinguistic-content candidate, kin to metaphor diagnosis (ex. 4).

---

## 35. Ambiguous relation between model and phenomenon

> The model is not intended to describe biological attention, but to isolate a computational structure that biological attention might instantiate under some conditions.

|Difficulty|Description|
|---|---|
|non-representational model relation|model isolates structure, not phenomenon directly|
|possible instantiation|biological phenomenon may instantiate structure|
|scope limitation|not a biological description|
|conditional relevance|depends on future mapping|
|cross-domain bridge|computational and biological levels interact|

**Resolution.** *Non-representational model relation* — the model does not *describe* biological attention, it *isolates a computational structure* that biological attention *might instantiate* — together with *possible instantiation* and *conditional relevance* (the relevance depends on a future mapping not yet made) is the *bounded scope* index now filed at [the reified relation object](_fleeting-ideas#^fleeting-edge-scope), which names this example: a model-isolates-structure edge whose bound is modal ("may instantiate") and deferred ("pending a future mapping"). *Scope limitation* ("not a biological description") is a negative scope qualifier — an [undischarged-commitment](3-aspect-specific/arguments-reasoning#^t3-undischarged-commitments)-style explicit exclusion. *Cross-domain bridge* (computational and biological levels interact) is a cross-domain relation, kin to the explanation-level relations of example 13.

**General lesson** → propagated to [the reified relation object](_fleeting-ideas#^fleeting-edge-scope). A model can relate to a phenomenon by *isolating a structure the phenomenon may instantiate*, rather than by describing it — a hedged, conditional, cross-domain relation, carried as a bounded edge by the edge-scope candidate. Reinforces the bounded-edge index (ex. 12).

---

## 36. Claim that creates a new object by criticism

> The failure of the decoding criterion does not merely motivate a better criterion; it reveals that “criterion” itself is too narrow, since task-relevance may require a family of tests with different failure modes.

|Difficulty|Description|
|---|---|
|criticism creates new target|criterion becomes family of tests|
|meta-level revision|object type changes from single criterion to diagnostic ensemble|
|failure-mode reasoning|tests are characterized by how they fail|
|not simple refinement|changes the class of acceptable solutions|
|inquiry expansion|opens a new design space|

**Resolution.** *Criticism creates new target* and *meta-level revision* — the failure of the decoding criterion does not motivate a *better criterion*, it reveals that "criterion" itself is the wrong object type, which should be a *family of tests* — is the *critique-driven re-typing* variant recorded in the re-typing-as-a-move enrichment of the [move vocabulary](_fleeting-ideas#^fleeting-move-vocabulary): an [undercutter](3-aspect-specific/arguments-reasoning#^t3-attack-target) whose payload is not a defeated claim but a re-typing of the question's target object. *Failure-mode reasoning* (the tests in the family are characterized by *how they fail*) connects to the [reasoning-schemes](3-aspect-specific/arguments-reasoning#^t3-reasoning-schemes) critical-questions mechanism — a critical question is a named failure mode. *Not simple refinement* / *inquiry expansion* (the move changes the class of acceptable solutions, opening a design space) is a question-network restructuring move under [goal-driven reasoning](_framework-criteria#^t1-goal-driven-reasoning).

**General lesson** → propagated to [what an attack edge targets](3-aspect-specific/arguments-reasoning#^t3-attack-target). A critique can do more than defeat a claim or open a sub-question: it can *re-type the inquiry's target object* — an undercutter whose payload is an object re-typing, now recorded as the critique-driven re-typing pattern at `^t3-attack-target`.

---

## 37. Statement with implicit dependency on counterfactuals

> To say that a feature contributes to the task is to say something about what the computation would have been without it, but that counterfactual is meaningful only relative to an admissible way of removing the feature.

|Difficulty|Description|
|---|---|
|counterfactual semantics|contribution depends on unrealized condition|
|admissibility constraint|intervention type matters|
|definition and methodology intertwined|concept depends on test procedure|
|hidden causal model|“without it” requires causal structure|
|non-local meaning|meaning depends on external intervention family|

**Resolution.** *Counterfactual semantics* and *hidden causal model* — to say a feature contributes to the task is a claim about *what the computation would have been without it* — is the counterfactual-content item of the [statement-modality](_fleeting-ideas#^fleeting-statement-modality) candidate: a counterfactual is a claim about an unrealized condition, distinct from an asserted claim or a defeasible warrant. *Admissibility constraint* and *non-local meaning* (the counterfactual is meaningful only relative to an *admissible way of removing the feature*) is example 25's intervention-validity concern, now structural — and the candidate records that a counterfactual is meaningful only relative to an admissible intervention family. *Definition and methodology intertwined* (the concept of "contribution" depends on the test procedure) is the limit on the three-operation split now recorded as a `[!WARNING]` at [t3-definition-normal-form](3-aspect-specific/ontology#^t3-definition-normal-form): for constitutively procedure-bound concepts, definition and validation cannot be fully separated.

**General lesson** → propagated to [statement modality](_fleeting-ideas#^fleeting-statement-modality) (counterfactual content) and [t3-definition-normal-form](3-aspect-specific/ontology#^t3-definition-normal-form) (limit on the three-operation split). Counterfactual content is a distinct propositional construct, sharper than the modal-operators gap, meaningful only relative to an admissible intervention family. Separately: the three-operation split assumes normalize / complete / validate are separable, but some concepts are constitutively defined by their test procedure — a recorded limit on the split.

---

## 38. Statement where the same relation is descriptive and normative

> The paper treats invariance as a desirable property of the metric, but in the present project invariance is not merely desirable; it is part of what makes the metric interpretable.

|Difficulty|Description|
|---|---|
|source interpretation|describes another paper’s stance|
|local normative strengthening|project assigns stronger role|
|same property, different status|desirable versus constitutive|
|interpretability criterion|not purely mathematical|
|cross-context semantic shift|relation changes by project context|

**Resolution.** *Source interpretation* (the statement describes a paper's stance — invariance is *desirable* for that paper) is the source-interpretation content kind from example 15. *Same property, different status* and *local normative strengthening* — the same property, invariance, is *desirable* in the source and *constitutive* in the present project — is the [ontology-modularity](_fleeting-ideas#^fleeting-ontology-modularity) candidate applied not to a term's *meaning* but to a property's *modal status*: the status of a relation is module-local. *Cross-context semantic shift* makes this explicit — the relation's status shifts by project context, a [context-object](_fleeting-ideas#^fleeting-context-object) indexing. *Interpretability criterion* (invariance is part of what makes the metric interpretable — not a purely mathematical property) is the definitional-force / desideratum axis seen at examples 18 and 25. **Resolved via staged candidates** — ontology modularity, the context-object, and source-interpretation are all staged candidates; one sharpening — modularity scopes not just term meaning but a property's modal status.

**General lesson** — no separate propagation; a sharpening of two already-filed candidates. [Ontology modularity](_fleeting-ideas#^fleeting-ontology-modularity) localises not only what a term *means* but what *modal status* a property holds (desirable in one context, constitutive in another); the [context-object](_fleeting-ideas#^fleeting-context-object) candidate indexes this. Reinforces source-interpretation as a content kind (ex. 15, propagated to [content about sources](_fleeting-ideas#^fleeting-source-facing-content)).

---

## 39. Critique of a hidden assumption in a literature tradition

> Much of the literature assumes that if two representational spaces are aligned, then the corresponding systems share some internal organization, but this inference may conflate similarity of outputs with similarity of mechanisms.

|Difficulty|Description|
|---|---|
|generalized literature claim|no single source asserted|
|hidden assumption extraction|identifies implicit inference pattern|
|possible conflation|not categorical error, but risk|
|output-mechanism distinction|central but not explicitly formalized|
|tradition-level object|“much of the literature” is a diffuse source|

**Resolution.** *Hidden assumption extraction* — the statement extracts an implicit inference pattern that "much of the literature" relies on (alignment of representational spaces implies shared internal organization) — is an [undischarged-commitment](3-aspect-specific/arguments-reasoning#^t3-undischarged-commitments) attributed not to one statement but to a tradition, and the critique is an [undercutter](3-aspect-specific/arguments-reasoning#^t3-attack-target) against that inference pattern. *Possible conflation* (the inference is a *risk*, not a categorical error) is a hedged undercutter — its strength is partial, not categorical. *Tradition-level object* — "much of the literature" is a diffuse source, not a citable work — is the tradition-level-diffuse-source item now filed at [content about sources](_fleeting-ideas#^fleeting-source-facing-content). *Output-mechanism distinction* (central but unformalized) is a `Distinction` object at low maturity.

**General lesson** → propagated to [content about sources](_fleeting-ideas#^fleeting-source-facing-content). A critique may target an inference pattern attributed to a *tradition* — "much of the literature" — a diffuse, uncitable source distinct from the identifiable `Source` kind; the candidate records this as a diffuse-source object, exposition-adjacent and kin to the source-interpretation item (ex. 15).

---

## 40. Statement whose role is to preserve ambiguity

> For now, it is better to keep “representation geometry” deliberately ambiguous between metric structure and transformation structure, because deciding too early would force the analysis toward either comparison or dynamics.

|Difficulty|Description|
|---|---|
|deliberate ambiguity|ambiguity is a methodological choice|
|temporal scope|“for now” restricts the policy|
|competing futures|comparison versus dynamics|
|anti-resolution move|framework must preserve rather than solve ambiguity|
|metacognitive function|statement governs inquiry strategy|

**Resolution.** *Deliberate ambiguity* and *anti-resolution move* — "representation geometry" is kept deliberately ambiguous between metric structure and transformation structure — is, under the re-cut at [t3-definition-normal-form](3-aspect-specific/ontology#^t3-definition-normal-form), a candidate set with resolution policy `will-not-resolve`. *Temporal scope* ("for now") is the *time-bounded* sub-case the resolution-policy field records: `will-not-resolve` with a review date, the term held plural by policy with resolution deferred rather than refused, connecting to the [partial-formalization](_framework-criteria#^t1-partial-formalization) maturity axis. *Competing futures* (comparison vs. dynamics) is the candidate set itself. *Metacognitive function* (the statement governs inquiry strategy, it is not domain content) is the inquiry-steering item of [non-assertive statement categories](_fleeting-ideas#^fleeting-non-assertive-statements), which names this example.

**General lesson** → propagated to [t3-definition-normal-form](3-aspect-specific/ontology#^t3-definition-normal-form) (the resolution-policy field) and [non-assertive statement categories](_fleeting-ideas#^fleeting-non-assertive-statements). Ambiguity-preservation can be a *time-bounded policy* — a term held plural *for now* with a review date; the resolution-policy field records this as the time-bounded sub-case of `will-not-resolve`. The statement that sets such a policy is itself inquiry-steering content (ex. 20).

---

## Summary of adversarial patterns

|Pattern|Example difficulty|
|---|---|
|productive ambiguity|a term should remain unresolved because its ambiguity is heuristically useful|
|local stipulation|a term receives a project-specific meaning that conflicts with common usage|
|deferred definition|definition is intentionally postponed until constraints are clearer|
|mixed evidential status|one sentence contains support, uncertainty, and objection|
|source interpretation|claim concerns how a paper should be read|
|method-object entanglement|method partly constructs the object it appears to reveal|
|meta-formal critique|formalization changes what becomes visible|
|level-shift|same term changes meaning across computational, algorithmic, and implementation levels|
|concept pathology|a concept is diagnosed as misleading, overloaded, or structurally unstable|
|inquiry steering|statement does not assert content, but directs future reasoning|
|analogy with failure boundary|analogy is useful only under explicitly limited conditions|
|co-determination|two objects mutually shape each other rather than standing in one-way dependence|
|negative operationalization|a concept is approached by rejecting false operational criteria|
|absence-as-evidence warning|absence of expected marker does not establish absence of phenomenon|
|status-dependent relation|a relation changes meaning depending on whether a claim is tentative, accepted, rejected, or exploratory|
