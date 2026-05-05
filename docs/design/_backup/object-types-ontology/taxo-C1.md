# Ontological Design for an Epistemic Object Framework - C1

## Primitive Types

| Type           | Role                                                                                                                                                                                                                                                                                                                                                                                                   |
| -------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| CONCEPT        | Refers and circumscribes. Named theoretical entity carrying _intensional_ content — the conditions of applicability, essential properties, scope of validity, and relationship to adjacent CONCEPTs.                                                                                                                                                                                                   |
| CLAIM          | Asserts propositional content (truth-apt). Polymorphism is captured through `epistemic_status` and a `claim_type` field.                                                                                                                                                                                                                                                                               |
| ARGUMENT       | Directed inference structure mapping a set of premises to a conclusion, made valid or strong by an explicit warrant. Polymorphism is captured by different warrants (deductive, inductive, abductive, analogical,  <br>transcendental, dialectical)                                                                                                                                                    |
| QUESTION       | Erotetic object encoding a _directed cognitive gap_. Generates inquiry chains, drives decomposition, and licenses the introduction of new CONCEPTs and CLAIMs by _epistemic necessity_. The `subquestions` field enables the erotetic DAG underlying decomposition methodology. The `answer_type` constrains what constitutes a satisfactory answer and thus what object types are expected to emerge. |
| PROBLEM        | Structured _productive gap_. Generates research programs. It carries explicit solution criteria, known constraints, and a boundary between known and unknown.                                                                                                                                                                                                                                          |
| MECHANISM      | Explanatory account of _how_ or _why_ a phenomenon occurs — specifying entities, their properties, their interactions, and the causal or functional structure that produces the target explanandum. It licenses _mechanistic reasoning_ — the ability to predict behavior by tracing entity-level dynamics.                                                                                            |
| ANALOGY        | Structural mapping between two domains — source and target — identifying correspondent entities, relations, or operations, together with explicit validity scope and breakdown conditions.                                                                                                                                                                                                             |
| EXAMPLE        | Concrete instantiation or illustration — either of a CONCEPT (demonstrating applicability) or of a CLAIM (evidential or pedagogical support). Includes counterexamples (`role = refutation`).                                                                                                                                                                                                          |
| DISTINCTION    | Differentiation between two CONCEPTs or CLAIMs that are liable to conflation, specifying the contrast criterion, the precise difference, and conditions under which conflation occurs.                                                                                                                                                                                                                 |
| INTERPRERATION | Assignment of semantic content to a formal or abstract structure within a specific domain or model. Bridges syntactic/structural objects and their meaning — essential whenever formal systems are applied to empirical or CONCEPTual domains.                                                                                                                                                         |

## Derived or Marginal Types

| Type                                         | Obtained as                                                                                                          | Separate Type?                                                                 |
| -------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------ |
| DEFINITION                                   | CLAIM serving as the DEFINITION field of a CONCEPT                                                                   | No                                                                             |
| THEOREM, AXIOM, CONJECTURE, LEMMA, COROLLARY | CLAIM. Their structural schema is identical; only derivation status and proof obligations differ.                    | No. It would yield unstable subtypes whose only discriminant is a status flag. |
| OBJECTION                                    | CLAIM with `dependencies` pointing to the target ARGUMENT or CLAIM. It can itself be a premise in a COUNTERARGUMENT. | No. It would duplicate CLAIM with only a relational tag as discriminant.       |
| COUNTEREXAMPLE                               | EXAMPLE with `role = refutation` with a target CLAIM covers the semantics entirely.                                  |                                                                                |

## Boundaries

### Question vs. Problem

- Questions ask _what is true_ — they generate inquiry chains and license the introduction of new objects by epistemic necessity.
- Problems ask _what must be constructed or proven under constraints_ — they generate research programs and license the introduction of new objects by productive necessity.

### MECHANISM vs. ARGUMENT vs. CLAIM

- MECHANISMs are process ontologies.
- ARGUMENTs are inference structures (proofs).
- CLAIMs are mere descriptions.

### ANALOGY vs. ARGUMENT

- ANALOGIES underpin analogical ARGUMENTs (typed ARGUMENT with `warrant_type = analogical`), but the mapping _itself_ is an independent object that can be referenced, critiqued, and extended. 
- The structural mapping has epistemic content independent of any particular ARGUMENT that uses it. 
- Multiple ARGUMENTs may draw on the same ANALOGY, and the ANALOGY itself is subject to independent evaluation along dimensions (structural depth, scope, disanalogy).

### DISTINCTION vs. CONCEPTs

- DISTINCTIONs are not merely pairs of CONCEPT objects — they carry the _contrastive analysis_ as primary content.
- DISTINCTION is retained as a first-class type because it licenses a specific reasoning move (CONCEPTual disambiguation) that appears in nearly every serious theoretical text and cannot be reduced to two CONCEPT nodes with a `related_concepts` link without losing the contrastive structure.

### INTERPRERATION vs. ARGUMENT vs. CLAIM

- INTERPRERATION is retained because it captures a genuinely distinct epistemic operation — _semantic grounding_ — that neither ARGUMENT nor CLAIM represents. 
- An INTERPRERATION is not an inference; it is a _meaning assignment_.
- The framework's expressiveness for theoretical physics, formal semantics, or philosophy of mathematics depends on it.
