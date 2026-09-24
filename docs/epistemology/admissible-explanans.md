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

The level of the explanans is the fourth dimension of the [epistemic task](epistemic-task.md), and it is optional.

The level of the explanans $\lambda$ fixes which **variables an admissible explanans may contain**. 

*Example*: one gamma oscillation admits explanantia at three levels:

- ion-channel conductances;
- spike timing in an excitatory–inhibitory loop;
- a mean-field equation for population rates.

Two independent axes supply the options for the level $\lambda$, and a justification records why the answer is bound that way: ^level-axes

| Specification | When it is required | What it varies | Options | Examples | Source |
| ------------- | ------------------- | -------------- | ------- | -------- | ------ |
| Compositional level | when the question restricts the parts whose activities may explain | the constituent kinds or index sets whose parts may enter the explanans | the [constituents of the target system](target-system.md#^constituents) · their sub-parts · aggregates of them | channel · neuron · circuit · population | [craver2007] |
| Substrate dependence | when the question restricts the answer to one realization, or refuses that restriction | whether the explanans variables are specific to one realization of the system | substrate-specific (variables of the particular parts) · substrate-independent (variables shared by every realization: functional roles, universality classes) · link (how substrate-specific variables realize substrate-independent ones) | membrane potentials of identified neurons (specific); an error signal, whatever its carrier (independent); the universality class of a phase transition (independent); how a circuit implements context-dependent gating (link) | [batterman2000]; [marr1982]; [bechtel2015] |
| Justification | whenever an axis is stated | why the research program binds the answer to these variables, and what an answer outside them would fail to deliver | one clause, carrying no commitment the axes already hold | "the forecast names which subsystem transitions and when, so the explanans must be resolved to individual subsystems" | — |

- **The level is optional.** When it is left open, the *default* level matches the [grain of the phenomenon](phenomenon.md#^resolution-proportionality) by proportionality: changes in the explanans variables must correspond to changes in the explanandum, without irrelevant detail [woodward2010]. A stated level records what the research program *stipulates*, for instance that only circuit-level explanations count.

- **Compositional levels are local.** Compositional levels order the parts of one mechanism that are constitutively relevant to its behavior into a part–whole hierarchy internal to that mechanism, not into strata of nature [craver2007]. The options therefore derive from the constituents declared for the target system.
	
- **Substrate dependence applies to any system.** Multiple realizability in the special sciences is an instance of universality in physics: macroscopic behavior shared by microscopically different systems [batterman2000]. *Example*: A spin glass admits explanations through its specific couplings or through its universality class, as a neural circuit admits explanations through identified neurons or through the functional roles they play.
	
- **Marr's levels decompose onto this axis and the other dimensions of the task.** Marr's framework applies only to information-processing systems [marr1982], and its three levels map onto general dimensions (proposal):
	
    - the computational level (what is computed, and why) is a [requested relation](requested-relation.md) of function or optimization, since it explains the computation by what the environment demands [bechtel2015];
    - the algorithmic level uses substrate-independent variables: representations and procedures;
    - the implementational level uses substrate-specific variables at a compositional level.
	
    A question that links two of Marr's levels takes the option "link": the answer gives both descriptions and the mapping between the two descriptions. Learning, added as a further level for trained systems [poggio2012], needs no value on this axis: a question about learning takes the acquisition itself as its phenomenon, for instance "training produces this algorithm".

- **The level bounds the terms of the answer without choosing them.** The terms $V$ of the proposed model belong to the [answer layer](answer-form.md#^answer-elements), whereas the level $\lambda$ only delimits the set from which the terms $V$ are drawn.

- **The level is fixed by the epistemic task, not by the [subject of inquiry](subject-of-inquiry.md).** The level restricts the admissible answers without naming an object of the question. Beyond its topic and its contrast, a why-question constrains its answers only through the relevance relation [vanfraassen1980], so the level $\lambda$ qualifies the relation $R$.

---
## Sources

Marks: ✓ the text itself was read · ◐ checked through an abstract, the publisher page or a secondary summary · ○ cited from standard knowledge, not fetched.

- [batterman2000] ◐ [Batterman, "Multiple realizability and universality", *British Journal for the Philosophy of Science* 51(1), 2000](https://philpapers.org/rec/BATMRA)
- [bechtel2015] ◐ [Bechtel & Shagrir, "The non-redundant contributions of Marr's three levels of analysis for explaining information-processing mechanisms", *Topics in Cognitive Science* 7(2), 2015](https://onlinelibrary.wiley.com/doi/10.1111/tops.12141)
- [craver2007] ◐ [Craver, *Explaining the Brain*, OUP, 2007](https://philpapers.org/rec/CRAETB-2)
- [marr1982] ○ Marr, *Vision*, Freeman, 1982
- [poggio2012] ◐ [Poggio, "The levels of understanding framework, revised", *Perception* 41, 2012](https://journals.sagepub.com/doi/10.1068/p7299)
- [vanfraassen1980] ◐ van Fraassen, *The Scientific Image*, ch. 5; [the chapter text](https://www.fitelson.org/290/vanfraassen_pte.pdf)
- [woodward2010] ◐ [Woodward, "Causation in biology…", *Biology & Philosophy* 25, 2010](https://link.springer.com/article/10.1007/s10539-010-9200-z)
