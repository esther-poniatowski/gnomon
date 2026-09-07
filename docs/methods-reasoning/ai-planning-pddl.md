---
tags:
  - reference
index: "[References and methods](_index.md)"
aliases:
  - Classical AI planning
---
## Domain III — Classical AI Planning (STRIPS / PDDL)

### III — Knowledge Model

The epistemic state (called the **world state**) is a **set of ground atoms** $s \subseteq \mathcal{L}$ where $\mathcal{L}$ is a first-order ground language. Under the **closed-world assumption**: $P \notin s \Rightarrow \neg P$ is true in $s$. Unknown propositions do not exist — the state is complete.

The planning problem is a triple $\langle s_0, \mathcal{A}, \mathcal{G} \rangle$:

- $s_0$: initial state
- $\mathcal{A}$: set of action schemas
- $\mathcal{G}$: goal condition (a set of literals that must hold)

### III — Epistemic Entities

|Entity|Definition|
|---|---|
|**State** $s$|Set of ground atoms currently true|
|**Action schema** $a$|A triple $\langle \text{pre}(a), \text{add}(a), \text{del}(a) \rangle$|
|**Ground action**|Instantiation of an action schema with concrete objects|
|**Plan** $\pi$|A sequence of ground actions $\langle a_1, \ldots, a_n \rangle$|
|**Goal** $\mathcal{G}$|A conjunctive condition on state atoms|

An action $a$ is **applicable** in state $s$ iff $\text{pre}(a) \subseteq s$. Application yields:

$$\text{apply}(a, s) = (s \setminus \text{del}(a)) \cup \text{add}(a)$$

This is the **STRIPS transition function** — deterministic, complete, and monotonic within a step (though the plan as a whole modifies state).

### III — State Evolution

A plan execution is a sequence of state transitions:

$$s_0 \xrightarrow{a_1} s_1 \xrightarrow{a_2} \cdots \xrightarrow{a_n} s_n$$

where $s_n \models \mathcal{G}$. Evolution is **fully deterministic** given action selection. There is no uncertainty, no defeasibility, no partial knowledge.

In PDDL extensions:

- **PDDL2.1**: numeric fluents and durative actions (temporal planning)
- **PDDL2.2**: derived predicates and timed initial literals
- **Contingent/conformant planning**: extends to partially observable or stochastic environments

### III — Step Selection

Plan synthesis is a **search problem** over the state space or plan space:

**Forward search** (progression): from $s_0$, apply applicable actions, explore reachable states toward $\mathcal{G}$. Step selection is guided by **heuristics**:

- $h^+$ (relaxed plan heuristic): estimate cost by ignoring delete effects
- $h^{\text{FF}}$: Fast-Forward heuristic, extracts a relaxed plan and uses its length
- $h^{\text{max}}$, $h^{\text{add}}$: max/additive cost-to-goal estimates

**Backward search** (regression): from $\mathcal{G}$, regress through action preconditions. Applicable when $\text{add}(a) \cap \mathcal{G} \neq \emptyset$; regression yields new subgoal $(\mathcal{G} \setminus \text{add}(a)) \cup \text{pre}(a)$.

**The critical structure**: in planning, **why** an action is selected is encoded in the **causal link** of the plan — action $a_i$ achieves precondition $p$ of $a_j$, expressed as $a_i \xrightarrow{p} a_j$. This causal structure is the planning-theoretic analogue of the "why" the proposed framework seeks, but it operates exclusively over propositional state changes — not over epistemic content or understanding.