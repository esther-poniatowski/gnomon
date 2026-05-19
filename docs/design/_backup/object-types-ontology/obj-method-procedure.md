# Object candidate — Method / Procedure

## Role

A method is a reusable pattern for performing an epistemic operation.

Its role is to state a repeatable procedure for a type of epistemic task.

Methods store procedural knowledge: how to test a conjecture class, normalize a definition, compare mechanisms, or construct counterexamples.

==TODO: What is the most fundamental: the method, or the procedure? Or are they synonyms?==

*Example*: cross-validation is a method for estimating model performance on held-out data.

*Examples of tasks*:

- solving
- testing
- evaluating
- constructing
- transforming
- decomposing
- comparing

## Properties

**Truth-apt**: No

**Functional stratum**: Procedural

**Internal structure**:

- **Task.** Epistemic task the method performs.
- **Inputs.** Objects or conditions required before use.
- **Steps.** Ordered or partially ordered moves.
- **Rules.** Admissible moves or decisions.
- **Output.** Object or state the method is meant to produce.
- **Stop condition.** Criterion for completion.
- **Failure modes** (context-dependent). Ways the method can break down.

## Encoding options

### Process model plus norms

**Category:** Composite object

**Specification:** Combine a process `MODEL`, normative `CLAIM`s, and target `QUESTION` links (e.g., randomized trial protocol).

**Pros.**
- Preserves ordered operations without treating procedure as primitive by default.
- Keeps admissibility claims, stopping criteria, and target questions explicit.
- Works when procedure can be represented rather than executed.

**Cons.**
- Procedural knowledge becomes less native when the system must orchestrate procedures.

### Operational primitive

**Category:** Primitive object

**Specification:** Keep `METHOD` primitive as the procedure selected, applied, or assessed by `QUESTION`, `ARGUMENT`, `MODEL`, or `EVALUATION`s (e.g., cross-validation).

**Pros.**
- Separates knowing-how from propositional claims and argument tokens.
- Supports execution, applicability, effectiveness, and admissibility as method-level assessments.
- Works when other objects target the procedure itself.

**Cons.**
- Needs strict subtype policy to avoid absorbing rules, plans, heuristics, and algorithms.

### Argument warrant

**Category:** Reduction to another object

**Specification:** Use `ARGUMENT` to carry the warrant that connects premise `CLAIM`s to a conclusion `CLAIM` (e.g., induction supports the general claim).

**Pros.**
- Fits proof strategies that function as warrant types.
- Covers proof by contradiction, proof by induction, and inference to the best explanation when they only license an argument.

**Cons.**
- Conflates reusable procedures with particular inferential moves unless type and token links stay explicit.
- Fails when the method does more than supply an argument warrant.

### Framework component

**Category:** Annotation on another object

**Specification:** Attach the procedure to `FRAMEWORK` as a background admissibility rule (e.g., always preregister experiments).

**Pros.**
- Works when the procedure only expresses background standards.
- Fits procedures that are not selected as local methods.

**Cons.**
- Too coarse for local operational methods.

### Method variant decomposition

**Category:** Variant decomposition

**Specification:** Replace generic `METHOD` with variants sorted by procedure family: algorithmic procedure, inference rule, policy, heuristic, evaluation protocol, and research plan (e.g., dynamic programming).

**Pros.**
- Prevents a single method type from mixing procedures, norms, and strategy.
- Distinguishes formal inference rules, proof strategies, scientific methodologies, research heuristics, and computational procedures.
- Fits procedure families that interact differently with `ARGUMENT`, `MODEL`, `QUESTION`, or `EVALUATION`s.

**Cons.**
- Adds subtype complexity before the taxonomy has stable use patterns.
- Loses a single generic procedure object for mixed or underspecified methods.

## Subtypes

Subtypes are meaningful along one dimension: the operation family performed by the procedure.

| Label                   | Description                                                                   | Encoding                                                                | Assessment                                                                                                        |
| ----------------------- | ----------------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------- |
| Inference rule          | Licenses a formal move from premises to conclusion.                           | `METHOD` subtype or warrant relation in `ARGUMENT`.                     | Stable when the rule is reusable across arguments.                                                                |
| Proof schema            | Gives a reusable pattern for constructing proofs (e.g., induction, reductio). | `METHOD` subtype linked to `DERIVATION / PROOF` as a type-level schema. | Stable when many proof tokens instantiate the same pattern; specific proof plans belong to `STRATEGY / PLANNING`. |
| Experimental design     | Specifies intervention, control, and observation procedure.                   | `METHOD` subtype linked to `EVIDENCE`.                                  | Stable when provenance and admissibility matter.                                                                  |
| Evaluation protocol     | States how an object is assessed.                                             | `METHOD` subtype linked to `EVALUATION` and `NORM`.                     | Stable when the assessment procedure is reusable.                                                                 |
| Computational procedure | Gives an algorithmic operation.                                               | `METHOD` subtype linked to code, model, or transformation target.       | Stable when execution and reproducibility matter.                                                                 |
| Heuristic               | Guides search under uncertainty without guaranteed success.                   | `METHOD` subtype with defeasible force.                                 | Useful when uncertainty belongs to the procedure itself.                                                          |
| Construction method     | Produces an example, witness, model, or proof object.                         | `METHOD` subtype linked to `EXAMPLE` or `MODEL`.                        | Stable when output production is central.                                                                         |
