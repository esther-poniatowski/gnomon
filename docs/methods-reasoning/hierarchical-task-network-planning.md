---
tags:
  - reference
index: "[Methods for reasoning](_index.md)"
aliases:
  - Hierarchical task network planning
---
## Domain IV — Hierarchical Task Network Planning (HTN)

HTN planning is the planning substrate most directly relevant to the proposed framework's goal decomposition layer, and merits separate treatment.

### IV — Knowledge Model

HTN planning distinguishes **primitive tasks** (directly executable actions, equivalent to PDDL actions) from **compound tasks** (abstract tasks requiring decomposition). The epistemic state is augmented with a **task network** $T$: a partially ordered set of tasks with causal and ordering constraints.

### IV — Epistemic Entities

|Entity|Definition|
|---|---|
|**Primitive task**|Ground action with preconditions and effects|
|**Compound task**|Abstract task with no direct execution semantics|
|**Method** $m$|A decomposition rule: compound task $\to$ task network|
|**Task network**|A partial order of tasks with constraints|
|**Decomposition tree**|The record of which methods were applied|

A method $m$ has the form:

$$m = \langle \text{task}(m),\ \text{pre}(m),\ \text{subtasks}(m),\ \text{constraints}(m) \rangle$$

meaning: to achieve $\text{task}(m)$ when $\text{pre}(m)$ holds, replace it with the network $\text{subtasks}(m)$ subject to $\text{constraints}(m)$.

### IV — State Evolution

HTN planning interleaves **decomposition** (replacing compound tasks by subtask networks) and **execution** (applying primitive tasks to world states). The dual evolution is:

$$\langle s, T \rangle \xrightarrow{\text{decompose } m} \langle s, T' \rangle \quad \text{(task refinement, no state change)}$$ $$\langle s, T \rangle \xrightarrow{\text{execute } a} \langle s', T \setminus {a} \rangle \quad \text{(state transition, task consumed)}$$

The plan is complete when the task network contains only primitive tasks all of which have been executed.

### IV — Step Selection

Step selection involves two interleaved choices:

1. **Method selection**: which method to apply to decompose a compound task — governed by precondition satisfaction and heuristic preferences among applicable methods
2. **Task selection**: which task in the network to execute or decompose next — governed by ordering constraints and conflict detection

The **decomposition tree** records the full hierarchical structure of the plan. This is structurally isomorphic to the proposed framework's Goal → Subgoal graph. However, in HTN, the decomposition is driven by **syntactic pattern matching** (does the compound task name match the method's task name?) with **semantic filtering** (are the preconditions satisfied?). The framework's planning schemas correspond precisely to HTN methods — but the proposed framework lacks the notion of **task/method typing** (the compound task name that triggers method selection), which is what makes HTN decomposition non-arbitrary.