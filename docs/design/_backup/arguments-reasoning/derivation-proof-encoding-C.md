---
tags:
  - backup
index: "[Argument and reasoning proposals](_index.md)"
aliases:
  - Derivation encoding — variant C
---
## Problem

Given a claim sequence $C_1, C_2, \ldots, C_n$ answering a sub-question $Q$, three distinct failures produce opacity:

- **Formal sufficiency without operative grounding**: the warrant licenses the step $C_i \vdash C_{i+1}$ but does not identify _which structural property of the objects under consideration_ makes the warrant applicable. Two applications of modus ponens differ at the explanatory level if one exploits linearity and the other exploits compactness; the formal warrant is identical but the conceptual content is not.
- **Flat annotation**: every step receives identical treatment, failing to distinguish between _low-content structural moves_ (substitution, unfolding a definition) and _high-content non-trivial moves_ that carry the genuine argumentative work.
- **Absent argument kernel**: every non-trivial argument has a small number of steps — often one — that are the _conceptual core_: the move that makes the rest follow tractably. When this step is unmarked, the reader must reverse-engineer it, which is precisely the failure of understanding.


---

## Core Theoretical Distinction: Warrant vs. Operative Property

Following Steiner's analysis of mathematical explanation, a step is explanatory only when the warrant is grounded in a _characterising property_ of the objects involved — a property that makes the relevant structure _this kind of thing_ rather than an arbitrary instance. 

| Concept                | Answers                                        | Role                            | Definition                                                                                                                              | Example                                                                                           |
| ---------------------- | ---------------------------------------------- | ------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- |
| **Warrant**            | What is the licence?                           | Provides the formal certificate | Inference schema or theorem licensing $C_i \vdash C_{i+1}$                                                                              | "by distributivity of $\land$ over $\lor$"                                                        |
| **Operative property** | Why does the problem yield here?               | Provides understanding          | Structural feature of the domain objects that makes the warrant applicable _here_ and that carries the explanatory weight               | "the finiteness of the index set, which makes the infinite intersection collapse to a finite one" |
| **Strategic function** | What does this purchase toward the conclusion? | Provides understanding          | What this step achieves within the local argument: what it _exposes_, _eliminates_, _reduces_, or _constructs_ relative to the sub-goal | "eliminates the existential quantifier by providing an explicit witness"                          |

All three are necessary; none is reducible to the others.

Separability test: if operative and strategic annotations reduce to restatements of the warrants, the representation has failed.

---

## Inferential Move Taxonomy

A step-level `move_type` classification that carries explanatory and automation-relevant information:

| Type           | Characterisation                                                                                                                                                                                                                     | Operative property          |
| -------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | --------------------------- |
| `structural`   | Purely formal manipulation: substitution, definition unfolding, syntactic normalisation.                                                                                                                                             | None; content-free          |
| `exposure`     | Rewrites a claim to make a hidden structure visible — e.g., completing the square, factoring, changing variable.                                                                                                                     | Structure being revealed    |
| `construction` | Introduces a new object, function, or set as a witness or auxiliary entity.                                                                                                                                                          | Constructive principle used |
| `reduction`    | Replaces the current proof obligation with an equivalent but more tractable one.                                                                                                                                                     | Equivalence exploited       |
| `pivot`        | Changes the conceptual frame — e.g., passing to the contrapositive, dualising, applying a bijection, lifting to a richer structure. This move is typically the kernel of the argument, which carries the highest explanatory weight. | ?                           |
| `closure`      | Discharges an open obligation: closes a case, eliminates a hypothesis, completes an induction.                                                                                                                                       | ?                           |
| `bounding`     | Establishes an inequality or containment used in a subsequent step.                                                                                                                                                                  | ?                           |

The `structural` type requires no operative property annotation. All other types require it. This enforces annotation effort proportional to explanatory content.

---

## Local Inference Node Format

| Field                | Type             | Description                                                                                                                                                                                                                                                                           |
| -------------------- | ---------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `id`                 | string           |                                                                                                                                                                                                                                                                                       |
| `claim`              | string           | Propositional content of $C_{i+1}$                                                                                                                                                                                                                                                    |
| `depends_on`         | [`step_id`, ...] | Direct predecessors in the local DAG                                                                                                                                                                                                                                                  |
| `move_type`          |                  | From taxonomy above                                                                                                                                                                                                                                                                   |
| `warrant`            | string           | What formally licenses the move (rule, theorem, or inference schema)                                                                                                                                                                                                                  |
| `operative_property` | string           | Structural feature of the domain objects that makes the warrant applicable here. This is the explanatory core of the step. Null only for `move_type: structural`.                                                                                                                     |
| `strategic_function` | string           | What this step achieves relative to the sub-goal (e.g. "exposes the fixed-point structure needed in step_07", "eliminates the positivity constraint by absorbing it into the norm bound")                                                                                             |
| `argument_kernel`    | boolean          | True if this step constitute a conceptual core of the argument. This field forces an explicit decision: _is this the key idea, or is it downstream of the key idea?_ A step qualifies if its removal would make the remainder either invalid or non-constructable by routine methods. |
| `epistemic_status`   | string           | established \| assumed \| conjectured \| provisional                                                                                                                                                                                                                                  |

Relation to explanatory understanding: This architecture operationalises a precise criterion: a local argument graph is _explanatorily adequate_ when a reader, after traversing the `operative_property` and `strategic_function` annotations without reading the formal `warrant` fields, can reconstruct _why the sub-question is answerable in this direction_ — i.e., what features of the domain objects make the conclusion reachable.

---

## Structural Constraints on the Local Argument Graph

| Constraint                                          | Rationale                                                                                                                                                                                | Failure modes                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| --------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Kernel-to-content ratio**                         | For a local argument graph answering a non-trivial sub-question, the number of kernel-flagged steps must be at least 1 but not higher than half the total number of steps.               | - An argument with $0$ kernel-flagged steps implies either that the reasoning is entirely routine (which should be stated) or that the annotator has not identified where the genuine difficulty lies. <br>- An argument graph with $> \lfloor n/2 \rfloor$ kernel steps for $n$ total steps indicates either that the sub-question has not been sufficiently decomposed, or that the annotator is inflating the difficulty of routine moves. |
| **Operative property non-redundancy**               | No two steps in the same local graph should declare identical operative properties unless they genuinely exploit the same structural feature in structurally parallel roles.             | Repeated operative properties signal that the argument has a unified structural basis that should be named at the sub-question level rather than reiterated at each step.                                                                                                                                                                                                                                                                     |
| **Strategic function forward-reference obligation** | Ahe `strategic_function` of any non-`closure` step must name — explicitly or by reference — a downstream step or the sub-goal itself.                                                    | A strategic function that does not connect to a downstream claim is incoherent: it asserts that the step achieves something without specifying what that something contributes.                                                                                                                                                                                                                                                               |
| **Kernel isolation test**                           | For each step flagged as an `argument_kernel`, the subgraph obtained by removing it and all steps that depend on it should not contain a path from the initial claims to the conclusion. | If such a path exists, the step is not a genuine kernel node — the argument could proceed without it, which contradicts its designation.                                                                                                                                                                                                                                                                                                      |

