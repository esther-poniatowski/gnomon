# Ontological Design for an Epistemic Object Framework - C3

## Primitive Types

The current decomposition organizes types along two orthogonal axes:

| Type                                     | Operative                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | Truth-apt | Structural             |
| ---------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------- | ---------------------- |
| CONCEPT                                  | Semantic grounding                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | No        | No                     |
| CLAIM                                    | Propositional assertion                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | Yes       | No                     |
| ARGUMENT                                 | Inferential evaluation                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | Partially | Yes (inferential)      |
| QUESTION                                 | Gap specification                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | No        | Yes (erotetic)         |
| MODEL                                    | Domain representation                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | No        | Yes (representational) |
| METHOD                                   | Operational specification                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | No        | Yes (procedural)       |
| FRAME / THEORETICAL FRAMEWORK (optional) | Coherent set of **paradigm-level commitments**: background CLAIMS, operative CONCEPTs (ontological assumptions), admissible MODELs, applicable METHODs, epistemic norms.<br>- constitute the epistemic context within which CLAIMs, MODELs, and ARGUMENTs are formulated and assessed<br>- provide a natural anchor for meta-epistemic CLAIMs about **theory-ladenness**, paradigm shifts, cross-framework comparisons<br>*Examples*: Bayesian epistemology, structural realism, constructivism, the Chomskyan generative program |           |                        |
| EVIDENCE                                 | Evidence has the following properties not shared by CLAIM:<br>-  not asserted but _cited_<br>- carries provenance, methodology, and reliability assessments<br>- functions as a **warrant-anchor** for ARGUMENTs (not as a premise in the standard sense)                                                                                                                                                                                                                                                                         |           |                        |

## Derived or Marginal Types

| Reasoning Mode                                                                                                                                                                                                                                                                                     | Coverage                                                            |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------- |
| Research planning                                                                                                                                                                                                                                                                                  | QUESTION + METHOD                                                   |
| Meta-epistemic evaluation (if not included as primitive)                                                                                                                                                                                                                                           | CLAIM (epistemic status attribute)                                  |
| Evidence (if not included as primitive)                                                                                                                                                                                                                                                            | CLAIMs with epistemic status = _empirical_ and role = _evidential_. |
| Heuristic<br>Decision rules operating under uncertainty with no guaranteed correctness, closer to a probabilistic procedural rule. Intermediate between METHOD (but lacks guaranteed stopping criteria and formal admissibility conditions), and CLAIM (not truth-apt in the propositional sense). | METHOD with explicit uncertainty annotations                        |

## Boundaries

### CONCEPT vs. CLAIM

**For collapse**:
- Every CONCEPT can be expressed as a cluster of definitional CLAIMs (necessary and sufficient conditions, applicability conditions, paradigm cases). Under this view, a CONCEPT is simply a named equivalence class of CLAIMs, and CONCEPT reduces to a CLAIM-cluster with a designated identifier.
- The CONCEPT/CLAIM boundary conflates two distinct distinctions:
	- (1) Semantic vs. propositional content
	- (2) Use vs. mention of conceptual content
- (1) A definitional CLAIM (e.g. "*a topological space is compact if and only if every open cover admits a finite subcover*") simultaneously:
	- encodes the intensional content of the CONCEPT (e.g. _compactness_),
	- constitutes a truth-apt propositional assertion.
- (2) CONCEPTs can be _refined_ by CLAIMs (a claim narrows the applicability conditions of a concept), and CLAIMs can _constitutively define_ CONCEPTs — creating a bidirectional dependency.

**Against collapse**:
- Eliminating CONCEPT collapses semantic grounding into propositional content, producing circular dependency.
- This conflates the linguistic encoding of a concept with the concept itself. A CONCEPT carries intensional content that is not exhausted by any finite set of definitional CLAIMs — this is the lesson of conceptual holism and the failure of the analytic-synthetic distinction for most theoretical terms (Quine, Putnam). Furthermore, CLAIMs presuppose CONCEPTs in their constituent terms: the CLAIM "compactness implies completeness in metric spaces" cannot be formulated without the prior circumscription of _compactness_, _completeness_, and _metric space_ as semantic objects. To encode these as CLAIMs would generate a vicious regress or an unanchored symbolic system.

**Design improvement**:
1. Introduce an explicit **semantic-vs-propositional** axis in the schema metadata.
2. Designate a CLAIM subtype `role: constitutive` for definitional CLAIMs that encode CONCEPT content — explicitly flagging their dual status.
3. Clarify in the CONCEPT schema that its content is the _semantic object_, while the definitional CLAIM is its _propositional encoding_. These are distinct nodes in the dependency graph, connected by a `grounds` or `encodes` relation.

### CLAIM vs. MODEL

This boundary is moderately stable but has a n

**For collapse**: Instability arises for **formal axiomatic systems** (axiomatic theories presented as claim-sets). A formal theory (e.g., ZFC set theory) consists of a set of CLAIMs (axioms + theorems). But the formal theory also constitutes a MODEL in the sense of specifying a class of intended interpretations. The same object has both a CLAIM-reading (propositional content) and a MODEL-reading (representational structure).

**Against collapse**:
- The distinction is one of **interpretive stance**, not ontological kind. Under the CLAIM-reading, axioms are propositional assertions about a domain. Under the MODEL-reading, the axiom system defines a class of satisfying structures.
- Axioms are CLAIMs that _characterize_ or _constrain_ a MODEL, not the MODEL itself. The MODEL is the intended interpretation or the class of structures satisfying those axioms.
- Model-theoretic distinction (Tarsky): a MODEL is a representational structure — a domain of objects with relations and operations — not a propositional assertion. A mathematical model is not a set of CLAIMs about the world; it is a structured object that _satisfies_ or _fails to satisfy_ CLAIMs.
- Collapsing MODEL into CLAIM would loose representational structure / Tarskian distinction.

**Design improvement**:
- The instability is resolvable through explicit schema design. These can be represented as two distinct linked nodes: a CLAIM-cluster (the axiom set) and a MODEL node (the class of intended interpretations), connected by a `characterizes` relation.
- Explicitly distinguish between a MODEL as a _representational structure_ and the CLAIM-cluster that _characterizes_ it. Introduce a `characterizes` edge type to link axiomatic CLAIMs to their intended MODEL.

### ARGUMENT vs CLAIM

**For collapse**: In formal logic, a proof is a sequence of CLAIMs connected by inference rules. ARGUMENT could reduce to a sequence of CLAIMs annotated with inference rule applications, making the inferential structure implicit in the annotation rather than explicit in the type.

**Against collapse**:
- A set of CLAIMs ${P_1, \ldots, P_n, C}$ does not specify the inferential structure (which claims function as premises, which as conclusion, nor does it specify the warrant connecting them).
- ARGUMENTs support reasoning operations that bare claim-sets do not: validity assessment, warrant evaluation, defeater analysis, argument mapping.
- Collapsing would encode ARGUMENTs as CLAIMs with implicit structure — a category error that sacrifices operational clarity. The reasoning system requires ARGUMENT as a first-class object precisely because it is the unit of inferential evaluation, not the unit of propositional content.

### ARGUMENT vs. MODEL

**For collapse**:
- Causal models are DAGs annotated with structural equations (in the tradition of Pearl), they encode conditional independence relations and interventional claims in a graph structure.
- They resembles the premise/conclusion structure of an ARGUMENT (structured ARGUMENT schemas).

**Against collapse**: The distinction is functional.
- An ARGUMENT is a _token-level inferential move_ — it makes a particular claim on the basis of particular premises under a particular warrant.
- A MODEL is a _type-level representational structure_ — it encodes the general dependency structure of a domain.
- A causal model enables many possible ARGUMENTs but is not itself an ARGUMENT.

**Design improvement**: This distinction is real but must be made explicit in schema documentation.

### CLAIM vs. METHOD

**For collapse**: Prescriptive CLAIMs (methodological norms, epistemic rules) superficially resemble METHODs.

**Against collapse**:
- The procedural/declarative distinction (knowing-how vs. knowing-that, deontic/operational divide) is philosophically well-established and operationally significant.
	- A prescriptive CLAIM is truth-apt: it can be argued for, contested, supported by evidence. "One ought to prefer simpler hypotheses" is a CLAIM that can be assessed as justified or unjustified.
	- A METHOD is not truth-apt: it is assessed as applicable, effective, admissible, or efficient — not as true or false.
- A METHOD is not reducible to a set of CLAIMs about what one should do, because:
	1. METHODs specify operational steps, not propositional assertions — they are executed, not evaluated for truth.
	2. Prescriptive CLAIMs (norms, rules) are truth-apt; METHODs are not — one does not assess a METHOD as true or false, but as applicable, effective, or admissible.
	3. METHODs encode procedural knowledge with decision structure (conditionals, stopping criteria) that is not naturally represented as a claim-set.

**Design improvement**: Extend the CLAIM schema with an explicit `modality` attribute encompassing: `descriptive`, `normative`, `prescriptive`, `conditional`, `modal`, `existential`. This differentiates prescriptive CLAIMs from METHODs at the schema level.

### ARGUMENT vs. METHOD

**For collapse**: The instability arises at proof strategies: is "proof by contradiction" a METHOD or a warrant type within ARGUMENT? Currently, the ARGUMENT schema lists warrant types (deductive, abductive, etc.) without clarifying that a METHOD can function as a warrant specification. A proof by induction is both an ARGUMENT (with a specific warrant) and an application of the METHOD of mathematical induction.

**Against collapse**: Collapsing METHOD into ARGUMENT conflates of type-level and token-level.
- A METHOD is a _type-level_ procedural schema — an abstract, reusable specification of a reasoning or operation procedure (e.g., mathematical induction, cross-validation, reflective equilibrium).
- An ARGUMENT is a _token-level_ inferential instance — a particular application of a warrant schema to specific premises yielding a specific conclusion.

**Design improvement**: Make the type/token relationship explicit in the dependency graph. Introduce an explicit `realizes` or `instantiates` relation from ARGUMENT to METHOD, indicating that a particular ARGUMENT instantiates a particular METHOD.

### QUESTION vs. METHOD

**For collapse**:
- Apparent similarity in structure: decomposition structure in QUESTION; step structure in METHOD.
- A research protocol can be read as both a METHOD (procedure for generating answers) and a decomposed QUESTION (structured research plan).

**Against collapse**:
- Collapsing QUESTION into CLAIM looses erotetic structure / answer-conditions.
- QUESTION specifies _what_ epistemic gap exists; METHOD specifies _how_ to fill a gap.
- Decomposing a QUESTION into sub-questions is erotetic reasoning, not procedural specification.

**Design improvement**: Treat the research protocol as a METHOD that is _guided by_ a QUESTION decomposition — i.e., a dependency relation, not a boundary overlap.

### QUESTION vs. CLAIM

**For collapse**: in formal erotetic logic (Wiśniewski), questions are reducible to sets of possible direct answers. Under this view, a QUESTION is a partition of logical space, expressible as a disjunction of CLAIMs.

**Against collapse**:
- This reduction of QUESTIONS to CLAIMS operates at the _logical_ level; at the _epistemic_ and _operational_ level, the QUESTION as a structured gap — with presuppositions, answer constraints, and decomposition — is a richer object than a disjunction.
- The distinction between truth-conditions and answer-conditions (drawn from erotetic logic) is operationally significant. A QUESTION is not equivalent to a CLAIM about ignorance (e.g., "it is unknown whether P"), because a QUESTION additionally carries:
	- presuppositional commitments that may be false and can be challenged
	- answer-type constraints that partition the space of admissible responses
	- decomposition structure that generates sub-questions
- These features are not expressible as CLAIMs without artificial encoding.
- Furthermore, QUESTIONs are the primary driver of research planning and decomposition — a reasoning mode listed as a target. Eliminating QUESTION would require routing all interrogative structure through CLAIM or METHOD, destroying the directness of representation.

### FRAME

A FRAME is not reducible to:

- A CONCEPT (too narrow; a FRAME is a coordinated system of concepts, norms, and models)
- A MODEL (a MODEL represents a domain; a FRAME conditions the entire reasoning space)
- A CLAIM (CLAIMs are made within a FRAME; a FRAME is a precondition, not a propositional content)
- A METHOD (a FRAME is not procedural)
