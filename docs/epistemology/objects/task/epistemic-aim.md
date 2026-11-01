---
tags:
  - theory
index: "[Epistemic task](docs/epistemology/objects/task/_index.md)"
aliases:
  - Epistemic aim
---
# Epistemic aim

> [!QUESTION] Goal: which cognitive achievements can an inquiry seek, and what counts as a direct answer for each?

The epistemic aim specifies the kind of direct answer that a question seeks. The aim is the first dimension of the [epistemic task](epistemic-task.md), the layer that fixes the kind of knowledge that an answer carries. The aim also selects the interrogative word of the research question. Together with the subject and the other dimensions of the task, the aim fixes the type of the [direct answers](../question/question.md#^answer-sets), as the [answer form](../answer/answer-form.md#^question-fixes-type) states.

## The registry of aims

The aims form an open registry. Each entry states its category and its answer conditions, and a new entry is admitted once it states both. The tables of this note own the content of the aims, their categories and their answer conditions, and the [registry of the options of a question](../../../../src/gnomon/data/vocabularies.yml) declares their identifiers, under the [decision on registries](../../../adr/registries-as-source.md#^concept-ownership). The [specifications that each aim requires](../../../specification/question-task.md#^required-by-aim) are documented with the epistemic task of a question. ^aim-registry

| Epistemic aim | Category | Operational question | Product types admitted | Examples | Status in literature |
| ------------- | -------- | -------------------- | ---------------------- | -------- | -------------------- |
| **Description / representation** (`description`) | answer content | _What structure does the target system have?_ | `phenomenon`, already named; `model`; `classification` | _What frequency and spatial extent do the gamma oscillations of the network have during visual stimulation?_ | Core aim, and central to the literature on how models represent their targets [friggnguyen2020] |
| **Exploration** (`exploration`) | conceptual work, when its equivalence criterion is an output; answer content, when the criterion is an input | _What happens in the system when these conditions vary?_ | `phenomenon`, not yet stated; `classification` | _Which collective patterns appear in the network as the ratio of excitation to inhibition varies?_ | Recognized for models and for laboratory inquiry alike, and studied under the name *exploratory experimentation* [steinle1997] [franklin2005] |
| **Prediction** (`prediction`) | answer content | _Given specified conditions, what will occur?_ | `target-claim` | _How does gamma power change if the stimulus contrast doubles?_ | Core aim; standard philosophy of science |
| **Explanation** (`explanation`) | answer content | _Why or how does this phenomenon occur?_ | `explanation`; `model`, at modal strength `possible` | _Why does the network oscillate at gamma frequency rather than remain asynchronous?_ | Core aim; major explanation traditions |
| **Modal knowledge** (`modal-knowledge`) | answer content | _What is possible, impossible, necessary, or contingent?_ | `consequence`, when the background of the target is closed, so that its admitted laws define the system completely; `target-claim`, when it is not | _Can a network without inhibitory neurons oscillate at gamma frequency at all?_ | Legitimate epistemic aim, though classified more accurately as a *modal dimension of knowledge* than as a category coordinate with explanation or prediction |
| **Knowledge of theories / models themselves** (`model-knowledge`) | answer content | _What follows from this theory/model? How does it behave?_ | `consequence` | _Which dynamical regimes does the Wilson–Cowan model exhibit as the coupling strength varies?_ | Recognized especially in exploratory and theoretical modelling |

- **The product types transpose the classification by demand.** The [types of problem](../problem/problem-types.md) map each [product type](../../processes/activities/epistemic-activities.md#^product-types) demanded onto the aims that it admits, and remain the source of that map. The column above reads the same map by aim. Four product types are admitted by no aim: `concept` and `measurement-procedure`, which an explication delivers; `inter-theory-relation`, which an integration delivers; and `knowledge-state-change`, which the [acceptance](../status/statuses-and-acceptance.md#^acceptance-act) of an answer produces. The remaining types are products of posing a problem, of designing and recording, or of evaluating an answer, so none of them is the direct answer to a question. Two of these types are told apart by their bearer. A `target-claim`, the product of prediction, is a claim about the target, whereas a `consequence` holds of a model and may be false of the target. The activity `model-prediction` therefore outputs a consequence. That consequence becomes a claim about the target only through the step of *transfer to the target*, which carries it through a [binding](../answer/model-and-binding.md#^binding-records), the record of the imputations from model to target that its asserter licenses. The step of transfer, and the binding activity that produces a binding, are pending a change of the [registry of activities](../../../../src/gnomon/data/registries/activities.yml). ^aim-product-types

- **Exploration versus description.** Exploration and description differ in the object that their question fixes. A descriptive question names its *phenomenon* and asks for its *features*. An exploratory question names only the observables to record and the conditions to vary, so the phenomenon itself is a product of the inquiry [steinle1997]. The question therefore fixes a search space in place of a phenomenon, as an [exploratory question](../subject/phenomenon.md#^exploratory-phenomenon).

## Categories of an aim

The registry classifies each aim in one of three categories, by what a direct answer under the aim delivers. Exploration takes its category from its question, which marks its equivalence criterion as an input or as an output: ^aim-categories

- **Answer content.** A direct answer states a claim about the target or about a model, true or false of it: a value, a dependence, a possibility or a consequence. Description, prediction, explanation, modal knowledge and model knowledge fall in this category, as does an exploration whose criterion is an input.
- **Conceptual work.** A direct answer forms the terms in which a domain is described: a criterion that partitions a space into classes, or a phenomenon not yet stated. Such an answer is judged as an explication is, by its adequacy rather than by its truth [carnap1950_logical]. Exploration falls in this category when its question marks the equivalence criterion as an output, so that the answer forms the classes and the phenomena of the explored space [steinle1997]. When the question fixes the criterion as an input, the partition under that criterion is true or false of the system, and the exploration is answer content. The product type `classification` follows the same division: it is answer content under description and under an exploration whose criterion is an input, and conceptual work only under an exploration whose criterion is an output. An explication, which also delivers a concept, answers no question of a registered aim: it acts on the [definiteness](../question/conditions-of-answerability.md#^eight-conditions) of a term, and its product `concept` is admitted by no aim, as the [product types](#^aim-product-types) state.
- **Mode of inquiry.** An entry names how an inquiry proceeds rather than what its answer contains, such as an inquiry that tests a claim fixed in advance. No such entry is registered today.

Only answer content and conceptual work generate an [aim block](../../../specification/answer.md#^aim-blocks). An entry of the category mode of inquiry qualifies the itinerary of an inquiry, and its questions take the aim whose content they seek.

## Answer conditions

Each aim states three answer conditions: what counts as a direct answer, when that answer is conclusive, and what the question presupposes. A *conclusive* answer settles the question as posed, so that no further direct answer is needed. Whether the answer is true is decided afterwards, by the [warrant tests](../answer/satisfaction-conditions.md). ^answer-conditions

| Aim | Direct answer | Conclusive when | Presupposes |
| --- | ------------- | --------------- | ----------- |
| `description` | an assignment of values to the observables or the features of the named phenomenon, at the grain of the question, with the quantification over instances that its scope fixes | every variable and every feature that the request covers has a value, with its uncertainty | the phenomenon is identified, and its observables are definable at the grain |
| `exploration` | a partition of the declared space into classes under an equivalence criterion, each class with the pattern that characterizes it | the partition covers the declared space at the resolution that the request fixes, and each class reported meets the detection criterion | the observables and the varied factors can be recorded over their ranges; no phenomenon is presupposed |
| `prediction` | a value or a distribution of a declared output of the target under a stated condition, with its uncertainty | the output is among the outputs to match, and the uncertainty lies within the required accuracy | the stated condition is a condition of the target within the domain of the question |
| `explanation` | a claim that named factors determine the phenomenon by a relation of the requested kind, and, when the question names foils, that they rule out each foil | the factors determine the phenomenon by a relation of the requested kind, every named foil is ruled out by some factor, and the modal strength is the requested one | the topic holds: the fact obtains, and each named foil does not [vanfraassen1980] |
| `modal-knowledge` | a claim that a property is possible, impossible or necessary, relative to the admitted laws and the domain | a possibility is witnessed by an instance; an impossibility or a necessity is proved, or shown by an exhaustive exclusion over the space of alternatives | the admitted laws and the domain fix the space of alternatives |
| `model-knowledge` | a consequence of the laws of a model (a derived law, a regime, a limit, a structural property), or a counterexample | a checked derivation settles the property that the request names, and discharges each proof obligation that the task states | the laws of the model are stated, so that its consequences are fixed |

- **An explanation need not be contrastive.** A how-question may name no foil, as the [contrast](../subject/contrast.md) of a question admits. The direct answer then states the factors that determine the phenomenon, and the clause on foils applies only when foils are named, as the [explanans of an answer](../answer/answer-form.md#^explanans-is-not-only-contrastive) states.

- **A why-question presupposes its topic.** A why-question is answered only if its topic is true and the contrast class holds the fact [vanfraassen1980]. The presupposition of an explanation therefore reads the evidential status of the phenomenon, and the [condition of soundness](../question/conditions-of-answerability.md#^eight-conditions) checks it before any answer is sought.

- **A conclusive answer can still fail.** The answer conditions fix the *form* of a settling answer. A prediction whose uncertainty lies within the required accuracy is conclusive, and it can still be false of the target, which the warrant test of fidelity decides.

## What is not an aim

- **A change of accepted claims is not an aim.** A change of the [accepted knowledge](../../foundations/inquiry-and-state.md#^state) $K$ is the effect of [accepting or withdrawing an answer](../status/statuses-and-acceptance.md#^acceptance-act), an act of the researcher that no direct answer to a question performs. The activities of the [revision](../../processes/activities/revision.md) family carry out that change under their norm. A demand to withdraw one of two clashing claims, which a conflict generates among the [questions of each obstacle](../problem/problem-types.md#^obstacle-questions), therefore takes no aim: its result is the revision itself, and the verdicts on the clashing claims are its inputs. ^acceptance

- **Understanding is not an aim.** Much of contemporary epistemology treats understanding as an achievement beyond possessing a correct explanation. The further element is *grasping* explanatory, structural or modal relations. The object of that grasp is disputed. One account names explanatory and coherence relations [kvanvig2003], another modal dependencies [grimm2010]. A third account ties understanding to a correct explanation, as the grasp of that explanation [strevens2013] or as knowledge of it [khalifa2017]. The dispute can stay unsettled, because the ground for excluding understanding from the registry holds under every account. First, understanding always bears *on* a product of the inquiry and never takes its place. That product may be a prediction, the behavior of a model or a modal result as readily as an explanation. Second, understanding constrains the *form* of an answer, whereas each aim of the registry fixes the type of its direct answers. Understanding therefore enters an inquiry in one of two places. First, understanding is a dimension of [appraisal](../answer/satisfaction-conditions.md#^understanding-appraised), through the virtues of intelligibility and structural transparency, which the question marks preferred or [constitutive](epistemic-pragmatic-virtues.md#^virtue-standing). Second, understanding can be the [declared use](../answer/answer-form.md#^declared-use) of an answer built on a model bound to no target. ^understanding

---
## Sources

> [!NOTE] Status of the claims
> - **Established:** the account of each aim and of understanding, and the presupposition of a why-question, as cited.
> - **Proposals:**
> 	- the three categories of an aim, and the category of each registered aim, exploration in particular;
> 	- the answer conditions of each aim, with the clause on foils conditional on named foils;
> 	- a change of accepted claims kept outside the registry of aims, as the effect of an act of acceptance;
> 	- the step of transfer to the target, through a binding, between the consequence of a model and a claim about the target.

Marks follow the [legend of reading marks](../../../../CONTRIBUTING.md#^reading-marks).

- [carnap1950_logical] ◐ Carnap, *Logical Foundations of Probability*, University of Chicago Press, 1950, ch. 1; the four requirements on an explication, checked through the [Stanford Encyclopedia of Philosophy](https://plato.stanford.edu/entries/carnap/)
- [franklin2005] ◐ [Franklin, "Exploratory experiments", _Philosophy of Science_ 72(5), 2005](https://philpapers.org/rec/FRAEE)
- [friggnguyen2020] ◐ [Frigg & Nguyen, *Modelling Nature: An Opinionated Introduction to Scientific Representation*, Synthese Library 427, Springer, 2020](https://doi.org/10.1007/978-3-030-45153-0); accounts of scientific representation
- [grimm2010] ◐ [Grimm, "The goal of explanation", _Studies in History and Philosophy of Science_ 41(4), 337–344, 2010](https://philpapers.org/rec/GRITGO-12)
- [khalifa2017] ◐ [Khalifa, *Understanding, Explanation, and Scientific Knowledge*, Cambridge University Press, 2017](https://doi.org/10.1017/9781108164276); understanding as explanatory knowledge
- [kvanvig2003] ◐ [Kvanvig, *The Value of Knowledge and the Pursuit of Understanding*, Cambridge UP, 2003](https://philpapers.org/rec/KVATVO-8)
- [steinle1997] ◐ [Steinle, "Entering new fields: exploratory uses of experimentation", *Philosophy of Science* 64(S4), S65–S74, 1997](https://doi.org/10.1086/392587)
- [strevens2013] ◐ [Strevens, "No understanding without explanation", *Studies in History and Philosophy of Science Part A* 44(3), 510–515, 2013](https://doi.org/10.1016/j.shpsa.2012.12.005); understanding why as the grasp of a correct explanation
- [vanfraassen1980] ◐ [van Fraassen, *The Scientific Image*, Clarendon Press, 1980](https://doi.org/10.1093/0198244274.001.0001); ch. 5, read in its abridged reprint, "The pragmatic theory of explanation", in Pitt (ed.), *Theories of Explanation*, Oxford University Press, 1988, 136–155 ([PDF](https://www.fitelson.org/290/vanfraassen_pte.pdf))
