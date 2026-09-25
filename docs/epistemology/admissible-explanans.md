---
role: definition
status: stable
index: "[Epistemology](docs/epistemology/_index.md)"
aliases:
  - Specifying the admissible explanans
  - Admissible explanans
tags: []
source:
---
# Specifying the admissible explanans

> [!QUESTION] Goal: what must be fixed to specify which variables an answer may use?

The level $\lambda$ fixes which **variables an admissible explanans may contain**. The level forms the fourth dimension of the [task that sets the kind of knowledge sought](epistemic-task.md).

*Example.* One gamma oscillation admits explanantia at three levels:

- ion-channel conductances;
- spike timing in an excitatory–inhibitory loop;
- a mean-field equation for population rates.

Two independent axes supply the options for the level $\lambda$. In addition, a justification records why the answer is bound to the options chosen: ^level-axes

| Specification | When it is required | Varied feature | Options | Examples | Source |
| ------------- | ------------------- | -------------- | ------- | -------- | ------ |
| Compositional level | when the question restricts the parts whose activities may explain the phenomenon | the constituent kinds or index sets whose parts may enter the explanans | the [constituents of the target system](target-system.md#^constituents) · their sub-parts · aggregates of them | channel · neuron · circuit · population | [craver2007] |
| Substrate dependence | when the question binds the answer to one realization of the system, or explicitly declines to do so | whether the explanans variables are specific to one realization of the system | substrate-specific (variables of the particular parts) · substrate-independent (variables shared by every realization: functional roles, universality classes) · link (how substrate-specific variables realize substrate-independent ones) | membrane potentials of identified neurons (specific) · an error signal on any carrier, or the universality class of a phase transition (independent) · how a circuit implements context-dependent gating (link) | [batterman2000]; [marr1982]; [bechtel2015] |
| Justification | whenever an axis is stated | why the research program binds the answer to these variables, and which content is lost when the explanans uses other variables | one clause that carries no commitment already held by the axes | "the forecast names when each subsystem transitions, so the explanans must resolve each of them individually" | — |

- **The level is optional.** An unstated level *defaults* to the [grain of the phenomenon](phenomenon.md#^resolution-proportionality) by proportionality. Proportionality requires the explanans variables to covary with the explanandum, and to carry no irrelevant detail [woodward2010]. A stated level, by contrast, records a *stipulation* of the research program, for instance that only explanations in terms of circuits count.

- **Compositional levels are local.** Compositional levels are internal to one mechanism: they order into a part–whole hierarchy the parts that are constitutively relevant to its behavior [craver2007]. The options therefore derive from the constituents declared for the target system.
	
- **Substrate dependence applies to any system.** The axis reaches beyond one science because multiple realizability in the special sciences is an instance of universality in physics: macroscopic behavior shared by microscopically different systems [batterman2000]. *Example.* A spin glass is explained either through its specific couplings or through its universality class. A neural circuit likewise admits two explanations: through identified neurons, or through their functional roles.
	
- **The three levels of analysis decompose onto the two axes and the other dimensions of the task.** The framework of three levels applies only to information-processing systems [marr1982]. Each of its levels maps onto dimensions that apply to any system (proposal):
	
    - The computational level states the computation and its rationale. This level corresponds to a [relation of function or optimization requested of the explanans](requested-relation.md), because it accounts for the computation through the demands that the environment places on the system [bechtel2015].
    - The algorithmic level uses substrate-independent variables: representations and procedures.
    - The implementational level uses substrate-specific variables at a compositional level.
	
    A question that links two levels of analysis takes the option `mapping`: the answer gives both descriptions and maps one onto the other. A further level, learning, has been added for trained systems [poggio2012]. A question about learning needs no value on the substrate axis, because its phenomenon is the acquisition itself (for instance, "training produces this algorithm").

- **The level bounds the terms of the answer without selecting any.** The terms $V$ of the proposed model belong to the [elements of a candidate answer](answer-form.md#^answer-elements). The level $\lambda$ only delimits the set from which these terms are drawn.

- **The level is fixed by the epistemic task, not by the [subject of inquiry](subject-of-inquiry.md).** The level restricts the admissible answers without naming an object of the question. Beyond its topic and its contrast, a why-question constrains its answers only through the relevance relation [vanfraassen1980]. The level $\lambda$ therefore qualifies the relation $R$.

---
## Sources

Marks follow [the legend that states how each entry was checked](../../CONTRIBUTING.md#^reading-marks).

- [batterman2000] ◐ [Batterman, "Multiple realizability and universality", *British Journal for the Philosophy of Science* 51(1), 2000](https://philpapers.org/rec/BATMRA)
- [bechtel2015] ◐ [Bechtel & Shagrir, "The non-redundant contributions of Marr's three levels of analysis for explaining information-processing mechanisms", *Topics in Cognitive Science* 7(2), 2015](https://onlinelibrary.wiley.com/doi/10.1111/tops.12141)
- [craver2007] ◐ [Craver, *Explaining the Brain*, OUP, 2007](https://philpapers.org/rec/CRAETB-2)
- [marr1982] ○ Marr, *Vision*, Freeman, 1982
- [poggio2012] ◐ [Poggio, "The levels of understanding framework, revised", *Perception* 41, 2012](https://journals.sagepub.com/doi/10.1068/p7299)
- [vanfraassen1980] ✓ van Fraassen, *The Scientific Image*, ch. 5, read in [the chapter text](https://www.fitelson.org/290/vanfraassen_pte.pdf)
- [woodward2010] ◐ [Woodward, "Causation in biology…", *Biology & Philosophy* 25, 2010](https://link.springer.com/article/10.1007/s10539-010-9200-z)
