---
tags:
  - definition
  - wip
index: "[Quantities and states](docs/epistemology/vocabulary/quantities/_index.md)"
aliases:
  - State, state space and configuration
  - State
  - State space
  - Configuration
---
# State, state space and configuration

> [!QUESTION] Goal: when does a set of values count as the state of a system, and how does a state differ from a configuration?

A **state** is the tuple of values that the state variables of a thing take at one time [bunge1977]:
$$F(t)=\langle F_1(t),\ldots,F_n(t)\rangle$$
The **state space** $\mathcal{X}$ is the set of tuples that the thing can take. When the laws of the thing exclude some tuples, the remaining set is its *lawful* state space [bunge1977].

## Senses

| Term | Community | Definition | Source |
| --- | --- | --- | --- |
| State | realist ontology | the tuple of values of the state variables of a thing at one time; its lawful state space holds the tuples admitted by the laws | [bunge1977] |
| State | dynamical systems | a point $x\in\mathcal{X}$ that, together with the dynamic, fixes every later point | — |
| Microstate, macrostate | statistical mechanics | a state over the variables of every constituent; a state over aggregate variables, realized by many microstates | — |
| State | quantum mechanics | a density operator, assigning a probability distribution to the outcomes of each observable; not itself a measured value | — |
| Configuration | classical mechanics | the values of the generalized coordinates $q$; the configuration space holds $q$, whereas the phase space holds the pairs $(q,p)$ | [goldstein2002] |
| Configuration | general usage | the arrangement of the constituents of a system at one instant | — |

The senses share one relativity: **a state is a state relative to chosen variables**. The same gas has a microstate over the positions and momenta of its molecules, and a macrostate over its pressure, volume and temperature.

## Distinctions

- **A configuration is part of a state.** The test is completeness: a set of values is a *complete*, or Markovian, state when the dynamic and those values fix every later value. In mechanics, the configuration $q$ fails the test, since two systems with the same positions and different momenta evolve differently. The pair $(q,p)$ passes the test. ^completeness-test
- **A state fixes no measured value in quantum mechanics.** The quantum state fixes the distributions of the outcomes, so a state and a measured value are distinct objects. In classical mechanics, by contrast, an ideal measurement reads a value of the state directly.
- **A configuration differs from a pattern by the number of instances.** The criterion is stated in the [vocabulary of patterns](../regularities/pattern-and-phenomenon.md).

## Relations to the method

- **The [completeness test](#^completeness-test) checks a declared state space against the laws.** A law with the role *evolution* can be written as a first-order rule on the declared variables only when the state passes the test. When the state fails the test, the record lacks a variable, such as a momentum, a delay line or a synaptic trace, or the evolution law must carry memory.
- **A macrostate is admissible only when interventions on it have unambiguous effects.** A phenomenon stated over aggregate variables groups many microstates. The [admissibility of aggregates](../../objects/subject/target-system.md#^aggregate-admissibility) requires that each intervention on the aggregate correspond to interventions on those microstates.

---
## Sources

Marks follow the [legend of reading marks](../../../../CONTRIBUTING.md#^reading-marks).

- [bunge1977] ◐ [Bunge, *Treatise on Basic Philosophy*, vol. 3, *Ontology I: The Furniture of the World*, Reidel, 1977](https://doi.org/10.1007/978-94-010-9924-0); ch. 3, "Thing", section "State"; the lawful state space is listed in the subject index and was checked through secondary sources
- [goldstein2002] ◐ [Goldstein, Poole & Safko, *Classical Mechanics*, 3rd ed., Addison-Wesley, 2002](https://www.pearson.com/en-us/subject-catalog/p/classical-mechanics/P200000006871/9780201657029)
