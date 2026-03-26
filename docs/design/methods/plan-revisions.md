

Create a note about audits
Improve decision rules
Improve procedural workflows

## Assessment of the Decision Rule System

## Global assessment

The main structural weakness is that several files mix three different aspects:

- the **normative constraint itself**  
- the **diagnostic test**  
- the **workflow mechanism** by which the test is enforced  

This produces partial duplication.

## I. Modularity and Separation of Concerns

### What is already well separated

#### Objective unity vs local necessity

Genuine distinction:

- **Objective unity** governs whether the note answers one inferential objective or several (“second objectives”)
- **Local necessity** governs whether a given unit is needed, once the objective is fixed. (“padding within one objective”).

Many systems collapse both into a single relevance rule, which makes audit ambiguous. 

#### Premise legitimacy vs proof strategy

Genuine distinction:

- **Premise legitimacy** asks whether the derivation is allowed to use a premise at all.  
- **Proof strategy** asks how the derivation is routed and what explanatory mechanism it must reveal.  

A proof can be perfectly legitimate in premises and still be poor in structure; conversely, a strategically elegant proof can still hide illicit assumptions.

#### Scope admissibility vs note-level admissibility

This distinction is also sound.

- **Scope admissibility** is project-level and external to the note.  
- **Objective unity** and **local necessity** are note-internal.  

This prevents a frequent failure mode in agent systems: a note that is locally coherent but globally off-mission.

### Where separation is not optimal

The main source of architectural friction is that some files are not really “rules” in the same sense as others.

#### Mathematical standards is not a rule — it is an audit checklist

Its six sub-checks do not introduce independent decision criteria: they aggregate and cross-reference two already-specified rules (proof strategies, premise legitimacy) plus four additional checks (assumptions, precision, relevance, failure modes). The result is dual specification: the same criterion is defined in its own file _and_ re-instantiated under mathematical standards. This violates the single-source-of-truth principle stated in the document's own preamble. 

The clean resolution is to either:

- (a) collapse proof strategies and premise legitimacy into mathematical standards as its sub-sections, suppressing them as independent rules;
- (b) demote mathematical standards to a pure enforcement instrument — a binding checklist that references the other rules by anchor without re-specifying their content.

**GPT**: Mathematical standards is not a peer rule; it is a meta-bundle. This file currently contains or instantiates:

- assumptions explicitness
- proof architecture
- premise legitimacy
- relevance
- failure modes
- some precision criteria

This is too composite to live beside atomic rules such as `objective unity` or `premise legitimacy`. It functions more as a **compliance bundle** or **audit profile** than as a single decision rule.

This creates two problems:

1. **Redundancy**: proof architecture duplicates `proof strategies`; premise legitimacy duplicates `premise legitimacy`; relevance overlaps with `local necessity`.
2. **Layer leakage**: the file spans epistemic, argumentative, and stylistic dimensions.

#### Writing principles is not a rule — it is a translation interface

Its stated purpose is to "translate selected epistemic and argumentative constraints into prose-level instructions." It introduces no original decision criterion: it inherits functional motivation, deductive continuity, claim/derivation/interpretation separation, interpretive scope, and premise legitimacy, and projects them onto the writing pass. This is a legitimate architectural pattern (a facade), but it should not be represented as a peer-level rule. It should be labeled explicitly as the stylistic instantiation of higher-layer rules, preventing the impression that it defines novel content-quality criteria.

**GPT**: Writing principles is not a peer rule, it is a meta-bundle. This file governs:

- register and tone  
- paragraph construction  
- display integration  
- prose-math flow  
- prose-level instantiations of higher-layer rules  

Again, this is not a single rule. It is a **writing profile** or **rendering policy**.

Its current formulation makes it partly derivative of other rules. That weakens modularity because the same constraint appears both:

- in the original higher-layer rule  
- in the prose-level restatement inside `writing_principles`  

Conceptually, it means the source of truth is no longer entirely singular.

#### Retention audit operator is partly a rule and partly an audit procedure

Test A operationalizes local necessity  
Test B operationalizes objective unity  
Test C operationalizes non-redundancy

This operator is not homogeneous. It is closer to an **audit harness** than to a rule. In a clean architecture, the retained source of truth would be:

- rule = normative constraint  
- operator = enforcement method tied to that rule

At present, the operator partly introduces new normativity, especially through Test C.

#### The integrative layer conflates content governance and workflow routing

Scope admissibility and divergence resolution serve fundamentally different functions. 

- Scope admissibility is a content-level criterion: it decides whether a candidate note's objective is admissible within the project. 
 - Divergence resolution is a workflow-routing protocol: it classifies discrepancies between contracted and delivered contributions and prescribes corrective actions.
 
 Placing them in the same "integrative layer" conflates the distinction between _what the note may contain_ and _what happens when it deviates from plan_. Divergence resolution belongs to a procedural workflow specification, not to the rule system governing generation quality. Its presence here risks being confused with a quality criterion rather than a recovery mechanism.

Divergence resolution is not a quality rule; it is workflow governance. This file is legitimate, but it belongs in a different category. It does not specify what a good note is. It specifies what to do when the produced note diverges from contract.

That is a **post-production routing policy**, not a writing-quality decision rule.

---

## II. Overlapping Rules and Merger Opportunities

#### Objective unity and scope admissibility

These overlap on “drift”, but at different levels:

- note-level inferential drift
- project-level research drift

This is acceptable.

### Retention audit operator is the audit-phase operationalization of two existing rules

The retention audit operator explicitly states that Test A operationalizes local necessity, Test B operationalizes objective unity, and Test C adds a non-redundancy check. 
- The first two tests introduce no new decision criteria: they convert existing planning-time rules into audit-time procedures using the removal test and the dependency-cone formalism. 
- Only Test C introduces genuinely new content (the non-redundancy check and the tie-break order). 
The architectural consequence is that the retention audit operator should not be listed as a rule at the same level as local necessity and objective unity. It should be represented as the audit-phase enforcement mechanism for those two rules, with Test C extracted as a standalone sub-criterion or appended as an audit operator of local necessity. The current structure implies that the agent must learn three separate rules when the operative content is one original rule (non-redundancy) plus the audit-time applications of two others.

**GPT**: A large portion of the retention audit operator is simply a second expression of local necessity and objective unity.

- Test A = local necessity in removal form  
- Test B = section-level atomicity/dependency-cone check  
- Test C = redundancy check, which is genuinely new  

This suggests the operator should be split:

- keep **A and B** as enforcement procedures attached to existing rules  
- extract **C** as its own rule, for example `non-redundancy`  

At present, the operator looks unified only because it is placed under one heading, not because it governs one coherent quality dimension.

### Retention audit operator Test B and Objective unity's non-atomicity test are substantially equivalent

Objective unity requires each major section to name its local output and immediate downstream consumer, and declares a note too broad when a section's output-consumer pair "differs materially from the note-level pair." Retention audit Test B requires each section to record a dependency signature (inputs, output, downstream consumer) and fails a section whose output "could be reused independently without the main result." The operative check is identical: does the section's output belong to the dependency cone of the main result? 

The difference is that the non-atomicity test is applied at *planning time* (contract specification) and Test B is applied at *audit time*. This is legitimate phase separation, but it should be represented as such — not as two distinct tests in two separate rules, but as one test applied in two enforcement phases.

### Functional motivation duplicates local necessity condition 2 for the specific case of major constructs

Local necessity condition 2 admits content that "introduces, motivates, or sets up an object, assumption, or distinction used in the note's argument." Functional motivation then specifies, for major constructs specifically, a six-field template (obstacle, missing information, candidate object, exact later step, what the object makes visible, why alternatives are inferior). The relationship is specialization: functional motivation is condition 2 applied to a particular granularity. The current presentation does not state this clearly, which creates a dual enforcement risk — the agent might check both rules independently and obtain conflicting signals, or check neither because each appears covered by the other. The fix is to make functional motivation an explicit sub-criterion of condition 2, activated when the introduced object qualifies as a major construct under the stated threshold.

### Side-result criterion is a single clause of local necessity

The side-result criterion introduces exactly one new check beyond local necessity: _authorization by the contract_. The five admissibility conditions of local necessity determine whether a content unit is _relevant_; the side-result criterion adds whether it is _authorized_. This is a sixth condition, not a distinct rule. It should be folded into local necessity as condition 6, with a note clarifying that conditions 1–5 test relevance and condition 6 tests authorization. The current representation as a standalone rule inflates the apparent complexity of the system and creates a split-enforcement problem: the agent must consult two rules to determine whether a side result should be included.

- **local necessity** asks whether content is inferentially justified
- **side-result criterion** asks whether that justified content is contract-authorized

### Local necessity interpretive sub-criterion partially overlaps claim/derivation/interpretation separation

Local necessity's interpretive sub-criterion (condition 5, ^bounded-interpretive-radius) prohibits interpretation that "introduces new concepts not used in the result, launches a broader synthesis across modules, surveys neighboring theories not needed locally, or develops philosophical or methodological commentary." Claim/derivation/interpretation separation independently prohibits interpretation units that "merely paraphrase the claim or replay the proof." Both rules constrain what an interpretation unit may contain, but from different directions: the former excludes outward expansion, the latter excludes backward regression toward the claim or derivation. The two constraints are complementary rather than redundant, but they should be stated in direct relation to each other — the interpretive sub-criterion governs scope _above_ the derivation (no new objects), while claim/derivation/interpretation separation governs scope _below_ the derivation (no re-derivation). Juxtaposing them explicitly, even briefly, would prevent the agent from treating them as governing the same failure.

### Local necessity vs deductive continuity

There is a real distinction, but the current phrasing sometimes makes them bleed together.

- **Local necessity** asks whether a unit belongs.
- **Deductive continuity** asks whether adjacent major steps are connected by explicit logical dependence.

However, some parts of local necessity already speak in terms of downstream use and inferential role, while deductive continuity also speaks in terms of section outputs and consumers. The conceptual border is therefore narrower in practice than in theory.

A cleaner distinction should be stated explicitly:

- **Local necessity**: unary admissibility test on a unit  
- **Deductive continuity**: binary relational test between units

### Mathematical standards vs Proof strategies and Premise legitimacy

Mathematical standards explicitly “instantiates” proof strategies, but also repeats core parts of it. This is unnecessary duplication. The standards file should refer to proof strategies, not restate them as one of its own sections.

Same issue for Premise legitimacy. The standards file should not own premise legitimacy. It should consume it.

### Claim/derivation/interpretation separation vs writing principles

This rule is argumentative, but many of its practical consequences are prose-level. The current system therefore expresses it twice:

- once as a structural role-separation rule  
- once as a prose-level writing principle  

This is operationally understandable, but conceptually duplicative.

## III. Necessity and Sufficiency for Writing Quality

### Are all current rules necessary?

Not all current **files** are necessary as peer-level decision rules. But most current **constraints** are necessary somewhere in the architecture. A distinction is needed between:

- necessity of the **constraint** 
- necessity of the **current file boundary**

**Necessary constraints**:

- scope control
- local admissibility
- premise accounting
- proof routing
- construct justification
- logical chaining
- role separation
- project-level admissibility
- divergence handling

**Unnecessary peer-level files**: Less necessary as separate peer rules:

- `mathematical standards`
- `writing principles`
- `retention audit operator` in its current bundled form
- `divergence resolution` as a “rule”

### Are the rules sufficient for best writing quality?

Not yet. They are close to sufficient for **rigorous, scoped, audit-friendly notes**, but not fully sufficient for **best writing quality** in the broader sense. Several quality dimensions remain under-specified.

#### Missing: notational and terminological coherence as an independent rule

The rules reference `registry/terminology.yaml` and lint tools in the stylistic layer, but no rule explicitly governs the stability and coherence of notation across a note or across notes in the same module. In formal mathematical writing, this is a distinct failure mode: the same mathematical object is denoted differently in setup and proof, equivalent formulations of a result are used interchangeably without declaring their equivalence, or a symbol is recycled for different objects across sections. A notational coherence criterion — at minimum requiring that each major symbol has a unique referent throughout the note and that notational changes relative to imported material are declared — would close this gap.

**GPT**: Terminology is mentioned via linting and registry files, but the rule system does not clearly state a quality rule such as:

- one concept, one term in local context  
- no silent renaming of the same object  
- no shift in meaning across sections without explicit declaration  

#### Missing: a transition quality requirement at the prose level

Deductive continuity ensures that each section uses a specific output from a preceding section as a logical input, and the skeleton is required to make this dependency explicit. However, no rule requires that the prose of the note itself makes the logical spine visible to the reader at the transition between sections. A note can satisfy deductive continuity (the logical dependence exists) and claim/derivation/interpretation separation (roles are distinct within sections) while still producing transitions that are opaque — where the reader cannot determine from the prose alone what the previous section established and why the current section follows. This is a prose-level failure not reducible to a logical or role-separation failure. A transition-quality sub-criterion within writing principles — requiring each section-opening passage to identify what was established in the preceding section and what specific inferential gap the current section closes — would make the skeleton's logical spine legible.

#### Under-specified: information ordering within units

Deductive continuity governs section-to-section dependence, but there is less explicit control over **intra-unit ordering**:

- claim before proof
- obstacle before construction
- local question before technical step
- result before interpretation or converse depending on note type

Some of this appears in writing principles and functional motivation, but not as a distinct enforceable ordering policy.

#### Insufficiently operationalized: target criterion in proof strategies

The explanatory target requirement (^explanatory-target) demands a sentence of the form "The derivation reveals that [result] holds because [structural reason]," where the structural reason must name a mathematical property. This is the most epistemically ambitious criterion in the system and correctly targets the distinction between verification and explanation. However, the criterion is binary as written: a derivation either names a structural reason or it does not. No rule specifies what constitutes a _sufficient_ structural reason, nor how to determine whether the named property genuinely explains the result versus being a post-hoc label. For example, a derivation might satisfy the letter of the requirement by writing "the result holds because of the symmetry of the kernel" without the derivation ever exhibiting that symmetry as a constructive mechanism. The constructive-direction sub-criterion (^constructive-direction) partially addresses this by requiring forward construction, but the connection between the explanatory target and the constructive-direction test should be made explicit: the structural reason in the explanatory target must correspond to the mechanism that the forward construction exposes, not to a property that could be verified after the fact.

#### Missing: Evidence-to-claim proportionality is implicit, not explicit

For mathematical notes this is partly handled by premise legitimacy and proof strategy. But for argumentative or mixed analytical writing, a rule is still useful:

- stronger claims require stronger local support
- interpretive or comparative claims must scale to actual evidence supplied

At present, the system assumes mainly mathematical notes; for broader “AI generation tasks”, sufficiency is weaker.

#### Missing: Abstraction control

A common failure mode in mathematically sophisticated AI writing is not mere scope drift, but **oscillation between abstraction levels** without controlled transition:

- a paragraph starts at high conceptual level
- drops into raw formalism
- rises back to interpretation

Claim/derivation/interpretation separation helps, but does not fully regulate level shifts. A dedicated rule on **abstraction-layer control** may improve prose quality materially.

#### Missing: Audience calibration

The current rules focus on inferential correctness and scope discipline. They do not fully govern **how much is assumed of the intended reader**.

A note can satisfy all current rules and still be poor because it is pitched at the wrong level of abstraction or compression.

A missing rule or explicit profile dimension is: "Audience calibration"

- what the intended reader is assumed to know  
- what can remain implicit  
- what needs one-line recall 
- what degree of compression is acceptable  

This is adjacent to premise legitimacy and writing principles, but not reducible to either.

#### Scope admissibility's enforcement is contract-time, not generation-time

If scope admissibility is enforced entirely during the contract specification phase (Architect pass, Gate "execution"), then it operates _before_ generation begins and cannot be meaningfully described as a generation-time rule. Its enforcement section confirms this: the Architect pass verifies conditions 1–6 before Phase 2 proceeds. At audit time, the coherence audit only verifies that no forbidden or deferred content was introduced — a check that is already implied by the contract compliance verification. The rule is necessary as a project-level constraint, but its placement in the generation rule system is misleading. It belongs to the contract formation protocol, where it would be listed as a binding pre-condition on contract acceptance.


## Summary Table

|Rule|Assessment|
|---|---|
|Objective unity|Retain; well-scoped|
|Local necessity|Retain; absorb side-result criterion as condition 6; absorb functional motivation as sub-criterion of condition 2|
|Functional motivation|Demote to sub-criterion of local necessity condition 2|
|Proof strategies|Retain; tighten the link between the explanatory target and the constructive-direction sub-criterion|
|Mathematical standards|Demote to enforcement checklist; remove dual-specification of proof strategies and premise legitimacy|
|Premise legitimacy|Retain as independent rule; remove re-specification from mathematical standards|
|Side-result criterion|Absorb into local necessity as condition 6|
|Retention audit operator|Demote to audit-phase enforcement mechanism for local necessity and objective unity; retain Test C as an independent non-redundancy sub-criterion|
|Deductive continuity|Retain|
|Claim/derivation/interpretation separation|Retain; add explicit cross-reference to interpretive sub-criterion of local necessity|
|Writing principles|Demote to translation interface; label explicitly as the stylistic facade of higher-layer rules|
|Scope admissibility|Relocate to contract formation protocol|
|Divergence resolution|Relocate to procedural workflow specification|
|_Notational coherence_|**Add as new rule** within writing principles or as an independent stylistic rule|
|_Transition quality_|**Add as sub-criterion** within writing principles|

## Recommended refactoring

The system should not be simplified by deleting core epistemic rules. The correct move is **refactoring by rule type**. A more modular system would separate four categories.

### I. Atomic normative rules

**True core.** The following should remain separate because each captures a non-substitutable failure mode:

- Objective unity
- Local necessity
- Functional motivation
- Proof strategy
- Premise legitimacy
- Deductive continuity
- Role separation (claim / derivation / interpretation)
- + Non-redundancy (new)
- Scope admissibility
- (Audience calibration or exposition calibration)

#### Extract `non-redundancy` as an independent rule

At present, redundancy appears in several places:

- objective unity indirectly
- local necessity indirectly
- retention audit Test C explicitly
- mathematical standards under relevance
- writing principles indirectly

This deserves a dedicated rule because redundancy is not reducible to irrelevance. Two units can each be relevant yet jointly redundant.

A clean rule would be: "Non-redundancy"

**Failure prevented**: two or more units make substantially the same contribution without additional inferential gain  
**Decision criterion**: if one unit can absorb the other without loss of claim, justification, or uniquely useful interpretation/example, the weaker unit must be merged or removed

This would stabilize Test C and reduce diffusion across other files.

### II. Composite quality profiles

These import rules for a given pass.

- Mathematical quality profile (mathematical_standards.md → mathematical_quality_profile.md)
- Writing quality profile (writing_principles.md → writing_quality_profile.md)

#### Mathematical standards

Recommended status: **composite audit profile**, not atomic rule.

Possible replacement: rename as `mathematical_quality_profile.md`.

This file should orchestrate checks, not compete with atomic rules. Define it as a bundle that imports:

- premise legitimacy
- proof strategies
- explicitness thresholds
- assumption visibility
- failure-mode reporting

Remove any normative content already owned elsewhere

#### Writing principles

Recommended status: **writing policy / rendering profile**, not decision rule.

This file should govern:

- sentence and paragraph form
- display/prose integration
- notation formatting
- register

It should not restate higher-layer rules except as explicit downstream rendering consequences, and even then by reference rather than partial duplication.

### III. Enforcement operators

These are stage-specific tests.

- Removal test
- Dependency-cone test
- Candidate-overlap test
- divergence classifier
- lint checks

- retention_audit_operator.md → split into:
    - removal_test.md
    - dependency_cone_test.md
    - candidate_overlap_test.md
- divergence_resolution.md → workflow/divergence_resolution.md

This would reduce conceptual duplication without discarding useful operational content.

### IV. Workflow governance

These route outcomes.

- Divergence resolution
- deferred-material protocol
- contract override protocol

This would sharply improve separation of concerns.

#### Reclassify divergence resolution

Recommended status: **workflow adjudication policy**

It is valuable, but it does not belong in the same rule inventory as epistemic and argumentative constraints.

---

## Specific comments on each rule

## Objective unity

Strong and well defined. The output-consumer criterion is useful.  
One caution: the notion of “main result family” risks admitting too much if left semantically loose. A sharper criterion for what counts as a legitimate companion output would improve robustness.

## Local necessity

Very strong rule. Probably the best file in the set.  
The five-condition structure is broad enough to cover real note content while still constraining drift.

One caution: conditions 3 and 5 may overlap in practice:

- regime comparison for meaning
- interpretive illustration of distinctions

This is not fatal, but audit instructions should explicitly state which label dominates when both seem available.

## Functional motivation

Necessary and valuable. It captures a high-frequency failure mode of AI drafting.  
It should remain focused on major construct introduction and not absorb broader explanatory obligations.

## Proof strategies

Very strong conceptually. The explanatory-target requirement is excellent.  
This is one of the most valuable parts of the system because it forces explanation of mechanism rather than post hoc verification.

One caution: some legitimate proofs are hybrid. The taxonomy should explicitly allow:

- primary family
- optional secondary family

Otherwise classification pressure may become performative.

## Mathematical standards

Useful content, weak modular status.  
Should become a profile, not remain a peer rule.

## Premise legitimacy

Necessary and well scoped.  
Particularly strong is the distinction between local proof, import, and explicit assumption.

## Side-result criterion

Useful and distinct.  
It adds authorization control beyond necessity.

## Retention audit operator

Useful operationally, but architecturally overloaded.  
Test C should be extracted into an independent non-redundancy rule.

## Deductive continuity

Necessary.  
The decomposition-pattern requirement is especially good because it prevents generic template writing.

One improvement: explicitly define the unit of continuity. At present the rule seems section-level. That should be stated more sharply.

## Claim / derivation / interpretation separation

Necessary and high value.  
It addresses one of the most common defects in AI-generated technical prose.

## Writing principles

Useful, but not a peer rule.  
It should remain the place for style and prose realization, not for partial restatement of higher-level logic.

## Scope admissibility

Necessary at project scale.  
This is one of the strongest protections against agentic drift in long research programs.

## Divergence resolution

Useful, but not a quality rule.  
It is workflow arbitration.

---
