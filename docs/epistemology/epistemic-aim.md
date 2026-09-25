---
role: definition
status: stable
index: "[Epistemology](docs/epistemology/_index.md)"
aliases:
  - Specifying the epistemic aim
  - Epistemic aim
tags: []
source:
---
# Specifying the epistemic aim

> [!QUESTION] Goal: what must be fixed to specify the kind of knowledge an inquiry seeks?

The epistemic aim specifies the cognitive achievement that an answer must deliver. The aim is the first dimension of the [epistemic task](epistemic-task.md), the layer that fixes the kind of knowledge that an answer carries. The aim also selects the interrogative word of the research question.

| Epistemic aim                                 | Operational question                                       | Epistemic product                                                                        | Examples                                                                                                     | Status in literature                                                                                                                                         |
| --------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Description / representation**              | _What structure does the target system have?_              | accurate characterization of states, patterns, properties, relations                     | _What frequency and spatial extent do the gamma oscillations of the network have during visual stimulation?_ | Core aim [deregt2005], and central to the literature on how models represent their targets                                                                                                           |
| **Exploration**                               | _What happens in the system when these conditions vary?_   | a phenomenon identified and characterized, or new concepts, classifications or regularities | _Which collective patterns appear in the network as the ratio of excitation to inhibition varies?_           | Recognized for models and for laboratory inquiry alike, and studied under the name *exploratory experimentation* [steinle1997] [franklin2005]                                                                 |
| **Prediction**                                | _Given specified conditions, what will occur?_             | warranted expectation about unknown outcomes                                             | _How does gamma power change if the stimulus contrast doubles?_                                              | Core aim; standard philosophy of science                                                                                                                     |
| **Explanation**                               | _Why or how does this phenomenon occur?_                   | explanatory relations identified — causal, mechanistic, mathematical, etc.        | _Why does the network oscillate at gamma frequency rather than remain asynchronous?_                         | Core aim; major explanation traditions                                                                                                                       |
| **Modal knowledge**                           | _What is possible, impossible, necessary, or contingent?_  | possibility /  impossibility / necessity claims                                          | _Can a network without inhibitory neurons oscillate at gamma frequency at all?_                              | Legitimate epistemic aim, though classified more accurately as a *modal dimension of knowledge* than as a category coordinate with explanation or prediction |
| **Knowledge of theories / models themselves** | _What follows from this theory/model? How does it behave?_ | consequences, regimes, limits, structural properties                                     | _Which dynamical regimes does the Wilson–Cowan model exhibit as the coupling strength varies?_               | Recognized especially in exploratory and theoretical modelling                                                                                               |

**Exploration versus description.** Exploration and description differ in the object that their question fixes:

- A descriptive question names its *phenomenon* and asks for its *features*.
- An exploratory question names only the observables to record and the conditions to vary, so the phenomenon itself is a product of the inquiry [steinle1997]. The question therefore fixes a search space in place of a phenomenon, as an [exploratory question](phenomenon.md#^exploratory-phenomenon).

**Understanding is not a coordinate aim.** Contemporary epistemology treats understanding as an achievement beyond possessing a correct explanation. The further element is *grasping* explanatory, structural or modal relations. The object of that grasp is disputed. One account names explanatory and coherence relations [kvanvig2003], another modal dependencies [grimm2010]. A third account identifies understanding with knowledge of an explanation (Khalifa, Strevens). The dispute can stay unsettled, because the ground for excluding understanding from the table of aims holds under every account. First, understanding always bears *on* a product of the inquiry and never takes its place. That product may be a prediction, the behavior of a model or a modal result as readily as an explanation. Second, the aim admits a single value, so an inquiry that declares understanding as its aim can pursue no other aim. An inquiry that demands understanding instead declares one of the aims in the table and fixes two requirements under it: its account must be followable, and the dependences on which it rests must be exposed. These two requirements amount to a [constitutive standing](epistemic-pragmatic-virtues.md#^virtue-standing) for intelligibility and structural transparency. The two virtues constrain the *form* of an answer. Each aim in the table instead fixes the subject of an answer and its required *content*. Understanding, a demand on form, is therefore excluded from a table whose aims fix content.

## Specifications each aim requires

Because an aim fixes the product that an answer must deliver, the aim also determines the specifications that the inquiry cannot leave open. Each aim adds specifications to those every inquiry fixes. An aim may also relax some general specifications: an aim that produces a phenomenon cannot require the question to state it in advance. The third column therefore lists the specifications that a note marks as always required but that the aim admits open. A dash marks an aim that neither adds nor relaxes a specification. Each dash is attested by a filled inquiry that pursues the aim and fixes nothing beyond the general requirements. Each entry names a field path. Each row documents the entry for one aim in the registry of [required fields](../../src/gnomon/data/requirements.yml), the authoritative source of the table. ^required-by-aim

| Aim | Additionally required | Admitted open, although required in general |
| --- | --- | --- |
| `description` | — | — |
| `exploration` | `phenomenon.detection_criterion` | `phenomenon.statement`, `phenomenon.category`, `phenomenon.evidential_status` |
| `prediction` | `phenomenon.manifestations`, `question.task.required_accuracy.outputs_to_match` | — |
| `explanation` | `question.subject.contrast.foil_set`, `question.task.requested_relation` | — |
| `modal-knowledge` | `question.task.modal_strength`, `question.task.proof_obligations` | — |
| `model-knowledge` | — | — |

- **An exploratory inquiry fixes no phenomenon in advance, so it must fix the criterion that would establish one.** The exploratory inquiry leaves open the statement, the category, the evidential status and the form of the manifestation, although every other aim fixes these four specifications. In their place, the detection criterion states the test that a candidate pattern must pass. The exploratory case illustrates a general division: a general requirement lists the fields of a complete record, and an aim marks the fields that an incomplete record may omit without error.

- **Only prediction compares an output against a measurement in every inquiry**, so the field `outputs_to_match` is required for this aim alone. An aim that seeks a proof, by contrast, requires no output to match, so an absent accuracy is *correct* for that aim.

---
## Sources

Marks follow the [legend of reading marks](../../CONTRIBUTING.md#^reading-marks).

- [steinle1997] ◐ [Steinle, "Entering new fields: exploratory uses of experimentation", *Philosophy of Science* 64, S65–S74, 1997](https://philpapers.org/rec/STEENF)
- [deregt2005] ◐ [de Regt & Dieks, "A contextual approach to scientific understanding", _Synthese_ 144, 2005](https://link.springer.com/article/10.1007/s11229-005-5000-4); criterion for intelligibility checked through secondary summaries
- [franklin2005] ◐ [Franklin, "Exploratory experiments", _Philosophy of Science_ 72(5), 2005](https://philpapers.org/rec/FRAEE)
- [grimm2010] ◐ [Grimm, "The goal of explanation", _Studies in History and Philosophy of Science_ 41(4), 337–344, 2010](https://philpapers.org/rec/GRITGO-12)
- [kvanvig2003] ◐ [Kvanvig, *The Value of Knowledge and the Pursuit of Understanding*, Cambridge UP, 2003](https://philpapers.org/rec/KVATVO-8)
