---
tags:
  - reference
index: "[References and methods](_index.md)"
aliases:
  - Proof theory
---
## Domain I — Proof Theory (Natural Deduction and Sequent Calculus)

### I — Knowledge Model

The epistemic state is a **sequent**: a pair $(\Gamma, \Delta)$ where $\Gamma$ is the set of current assumptions (the context) and $\Delta$ is the set of goals or derived conclusions. In natural deduction, the single-conclusion variant gives $\Gamma \vdash \phi$, read: under assumptions $\Gamma$, formula $\phi$ is derivable.

The context $\Gamma$ is **local to a proof branch** — it can be extended by assumption introduction and contracted by discharge. It is not a global epistemic state: it represents what is _available_ for derivation in a given subproof, not what is _known_ in a broader sense.

### I — Epistemic Entities

|Entity|Definition|
|---|---|
|**Formula** $\phi$|A well-formed expression in the object language ($\wedge, \vee, \rightarrow, \forall, \exists$)|
|**Judgment** $\Gamma \vdash \phi$|A claim that $\phi$ is derivable from $\Gamma$|
|**Proof term** (under Curry-Howard)|A typed $\lambda$-term $t : \phi$ witnessing the derivability|
|**Assumption**|A formula $\phi \in \Gamma$, possibly dischargeable|
|**Derivation tree**|A finite tree of judgments connected by rule applications|

No representation of _why_ a goal is chosen, _why_ a rule is selected, or _what is understood_ exists at this level. The formalism is purely **validity-tracking**.

### I — State Evolution

A derivation is constructed by applying **inference rules**, which are schemas of the form:

$$\frac{\Gamma_1 \vdash \phi_1 \quad \cdots \quad \Gamma_n \vdash \phi_n}{\Gamma \vdash \phi} \text{ (rule name)}$$

In natural deduction, rules come in pairs:

- **Introduction rules** ($\phi$-I): construct a proof of $\phi$ from subproofs of its components
- **Elimination rules** ($\phi$-E): extract consequences from a proof of $\phi$

Example for $\wedge$:

$$\frac{\Gamma \vdash \phi \quad \Gamma \vdash \psi}{\Gamma \vdash \phi \wedge \psi} \wedge\text{-I} \qquad \frac{\Gamma \vdash \phi \wedge \psi}{\Gamma \vdash \phi} \wedge\text{-E}_1$$

State evolution is **monotonic**: the derivation tree grows; no previously derived judgment is retracted. The derivation is complete when all open leaves (subgoals) are closed by axiom rules ($\Gamma, \phi \vdash \phi$).

In **sequent calculus** (Gentzen's LK/LJ), both antecedent and succedent are explicit, and rules operate on the structure of both sides simultaneously. This makes structural properties (weakening, contraction, exchange) explicit, and the **cut rule**:

$$\frac{\Gamma \vdash \phi \quad \phi, \Delta \vdash \psi}{\Gamma, \Delta \vdash \psi} \text{ cut}$$

is the central composition principle. **Cut-elimination** (Gentzen's Hauptsatz) proves that every derivation using cut has a cut-free equivalent — this is the proof-theoretic analogue of removing lemmas and is the foundational termination result.

### I — Step Selection

In proof theory as a **formalism**, step selection is not specified — it is the task of the prover (human or automated). The formalism defines _what is valid_, not _what to try next_.

In **automated theorem proving** (resolution-based, e.g., Robinson 1965), step selection is governed by:

- **Unification**: determining whether two formulas can be made identical by substitution
- **Resolution strategy**: (hyperresolution, set-of-support, ordered resolution) — heuristic orderings on which clauses to resolve first
- **Proof search as graph search**: the search space is the set of all derivable sequents; strategies (BFS, DFS, A*, DPLL for propositional logic) navigate this space

The **inference rules do not themselves encode why a step is taken** — strategy is external to the formalism.