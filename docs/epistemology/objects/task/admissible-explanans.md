---
tags:
  - theory
index: "[Epistemic task](docs/epistemology/objects/task/_index.md)"
aliases:
  - Admissible explanans
---
# Admissible explanans

> [!QUESTION] Goal: which variables may an explanans contain, and along which axes is that bound set?

The bound on the explanans $\lambda$ fixes which **variables an admissible explanans may contain**: it is the set of variables from which an explanans may be drawn. The bound forms the fourth dimension of the [epistemic task](epistemic-task.md), the layer that sets the kind of knowledge sought.

*Example.* One gamma oscillation admits explanantia at three levels:

- ion-channel conductances;
- spike timing in an excitatory–inhibitory loop;
- a mean-field equation for population rates.

The options of the bound $\lambda$ along its two axes, compositional level and substrate dependence, are listed in the [epistemic task of a question](../../../specification/question-task.md#^level-axes).

- **The bound is optional.** An unstated bound *defaults* to the [grain of the phenomenon](../subject/phenomenon.md#^resolution-proportionality) by proportionality. Proportionality requires the explanans variables to covary with the explanandum, and to carry no irrelevant detail [woodward2010]. A stated bound, by contrast, records a *stipulation* of the research program, for instance that only explanations in terms of circuits count.

- **Compositional levels are local.** Compositional levels are internal to one mechanism: they order into a part–whole hierarchy the parts that are constitutively relevant to its behavior [craver2007]. The options therefore derive from the constituents declared for the target system.
	
- **Substrate dependence applies to any system.** The axis reaches beyond one science because multiple realizability in the special sciences is an instance of universality in physics: macroscopic behavior shared by microscopically different systems [batterman2000]. *Example.* A spin glass is explained either through its specific couplings or through its universality class. A neural circuit likewise admits two explanations: through identified neurons, or through their functional roles.
	
- **The three levels of analysis decompose onto the two axes and the other dimensions of the task.** The framework of three levels applies only to information-processing systems [marr1982]. Each of its levels maps onto dimensions that apply to any system (proposal):
	
    - The computational level states the computation and its rationale. This level corresponds to a relation of [function or optimization](requested-relation.md) requested of the explanans, because it accounts for the computation through the demands that the environment places on the system [bechtel2015].
    - The algorithmic level uses substrate-independent variables: representations and procedures.
    - The implementational level uses substrate-specific variables at a compositional level.
	
    A question that links two levels of analysis takes the option `mapping`: the answer gives both descriptions and maps one onto the other. A further level, learning, has been added for trained systems [poggio2012]. A question about learning needs no value on the substrate axis, because its phenomenon is the acquisition itself (for instance, "training produces this algorithm").

- **The bound delimits the terms of the answer without selecting any.** The terms $V$ of the proposed model belong to the [elements of the model on which a candidate answer rests](../../../specification/model.md#^model-elements). The bound $\lambda$ only delimits the set from which these terms are drawn.

- **The bound is fixed by the epistemic task, not by the [subject of inquiry](../subject/subject-of-inquiry.md).** The bound restricts the admissible answers without naming an object of the question. Beyond its topic and its contrast, a why-question constrains its answers only through the kind of information that it requests [vanfraassen1980], which the [requested relation](requested-relation.md) $R$ fixes. The bound $\lambda$ therefore qualifies the relation $R$.

---
## Sources

Marks follow the [legend of reading marks](../../../../CONTRIBUTING.md#^reading-marks).

- [batterman2000] ◐ [Batterman, "Multiple realizability and universality", *British Journal for the Philosophy of Science* 51(1), 2000](https://philpapers.org/rec/BATMRA)
- [bechtel2015] ◐ [Bechtel & Shagrir, "The non-redundant contributions of Marr's three levels of analysis for explaining information-processing mechanisms", *Topics in Cognitive Science* 7(2), 2015](https://onlinelibrary.wiley.com/doi/10.1111/tops.12141)
- [craver2007] ◐ [Craver, *Explaining the Brain: Mechanisms and the Mosaic Unity of Neuroscience*, Oxford University Press, 2007](https://doi.org/10.1093/acprof:oso/9780199299317.001.0001)
- [marr1982] ◐ [Marr, *Vision: A Computational Investigation into the Human Representation and Processing of Visual Information*, W. H. Freeman, 1982; reissued MIT Press, 2010](https://doi.org/10.7551/mitpress/9780262514620.001.0001)
- [poggio2012] ◐ [Poggio, "The levels of understanding framework, revised", *Perception* 41, 2012](https://journals.sagepub.com/doi/10.1068/p7299)
- [vanfraassen1980] ◐ [van Fraassen, *The Scientific Image*, Clarendon Press, 1980](https://doi.org/10.1093/0198244274.001.0001); ch. 5, read in its abridged reprint, "The pragmatic theory of explanation", in Pitt (ed.), *Theories of Explanation*, Oxford University Press, 1988, 136–155 ([PDF](https://www.fitelson.org/290/vanfraassen_pte.pdf))
- [woodward2010] ◐ [Woodward, "Causation in biology: stability, specificity, and the choice of levels of explanation", *Biology & Philosophy* 25(3), 287–318, 2010](https://doi.org/10.1007/s10539-010-9200-z)
