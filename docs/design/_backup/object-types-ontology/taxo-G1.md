
# Ontological Design for an Epistemic Object Framework - G1

## Primitive Types

A minimal but sufficiently expressive ontology can be organized into six canonical families.

### Question-like objects

They are the **targets of inquiry themselves**.

|Type|Function|Identity kernel|
|---|---|---|
|**Question**|asks for an answer, condition, criterion, comparison, explanation, or construction|interrogative content + scope|
|**Problem**|question with stronger operational or research commitment|question + target conditions|
|**Subquestion**|same ontological kind as question, but linked by decomposition relations|same as question|

A `Question` belongs in the canonical layer because it has independent epistemic identity.  
An `ArgumentBundle` does **not** replace the question; it assembles materials relative to it.

### Conceptual objects

These fix the semantic vocabulary of the framework.

|Type|Function|Identity kernel|
|---|---|---|
|**Concept**|stable referential unit for a notion|conceptual referent|
|**Definition**|gives admissible content to a concept or predicate|definiendum + defining content|
|**Notation**|assigns symbolic or linguistic expression|expression + referent|

Separate `Concept` from `Definition`:

- the concept is the semantic node
- the definition is one formulation that fixes or revises it

This allows alternative definitions, reformulations, historical variants, or refined versions without destroying object identity.

---

### Statement-like objects

These carry truth-apt content.

| Type           | Function                                                         | Identity kernel                 |
| -------------- | ---------------------------------------------------------------- | ------------------------------- |
| **Assumption** | accepted premise, local or global                                | propositional content + scope   |
| **Claim**      | assertoric proposition that may be proved, supported, or refuted | propositional content + context |

A strong design choice consists in treating `Theorem`, `Lemma`, `Proposition`, `Corollary` not as distinct ontological types, but as `Claim.kind = theorem / lemma / proposition / corollary`.

The reason is that their semantic nature is the same. The distinction is mostly rhetorical, organizational, or argumentative.

---

### Justificatory objects

These connect statements to their grounds.

|Type|Function|Identity kernel|
|---|---|---|
|**Proof**|establishes one claim from premises or prior results|target claim + justificatory content|
|**Derivation**|computational or formal chain yielding a result|target result + derivational content|
|**ArgumentSketch**|incomplete but structured justification|target + partial support structure|

A Proof must prove exactly one claim-like object. This gives proof objects a sharp target and prevents diffuse prose from becoming ontologically ambiguous.

If several proofs exist for the same claim, they remain distinct proof objects linked to the same target claim.

---

### Constructive and evidential objects

These are indispensable in research practice if the knowledge base is meant to support actual research reasoning rather than only theorem exposition. They should not be collapsed into prose.

|Type|Function|Identity kernel|
|---|---|---|
|**Example**|exhibits a case satisfying a concept, claim, or phenomenon|exhibited object + target|
|**Counterexample**|falsifies a universal statement or candidate criterion|exhibited object + refuted target|
|**Construction**|gives a procedure producing an object or witness|constructive rule + target class|
|**Observation**|records a stable empirical or analytic regularity not yet elevated to theorem|content + evidential basis|

---

### Source-grounding objects

If provenance and traceability is operationally important, a distinct family should be introduced.

|Type|Function|
|---|---|
|**SourceFragment**|anchored excerpt or localized external content|
|**ReferenceRecord**|bibliographic source entity|
|**EvidenceRecord**|observation, dataset result, experiment trace, or computational run|

If provenance is secondary, these can remain metadata instead of canonical objects.

