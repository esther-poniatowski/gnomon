---
tags:
  - definition
  - wip
index: "[Change](docs/epistemology/vocabulary/change/_index.md)"
aliases:
  - Computation
  - Function computed
  - Canonical computation
  - Implementation map
---
# Computation

> [!QUESTION] Goal: does a statement about a computation name the function computed, the algorithm, the implementation or the process of computing, and when does a physical system implement a computation?

A **computation** is described at three levels [marr1982]:

- the *function computed*: a map from inputs to outputs, together with its goal;
- the *algorithm*: a representation of the inputs and outputs, and a sequence of abstract states that produces the map;
- the *implementation*: the physical process that realizes the algorithm.

## Senses

| Term | Community | Definition | Source |
| --- | --- | --- | --- |
| Computational level | cognitive science | the function computed and the reason for computing it | [marr1982] |
| Algorithmic level | cognitive science | the representation of the inputs and outputs, and the algorithm that transforms one into the other | [marr1982] |
| Implementational level | cognitive science | the physical realization of the representation and of the algorithm | [marr1982] |
| Implementation | philosophy of mind | a physical system implements an automaton when a map from its physical states to the abstract states commutes with the two dynamics | [putnam1988]; [chalmers1996] |
| Mechanistic computation | philosophy of science | the processing of vehicles by a functional mechanism according to a rule sensitive to properties of the vehicles | [piccinini2015] |
| Canonical computation | neuroscience | a computation repeated across brain regions and modalities, realized by different mechanisms in different systems | [carandini2012] |

## Test case: computing

The term "computing" sets three requirements on the [definitions of process and event](process-event-history.md).

- **The state space can be abstract.** A computation is defined over the states of an automaton. The abstract states are related to the physical states by an *implementation map* $\psi$ that commutes with the dynamics: $\psi\circ\varphi_{\mathrm{phys}}=\varphi_{\mathrm{abs}}\circ\psi$, where $\varphi_{\mathrm{phys}}$ and $\varphi_{\mathrm{abs}}$ are the [evolution maps](dynamic.md) of the physical and the abstract dynamics. ^implementation-map
- **The implementation map must be constrained.** Without further constraints on $\psi$, every open system implements every finite automaton [putnam1988]. Counterfactual and causal constraints on $\psi$ block this result [chalmers1996], and so does a mechanistic account of computation [piccinini2015].
- **A process type can be individuated by its function.** At the computational level, a computation is identified by its input–output function. At the algorithmic level, it is identified by its sequence of abstract states [marr1982].

With these requirements, "computing" is a [process](process-event-history.md#^process) type at the algorithmic level: an equivalence class of physical histories under $\psi$. "Computing $f(3)$", the value of a function $f$ at the argument 3, is an [event](process-event-history.md#^event), since it culminates in the output. Computing is also an [activity](mechanistic-activity.md) in the mechanistic sense, since it has bearers and produces changes.

## Distinctions

- **Computing is a process, and the function computed is a static map.** The term "computation" names both objects. Computing unfolds along a course and falls in the process class. The function computed has no course: a record states it as a law with the role *input–output*.
- **A canonical computation is realized by several mechanisms.** Divisive normalization computes $y_i=\gamma\, u_i^n/(s^n+\sum_{i'} u_{i'}^n)$, where $u_i$ is the drive of unit $i$, $y_i$ its output, $s$ a semisaturation constant, and $\gamma$ and $n$ positive constants [carandini2012]. Different circuits compute this function in different systems [carandini2012]. Therefore, a claim about the function computed does not fix a mechanism, and a [mechanistic model](../regularities/mechanism-and-mechanistic-model.md) of one circuit does not, by itself, explain the same computation in another circuit.
- **The three levels of a computation are levels of description.** Each level describes the same system in its own vocabulary, so each level is a *level of description* in the [vocabulary of levels](../quantities/scale-and-level.md). None of the three is a level of organization, since no level of a computation is a part of another level.

## Relations to the method

- **The normalization map is a law, and the relaxation that realizes it is a process.** The concept under which each item falls is listed among the [representational items and their concepts](../representations/representation-and-encoding.md#^decision-table).
- **A computation stated at an abstract level requires its implementation map.** Each abstract variable is an [aggregate](../../objects/subject/target-system.md#^aggregate-variables) whose defining map is $\psi$, so the abstract variables are functions on the physical state space.

---
## Sources

Marks follow the [legend of reading marks](../../../../CONTRIBUTING.md#^reading-marks).

- [carandini2012] ◐ [Carandini & Heeger, "Normalization as a canonical neural computation", *Nature Reviews Neuroscience* 13(1), 51–62, 2012](https://doi.org/10.1038/nrn3136); the normalization equation in Box 1, and the claim that the computation, not the biophysical mechanism, is common across systems, checked through passages of the full text
- [chalmers1996] ◐ [Chalmers, "Does a rock implement every finite-state automaton?", *Synthese* 108(3), 309–333, 1996](https://doi.org/10.1007/BF00413692)
- [marr1982] ◐ [Marr, *Vision: A Computational Investigation into the Human Representation and Processing of Visual Information*, W. H. Freeman, 1982; reissued MIT Press, 2010](https://doi.org/10.7551/mitpress/9780262514620.001.0001)
- [piccinini2015] ◐ [Piccinini, *Physical Computation: A Mechanistic Account*, Oxford University Press, 2015](https://doi.org/10.1093/acprof:oso/9780199658855.001.0001)
- [putnam1988] ◐ [Putnam, *Representation and Reality*, MIT Press, 1988](https://mitpress.mit.edu/9780262660747/representation-and-reality/); appendix, pp. 121–125: "every ordinary open system is a realization of every abstract finite automaton"
