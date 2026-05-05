# Ontological Design for an Epistemic Object Framework - C4

## Primitive Types

| Type        | Functional Stratum          | Inferential Role                                                                                                                                                                                                            |
| ----------- | --------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| CONCEPT     | Semantic                    | Non-truth-apt semantic unit; substrate of propositional content                                                                                                                                                             |
| MODEL       | Semantic / Representational | Organized domain representation; licenses derivations and analogical transfer                                                                                                                                               |
| CLAIM       | Propositional               | Truth-apt propositional commitment                                                                                                                                                                                          |
| QUESTION    | Propositional-directive     | Structured epistemic gap with answerhood conditions                                                                                                                                                                         |
| ARGUMENT    | Inferential                 | Inferential structure licensing a conclusion from premises                                                                                                                                                                  |
| EXPLANATION | Inferential                 | Revelatory structure answering why-questions. Its schema should specify: explanans (CLAIM/MODEL), explanandum (CLAIM), explanatory type (causal, mechanistic, unificationist, functional, contrastive), and directionality. |
| METHOD      | Procedural                  | Prescriptive schema governing reasoning or inquiry                                                                                                                                                                          |
| FRAME       | Framework                   | Background configuration constituting admissibility conditions for reasoning                                                                                                                                                |

## Derived or Marginal Types

| Type                         | Role                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | Obtained as                                                                                                                                                                                                     |
| ---------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| THEOREM / AXIOM / CONJECTURE | CLAIMs differentiated by epistemic status and relationship to ARGUMENT:<br>- AXIOM: CLAIM with no dependency on any ARGUMENT (foundational, stipulated)<br>- THEOREM: CLAIM with a demonstrative ARGUMENT (proof) as dependency<br>- CONJECTURE: CLAIM with incomplete or absent ARGUMENT support, positive epistemic warrant                                                                                                                                                                                                                                                                                                                                                                                                                                                      | Subtypes of CLAIM, enforced by epistemic-status field and its relations to ARGUMENT nodes                                                                                                                       |
| MECHANISM                    | Causal-structural model specifying the entities, activities, and organizational features that produce a phenomenon. It differs from a general MODEL in its causal-process structure and its tight coupling to EXPLANATION (mechanisms explain by describing how a process operates). It is also distinct from a pure formal model.                                                                                                                                                                                                                                                                                                                                                                                                                                                 | Subtype of MODEL. It is not a primitive but must be structurally defined — not merely a label — because its explanatory coupling to EXPLANATION nodes is a first-class inferential dependency.                  |
| ANALOGY                      | Maps structural relations from a source domain to a target domain and licenses inference about the target based on known properties of the source. Analogical models are scientific models grounded in structural analogy to a better-understood domain (the Bohr atom as a solar system; fluid dynamics as an electrical circuit analogy). It has an inferential function distinct from deduction (it does not preserve truth) and distinct from induction (it operates on structural similarity, not frequency). It is not a MODEL (it does not organize a domain) but uses cross-domain structure to license a reasoning move. An analogical MODEL uses an ANALOGY to justify a MODEL structure, coupling ARGUMENT and MODEL in a way that requires explicit schema treatment.  | Subtype of ARGUMENT (Analogical) with its own schema (source domain, target domain, structural mapping, transferred claim, disanalogy conditions), namely a mandatory ANALOGIZES relation to its source domain. |
| OBJECTION                    | ARGUMENT directed against a CLAIM or another ARGUMENT. It is defined by its target and its adversarial inferential role.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | Subtype of ARGUMENT (Adversarial) with a TARGETS relation to the challenged object                                                                                                                              |
| EXAMPLE                      | These are typed relations (INSTANTIATES, REFUTES), not primitives or subtypes. However, the relation types must be explicitly specified in the relational schema — their absence constitutes a relational vocabulary gap.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | CLAIM standing in an INSTANTIATES relation to a general CLAIM                                                                                                                                                   |
| COUNTEREXAMPLE               |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | CLAIM standing in a REFUTES-BY-INSTANTIATION relation to a universal CLAIM                                                                                                                                      |
| INTERPRETATION               | Assigns semantic content to formal expressions or resolves ambiguity in natural language CLAIMs or MODELs. It is an INTERPRETS relation from one object (interpretive schema) to another (interpreted object), not an independent node type.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | Typed relation, requires explicit inclusion in the *relational* vocabulary.                                                                                                                                     |
| DISTINCTION                  | Differentiates two CONCEPTs by specifying the property on which they diverge.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | Typed relation: DIFFERENTIATES relation between CONCEPT nodes                                                                                                                                                   |
| NORM                         | A methodological norm is either:<br>- a prescriptive CLAIM about what constitutes admissible reasoning <br>    a constraint on METHOD application                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | Component of FRAME / Attribute of METHOD                                                                                                                                                                        |
| TAXONOMY                     | Hierarchical organization of CONCEPTs under IS-A and SUBSUMES relations. It is a structured CONCEPT graph                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | Composite CONCEPT structure, expressed via typed relations.                                                                                                                                                     |
| PARADIGM                     | A Kuhnian paradigm is a FRAME at the highest level of scope and entrenchment. It adds a historical-community dimension to FRAME (macro-scale, community-constitutive).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | Subtype of FRAME                                                                                                                                                                                                |
| DEFINITION                   | A definition may be read as:<br>- a semantic act circumscribing a CONCEPT (non-truth-apt, CONCEPT-level)  <br>    a stipulative CLAIM (truth-apt by convention)  <br>    a relation (DEFINES: definiendum CONCEPT → definiens complex).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | Relation DEFINES from CONCEPT to a structured CONCEPT/CLAIM complex, with a stipulative-vs-descriptive attribute.                                                                                               |
| PROOF STRATEGY               | A proof strategy (proof by mathematical induction, reductio ad absurdum) is a type-level METHOD schema for constructing ARGUMENT tokens.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | Subtype of METHOD (formal) or ARGUMENT type-level schema                                                                                                                                                        |

Structural Subtypes (not primitives, but schema-enforced)

- CLAIM: AXIOM, THEOREM, CONJECTURE, HYPOTHESIS, EMPIRICAL GENERALIZATION
- ARGUMENT: DEDUCTIVE, INDUCTIVE, ABDUCTIVE, ANALOGICAL, ADVERSARIAL
- EXPLANATION: CAUSAL, MECHANISTIC, UNIFICATIONIST, FUNCTIONAL, CONTRASTIVE
- MODEL: FORMAL, MECHANISTIC, PHENOMENOLOGICAL, COMPUTATIONAL, CONCEPTUAL
- METHOD: FORMAL PROCEDURE, HEURISTIC, EXPERIMENTAL DESIGN, PROOF STRATEGY
- FRAME: PARADIGM (macro-scale), RESEARCH PROGRAMME, LOCAL FRAMEWORK

## Boundaries

### CONCEPT vs. CLAIM

**For collapse**: The standard reductionist argument holds that concepts are recoverable from propositional content as sub-propositional constituents — that is, CONCEPTs are simply the subjects, predicates, and operators of CLAIMs, and can be dispensed with as independent nodes.

**Against collapse**: This reduction fails in the target domains. CONCEPT is necessary as a non-truth-apt semantic primitive.
- Conceptual analysis, disambiguation, intensional refinement, and taxonomic structuring are irreducibly concept-level operations that do not generate propositional output — they transform the semantic objects from which propositions are subsequently constructed.
- In philosophy, the central inquiry is frequently whether a concept is coherent, extensionally determinate, or correctly circumscribed — not whether any given CLAIM about it is true.
- In mathematics, the construction of new mathematical objects (category, functor, manifold) is a CONCEPT-level act prior to any theorem.

### CLAIM vs. MODEL vs. ARGUMENT

**For collapse**: CLAIMs could be absorbed into MODEL as labeled nodes, or into ARGUMENT as premise/conclusion roles.

**Against collapse**: CLAIM is the minimal truth-apt unit and the fundamental currency of epistemic commitment. Every other primitive either presupposes CLAIMs (ARGUMENT requires propositional content as premises/conclusions), is grounded in CLAIMs (FRAME contains background CLAIMs), or targets CLAIMs (QUESTION seeks to establish a CLAIM). CLAIMs are irreducible.

**Design improvement**: CLAIM currently subsumes axioms, theorems, conjectures, hypotheses, empirical generalizations, modal claims, normative claims, and interpretive claims. These differ significantly in epistemic status, inferential role, and dependency structure. To avoid overloading, enforce a structured epistemic-status attribute schema on CLAIM and to recognize major functional subtypes (AXIOM, THEOREM, CONJECTURE, HYPOTHESIS) with well-defined schema differences, particularly regarding their relationship to ARGUMENT nodes.

**Meta-epistemic layer.** The ontology currently does not support meta-epistemic evaluation abd reflexive reasoning — making CLAIMs _about_ nodes, evaluating argument quality, or assessing epistemic status at the graph level. 

 Recommended resolution is either: 
 - a META-CLAIM subtype whose content is a proposition about another node, with a reflexive typing constraint
 - an explicit evaluation annotation layer orthogonal to the node taxonomy. 
 
 The choice has significant implications for graph query and traversal semantics.
 
### QUESTION vs. CLAIM

**For collapse**: QUESTION could be eliminated in favor of a negated or incomplete CLAIM, or absorbed into METHOD as a procedural directive.

**Against collapse**: Erotetic logic establishes questions as irreducibly distinct from propositional content. A QUESTION carries a presupposition structure, an answerhood condition, a set of admissible partial answers, and a decomposition structure. None of these are recoverable from CLAIMs or METHODs without loss of structural information. Questions are the epistemic targets that organize inquiry; their elimination would make research planning and question decomposition structurally opaque.

**Design improvement**: The type/token distinction applies: a question type (the general structure of an inquiry) versus a question token (a specific instance of that question in a reasoning context). This should be explicitly annotated.

### ARGUMENT vs. CLAIM

**For collapse**: ARGUMENT could be reduced to a structured set of CLAIMs with dependency annotations, replacing the inferential primitive with a relational pattern over CLAIM nodes.

**Against collapse**: The inferential structure of an argument — the warrant relation, the movement from premises to conclusion, the logical form — is first-class information for reasoning transparency, which is not recoverable from a set of claims plus a dependency edge. An ARGUMENT encodes inferential license: _why_ the conclusion follows (or is supported), under what assumptions, via what inference principle.

**Design improvement**:
- Differentiate ARGUMENT by inferential type: deductive, inductive, abductive, analogical. Analogical arguments have fundamentally different inferential structure — they operate by cross-domain structural mapping, not logical consequence — and their assimilation to a homogeneous ARGUMENT type damages reasoning transparency for analogical reasoning. The recommended approach is to specify inferential-type as a mandatory schema field, with ANALOGICAL ARGUMENT as a structurally specified subtype.
- **Token/type concern.** An argument schema (proof by contradiction as a strategy type) versus an argument token (the specific proof of $\sqrt{2} \notin \mathbb{Q}$) must be explicitly distinguished. The schema should enforce instantiation relations between type-level and token-level nodes.

### MODEL vs. CLAIMs + CONCEPTS

**For collapse**: MODEL could be reduced to a structured compound of CLAIMs and CONCEPTs, making it a derived rather than primitive object.

**Against collapse**: A MODEL is not a conjunction of CLAIMs. It constitutes a coherent representational structure — an organized system of relations, entities, and constraints — that collectively represents a domain. The emergent organizational role of this structure (its capacity to license derivations, support analogical transfer, frame what counts as a fact about the domain) is not recoverable from any flat set of CLAIMs. 

**Design improvement**: MODEL subsumes mathematical structures (formal models), scientific models (mechanistic, phenomenological), conceptual frameworks (informal theoretical models), and computational models. These differ in their verification conditions, internal structure, and relationship to CLAIMs and ARGUMENTs. More critically, MECHANISM — a causal-structural model type central to scientific explanation — is invisible within the current taxonomy. MECHANISM should be a structurally defined subtype of MODEL with an explicit causal-process schema.

### METHOD vs. ARGUMENT vs. FRAME

**For collapse**: METHOD could be reduced to a specialized ARGUMENT schema (procedural argument) or absorbed into FRAME as a component norm.

**Against collapse**: METHOD has a distinct functional role: it is prescriptive and generative, not descriptive or inferential. It governs _how_ reasoning proceeds, not _what_ is concluded. 
- A proof strategy (induction, contradiction) is not an argument — it is a schema for constructing arguments. 
- An experimental design is not a claim — it is a procedural schema for generating evidence. 

**Design improvement**: **Overloading concern.** METHOD conflates:

- Formal inference rules (modus ponens)
- Proof strategies (proof by induction)
- Scientific methodologies (randomized controlled trial)
- Research heuristics (decompose-and-recombine)
- Computational procedures (dynamic programming)

The distinction between formal inference rules (which are truth-preserving and schema-level) and heuristics (which are approximate, domain-specific, and defeasible) is strategically significant. Conflating them under a homogeneous METHOD type obscures the epistemic status of reasoning moves that rely on them. The schema should enforce a methodological-type attribute with at least the distinction between formal procedures and heuristic schemas.

### EXPLANATION vs. ARGUMENT

**Against collapse**:
- The asymmetry between explanation and argument is a foundational result in philosophy of science: the same logical relationship between propositions can constitute an argument in one direction and an explanation in another (the Bromberger flagpole asymmetry, the Hempel-Oppenheim problematic).
- Explanations answer _why_-questions with a distinct illocutionary and inferential structure that cannot be reduced: an explanation has an explanans, an explanandum, and an explanatory relation.
- Explanatory reasoning (mechanistic, causal, teleological, unificationist) — does not reduce to ARGUMENT (which formalizes logical _consequence_ or support) nor to MODEL (which formalizes representation).
- The required reasoning modes explicitly include mechanistic explanation and causal explanation. Without EXPLANATION as a primitive, these modes can only be encoded as ARGUMENTs with special annotations — a structural opacity that directly violates the absolute evaluative priority.

### FRAME

**Against collapse**: FRAME is necessary because it captures a holistic conditioning function that cannot be decomposed into a mere sum of individual CLAIMs, METHODs, and CONCEPTs. A FRAME determines _what counts as a valid reasoning move_ — it sets admissibility conditions on arguments, explanations, and models. This conditioning function is genuinely emergent at the system level; no individual component of the FRAME performs it. Elimination would force this holistic structure into implicit, untracked assumptions distributed across all other nodes, damaging reasoning transparency severely.

**Inflation Risk**: FRAME as specified encompasses: 
- ontological commitments, 
- methodological norms,
- explanatory ideals, 
- admissibility standards, 
- conceptual background,
- privileged problem formulations. 

This corresponds to a fusion of several theoretically distinct structures:

- **Quinean holism**: background CLAIMs insulated from revision
- **Kuhnian paradigm**: exemplars, disciplinary matrix, problem formulations
- **Lakatosian research programme**: hard core (non-negotiable CLAIMs), protective belt, positive and negative heuristics (METHODs)
- **Wittgensteinian hinges**: propositions held fast as framework conditions
- **Logical empiricist framework**: constitutive vs. regulative principles

These differ in their structure, their relationship to revision, and their inferential role. A FRAME that silently absorbs all of them risks becoming a theoretical black box.

Without a defined internal schema, FRAME will absorb any object that does not fit cleanly into the other six categories. This makes FRAME a residual category — the ontological equivalent of "miscellaneous" — which is epistemically detrimental for classification stability.

**Design improvement**:

FRAME should be retained but internally decomposed via a mandatory structured schema with explicit inferential role specifications:

```
FRAME {
  id: URI
  label: string
  ontological_commitments: CLAIM[]     // background CLAIMs treated as constitutive
  methodological_norms: METHOD[]       // admissibility-conditioning procedures
  explanatory_standards: CRITERION[]  // what counts as an adequate explanation
  admissibility_conditions: RULE[]    // what arguments/models are licensed
  privileged_questions: QUESTION[]    // constitutive research problems
  background_concepts: CONCEPT[]      // conceptual vocabulary defining the domain
  scope: token | type                  // instance vs. schema
  revision_resistance: float          // degree of entrenchment [0,1]
}
```

The revision-resistance attribute allows the ontology to represent the difference between a loosely held background assumption and a paradigm-constitutive commitment, which are epistemically distinct.

**Should FRAME Be Split?**

The most principled split would separate:

- **COMMITMENT**: Ontological commitments (background CLAIMs)
- **STANDARD**: Evaluative criteria (admissibility, explanatory ideals)

However, this split damages the holistic conditioning function that makes FRAME valuable. A research paradigm is not a list of commitments plus a list of standards — it is an integrated structure in which commitments and standards co-determine each other. The internal schema approach achieves the expressivity of the split without sacrificing holistic structure.

## Remaining Unresolved Risks

**Cross-FRAME reasoning.** Framework comparison, paradigm shift, and incommensurability analysis all require structure that spans multiple FRAMEs. The current ontology provides no cross-FRAME relational primitives. FRAME-to-FRAME relations (INCOMMENSURABLE-WITH, TRANSLATES-INTO, SUBSUMES, CONFLICTS-WITH) are necessary for paradigm-level reasoning to be structurally transparent rather than merely asserted.

**Dynamics.** ==CRUCIAL== The ontology is essentially static — it represents the structure of epistemic objects but not their dynamics, how knowledge is constructed via inferential moves. The ontology cannot represent the epistemic dynamics of ongoing inquiry. 

**Token–type distinction**: This distinction is not optimally structurally unresolved. The ontology sometimes conflates type-level schemas (an argument form, a modeling strategy, a method class) with token-level instantiations (a specific proof, a concrete model, an applied procedure).

**Granularity calibration.** ==IMPORTANT== The token/type stratification resolves one dimension of granularity but not all. The ontology does not specify the granularity criteria for node individuation — when two similar CLAIMs are distinct nodes versus variants of one node, or when a sub-argument warrants its own ARGUMENT node versus being internal to a parent ARGUMENT. Without explicit individuation criteria, different annotators will produce structurally incomparable graphs, undermining the ontology's utility for systematic reasoning representation.

|Reasoning Mode|Supported?|Gap|
|---|---|---|
|Formal derivation|✓|None|
|Mechanistic explanation|⚠|MECHANISM implicit; EXPLANATION absent|
|Analogical reasoning|⚠|ANALOGICAL ARGUMENT not structurally specified|
|Conceptual clarification|✓|DISTINCTION relation not explicit|
|Semantic grounding|⚠|INTERPRETATION relation absent|
|Question decomposition|✓|Decomposition relations not specified|
|Research planning|✓|None|
|Comparative reasoning|⚠|No COMPARISON relation or cross-MODEL structure|
|Example-based reasoning|⚠|INSTANTIATES relation not specified|
|Heuristic reasoning|⚠|HEURISTIC / formal METHOD conflation|
|Meta-epistemic evaluation|✗|No meta-level or reflexive CLAIM structure|
|Paradigm-level reasoning|✓|Paradigm as FRAME subtype|
|Framework comparison|⚠|Cross-FRAME relational structure absent|