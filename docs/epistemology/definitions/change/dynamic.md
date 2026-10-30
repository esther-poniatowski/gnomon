---
tags:
  - definition
  - wip
index: "[Change](docs/epistemology/definitions/change/_index.md)"
aliases:
  - Dynamic
  - Dynamics
  - Evolution map
  - Law of evolution
---
# Dynamic

> [!QUESTION] Goal: what does a dynamic fix about a system, and how does it differ from a process, a law and a mechanism?

A **dynamic** is the rule by which the state of a system changes. For a deterministic and autonomous system, the dynamic is written as an evolution map
$$\varphi:\mathbb{T}\times\mathcal{X}\to\mathcal{X},\qquad \varphi(0,x)=x,\qquad \varphi(t+s,x)=\varphi(t,\varphi(s,x)),$$
over a time set $\mathbb{T}$ and a [state space](../quantities/state-and-configuration.md) $\mathcal{X}$. The map is a construct, stated over a chosen state space. In realist ontology, the pattern of change that it represents is the *law of evolution* of a thing [bunge1977], a law in the pattern sense.

## Senses

| Form | Time set $\mathbb{T}$ | Statement | Example |
| --- | --- | --- | --- |
| Flow | $\mathbb{R}$ | an ordinary differential equation $\dot x=F(x)$, whose solutions define $\varphi$ | a rate model of a neural population |
| Map | $\mathbb{Z}$ or $\mathbb{N}$ | an iterated function $x_{n+1}=g(x_n)$ | one step of gradient descent |
| Stochastic dynamic | $\mathbb{R}$ or $\mathbb{N}$ | a transition kernel, or a stochastic differential equation | a neuron driven by noise |

The dynamic **generates** the histories of the system. Each [history](process-event-history.md#^history) is a segment of an orbit $t\mapsto\varphi(t,x_0)$, and each process shown by the system is a predicate satisfied by some of those segments.

## Distinctions

Four terms are often used for one another. The four terms differ in their type and in the information required by each:

| Term | Type | Requires a decomposition into constituents? | Example for a population oscillation |
| --- | --- | --- | --- |
| [Process](process-event-history.md#^process) | a predicate on trajectory segments, satisfied by histories | no | the population rate oscillates |
| Dynamic | a rule that generates trajectories | no | $\dot r=-r+\phi(Wr+u)$ over an aggregate rate $r$, with an external input $u$ |
| [Law](../regularities/law.md) | an invariant pattern among states, or the statement of it | no | the period depends on the time constant alone |
| [Mechanism](../regularities/mechanism-and-mechanistic-model.md) | organized constituents and activities that produce a phenomenon | yes | excitatory and inhibitory neurons in a delayed feedback loop |

- **A dynamic and a law can be stated over variables alone, whereas a mechanism requires a decomposition.** A dynamic over an aggregate rate names no constituent, whereas a mechanism names the constituents that engage in its activities. The decomposition is the test of [mechanistic form](../regularities/mechanism-and-mechanistic-model.md#^mechanistic-model-test), and a model that fails it is phenomenological. ^decomposition-test
- **A law need not be a dynamic.** A conservation law and an equation of state constrain the states that may hold together, and neither generates a trajectory.
- **A dynamic is global, and an activity is local.** Each term of an additive decomposition of the dynamic is read as a candidate activity in the [vocabulary of activity](mechanistic-activity.md#^activity-term).
- **A causal structure need not be a dynamic.** A causal structure states which variables change under an intervention on a given variable [woodward2003]. Such dependencies need not form a rule of change in time, and some mechanistic descriptions admit no representation by local differential equations. Therefore, a dynamic is one realization of a causal structure. ^causal-structure

## Relations to the method

- **A dynamic is a law with the role *evolution*.** Among the roles of a law, which the [background record](../../subject/background.md#^laws) lists, only the role *evolution* generates trajectories.
- **A causal answer may state no law of evolution.** A [causal structure](#^causal-structure) need not be a dynamic, so a record may state how the explanandum depends on interventions, without any law with the role *evolution*.

---
## Sources

Marks follow the [legend of reading marks](../../../../CONTRIBUTING.md#^reading-marks).

- [bunge1977] ◐ [Bunge, *Treatise on Basic Philosophy*, vol. 3, *Ontology I: The Furniture of the World*, Reidel, 1977](https://doi.org/10.1007/978-94-010-9924-0)
- [woodward2003] ◐ [Woodward, *Making Things Happen: A Theory of Causal Explanation*, Oxford University Press, 2003](https://doi.org/10.1093/0195155270.001.0001)
