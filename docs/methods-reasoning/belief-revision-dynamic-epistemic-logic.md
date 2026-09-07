---
tags:
  - reference
index: "[Methods for reasoning](_index.md)"
aliases:
  - Belief revision and dynamic epistemic logic
---
## Domain VI — Belief Revision and Dynamic Epistemic Logic

These two frameworks address **how epistemic states change** — the component most absent from the proposed architecture's current form.

### VI — AGM Belief Revision

**Knowledge model**: An epistemic state is a **belief set** $K$: a deductively closed set of sentences ($K = \text{Cn}(K)$ where $\text{Cn}$ is the consequence closure operator).

**Epistemic entities**:

|Operation|Notation|Definition|
|---|---|---|
|**Expansion**|$K + \phi$|$\text{Cn}(K \cup {\phi})$ — add $\phi$ unconditionally|
|**Contraction**|$K - \phi$|Remove $\phi$ from $K$ with minimal loss|
|**Revision**|$K * \phi$|Add $\phi$ to $K$ consistently, possibly retracting beliefs|

The **AGM postulates** (Alchourrón, Gärdenfors, Makinson 1985) axiomatize rational revision. The **Levi identity** connects them: $K * \phi = (K - \neg\phi) + \phi$ — first contract the negation, then expand with the new belief.

**Grove sphere semantics**: belief sets are represented as nested spheres of possible worlds ordered by "closeness" to the current epistemic state. Revision with $\phi$ selects the closest $\phi$-world(s).

**State evolution**: the three operations define how a belief set transforms upon receiving new information. This is the formalism for representing **epistemic gain** as a state transition — exactly what the proposed framework lacks.

### VI — Dynamic Epistemic Logic (DEL)

**Knowledge model**: A **Kripke model** $\mathcal{M} = \langle W, \sim_i, V \rangle$ where:

- $W$ is a set of possible worlds
- $\sim_i$ is an accessibility relation for agent $i$ (worlds $i$ considers epistemically possible)
- $V$ assigns truth values to propositions at each world

**Epistemic entities**:

|Entity|Semantics|
|---|---|
|$K_i \phi$|Agent $i$ knows $\phi$ (true in all worlds $i$-accessible from current world)|
|$B_i \phi$|Agent $i$ believes $\phi$ (true in most plausible accessible worlds)|
|**Public announcement** $!\phi$|Updates all agents: eliminate worlds where $\phi$ is false|
|**Action model**|Encodes complex epistemic events (private communications, deceptive actions)|

**State evolution** under a public announcement $!\phi$:

$$\mathcal{M} | \phi = \langle W^\phi, \sim_i^\phi, V^\phi \rangle$$

where $W^\phi = {w \in W \mid \mathcal{M}, w \models \phi}$ — worlds inconsistent with $\phi$ are eliminated. This models **learning** as possible-world elimination.

**Step selection**: DEL models _how_ epistemic states change under communicative and observational events. It does not model strategic selection of what to investigate next — but it provides the formal semantics for what it means to **gain knowledge** at each step, which is precisely the epistemic gain representation the proposed framework requires.