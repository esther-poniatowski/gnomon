---
tags:
  - method
index: "[Epistemic task](docs/epistemology/epistemic-task/_index.md)"
aliases:
  - Specifying the epistemic aim
  - Epistemic aim
---
# Specifying the epistemic aim

> [!QUESTION] Goal: what must be fixed to specify the kind of knowledge an inquiry seeks?

The epistemic aim specifies the kind of direct answer that a question seeks. The aim is the first dimension of the [epistemic task](epistemic-task.md), the layer that fixes the kind of knowledge that an answer carries. The aim also selects the interrogative word of the research question. Together with the other parameters of the question, the aim fixes the type of the direct answers, as the [answer form](../answer/answer-form.md#^question-fixes-type) states.

## The registry of aims

The aims form an open registry. Each entry states its category and its answer conditions, and a new entry is admitted once it states both. The [registry of the options of a question](../../../src/gnomon/data/vocabularies.yml) lists the aims registered today, and the registry of [required fields](../../../src/gnomon/data/requirements.yml) states what each of them requires. ^aim-registry

| Epistemic aim | Category | Operational question | Product types admitted | Examples | Status in literature |
| ------------- | -------- | -------------------- | ---------------------- | -------- | -------------------- |
| **Description / representation** (`description`) | answer content | _What structure does the target system have?_ | `phenomenon`, already named; `model`; `classification` | _What frequency and spatial extent do the gamma oscillations of the network have during visual stimulation?_ | Core aim [deregt2005], and central to the literature on how models represent their targets |
| **Exploration** (`exploration`) | conceptual work, when its equivalence criterion is an output; answer content, when the criterion is an input | _What happens in the system when these conditions vary?_ | `phenomenon`, not yet stated; `classification` | _Which collective patterns appear in the network as the ratio of excitation to inhibition varies?_ | Recognized for models and for laboratory inquiry alike, and studied under the name *exploratory experimentation* [steinle1997] [franklin2005] |
| **Prediction** (`prediction`) | answer content | _Given specified conditions, what will occur?_ | `hypothesis` | _How does gamma power change if the stimulus contrast doubles?_ | Core aim; standard philosophy of science |
| **Explanation** (`explanation`) | answer content | _Why or how does this phenomenon occur?_ | `explanation`; `model`, at modal strength `possible` | _Why does the network oscillate at gamma frequency rather than remain asynchronous?_ | Core aim; major explanation traditions |
| **Modal knowledge** (`modal-knowledge`) | answer content | _What is possible, impossible, necessary, or contingent?_ | `consequence`, when the background of the target is closed; `hypothesis`, when it is not | _Can a network without inhibitory neurons oscillate at gamma frequency at all?_ | Legitimate epistemic aim, though classified more accurately as a *modal dimension of knowledge* than as a category coordinate with explanation or prediction |
| **Knowledge of theories / models themselves** (`model-knowledge`) | answer content | _What follows from this theory/model? How does it behave?_ | `consequence` | _Which dynamical regimes does the Wilson–Cowan model exhibit as the coupling strength varies?_ | Recognized especially in exploratory and theoretical modelling |

- **The product types transpose the classification by demand.** The [types of problem](../definitions/inquiry/problem-types.md) map each [product type](../definitions/activities/epistemic-activities.md#^product-types) demanded onto the aims that it admits, and remain the source of that map. The column above reads the same map by aim. Four product types are admitted by no aim: `concept` and `measurement-procedure`, which an explication delivers; `inter-theory-relation`, which an integration delivers; and `knowledge-state-change`, which the [acceptance](#^acceptance) of an answer produces. The remaining types are products of posing a problem, of designing and recording, or of evaluating an answer, so none of them is the direct answer to a question. ^aim-product-types

- **Exploration versus description.** Exploration and description differ in the object that their question fixes. A descriptive question names its *phenomenon* and asks for its *features*. An exploratory question names only the observables to record and the conditions to vary, so the phenomenon itself is a product of the inquiry [steinle1997]. The question therefore fixes a search space in place of a phenomenon, as an [exploratory question](../subject/phenomenon.md#^exploratory-phenomenon).

## Categories of an aim

The registry classifies each aim in one of three categories, by what a direct answer under the aim delivers. Exploration takes its category from its question, which marks its equivalence criterion as an input or as an output: ^aim-categories

- **Answer content.** A direct answer states a claim about the target or about a model, true or false of it: a value, a dependence, a possibility or a consequence. Description, prediction, explanation, modal knowledge and model knowledge fall in this category, as does an exploration whose criterion is an input.
- **Conceptual work.** A direct answer forms the terms in which a domain is described: a criterion that partitions a space into classes, or a phenomenon not yet stated. Such an answer is judged by its adequacy rather than by its truth, as an explication is [carnap1950_logical]. Exploration falls in this category when its question marks the equivalence criterion as an output, so that the answer forms the classes and the phenomena of the explored space [steinle1997]. When the question fixes the criterion as an input, the partition under that criterion is true or false of the system, and the exploration is answer content. The product type `classification` follows the same division: it is answer content under description and under an exploration whose criterion is an input, and conceptual work only under an exploration whose criterion is an output. An explication, which also delivers a concept, answers no question of a registered aim: it acts on the [definiteness](../definitions/inquiry/conditions-of-answerability.md#^eight-conditions) of a term, and its product `concept` is admitted by no aim, as the [product types](#^aim-product-types) state.
- **Mode of inquiry.** An entry names how an inquiry proceeds rather than what its answer contains, such as an inquiry that tests a claim fixed in advance. No such entry is registered today.

Only answer content and conceptual work generate an [aim block](../answer/answer-form.md#^aim-blocks). An entry of the category mode of inquiry qualifies the itinerary of an inquiry, and its questions take the aim whose content they seek.

## Answer conditions

Each aim states three answer conditions: what counts as a direct answer, when that answer is conclusive, and what the question presupposes. A *conclusive* answer settles the question as posed, so that no further direct answer is needed. Whether the answer is true is decided afterwards, by the [warrant tests](../answer/satisfaction-conditions.md). ^answer-conditions

| Aim | Direct answer | Conclusive when | Presupposes |
| --- | ------------- | --------------- | ----------- |
| `description` | an assignment of values to the explanandum variables or the features of the named phenomenon, at the grain of the question, with the quantification over instances that its scope fixes | every variable and every feature that the request covers has a value, with its uncertainty | the phenomenon is identified, and its explanandum variables are definable at the grain |
| `exploration` | a partition of the declared space into classes under an equivalence criterion, each class with the pattern that characterizes it | the partition covers the declared space at the resolution that the request fixes, and each class reported meets the detection criterion | the observables and the varied factors can be recorded over their ranges; no phenomenon is presupposed |
| `prediction` | a value or a distribution of a declared output of the target under a stated condition, with its uncertainty | the output is among the outputs to match, and the uncertainty lies within the required accuracy | the stated condition is a condition of the target within the domain of the question |
| `explanation` | a claim that named factors make the difference between the fact and each foil, by a relation of the requested kind | every foil of the contrast is ruled out by some factor, the relation has the requested kind, and the modal strength is the requested one | the topic holds: the fact obtains, and each foil does not [vanfraassen1980] |
| `modal-knowledge` | a claim that a property is possible, impossible or necessary, relative to the admitted laws and the domain | a possibility is witnessed by an instance; an impossibility or a necessity is proved, or established by an exhaustive exclusion over the space of alternatives | the admitted laws and the domain fix the space of alternatives |
| `model-knowledge` | a consequence of the laws of a model (a derived law, a regime, a limit, a structural property), or a counterexample | a checked derivation settles the property that the request names, and discharges each proof obligation that the task states | the laws of the model are stated, so that its consequences are fixed |

- **A why-question presupposes its topic.** A why-question is answered only if its topic is true and the contrast class holds the fact [vanfraassen1980]. The presupposition of an explanation therefore reads the evidential status of the phenomenon, and the [condition of soundness](../definitions/inquiry/conditions-of-answerability.md#^eight-conditions) checks it before any answer is sought.

- **A conclusive answer can still fail.** The answer conditions fix the *form* of a settling answer. A prediction whose uncertainty lies within the required accuracy is conclusive, and it can still be false of the target, which the warrant test of fidelity decides.

## What is not an aim

- **A change of accepted claims is not an aim.** A change of accepted claims is the effect of accepting an answer: a revision of the belief base $K$ of an inquiry, a finite set of accepted claims on a named corpus [hansson1999] [levi1980]. The revision also has a named owner, the researcher or the group that accepts. Its record names the corpus revised, the owner, the answer accepted or withdrawn, and the verdict, credence or ranking on which the revision rests. The activities of the revision family perform it, `belief-revision` for one answer, and the [proposed candidates](../definitions/inquiry/epistemic-problem.md#^candidates) enter the background only through them. A demand to withdraw one of two clashing claims, which a conflict generates among the [questions of each obstacle](../definitions/inquiry/problem-types.md#^obstacle-questions), therefore takes no aim: its result is the revision itself, and the verdicts on the clashing claims are its inputs. ^acceptance

- **Understanding is not an aim.** Contemporary epistemology treats understanding as an achievement beyond possessing a correct explanation. The further element is *grasping* explanatory, structural or modal relations. The object of that grasp is disputed. One account names explanatory and coherence relations [kvanvig2003], another modal dependencies [grimm2010]. A third account identifies understanding with knowledge of an explanation (Khalifa, Strevens). The dispute can stay unsettled, because the ground for excluding understanding from the registry holds under every account. First, understanding always bears *on* a product of the inquiry and never takes its place. That product may be a prediction, the behavior of a model or a modal result as readily as an explanation. Second, understanding constrains the *form* of an answer, whereas each aim of the registry fixes the type of its direct answers. Understanding therefore enters an inquiry in one of two places. First, understanding is a dimension of [appraisal](../answer/satisfaction-conditions.md#^understanding-appraised), through the virtues of intelligibility and structural transparency, which the question marks preferred or [constitutive](epistemic-pragmatic-virtues.md#^virtue-standing). Second, understanding can be the [declared use](../answer/answer-form.md#^declared-use) of an answer built on a model bound to no target. ^understanding

## Specifications each aim requires

Because an aim fixes the product that an answer must deliver, the aim also determines the specifications that the inquiry cannot leave empty. Each aim adds specifications to those every inquiry fixes. Under some aims, the inquiry itself produces some general specifications: an aim that produces a phenomenon cannot require the question to state it in advance. Therefore, the third column lists the specifications that a note marks as required in general but that the inquiry itself produces. On those paths alone, an empty field is admitted. A dash marks an aim that neither adds nor produces a specification. Each dash is attested by a filled inquiry that pursues the aim and fixes nothing beyond the general requirements. Each entry names a field path. Each row documents the entry for one aim in the registry of [required fields](../../../src/gnomon/data/requirements.yml), the authoritative source of the table. ^required-by-aim

| Aim | Additionally required | Produced by the inquiry, although required in general |
| --- | --- | --- |
| `description` | — | — |
| `exploration` | `phenomenon.detection_criterion` | `phenomenon.statement`, `phenomenon.category`, `phenomenon.occurrence`, `phenomenon.evidential_status` |
| `prediction` | `phenomenon.manifestations`, `question.task.required_accuracy.outputs_to_match` | — |
| `explanation` | `question.subject.contrast.foil_set`, `question.task.requested_relation` | — |
| `modal-knowledge` | `question.task.modal_strength`, `question.task.proof_obligations` | — |
| `model-knowledge` | — | — |

- **An exploratory inquiry fixes no phenomenon in advance, so it must fix the criterion that would establish one.** The exploratory inquiry produces the statement, the category, the occurrence class and the evidential status, although every other aim fixes these four specifications. In their place, the detection criterion states the test that a candidate pattern must pass. Exploration illustrates a general division: a general requirement lists the fields of a complete record, and an aim marks the fields that the inquiry itself fills.

- **Only prediction compares an output against a measurement in every inquiry**, so the field `outputs_to_match` is required for this aim alone. An aim that seeks a proof, by contrast, requires no output to match, so an absent accuracy is *correct* for that aim.

---
## Sources

> [!NOTE] Status of the claims
> - **Established:** the account of each aim and of understanding, the presupposition of a why-question, and belief bases, as cited.
> - **Proposals:**
> 	- the three categories of an aim, and the category of each registered aim, exploration in particular;
> 	- the answer conditions of each aim;
> 	- acceptance as a revision of a belief base on a named corpus with a named owner, outside the registry of aims.

Marks follow the [legend of reading marks](../../../CONTRIBUTING.md#^reading-marks).

- [carnap1950_logical] ◐ Carnap, *Logical Foundations of Probability*, University of Chicago Press, 1950, ch. 1; the four requirements on an explication, checked through the [Stanford Encyclopedia of Philosophy](https://plato.stanford.edu/entries/carnap/)
- [deregt2005] ◐ [de Regt & Dieks, "A contextual approach to scientific understanding", _Synthese_ 144, 2005](https://link.springer.com/article/10.1007/s11229-005-5000-4); criterion for intelligibility checked through secondary summaries
- [franklin2005] ◐ [Franklin, "Exploratory experiments", _Philosophy of Science_ 72(5), 2005](https://philpapers.org/rec/FRAEE)
- [grimm2010] ◐ [Grimm, "The goal of explanation", _Studies in History and Philosophy of Science_ 41(4), 337–344, 2010](https://philpapers.org/rec/GRITGO-12)
- [hansson1999] ○ Hansson, *A Textbook of Belief Dynamics*, Kluwer, 1999; belief bases, as opposed to belief sets closed under consequence
- [kvanvig2003] ◐ [Kvanvig, *The Value of Knowledge and the Pursuit of Understanding*, Cambridge UP, 2003](https://philpapers.org/rec/KVATVO-8)
- [levi1980] ○ Levi, *The Enterprise of Knowledge*, MIT Press, 1980; the corpus of knowledge relative to which inquiry proceeds
- [steinle1997] ◐ [Steinle, "Entering new fields: exploratory uses of experimentation", *Philosophy of Science* 64, S65–S74, 1997](https://philpapers.org/rec/STEENF)
- [vanfraassen1980] ✓ van Fraassen, _The Scientific Image_, ch. 5; [the chapter text](https://www.fitelson.org/290/vanfraassen_pte.pdf)
