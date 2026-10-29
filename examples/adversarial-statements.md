---
tags:
  - examples
index: "[Worked inquiries](examples/_index.md)"
aliases:
  - Adversarial statements
---
# Adversarial statements

These statements form a test set for the expressivity of three parts of `gnomon`: the concept record of the goal `vocabulary-records`, the framework of the goal `derivation-framework`, and the pilot of the goal `model-design`, all listed in the [project goals](../TODO.md). A part passes a statement when its records can state the statement without losing any feature that the table of the statement lists.

Each statement is a free-form sentence about neural representations or their interpretation. The statements were written to resist normalization into a simple definition, support, contrast or citation relation. Each table names the features that make its statement hard to formalize. The resolutions of these statements in the vocabulary of the retired design documentation, with their verdicts, remain in the git history at commit 9e138e2.

---

## 0. Definition by genus and differentia

**Statement.** "A feedforward network is a network where the flow of information is unidirectional." ^example-genus-differentia

**Normalized roles.** The statement is a definition with four components:

- *definiendum* — the concept `feedforward network`, the term being defined.
- *genus* — `feedforward network` is a subtype of `network`.
- *differentia attribute* — the attribute `flow of information`, an attribute of the genus.
- *differentia value* — the value `unidirectional`, which the differentia attribute takes.

**Difficulty.** The differentia references `network` and `flow of information`, which the records may not yet define. Requiring the researcher to define every referenced term first produces an infinite regress and overburdens authoring.

---

## 1. Definitions with unstable genus and implicit criterion shift

> A feedforward network is not merely a network without recurrence, but a computational regime in which the relevant causal dependencies can be represented as an acyclic order, provided that feedback-like effects introduced by training, normalization, or external control are not counted as part of the forward computation. ^example-definitions-with-unstable-genus-and-implicit-criterion-shift

| Difficulty              | Description                                                           |
| ----------------------- | --------------------------------------------------------------------- |
| unstable genus          | `feedforward network` shifts from object type to computational regime |
| negative definition     | “not merely” rejects an expected definition                           |
| hidden criterion        | recurrence is replaced by causal representability                     |
| boundary exclusion      | training, normalization, external control are excluded                |
| context-sensitive scope | “forward computation” is treated as a restricted temporal slice       |

---

## 2. Conceptual distinction that also revises the target concept

> The distinction between information being present in a representation and information being used by the system is not an additional refinement of representational analysis; it changes what should count as representation in the first place. ^example-conceptual-distinction-that-also-revises-the-target-concept

|Difficulty|Description|
|---|---|
|distinction-as-revision|the distinction modifies the concept it distinguishes|
|meta-conceptual move|the statement concerns the criteria for concept application|
|normative force|“should count” is not descriptive|
|target ambiguity|“representation” may mean data structure, neural state, or explanatory construct|

---

## 3. Argument with an undercutting condition hidden inside an example

> If a variable is linearly decodable from every hidden layer but ablating the subspace carrying it has no effect on the model’s behaviour, then the decodability result looks less like evidence of representation and more like evidence of redundant statistical alignment. ^example-argument-with-an-undercutting-condition-hidden-inside-an-example

|Difficulty|Description|
|---|---|
|hypothetical evidence|no concrete empirical result is asserted|
|comparative reinterpretation|one evidential role is displaced by another|
|implicit undercutter|decodability is weakened as evidence|
|latent alternative explanation|“redundant statistical alignment” introduces a competing construct|
|modal softness|“looks less like” avoids strict entailment|

---

## 4. Research question embedded in a critique

> The problem with asking whether a network “contains” a concept is that the question presupposes a container model of representation, whereas the more relevant issue may be whether the concept is stabilized across transformations that preserve the task. ^example-research-question-embedded-in-a-critique

|Difficulty|Description|
|---|---|
|question critique|the statement attacks the framing of a question|
|metaphor diagnosis|“container model” is a conceptual metaphor, not a formal claim|
|alternative inquiry|a replacement question is introduced|
|task-relative criterion|“preserve the task” is itself theoretically loaded|
|soft modality|“may be” marks tentative redirection|

---

## 5. Definition by refusal of inadequate operationalizations

> Task-relevance cannot be identified with decodability, causal effect, or mutual information alone, because each captures a different shadow of the relation between a representation and a task. ^example-definition-by-refusal-of-inadequate-operationalizations

|Difficulty|Description|
|---|---|
|negative triangulation|concept is defined by rejecting several approximations|
|metaphorical content|“shadow” is meaningful but non-literal|
|plural partial adequacy|rejected criteria are not simply false|
|missing positive definition|no direct criterion is supplied|
|relation reification|“relation between representation and task” becomes the true object|

---

## 6. Claim whose force depends on disciplinary perspective

> In neuroscience, calling a feature “represented” often means that it is recoverable from activity; in mechanistic interpretability, the same word is misleading unless the feature participates in the computation. ^example-claim-whose-force-depends-on-disciplinary-perspective

|Difficulty|Description|
|---|---|
|discipline-relative semantics|same term has different standards across fields|
|no global definition|neither use is declared universally correct|
|pragmatic evaluation|“misleading” is not a truth-functional predicate|
|implicit contrast|recoverability versus participation|
|sociolinguistic content|the statement describes scientific usage norms|

---

## 7. Derivation whose conclusion is a changed viewpoint

> Once the context variable is treated not as an input feature but as an instruction selecting a task, the apparent geometry of the representation should no longer be interpreted as encoding a larger stimulus space, but as implementing a family of conditional coordinate systems. ^example-derivation-whose-conclusion-is-a-changed-viewpoint

|Difficulty|Description|
|---|---|
|reclassification of object|context variable becomes instruction|
|interpretation shift|geometry receives a new explanatory role|
|negative and positive reading|one interpretation is rejected, another introduced|
|metaphorical-formal hybrid|“conditional coordinate systems” is both suggestive and technical|
|dependency on modelling choice|conclusion depends on how context is treated|

---

## 8. Argument where the warrant is methodological rather than propositional

> The reason to compare representational geometries across contexts is not that geometry is the final object of interest, but that geometry is the least arbitrary level at which global transformations can be made visible without committing to a particular decoder. ^example-argument-where-the-warrant-is-methodological-rather-than-propositional

|Difficulty|Description|
|---|---|
|methodological justification|argues for an analysis strategy|
|non-finality|the chosen object is instrumental, not ultimate|
|comparative criterion|“least arbitrary” is a methodological value judgment|
|implicit alternatives|decoders are rejected without being enumerated|
|visualization role|“made visible” mixes cognition, method, and explanation|

---

## 9. Statement that introduces an explanatory gap rather than a claim

> Even if two contexts produce separable manifolds, it remains unclear whether this separation is the mechanism by which the network solves the task or merely the geometric trace of some lower-level routing process. ^example-statement-that-introduces-an-explanatory-gap-rather-than-a-claim

|Difficulty|Description|
|---|---|
|uncertainty as content|the main object is an unresolved ambiguity|
|alternative explanations|mechanism versus trace|
|same observation, different roles|separability can be causal or epiphenomenal|
|hidden demand|asks for criteria distinguishing mechanism from trace|
|non-assertive structure|the statement advances inquiry by suspending commitment|

---

## 10. Conceptual move that changes granularity

> What appears as one representation at the layer level may decompose into several task-specific sub-representations once the computation is analysed along paths rather than units. ^example-conceptual-move-that-changes-granularity

|Difficulty|Description|
|---|---|
|scale dependence|representation depends on analysis granularity|
|perspective-dependent ontology|layer-level versus path-level entities|
|modal re-description|“may decompose” is exploratory|
|implicit methodological intervention|path analysis changes the ontology|
|object instability|“one representation” may not survive refinement|

---

## 11. Claim with locally scoped technical vocabulary

> In this project, “attention” should not mean a learned weighting mechanism in the transformer sense, but any context-dependent deformation of representational geometry that selectively increases task-relevant separability. ^example-claim-with-locally-scoped-technical-vocabulary

|Difficulty|Description|
|---|---|
|local stipulation|term meaning is project-specific|
|exclusion of standard meaning|transformer attention is explicitly rejected|
|functional redefinition|attention becomes a geometric operation|
|normative terminology|“should not mean” is a methodological stipulation|
|composite criterion|deformation, selectivity, task relevance, separability|

---

## 12. Argument whose premise is an analogy with restricted scope

> The analogy with eigenvectors is useful only insofar as both aim to identify intrinsic directions of transformation; it becomes misleading as soon as one forgets that neural representations need not be governed by a linear operator with stable invariant subspaces. ^example-argument-whose-premise-is-an-analogy-with-restricted-scope

|Difficulty|Description|
|---|---|
|bounded analogy|analogy has explicit scope and failure condition|
|mixed support and warning|the analogy is both useful and dangerous|
|technical disanalogy|linear operators and neural representations differ structurally|
|condition on misuse|problem arises from a forgotten assumption|
|no simple relation|not just `analogous_to` or `not_analogous_to`|

---

## 13. A claim whose truth depends on the level of explanation

> At the computational level, the task demands an invariant decision rule; at the algorithmic level, the network may implement this through equivariant intermediate representations rather than invariant ones. ^example-a-claim-whose-truth-depends-on-the-level-of-explanation

|Difficulty|Description|
|---|---|
|multi-level structure|Marr-level distinction is essential|
|apparent contradiction|invariant task rule versus equivariant representations|
|explanatory compatibility|distinct claims coexist at different levels|
|modality|“may implement” is not categorical|
|relation between levels|implementation relation is central but implicit|

---

## 14. Open-ended inquiry move disguised as a conclusion

> The failure of pairwise similarity measures is therefore not merely empirical; it suggests that the object being compared has been underspecified. ^example-open-ended-inquiry-move-disguised-as-a-conclusion

|Difficulty|Description|
|---|---|
|conclusion opens problem|result generates a new object-level question|
|empirical-to-conceptual shift|failure of method diagnoses underspecified object|
|hidden presupposition|comparison requires a defined object of comparison|
|non-deductive inference|“suggests” expresses abductive movement|
|underspecification target|unclear whether object is representation, geometry, context, or task|

---

## 15. Source-sensitive claim with interpretive uncertainty

> Saxe et al. seem to treat learning dynamics as revealing the structure of the task through singular modes, but it is not obvious whether this should be read as a claim about representations themselves or about the input-output map implemented by the whole network. ^example-source-sensitive-claim-with-interpretive-uncertainty

|Difficulty|Description|
|---|---|
|uncertain attribution|“seem to treat” avoids direct citation commitment|
|interpretive ambiguity|two readings of a source are possible|
|source-sensitive meaning|claim concerns what an author means|
|theory-object ambiguity|representations versus global map|
|requires hermeneutic tracking|interpretation may later be revised|

---

## 16. Claim involving partial formalization and residual intuition

> The covariance recursion gives a precise handle on how correlations propagate, but the sense in which this constitutes an explanation of representation formation remains partly metaphorical unless the relevant task variables are identified inside the recursion. ^example-claim-involving-partial-formalization-and-residual-intuition

|Difficulty|Description|
|---|---|
|formal tool with interpretive gap|mathematics exists but explanatory status is unclear|
|partial adequacy|recursion is useful but insufficient|
|metaphor diagnosis|“explanation” may be only metaphorical|
|missing bridge|task variables must be identified in formal dynamics|
|layered evaluation|precision and understanding are separated|

---

## 17. Statement with deferred object identity

> The same “representation” may be the activity vector, the subspace spanned by task-relevant variation, the equivalence class under readout-preserving transformations, or the causal role played in the computation. ^example-statement-with-deferred-object-identity

|Difficulty|Description|
|---|---|
|term fragmentation|one term maps to multiple candidate objects|
|no chosen resolution|alternatives remain open|
|different ontological types|vector, subspace, equivalence class, causal role|
|formalization-sensitive identity|object identity depends on modelling choice|
|not merely ambiguity|each candidate may be scientifically legitimate|

---

## 18. Conceptual critique with implicit desiderata

> A metric that changes under arbitrary reparameterizations of the hidden layer may still be statistically informative, but it cannot serve as an intrinsic characterization of the network’s computation. ^example-conceptual-critique-with-implicit-desiderata

|Difficulty|Description|
|---|---|
|dual evaluation|statistically useful but theoretically inadequate|
|implicit desideratum|intrinsic characterization requires invariance|
|contrast between goals|information versus characterization|
|hidden formal property|reparameterization invariance is not spelled out|
|normative methodological claim|“cannot serve” depends on research aim|

---

## 19. Claim where context changes the type of the object

> When the cue is treated as a context, the representation is a family indexed by tasks; when the cue is treated as a stimulus, the representation is a single geometry over an enlarged input space. ^example-claim-where-context-changes-the-type-of-the-object

|Difficulty|Description|
|---|---|
|modelling choice changes object type|family versus single geometry|
|same data, different ontology|cue receives different role|
|indexical structure|context induces task-indexed representation|
|no empirical difference necessarily|distinction may be conceptual|
|formalization fork|later analyses diverge from this choice|

---

## 20. Research move involving strategic non-definition

> It may be premature to define task-relevance directly; instead, the inquiry should first isolate the transformations under which any acceptable definition must remain invariant. ^example-research-move-involving-strategic-non-definition

|Difficulty|Description|
|---|---|
|intentional deferral|definition is postponed deliberately|
|meta-criterion first|invariance constraints precede definition|
|inquiry strategy|statement directs research process|
|non-object-level content|concerns order of investigation|
|negative operationality|defines what not to do yet|

---

## 21. Boundary case as concept probe

> A neuron that carries task information only because it is correlated with another genuinely causal feature is precisely the kind of case that forces the difference between encoding and use to become explicit. ^example-boundary-case-as-concept-probe

|Difficulty|Description|
|---|---|
|boundary case|example tests a conceptual distinction|
|indirect information|information arises through correlation|
|causal asymmetry|causal feature differs from correlated carrier|
|case-as-method|example is used to force clarification|
|latent classification problem|neuron may encode without being used|

---

## 22. Statement whose content is a failure mode of a concept

> The danger of “representation” is that it can name either the structure that explains the computation or merely the structure that an external observer can recover from the system. ^example-statement-whose-content-is-a-failure-mode-of-a-concept

|Difficulty|Description|
|---|---|
|concept pathology|statement diagnoses a problematic ambiguity|
|observer-relative content|one reading depends on external recovery|
|explanatory contrast|explanation versus recoverability|
|warning rather than claim|function is cautionary|
|non-standard object|“danger of a concept” is itself a research object|

---

## 23. Mixed epistemic status within a single statement

> It is plausible, though not yet demonstrated, that the context-dependent rotation observed in the hidden space reflects a learned gating mechanism rather than a mere change in decoding basis. ^example-mixed-epistemic-status-within-a-single-statement

|Difficulty|Description|
|---|---|
|explicit uncertainty|plausible but undemonstrated|
|observation-to-mechanism inference|geometric observation suggests mechanism|
|competing explanation|gating mechanism versus decoding basis|
|evidential weakness|not yet demonstrated|
|modality is local|uncertainty applies to one inferential link, not all terms|

---

## 24. Derivation with a hidden change of representation language

> Rewriting the network function as a sum over paths makes some distributed effects look local, but only because locality has been moved from units to paths. ^example-derivation-with-a-hidden-change-of-representation-language

|Difficulty|Description|
|---|---|
|representation-language shift|path expansion changes explanatory vocabulary|
|apparent simplification|distributed becomes local|
|hidden cost|locality is relocated, not discovered|
|meta-representational claim|concerns effect of formalism itself|
|conceptual caution|warns against reifying the new representation|

---

## 25. Statement introducing a comparative adequacy criterion

> A useful notion of task-relevance should reject both features that are merely decodable and features that are causally active only under interventions that destroy the computation being studied. ^example-statement-introducing-a-comparative-adequacy-criterion

|Difficulty|Description|
|---|---|
|desideratum for definition|not a definition, but a constraint on one|
|two-sided exclusion|rejects two different false positives|
|intervention validity|some causal tests are methodologically invalid|
|dependence on “computation being studied”|target process must be fixed|
|normativity|“useful notion should reject” is evaluative|

---

## 26. Statement where a method produces the object it measures

> A clustering analysis of representations may reveal task-relevant groups, but it may also impose the very discreteness that later appears as evidence for those groups. ^example-statement-where-a-method-produces-the-object-it-measures

|Difficulty|Description|
|---|---|
|method-object circularity|method may construct the observed object|
|epistemic contamination|evidence depends on analysis procedure|
|ambiguous outcome|reveal versus impose|
|reflexive critique|method affects interpretation of its result|
|no simple support/attack|same method is useful and suspect|

---

## 27. Claim with temporal evolution and conceptual instability

> Early in training, the network may encode context as an auxiliary feature; later, the same context may become the organizing principle of the representation space. ^example-claim-with-temporal-evolution-and-conceptual-instability

|Difficulty|Description|
|---|---|
|diachronic change|role changes over training|
|same object changes type|auxiliary feature becomes organizing principle|
|non-static relation|relation between context and representation evolves|
|developmental explanation|learning trajectory matters|
|vague transition|no precise boundary between stages|

---

## 28. Statement using absence as evidence

> The absence of a clean context axis does not show that context is absent from the representation; it may show that context acts by deforming the whole space rather than occupying a separable direction. ^example-statement-using-absence-as-evidence

|Difficulty|Description|
|---|---|
|negative evidence|absence of marker does not imply absence of phenomenon|
|alternative mode of presence|axis versus deformation|
|measurement critique|detectable form differs from actual form|
|implicit model of representation|separable direction versus global transformation|
|epistemic caution|prevents false negative inference|

---

## 29. Conceptual dependence between two definitions

> The definition of “task variable” cannot be fixed independently of the definition of “task,” because what counts as a variable depends on which distinctions the task itself makes relevant. ^example-conceptual-dependence-between-two-definitions

|Difficulty|Description|
|---|---|
|mutual dependence|definitions are not independent|
|relevance dependence|variables depend on task distinctions|
|anti-modular pressure|cannot define concepts one by one|
|circularity risk|task and task variable constrain each other|
|intensional relation|“makes relevant” is not a simple attribute|

---

## 30. Statement where a term is intentionally overloaded

> The word “geometry” is useful here precisely because it can refer at once to metric relations, transformation structure, and the visual intuition that makes changes in representation intelligible. ^example-statement-where-a-term-is-intentionally-overloaded

|Difficulty|Description|
|---|---|
|productive ambiguity|overload is not an error|
|multiple semantic layers|metric, transformation, visual intuition|
|intentional non-disambiguation|ambiguity has cognitive value|
|anti-normalization pressure|forced splitting may lose meaning|
|pragmatic justification|usefulness depends on cognitive role|

---

## 31. Qualitative theoretical conjecture with no clean predicate form

> Perhaps what matters is not whether the network has learned a representation of the context, but whether the context has become a principle according to which other variables are organized. ^example-qualitative-theoretical-conjecture-with-no-clean-predicate-form

|Difficulty|Description|
|---|---|
|exploratory conjecture|marked by “perhaps”|
|question transformation|shifts object from representation to organization principle|
|abstract relation|context organizes other variables|
|no direct predicate|difficult to formalize without distortion|
|conceptual reframing|advances inquiry by changing focus|

---

## 32. Ambiguous explanatory priority

> The task may explain the geometry, but the learned geometry may also explain which aspects of the task the network effectively treats as relevant. ^example-ambiguous-explanatory-priority

|Difficulty|Description|
|---|---|
|bidirectional explanation|task explains geometry and geometry explains effective task|
|circular-looking relation|explanatory dependency is not strictly linear|
|distinction between task and effective task|objective task differs from network-internal task|
|explanatory priority unresolved|no direction is privileged|
|requires co-determination model|simple cause/effect relation is insufficient|

---

## 33. Meta-theoretical claim about formalization

> Formalizing representation as an equivalence class may solve the problem of arbitrary coordinates, but it also risks erasing the very implementation details that make the representation mechanistically informative. ^example-meta-theoretical-claim-about-formalization

|Difficulty|Description|
|---|---|
|formalization trade-off|gains invariance, loses implementation detail|
|evaluates representation choice|statement concerns modelling formalism|
|risk rather than fact|modal caution|
|competing desiderata|coordinate-free versus mechanistic|
|anti-single-object pressure|representation has incompatible useful aspects|

---

## 34. Statement whose main content is a research constraint

> Any account of hierarchical build-up must explain not only why deeper layers are more abstract, but why the particular abstractions that emerge are those useful for the task. ^example-statement-whose-main-content-is-a-research-constraint

|Difficulty|Description|
|---|---|
|adequacy constraint|imposes burden on theories|
|rejects weak explanation|abstraction alone is insufficient|
|teleological-looking language|“useful for the task” requires care|
|emergence requirement|process of abstraction matters|
|comparative scope|applies to any acceptable account|

---

## 35. Ambiguous relation between model and phenomenon

> The model is not intended to describe biological attention, but to isolate a computational structure that biological attention might instantiate under some conditions. ^example-ambiguous-relation-between-model-and-phenomenon

|Difficulty|Description|
|---|---|
|non-representational model relation|model isolates structure, not phenomenon directly|
|possible instantiation|biological phenomenon may instantiate structure|
|scope limitation|not a biological description|
|conditional relevance|depends on future mapping|
|cross-domain bridge|computational and biological levels interact|

---

## 36. Claim that creates a new object by criticism

> The failure of the decoding criterion does not merely motivate a better criterion; it reveals that “criterion” itself is too narrow, since task-relevance may require a family of tests with different failure modes. ^example-claim-that-creates-a-new-object-by-criticism

|Difficulty|Description|
|---|---|
|criticism creates new target|criterion becomes family of tests|
|meta-level revision|object type changes from single criterion to diagnostic ensemble|
|failure-mode reasoning|tests are characterized by how they fail|
|not simple refinement|changes the class of acceptable solutions|
|inquiry expansion|opens a new design space|

---

## 37. Statement with implicit dependency on counterfactuals

> To say that a feature contributes to the task is to say something about what the computation would have been without it, but that counterfactual is meaningful only relative to an admissible way of removing the feature. ^example-statement-with-implicit-dependency-on-counterfactuals

|Difficulty|Description|
|---|---|
|counterfactual semantics|contribution depends on unrealized condition|
|admissibility constraint|intervention type matters|
|definition and methodology intertwined|concept depends on test procedure|
|hidden causal model|“without it” requires causal structure|
|non-local meaning|meaning depends on external intervention family|

---

## 38. Statement where the same relation is descriptive and normative

> The paper treats invariance as a desirable property of the metric, but in the present project invariance is not merely desirable; it is part of what makes the metric interpretable. ^example-statement-where-the-same-relation-is-descriptive-and-normative

|Difficulty|Description|
|---|---|
|source interpretation|describes another paper’s stance|
|local normative strengthening|project assigns stronger role|
|same property, different status|desirable versus constitutive|
|interpretability criterion|not purely mathematical|
|cross-context semantic shift|relation changes by project context|

---

## 39. Critique of a hidden assumption in a literature tradition

> Much of the literature assumes that if two representational spaces are aligned, then the corresponding systems share some internal organization, but this inference may conflate similarity of outputs with similarity of mechanisms. ^example-critique-of-a-hidden-assumption-in-a-literature-tradition

|Difficulty|Description|
|---|---|
|generalized literature claim|no single source asserted|
|hidden assumption extraction|identifies implicit inference pattern|
|possible conflation|not categorical error, but risk|
|output-mechanism distinction|central but not explicitly formalized|
|tradition-level object|“much of the literature” is a diffuse source|

---

## 40. Statement whose role is to preserve ambiguity

> For now, it is better to keep “representation geometry” deliberately ambiguous between metric structure and transformation structure, because deciding too early would force the analysis toward either comparison or dynamics. ^example-statement-whose-role-is-to-preserve-ambiguity

|Difficulty|Description|
|---|---|
|deliberate ambiguity|ambiguity is a methodological choice|
|temporal scope|“for now” restricts the policy|
|competing futures|comparison versus dynamics|
|anti-resolution move|framework must preserve rather than solve ambiguity|
|metacognitive function|statement governs inquiry strategy|

---

## Summary of adversarial patterns

The patterns below recur across the statements. Each row names one pattern and the difficulty that it creates for a formalization.

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
