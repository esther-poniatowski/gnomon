---
tags:
  - reference
index: "[Methods for reasoning](_index.md)"
aliases:
  - Formal reasoning domains overview
---

# Internal Workings of Formal Reasoning Domains

## Organizational Schema

For each domain, four questions are addressed with technical precision:

1. **Knowledge model** — what constitutes the epistemic state; what entities are primitive
2. **Epistemic entities** — the typed objects the formalism manipulates
3. **State evolution** — how the knowledge state changes under reasoning
4. **Step selection** — the mechanism by which the next reasoning step is determined

Six domains are covered: proof theory, dependent type theory, classical AI planning, hierarchical task network planning, argumentation theory, and belief revision / dynamic epistemic logic.

## Comparative Analysis Across Domains

| Domain                | Epistemic State                   | Reasoning Step                     | Step Selection Mechanism                  | Handles "Why"                       |
| --------------------- | --------------------------------- | ---------------------------------- | ----------------------------------------- | ----------------------------------- |
| Natural deduction     | Context $\Gamma$, goal $\phi$     | Rule application                   | External (human / heuristic search)       | Intro/elim semantics only           |
| Dependent type theory | Typed context $\Gamma$, goal type | Tactic application                 | Goal-directed refinement                  | No — pragmatics external            |
| STRIPS/PDDL           | Ground atom set                   | Action application                 | Heuristic forward/backward search         | Causal links only                   |
| HTN planning          | World state + task network        | Decomposition / execution          | Method matching + precondition filter     | Decomposition tree                  |
| Dung / ASPIC+         | Argumentation framework           | Argument construction              | Dialogue protocol + strategy              | Warrant / backing                   |
| AGM revision          | Deductively closed belief set     | Expansion / contraction / revision | Rational postulates (no procedural model) | Minimal change principle            |
| DEL                   | Kripke model over worlds          | Announcement / action              | Event model application                   | Epistemic gain as world elimination |

## What No Existing Domain Provides

No existing formalism simultaneously provides:

1. **Stratified justification** — encoding of "why" at each granularity from strategic orientation to atomic derivation
2. **Partial specification tolerance** — admitting incompletely specified concepts and arguments as legitimate intermediate objects
3. **Unified validity conditions** — a single semantic framework that can accommodate both monotonic proof-theoretic steps and defeasible argumentative steps without forcing a choice between them
4. **Procedural epistemic gain** — a formal representation of the transition from not-understanding to understanding, not merely from not-knowing to knowing

This maps precisely onto the proposed framework's stated objectives — and confirms that the novelty claims are correctly positioned relative to the formal landscape, provided the interface problems identified in the prior adversarial evaluation are resolved.

---

## Evaluation of Novelty Claims

| Dimension                      | Assessment                                                                       |
| ------------------------------ | -------------------------------------------------------------------------------- |
| **Novelty claim 1**            | Partially novel; must be positioned precisely against DTT and its limits         |
| **Novelty claim 2**            | Genuinely novel as a systematic requirement; not yet architecturally realized    |

### Unified Formalism for Mathematical and Conceptual Reasoning

#### Precise Positioning of the Claim

This claim is **partially novel** but requires sharper positioning against existing work that partially addresses it.

**Martin-Löf Dependent Type Theory (DTT)** already achieves a form of this unification. Under the Curry-Howard-Lambek correspondence, propositions are types, proofs are terms, and the same formal language can express both:

- Mathematical proofs: as typed derivations
- Conceptual definitions: as type formation rules and introduction rules
- Structural properties: as dependent types

Systems such as Coq, Agda, and Lean operationalize this. The framework must explicitly confront what it provides that DTT does not — otherwise it risks reinventing a fragment of dependent type theory with weaker foundations.

**What DTT cannot do** — and where genuine space exists:

- DTT requires complete formalization. Conceptual reasoning in philosophy and empirical science operates under **partial specification**: concepts are introduced before their full formal characterization is available.
- DTT has no native representation of **why a definition is introduced** — only that it is well-typed. The justificatory pragmatics of concept introduction are external to the type theory.
- DTT handles classical mathematical reasoning but is poorly suited to **abductive**, **analogical**, or **defeasible** inference, which are constitutive of empirical and conceptual research.

**Precise novelty claim 1 should therefore be restated as**: unification of formal and informal reasoning under a framework that tolerates **partial specification**, handles **defeasibility**, and represents **justificatory pragmatics** — not merely logical structure. This is a genuine gap that DTT does not fill.

#### Granularity Alignment Problem

Even granting the novelty, unification introduces a structural tension. Mathematical proof and conceptual reasoning differ not merely in formality but in **granularity norms**:

- A proof step is admissible when it follows by a rule with finite explicit warrant.
- A conceptual move (e.g., introducing a new frame, adopting a theoretical analogy) is admissible when it is **epistemically motivated** — a far weaker and context-dependent condition.

A unified formalism must either:

- **Stratify** the two reasoning types under a common meta-language with distinct validity conditions at each stratum, or
- **Reduce** one to the other — which either over-formalizes conceptual reasoning or under-specifies mathematical proof

The framework currently does neither. This is a design decision that must be made explicit before the synthesis program can proceed.

### Explicit Representation of "Why" at Each Granularity Level

#### Stronger and More Original Claim

No existing formalism systematically enforces explicit justificatory representation at each granularity level simultaneously. To be precise about what exists:

|Formalism|What it captures|What it omits|
|---|---|---|
|Natural deduction|Why a rule is applied (intro/elim semantics)|Why the goal was chosen; why this proof strategy|
|Toulmin model|Why a claim is made (warrant, backing)|Granularity below claim level; mathematical derivation|
|Lakatos (Proofs and Refutations)|Why a proof is revised (counterexample dynamics)|Operational architecture; formal derivations|
|Kitcher (explanatory unification)|Why an explanation is satisfying (argument patterns)|Procedural structure; conceptual reasoning dynamics|
|PDDL|Why an action is performed (preconditions, goal contribution)|Epistemic content; understanding; informal reasoning|

The proposed framework targets the **intersection of all omissions** — which is a genuine gap. However, "enforcing explicit representation of why at each level" is not itself an architecture — it is a **requirement** that the architecture must satisfy. The adversarial question is whether the tripartite synthesis actually produces mechanisms for satisfying it, or merely relocates the problem.

#### "Why" Regress at Each Level

Representing "why" at each granularity level generates a structured regress of justificatory demands:

- Why is this **operation schema** applied? → Justified by the Work Unit's goal
- Why is this **Work Unit's goal** adopted? → Justified by the Planning Schema
- Why is this **Planning Schema** selected? → Justified by... what?
- Why is this **Question** the right question? → Justified by... what?

The framework as specified terminates justification at the Planning Schema level without representing the **research orientation** that selects among competing schemas. This is the layer at which genuine epistemic gain is located for a researcher: the strategic insight that _this_ decomposition is productive, not merely that it is formally valid.

Argumentation theory can partially address this — warrants and backings can represent why a schema was selected — but this requires the argumentation layer to operate **above** the planning layer, not merely alongside the execution layer. The architectural positioning of argumentation theory therefore needs revision.

## Coherence of the Tripartite Synthesis

The proposed assignment of roles is:

| Dimension                | Proposed role                                              | Assessment                                                                       |
| ------------------------ | ---------------------------------------------------------- | -------------------------------------------------------------------------------- |
| **Proof theory**         | Atomic operations, derivation steps                        | Correctly scoped; requires epistemic extension for non-monotonic contexts        |
| **Argumentation theory** | Understanding-bearing constructs, justificatory pragmatics | Must be positioned above planning, not alongside execution                       |
| **AI planning**          | Operational architecture, goal-to-subgoal decomposition    | Requires epistemic PDDL extension; closed-world assumption is incompatible as-is |

### Interface Problems 

#### Monotonicity vs. Defeasibility

Proof theory is **monotonic**: in a sequent calculus or natural deduction system, $\Gamma \vdash \phi$ implies $\Gamma, \psi \vdash \phi$ for any $\psi$. The derivation relation is preserved under premise addition.

Argumentation theory is **non-monotonic**: an argument $A$ for conclusion $\phi$ can be defeated by a counterargument $B$, and adding $B$ to the argument set can retract $\phi$. This is structurally required to represent conceptual revision, defeasible inference, and hypothesis elimination.

A synthesis that uses both in a single framework must specify, at every node of the reasoning graph, which validity regime applies. If a Work Unit contains proof-theoretic operations, its outputs are monotonically valid. If a Work Unit contains argumentation-theoretic constructs, its outputs are defeasibly valid. **The interface between these two zones is undefined in the current proposal** and constitutes a semantic fault line.

Concretely: when a defeasible argument supplies a warrant for a planning schema selection, and that argument is later defeated, does the planning schema get retracted? Does the Work Unit it generated get invalidated? The framework cannot answer this without a formal revision semantics that spans both logical regimes.

#### PDDL Closed-World Assumption vs. Epistemic Open World

Classical PDDL planning operates under the **closed-world assumption**: anything not known to be true is false. This is appropriate for robotic action planning where the state space is finite and enumerable.

Epistemic reasoning operates under an **open-world assumption**: unknown propositions are neither true nor false — they are targets of inquiry. A framework for research reasoning must represent states of **incomplete knowledge** as first-class objects, not as absences.

Using PDDL-style precondition-effect structures for epistemic state transitions will generate systematic errors: operation schemas whose preconditions include "evidence $E$ supports hypothesis $H$" will be incorrectly evaluated as inapplicable whenever $E$ is not yet in the epistemic object store, rather than correctly evaluated as _pending_ or _requiring investigation_.

An epistemic PDDL would require at minimum:

- Epistemic operators: $K\phi$ (known), $B_p \phi$ (believed with probability $p$), $?\phi$ (unknown)
- Revision operators: $+\phi$ (update), $-\phi$ (contraction), following AGM belief revision theory
- Goal conditions expressible over epistemic states, not just object states

This is a substantial extension of standard PDDL, and the framework must either adopt it explicitly or specify an alternative planning substrate.

#### Granularity Mismatch

The three formalisms operate at incommensurable granularities by default:

- Proof theory operates at the level of **individual inference steps** (one rule application)
- AI planning operates at the level of **action sequences over state spaces** (multi-step plans)
- Argumentation theory operates at the level of **claims with justificatory support structures** (potentially spanning entire arguments)

A synthesis requires explicit **granularity bridges**: specifications of how a planning-level action decomposes into proof-theoretic steps, and how an argumentation-level warrant licenses a planning-level schema. Without these bridges, the three layers are architecturally adjacent but not formally integrated — they constitute three separate formalisms applied to different parts of the object, not a unified system.

### Requirements for a Viable Synthesis Program

The tripartite synthesis is **architecturally plausible** but **not yet formally coherent**. For it to be realized as a unified system, the following must be resolved:

### Common Semantic Substrate

All three formalisms must operate over a shared representation layer. A candidate is a **typed epistemic state space** $\mathcal{E}$, where:

$$\mathcal{E} = \langle O, R, J, \partial \rangle$$

- $O$: typed epistemic objects (concepts, claims, models, evidence)
- $R$: relations over $O$ (support, defeat, dependency, instantiation)
- $J$: justificatory annotations (warrant source, strength, defeasibility status)
- $\partial$: a revision operator on $\mathcal{E}$ following AGM postulates

Proof-theoretic operations would be transitions $\mathcal{E} \to \mathcal{E}'$ that are monotonic over $O$. Argumentation-theoretic constructs would be structures over $R$ and $J$. Planning schemas would be policies over $\mathcal{E}$.

### Formal Granularity Stratification

Define a stratification $L_0 \subset L_1 \subset L_2$ where:

- $L_0$ (proof-theoretic): atomic derivation steps with explicit rule schemas
- $L_1$ (planning): goal-decomposition schemas with preconditions over $L_0$ outputs
- $L_2$ (argumentation): justificatory structures that license $L_1$ schema selection and carry epistemic gain annotations

The "why" requirement is then formalized as: every $L_1$ node must carry a $L_2$ warrant; every $L_0$ node must carry an $L_1$ goal attribution. This makes the requirement structurally enforced, not merely aspirational.

### Revision Propagation Semantics

Specify how revision at each layer propagates downward:

- $L_2$ argument defeat → schema retraction at $L_1$
- $L_1$ goal revision → Work Unit invalidation or re-instantiation at $L_0$
- $L_0$ derivation failure → goal revision trigger at $L_1$

This transforms the unidirectional cascade of the current architecture into a **bidirectional revision network**, which is necessary for the framework to represent actual research reasoning.

