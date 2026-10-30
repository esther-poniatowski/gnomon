---
tags:
  - theory
index: "[Answer and assessment](docs/epistemology/objects/answer/_index.md)"
aliases:
  - Answer form
---
# Answer form

> [!QUESTION] Goal: what form must a candidate answer take, given the question that it answers?

The form of a candidate answer is derived from the [subject](../subject/subject-of-inquiry.md) and the [epistemic task](../task/epistemic-task.md) of the inquiry, and constitutes one [layer of its specification](../question/question-specification.md). The full atomic question, its [aim](../task/epistemic-aim.md) together with its parameters, fixes the type of its direct answers: a question is determined by its admissible answers [hamblin1958] [belnap1976]. A research question is a graph of atomic questions, linked by the [links between questions](../question/question.md#^linked-questions), and each candidate answer answers one atomic question. A question may stay *open*, with no answer type yet, while its answer space is not formed. Such a question admits no candidate until its answer type is fixed, as the condition of [answer type](../../processes/inquiry/conditions-of-answerability.md#^eight-conditions) states. ^question-fixes-type

> [!IMPORTANT] Conditions of satisfaction
> The tests that an answer must pass are stated before any candidate is evaluated [nosek2018]. These tests form the [conditions of satisfaction](satisfaction-conditions.md) of the answer.

> [!WARNING] The claim is sought, not specified
> The answer form is distinct from the **subject of inquiry**. The subject of inquiry, as the initial research objective, usually *fixes* the system $S$, the phenomenon $P$, the contrast $X$ and the domain $D$. The *claim* of the answer, and for an explanation its explanatory factors, the *explanans* $E$ [hempel1948], are in contrast generally *absent* from that objective. The inquiry attempts to discover them, as *components of the answer*.

## Form of the answer

The [answer record](../../../specification/answer.md) documents each field of a candidate answer, with its admitted values and examples.

- **The type of a question fixes the type of its answers.** A question is determined by its admissible answers [hamblin1958] [belnap1976], and a why-question by its topic, its contrast class and its relevance relation [vanfraassen1980]. Requiring the same components of every answer would therefore treat every question as a why-question. The core holds the elements that every claim has, and the aim block holds those that only the aim of the question requires. ^core-and-block

- **Grounds are general, and their explanatory reading is not.** Every claim depends on grounds, and sensitivity analysis, robustness analysis and explanatory proofs show that this dependence is not specific to explanation [saltelli2008] [weisberg2006] [steiner1978] [lange2017]. Only an explanation reads some dependences as difference-making of a requested kind, relative to a contrast [woodward2003] [strevens2008]. A predictor need not explain [shmueli2010]. Therefore, the grounds and the dependence belong to the core, and the claim that a dependence is explanatory belongs to the [block of an explanation](#^explanation-block). ^grounds-are-general

- **The domain of a deductive claim follows from its hypotheses.** A derivation or a proof establishes its claim only under the assumptions, the idealizations and the conditions from which it starts. The domain of such a claim is therefore read from its assumptions and its conditions, and from the range over which each idealization holds. The idealization itself does not enter the domain, since it is false of the target: a domain read from the mean-field limit would contain only the limit system. The [scope test](satisfaction-conditions.md) compares it with the domain of the question. A domain stated beside the grounds could exceed what the derivation shows. ^derived-domain

- **Idealizations license the derivation and bound the claim.** An idealization is a distortion of the target introduced on purpose [weisberg2007]. A factor omitted from the model is a distortion only when the answer is read as complete for that factor: the omission then asserts that the factor is absent. When the claim says nothing about the factor, the omission is an *abstraction*, recorded among the abstractions. An abstraction asserts nothing about the omitted factor, so it introduces no falsehood about the target, as the [truth test](../../vocabulary/representations/idealization-and-abstraction.md#^truth-test) states. An idealization serves two functions. First, it lets the laws on which the claim rests be derived from the [laws admitted in the background](../knowledge/background.md#^laws). Second, it restricts the range over which the claim holds. Each idealization names one of three motives: tractability, isolation or limit. For *tractability*, the idealization applies where the undistorted system admits no analysis. For *isolation*, the idealization removes a factor judged irrelevant. For a *limit*, the idealization exposes the behavior of a limit system. Each idealization also states the gain that it brings, since an assumption whose benefit cannot be named is not needed [weisberg2007]. Idealizations also differ in whether they can be removed, and the field `removable` records that difference. A controlled idealization is removed by *de-idealization*, in successive steps, since a correction to the idealized result is known. Other idealizations are ineliminable: the model cannot be stated without these assumptions. Where neither status is known, the field holds `unknown`. Whether an assumption distorts depends on the target, which is a relation between the model and the target [weisberg2007]. The [model](../../../specification/model.md#^model-elements) therefore declares only the assumptions that its laws require, with their motive, gain and removability, since these do not depend on the target. The answer classifies each assumption on which its claim depends: as an idealization of its target, with the range over which it holds, or as a restriction of the domain under the [rule on limits](../../../specification/answer.md#^limit-rule). An idealization is thus recorded once, as a ground with the role `idealization`, and the [robustness test](satisfaction-conditions.md) checks whether the claim survives each of them. ^idealizations

- **The erotetic relation states how far the answer answers its question.** The relation takes four values, and each of them routes the [assessment](satisfaction-conditions.md#^erotetic-routing) of the answer: ^erotetic-relation
    - **complete**: the answer is a direct answer that is [conclusive](../task/epistemic-aim.md#^answer-conditions) under the answer conditions of its aim;
    - **partial**: the answer narrows the direct answers of the same question without being conclusive. Its aim block holds the part of the request that the answer settles, and the question stays open to a further answer that settles the rest;
    - **corrective**: the answer shows that a presupposition of the question is false [belnap1976]. A corrective answer holds no aim block, since the question has no true direct answer. Once accepted, the answer refutes the [soundness](../../processes/inquiry/conditions-of-answerability.md#^eight-conditions) of the question, and an outright refutation [dissolves](../problem/epistemic-problem.md#^problem-outcomes) the problem that the question serves;
    - **reformulating**: the answer answers a revised question, which it names, and it is assessed against that revised question.

- **An answer whose claim bears on no target declares its use.** A model can be studied without being bound to any phenomenon: as a tool, as a proof of principle that a behavior can arise, as a conceptual exploration of a class of models, or for the understanding that it affords. Such an answer cites no binding and states its use instead. A declared use is admitted only when the claim bears on a model or on a formal class: ^declared-use
    - a consequence or a counterexample of model knowledge;
    - a modal claim whose witness is a model;
    - an exploration of a class of models;
    - a claim of possible strength over a formal target.

  A claim of actual strength about an empirical target, and any prediction or description of a target, requires a binding instead, since only a binding lets fidelity be computed. The declared use states the property that the model must have for that use, such as the behavior that a proof of principle exhibits, and the warrant test of [adequacy to use](satisfaction-conditions.md#^warrant-through-binding) checks that property [parker2020]. Understanding, when an inquiry seeks it from such a model, is one declared use, as the [epistemic aim](../task/epistemic-aim.md#^understanding) states.

- **A link between two substrates is answered by a *mapping*.** A question that bounds the explanans to the [link between two substrates](../task/admissible-explanans.md) asks how a role is realized. Neither of the two descriptions alone answers that question: the description specific to one substrate states the events without the role that they play, and the description independent of any substrate states the role without its carrier. The model declares both descriptions, since each of them consists of quantities and laws. The claim of the answer then states, per mapping, which expression over one substrate realizes which role [marr1982] [bechtel2015]. Only the mapping is new, and it can be false, so it belongs to the claim rather than to the model. ^link-is-a-mapping

- **Answers are linked by typed relations.** Five relations link one answer to another: ^answer-relations
    - `supports`: the claim of the answer is a ground of the other answer;
    - `presupposes`: the answer is admissible only if the other answer is true;
    - `tests`: the claim of the answer is a consequence of the other answer, compared with the target;
    - `defeats`: the claim of the answer, once accepted, removes a ground of the other answer;
    - `revises`: the answer replaces the other answer over time. The earlier answer stays unchanged, and the relation records the lineage of the answer.

- **The route of an answer decides whether it needs a model record.** The [rule on models and bindings](model-and-binding.md#^when-a-binding) states, for each object on which a route can run, whether the answer needs a model record and a binding.

## The block of an explanation

The block of an explanation holds what makes the dependences of the core explanatory. An explanatory proof, which explains why a mathematical result holds, is an answer of model knowledge linked to this block by `supports` [steiner1978] [lange2017]. ^explanation-block

- **How-actually and how-possibly follow from the modal strength.** The explanation claims the modal strength that its core states, and the [modal strength](../task/modal-strength.md) requested by the question decides whether the explanation must be how-actually or how-possibly. The block holds no field of its own for that distinction.

- **A factor need not exist in the target.** Minimal models, holistic distortions and explanations by constraint explain without a correspondence between their factors and parts of the target [battermanrice2014] [rice2021] [lange2017]. Each factor therefore carries a *target status*, which states how it bears on the target. When the route runs on a model, the [binding](../../../specification/binding.md#^binding-record) of the answer supplies what that status requires: ^target-status
    - **denoting**: the factor denotes a quantity or a part of the target, and a feature pair of type `quantity`, or of type `component` for a unit of the model alone, carries it onto that quantity or that part;
    - **coarse-graining**: the factor describes a feature of the target at a stated level, and a feature pair of type `pattern` or `regime` carries it onto that feature;
    - **limit construct**: the factor holds only in a limit system. A feature pair of type `invariance-class` places the target in the universality class of that limit, and the argument for that placement is a ground of the answer with the role `warrant`;
    - **structural constraint**: the factor is a constraint that the target is claimed to satisfy, such as a symmetry, a conservation law or a bound, stated through a feature pair of type `invariance-class` or `modal-profile`.

  When the route runs on the target itself, a factor stated over the symbols of the target is `denoting` by declaration, and no binding is needed. Under a [declared use](#^declared-use), the claim bears on no target, so no factor carries a target status.

- **The explanatory claim names the determinant, including for a nomological or a mathematical relation.** The laws of a model can reproduce the phenomenon by derivation without identifying its determinant. The explanatory claim must therefore name the property that makes the law, the structure or the derivation relevant (e.g. a symmetry, a conservation, a bound, a rank, a saturation). This requirement is essential for an explanation that rests on a *constraint*: a fact more necessary than the ordinary laws, such as a symmetry or a conservation law [lange2017].

- **A factor is a property, possibly stated in no record.** A factor rarely coincides with a declared element. Instead, the factor is a condition on such an element, or one of its properties. Such properties include a law that is invariant, additive or factorizing, a structure that is sparse or low-rank, and an arrangement that closes a feedback loop. Such a property is often *found* by the answer and absent from every earlier record. ^factor-may-be-found

- **A factor states its *path* to the phenomenon.** A list of factors alone leaves unstated how each of them contributes: the same quantity may enter two accounts and support each of them for a different reason. A factor therefore states its claim and the element on which it bears. The factor also states the laws and [relations of the organization](../knowledge/background.md#^organization) that carry its effect, and the explanandum variable or manifestation that it accounts for. This chain consists of symbols that the records already declare, so a reader can follow it from the factor to the phenomenon. The steps that the chain leaves unstated, however, belong to the `procedure` of the factor. ^factor-states-its-chain

- **A factor supports the explanation whether or not the question names a foil.** The explanation relies on a determinant property that makes the phenomenon arise, whether the question names no foil or two. Questions without a foil occur in practice: three of the seven test inquiries state a [contrast](../subject/contrast.md) whose locus is `none`. For those three, an explanans defined as the difference between fact and foil cannot be filled. The claim of a factor therefore states the determinant on which the explanation relies. The demand to separate fact from foil stays instead in the record of the contrast. Where a foil is named, a factor states which foils it rules out, and the contrast test compares that statement. ^explanans-is-not-only-contrastive

- **An explanation may draw on the environment, and then names the external system on which it draws.** The external systems pass the [inclusion test](../subject/subject-of-inquiry.md#^inclusion-test) of the subject of inquiry. An explanation may therefore account for the phenomenon by the structure of the inputs, or by the class of system that reads the outputs. Each factor that draws on the environment names the external system involved, which resolves to an [external system](../subject/target-system.md) that the target declares. When the route runs on a model, the model declares its own counterpart of that external system, and the binding pairs the two. ^explanans-appeals

- **The choice of terms determines [epistemic and pragmatic virtues](../task/epistemic-pragmatic-virtues.md).** An explanation may pass the tests of [admissibility and warrant](satisfaction-conditions.md) and still leave implicit the factors on which it rests. Its characteristic consequences then cannot be recognized without the full calculation [deregt2005]. The factors stay implicit because they may appear only in derived terms. Such factors express novel and robust behavior, yet remain deducible from the microscopic description [butterfield2011]. The terms that the model retains therefore determine virtues such as economy, generality, structural transparency and intelligibility. *Example*: the question "how does a trained network solve this task?" is answered completely, in declared variables, by composing the local operations of every neuron across layers. The factors on which the explanation rests, however, appear in a few collective coordinates of the population dynamics [vyas2020], in the eigenmodes of the connectivity, or in mean-field order parameters. A model that [re-individuates the system](model-and-binding.md#^perspective) is therefore judged by the factors that the explanation makes explicit. The [conditions of satisfaction](satisfaction-conditions.md) that the question already imposes perform that judgement.

The answer to a why-question takes the form "$P$, in contrast to (the rest of) $X$ because $E$" [vanfraassen1980]. The claim of an explanation fills that form with the elements of the core, of the block and of the model, in a sentence frame:

> In [S] under [D], [P] rather than [X], because [E], related to [Y] by [relation R] through [L], assuming [I].

*Example* of an explanatory answer:

- target system $S$: a network of excitatory and inhibitory neurons;
- background conditions $D$: under constant drive;
- explanandum $P$: synchronous oscillations at gamma frequency;
- contrast $X$: asynchronous activity under the same drive;
- factors $E$: inhibitory feedback with a synaptic delay, destabilizing the asynchronous state; the delay denotes the synaptic delay of the network;
- relation $R$ and laws $L$: a mathematical derivation, through the linear stability of the mean-field rate equations of the model;
- idealizations $I$: the mean-field limit of infinitely many neurons, an assumption that the laws of the model require, classified by the answer as an idealization of the finite network and recorded among its grounds.

When the [requested relation](../task/requested-relation.md) is mechanistic or constitutive, the elements of the model and of the block map onto the constituents of a [mechanism](mechanism.md):

| Constituent of a [mechanism](mechanism.md)                                       | Element of the model or of the block                                                                     |
| ---------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| components (entities)                                                              | the constituents $C$ of the model, possibly other than those [declared for the system](../subject/target-system.md) |
| properties and states of the components                                            | the terms $V$ of the model                                                                               |
| activities and interactions                                                        | the laws or structural relations $L$ of the model                                                        |
| organization                                                                       | the organization $O$ of the model                                                                        |
| the components, activities and organization that make the difference to $P$        | the factors $E$ of the block                                                                             |

In a reduced model, the components of the mechanism are the [re-individuated constituents](model-and-binding.md#^perspective): modes, collective coordinates or effective units, each carrying its defining map. The mechanism is then stated over those units, and the declared constituents appear only through that map.

For a nomological, statistical or mathematical relation, the organization $O$ of the model stays empty, and its laws $L$ carry the law, the probabilistic dependence or the derivation.

---
## Sources

> [!NOTE] Status of the claims
> - **Established:** the determination of a question by its admissible answers, the generality of dependence beyond explanation, the explanatory roles of distortions and constraints, and the account of each element, as cited.
> - **Proposals:**
> 	- one typed claim per answer, with a core shared by every aim and one aim block;
> 	- the roles of a ground, and the domain of a deductive claim derived from its grounds;
> 	- the declaration of an assumption by the model and its classification as an idealization by the answer, relative to its target, with abstractions kept apart from the grounds;
> 	- the four values of the erotetic relation and the five relations between answers;
> 	- the declared use, admitted only for a claim on a model or a formal class, with an open list of uses;
> 	- an explanatory proof recorded as an answer of model knowledge that supports an explanation;
> 	- the four target statuses of a factor, each with the feature pair that it requires;
> 	- the four kinds of factor (a condition on a quantity, a property of a structure, a property of a law, a feature of the organization);
> 	- the mapping of the elements onto a mechanism, written in the [shared notation](../../vocabulary/notation/notation.md).

Marks follow the [legend of reading marks](../../../../CONTRIBUTING.md#^reading-marks).

- [battermanrice2014] ◐ Batterman & Rice, "Minimal model explanations", *Philosophy of Science* 81(3), 349–376, 2014
- [bechtel2015] ◐ [Bechtel & Shagrir, "The non-redundant contributions of Marr's three levels of analysis for explaining information-processing mechanisms", *Topics in Cognitive Science* 7(2), 2015](https://onlinelibrary.wiley.com/doi/10.1111/tops.12141)
- [belnap1976] ○ Belnap & Steel, *The Logic of Questions and Answers*, Yale University Press, 1976; questions fixed by their answers, and corrective answers, which deny a presupposition
- [butterfield2011] ◐ [Butterfield, "Less is different: emergence and reduction reconciled", _Foundations of Physics_ 41, 2011](https://philpapers.org/rec/BUTLID)
- [deregt2005] ◐ [de Regt & Dieks, "A contextual approach to scientific understanding", _Synthese_ 144, 2005](https://link.springer.com/article/10.1007/s11229-005-5000-4); criterion for intelligibility checked through secondary summaries
- [hamblin1958] ○ Hamblin, "Questions", *Australasian Journal of Philosophy* 36, 1958
- [hempel1948] ○ Hempel & Oppenheim, "Studies in the logic of explanation", _Philosophy of Science_ 15(2), 1948
- [lange2017] ◐ [Lange, _Because Without Cause: Non-Causal Explanations in Science and Mathematics_, OUP, 2017](https://global.oup.com/academic/product/because-without-cause-9780190269487), part I on explanations by constraint
- [marr1982] ○ Marr, *Vision*, Freeman, 1982
- [nosek2018] ◐ [Nosek, Ebersole, DeHaven & Mellor, "The preregistration revolution", _PNAS_ 115(11), 2018](https://www.pnas.org/doi/10.1073/pnas.1708274114)
- [parker2020] ◐ Parker, "Model evaluation: an adequacy-for-purpose view", *Philosophy of Science* 87(3), 457–477, 2020
- [rice2021] ◐ Rice, *Leveraging Distortions: Explanation, Idealization, and Universality in Science*, MIT Press, 2021
- [saltelli2008] ○ Saltelli et al., *Global Sensitivity Analysis: The Primer*, Wiley, 2008
- [shmueli2010] ○ Shmueli, "To explain or to predict?", *Statistical Science* 25(3), 2010
- [steiner1978] ◐ Steiner, "Mathematical explanation", *Philosophical Studies* 34, 1978
- [strevens2008] ○ Strevens, *Depth: An Account of Scientific Explanation*, Harvard University Press, 2008
- [vanfraassen1980] ✓ van Fraassen, _The Scientific Image_, ch. 5; [the chapter text](https://www.fitelson.org/290/vanfraassen_pte.pdf)
- [vyas2020] ◐ [Vyas, Golub, Sussillo & Shenoy, "Computation through neural population dynamics", _Annual Review of Neuroscience_ 43, 2020](https://www.annualreviews.org/content/journals/10.1146/annurev-neuro-092619-094115)
- [weisberg2006] ◐ [Weisberg, "Robustness analysis", _Philosophy of Science_ 73(5), 2006](https://philpapers.org/rec/MICRA)
- [weisberg2007] ◐ [Weisberg, "Three kinds of idealization", _Journal of Philosophy_ 104(12), 2007](https://www.pdcnet.org/jphil/content/jphil_2007_0104_0012_0639_0659); de-idealization and ineliminable idealizations checked through [SEP, "Models in science"](https://plato.stanford.edu/entries/models-science/)
- [woodward2003] ○ [Woodward, _Making Things Happen_, OUP, 2003](https://academic.oup.com/book/4324)
