---
tags:
  - theory
index: "[Subject of inquiry](docs/epistemology/subject/_index.md)"
aliases:
  - Phenomenon (subject of inquiry)
---
# Phenomenon

> [!QUESTION] Goal: what must be fixed to specify the phenomenon that an inquiry is about?

The phenomenon is the second component of the [subject of inquiry](subject-of-inquiry.md): the behavior of the target system that the question concerns. The record also owns the estimator of its explanandum variables, from which their estimates are computed, and declares what its data depend on, so that a model can be compared with it through a [binding](../../specification/binding.md#^binding-record).

> [!WARNING] Phenomena are features inferred from data, but they are distinct from the data [bogen1988].

The fields of the record are documented in the [phenomenon record](../../specification/phenomenon.md).

- **The explanandum variables restate the behavior in terms of the system's state.** Their possible values matter because an explanation answers counterfactual ("what-if-things-had-been-different") questions. Such a question asks for the changes that would have given $Y$ another value [woodward2003]. The same values also supply the default foils of the contrast $X$.

- **The value set fixes which comparisons between values are meaningful**, and hence which dependence claims are available to an answer. An enumeration supports no more than identity. An interval of the reals also carries magnitudes. A `maps` or `measures` expression carries the structure of the objects that it builds. *Example*: values in `enum("low", "high")` support "the stronger the input, the higher $Y$" only once the enumeration is ordered [stevens1946]. The same set also fixes the grain of the values: `enum("oscillating", "silent")` is coarser than an interval of frequencies.

> [!NOTE] Behavior and manifestation
> The name "behavior" is kept for the occurrent itself: the activity or process [kaiser2017]. A manifestation is a feature of the occurrent, such as its frequency, amplitude or spatial extent [craver2013].

- **The course and the occurrence class state how the behavior unfolds.** The three [occurrence classes](../definitions/change/process-event-history.md#^state-class) differ in the segments on which they hold. A state holds at every point of a segment. A process holds on every sub-segment longer than the grain. An event holds of a segment and of none of its parts. A predicate in none of the three classes, such as "the mean rate over the window exceeds 5 Hz", enters the record as an [observable over a declared window](../definitions/change/process-event-history.md#^window-observable). ^course-and-occurrence

- **The category fixes the admitted occurrence classes of a phenomenon.** A particular occurrence is one token of a state, a process or an event. A regularity relates occurrences without being one, and a capacity is a [disposition](../definitions/regularities/capacity-and-disposition.md), so neither takes an occurrence class. A structural property holds at each point of the course, as a state does.

- **The category narrows the [requested relation](../epistemic-task/requested-relation.md) $R$.** *Examples*: in psychology, capacities are explained by functional analysis. Effects, by contrast, are regularities that themselves require explanation [cummins2000].

- **The option "Structural property" is not standard.** An account of phenomena as occurrents excludes structural properties, unless each is restated as the outcome of a process [kaiser2017]. *Example*: the "low dimensionality of a learned representation" is a structural property. Restated as the outcome of a process, the phenomenon reads "training produces a low-dimensional representation". The restatement matters because this version admits mechanistic and dynamical answers.

- **A qualitative phenomenon may later become a quantitative one.** A manifestation of the form *value*, whose value is a label such as "synchronous", serves as long as the phenomenon has been neither operationalized nor characterized in detail. Once more data are gathered or the analysis is refined, the manifestation may gain *features* that parametrize it. These features then provide new variables to relate quantitatively to the conditions. *Example*: "oscillations" may first serve as a qualitative label, and later be parametrized by a phase, an amplitude and other features.

- **Conditions and byproducts form a closed list of five standard kinds** [craver2013], each stated in its own row of the specification table. A background factor that the question varies leaves the domain $D$, because the [domain test](domain.md#^domain-test) holds every quantity in $D$ equal between fact and foil. The place of such a factor in the record then depends on how the question varies it and on the form of the claim. A factor that the question sweeps becomes an index of an observable when the claim is a function of the swept values. The same factor becomes a source of variation across instances when the claim is a distribution over its draws. A factor whose two values the question opposes becomes a foil of the contrast $X$. A factor enters the record as a modulating condition only once its effect is *established*. ^conditions-byproducts

- **Granularity must be specified as a property of the phenomenon.** Proportionality requires cause and effect to be described without irrelevant detail [woodward2010]. The grain at which a phenomenon is described therefore sets the grain at which a matching explanans is sought by default. ^resolution-proportionality

- **The signature and the scope are specified independently.** The states recorded for a phenomenon form an array indexed by constituents $i$, by the course $t$ and by instances $k$. Each of these three families holds as many indices as the observable takes. Of these, the signature holds the indices that the observable itself carries, whereas the scope over instances sets the extent of the claim over the reference class. *Example*: two statements of the same oscillation differ in both the signature and the scope:

    - "the network oscillates": the mean rate over the excitatory neurons, summarized over the trial, so the signature is empty and the scope is one typical instance;
    - "the spike phase of each neuron over time, across network initializations": the signature holds the constituent and the time, and the scope is a distribution over instances.

- **An index is declared only for a dimension that takes several values:**

    - a constituent kind, for a bearer with many units;
    - the course, for a behavior that unfolds in time or along a parameter;
    - a source of variation, for a reference class or for repeated realizations.

    The restriction matters because each declared index changes the admissible answers. *Examples*: a correlation computed over aggregates can differ from its value over individuals [robinson1950]. The result can also depend on the order of the averaging over instances relative to the analysis: the quenched and annealed computations differ [mezard1987].

- **A censored event is not a large value.** Within a finite observation window, either the event occurs and its time is recorded, or only the horizon is known. A single number pooling an event time with a horizon represents neither. The record therefore states the horizon and the censoring beside the observable, not inside its value. ^censoring-is-not-a-value

- **The evidential status carries the presupposition of a question.** The reason is that a why-question presupposes that its topic is true [vanfraassen1980]. If a phenomenon is only predicted, then either the question is conditional or the [epistemic aim is detection](../epistemic-task/epistemic-aim.md). For instance, the question of characterizing "memory transfer" was abandoned once the phenomenon was rejected [colaco2018].

- **An object of research may admit several phenomena** when the [epistemic aim is a description](../epistemic-task/epistemic-aim.md). Experimental work often targets an "object of research", such as a memory system. Several phenomena then serve both as components of that object and as evidence for it [feest2017].

- **A phenomenon owns the estimator of its explanandum variables.** The values of an explanandum variable are inferred from the data, and a measurement outcome is itself inferred through a model [tal2013]. The phenomenon therefore states the estimator, the version of the data and the uncertainty of each estimated variable. The estimates are computed from these entries, as a [comparison](../answer/model-and-binding.md#^comparison-recomputed) is, and never recorded by hand. A descriptive answer whose route is an estimation on the target cites the computed estimate as its claim, with the estimator and the version of the data among its grounds. A [comparison](../answer/model-and-binding.md#^comparison) of a model with the phenomenon reads these estimates when its binding targets the phenomenon. When the binding targets the data instead, the comparison reads the version of the data through an observation operator. In both cases, no answer estimates the explanandum variables a second time. In an exploratory inquiry, the phenomenon record holds the candidate observables and their estimator, as for any phenomenon, and the answer holds the content that the estimates do not fix: the partition of the explored space into classes, and the pattern of each class. ^phenomenon-owns-estimation

- **A phenomenon declares what its data depend on.** Data models can contain the models under test, and a data model is adequate for some purposes and not for others [bokulichparker2021]. The phenomenon therefore declares four facts about its data, so that a comparison can detect circularity and the warrant test of [phenomenon established](../answer/satisfaction-conditions.md) can read the adequacy of the data: ^data-model-declarations
    - the models of its data model, each with its kind: instrument model, background simulation, assimilation model or reconstruction [parker2017];
    - its observation error, which the data own, whereas the structural discrepancy belongs to the binding and the tolerance to the question, as the [owners of the discrepancy](../answer/model-and-binding.md#^discrepancy-owners) state;
    - the selection of its pattern, with the question that motivated the selection, since a pattern selected for one question can be uninformative for another;
    - the purposes for which its data model is adequate.

    A comparison raises its flag of circularity when a declared model of the data model overlaps with the model or the grounds of the answer compared.

- **An exploratory question fixes a search space, and the inquiry produces the phenomenon.** Exploratory experimentation varies parameters systematically to find regularities and to form concepts, when no theory yet delimits the phenomenon [steinle1997]. This search is supported by instruments that measure many variables at once [franklin2005].

    *Example*: "in a recurrent network trained on a task that depends on a context cue, which patterns appear in the population activity as the strength of that cue varies?" ^exploratory-phenomenon

---
## Sources

Marks follow the [legend of reading marks](../../../CONTRIBUTING.md#^reading-marks).

- [bogen1988] ○ Bogen & Woodward, "Saving the phenomena", _Philosophical Review_ 97(3), 1988
- [bokulichparker2021] ◐ Bokulich & Parker, "Data models, representation and adequacy-for-purpose", *European Journal for Philosophy of Science* 11, 31, 2021
- [colaco2018] ◐ [Colaço, "Rip it up and start again", _SHPS A_ 72, 2018](https://www.sciencedirect.com/science/article/abs/pii/S003936811730211X)
- [craver2013] ◐ [Craver & Darden, _In Search of Mechanisms_, U. Chicago Press, 2013](https://press.uchicago.edu/ucp/books/book/chicago/I/bo16123713.html)
- [cummins2000] ✓ [Cummins, "How does it work?" versus "What are the laws?", in _Explanation and Cognition_, MIT Press, 2000](https://direct.mit.edu/books/edited-volume/4894/chapter/623167/How-Does-It-Work-versus-What-Are-the-Laws-Two)
- [feest2017] ◐ [Feest, "Phenomena and objects of research…", _Philosophy of Science_ 84(5), 2017](https://philarchive.org/rec/FEEPAO)
- [franklin2005] ◐ [Franklin, "Exploratory experiments", _Philosophy of Science_ 72(5), 2005](https://philpapers.org/rec/FRAEE)
- [kaiser2017] ◐ [Kaiser & Krickel, "The metaphysics of constitutive mechanistic phenomena", _BJPS_ 68(3), 2017](https://academic.oup.com/bjps/article/68/3/745/2669661)
- [mezard1987] ◐ Mézard, Parisi & Virasoro, _Spin Glass Theory and Beyond_, World Scientific, 1987, quenched versus annealed averages
- [parker2017] ◐ Parker, "Computer simulation, measurement, and data assimilation", *British Journal for the Philosophy of Science* 68(1), 273–304, 2017
- [robinson1950] ◐ [Robinson, "Ecological correlations and the behavior of individuals", _American Sociological Review_ 15(3), 1950](https://en.wikipedia.org/wiki/Ecological_correlation)
- [steinle1997] ◐ [Steinle, "Entering new fields: exploratory uses of experimentation", _Philosophy of Science_ 64, S65–S74, 1997](https://philpapers.org/rec/STEENF)
- [stevens1946] ◐ Stevens, "On the theory of scales of measurement", _Science_ 103, 1946, via [Wikipedia, Level of measurement](https://en.wikipedia.org/wiki/Level_of_measurement)
- [tal2013] ◐ Tal, "Old and new problems in philosophy of measurement", *Philosophy Compass* 8(12), 1159–1173, 2013
- [vanfraassen1980] ✓ van Fraassen, _The Scientific Image_, ch. 5, with [the chapter text](https://www.fitelson.org/290/vanfraassen_pte.pdf)
- [woodward2003] ○ [Woodward, _Making Things Happen_, OUP, 2003](https://academic.oup.com/book/4324)
- [woodward2010] ◐ [Woodward, "Causation in biology…", _Biology & Philosophy_ 25, 2010](https://link.springer.com/article/10.1007/s10539-010-9200-z)
