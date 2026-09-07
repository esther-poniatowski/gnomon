---
tags:
  - reference
index: "[Methods for reasoning](_index.md)"
aliases:
  - Dependent type theory
---
## Domain II — Dependent Type Theory (Martin-Löf)

### II — Knowledge Model

The epistemic state is a **context** $\Gamma$, a sequence of variable-type bindings:

$$\Gamma = (x_1 : A_1,\ x_2 : A_2(x_1),\ \ldots,\ x_n : A_n(x_1, \ldots, x_{n-1}))$$

The key departure from proof theory: **types can depend on terms**. $A_2$ may depend on the value of $x_1$, not merely its type. This makes the context a **structured epistemic record** where each entry's meaning depends on prior entries — directly encoding conceptual dependence.

Under the **propositions-as-types** correspondence:

- A type $A$ is simultaneously a proposition and a set of its proofs
- A term $t : A$ is simultaneously a proof of proposition $A$ and an element of set $A$
- A dependent function type $\prod_{x:A} B(x)$ is simultaneously a universal statement $\forall x : A.\ B(x)$ and a function that, given an element of $A$, produces an element of $B(x)$

### II — Epistemic Entities

|Entity|Epistemic Role|
|---|---|
|**Type** $A : \mathcal{U}$|Proposition / concept / set|
|**Term** $t : A$|Proof / element / witness|
|**Dependent type** $B : A \to \mathcal{U}$|Predicate / parametric concept|
|**Universe** $\mathcal{U}_i$|Type of types at level $i$ — enables reflection|
|**Identity type** $\text{Id}_A(a, b)$|Proposition that $a$ and $b$ are equal in $A$; its inhabitants are proofs of equality|
|**$\Sigma$-type** $\sum_{x:A} B(x)$|Existential / dependent pair: "there exists $x:A$ such that $B(x)$"|

This allows **definition**, **theorem**, **proof**, and **construction** to be uniformly represented as typed terms — the unification claim in the framework's novelty claim 1 is partially realized here.

### II — State Evolution

Context extension: $\Gamma \to \Gamma, x : A$ when $\Gamma \vdash A : \mathcal{U}$ (a new concept/variable is introduced with well-typed type). This is the formal analogue of introducing a new concept into the reasoning.

Substitution: replacing $x$ by a term $t : A$ throughout yields a new context — the formal analogue of instantiation.

**Reduction** (computation): terms reduce according to $\beta$, $\eta$, and other rules. $(\lambda x.\ t)\ a \rightsquigarrow t[a/x]$. Reduction is **strongly normalizing** (in MLTT without unrestricted recursion), guaranteeing that every computation terminates — the type-theoretic analogue of cut-elimination.

### II — Step Selection

Proof construction in DTT proceeds by **goal-directed refinement** (as in Coq's tactic language):

1. Current state: a goal $\Gamma \vdash ?g : A$ (find a term of type $A$ in context $\Gamma$)
2. Apply a **tactic** that decomposes $A$ into subgoals, e.g.:
    - `intro x` when $A = \prod_{x:B} C(x)$: extends $\Gamma$ with $x : B$, new goal is $?g' : C(x)$
    - `apply f` when $f : B \to A$: new goal is $?g'' : B$
    - `exact t` when $t : A$: closes the goal
3. Tactics are selected by the human prover or by **proof search algorithms** (e.g., `auto`, `eauto` in Coq) that perform bounded backward chaining

The critical point: **tactic selection is the locus of mathematical understanding**. A skilled mathematician selects tactics based on structural recognition (this goal has the shape of a standard construction), analogy (this resembles a proof I know), and strategy (it is more efficient to work backwards from the goal). This is exactly what the proposed framework aims to represent explicitly — and DTT does not.