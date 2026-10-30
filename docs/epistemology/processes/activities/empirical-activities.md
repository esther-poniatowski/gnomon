---
tags:
  - theory
  - wip
index: "[Epistemic activities](docs/epistemology/processes/activities/_index.md)"
aliases:
  - Empirical activities
  - Experimental design
  - Observation and measurement
  - Experiment and intervention
  - Phenomenon detection
---
# Empirical activities

> [!QUESTION] Goal: which activities design an inquiry into a target and obtain data and phenomena from it, and by which norm is each judged?

The activities of this family output a design of inquiry, [data](../../vocabulary/quantities/variable-value-observable.md) or a [phenomenon](../../vocabulary/regularities/pattern-and-phenomenon.md). Each activity of this family is typed by its [signature](epistemic-activities.md#^activity-criterion).

## Signatures

| Activity | Inputs | Output | Mode | Context |
| --- | --- | --- | --- | --- |
| `experimental-design` | `question`, `model` | `design` | deductive | justification |
| `observation` | `design` | `data` | non-inferential | justification |
| `measurement` | `measurement-procedure`, `design` | `data` | non-inferential | justification |
| `intervention` | `design` | `data` | non-inferential | justification |
| `phenomenon-detection` | `data` | `phenomenon` | inductive | justification |

## Norms

| Activity | Operation | The test `norm.<activity-id>` passes when |
| --- | --- | --- |
| `experimental-design` | fix the protocol of an experiment or of a simulation run (e.g. conditions, interventions, controls, sample) before any data are recorded | the possible outcomes discriminate the rival answers to the question: each rival predicts a different outcome, so the design would probably detect an error in any false rival [fisher1935] [mayo1996] [mayo2018] |
| `observation` | register features of the target through an instrument, or assemble existing recordings of it | the instrument is reliable, as established independently of the claim under test [hacking1983] |
| `measurement` | assign values to a property by a map that preserves its empirical relations | a representation theorem guarantees that the map exists, a uniqueness theorem fixes its admissible transformations, and the scale type is stated [krantz1971] |
| `intervention` | set a variable of the target, and record the response | the intervention changes the response only through the manipulated variable, and is independent of the other causes of the response [woodward2003] [hacking1983] |
| `phenomenon-detection` | infer a stable feature of the target from data | the feature is stable across independent procedures, replications included, and confounders and artefacts are controlled [bogen1988] [woodward1989] |

## Distinctions

- **Design and execution differ in their output.** Experimental design outputs a design, judged before any datum exists by its possible outcomes. Observation, measurement and intervention execute a design, and output data.
- **Observation and measurement differ in their requirements.** Observation produces records of features. Such records may be categorical, with no numerical representation. Measurement requires a [scale](../../vocabulary/quantities/scale-and-level.md), and on the model-based account also a model of the measuring process [tal2020].
- **Observation and intervention differ by manipulation.** An intervention sets a variable, whereas observation records the target as it is [hacking1983]. Therefore, an intervention can support a causal claim under fewer assumptions about confounders than observation requires [woodward2003].
- **Phenomenon detection is an inference.** The data of one procedure carry its idiosyncrasies, so a phenomenon is typically detected by comparing data across procedures [bogen1988].

## Relations to the method

- **The evidential status of a phenomenon records the outcome of detection.** A phenomenon may be established across data sets or methods, reported once, predicted, or derived within a model, so the status separates a phenomenon that detection has reached from one that a theory only predicts, independently of any account that explains it.
- **A law with the role *measurement* states the observation map of an instrument.** The law relates the reading of the instrument to a quantity of the target, so a measurement outcome is inferred through that law, as the model-based account of measurement among the distinctions of this note holds.
- **A clamped variable in the domain records an intervention.** A [clamped state variable](../../objects/subject/domain.md) is removed from the dynamics and treated as an input, just as an intervention replaces the equation of its target variable.

The fields that record the outcome of detection and the observation map of an instrument are documented in the [phenomenon record](../../../specification/phenomenon.md) and in the [background record](../../../specification/background.md).

---
## Sources

Marks follow the [legend of reading marks](../../../../CONTRIBUTING.md#^reading-marks).

- [bogen1988] ◐ [Bogen & Woodward, "Saving the phenomena", *Philosophical Review* 97(3), 303–352, 1988](https://doi.org/10.2307/2185445)
- [fisher1935] ◐ [Fisher, *The Design of Experiments*, Oliver and Boyd, 1935](https://en.wikipedia.org/wiki/The_Design_of_Experiments); randomization, replication and blocking as principles of design, checked through secondary summaries
- [hacking1983] ◐ [Hacking, *Representing and Intervening: Introductory Topics in the Philosophy of Natural Science*, Cambridge University Press, 1983](https://doi.org/10.1017/CBO9780511814563)
- [krantz1971] ◐ [Krantz, Luce, Suppes & Tversky, *Foundations of Measurement*, vol. I, *Additive and Polynomial Representations*, Academic Press, 1971](https://shop.elsevier.com/books/additive-and-polynomial-representations/krantz/978-0-12-425401-5)
- [mayo1996] ◐ [Mayo, *Error and the Growth of Experimental Knowledge*, University of Chicago Press, 1996](https://www.press.uchicago.edu/ucp/books/book/chicago/E/bo3637756.html)
- [mayo2018] ◐ [Mayo, *Statistical Inference as Severe Testing: How to Get beyond the Statistics Wars*, Cambridge University Press, 2018](https://doi.org/10.1017/9781107286184)
- [tal2020] ◐ [Tal, "Measurement in science", *Stanford Encyclopedia of Philosophy*, substantive revision 7 August 2020](https://plato.stanford.edu/entries/measurement-science/); §7, model-based accounts
- [woodward1989] ◐ [Woodward, "Data and phenomena", *Synthese* 79(3), 393–472, 1989](https://doi.org/10.1007/BF00869282)
- [woodward2003] ◐ [Woodward, *Making Things Happen: A Theory of Causal Explanation*, Oxford University Press, 2003](https://doi.org/10.1093/0195155270.001.0001)
