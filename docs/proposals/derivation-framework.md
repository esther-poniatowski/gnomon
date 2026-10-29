---
tags:
  - ideas
index: "[Proposals](docs/proposals/_index.md)"
aliases:
  - Proposals for the derivation framework
---
# Proposals for the derivation framework

The goal [`derivation-framework`](../../TODO.md) formalizes derivation, its results, and synthesis.

## Algebraic data types for propositional content

Propositional content is represented by a recursive algebraic data type, with the constructors `Atom`, `Not`, `And`, `Or` and `Implies`, rather than by a string or by prose. The grammar `φ ::= p | ¬φ | φ∧φ | φ∨φ | φ→φ` admits structural pattern matching, and a string does not. The [decision on expression syntax](../adr/expression-syntax.md) already gives each formula a term structure: an S-expression core, whose operators are head symbols. The open part is whether the claim of an answer admits logical connectives as operators of that core. The goal `audit-local-repairs` currently counts `and` written as an operator as a defect of the worked inquiries.

A grammar for propositional content must also state four constructs that the primitives of a programming language lack: quantification over an open domain, a condition or a regime under which a claim holds, approximate or conditional equality, and the distinction between using a claim and mentioning it.

**Literature.** None cited beyond the construct of algebraic data types.

**Bears on.** [`derivation-framework`](../../TODO.md).

## Statement modality

A statement need not assert its content. Two modalities appear in the test set:

- **A hypothetical statement.** A whole statement is conditional: "if such evidence held, it would mean Z" ([example 3](../../examples/adversarial-statements.md#^example-argument-with-an-undercutting-condition-hidden-inside-an-example), [example 4](../../examples/adversarial-statements.md#^example-research-question-embedded-in-a-critique)).
- **A counterfactual claim.** A claim concerns what a computation would have been under an intervention that did not take place. "The feature contributes to the task" unpacks as a claim about the computation without the feature ([example 37](../../examples/adversarial-statements.md#^example-statement-with-implicit-dependency-on-counterfactuals)). Such a claim has a meaning only relative to a family of admissible interventions.

The [attitude of a claim](../epistemology/definitions/representations/claim-and-hypothesis.md#^attitude-support), `entertained`, `hypothesized`, `accepted` or `retracted`, already marks a claim that is not asserted. The candidate concerns the content instead: a conditional claim can be accepted as a whole while its antecedent is not asserted, and a counterfactual claim must name its family of interventions.

**Literature.** None cited; the candidate derives from the statements of the test set.

**Bears on.** [`derivation-framework`](../../TODO.md).

## Proof objects

A proof is a structured record, not a prose field attached to a proposition. It holds steps, assumptions, and dependencies on mathematical objects, and one proposition may hold several proofs and several countermodels. A proof assistant separates elaboration, which turns a semi-formal statement into a formal object, from checking, which a small trusted kernel performs. The other concepts borrowed are the context (the active assumptions, definitions and notation), the term, the tactic (an operation from a goal to subgoals), the goal state, and the dependency graph.

The [decision on expression syntax](../adr/expression-syntax.md) declines the term language of a proof assistant, because `gnomon` specifies an inquiry without proving its claims. The structure of a proof, its steps, assumptions, goal states and dependencies, therefore remains a candidate, whereas mechanical checking belongs to a later formalization.

**Literature.** Proof assistants, with the background stated in [proof theory](../references/proof-theory.md) and [dependent type theory](../references/dependent-type-theory.md).

**Bears on.** [`derivation-framework`](../../TODO.md).

## Term rewriting with traces

A rewrite rule `l → r` replaces an expression that matches the pattern `l` by the expression `r`, and leaves a trace that records the source, the target, the rule and its justification. The rules cover normalizing a formula, expanding a definition, applying a theorem, translating a notation, refining a concept, compressing an argument and transforming a proof. A rewrite records a transformation that an author applied; no program applies the rules to derive content.

A rewrite can preserve meaning and still change what reads as explanatory. Rewriting the function of a network as a sum over paths makes some distributed effects look local, because locality moves from the units to the paths ([example 24](../../examples/adversarial-statements.md#^example-derivation-with-a-hidden-change-of-representation-language)). The trace must therefore also record this explanatory shift: what the new representation makes local, simple or salient, which the former one did not.

**Literature.** Term rewriting systems.

**Bears on.** [`derivation-framework`](../../TODO.md). The candidate first bore on the primitiveness of operations, now held by `research-actions`, as a kind of operation that transforms content.

## Format of a derivation step

A step of a derivation holds three fields, each of which answers its own question:

- the **warrant** states what licenses the step: the rule, the theorem or the definition applied;
- the **operative property** names the structural feature of the objects that makes the warrant apply at that step, such as the finiteness of an index set, which reduces an infinite intersection to a finite one;
- the **strategic function** states what the step achieves toward its subgoal, by exposing, eliminating, reducing or constructing.

A separability test checks the format: when the operative property and the strategic function restate the warrant, the step is not represented. A reader who follows the operative properties and the strategic functions alone can then reconstruct why the subgoal is reachable in the chosen direction.

A step also transforms a proof state, made of the target, the facts available and the obstacle that blocks an immediate conclusion. The step records the state before and after, so its change shows which facts became available and which obstacle disappeared. The obstacles recur: a target too complex, a mismatch of syntactic form, a hidden existential quantifier, a missing witness or bound, a dependence on several cases, an invariant not yet isolated, and facts stated in the wrong vocabulary. The progress of a step takes one of a few forms: a compound goal split into subgoals, a target rewritten to match an available theorem, a component extracted from a conjunction, a witness introduced for an existential goal, an expression normalized, an exhaustive partition into cases, and a global property replaced by a local criterion. The reason for a move differs from its warrant: the warrant states why the step is valid, and the reason states why the step is relevant at that point. The [proof objects](#proof-objects) already hold the goal state, and the [grammars for the rationale of a step](research-corrections.md#grammars-for-the-rationale-of-a-step) give the reason a grammar; the candidate adds the operative property, the obstacle and the typed progress.

**Literature.** Steiner's account of mathematical explanation, in which an explanatory proof rests on a characterizing property of the objects involved.

**Bears on.** [`derivation-framework`](../../TODO.md).

**Retired source.** `docs/design/_backup/arguments-reasoning/derivation-proof-encoding-C.md` and `docs/design/_backup/arguments-reasoning/derivation-proof-encoding-G.md`, at commit 9e138e2.

## Closed vocabulary of moves

The moves of a derivation fall in four families:

- **structural** moves reorganize the target or the facts without adding information: `unfold_definition`, `fold_definition`, `decompose_goal`, `decompose_fact`, `rephrase_goal`, `normalize_expression`;
- **transport** moves carry information through a rule or a map: `instantiate_rule`, `specialize_hypothesis`, `transport_along_equivalence`, `monotonic_transfer`, `substitute_equals`;
- **search** moves create a missing object or a structure of cases: `introduce_witness`, `choose_parameter`, `split_cases`, `introduce_auxiliary_claim`, `introduce_invariant`;
- **closure** moves complete a prepared derivation: `apply_criterion`, `derive_contradiction`, `aggregate_subresults`, `discharge_assumption`.

A structural move needs no operative property, so the cost of annotating a step follows its content. A compression rule lets a step omit its obstacle and its reason only when the move is terminally obvious: the target matches a standard rule, no alternative move is plausible, and the progress is immediate and unique. These moves act inside a derivation, whereas the [moves that improve an idea](research-actions.md#moves-that-improve-an-idea) act on research content as a whole.

**Literature.** None cited.

**Bears on.** [`derivation-framework`](../../TODO.md).

**Retired source.** `docs/design/_backup/arguments-reasoning/derivation-proof-encoding-G.md`, at commit 9e138e2.

## Kernel, segments and defects of a derivation

A kernel step is the conceptual core of a derivation: without it, the rest of the derivation is invalid or cannot be built by routine means. An isolation test checks a step flagged as kernel: once the step and every step that depends on it are removed, no path of the dependence graph leads from the premises to the conclusion. The test is a query of reachability over authored dependence, which the [decision against inference at run time](../adr/no-run-time-inference.md#^admitted-computation) admits.

Between the step and the whole derivation, a segment groups the contiguous steps that serve one subgoal, and names its strategy, such as a reduction to the finite-dimensional case by compactness, and the obstacles that it resolves. Three conditions make a derivation adequate:

- **C1**, the warrant of each step is stated at the right generality, neither restating the instance nor trivially permissive;
- **C2**, the reason for a step names a contrastive choice: why this inference rather than one salient alternative;
- **C3**, the subgoals form a well-founded tree rooted at the thesis, and a step that closes no assumption, discharges no obstacle and serves no segment is idle.

Six named defects make a derivation look arbitrary: a **blind step** has a warrant and no local reason; a **hidden obstacle** is a non-trivial rewrite without the obstacle that it removes; a **spurious move** is valid and makes no progress; a **teleological gap** is a move that does not aim at the current target; an **untyped transition** is a move outside the vocabulary of moves; and a **state ambiguity** leaves unclear which facts are active at a step.

An intermediate lemma becomes a unit with an identifier of its own. A consequence derived on the way to another result then has a record, which closes the gap that the [registry of product types](../../src/gnomon/data/registries/product-types.yml) states for the product `consequence`.

**Literature.** Kitcher's account of explanation by unification, for segments that instantiate one pattern across derivations.

**Bears on.** [`derivation-framework`](../../TODO.md), whose report of idle units C3 specifies.

**Retired source.** `docs/design/_backup/arguments-reasoning/derivation-proof-encoding-C.md`, `docs/design/_backup/arguments-reasoning/derivation-proof-encoding-G.md` and `docs/design/_backup/architecture-C.md`, at commit 9e138e2.
