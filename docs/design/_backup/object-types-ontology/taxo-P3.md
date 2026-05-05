
# Taxonomy - P3

## Families

A minimal but sufficiently expressive ontology can be organized into six canonical families.


| Family                                  | Role                                                                  | Examples                           |
| --------------------------------------- | --------------------------------------------------------------------- | ---------------------------------- |
| **Question-like objects**               | Define the **targets of inquiry themselves** (not inquiry bundles)    | question, problem, subquestion     |
| **Conceptual objects**                  | Fix the **semantic vocabulary** of the framework                      | concept, definition, notation      |
| **Statement-like objects**              | Carry truth-apt content.                                              | assumption, claim, conjecture      |
| **Justificatory objects**               | Connect statements to their grounds.                                  | proof, derivation, argument-sketch |
| **Constructive and evidential objects** | Support actual research reasoning rather than only theorem exposition |                                    |
| **Source-grounding objects**            |                                                                       |                                    |

## Question-like objects

|Type|Function|Identity kernel|
|---|---|---|
|**Question**|asks for an answer, condition, criterion, comparison, explanation, or construction|interrogative content + scope|
|**Problem**|question with stronger operational or research commitment|question + target conditions|
|**Subquestion**|same ontological kind as question, but linked by decomposition relations|same as question|

*Distinction*:

- A `Question` belongs in the canonical layer because it has independent epistemic identity.  
- An `ArgumentBundle` does **not** replace the question; it assembles materials relative to it.

## Conceptual objects

| Type           | Function                                           | Identity kernel                |
| -------------- | -------------------------------------------------- | ------------------------------ |
| **Concept**    | stable referential unit for a notion               | conceptual referent            |
| **Definition** | gives admissible content to a concept or predicate | definiendum + defining content |
| **Notation**   | assigns symbolic or linguistic expression          | expression + referent          |

*Distinction*:  `Concept` vs. `Definition`

- the concept is the semantic node
- the definition is one formulation that fixes or revises it

This distinction allows alternative definitions, reformulations, historical variants, or refined versions without destroying object identity.

## Statement-like objects

|Type|Function|Identity kernel|
|---|---|---|
|**Assumption**|accepted premise, local or global|propositional content + scope|
|**Claim**|assertoric proposition that may be proved, supported, or refuted|propositional content + context|
|**Conjecture**|same ontological family as claim, but different status|claim content + open status|

*Distinction*: `Theorem`, `Lemma`, `Proposition`, `Corollary` can be treated not as distinct ontological types, but as a subtyme of claim.

`Claim.kind = theorem / lemma / proposition / corollary`

Justification: their semantic nature is the same. The distinction is mostly rhetorical, organizational, or argumentative.

## Justificatory objects

| Type               | Function                                             | Identity kernel                      |
| ------------------ | ---------------------------------------------------- | ------------------------------------ |
| **Proof**          | establishes one claim from premises or prior results | target claim + justificatory content |
| **Derivation**     | computational or formal chain yielding a result      | target result + derivational content |
| **ArgumentSketch** | incomplete but structured justification              | target + partial support structure   |

 Rule: a `Proof` must prove **exactly one** claim-like object.

Proof objects have a sharp target and prevent diffuse prose from becoming ontologically ambiguous.

If several proofs exist for the same claim, they remain distinct proof objects linked to the same target claim.

## Constructive and evidential objects

|Type|Function|Identity kernel|
|---|---|---|
|**Example**|exhibits a case satisfying a concept, claim, or phenomenon|exhibited object + target|
|**Counterexample**|falsifies a universal statement or candidate criterion|exhibited object + refuted target|
|**Construction**|gives a procedure producing an object or witness|constructive rule + target class|
|**Observation**|records a stable empirical or analytic regularity not yet elevated to theorem|content + evidential basis|

## Source-grounding objects (optional)

If provenance (traceability) is operationally important, a distinct family should be introduced. If provenance is secondary, these can remain metadata instead of canonical objects.

|Type|Function|
|---|---|
|**SourceFragment**|anchored excerpt or localized external content|
|**ReferenceRecord**|bibliographic source entity|
|**EvidenceRecord**|observation, dataset result, experiment trace, or computational run|

