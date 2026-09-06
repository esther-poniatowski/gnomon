---
tags:
  - criteria
index: "[Framework-level criteria](_index.md)"
aliases:
  - Reasoning integrity (criteria)
---
# Reasoning integrity — Framework-level criteria

## Justification levels ^t1-justification-levels

Reasoning yields **genuine understanding**, not merely formal validity. Downstream readers can recover *why* the inquiry advanced, not only *that* it did.

The framework makes reasoning recoverable by linking five levels of justification within every reasoning:

| Level              | Question answered                                      | Determined by                                                                                                                                       | Examples                                                                                                       |
| ------------------ | ------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| **Licensing**      | Why is the move *valid*, under which *warrant*?        | The acceptability conditions of the operation itself: its **support** and the **inferential pattern** it relies on                                  | a deduction is valid; a statistical inference is significant                                                   |
| **Teleological**   | Which *goal* does this move serve?                     | The **epistemic gap** (what is lacking or blocked), associated with a *question* and/or *objective* (the local goal introduced to address that gap) | the move targets an unresolved sub-question; it addresses a blocking obstacle                                  |
| **Strategic**      | Why is this transformation *appropriate* to that goal? | The **rationale**: why this move, among the available ones, advances the objective                                                                  | the move dissects the gap into tractable parts; it isolates the decisive condition                             |
| **Explanatory**    | Why does this move improve *understanding*?            | The **epistemic gain**: the mechanism revealed, the contrast exposed, the "why"/"how" answered                                                      | it identifies the characteristic property that is essential to the proof, an underlying invariant or structure |
| **Manipulability** | How can the reasoning be *leveraged* now?              | The **operations affordances** the move enables: reconstruction, contrast, compression, transfer, diagnosis                                         | the strategy can be reconstructed; the pattern can be transferred to another problem                           |

**Independence of the levels.** These levels are mutually independent, in the sense that no level determines another. Therefore, each must be representable on its own.

*Examples*: A deductive move can address any kind of gap; a case-split can be licensed deductively, abductively, or heuristically.

> [!hint] Authoritative sources
> This decomposition draws on:
> - Toulmin's _claim–data–warrant–backing_ architecture
> - van Fraassen's analysis of _why-questions relative to contrast classes_
> - Polya's heuristic theory, the proof-strategic layer
> - Detlefsen's and Steiner's analyses of mathematical explanation: a proof that _convinces_ is not equivalent to a proof that _explains_, conviction follows from formal derivability while explanation requires that the inferential moves be grounded in the _distinguishing properties_ of the objects under consideration, and that the global structure be recoverable from local annotations.

**Failure mode prevented.** A formalism that records only licensing (formal validity) reduces research reasoning to proof-checking and silently drops the teleological, strategic, explanatory, and manipulability levels that distinguish a research artefact from a verified script.

> [!info] Criterion scope
> The five levels **constrain the structural ontology** (objects and relations) that the framework must provide. Selecting the object kinds and relations that encode each level is a downstream Tier-2/3 decision.

**Upstream dependencies.**

- [Inquiry content and progression](framework-foundations#^t1-inquiry-content-and-progression) (parent criterion): the justification-level model is the epistemic-axis specialisation of capturing genuine reasoning.

**Downstream consequences.**

[Justification levels](#^t1-justification-levels) is the overarching criterion for *Reasoning integrity*. Each of its five justification levels has exactly one sub-criterion stating that level's general desideratum:

- [Valid licensing](#^t1-valid-licensing) — *Licensing* level.
- [Served goal](#^t1-served-goal) — *Teleological* level.
- [Apt strategy](#^t1-apt-strategy) — *Strategic* level.
- [Explanatory gain](#^t1-explanatory-gain) — *Explanatory* level.
- [Manipulable reasoning](#^t1-manipulable-reasoning) — *Manipulability* level.

Two further downstream consequences:

- Per-level encoding decisions (in the reasoning-structure theme): how each of the five levels is recorded.
- Justificatory-level placement (decision in the reasoning-structure theme): where each level is recorded — on the move itself or on the recruiting context.
- [Partial formalization](expressive-depth#^t1-partial-formalization) (tension per `^t2-x2`): deeper formalization improves recoverability of reasoning at the cost of authoring overhead.

> [!info] Sections below
> For each justification level, a sub-criterion states the general desideratum for that level, and its facets name the specific conditions that must be met to satisfy it. Each facet is checkable by validators and realised by a Tier-2/3 machinery. The sub-criterion and its facets are stated in terms of the justification level's own concepts (e.g. "warrant", "goal", "rationale", "epistemic gain", "affordance") rather than the machinery that implements it, so that the criterion remains stable even if the machinery evolves.

## Valid licensing ^t1-valid-licensing

Every reasoning move is **validly licensed**: it rests on a warrant whose support and inferential pattern make the move acceptable, and the licensing chain as a whole is well-formed.

- **No circular reasoning** ^t1-vl-no-circular
  A step's justification must not *ultimately rest on itself*. Tracing the licensing chain from any step must not return to that step.
  *Implementing machinery*: [the snapshot dependency graph is a DAG](2-architecture/relations-graph#^t2-snapshot-dag-property) (Tier-2 decision) and [cycle-detection rule](3-aspect-specific/arguments-reasoning#^t3-d-cycle-detection) (Tier-3 machinery decision).

- **No silent incompleteness** ^t1-vl-no-silent
  A chain and its conclusion must not secretly depend on an unstated hypothesis or an undischarged assumption; the licensing must explicitly account for which assumptions remain open.
  *Implementing machinery*: [assumption-discharge mechanism](3-aspect-specific/arguments-reasoning#^t3-assumption-discharge-mechanism) (Tier-3 machinery open question).

- **Adequate justification** ^t1-vl-justification-adequacy
  Each move is backed by a **warrant**: its support is sufficient for the strength claimed, its premises are themselves legitimate to use, and salient objections to it are pre-empted.
  *Implementing machinery*: the [warrant-completeness rule](3-aspect-specific/arguments-reasoning#^t3-d-warrant-completeness) (Tier-3 machinery decision) and [warrant adequacy](3-aspect-specific/arguments-reasoning#^t3-d-warrant-adequacy) (Tier-3 machinery open question).

- **Composition of warrant kinds** ^t1-vl-warrant-composition
  A chain may combine steps governed by warrants of different kinds: *monotonic* (proof-theoretic) warrants license steps valid regardless of the state of the inquiry, defeasible only by revision of the warrant itself; *defeasible* (argumentation-theoretic) warrants license steps valid only under the current state, defeatable by new content. The warrant kind of a step must be explicit, so that a downstream consumer can determine whether the step's conclusion is retractable. Whenever a step of one kind supports a step of the other (a "warrant-kind boundary"), the licensing must specify how the downstream step inherits the upstream step's strength and defeat conditions.
   *Implementing machinery*: [warrant-kind annotation on support relations](2-architecture/validity-revision#^t2-warrant-annotation) (Tier-2 decision) and the warrant-kind boundary rule in the validity-revision theme.

- **Calibrated commitment** ^t1-vl-calibrated-commitment
  The modal strength attached to a conclusion (possible, plausible, supported, established, necessary) matches is the support actually marshalled for it.
  *Implementing machinery*: [epistemic status](2-architecture/object-kinds#^t2-epistemic-status) (Tier-2 decision) and the status vocabulary; the proportionality requirement itself is the open theme-local criterion the [commitment-calibration check](3-aspect-specific/arguments-reasoning#^t3-d-commitment-calibration).

- **Acknowledged limitations** ^t1-vl-acknowledged-limits
  The reasoning explicitly states its own limitations and unresolved tensions. When the reasoning relies on *defeasible* warrants, it explicitly records the major defeaters it is exposed to and how each is handled: rebutted, accommodated, or accepted as a residual risk.
  *Implementing machinery*: the [defeater record](3-aspect-specific/arguments-reasoning#^t3-d-defeater-record) and [limitation disclosure](3-aspect-specific/arguments-reasoning#^t3-d-limitation-disclosure) (Tier-3 machinery open questions).

**Failures mode prevented.** A formalism that records a move's *result* without its warrant may accept invalid moves. It cannot guarantee that the recorded reasoning actually supports its conclusions, and it cannot be used to identify and correct errors in the reasoning.

**Upstream dependencies.**

- [Justification levels](#^t1-justification-levels) (parent criterion): valid licensing is the *Licensing*-level sub-criterion.
- [Inquiry content and progression](framework-foundations#^t1-inquiry-content-and-progression) (cross-group ancestor criterion in *Framework foundation*): an unlicensed or circularly-licensed move falsifies the representation.
- [Reasoning-types coverage](expressive-depth#^t1-reasoning-types-coverage) (cross-group ancestor criterion in *Expressive depth*): without multiple warrant kinds there is no warrant-kind boundary to govern.

**Downstream consequences.** One further consequence is not facet-specific:

- [Revision accountability](research-activities-workflows#^t1-revision-accountability) (tension per `^t2-x4`): revision history is cyclic, whereas the no-circular-reasoning facet requires the snapshot graph to remain acyclic; the resolution is the snapshot-vs-history slicing.

> [!NOTE] Not every cycle is vicious
> The requirement of [no circular reasoning](#^t1-vl-no-circular) must distinguish a vicious justification cycle from a legitimate mutual constraint — co-definition between two definitions, or co-determination between two explanatory relations — which looks circular without closing a loop in a *justification* chain. How the cycle-detection machinery draws that distinction is the open question [vicious cycle versus legitimate mutual constraint](3-aspect-specific/arguments-reasoning#^t3-mutual-constraint).

## Served goal ^t1-served-goal

Every reasoning move **serves a stated epistemic gap**: whatever the inquiry currently *lacks* or is *blocked* by.

> [!note]
> The epistemic gap can be formulated either by:
> - a **question** to be answered,
> - a **problem** to be solved,
> - a **goal** to be achieved.

- **Gap-rooted move** ^t1-sg-gap-rooted
  Every move explicitly names the epistemic gap it serves. Every move either decomposes a gap into sub-gaps or advances the resolution of one.
  *Implementing machinery*: the gap-decomposition mechanism (Tier-2 reasoning-structure decision) and the [gap-tree well-foundedness check](3-aspect-specific/arguments-reasoning#^t3-d-gap-tree-check) (Tier-3 machinery open question), which requires the gap tree to be well-founded and rooted at the principal gap.

- **Stated success conditions** ^t1-sg-success-conditions
  Each gap carries success conditions: what would count as resolving it, what resolved state must obtain.
  *Implementing machinery*: the gap-decomposition mechanism records each sub-gap's success conditions; [inquiry-format](workflows#^t3-inquiry-format) (Tier-3 workflows decision) presents the resolved gap-network.

- **Stated admissibility conditions** ^t1-sg-admissibility
  Each sub-gap carries admissibility conditions: what licenses it as a legitimate decomposition of its *parent*.
  *Implementing machinery*: the gap-decomposition mechanism (Tier-2 reasoning-structure decision) records each sub-gap's admissibility conditions alongside its success conditions.

Together, the success and admissibility conditions yield a **coherent tree of epistemic gaps** in which every gap is anchored to a parent and every move is licensed as either an apt decomposition of a gap or an apt step toward the success conditions of one.

> [!NOTE] Criterion scope
> The [taxonomy of epistemic-gaps](3-aspect-specific/ontology#^t3-epistemic-gap-subtypes) is a Tier-3 decision. Each type of gap form motivates the object kinds and the operation library the framework must admit.

**Failure modes prevented.** A reasoning that proceeds by *topical association* — each step is *about* the same subject as the parent gap — appears to be goal-directed yet produces a conclusion with no identifiable connection to the inquiry. Results accumulate without a clear path from the initial gap to the final result. Without success and admissibility conditions, it is not possible to check whether an argument actually settled the gap it claims to serve.

**Upstream dependencies.**

- [Justification levels](#^t1-justification-levels) (parent criterion): served goal is the *Teleological*-level sub-criterion.

**Downstream consequences.** Two further consequences are not facet-specific:

- [Gap-form taxonomy](3-aspect-specific/ontology#^t3-epistemic-gap-subtypes) (open decision in the ontology theme): the forms an epistemic gap can take, and the object kinds and operations each form motivates.
- [Inquiry-scope](workflows#^t3-inquiry-scope) (decision in the workflows theme): how the target gap of an inquiry is stated and bounded.

## Apt strategy ^t1-apt-strategy

Every reasoning move effectively **serves its declared objective**: the transformation it performs must be appropriate and relevant toward that gap.

- **Recorded rationale** ^t1-as-rationale
  Every move carries a rationale stating why this route advances the gap's resolution, and why it is selected among the available alternatives.
  *Implementing machinery*: the motivation-encoding specification (Tier-2 reasoning-fields decision); the [rationale and rejected-alternative record](3-aspect-specific/arguments-reasoning#^t3-d-rationale-record) (Tier-3 machinery open question), requiring the rationale to name a contrastive choice.

- **Local necessity** ^t1-as-local-necessity
  In a reasoning chain, every included unit (e.g. premise, step, concept) is *effectively used* to reach the conclusion.
  *Implementing machinery*: the [idle-unit detection rule](3-aspect-specific/arguments-reasoning#^t3-d-idle-unit-detection) (Tier-3 machinery open question).

- **Direct route** ^t1-as-directness
  The reasoning reaches its conclusion by a direct route, without introducing detours or unnecessary intermediate constructions.
  *Implementing machinery*: the [route-directness measure](3-aspect-specific/arguments-reasoning#^t3-d-directness-measure) (Tier-3 machinery open question), requiring no avoidable detour.

**Failure mode prevented.** A move may serve a real gap yet be inapt — it carries idle units, detours, or avoidable complexity that obscures the load-bearing steps. Such a move is not only inefficient, it fails to clarify the structure of the inquiry and thus hinders further progress.

**Upstream dependencies.**

- [Justification levels](#^t1-justification-levels) (parent criterion): apt strategy is the *Strategic*-level sub-criterion.
- [Served goal](#^t1-served-goal) (peer sub-criterion): a rationale is apt *relative to* the gap the move serves; aptness presupposes that a gap is named.

**Downstream consequences.** One further consequence is not facet-specific:

- [Partial formalization](expressive-depth#^t1-partial-formalization) (tension per `^t2-x2`): full annotation of every move's rationale and every sub-gap's admissibility conditions is heavy; partial annotation profiles trade depth for ergonomics.

## Explanatory gain ^t1-explanatory-gain

Every reasoning yields **cognitive gains** that increase intelligibility and understanding of the inquiry.

- **Recoverable gain** ^t1-eg-gain-recorded
  Every reasoning chain records the gain it contributes. This gain must go *beyond* restating the gap addressed; it should yield additional insights or implications about the whole inquiry. For example, a move that dissects a gap into two sub-gaps reveals a structural case distinction which is not already stated by the gap itself, and which could be exploited by further moves. Unlike the previous levels, the criterion applies to a reasoning *chain*, rather than being strictly required for *each move* in isolation — some moves may be purely strategic or manipulative.
  *Implementing machinery*: the [explanatory-gain enum](3-aspect-specific/reasoning-fields#^t3-gain-kind-enum) (Tier-3 reasoning-fields decision) names the kinds of gain a move can record.

- **Exposed dependence network** ^t1-eg-dependence-network
  The reasoning makes explicit how its components (assumptions, definitions, intermediate claims, conclusions) are connected: which claims support which conclusions, which mechanisms explain which effects, which assumptions are necessary or sufficient for which results.
  *Implementing machinery*: the [dependence-network exposure](3-aspect-specific/arguments-reasoning#^t3-d-dependence-network) (Tier-3 machinery open question).

- **Counterfactual sensitivity (why)** ^t1-eg-why-counterfactual-sensitivity
  The gain addresses *why* the result holds by isolating the *load-bearing factors*: which characteristic properties the result depends on, and what would have to change for it to fail.

- **Mechanism extraction (how)** ^t1-eg-how-mechanism-extraction
  The reasoning gain addresses *how* the result holds by extracting the *causal or structural mechanism*: the components and relations whose interaction generates the result. This is the harder requirement: a reasoning may correctly identify what the result depends on without exhibiting the mechanism that produces it.
  *Implementing machinery*: the [mechanism and difference-maker fields](3-aspect-specific/arguments-reasoning#^t3-d-explanatory-depth) (Tier-3 machinery open question), with mechanism extraction and counterfactual sensitivity as its two sub-aspects.

- **Unification** ^t1-eg-unification
  Where a unifying principle genuinely exists, the gain extracts a deeper structure (a small number of principles) that explains many cases, rather than treating each separately.
  *Implementing machinery*: the [unification construct](3-aspect-specific/arguments-reasoning#^t3-d-unification) (Tier-3 machinery open question).

**Failure modes prevented.** A reasoning can be valid and goal-directed yet explanatorily inert — each move advances the argument without the reader ever grasping *why* the conclusion holds or *how* it is generated.

**Upstream dependencies.**

- [Justification levels](#^t1-justification-levels) (parent criterion): explanatory gain is the *Explanatory*-level sub-criterion.
- [Apt strategy](#^t1-apt-strategy) (peer sub-criterion): the gain a move yields is distinct from, and must exceed, the strategic objective that motivated it.

**Downstream consequences.** No further non-facet consequence.

## Manipulable reasoning ^t1-manipulable-reasoning

The recorded reasoning is **manipulable**: a reader can *operate* on it, not only follow it. It must go beyond the explanatory level, enabling the researcher to *extend* the insights to other contexts or problems. For example, a move that identifies a key invariant may be explanatory, but its manipulability gain is that the invariant can be used as a pivot for further reasoning steps.

- **Compression and global reconstruction** ^t1-mr-compression-reconstruction
  The reasoning exposes its hierarchical strategic blocks and compresses the argument into a high-level pattern, so that a reader can reconstruct the strategy from scratch.
  *Implementing machinery*: the compressed-essence mechanism (Tier-2 reasoning-fields decision); the global-reconstruction mechanism (Tier-2 reasoning-fields decision); the [strategic-hierarchy structure](3-aspect-specific/arguments-reasoning#^t3-d-strategic-hierarchy) (Tier-3 machinery open question), whose global-to-local structure makes reconstruction tractable.

- **Transfer** ^t1-mr-transfer
  A reader can reuse the strategic pattern in another problem.
  *Implementing machinery*: the pattern-transfer mechanism (Tier-2 reasoning-fields decision); the [pattern-transfer machinery](3-aspect-specific/arguments-reasoning#^t3-d-pattern-transfer) (Tier-3 machinery open question), whose three conditions — pattern extraction, cross-case recognition, stability under variation — make transfer concrete.

- **Diagnosis** ^t1-mr-diagnosis
  A reader can locate weak points: what questions remain unanswered, what claims are loosely supported, what results are narrow or specific, what conditions are most restrictive.
  *Implementing machinery*: the diagnosis-weakness mechanism (Tier-2 reasoning-fields decision).

- **Comparisons and analogies** ^t1-mr-contrast
  The reasoning clarifies concepts and results by identifying similarities and distinctions between cases, and/or mapping the patterns onto familiar domains.
  *Implementing machinery*: the contrastive-reasoning mechanism (Tier-2 reasoning-fields decision).

- **Concrete illustration** ^t1-mr-illustration
  The reasoning applies to concrete instances: worked examples that instantiate the general pattern.
  *Implementing machinery*: the [worked-example link](3-aspect-specific/arguments-reasoning#^t3-d-worked-example) (Tier-3 machinery open question).

- **Misconception dismissal** ^t1-mr-misconception
  The reasoning anticipates predictable misconceptions (misreadings, naive models...), and supplies the counter-examples and clarifications that correct them.
  *Implementing machinery*: the [misconception record](3-aspect-specific/arguments-reasoning#^t3-d-misconception) (Tier-3 machinery open question).

**Failure mode prevented.** A reasoning can be understandable in principle (the reader can follow each step) yet not manipulable (the reader cannot extract the strategy, transfer it, or apply it to nearby problems). Such a reasoning remains inert.

**Upstream dependencies.**

- [Justification levels](#^t1-justification-levels) (parent criterion): manipulable reasoning is the *Manipulability*-level sub-criterion.
- [Explanatory gain](#^t1-explanatory-gain) (peer sub-criterion): the reader operations act on the understanding the explanatory gain produces.

**Downstream consequences.** No further non-facet consequence.