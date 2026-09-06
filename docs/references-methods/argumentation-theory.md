---
tags:
  - reference
index: "[References and methods](_index.md)"
aliases:
  - Argumentation theory
---
## Domain V — Argumentation Theory

### V — Knowledge Model

#### Dung Abstract Argumentation (1995)

The epistemic state is an **argumentation framework** $\mathcal{AF} = \langle \mathcal{A}, \mathcal{R} \rangle$ where:

- $\mathcal{A}$ is a set of **arguments** (atomic, no internal structure)
- $\mathcal{R} \subseteq \mathcal{A} \times \mathcal{A}$ is the **attack relation**: $(A, B) \in \mathcal{R}$ means $A$ attacks $B$

No claim content is represented. The framework reasons about **dialectical status**: which arguments survive under attack.

#### ASPIC+ (Structured Argumentation)

The epistemic state is richer:

- **Knowledge base** $\mathcal{K}$: a set of formulas partitioned into strict ($\mathcal{K}_n$) and defeasible ($\mathcal{K}_p$) premises
- **Rule set** $\mathcal{R}$: strict rules ($A_1, \ldots, A_n \Rightarrow C$, cannot be attacked) and defeasible rules ($A_1, \ldots, A_n \Rightarrow C$, can be attacked via undercutting or rebuttal)
- **Preference ordering** $\leq$ over arguments: determines which attacks succeed as **defeats**

### V — Epistemic Entities

|Entity|Definition|
|---|---|
|**Argument** $A$|In ASPIC+: a tree of rule applications from $\mathcal{K}$ to a conclusion $\text{conc}(A)$|
|**Attack**|Rebuttal (attack on conclusion), undercutting (attack on rule application), undermining (attack on defeasible premise)|
|**Defeat**|An attack that succeeds given the preference ordering|
|**Extension** $E \subseteq \mathcal{A}$|A maximal set of mutually acceptable arguments|
|**Warrant** (Toulmin)|The general rule or principle licensing the step from grounds to claim|
|**Backing**|The epistemic support for the warrant itself|
|**Rebuttal**|A defeating counterargument or exception|

Dung's semantics define what counts as an acceptable set of arguments:

- **Conflict-free**: $E$ contains no arguments that attack each other
- **Defense**: $E$ defends every $A \in E$ (attacks on $A$ are counter-attacked by $E$)
- **Complete extension**: conflict-free + defends all its elements + contains all defended arguments
- **Grounded extension**: the minimal complete extension (skeptical semantics)
- **Preferred extension**: maximal complete extensions (credulous semantics)

### V — State Evolution

Argumentation state evolution occurs via **argument addition** and **preference revision**:

- Adding a new argument $B$ may attack existing arguments and alter which extensions are admissible
- Revising preferences $\leq$ may change which attacks become defeats

In **dialogue-based argumentation** (Walton's dialogue types: persuasion, inquiry, negotiation, deliberation, information-seeking, eristic):

- Two agents alternately put forward arguments and counterarguments
- The dialogue terminates when no new arguments are available or a resolution condition is met
- The **burden of proof** governs which party must provide arguments at each stage

This is the argumentation-theoretic representation of **reasoning dynamics** — the temporal unfolding of argument construction and revision under adversarial or collaborative dialogue. For the proposed framework, this models the evolution of _justificatory support_ for schema selections over the course of reasoning.

### V — Step Selection

In formal argumentation, "step selection" corresponds to the choice of which argument to construct or advance next. This is governed by:

- **Dialogue protocol**: the legal move set at each stage (which types of arguments are permitted in response to the current argument)
- **Strategic reasoning** (Dung/Riveret/Bench-Capon): selecting arguments that maximize the probability of achieving a winning position — an explicit model of _argumentative strategy_
- **Relevance**: a new argument must attack or support an argument already in play (prevents arbitrary insertion)

The **critical point for the framework**: argumentation theory provides a formal model of **why a particular justificatory move is selected** — it must respond to an existing attack or advance a defensive position. This is the closest existing formal model to the "why is this step introduced" requirement of R1.