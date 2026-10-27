---
role: definition
status: wip
index: "[Definitions](docs/epistemology/definitions/_index.md)"
aliases:
  - Variable, value, observable, parameter and data
  - Variable
  - Value
  - Observable
  - Parameter
  - Data
tags: []
source:
---
# Variable, value, observable, parameter and data

> [!QUESTION] Goal: which formal object does a record declare when it declares a variable, an observable or a parameter, and what do its data record?

A **variable** is an [attribute](property-attribute-predicate.md) formalized as a function with a domain and a codomain. The other four terms specialize that function or its outputs:

- a value is one output;
- an observable is a variable tied to a measurement;
- a parameter is a variable held fixed;
- data are recorded values.

## Senses

| Term | Community | Definition | Source |
| --- | --- | --- | --- |
| Variable | realist ontology | a state function $F:\mathcal{D}\to\mathcal{V}$ that assigns to each thing, at each time, a value in a codomain $\mathcal{V}$ | [bunge1977] |
| Variable | probability | a random variable: a measurable function $F:\Omega\to\mathbb{R}$ on a probability space | [kolmogorov1933] |
| Variable | logic | a placeholder that ranges over a domain and is bound by a quantifier | [quine1948] |
| Value | all | an element $v\in\mathcal{V}$ of the codomain; the output $F(d)$ of the variable at one argument | — |
| Observable | empiricist philosophy of science | an entity detectable by the unaided senses, opposed to a theoretical entity | [vanfraassen1980] |
| Observable | classical and quantum physics | a measurable function on the phase space (classical); a self-adjoint operator on the state space (quantum) | — |
| Observable | control theory | the output $y=h(x)$ of an observation function; a system is *observable* when its state can be reconstructed from its outputs over time | [kalman1960] |
| Latent variable | statistics | a variable of a model, read directly by no observation function, whose values are inferred | — |
| Parameter | statistics | an index $\theta$ of a family of distributions $\{P_\theta\}$: fixed within one model of the family, varied across its models | [mccullagh2002] |
| Data | philosophy of science | records of values produced by one experimental procedure and carrying the idiosyncrasies of that procedure | [bogen1988] |

The three senses of *observable* answer different questions. The empiricist sense classifies entities by human perception. The physical sense names a quantity defined on the state. The control sense names a map from the state to the outputs, and adds a property of the whole system.

## Distinctions

- **A variable is a function, and a value is one of its outputs.** The pair is sometimes described as a type and its tokens. That description is inexact, because a value such as 37 °C is itself shared by many things and many times. The exact relation is that of a function to an element of its codomain.
- **An attribute becomes a variable once its domain and codomain are fixed.** The same attribute, temperature, gives two variables when it is assigned to each neuron or to the whole tissue, because the domains differ. The codomain, in turn, fixes the meaningful comparisons between values, as the [vocabulary of scales](scale-and-level.md) states.
- **An observable is a variable with an observation map; a latent variable has none.** The distinction is relative to the instruments assumed. A membrane potential is observable under patch clamp and latent in a recording of spikes alone.
- **A parameter, a state variable and an exogenous variable differ in role only.** The [role test](#^role-test) fixes the role of a declared quantity, relative to the course of one phenomenon.
- **Data are not the values of the observable.** Data carry the noise, the artefacts and the procedure of one experiment. Data are separated from the phenomenon detected through them in the [vocabulary of phenomena](pattern-and-phenomenon.md).

## Role test of a quantity

Three questions about one phenomenon decide the role of a declared quantity. The first asks whether its value varies along the [course](process-event-history.md#^course) of the phenomenon. The second asks, for a quantity constant along the course, whether its value varies across the instances compared by the phenomenon. The third asks, for a quantity that varies along the course, whether the system or its environment sets that value. ^role-test

| Along the course | Across the instances | Value set by | Role | Place in the records |
| --- | --- | --- | --- | --- |
| varies | — | the system | state variable | a variable of the target, with `determined: within`; for a parameter of the target, an entry of `course.varies` |
| varies | — | outside the system | exogenous variable | a variable of the target, with `determined: outside`; for a parameter of the target, an entry of `course.varies` |
| constant | varies | the question | index of an observable, when the claim is a function of the values; source of variation, when the claim is a distribution over draws | a parameter of the target, or the initial value of a variable, named by the phenomenon among its indices or its sources of variation |
| constant | constant | — | parameter | a parameter of the target, named by neither |

- **The target declares a quantity by the course of its laws of evolution.** The target record declares a quantity as a parameter when the quantity stays constant along the course of the background laws with the role *evolution*, and as a variable otherwise. A phenomenon whose course makes a declared parameter vary lists that parameter in `phenomenon.course.varies`. *Example*: the weights $W$ of a network are parameters of the target, since its law of evolution keeps them fixed while the network relaxes to a fixed point. Training changes $W$, so the phenomenon of training lists $W$ in `course.varies`, where $W$ takes the role of a variable. ^declaration-rule
- **The role test is relative to a phenomenon, whereas the declaration belongs to the target.** One quantity can take two roles in two phenomena of the same target. The target declares it once, and each phenomenon states the role of the quantity within that phenomenon.

## Consequences for a record

- **A declared variable is a state function.** Its signature fixes the domain $\mathcal{D}$, as a product of constituent kinds and index sets, and its value set fixes the codomain $\mathcal{V}$. This signature is stated by the [places of a quantity](../target-system.md#^places).
- **The explanandum variables of a phenomenon are observables in the physical sense.** Each explanandum variable is a function of the state variables of the target, as the [specification of the phenomenon](../phenomenon.md) requires.
- **The control sense of observable corresponds to a law with the role *measurement*.** Such a law states how an instrument registers the state, so it plays the part of the observation function $h$. The empiricist sense has no field in a record.
- **A parameter of the target is fixed along every course, except the courses that list it in `varies`.** The [target specification](../target-system.md) applies the [role test](#^role-test) with this reading. The criterion coincides with the statistical sense of parameter when one run of the system counts as one model of the family.

---
## Sources

Marks follow the [legend of reading marks](../../../CONTRIBUTING.md#^reading-marks).

- [bogen1988] ◐ [Bogen & Woodward, "Saving the phenomena", *Philosophical Review* 97(3), 303–352, 1988](https://doi.org/10.2307/2185445)
- [bunge1977] ◐ [Bunge, *Treatise on Basic Philosophy*, vol. 3, *Ontology I: The Furniture of the World*, Reidel, 1977](https://doi.org/10.1007/978-94-010-9924-0); the state function and the lawful state space are introduced in ch. 3, "Thing", section "State"
- [kalman1960] ◐ [Kalman, "On the general theory of control systems", *IFAC Proceedings Volumes* 1(1), 491–502, 1960](https://doi.org/10.1016/S1474-6670(17)70094-8); Proceedings of the First IFAC Congress, Moscow
- [kolmogorov1933] ◐ [Kolmogoroff, *Grundbegriffe der Wahrscheinlichkeitsrechnung*, Springer, 1933](https://doi.org/10.1007/978-3-642-49888-6)
- [mccullagh2002] ◐ [McCullagh, "What is a statistical model?", *Annals of Statistics* 30(5), 1225–1310, 2002](https://doi.org/10.1214/aos/1035844977)
- [quine1948] ◐ [Quine, "On what there is", *Review of Metaphysics* 2(5), 21–38, 1948](https://en.wikisource.org/wiki/On_What_There_Is)
- [vanfraassen1980] ◐ [van Fraassen, *The Scientific Image*, Clarendon Press, 1980](https://doi.org/10.1093/0198244274.001.0001)
