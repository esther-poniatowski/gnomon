---
tags:
  - decision
status: accepted
created: 2026-10-29
revised: 2026-10-29
index: "[Architecture decisions](docs/adr/_index.md)"
aliases:
  - Answers, models and bindings
---
# Answers, models and bindings

> [!QUESTION] Goal: which records hold a candidate answer, the model on which it rests, and the relation of that model to the phenomenon, so that each answer has the form that its question requires and its values can be compared with the target?

The [audits of the model design](../audits/_index.md) and the trials run on the test records exposed three defects. Every answer must state an explanans, even when its aim is not explanation. The values that an answer derives are bound to no output of the phenomenon, so the tests of fidelity and of required accuracy cannot be computed. A stylized model enters the quantities of its target by `reference`, which asserts an identity that a model never has with its target. An analysis of the answer forms per aim and of the binding to the target, followed by an adversarial review of its foundations, settled the design below. Both analyses reasoned from the literature, without reading the records of `gnomon`. A review of the method notes that implement the decision refined it in place on six points: the declared use, the erotetic relation, idealizations, the estimates of a phenomenon, the discrepancy, and the calibration treatments. The method notes now own the details of these points and the fields of every record, so the decision below states only the structure.

## Decision

**Questions.** The full atomic question, its aim together with its parameters, fixes the type of its direct answers. A research question is a graph of atomic questions, linked by the [links between questions](../epistemology/inquiry/question.md#^linked-questions). A question may stay *open*, with no answer type yet, while its answer space is not formed.

**Aims.** The aims form an open [registry](../epistemology/epistemic-task/epistemic-aim.md#^aim-registry), in which each entry states its [answer conditions](../epistemology/epistemic-task/epistemic-aim.md#^answer-conditions). Only the aims of answer content and of conceptual work generate an aim block. A change of accepted claims is not an aim, since it is the effect of accepting an answer. Understanding is not an aim either, since it is a dimension of assessment or a declared use of an answer.

**Answers.** An answer is one typed claim with its grounds, so a model that serves two aims grounds two answers. Each answer holds a core, whose elements every aim requires, and one aim block, which holds the elements that the aim of its question requires. Answers are linked to one another by typed relations. The elements of the core, the erotetic relation, the aim blocks, the target status of an explanatory factor, the declared use and the relations between answers are specified in the [answer form](../epistemology/answer/answer-form.md#^core-and-block).

**Models.** A model is a record of its own, which several answers can ground. A family of models can ground one answer, each model with its own binding, and the family is then assessed as a whole. The fields are specified in the [model record](../epistemology/answer/model-and-binding.md#^model-record).

**Bindings.** A binding is a record of its own, which relates a model in use to a phenomenon or to its data, and which records the surrogative inferences that its asserter licenses from the model to the target. A claim of actual strength about an empirical target, and any prediction or description of a target, requires a binding. An answer whose claim bears only on a model or on a formal class declares its use instead. The fields are specified in the [binding record](../epistemology/answer/model-and-binding.md#^binding-record).

**Keys.** Observation operators, maps of units and of aggregation, and qualitative abstractions are shared, versioned records, which several bindings reference. The fields are specified in the [key record](../epistemology/answer/model-and-binding.md#^key-record).

**Phenomena.** A phenomenon owns the [estimator of its explanandum variables](../epistemology/subject/phenomenon.md#^phenomenon-owns-estimation), and it [declares the facts on which its data depend](../epistemology/subject/phenomenon.md#^data-model-declarations).

**Comparisons.** A comparison is computed, not recorded, from a binding, a version of the data, and the metric and the tolerance of the question. A revised binding is a new version and leaves earlier comparisons unchanged. The facts that a comparison reports are specified with the [computed comparison](../epistemology/answer/model-and-binding.md#^comparison-reports), and the tests that read them in the [conditions of satisfaction](../epistemology/answer/satisfaction-conditions.md#^fidelity-reads-reports).

## Constraints that decide the design

- **The type of a question fixes the type of its answers.** A question is determined by its admissible answers [hamblin1958] [belnap1976], and a why-question by its topic, its contrast class and its relevance relation [vanfraassen1980]. Requiring the same components of every answer treats every question as a why-question.
- **Grounds are general, and their explanatory reading is not.** Every claim depends on grounds, and sensitivity, robustness and explanatory proofs show that dependence is not specific to explanation [saltelli2008] [weisberg2006] [steiner1978] [lange2017]. Only explanation reads some dependences as difference-making of a requested kind, relative to a contrast [woodward2003] [strevens2008]. A predictor need not explain [shmueli2010].
- **One model grounds several answers.** Once each answer holds one typed claim, a binding owned by the answer would be repeated across every claim that shares the model. Several bindings use the same observation operators and maps of units, and a measurement outcome is itself inferred through a model, which can be revised [tal2013] [parker2017].
- **Explanatory factors need not exist in the target.** Minimal models, holistic distortions and explanations by constraint explain without a correspondence of factors [battermanrice2014] [rice2021] [lange2017].
- **Representation need not be a mapping of quantities.** The binding records the inferences that it licenses, which keeps it neutral between theories of representation [suarez2004] [friggnguyen2020]. Similarity holds in respects and degrees fixed by a purpose [giere2004] [weisberg2013], and adequacy is relative to a purpose [parker2020].
- **Phenomena depend on models.** Data models can contain the models under test, and they are adequate for a purpose [bokulichparker2021]. A comparison that ignores the overlap can be circular.
- **Discrepancy has three owners**, which the [binding note](../epistemology/answer/model-and-binding.md#^discrepancy-owners) assigns [kennedyohagan2001] [brynjarsdottir2014]. Using calibration data for confirmation is legitimate or not depending on the method [steelewerndl2013], so the comparison must report its treatment.

## Options weighed

| Option | Benefit | Reason it is not taken |
| ------ | ------- | ---------------------- |
| A uniform form, with every block optional and rules conditioned on the aim | One schema, simple queries across aims | The form represents the same content as typed answers, so the choice rests on the unit of an answer; with blocks optional, an answer can still carry a pseudo-explanans |
| Typed result blocks without a shared core | Each aim has exactly its fields | The grounds, the domain and the status cannot be compared across aims, and their fields repeat in every block |
| Typed answers with a binding owned by the answer | The author of the answer commits to its interpretation | One model grounds several answers, so every binding would be repeated, and shared keys would be copied |
| A network of untyped claims, linked by support and attack | No premature commitment in exploratory phases | No answer has a condition of conclusiveness; an open question, with its answer type still to come, covers the exploratory phase |
| Typed answers on a shared core, with separate model, binding and key records | Each answer shows what its aim requires, and models, keys and phenomena are reused without repetition | — |

## Consequences

- The explanans is no longer required of every answer. Its premises become the grounds of the core, and its relevance becomes the block of an explanation.
- The answer template is restructured into a core and aim blocks, and three record kinds are added: the model, the binding and the key. The phenomenon and the assessment gain the declarations that their method notes specify, and the comparison is computed.
- The decision of 2026-09-24 (commit 08cc32d), which declared the model of an answer with the blocks of the target, is superseded: the model has a record of its own.
- The use of `reference` for a stylized constituent ends: a model relates to its target through a binding.
- The method notes that describe the answer, the phenomenon and the assessment remain to be revised, and the registry of aims gains its answer conditions.
- A pilot on contrasting test cases precedes any migration of the records, as both audits require, and the [project goals](../../TODO.md) track it.

---
## Sources

Marks follow the [legend of reading marks](../../CONTRIBUTING.md#^reading-marks). The sources were checked by the two analyses, through searches of their bibliographic records; a mark ◐ records such a check, and a mark ○ a source cited from memory.

- [battermanrice2014] ◐ Batterman & Rice, "Minimal model explanations", *Philosophy of Science* 81(3), 349–376, 2014
- [belnap1976] ○ Belnap & Steel, *The Logic of Questions and Answers*, Yale University Press, 1976
- [bokulichparker2021] ◐ Bokulich & Parker, "Data models, representation and adequacy-for-purpose", *European Journal for Philosophy of Science* 11, 31, 2021
- [brynjarsdottir2014] ◐ Brynjarsdóttir & O'Hagan, "Learning about physical parameters: the importance of model discrepancy", *Inverse Problems* 30, 114007, 2014
- [friggnguyen2020] ◐ Frigg & Nguyen, *Modelling Nature: An Opinionated Introduction to Scientific Representation*, Springer, 2020; denotation, exemplification, key and imputation
- [giere2004] ◐ Giere, "How models are used to represent reality", *Philosophy of Science* 71(5), 742–752, 2004
- [hamblin1958] ○ Hamblin, "Questions", *Australasian Journal of Philosophy* 36, 1958
- [kennedyohagan2001] ◐ Kennedy & O'Hagan, "Bayesian calibration of computer models", *Journal of the Royal Statistical Society B* 63(3), 425–464, 2001
- [lange2017] ◐ Lange, *Because Without Cause: Non-Causal Explanations in Science and Mathematics*, Oxford University Press, 2017
- [parker2017] ◐ Parker, "Computer simulation, measurement, and data assimilation", *British Journal for the Philosophy of Science* 68(1), 273–304, 2017
- [parker2020] ◐ Parker, "Model evaluation: an adequacy-for-purpose view", *Philosophy of Science* 87(3), 457–477, 2020
- [rice2021] ◐ Rice, *Leveraging Distortions: Explanation, Idealization, and Universality in Science*, MIT Press, 2021
- [saltelli2008] ○ Saltelli et al., *Global Sensitivity Analysis: The Primer*, Wiley, 2008
- [shmueli2010] ○ Shmueli, "To explain or to predict?", *Statistical Science* 25(3), 2010
- [steelewerndl2013] ◐ Steele & Werndl, "Climate models, calibration, and confirmation", *British Journal for the Philosophy of Science* 64(3), 609–635, 2013
- [steiner1978] ◐ Steiner, "Mathematical explanation", *Philosophical Studies* 34, 1978
- [strevens2008] ○ Strevens, *Depth: An Account of Scientific Explanation*, Harvard University Press, 2008
- [suarez2004] ◐ Suárez, "An inferential conception of scientific representation", *Philosophy of Science* 71(5), 767–779, 2004
- [tal2013] ◐ Tal, "Old and new problems in philosophy of measurement", *Philosophy Compass* 8(12), 1159–1173, 2013
- [vanfraassen1980] ✓ van Fraassen, *The Scientific Image*, Clarendon Press, 1980, ch. 5; [the chapter text](https://www.fitelson.org/290/vanfraassen_pte.pdf)
- [weisberg2006] ◐ Weisberg, "Robustness analysis", *Philosophy of Science* 73(5), 730–742, 2006
- [weisberg2013] ◐ Weisberg, *Simulation and Similarity: Using Models to Understand the World*, Oxford University Press, 2013
- [woodward2003] ○ Woodward, *Making Things Happen: A Theory of Causal Explanation*, Oxford University Press, 2003
