---
tags:
  - specification
index: "[Specification](docs/specification/_index.md)"
aliases:
  - Phenomenon record
  - Specifying the phenomenon
---
# Phenomenon record

> [!QUESTION] Goal: what does a researcher write in each field of a phenomenon record?

The grounds of these fields are stated in the note on the [phenomenon](../epistemology/objects/subject/phenomenon.md).

The phenomenon is stated once in words and once formally, by the observables and the manifestations. The statement in words follows one frame:

> [bearer: noun phrase] | [behavior: verb phrase] | [conditions: clause]

*Example*: "the excitatory population | oscillates at gamma frequency | when a visual stimulus is presented (precipitating condition)".

| Specification | When it is required | Options or frame | Examples | Source |
| ------------- | ------------------- | ---------------- | -------- | ------ |
| Statement | from `identified` | "[bearer of the phenomenon] [its behavior]", as a reading | "the excitatory population oscillates at gamma frequency" | [kaiser2017], "object-involving occurrent"; [craver2007], "$S$'s $\psi$-ing" |
| Commitment — how far the record fixes the phenomenon | always | `identified`: a definite description and pointers fix the referent · `specified`: the observables and the manifestations are written, and their symbols resolve | the geometry of the fixed points of the benchmark networks, named before any kernel is written (identified); the same geometry stated by a kernel over the inputs (specified) | [levels of commitment](../epistemology/objects/question/question.md#^commitment-levels) |
| Identification — what fixes the referent before any observable is declared | from `identified` | a definite description of the behavior, with pointers to the data, the results or the publications that report it | the delay between fitting and generalization reported for networks trained on algorithmic tasks | reference fixing [kripke1980] |
| Identification: description | with the identification | a noun phrase that picks out one behavior of the target | the stationary localized states of the equation, with the branches that organize them | [kripke1980] |
| Identification: pointers | with the identification | per pointer, a data set, a result or a publication | the article that reports the phenomenon; a figure of a simulation study | — |
| Category | from `specified` | particular occurrence · regularity (effect) · capacity · structural property | the burst recorded at $t=12$ s (particular occurrence); gamma power increases with stimulus contrast (regularity); gating inputs by context (capacity); a low-dimensional representation (structural property) | [hempel1948]; [cummins2000] |
| Course — the ordered index along which the behavior unfolds | from `specified` | an index, a grain and the parameters of the target that vary along the course | the training steps of a network; the time of a flow; a stimulus parameter swept by the question | [course of a history](../epistemology/vocabulary/change/process-event-history.md#^course) |
| Course: index | with the course | the symbol of an index set of the target or of this record: time, a training step, or an input parameter | the training step; the time | [course of a history](../epistemology/vocabulary/change/process-event-history.md#^course) |
| Course: grain | with the course | an expression giving the shortest segment on which a predicate of the behavior is evaluated | one training step; one turnover time of the largest eddies | [process predicates](../epistemology/vocabulary/change/process-event-history.md#^process) |
| Course: varies | when a parameter of the target changes along this course | the symbols of those parameters | the weights of a network along training | [role test](../epistemology/vocabulary/quantities/variable-value-observable.md#^role-test) |
| Occurrence — the class of the occurrences that the phenomenon concerns | from `specified` | state · process · event · not-applicable, for a capacity | the network sits at its fixed point (state); the turbulent flow (process); the first crossing of a loss threshold (event) | [mourelatos1978] |
| Index sets | when an observable is indexed by a set that the target system does not declare | "[symbol]", with the set expression that it collects and its structure: continuum · discrete set · interval | the separation and the lag of a correlation; the order of a structure function; a prediction horizon | — |
| Explanandum variables | whenever the contrast takes its foils from the values of the variable, or the answer must be tested against measurements | a reference to a quantity that the target declares, or "[symbol] ∈ [set expression]" with a reading naming it in words | $Y$ = the regime of the population activity, with values "asynchronous" and "synchronous" | [woodward2003] |
| Explanandum variables: signature (indices $i$ and $t$) | when the observable takes at least one index | the free indices of the definition: a constituent kind, an index set, time, a parameter, or a new index that it introduces | the spike phase of each neuron over time (two indices); a correlation over separation and lag (two indices); a stationary rate (none) | — |
| Explanandum variables: scale | when the values of the observable are measured | nominal · ordinal · interval · ratio · absolute · not-applicable | a regime label (nominal); a delay counted in training steps (ratio) | levels of measurement [stevens1946] |
| Explanandum variables: expression | when the observable is derived from the state variables | "[expression over declared symbols]", whose binders consume the indices that it aggregates | the mean of the constituent rates; the minimum abundance $\min_i N_i$; the delay $t_{gen}-t_{fit}$ | — |
| Explanandum variables: event | when the observable is the time of an event | the origin from which the clock starts, the horizon at which observation stops, and the censoring (right · left · interval · none) for an event whose time is unknown | a generalization event observed up to a finite training horizon, right-censored when the criterion is never met | survival analysis, censoring [ich2019] |
| Explanandum variables: estimator | when the values of the observable are estimated from data | the estimator that computes the values from the data, the version of the data on which it runs, and the uncertainty that it reports; the estimates themselves are computed from these entries, not recorded | the peak of the power spectrum, estimated by Welch's method on version 3 of the recordings, with a bootstrap interval | the [estimation owned by the phenomenon](../epistemology/objects/subject/phenomenon.md#^phenomenon-owns-estimation) |
| Manifestations | from `specified` | per form, "[expression over the explanandum variables]" with its form: value · dependence · functional form · scaling · relation | $Y$ is "synchronous" (value); gamma power increases with contrast (dependence); $m(t)=A\sin(2\pi f t+\varphi)$ (functional form); $S_p(r)\sim r^{\zeta_p}$ (scaling); feasibility implies local stability (relation) | [hempel1948]; [woodward2003] |
| Manifestations: features | when the form carries quantities that characterize the behavior | per feature, "[symbol] ∈ [set expression]" with the value observed within that set | the amplitude, the frequency and the phase of an oscillation; the exponents of a scaling law | [craver2013] |
| Scope over instances (index $k$) — an instance is a member of the reference class of $S$, or one realization of a system (a trial, a random initialization, a disorder sample) | when the question ranges over a reference class or over repeated realizations | per source of variation, the declared quantities that it varies and the other sources held fixed meanwhile. Each entry also records its source: class member · realization · parameter draw · structure draw · scenario. It records its quantification as well: single instance · typical instance · ensemble summary · ensemble distribution · universal, meaning every member of the admitted class | the initialization draw, conditional on a fixed training specification (ensemble distribution); every model of the admitted class (universal) | [lundberg2021]; [ich2019] |
| Conditions and byproducts: precipitating conditions | when a condition must hold for the behavior to occur | per condition, an expression over declared symbols with a justification | a visual stimulus is presented | [craver2013] |
| Conditions and byproducts: inhibiting conditions | when a condition is known to prevent the behavior | per condition, an expression over declared symbols with a justification | feedforward inhibition is raised past the threshold that suppresses the oscillation | [craver2013] |
| Conditions and byproducts: modulating conditions | when a condition changes a feature of the behavior without preventing it | per condition, the relation that it induces, as an expression naming the affected feature and the controlling quantity. An entry names the regime when the relation holds only there. Each condition carries a reading | a higher stimulus contrast increases the gamma power and shifts its peak frequency upward | [craver2013] |
| Conditions and byproducts: nonstandard circumstances | when the behavior is obtained only under unusual circumstances | per circumstance, an expression over declared symbols, with a justification. The justification names the unusual feature and the procedure that produces the circumstance | a slice preparation under carbachol | [craver2013] |
| Conditions and byproducts: byproducts | when the behavior has further effects outside the phenomenon | per byproduct, an expression over declared symbols with a justification that gives the reason for excluding it from the phenomenon | the metabolic cost of the sustained spiking | [craver2013] |
| Evidential status | from `specified` | established across data sets or methods · reported · predicted · derived within a model | gamma oscillations in V1, recorded across laboratories (established); a transition to chaos in mean-field theory (predicted); the stationary rate of a balanced network (derived) | [bogen1988]; [colaco2018] |
| Detection criterion | when the phenomenon is the product of the inquiry, or its status is weaker than established | per test, the condition that a candidate pattern must satisfy to count as established. The test also names the sources of variation across which the pattern must hold, and the external systems of the target that bound its conclusions | a pattern counts as established when it recurs across instances and across recording methods | [bogen1988]; [exploratory questions](../epistemology/objects/subject/phenomenon.md#^exploratory-phenomenon) |
| Data | when the status rests on recorded or derived material | per entry, "[pointer to a data set, a recording or a derivation]" that establishes the phenomenon, with its version | a recording session, version 3; a published figure; the derivation of a stationary rate | [bogen1988]; [colaco2018] |
| Data model — the models through which the data are produced or processed before they establish the phenomenon | when a model intervenes between the raw records and the data | per model, its kind: instrument model · background simulation · assimilation model · reconstruction, and the model record or the publication that states it | the forward model of the electrodes (instrument model); the reanalysis that fills the gaps of a temperature record (assimilation model) | [bokulichparker2021]; [parker2017] |
| Observation error | when the values of the explanandum variables are compared with an answer | per explanandum variable or per data set, an error model: a distribution or a bound | a Gaussian error of 2 Hz on the peak frequency | [kennedyohagan2001] |
| Pattern selection — how the pattern stated by the manifestations was selected from the data | when the data admit other patterns than the one stated | the selection procedure, the patterns set aside, and the question that motivated the selection | the gamma band selected among the bands of the spectrum, for the question of synchrony | [bokulichparker2021] |
| Adequacy — the purposes for which the data model is adequate | when the record declares a data model | per purpose, the question or the kind of use for which the data model is adequate, with its grounds | adequate for the peak frequency, not for the phase of single neurons | [bokulichparker2021] |

- **A record at commitment `identified` names a behavior before stating it formally.** The identification fixes which behavior the record is about, so a question can refer to it while its observables are still unwritten. The record reaches `specified` once its category, its course, its occurrence class, its manifestations and its evidential status are filled and its symbols resolve. ^phenomenon-commitment

- The [category of a phenomenon fixes its admitted occurrence classes](../epistemology/objects/subject/phenomenon.md). The checker reads the admitted classes from the [registry of requirements](../../src/gnomon/data/requirements.yml): ^occurrence-by-category

| Category | Admitted occurrence |
| --- | --- |
| `particular-occurrence` | `state`, `process`, `event` |
| `regularity` | `not-applicable` |
| `capacity` | `not-applicable` |
| `structural-property` | `state` |

- **A phenomenon of category `capacity` states its conditional and its criterion in its manifestations.** The manifestations name the class of inputs, the class of outputs and the criterion of performance, as the [definition of a capacity](../epistemology/vocabulary/regularities/capacity-and-disposition.md) requires. ^capacity-manifestations

- **An entry of a phenomenon holds of the members that carry its symbols.** When the members of a target system differ in their declarations, the record states [variants](target-system.md#^variants), each marking the entries carried by part of the class. A phenomenon declares no variants of its own: the members carrying a symbol are read from the record of its target system. Some entries of a phenomenon name a symbol carried by one variant only (e.g. an observable, a manifestation, a source of variation, a detection test or a condition). Such an entry names that variant and holds of it only. An entry left unmarked, by contrast, ranges over the whole class, including members for which its claim cannot be read. *Example*: the competitive-exclusion bound cannot be read of a community with direct interactions, because no resource pool limits its species. ^entries-hold-of-members

- **A claim that depends on the scale type of a variable requires the field `scale` of that variable.**

- An exploratory question has the same fields as any other question, but each of them takes a different status:

    - empty, since they form the answer: the statement, the category, the occurrence class and the evidential status;
    - required, filled with the candidate observables: explanandum variables, with their value sets and signatures;
    - required, filled with the varied factors and their ranges: conditions of $P$, since the [operational test](../epistemology/objects/subject/domain.md#^domain-test) excludes them from $D$;
    - required, stated as the detection criterion from which the evidential status follows: the condition that a candidate pattern must satisfy to count as established, such as stability across instances [bogen1988];
    - empty: the contrast $X$.

---
## Sources

Marks follow the [legend of reading marks](../../CONTRIBUTING.md#^reading-marks).

- [bogen1988] ◐ [Bogen & Woodward, "Saving the phenomena", *Philosophical Review* 97(3), 303–352, 1988](https://doi.org/10.2307/2185445)
- [bokulichparker2021] ◐ Bokulich & Parker, "Data models, representation and adequacy-for-purpose", *European Journal for Philosophy of Science* 11, 31, 2021
- [colaco2018] ◐ [Colaço, "Rip it up and start again", _SHPS A_ 72, 2018](https://www.sciencedirect.com/science/article/abs/pii/S003936811730211X)
- [craver2007] ◐ [Craver, *Explaining the Brain: Mechanisms and the Mosaic Unity of Neuroscience*, Oxford University Press, 2007](https://doi.org/10.1093/acprof:oso/9780199299317.001.0001)
- [craver2013] ◐ [Craver & Darden, *In Search of Mechanisms: Discoveries across the Life Sciences*, University of Chicago Press, 2013](https://press.uchicago.edu/ucp/books/book/chicago/I/bo16123713.html)
- [cummins2000] ✓ [Cummins, "How does it work?" versus "What are the laws?", in _Explanation and Cognition_, MIT Press, 2000](https://direct.mit.edu/books/edited-volume/4894/chapter/623167/How-Does-It-Work-versus-What-Are-the-Laws-Two)
- [hempel1948] ◐ [Hempel & Oppenheim, "Studies in the logic of explanation", *Philosophy of Science* 15(2), 135–175, 1948](https://doi.org/10.1086/286983)
- [ich2019] ◐ [ICH E9(R1) Addendum on Estimands](https://en.wikipedia.org/wiki/ICH_E9\(R1\)_Addendum_On_Estimands_and_Sensitivity_Analyses_in_Clinical_Trials)
- [kaiser2017] ◐ [Kaiser & Krickel, "The metaphysics of constitutive mechanistic phenomena", _BJPS_ 68(3), 2017](https://academic.oup.com/bjps/article/68/3/745/2669661)
- [kennedyohagan2001] ◐ [Kennedy & O'Hagan, "Bayesian calibration of computer models", *Journal of the Royal Statistical Society, Series B* 63(3), 425–464, 2001](https://doi.org/10.1111/1467-9868.00294)
- [kripke1980] ◐ Kripke, *Naming and Necessity*, Harvard University Press, 1980; pp. 54–57; reference fixing by a description, checked through secondary sources
- [lundberg2021] ✓ [Lundberg, Johnson & Stewart, "What is your estimand?", _ASR_ 86(3), 2021](https://journals.sagepub.com/doi/abs/10.1177/00031224211004187)
- [mourelatos1978] ◐ Mourelatos, "Events, processes, and states", _Linguistics and Philosophy_ 2(3), 415–434, 1978; the three classes of situations, checked through secondary sources
- [parker2017] ◐ Parker, "Computer simulation, measurement, and data assimilation", *British Journal for the Philosophy of Science* 68(1), 273–304, 2017
- [stevens1946] ◐ [Stevens, "On the theory of scales of measurement", *Science* 103(2684), 677–680, 1946](https://doi.org/10.1126/science.103.2684.677); via [Wikipedia, Level of measurement](https://en.wikipedia.org/wiki/Level_of_measurement)
- [woodward2003] ◐ [Woodward, *Making Things Happen: A Theory of Causal Explanation*, Oxford University Press, 2003](https://doi.org/10.1093/0195155270.001.0001)
