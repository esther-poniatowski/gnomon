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

The epistemic aim is the first dimension of the [epistemic task](epistemic-task.md): the cognitive achievement that the answer must deliver. The aim also selects the interrogative word of the research question.

| Epistemic aim                                 | Operational question                                                         | Epistemic product                                                                        | Examples                                                                                                             | Status in literature                                                                                                                         |
| --------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- |
| **Description / representation**              | _What structure does the target system have?_                                | accurate characterization of states, patterns, properties, relations                     | _What frequency and spatial extent do the gamma oscillations of the network have during visual stimulation?_         | Core aim; de Regt, model-representation literature                                                                                           |
| **Exploration**                               | _What happens in the system when these conditions vary?_                     | a phenomenon identified and characterized; new concepts, classifications or regularities | _Which collective patterns appear in the network as the ratio of excitation to inhibition varies?_                   | Recognized for experiments and models alike; Steinle, Franklin (exploratory experimentation)                                                 |
| **Prediction**                                | _Given specified conditions, what will occur?_                               | warranted expectation about unknown outcomes                                             | _How does gamma power change if the stimulus contrast doubles?_                                                      | Core aim; standard philosophy of science                                                                                                     |
| **Explanation**                               | _Why or how does this phenomenon occur?_                                     | identification of explanatory relations — causal, mechanistic, mathematical, etc.        | _Why does the network oscillate at gamma frequency rather than remain asynchronous?_                                 | Core aim; major explanation traditions                                                                                                       |
| **Modal knowledge**                           | _What is possible, impossible, necessary, or contingent?_                    | possibility /  impossibility / necessity claims                                          | _Can a network without inhibitory neurons oscillate at gamma frequency at all?_                                      | Legitimate epistemic aim, but better viewed as a *modal dimension of knowledge* than as a coordinate category with explanation or prediction |
| **Knowledge of theories / models themselves** | _What follows from this theory/model? How does it behave?_                   | consequences, regimes, limits, structural properties                                     | _Which dynamical regimes does the Wilson–Cowan model exhibit as the coupling strength varies?_                       | Recognized especially in exploratory and theoretical modelling                                                                               |

**Exploration versus Description**. Exploration differs from description by *what the question fixes*:

- A descriptive question names its *phenomenon* and asks for its *features*. 
- An exploratory question names only what to observe and what to vary, and the phenomenon itself is the product [steinle1997]. The [question then fixes a search space](phenomenon.md#^exploratory-phenomenon)  in place of a phenomenon.

**Understanding is not a coordinate aim.** Contemporary epistemology treats understanding as a further achievement, characterized by *grasping* explanatory, structural or modal relations rather than merely possessing a correct explanation: Kvanvig emphasizes grasp of explanatory and coherence relations and Grimm grasp of modal dependencies, while Khalifa and Strevens hold that understanding just is knowledge of an explanation. This framework does not settle that dispute, and it leaves understanding out of the table above for a reason independent of it. Understanding is sought *of* a product rather than *instead* of one: an inquiry seeks to understand a prediction, the behavior of a model or a modal result as readily as an explanation, so an aim that admits one value could not carry it without excluding every combination. What an inquiry demanding understanding fixes is that its account be followable and that the dependences it rests on be exposed, which is [intelligibility and structural transparency held constitutive](epistemic-pragmatic-virtues.md#^virtue-standing), on whatever aim it pursues. Those two virtues bear on the form in which an answer is presented, where every aim in the table bears on what the answer is about or must contain, and that is the difference the table would otherwise hide.

## Specifications each aim requires

An aim fixes what an answer must deliver, and thereby which specifications the inquiry cannot leave open. The rows below add to what every inquiry fixes, and they also relax it: an aim that produces a phenomenon cannot be asked to state that phenomenon in advance. The third column therefore names the specifications a note marks required always and this aim admits open. An aim that neither adds nor relaxes is written with a dash; each dash rests on a filled inquiry that pursues that aim and fixes nothing beyond the general requirements. Each entry names a field path. [The requirement registry](../../src/gnomon/data/requirements.yml) owns the table, and the rows here document that registry. ^required-by-aim

| Aim | Additionally required | Admitted open, although required in general |
| --- | --- | --- |
| `description` | — | — |
| `exploration` | `phenomenon.detection_criterion` | `phenomenon.statement`, `phenomenon.category`, `phenomenon.evidential_status` |
| `prediction` | `phenomenon.manifestations`, `question.task.required_accuracy.outputs_to_match` | — |
| `explanation` | `question.subject.contrast.foil_set`, `question.task.requested_relation` | — |
| `modal-knowledge` | `question.task.modal_strength`, `question.task.proof_obligations` | — |
| `model-knowledge` | — | — |

- **Exploration is the aim that fixes no phenomenon, so it must fix what would establish one.** The statement, the category, the evidential status and the form of the manifestation stay open, although every other aim fixes them, and the detection criterion carries the test a candidate pattern has to pass. A general requirement and an aim therefore meet: the first states what a complete record carries, and the second states where an incomplete one is correct.

- **Prediction is the only aim that always compares an output against a measurement**, so it is the one that always requires outputs to match. An aim seeking a proof requires none, and leaving the accuracy absent is then correct rather than incomplete.

---
## Sources

Marks: ✓ the text itself was read · ◐ checked through an abstract, the publisher page or a secondary summary · ○ cited from standard knowledge, not fetched.

- [steinle1997] ◐ [Steinle, "Entering new fields: exploratory uses of experimentation", *Philosophy of Science* 64, S65–S74, 1997](https://philpapers.org/rec/STEENF)
