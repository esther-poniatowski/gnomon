---
tags:
  - decision
status: accepted
created: 2026-10-29
revised: 2026-11-03
index: "[Architecture decisions](docs/adr/_index.md)"
aliases:
  - Answers, models and bindings
---
# Answers, models and bindings

> [!QUESTION] Goal: which records hold a candidate answer, the model on which it rests, and the relation of that model to the phenomenon, so that each answer has the form that its question requires and its values can be compared with the target?

The [audits of the model design](https://github.com/esther-poniatowski/gnomon/blob/a651f8789d763fb082c0a64a91a597a42cc0cb80/docs/audits/_index.md) and the trials run on the test records exposed three defects. Every answer must state an explanans, even when its aim is not explanation. The values that an answer derives are bound to no output of the phenomenon, so the tests of fidelity and of required accuracy cannot be computed. A stylized model enters the quantities of its target by `reference`, which asserts an identity that a model never has with its target. An analysis of the answer forms per aim and of the binding to the target, followed by an adversarial review of its foundations, settled the design below. Both analyses reasoned from the literature, without reading the records of `gnomon`. A review of the notes that implement the decision refined it in place on seven points: the declared use, the erotetic relation, idealizations, the estimates of a phenomenon, the discrepancy, the calibration treatments, and the account of representation. The notes of the epistemology and of the specification now own the details of these points and the fields of every record, so the decision below states only the structure. A pilot on four contrasting inquiries, recorded in the [audit of the pilot](https://github.com/esther-poniatowski/gnomon/blob/a651f8789d763fb082c0a64a91a597a42cc0cb80/docs/audits/model-design-pilot.md), then amended the decision on five points: derived models, the binding of a question with outputs to match, the warrant, the constants of a bound, and the checks of answers, models and bindings.

## Decision

**Questions.** The full atomic question, its aim together with its parameters, fixes the type of its direct answers. A research question is usually composed of atomic questions, linked by the [links between questions](../epistemology/objects/question/question.md#^linked-questions), and each candidate answer answers one atomic question. A question may stay *open*, with no answer type yet, while its answer space is not formed.

**Aims.** The aims form an open [registry](../epistemology/objects/task/epistemic-aim.md#^aim-registry), in which each entry states its [answer conditions](../epistemology/objects/task/epistemic-aim.md#^answer-conditions). Only the aims of answer content and of conceptual work generate an aim block. A change of accepted claims is not an aim, since it is the effect of accepting an answer. Understanding is not an aim either, since it is a dimension of assessment or a declared use of an answer.

**Answers.** An answer is one typed claim with its grounds, so a model that serves two aims grounds two answers. Each answer holds a core, whose elements every aim requires, and one aim block, which holds the elements that the aim of its question requires. Answers are linked to one another by typed relations. The elements of the core, the erotetic relation, the aim blocks, the target status of an explanatory factor, the declared use and the relations between answers are specified in the [answer form](../epistemology/objects/answer/answer-form.md#^core-and-block).

**Models.** A model is a record of its own, which several answers can ground. A family of models can ground one answer, each model with its own binding, and the family is then assessed as a whole. The fields are specified in the [model record](../specification/model.md#^model-record).

**Derived models.** A model may derive from parent models by typed operations, and it declares only the symbols that its operations yield, such as a collective variable. Each operation is typed relative to its parent. Only an answer classifies an operation or an assumption of the model relative to its target, through a ground. The kinds of operation and their classes of error are defined with the [derived models](../epistemology/objects/answer/model-and-binding.md#^derived-models). A model without a parent states its constituents, its variables and its laws, whereas a derived model states its operations, as the [model record](../specification/model.md#^model-parents) requires.

**Bindings.** A binding is a record of its own, which relates a model in use to a phenomenon or to its data, and which records the surrogative inferences that its asserter licenses from the model to the target. A claim of actual strength about an empirical target, and any prediction or description of a target, requires a binding. An answer on a model other than its target also requires a binding when its question names outputs to match, even if the target is a formal class. An answer whose claim bears only on a model or on a formal class, under a question that names no output, declares its use instead. An argued pair of a binding may stand as a [ground of role `warrant`](../epistemology/objects/knowledge/grounds-and-dependence.md#^ground-roles), beside a law of a model or of a background. The fields are specified in the [binding record](../specification/binding.md#^binding-record).

**Keys.** Observation operators, maps of units and of aggregation, and qualitative abstractions are shared, versioned records, which several bindings reference. The fields are specified in the [key record](../specification/key.md#^key-record).

**Phenomena.** A phenomenon owns the [estimator of its observables](../epistemology/objects/subject/phenomenon.md#^phenomenon-owns-estimation), and it [declares the facts on which its data depend](../epistemology/objects/subject/phenomenon.md#^data-model-declarations). A constant of a bound is a [feature of the manifestation](../specification/phenomenon.md#^bound-constants) that states the bound.

**Comparisons.** A comparison is computed, not recorded, from a binding, a version of the data, and the metric and the tolerance of the question. A revised binding is a new version and leaves earlier comparisons unchanged. The facts that a comparison reports are specified with the [computed comparison](../epistemology/objects/answer/model-and-binding.md#^comparison-reports), and the tests that read them in the [conditions of satisfaction](../epistemology/objects/answer/satisfaction-conditions.md#^fidelity-reads-reports).

**Checks.** The vocabulary check reads answers, models and bindings. Each record resolves its bare symbols against the [tables visible](flat-symbol-table.md#^visible-tables) from it, and reaches a unit without a symbol, such as an operation or a pair, by its identifier.

## Constraints that decide the design

- **The type of a question fixes the type of its answers.** A question is determined by its direct answers [hamblin1958] [belnap1976], and a why-question by its topic, its contrast class and its relevance relation [vanfraassen1980]. Determination by the admissible answers is discarded: the admissible answers depend on the tests and on the constitutive virtues, which fix standards and not the question, so two questions with the same direct answers would differ by their tests alone, as the [answers of a question](../epistemology/objects/question/question.md#^answer-sets) state. Requiring the same components of every answer treats every question as a why-question.
- **Grounds are general, and their explanatory reading is not.** Every claim depends on grounds, and sensitivity, robustness and explanatory proofs show that dependence is not specific to explanation [saltelli2008] [weisberg2006] [steiner1978] [lange2017]. Only explanation reads some dependences as difference-making of a requested kind, relative to a contrast [woodward2003] [strevens2008]. A predictor need not explain [shmueli2010].
- **One model grounds several answers.** Once each answer holds one typed claim, a binding owned by the answer would be repeated across every claim that shares the model. Several bindings use the same observation operators and maps of units, and a measurement outcome is itself inferred through a model, which can be revised [tal2013] [parker2017].
- **Explanatory factors need not exist in the target.** Minimal models, holistic distortions and explanations by constraint explain without a correspondence of factors [battermanrice2014] [rice2021] [lange2017].
- **Representation need not be a mapping of quantities.** The binding records the inferences that its asserter licenses [suarez2004], stated in the vocabulary of denotation, exemplification, key and imputation as a choice of the method [friggnguyen2020]. Its computed pairs assert similarities in stated respects and to the degrees that its structural discrepancy states [giere2004] [weisberg2013], its argued pairs assert the claims that their arguments license, and adequacy is relative to a purpose [parker2020]. The binding stays neutral on the constitution of representation, since every account evaluates an imputation by whether the target has the imputed feature. The earlier wording, neutral between theories of representation, is dropped: the vocabulary of the DEKI account is itself drawn from one theory, so the neutrality holds only for the constitution of representation. Three alternatives are discarded, as the table after this list states.
- **Phenomena depend on models.** Data models can contain the models under test, and they are adequate for a purpose [bokulichparker2021]. A comparison that ignores the overlap can be circular.
- **Discrepancy has three owners**, which the [binding note](../epistemology/objects/answer/model-and-binding.md#^discrepancy-owners) assigns [kennedyohagan2001] [brynjarsdottir2014]. Using calibration data also for confirmation is legitimate under a Bayesian or likelihood account of incremental confirmation, provided that the prior over the calibration parameters was fixed before those data [steelewerndl2013]. Other accounts state other conditions, so the comparison must report its treatment.

The constraint on representation discards three alternatives:

| Alternative | Reason it is not taken |
| --- | --- |
| Similarity as the constitution of every binding | The alternative commits the records to one account of representation, and an argued pair, such as a localization, asserts no degree of similarity |
| The DEKI account adopted as the account of representation | The alternative asserts that the four conditions of that account suffice for representation, a contested claim on which no test of the method depends |
| A bare record of licensed inferences, without the vocabulary of the DEKI account | The record would not separate the feature of the model, the feature imputed to the target and the key, from which the comparison is computed |

## Options weighed

| Option | Benefit | Reason it is not taken |
| ------ | ------- | ---------------------- |
| A uniform form, with every block optional and rules conditioned on the aim | One schema, simple queries across aims | The form represents the same content as typed answers, so the choice rests on the unit of an answer; with blocks optional, an answer can still carry a pseudo-explanans |
| Typed result blocks without a shared core | Each aim has exactly its fields | The grounds, the domain and the status cannot be compared across aims, and their fields repeat in every block |
| Typed answers with a binding owned by the answer | The author of the answer commits to its interpretation | One model grounds several answers, so every binding would be repeated, and shared keys would be copied |
| A network of untyped claims, linked by support and attack | No premature commitment in exploratory phases | No answer has a condition of conclusiveness; an open question, with its answer type still to come, covers the phase before its answer space is formed, and the aim `exploration` covers the search of a declared space |
| Typed answers on a shared core, with separate model, binding and key records | Each answer shows what its aim requires, and models, keys and phenomena are reused without repetition | — |

The pilot discards five alternatives to its amendments:

| Alternative | Reason it is not taken |
| --- | --- |
| Operations typed relative to the target | One model grounds answers on several targets, so the model would carry classifications that each answer owns |
| Constituents, variables and laws required of every model | A derived model would declare again the symbols of its parents, which stay visible to it |
| A binding only for an empirical target | The fidelity test compares the values of a model with the outputs that its question names, and only a binding states the pairs that the comparison reads |
| A new ground role for the placement of a target in the regime of a limit | The role `warrant` already licenses the step from the other grounds to the claim, so a second role would split one function |
| A constant of a bound as a derived phenomenon | The bound, its constant and its horizon would sit in two records, although one manifestation asserts them together |

## Consequences

- The explanans is no longer required of every answer. Its premises become the grounds of the core, and its relevance becomes the block of an explanation.
- The answer template is restructured into a core and aim blocks, and three record kinds are added: the model, the binding and the key. The phenomenon and the assessment gain the declarations that their specification notes document, and the comparison is computed.
- The decision of 2026-09-24 (commit 08cc32d), which declared the model of an answer with the blocks of the target, is superseded: the model has a record of its own.
- The use of `reference` for a stylized constituent ends: a model relates to its target through a binding.
- The notes that describe the answer, the phenomenon and the assessment remain to be revised, and the registry of aims gains its answer conditions.
- The pilot on four contrasting inquiries ratified the design with the amendments above. The worked inquiries outside the pilot migrate under the goal `model-design` of the [project goals](../../TODO.md).

---
## Sources

Marks follow the [legend of reading marks](../../CONTRIBUTING.md#^reading-marks). The sources were checked by the two analyses, through searches of their bibliographic records; a mark ◐ records such a check, and a mark ○ a source cited from memory.

- [battermanrice2014] ◐ Batterman & Rice, "Minimal model explanations", *Philosophy of Science* 81(3), 349–376, 2014
- [belnap1976] ◐ [Belnap & Steel, *The Logic of Questions and Answers*, Yale University Press, 1976](https://catalogue.bnf.fr/ark:/12148/cb353871722)
- [bokulichparker2021] ◐ Bokulich & Parker, "Data models, representation and adequacy-for-purpose", *European Journal for Philosophy of Science* 11, 31, 2021
- [brynjarsdottir2014] ◐ Brynjarsdóttir & O'Hagan, "Learning about physical parameters: the importance of model discrepancy", *Inverse Problems* 30, 114007, 2014
- [friggnguyen2020] ◐ [Frigg & Nguyen, *Modelling Nature: An Opinionated Introduction to Scientific Representation*, Synthese Library 427, Springer, 2020](https://doi.org/10.1007/978-3-030-45153-0); denotation, exemplification, key and imputation
- [giere2004] ◐ Giere, "How models are used to represent reality", *Philosophy of Science* 71(5), 742–752, 2004
- [hamblin1958] ◐ [Hamblin, "Questions", *Australasian Journal of Philosophy* 36(3), 159–168, 1958](https://doi.org/10.1080/00048405885200211)
- [kennedyohagan2001] ◐ [Kennedy & O'Hagan, "Bayesian calibration of computer models", *Journal of the Royal Statistical Society, Series B* 63(3), 425–464, 2001](https://doi.org/10.1111/1467-9868.00294)
- [lange2017] ◐ Lange, *Because Without Cause: Non-Causal Explanations in Science and Mathematics*, Oxford University Press, 2017
- [parker2017] ◐ Parker, "Computer simulation, measurement, and data assimilation", *British Journal for the Philosophy of Science* 68(1), 273–304, 2017
- [parker2020] ◐ [Parker, "Model evaluation: an adequacy-for-purpose view", *Philosophy of Science* 87(3), 457–477, 2020](https://doi.org/10.1086/708691)
- [rice2021] ◐ Rice, *Leveraging Distortions: Explanation, Idealization, and Universality in Science*, MIT Press, 2021
- [saltelli2008] ◐ [Saltelli, Ratto, Andres, Campolongo, Cariboni, Gatelli, Saisana & Tarantola, *Global Sensitivity Analysis: The Primer*, Wiley, 2008](https://doi.org/10.1002/9780470725184)
- [shmueli2010] ◐ [Shmueli, "To explain or to predict?", *Statistical Science* 25(3), 289–310, 2010](https://doi.org/10.1214/10-STS330)
- [steelewerndl2013] ✓ [Steele & Werndl, "Climate models, calibration, and confirmation", *British Journal for the Philosophy of Science* 64(3), 609–635, 2013](https://doi.org/10.1093/bjps/axs036); read in full in the authors' accepted manuscript ([LSE Research Online](https://researchonline.lse.ac.uk/id/eprint/44236/)), pages of the manuscript: §3, pp. 8–13, double counting is legitimate under a Bayesian or relative-likelihood account of incremental confirmation, the support being read from the ratio of likelihoods averaged over the conditional priors of the parameters; §5, pp. 17–20, those priors must not already incorporate the data; p. 9, posteriors and absolute confirmation are "a further matter"
- [steiner1978] ◐ Steiner, "Mathematical explanation", *Philosophical Studies* 34, 1978
- [strevens2008] ◐ Strevens, *Depth: An Account of Scientific Explanation*, Harvard University Press, 2008
- [suarez2004] ◐ Suárez, "An inferential conception of scientific representation", *Philosophy of Science* 71(5), 767–779, 2004
- [tal2013] ◐ [Tal, "Old and new problems in philosophy of measurement", *Philosophy Compass* 8(12), 1159–1173, 2013](https://doi.org/10.1111/phc3.12089)
- [vanfraassen1980] ◐ [van Fraassen, *The Scientific Image*, Clarendon Press, 1980](https://doi.org/10.1093/0198244274.001.0001); ch. 5; [the chapter text](https://www.fitelson.org/290/vanfraassen_pte.pdf)
- [weisberg2006] ◐ [Weisberg, "Robustness analysis", *Philosophy of Science* 73(5), 730–742, 2006](https://doi.org/10.1086/518628)
- [weisberg2013] ◐ [Weisberg, *Simulation and Similarity: Using Models to Understand the World*, Oxford University Press, 2013](https://doi.org/10.1093/acprof:oso/9780199933662.001.0001)
- [woodward2003] ◐ [Woodward, *Making Things Happen: A Theory of Causal Explanation*, Oxford University Press, 2003](https://doi.org/10.1093/0195155270.001.0001)
