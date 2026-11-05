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

> [!QUESTION] Goal: which activities design the plans that an inquiry executes, obtain data and phenomena from its target, and by which norm is each judged?

The activities of this family output a [design](../../../specification/design.md), [data](../../vocabulary/quantities/variable-value-observable.md) or a [phenomenon](../../vocabulary/regularities/pattern-and-phenomenon.md). Each activity of this family is typed by its [signature](epistemic-activities.md#^activity-criterion).

## Signatures

| Activity | Inputs | Output | Mode | Context |
| --- | --- | --- | --- | --- |
| `experimental-design` | `question`, `model` | `design` | deductive | justification |
| `method-design` | `question`, `model` (optional) | `design` | deductive | both |
| `scheme-design` | `question`, `model` (optional) | `design` | deductive | both |
| `observation` | `design` | `data` | model-based | justification |
| `measurement` | `measurement-procedure`, `design` | `data` | model-based | justification |
| `intervention` | `design` | `data` | non-inferential | justification |
| `phenomenon-detection` | `data` | `phenomenon` | inductive | justification |
| `phenomenon-specification` | `identified-subject`, `target-specification` | `phenomenon` | non-inferential | discovery |
| `phenomenon-derivation` | `consequence`, `target-specification` | `phenomenon` | non-inferential | discovery |

- **Observation and measurement are model-based inferences.** Each infers an outcome from the output of an instrument through a model of that instrument and of its interaction with the target [tal2013]. The method commits to this account of access in its [stance on mediated access](../../foundations/existence-and-access.md#^mediated-access), and extends it from measurement to observation through an instrument. Their mode is therefore `model-based`. ^model-based-modes

## Norms

| Activity | Operation | The norm passes when |
| --- | --- | --- |
| `experimental-design` | fix the protocol of an experiment or of a simulation run (e.g. conditions, interventions, controls, sample) before any data are recorded | the possible outcomes discriminate the rival answers to the question: each rival predicts a different outcome, so the design would probably detect an error in any false rival [fisher1935] [mayo1996] [mayo2018] |
| `method-design` | fix a method that solves the task of a question: its inputs, its steps, its rules and its condition of stopping | on every admissible input, an execution stops after finitely many steps, each step is defined precisely enough to be executed, and the output achieves the task [knuth1997] |
| `scheme-design` | fix a reusable way of deriving, such as a proof technique: its conditions of application, its steps and posits, its effect and its modes of failure, as a design of kind `method` | under its conditions of application, each step is licensed by a warrant and the steps yield the stated effect, and each mode of failure names the situation that announces it and the patch that it calls for [bundy2002] |
| `observation` | register features of the target through an instrument, or assemble existing recordings of it | the instrument is reliable, as shown independently of the claim under test [hacking1983] |
| `measurement` | assign values to a property by a map that preserves its empirical relations | a representation theorem guarantees that the map exists, a uniqueness theorem fixes its admissible transformations, and the scale type is stated [krantz1971]; the outcome is inferred from the reading through a stated model of the measuring process [tal2013] |
| `intervention` | set a variable of the target, and record the response | the intervention changes the response only through the manipulated variable, and is independent of the other causes of the response [woodward2003] [hacking1983] |
| `phenomenon-detection` | infer from data a behavior of the target, robust across procedures, or its absence from a closed search | the feature is stable across independent procedures, replications included, and confounders and artefacts are controlled; an absence is inferred only from a search whose procedures would probably have detected the feature within its stated scope [bogen1988] [woodward1989] [mayo1996] |
| `phenomenon-specification` | raise an identified phenomenon to commitment `specified`: state its observables, its manifestations and its course over the declared quantities of the target | each observable is an expression over the declared quantities of the target, and the manifestations restate the identified behavior [craver2013] |
| `phenomenon-derivation` | state a derived consequence as a phenomenon of the target, whose evidential status is derived or predicted | the phenomenon restates the consequence over observables of the target, and its evidential status is derived or predicted |

## Distinctions

- **Measurement is an empirical activity, distinct from a measure in the sense of measure theory.** A measurement assigns numbers to a property of the target by a map that preserves its empirical relations, and the representational theory of measurement states when such a map exists and how unique it is [krantz1971]. A measure, in measure theory, is a countably additive function on the subsets of a set, an object of mathematics that the operator `measures` builds in an expression. The records reserve the noun "measure" for the second sense, and name the first by "measurement" or, for a function that compares values, by "metric". ^measurement-and-measure

- **Detection, specification and derivation of a phenomenon differ in their source.** Detection infers a phenomenon from data. Specification states a phenomenon already identified over the declared quantities of the target, so that the questions about it become definite; the mechanistic sciences characterize a phenomenon in this way before they build a schema of its mechanism [craver2013]. Derivation states as a phenomenon a consequence of a model or of the admitted laws, whose evidential status is then derived or predicted, and which a later detection may establish. ^phenomenon-sources

- **Design and execution differ in their output.** Experimental design outputs a design, judged before any datum exists by its possible outcomes. Observation, measurement and intervention execute a design, and output data.
- **Method design and scheme design differ in their norm.** Both output a design of kind `method`. A method is executed, so its norm requires that every execution stops and achieves the task [knuth1997]. A [scheme of derivation](../../objects/derivation/segment-and-scheme.md) is applied by the segments of derivations. Therefore, its norm requires that its conditions of application license its steps and yield its effect, as the methods of proof planning state their preconditions and their effects [bundy2002].
- **Experimental design and method design differ in their task.** An experimental design obtains data that discriminate the rival answers to a question. A method obtains the answer itself, by computation or by construction, such as an algorithm that enumerates the fixed points of a network. A method that runs on a model is executed by [simulation](model-analysis.md), which takes a model and a design. Each activity outputs its own kinds of design: `experimental-design` the kinds `experiment` and `simulation-run`, and `method-design` the kind `method`. The [partition by output type](epistemic-activities.md#^families) files method design in this family, since its output is a design, although its execution need not reach the target.
- **Observation and measurement differ in their requirements.** Observation produces records of features. Such records may be categorical, with no numerical representation, and they rest on a model of the instrument only. Measurement requires, in addition, a [scale](../../vocabulary/quantities/scale-and-level.md), and its model covers the whole measuring process [tal2020].
- **The norm of measurement combines two accounts.** The representational account states the conditions under which a scale exists: a map that preserves the empirical relations of a property, its admissible transformations, and its type [krantz1971]. The model-based account adds that an outcome is inferred from a reading through a model of the instrument and of its interaction with the object [tal2013]. The method commits to the model-based account in its stance on [access](../../foundations/existence-and-access.md). The norm requires both parts: the representational part fixes what a value means on its scale, and the model-based part fixes which quantity a reading measures.
- **Observation and intervention differ by manipulation.** An intervention sets a variable, whereas observation records the target as it is [hacking1983]. Therefore, an intervention can support a causal claim under fewer assumptions about confounders than observation requires.
- **Phenomenon detection is an inference.** The data of one procedure carry its idiosyncrasies, so a phenomenon is typically detected by comparing data across procedures [bogen1988]. The robustness that detection requires holds across procedures, not across time: only a phenomenon of the category *regularity* must recur, and a phenomenon can occur once, as the note on [phenomena](../../vocabulary/regularities/pattern-and-phenomenon.md) states.

## Relations to the method

- **The evidential status of a phenomenon records the outcome of detection.** A phenomenon may have the evidential status `established`, across data sets or methods; `reported`, once; `predicted`; or `derived`, within a model. The status therefore separates a phenomenon that detection has reached from one that a theory only predicts, independently of any account that explains it.
- **A law with the role *measurement* states the observation map of an instrument.** The law relates the reading of the instrument to a quantity of the target, so a measurement outcome is inferred through that law, as the model-based part of the norm of measurement requires.
- **A clamped variable among the conditions held fixed records an intervention.** A [clamped state variable](../../objects/subject/domain.md) is removed from the dynamics and treated as an input, just as an intervention replaces the equation of its target variable.

The fields that record the outcome of detection and the observation map of an instrument are documented in the [phenomenon record](../../../specification/phenomenon.md) and in the [background record](../../../specification/background.md).

---
## Sources

Marks follow the [legend of reading marks](../../../../CONTRIBUTING.md#^reading-marks).

- [bogen1988] ◐ [Bogen & Woodward, "Saving the phenomena", *Philosophical Review* 97(3), 303–352, 1988](https://doi.org/10.2307/2185445)
- [bundy2002] ◐ [Bundy, "A critique of proof planning", in Kakas & Sadri (eds.), *Computational Logic: Logic Programming and Beyond*, Part II, LNAI 2408, Springer, 160–177, 2002](https://doi.org/10.1007/3-540-45632-5_7); methods with preconditions and effects, and proof critics, §1.1, read on the [author's copy](https://www.inf.ed.ac.uk/publications/online/1311.pdf)
- [craver2013] ◐ [Craver & Darden, *In Search of Mechanisms: Discoveries across the Life Sciences*, University of Chicago Press, 2013](https://press.uchicago.edu/ucp/books/book/chicago/I/bo16123713.html); the features of a manifestation and the five kinds of conditions and byproducts cited from standard knowledge
- [fisher1935] ◐ [Fisher, *The Design of Experiments*, Oliver and Boyd, 1935](https://en.wikipedia.org/wiki/The_Design_of_Experiments); randomization, replication and blocking as principles of design, checked through secondary summaries
- [hacking1983] ◐ [Hacking, *Representing and Intervening: Introductory Topics in the Philosophy of Natural Science*, Cambridge University Press, 1983](https://doi.org/10.1017/CBO9780511814563)
- [knuth1997] ○ Knuth, *The Art of Computer Programming*, vol. 1, *Fundamental Algorithms*, 3rd ed., Addison-Wesley, 1997, §1.1; the finiteness, the definiteness, the inputs, the outputs and the effectiveness of an algorithm
- [krantz1971] ◐ [Krantz, Luce, Suppes & Tversky, *Foundations of Measurement*, vol. I, *Additive and Polynomial Representations*, Academic Press, 1971](https://shop.elsevier.com/books/additive-and-polynomial-representations/krantz/978-0-12-425401-5)
- [mayo1996] ◐ [Mayo, *Error and the Growth of Experimental Knowledge*, University of Chicago Press, 1996](https://www.press.uchicago.edu/ucp/books/book/chicago/E/bo3637756.html)
- [mayo2018] ◐ [Mayo, *Statistical Inference as Severe Testing: How to Get beyond the Statistics Wars*, Cambridge University Press, 2018](https://doi.org/10.1017/9781107286184)
- [tal2013] ◐ [Tal, "Old and new problems in philosophy of measurement", *Philosophy Compass* 8(12), 1159–1173, 2013](https://doi.org/10.1111/phc3.12089); a measurement outcome is inferred through a model of the measuring process
- [tal2020] ◐ [Tal, "Measurement in science", *Stanford Encyclopedia of Philosophy*, substantive revision 7 August 2020](https://plato.stanford.edu/entries/measurement-science/); §7, model-based accounts
- [woodward1989] ◐ [Woodward, "Data and phenomena", *Synthese* 79(3), 393–472, 1989](https://doi.org/10.1007/BF00869282)
- [woodward2003] ◐ [Woodward, *Making Things Happen: A Theory of Causal Explanation*, Oxford University Press, 2003](https://doi.org/10.1093/0195155270.001.0001)
