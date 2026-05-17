# Arguments and reasoning

> [!INFO] Tier and source
> **Tier 3 (per aspect).** Stub file. Holds criteria that constrain the structure and quality of argumentative reasoning (assemblies relative to a target and their internal moves). Traces to [t1-intelligibility](../1-framework/reasoning-integrity#^t1-justification-levels), [t1-non-arbitrary](../1-framework/reasoning-integrity#^t1-served-goal), [t2-revision-semantics](vendor/gnomon/docs/design/2-architecture/constraints#^t2-revision-semantics), and what an assembly may contain under [promotion of assembly-local records](vendor/gnomon/docs/design/2-architecture/reasoning-structure#^t2-assembly-record-promotion).

---

> [!INFO] Machinery, not criteria
> This file holds the **implementing machinery** for the *Reasoning integrity* theme: for each justification level of [recoverable reasoning](../1-framework/reasoning-integrity#^t1-justification-levels) and its sub-criterion facets, a concrete design question about *how* the facet is realised. The facets state the *goals* at Tier 1; the entries below ask, per facet, what objects, fields, relations, or validator rules implement that goal. An entry is a **decision** when a mechanism is already chosen, an **open question** otherwise. The four open questions at the end (reusable schemes, attack-target, undischarged commitments, mutual constraint) predate this machinery section and are kept as authored.

---

## Decisions

### Warrant completeness rule ^t3-d-warrant-completeness

> [!QUESTION] What validator rule enforces that every derived claim carries a warrant?

Implements the [adequate-justification facet](../1-framework/reasoning-integrity#^t1-vl-justification-adequacy) of *valid licensing*, at the completeness grain.

**Chosen rule.** Every derived claim has at least one incoming `supports` edge, and that edge carries an explicit warrant. A derived claim with no warranted `supports` edge is a build-time validation error. This is the structural minimum; whether the warrant's support is *sufficient* and its premises *legitimate* is the separate open question [warrant adequacy](#^t3-d-warrant-adequacy).

### Cycle detection with mutual-constraint exemption ^t3-d-cycle-detection

> [!QUESTION] What validator rule detects a circular justification, and how does it exempt a legitimate mutual constraint?

Implements the [no-circular-reasoning facet](../1-framework/reasoning-integrity#^t1-vl-no-circular) of *valid licensing*.

**Chosen rule.** Within a reasoning snapshot, the dependency graph (`depends_on`, `supports`, and the sub-goal hierarchy) must be a directed acyclic graph; a cycle is a hard build-time error, realising [the snapshot dependency graph is a DAG](vendor/gnomon/docs/design/2-architecture/constraints#^t2-snapshot-dag). The rule must **exempt** structures marked as a legitimate mutual constraint — co-definition or co-determination — rather than flag them; how that exemption is expressed is the open question [vicious cycle versus legitimate mutual constraint](#^t3-mutual-constraint).

---

## Open questions

The machinery questions below are grouped by the justification level whose sub-criterion facets they implement. Each asks how a facet's *goal* is realised in objects, fields, relations, or validator rules.

### Licensing-level machinery

#### Assumption-discharge mechanism ^t3-assumption-discharge-mechanism

> [!QUESTION] How does the framework handle an assumed node — discharge it, absorb it, or flag it as residue?

Implements the [no-silent-incompleteness facet](../1-framework/reasoning-integrity#^t1-vl-no-silent) of *valid licensing*. Every assumed node must be accounted for: detection of a silently incomplete reasoning depends on the framework tracking which assumptions remain open. Three candidate paths for an assumed node:

- **Eliminate by downstream proof** — a later step discharges the assumption, which is then no longer open.
- **Absorb into the conclusion** — the assumption is promoted to a stated hypothesis the conclusion is explicitly conditional on.
- **Flag as unresolved residue** — the assumption stays open and is surfaced as epistemic debt.

Resolution must state which paths the framework admits, how an assumed node records its discharge status, and how the validator distinguishes a discharged assumption from an undischarged one. The closely related question of presuppositions a *statement* carries is [undischarged commitments of a statement](#^t3-undischarged-commitments).

#### Warrant adequacy ^t3-d-warrant-adequacy

> [!QUESTION] How are support sufficiency, premise legitimacy, and rebuttal pre-emption recorded and checked?

Implements the [adequate-justification facet](../1-framework/reasoning-integrity#^t1-vl-justification-adequacy) of *valid licensing*, beyond the completeness minimum of [warrant completeness](#^t3-d-warrant-completeness). A warrant may be present yet inadequate — its support insufficient for the strength claimed, its premises not themselves legitimate to use, or salient objections left unaddressed. Resolution must state what a warrant records so adequacy is checkable: how support strength is represented, how premise legitimacy is established (and whether legitimacy is itself a recorded status), and how pre-empted objections attach to a warrant. It connects to the warrant-generality question [warrant generality](#^t3-d-warrant-generality): a warrant stated at the wrong generality cannot be assessed for adequacy.

#### Warrant generality ^t3-d-warrant-generality

> [!QUESTION] How is a warrant recorded at a generality that is neither too specific to reuse nor too generic to be informative?

Implements the [adequate-justification facet](../1-framework/reasoning-integrity#^t1-vl-justification-adequacy) of *valid licensing*. A warrant stated too specifically cannot license any step but the one it was written for; stated too generically it asserts nothing checkable. Resolution must state how the framework records a warrant's generality, and whether reusable warrants are factored out as named [reasoning schemes](#^t3-reasoning-schemes) (whose warrant template is the general bridge principle).

#### Warrant-kind boundary rule ^t3-d-warrant-boundary

> [!QUESTION] When a step under one warrant kind supports a step under another, how does the downstream step inherit strength and defeat conditions?

Implements the [warrant-composition facet](../1-framework/reasoning-integrity#^t1-vl-warrant-composition) of *valid licensing*. At a warrant-kind boundary — a monotonic step supporting a defeasible one, or the reverse — the downstream step's strength and defeat conditions are not self-evident. Resolution must state the inheritance rule; it is shared with the validity-revision theme's boundary-rule decision and with [defeasibility and regime stratification](vendor/gnomon/docs/design/2-architecture/constraints#^t2-defeasibility).

#### Commitment-calibration check ^t3-d-commitment-calibration

> [!QUESTION] What validator rule checks that a conclusion's modal status matches the support recorded for it?

Implements the [calibrated-commitment facet](../1-framework/reasoning-integrity#^t1-vl-calibrated-commitment) of *valid licensing*. The modal-strength vocabulary — possible, plausible, supported, established, necessary — is the [epistemic status](vendor/gnomon/docs/design/2-architecture/object-kinds#^t2-epistemic-status) decision; this question is the *check* that the status claimed is proportional to the support marshalled. Resolution must state how support strength is compared against claimed status, and what the validator does on a mismatch (an overclaimed conclusion propagates its overclaim downstream, so a mismatch is a licensing error, not a style note).

#### Defeater record ^t3-d-defeater-record

> [!QUESTION] What field records the defeaters a reasoning faces and how each is handled?

Implements the [acknowledged-limitations facet](../1-framework/reasoning-integrity#^t1-vl-acknowledged-limits) of *valid licensing*, for the externally-facing half — the objections a reasoning is exposed to. A reasoning on defeasible warrants may be sufficient against its stated premises yet fragile under objections it never names. Resolution must state what records each major defeater and its disposition — rebutted, accommodated, or accepted as a residual risk — and how this connects to the attack edges of [what an attack edge targets](#^t3-attack-target).

#### Limitation disclosure ^t3-d-limitation-disclosure

> [!QUESTION] What records a reasoning's stated limitations, unresolved tensions, and fairly-reconstructed rejected alternatives?

Implements the [acknowledged-limitations facet](../1-framework/reasoning-integrity#^t1-vl-acknowledged-limits) of *valid licensing*, for the self-disclosure half — distinct from the defeater record above, which concerns external objections. A reasoning that hides its open tensions, or reconstructs a rejected position as a straw target, appears more settled than it is. Resolution must state what records a limitation or unresolved tension, and what discipline governs the fair reconstruction of a set-aside alternative (representing it at its strongest).

### Teleological-level machinery

#### Gap-tree well-foundedness check ^t3-d-gap-tree-check

> [!QUESTION] What validator rule checks the gap tree is well-founded, rooted at the principal gap, with no idle steps?

Implements the [gap-rooted-move facet](../1-framework/reasoning-integrity#^t1-sg-gap-rooted) of *served goal*. Every move either decomposes a gap into sub-gaps or advances the resolution of one; the resulting tree must be well-founded and rooted at the principal gap, with no explanatorily idle step. Resolution must state the validator rule that detects an idle step (a move serving no gap) and a mis-rooted or non-well-founded tree.

#### Gap-decomposition record ^t3-d-gap-decomposition

> [!QUESTION] How does the framework record, per sub-gap, its success and admissibility conditions?

Implements two facets of *served goal* — [stated success conditions](../1-framework/reasoning-integrity#^t1-sg-success-conditions) and [stated admissibility conditions](../1-framework/reasoning-integrity#^t1-sg-admissibility) — which share one mechanism: the record attached to each sub-gap. Success conditions state what would count as resolving the sub-gap; admissibility conditions state what licenses it as a legitimate decomposition of its parent. Resolution must state the field set each sub-gap carries, and how the validator checks a sub-gap that has one without the other. The form a gap itself takes — question, problem, goal — is the [gap-form taxonomy](vendor/gnomon/docs/design/3-aspect-specific/ontology#^t3-epistemic-gap-subtypes).

### Strategic-level machinery

#### Rationale and rejected-alternative record ^t3-d-rationale-record

> [!QUESTION] What strategic-annotation fields record a move's rationale and the alternatives it rejected?

Implements the [recorded-rationale facet](../1-framework/reasoning-integrity#^t1-as-rationale) of *apt strategy*. A move's rationale states why this route advances the gap and why it was chosen over the alternatives; a rationale that names no rejected alternative is uninformative, and at a branch point with multiple admissible routes the chosen route must record at least one rejected alternative. Resolution must state the strategic-annotation field set — connecting to the [reasoning-annotation field set](vendor/gnomon/docs/design/3-aspect-specific/reasoning-fields) — and the validator rule that flags a non-contrastive rationale or a hidden branch choice.

#### Idle-unit detection ^t3-d-idle-unit-detection

> [!QUESTION] What validator rule detects an inferentially idle unit within a reasoning?

Implements the [local-necessity facet](../1-framework/reasoning-integrity#^t1-as-local-necessity) of *apt strategy*. Once the objective is fixed, every premise, step, and concept must be genuinely used to reach the conclusion. Resolution must state how the validator establishes that a unit contributes nothing — e.g. that no path from the unit reaches the conclusion in the dependency graph — distinct from corpus-grain [non-redundancy](../1-framework/modular-content-organization#^t1-non-redundancy).

#### Route-directness measure ^t3-d-directness-measure

> [!QUESTION] How is an avoidable detour operationally defined and detected?

Implements the [direct-route facet](../1-framework/reasoning-integrity#^t1-as-directness) of *apt strategy*. A reasoning may reach its conclusion through avoidable intermediate constructions that obscure the load-bearing steps. Resolution must state what counts as a detour operationally — a measure over the dependency graph, a comparison against a shorter admissible route, or an authored judgement — and whether directness is checked or only advised.

### Explanatory-level machinery

#### Conceptual-effect field ^t3-d-conceptual-effect

> [!QUESTION] What field records the cognitive gain — the conceptual effect — a step contributes?

Implements the [recoverable-gain facet](../1-framework/reasoning-integrity#^t1-eg-gain-recorded) of *explanatory gain*. Every non-trivial step has a conceptual effect — what it transforms, into what, and why — that must be recorded and recoverable, and that must go beyond restating the gap addressed. Resolution must state the field that records the effect; the catalogue of gain kinds it may take is the [explanatory-gain enum](vendor/gnomon/docs/design/3-aspect-specific/reasoning-fields#^t3-gain-kind-enum).

#### Dependence-network exposure ^t3-d-dependence-network

> [!QUESTION] What relation set exposes a reasoning's dependence, modal, and structural network?

Implements the [exposed-dependence-network facet](../1-framework/reasoning-integrity#^t1-eg-dependence-network) of *explanatory gain*. The reasoning must make explicit what supports what, what explains what, what would change what. This is the content requirement that the relational structure be authored; the tooling to query it once authored is [relational queryability](../1-framework/modular-content-organization#^t1-relational-queryability). Resolution must state which relations carry the dependence, modal, and structural links — connecting to the [typed relation vocabulary](vendor/gnomon/docs/design/2-architecture/relations-graph#^t2-typed-relation-vocabulary).

#### Mechanism and difference-maker fields ^t3-d-explanatory-depth

> [!QUESTION] What fields record the generating mechanism and the difference-making properties of a result?

Implements two facets of *explanatory gain* — [mechanism extraction](../1-framework/reasoning-integrity#^t1-eg-how-mechanism-extraction) (the *how*) and [counterfactual sensitivity](../1-framework/reasoning-integrity#^t1-eg-why-counterfactual-sensitivity) (the *why*) — which share the explanatory-depth machinery. Mechanism extraction records the causal or structural mechanism whose operation generates the result; counterfactual sensitivity records the difference-making characteristic properties and what would have to change for the conclusion to fail. Resolution must state the field set for each, recognising that mechanism extraction is the harder of the two.

> [!NOTE] Symmetry and invariance as explanation forms
> The forms explanatory depth can take include cause or mechanism, structure or nomology, and symmetry or invariance. Symmetry explanation is often a special case of structural, mathematical, or nomological explanation: it explains by showing that certain distinctions cannot matter because the theory is invariant under transformations that erase them. Invariance is broader than symmetry — a symmetry is usually an invariance under a group of transformations, but invariance can also concern interventions, changes of scale, reparameterizations, coordinate transformations, or background conditions. In Woodward-style causal explanation, invariance under interventions distinguishes stable explanatory generalizations from accidental ones. The catalogue of these forms is the [explanatory-gain enum](vendor/gnomon/docs/design/3-aspect-specific/reasoning-fields#^t3-gain-kind-enum).

#### Unification construct ^t3-d-unification

> [!QUESTION] What construct records that one principle explains many cases?

Implements the [unification facet](../1-framework/reasoning-integrity#^t1-eg-unification) of *explanatory gain*. Where a unifying principle genuinely exists, the reasoning extracts a deeper structure — a small number of principles — that explains many cases rather than treating each separately. Resolution must state what records the unifying principle and its instances; a candidate vehicle is a named [reasoning scheme](#^t3-reasoning-schemes), whose warrant template is the shared principle.

### Manipulability-level machinery

#### Strategic-hierarchy and compressed-essence structure ^t3-d-strategic-hierarchy

> [!QUESTION] What structure records the global-to-local strategic hierarchy and a compressed essence of the reasoning?

Implements the [compression-and-reconstruction facet](../1-framework/reasoning-integrity#^t1-mr-compression-reconstruction) of *manipulable reasoning*. A reader reconstructs the strategy from scratch only if the reasoning is organised from global structure to local derivation rather than as a flat chain. Two distinct hierarchies must be recorded: a **structural hierarchy** (overview down to detailed derivation) and a **relevance hierarchy** (core determinants distinguished from peripheral detail — connecting to the relevance-vocabulary theme). Resolution must state the structure that carries both, and the compressed-essence representation that summarises the argument by strategic blocks.

#### Pattern-transfer machinery ^t3-d-pattern-transfer

> [!QUESTION] What machinery supports extracting a strategic pattern, recognising it in nearby cases, and varying it?

Implements the [transfer facet](../1-framework/reasoning-integrity#^t1-mr-transfer) of *manipulable reasoning*. Transfer is concretely supported when three conditions hold:

- **Pattern extraction.** The strategy is separable from its specific content — the move sequence and its rationale lift out as a pattern with content slots to refill. The framework's vehicle for an extracted pattern is a reusable scheme; see [reusable reasoning schemes](#^t3-reasoning-schemes).
- **Cross-case recognition.** The pattern is stated generally enough that a reader recognises it in a nearby problem with different content but the same strategic shape.
- **Stability under variation.** The pattern survives perturbation — it continues to apply when premises, parameters, or the domain vary within a stated range.

Resolution must state the machinery for each. The third connects to the counterfactual-sensitivity facet of explanatory depth: isolating the difference-makers tells a reader which variations the pattern tolerates.

#### Weak-point surfacing ^t3-d-weak-point-surfacing

> [!QUESTION] What machinery surfaces a reasoning's weak points for a reader?

Implements the [diagnosis facet](../1-framework/reasoning-integrity#^t1-mr-diagnosis) of *manipulable reasoning*. A reader must be able to locate what is weak — unanswered questions, loosely supported claims, narrow or specific results, restrictive conditions. Resolution must state what makes these locatable: a derived diagnostic view, status fields read off the graph, or a dedicated audit projection. It consumes the records produced by [limitation disclosure](#^t3-d-limitation-disclosure) and [defeater record](#^t3-d-defeater-record).

#### Comparison and analogy record ^t3-d-comparison-analogy

> [!QUESTION] What records the comparisons and analogies a reasoning uses to clarify its concepts and results?

Implements the [comparison-and-analogy facet](../1-framework/reasoning-integrity#^t1-mr-contrast) of *manipulable reasoning*. A reasoning clarifies by identifying similarities and distinctions between cases, and by mapping its patterns onto domains the reader already commands. Resolution must state what records a comparison (the cases contrasted and the distinguishing property) and an analogy (the source domain and the structural mapping).

#### Worked-example link ^t3-d-worked-example

> [!QUESTION] What links a reasoning to the worked examples that instantiate it?

Implements the [concrete-illustration facet](../1-framework/reasoning-integrity#^t1-mr-illustration) of *manipulable reasoning*. A reasoning exposes its structure through worked examples that instantiate the general pattern on a specific case — the anchor that lets a reader reconstruct the abstract pattern. Resolution must state the relation linking a reasoning to its instantiating examples. (Analogies, which map a pattern onto a familiar domain, are recorded by [comparison and analogy](#^t3-d-comparison-analogy), not here.)

#### Misconception record ^t3-d-misconception

> [!QUESTION] What records the misconceptions a reasoning anticipates and the counter-examples that correct them?

Implements the [misconception facet](../1-framework/reasoning-integrity#^t1-mr-misconception) of *manipulable reasoning*. A reasoning anticipates the naive models and predictable misreadings a reader brings, and supplies the counter-examples and clarifications that correct them. Resolution must state what records an anticipated misconception and its corrective; the corrective is often a contrast, so this connects to [comparison and analogy](#^t3-d-comparison-analogy).

---

## Open questions — argumentation structure

The four open questions below predate the machinery section above and concern the structure of argumentation objects rather than a single justification-level facet.

### Reusable reasoning schemes ^t3-reasoning-schemes

> [!QUESTION] Does the framework admit named, reusable reasoning schemes as a content kind, separate from individual filled arguments?

A reasoning scheme is a reusable template for a recurring form of defeasible reasoning, drawn from Walton-style argumentation-scheme theory. A scheme separates a general reasoning pattern from the specific content inserted into it, and so directly addresses the generalizable-versus-context-specific tension: the scheme is reusable, the filled slots preserve local content.

A scheme carries four parts:

- **Slots** — the context-specific propositions a use of the scheme must fill.
- **Warrant template** — the general bridge principle the scheme licenses, stated with slot variables.
- **Critical questions** — a systematic stress test attached to the scheme; each question probes a way the scheme can fail.
- **Applicability conditions** — when the scheme is a legitimate move.

Candidate schemes for a research framework: argument from analogy (transfer a structure across domains), argument from sign (infer latent structure from an observable marker), argument from expert opinion (use literature authority under source constraints), causal argument, argument from consequences, argument from classification, methodological argument (justify a method or analysis-strategy choice — "use this analysis because it is the least arbitrary level" — rather than a propositional inference; the worked-example suite, example 8, surfaces this as a distinct argument target the five-level justification model does not cover).

A use of a scheme is a separate object — a scheme instance — pairing the scheme with its slot values, local qualifiers, and local defeaters.

Bears on [t2-operation-primitiveness](vendor/gnomon/docs/design/2-architecture/operations-and-modes#^t2-operation-primitiveness): a scheme is one candidate form an operation schema can take. Bears on [served goal](../1-framework/reasoning-integrity#^t1-served-goal): the critical questions of a scheme are a source of admissible sub-gaps. Staged inputs and the broader paradigm survey are in [_fleeting-ideas](vendor/gnomon/docs/design/_fleeting-ideas#^fleeting-move-vocabulary).

> [!WARNING] Editable templates, not fixed labels
> A scheme is a template authors edit, extend, and instantiate, not a closed taxonomic label. Treating schemes as a fixed category set would make them classificatory rather than productive.

### What an attack edge targets ^t3-attack-target

> [!QUESTION] When one object attacks another, does the framework record what the attack targets — the conclusion, or the inference that reaches it?

Structured-argumentation practice (ASPIC+) distinguishes two attack kinds that a single `attacks` edge conflates:

- **Rebuttal** — an attack on a *conclusion*: a competing object asserts the negation or a defeater of the target's claim.
- **Undercutter** — an attack on an *inference*: the attacker grants the grounds but denies that the warrant licenses the step from grounds to conclusion.

The distinction is sharper than a generic disagreement edge. Many research conflicts are not contradictions between conclusions; the attack targets a method, an operationalisation, an analogy, or an interpretive bridge. A worked instance: linear decodability of a variable from a representation is offered as grounds that the variable is represented; the undercutter grants the decodability but denies the warrant connecting decodability to representational use — it targets the inference, not the conclusion.

A third attack target is the **framing of a question**: a critique that the question itself presupposes something illegitimate. The worked-example suite (example 4) gives the instance — asking whether a network "contains" a concept presupposes a container model of representation; the critique attacks neither a conclusion nor an inference but the presupposition built into the question. This target kind connects to [discharge accounting for assumptions](#^t3-undischarged-commitments): the presupposition a question carries is an undischarged commitment, and a framing-attack surfaces it. The attack-target vocabulary should therefore admit a third value — an attack on a `Question`'s framing — alongside rebuttal and undercutter.

**Method-result circularity** is a specific undercutter worth recording as a recurring pattern. The worked-example suite (example 26) gives the instance — a clustering analysis may *reveal* task-relevant groups, or may *impose* the very discreteness that later appears as evidence for those groups. The critique grants the result but attacks the inference from result to conclusion, by noting that the method partly constructed the object it then measured. This is not a justification cycle (nothing in the recorded chain returns to itself) and not a mutual constraint; it is an undercutter whose ground is the method-object relation. The framework should record when a result is method-dependent in a way that undercuts its evidential force.

**Critique-driven re-typing** is a further undercutter pattern (worked-example suite, example 36). A critique can do more than defeat a claim: it can re-type the inquiry's *target object* — the failure of a decoding criterion reveals that "an acceptable criterion" is the wrong object kind, and the target should instead be "a family of tests characterized by their failure modes". The undercutter's payload is not a defeated conclusion but a re-typing of what the question is about. This is distinct from a modelling-choice re-typing (which is a branch point whose rejected alternative is recorded per the [rationale and rejected-alternative record](#^t3-d-rationale-record)) and from a process-trajectory re-typing (a temporal fact about the phenomenon): only the critique-driven case is an attack edge, and it belongs here.

Bears on [t2-typed-relation-vocabulary](vendor/gnomon/docs/design/2-architecture/relations-graph#^t2-typed-relation-vocabulary): the relation vocabulary either carries distinct `rebuts`, `undercuts`, and framing-attack labels, or a single `attacks` label with a target-discriminator field. The acceptance-set computation that structured argumentation builds on these edges is out of scope per [t1-no-runtime-inference](vendor/gnomon/docs/design/1-framework/external-interfaces#^t1-no-runtime-inference); only the authored, typed edges are in scope.

### Undischarged commitments of a statement ^t3-undischarged-commitments

> [!QUESTION] How does the framework record the propositional commitments a statement leans on but does not assert — and how strong is each?

A statement carries commitments beyond the content it asserts. A definition that references undefined terms presupposes background propositions: that the genus is a meaningful concept, that the genus can bear the differentia attribute, that the attribute admits the stated value. These presuppositions are not errors. They are **deferred obligations** — epistemic debt the statement incurs and the framework should track rather than silently absorb. This bears on the no-silent-incompleteness facet of [valid licensing](../1-framework/reasoning-integrity#^t1-valid-licensing): an undischarged presupposition is exactly the kind of hidden dependency that silent-incompleteness detection must surface. The discharge of such obligations is governed by the same mechanism as assumption discharge — see [t3-assumption-discharge-mechanism](#^t3-assumption-discharge-mechanism) once that decision is drafted.

Three refinements distinguish what a statement commits to:

- **Presuppositions as first-class objects, with priority.** Each presupposition records its content, the statement that incurred it, its role, its resolution status, and a priority. Priority lets the framework defer low-urgency obligations (a value term awaiting a directionality concept) without losing them, while flagging high-urgency ones (an undefined genus).
- **Three strengths of commitment.** A statement's use of a term is weaker than the background structure it presupposes, which is weaker than a global axiom. "Term Z functions here as an attribute of Y" (a *local role*) is weaker than "the definition presupposes Y can bear attribute Z" (a *provisional commitment*), which is weaker than "every Y bears attribute Z" (a *global ontology axiom*). Promotion from a weaker to a stronger commitment is explicit, never automatic. Bears on [t2-epistemic-status](vendor/gnomon/docs/design/2-architecture/object-kinds#^t2-epistemic-status).
- **Definitional force.** A statement of the form "an X is a Y where Z is W" may carry a necessary condition, a sufficient condition, a biconditional definition, or an informal characterisation. Scientific prose rarely marks which. The normalized object records definitional force as an explicit, possibly uncertain value rather than silently committing to the strongest reading. Bears on [t1-partial-formalization](../1-framework/expressive-depth#^t1-partial-formalization).

Bearing criteria: [valid licensing](../1-framework/reasoning-integrity#^t1-valid-licensing) (no-silent-incompleteness facet), [t1-partial-formalization](../1-framework/expressive-depth#^t1-partial-formalization), [t2-epistemic-status](vendor/gnomon/docs/design/2-architecture/object-kinds#^t2-epistemic-status).

The motivating worked example and the companion definition-structure refinements are recorded at [normalized definition form](vendor/gnomon/docs/design/3-aspect-specific/ontology#^t3-definition-normal-form) and [_worked-examples](vendor/gnomon/docs/design/_worked-examples#^example-genus-differentia).

### Vicious cycle versus legitimate mutual constraint ^t3-mutual-constraint

> [!QUESTION] How does the cycle-detection machinery distinguish a vicious justification cycle from a legitimate mutual constraint between definitions or between explanatory relations?

The no-circular-reasoning facet of [valid licensing](../1-framework/reasoning-integrity#^t1-valid-licensing) forbids a justification chain that ultimately rests on itself, and the [cycle-detection rule](#^t3-d-cycle-detection) flags any cycle in the snapshot graph as a hard error. But not every cycle is vicious. Two structures look circular without forming a closed loop in a *justification* chain:

- **Co-definition** — two definitions are mutually dependent: "task variable" cannot be fixed independently of "task", since what counts as a variable depends on which distinctions the task makes relevant ([conceptual dependence between two definitions](vendor/gnomon/docs/design/_worked-examples#^example-conceptual-dependence-between-two-definitions)). Neither is prior; they must be co-authored. This is a definition-structure concern — see [normalized definition form](ontology#^t3-definition-normal-form), whose forward-reference placeholders assume one definiendum per template.
- **Co-determination** — two objects each explain an aspect of the other: the task explains the geometry, and the geometry explains which aspects of the task are effectively treated as relevant ([ambiguous explanatory priority](vendor/gnomon/docs/design/_worked-examples#^example-ambiguous-explanatory-priority)). A simple directed `explains` edge cannot capture this.

A staged candidate is recorded at [legitimate mutual constraint](vendor/gnomon/docs/design/_fleeting-ideas#^fleeting-mutual-constraint): a co-definition construct (a cluster of definitions admitted together, the mutual constraint recorded and marked legitimate) and a co-determination relation. It also notes that a precise `Distinction` (task vs. effective task) often dissolves the apparent circularity by separating the endpoints, so the two edges no longer share both ends. Resolution must state the rule the cycle check applies to tell a vicious cycle from a marked mutual constraint, and whether the co-definition construct and co-determination relation enter the [typed relation vocabulary](vendor/gnomon/docs/design/2-architecture/relations-graph#^t2-typed-relation-vocabulary).

Bearing criteria: [valid licensing](../1-framework/reasoning-integrity#^t1-valid-licensing) (no-circular-reasoning facet).
