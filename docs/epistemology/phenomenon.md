---
role: definition
status: stable
index: "[Epistemology](docs/epistemology/_index.md)"
aliases:
  - Specifying the phenomenon
  - Phenomenon (subject of inquiry)
tags: []
source:
---
# Specifying the phenomenon

> [!QUESTION] Goal: what must be fixed to specify the phenomenon that an inquiry is about?

The phenomenon is the second component of the [subject of inquiry](subject-of-inquiry.md): the behavior of the target system that the question concerns.

> [!WARNING] Phenomena are features inferred from data, but they are distinct from the data [bogen1988].

The phenomenon is stated once in words and once formally, by the observables and the manifestations. The statement in words follows one frame:

> [bearer: noun phrase] | [behavior: verb phrase] | [conditions: clause]

*Example*: "the excitatory population | oscillates at gamma frequency | when a visual stimulus is presented (precipitating condition)".

| Specification | When it is required | Options or frame | Examples | Source |
| ------------- | ------------------- | ---------------- | -------- | ------ |
| Statement | always | "[bearer of the phenomenon] [its behavior]", as a reading | "the excitatory population oscillates at gamma frequency" | [kaiser2017], "object-involving occurrent"; [craver2007], "$S$'s $\psi$-ing" |
| Category | always | particular event · regularity (effect) · capacity · structural property | the burst recorded at $t=12$ s (event); gamma power increases with stimulus contrast (regularity); gating inputs by context (capacity); a low-dimensional representation (structural property) | [hempel1948]; [cummins2000] |
| Index sets | when an observable is indexed by a set that the target system does not declare | "[symbol]", with the set expression that it collects and its structure: continuum · discrete set · interval | the separation and the lag of a correlation; the order of a structure function; a prediction horizon | — |
| Explanandum variables | whenever the contrast takes its foils from the values of the variable, or the answer must be tested against measurements | a reference to a quantity that the target declares, or "[symbol] ∈ [set expression]" with a reading naming it in words | $Y$ = the regime of the population activity, with values "asynchronous" and "synchronous" | [woodward2003] |
| Explanandum variables: signature (indices $i$ and $t$) | when the observable takes at least one index | the free indices of the definition: a constituent kind, an index set, time, a parameter, or a new index that it introduces | the spike phase of each neuron over time (two indices); a correlation over separation and lag (two indices); a stationary rate (none) | — |
| Explanandum variables: expression | when the observable is derived from the state variables | "[expression over declared symbols]", whose binders consume the indices that it aggregates | the mean of the constituent rates; the minimum abundance $\min_i N_i$; the delay $t_{gen}-t_{fit}$ | — |
| Explanandum variables: event | when the observable is the time of an event | the origin from which the clock starts, the horizon at which observation stops, and the censoring (right · left · interval · none) for an event whose time is unknown | a generalization event observed up to a finite training horizon, right-censored when the criterion is never met | survival analysis, censoring [ich2019] |
| Manifestations | always | per form, "[expression over the explanandum variables]" with its form: value · dependence · functional form · scaling · relation | $Y$ is "synchronous" (value); gamma power increases with contrast (dependence); $m(t)=A\sin(2\pi f t+\varphi)$ (functional form); $S_p(r)\sim r^{\zeta_p}$ (scaling); feasibility implies local stability (relation) | [hempel1948]; [woodward2003] |
| Manifestations: features | when the form carries quantities that characterize the behavior | per feature, "[symbol] ∈ [set expression]" with the value observed within that set | the amplitude, the frequency and the phase of an oscillation; the exponents of a scaling law | [craver2013] |
| Scope over instances (index $k$) — an instance is a member of the reference class of $S$, or one realization of a system (a trial, a random initialization, a disorder sample) | when the question ranges over a reference class or over repeated realizations | per source of variation, the declared quantities that it varies and the other sources held fixed meanwhile. Each entry also records its source: class member · realization · parameter draw · structure draw · scenario. It records its quantification as well: single instance · typical instance · ensemble summary · ensemble distribution · universal, meaning every member of the admitted class | the initialization draw, conditional on a fixed training specification (ensemble distribution); every model of the admitted class (universal) | [lundberg2021]; [ich2019] |
| Conditions and byproducts: precipitating conditions | when a condition must hold for the behavior to occur | per condition, an expression over declared symbols with a justification | a visual stimulus is presented | [craver2013] |
| Conditions and byproducts: inhibiting conditions | when a condition is known to prevent the behavior | per condition, an expression over declared symbols with a justification | feedforward inhibition is raised past the threshold that suppresses the oscillation | [craver2013] |
| Conditions and byproducts: modulating conditions | when a condition changes a feature of the behavior without preventing it | per condition, the relation that it induces, as an expression naming the affected feature and the controlling quantity. An entry names the regime when the relation holds only there. Each condition carries a reading | a higher stimulus contrast increases the gamma power and shifts its peak frequency upward | [craver2013] |
| Conditions and byproducts: nonstandard circumstances | when the behavior is obtained only under unusual circumstances | per circumstance, an expression over declared symbols, with a justification. The justification names the unusual feature and the procedure that produces the circumstance | a slice preparation under carbachol | [craver2013] |
| Conditions and byproducts: byproducts | when the behavior has further effects outside the phenomenon | per byproduct, an expression over declared symbols with a justification that gives the reason for excluding it from the phenomenon | the metabolic cost of the sustained spiking | [craver2013] |
| Evidential status | always | established across data sets or methods · reported · predicted · derived within a model | gamma oscillations in V1, recorded across laboratories (established); a transition to chaos in mean-field theory (predicted); the stationary rate of a balanced network (derived) | [bogen1988]; [colaco2018] |
| Detection criterion | when the phenomenon is the product of the inquiry, or its status is weaker than established | per test, the condition that a candidate pattern must satisfy to count as established. The test also names the sources of variation across which the pattern must hold, and the external systems of the target that bound its conclusions | a pattern counts as established when it recurs across instances and across recording methods | [bogen1988]; [exploratory questions](#^exploratory-phenomenon) |
| Data | when the status rests on recorded or derived material | per entry, "[pointer to a data set, a recording or a derivation]" that establishes the phenomenon | a recording session; a published figure; the derivation of a stationary rate | [bogen1988]; [colaco2018] |

- **The explanandum variables restate the behavior in terms of the system's state.** Their possible values matter because an explanation answers counterfactual ("what-if-things-had-been-different") questions. Such a question asks for the changes that would have given $Y$ another value [woodward2003]. The same values also supply the default foils of the contrast $X$.

- **The value set fixes which comparisons between values are meaningful**, and hence which dependence claims are available to an answer. An enumeration supports no more than identity. An interval of the reals also carries magnitudes. A `maps` or `measures` expression carries the structure of the objects that it builds. *Example*: values in `enum("low", "high")` support "the stronger the input, the higher $Y$" only once the enumeration is ordered [stevens1946]. The same set also fixes the grain of the values: `enum("oscillating", "silent")` is coarser than an interval of frequencies.

> [!NOTE] Behavior and manifestation
> The name "behavior" is kept for the occurrent itself: the activity or process [kaiser2017]. A manifestation is a feature of the occurrent, such as its frequency, amplitude or spatial extent [craver2013].

- **The category narrows the [requested relation](requested-relation.md) $R$.** *Examples*: in psychology, capacities are explained by functional analysis. Effects, by contrast, are regularities that themselves require explanation [cummins2000].

- **The option "Structural property" is not standard.** An account of phenomena as occurrents excludes structural properties, unless each is restated as the outcome of a process [kaiser2017]. *Example*: the "low dimensionality of a learned representation" is a structural property. Restated as the outcome of a process, the phenomenon reads "training produces a low-dimensional representation". The restatement matters because this version admits mechanistic and dynamical answers.

- **A qualitative phenomenon may later become a quantitative one.** A manifestation of the form *value*, whose value is a label such as "synchronous", serves as long as the phenomenon has been neither operationalized nor characterized in detail. Once more data are gathered or the analysis is refined, the manifestation may gain *features* that parametrize it. These features then provide new variables to relate quantitatively to the conditions. *Example*: "oscillations" may first serve as a qualitative label, and later be parametrized by a phase, an amplitude and other features.

- **An entry of a phenomenon holds of the members that carry its symbols.** When the members of a target system differ in their declarations, the record states [variants](target-system.md#^variants), each marking the entries carried by part of the class. A phenomenon declares no variants of its own: the members carrying a symbol are read from the record of its target system. Some entries of a phenomenon name a symbol carried by one variant only (e.g. an observable, a manifestation, a source of variation, a detection test or a condition). Such an entry names that variant and holds of it only. An entry left unmarked, by contrast, ranges over the whole class, including members for which its claim cannot be read. *Example*: the competitive-exclusion bound cannot be read of a community with direct interactions, because no resource pool limits its species. ^entries-hold-of-members

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

- **The evidential status carries the presupposition of a question.** The reason is that a why-question presupposes that its topic is true [vanfraassen1980]. If a phenomenon is only predicted, then either the question is conditional or the [epistemic aim is detection](epistemic-aim.md). For instance, the question of characterizing "memory transfer" was abandoned once the phenomenon was rejected [colaco2018].

- **An object of research may admit several phenomena** when the [epistemic aim is a description](epistemic-aim.md). Experimental work often targets an "object of research", such as a memory system. Several phenomena then serve both as components of that object and as evidence for it [feest2017].

- **An exploratory question leaves the phenomenon open and fixes a search space instead.** Exploratory experimentation varies parameters systematically to find regularities and to form concepts, when no theory yet delimits the phenomenon [steinle1997]. This search is supported by instruments that measure many variables at once [franklin2005]. An exploratory question has the same fields as any other question, but each of them takes a different status:

    - open, since they form the answer: bearer, behavior, category;
    - required, filled with the candidate observables: explanandum variables, with their value sets and signatures;
    - required, filled with the varied factors and their ranges: conditions of $P$, since the [operational test](domain.md#^domain-test) excludes them from $D$;
    - required, stated as the detection criterion: evidential status, namely the condition that a candidate pattern must satisfy to count as established, such as stability across instances [bogen1988];
    - empty: the contrast $X$.

    *Example*: "in a recurrent network trained on a task that depends on a context cue, which patterns appear in the population activity as the strength of that cue varies?" ^exploratory-phenomenon

---
## Sources

Marks follow the [legend of reading marks](../../CONTRIBUTING.md#^reading-marks).

- [bogen1988] ○ Bogen & Woodward, "Saving the phenomena", _Philosophical Review_ 97(3), 1988
- [colaco2018] ◐ [Colaço, "Rip it up and start again", _SHPS A_ 72, 2018](https://www.sciencedirect.com/science/article/abs/pii/S003936811730211X)
- [craver2007] ◐ [Craver, _Explaining the Brain_, OUP, 2007](https://philpapers.org/rec/CRAETB-2)
- [craver2013] ◐ [Craver & Darden, _In Search of Mechanisms_, U. Chicago Press, 2013](https://press.uchicago.edu/ucp/books/book/chicago/I/bo16123713.html)
- [cummins2000] ✓ [Cummins, "How does it work?" versus "What are the laws?", in _Explanation and Cognition_, MIT Press, 2000](https://direct.mit.edu/books/edited-volume/4894/chapter/623167/How-Does-It-Work-versus-What-Are-the-Laws-Two)
- [feest2017] ◐ [Feest, "Phenomena and objects of research…", _Philosophy of Science_ 84(5), 2017](https://philarchive.org/rec/FEEPAO)
- [franklin2005] ◐ [Franklin, "Exploratory experiments", _Philosophy of Science_ 72(5), 2005](https://philpapers.org/rec/FRAEE)
- [hempel1948] ○ Hempel & Oppenheim, "Studies in the logic of explanation", _Philosophy of Science_ 15(2), 1948
- [ich2019] ◐ [ICH E9(R1) Addendum on Estimands](https://en.wikipedia.org/wiki/ICH_E9\(R1\)_Addendum_On_Estimands_and_Sensitivity_Analyses_in_Clinical_Trials)
- [kaiser2017] ◐ [Kaiser & Krickel, "The metaphysics of constitutive mechanistic phenomena", _BJPS_ 68(3), 2017](https://academic.oup.com/bjps/article/68/3/745/2669661)
- [lundberg2021] ✓ [Lundberg, Johnson & Stewart, "What is your estimand?", _ASR_ 86(3), 2021](https://journals.sagepub.com/doi/abs/10.1177/00031224211004187)
- [mezard1987] ◐ Mézard, Parisi & Virasoro, _Spin Glass Theory and Beyond_, World Scientific, 1987, quenched versus annealed averages
- [robinson1950] ◐ [Robinson, "Ecological correlations and the behavior of individuals", _American Sociological Review_ 15(3), 1950](https://en.wikipedia.org/wiki/Ecological_correlation)
- [steinle1997] ◐ [Steinle, "Entering new fields: exploratory uses of experimentation", _Philosophy of Science_ 64, S65–S74, 1997](https://philpapers.org/rec/STEENF)
- [stevens1946] ◐ Stevens, "On the theory of scales of measurement", _Science_ 103, 1946, via [Wikipedia, Level of measurement](https://en.wikipedia.org/wiki/Level_of_measurement)
- [vanfraassen1980] ✓ van Fraassen, _The Scientific Image_, ch. 5, with [the chapter text](https://www.fitelson.org/290/vanfraassen_pte.pdf)
- [woodward2003] ○ [Woodward, _Making Things Happen_, OUP, 2003](https://academic.oup.com/book/4324)
- [woodward2010] ◐ [Woodward, "Causation in biology…", _Biology & Philosophy_ 25, 2010](https://link.springer.com/article/10.1007/s10539-010-9200-z)
