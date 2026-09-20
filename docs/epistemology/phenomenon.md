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

> [!WARNING] Phenomena are features inferred from data, but they are distinct from the data [bogen1988].

Read together, the phenomenon is described in a statement:

> [bearer: noun phrase] | [behavior: verb phrase] | [conditions: clause]

*Example*: "the excitatory population | oscillates at gamma frequency | when a visual stimulus is presented (precipitating condition)".

| Specification | When it is required | Options or frame | Examples | Source |
| ------------- | ------------------- | ---------------- | -------- | ------ |
| Statement: bearer | always | "[$S$, a part of $S$, an aggregate of parts]" | "the excitatory population" | [kaiser2017], "object-involving occurrent" |
| Statement: behavior | always | "[verb phrase: what the bearer does or undergoes]" | "oscillates at gamma frequency" | [craver2007], "$S$'s $\psi$-ing"; [kaiser2017] |
| Category | always | particular event · regularity (effect) · capacity · structural property | the burst recorded at $t=12$ s (event); gamma power increases with stimulus contrast (regularity); gating inputs by context (capacity); a low-dimensional representation (structural property) | [hempel1948]; [cummins2000] |
| Explanandum variables | whenever the contrast takes its foils from the values of the variable, or the answer must be tested against measurements | "[variable $Y$] takes [value $y$] among [possible values of $Y$]" | $Y$ = "regime of the population activity", $y$ = "synchronous" (possible values: "asynchronous", "synchronous") | [woodward2003] |
| Explanandum variables: scale | with each variable | categorical, e.g. presence or class (nominal) · ordinal, e.g. sign or rank · quantitative, e.g. magnitude (interval or ratio) | "the network oscillates": categorical; "the spike phase of each neuron over time": quantitative | [stevens1946] |
| Explanandum variables: parts covered (index $i$) | when the bearer has several constituents | "[the constituents that the variable covers: every unit, a named subpopulation, or one unit]" | every neuron of the excitatory population; the units of layer 2/3; the one recorded neuron | — |
| Explanandum variables: aggregation | when the variable covers several constituents | each constituent kept apart · summary over the constituents (mean, total) · distribution over the constituents | the rate of each neuron (each constituent kept apart); the population rate (summary); the distribution of rates across neurons (distribution) | — |
| Explanandum variables: followed along (index $t$) | always, since a variable that is followed along nothing takes the value none | time · a parameter of the system or of an external system · none | the course of one trial (time); the width of the network (parameter); a stationary rate, which is followed along nothing (none) | — |
| Explanandum variables: profile | when the variable is followed along time or along a parameter | single value · summary over the course (average, stationary value) · full profile (trajectory, curve, scaling law) | stationary rate (single value); time-averaged gamma power (summary); accuracy as a function of network width (full profile) | — |
| Scope over instances (index $k$) — an instance is a member of the reference class of $S$, or one realization of a system (a trial, a random initialization, a disorder sample) | when the question ranges over a reference class or over repeated realizations | single instance · typical instance (holds for almost every instance) · ensemble summary · ensemble distribution | one trained network (single); the typical network across initializations (typical); mean accuracy over initializations (ensemble summary) | [lundberg2021]; [ich2019] |
| Conditions and byproducts: precipitating | when a condition must hold for the behavior to occur | "[condition that triggers the behavior]" | a visual stimulus is presented | [craver2013] |
| Conditions and byproducts: inhibiting | when a condition is known to prevent the behavior | "[condition that prevents the behavior]" | feedforward inhibition is raised above the threshold that suppresses the oscillation | [craver2013] |
| Conditions and byproducts: modulating | when a condition changes a feature of the behavior without preventing it | "[condition]" changes "[feature of the behavior]" by "[direction or size of the change]" | raising the stimulus contrast increases the gamma power and shifts its peak frequency upward | [craver2013] |
| Conditions and byproducts: nonstandard | when the behavior is obtained only under unusual circumstances | "[unusual circumstance under which the behavior can be made to occur]" | a slice preparation under carbachol | [craver2013] |
| Conditions and byproducts: byproducts | when the behavior has further effects outside the phenomenon | "[further effect of the behavior, outside the phenomenon itself]" | the metabolic cost of the sustained spiking | [craver2013] |
| Evidential status | always | established across data sets or methods · reported · predicted · derived within a model | gamma oscillations in V1, recorded across laboratories (established); a transition to chaos predicted by mean-field theory (predicted); the stationary rate of a balanced network (derived) | [bogen1988]; [colaco2018] |
| Detection criterion | when the phenomenon is the product of the inquiry, or its status is below established | "[what a candidate pattern must satisfy to count as established]" | a pattern counts as established when it recurs across instances and across recording methods | [bogen1988]; [exploratory questions](#^exploratory-phenomenon) |
| Data | when the status rests on recorded or derived material | per entry, "[pointer to a data set, a recording or a derivation]" that establishes the phenomenon | a recording session; a published figure; the derivation of a stationary rate | [bogen1988]; [colaco2018] |

- **The explanandum variable(s) restates the behavior in terms of the system's state.** The possible values matter because an explanation answers counterfactual questions ("what-if-things-had-been-different"): which changes would have given $Y$ another value [woodward2003]. The same values supply the default foils of the contrast $X$.

- **The value scale fixes which comparisons between values are meaningful**, and hence which dependence claims an answer can make. *Example*: an ordinal variable supports "the stronger the input, the higher $Y$", not "$Y$ doubles" [stevens1946]. The grain of the values is fixed separately, by the possible values listed for $Y$: "oscillates or not" is coarser than "oscillates at 30, 40 or 60 Hz".

> [!NOTE] Manifestations of the phenomenon
> "Manifestations" denote the features of the behavior, such as its frequency, amplitude or spatial extent [craver2013]. These features are recorded in the behavior, in the explanandum variables and in the rows that follow them over parts, over the course and over instances. The name "behavior" is kept for the occurrent itself: the activity or process [kaiser2017].

- **Category narrows the [requested relation](requested-relation.md) $R$.** *Examples*: In psychology, capacities are explained by functional analysis. Effects are regularities that themselves need explaining [cummins2000].
	
- **The option "Structural property" is not standard**. The occurrent analysis [kaiser2017] excludes such a property, unless it is restated as the outcome of a process. *Example*: the "low dimensionality of a learned representation" is a structural property, that may be reformulated as: "training produces a low-dimensional representation". The restated version admits mechanistic and dynamical answers.

- **Qualitative phenomena might be later turned into quantitative phenomena**. The "qualitative" option serves as soon as the phenomenon has not been operationalized nor characterized in details. After gathering more data or refining the analysis, the phenomenon may be formalized and parametrized, providing new variables to be related quantitatively to the conditions. *Example*: "oscillations" can be at first a qualitative label, but subsequently, they can be parametrized with a phase, amplitude, etc.
	
- **Conditions and byproducts form a closed list of five standard kinds** [craver2013], stated one per row above. A background factor that the question varies leaves the domain $D$ by the [operational test](domain.md#^domain-test), and becomes one of these conditions or a foil of the contrast $X$. ^conditions-byproducts
	
- **Granularity must be specified as a property of the phenomenon.** Proportionality requires cause and effect to be described without irrelevant detail [woodward2010]. The grain at which a phenomenon is described therefore sets the grain at which a matching explanans is sought by default. ^resolution-proportionality
	
- **The rows over parts, over the course and over instances are specified independently.** The states recorded for a phenomenon form an array $x_i(t;k)$, indexed by constituent $i$, by time or a parameter $t$, and by instance $k$. The parts covered and the aggregation say which constituents the variable ranges over and how their values are combined; what the variable is followed along, and the profile kept of it, say the same for the course; the scope over instances sets the extent of the claim over the reference class. The first four belong to the variable itself, whereas the last belongs to the claim. *Example*: two statements of the same oscillation differ in every row:
	
    - "the network oscillates": every neuron of the excitatory population, summarized · followed along time, summarized · typical instance;
    - "the spike phase of each neuron over time, across network initializations": every neuron, kept apart · followed along time, full profile · ensemble distribution.
    
- **A row is required only when what it indexes takes several values:** the parts, for a bearer with many constituents; the course, for a behavior that unfolds along time or a parameter, and which otherwise is followed along nothing; the instances, for a reference class or for repeated realizations. Each row changes the admissible answers. *Examples*: a correlation computed over aggregates can differ from the same correlation computed over individuals [robinson1950], and an average taken over instances before the analysis can differ from one taken after, as a quenched average differs from an annealed one [mezard1987].

- **Evidential status carries a question's presupposition.** A why-question presupposes that its topic is true [vanfraassen1980]. If a phenomenon is only predicted, then the question is conditional, or the  [epistemic aim](epistemic-aim.md) is detection. For instance, the question of characterizing the "memory transfer" phenomenon was abandoned after this phenomenon was rejected [colaco2018].
	
- **An object of research may admit several phenomena** when the [epistemic aim](epistemic-aim.md) is a description. Experimental research often targets an "object of research", such as a memory system. Phenomena serve both as components of that object and as evidence for it [feest2017].

- **An exploratory question leaves the phenomenon open and fixes a search space instead.** Exploratory experimentation varies parameters systematically to find regularities and to form concepts, when no theory yet delimits the phenomenon [steinle1997]. Instruments that measure many variables at once support this search [franklin2005]. This form of inquiry uses the same fields as any other question, only their status change: 
	
    - open, since they form the answer: bearer, behavior, category;
    - required, filled with the candidate observables: explanandum variables, with their value scales and index rows;
    - required, filled with the varied factors and their ranges: conditions of $P$, since a factor that the question varies leaves $D$ by the [operational test](domain.md#^domain-test);
    - required, stated as the detection criterion: evidential status, namely what a candidate pattern must satisfy to count as established, for instance stability across instances [bogen1988];
    - empty: the contrast $X$.
	
    *Example*: "in a recurrent network trained on a context-dependent task, which patterns appear in the population activity as the strength of the context signal varies?" ^exploratory-phenomenon

---
## Sources

Marks: ✓ the text itself was read · ◐ checked through an abstract, the publisher page or a secondary summary · ○ cited from standard knowledge, not fetched in this session.

- [bogen1988] ○ Bogen & Woodward, "Saving the phenomena", _Philosophical Review_ 97(3), 1988
- [colaco2018] ◐ [Colaço, "Rip it up and start again", _SHPS A_ 72, 2018](https://www.sciencedirect.com/science/article/abs/pii/S003936811730211X)
- [craver2007] ◐ [Craver, _Explaining the Brain_, OUP, 2007](https://philpapers.org/rec/CRAETB-2)
- [craver2013] ◐ [Craver & Darden, _In Search of Mechanisms_, U. Chicago Press, 2013](https://press.uchicago.edu/ucp/books/book/chicago/I/bo16123713.html)
- [cummins2000] ✓ [Cummins, "How does it work?" versus "What are the laws?", in _Explanation and Cognition_, MIT Press, 2000](https://direct.mit.edu/books/edited-volume/4894/chapter/623167/How-Does-It-Work-versus-What-Are-the-Laws-Two)
- [feest2017] ◐ [Feest, "Phenomena and objects of research…", _Philosophy of Science_ 84(5), 2017](https://philarchive.org/rec/FEEPAO)
- [franklin2005] ◐ [Franklin, "Exploratory experiments", _Philosophy of Science_ 72(5), 2005](https://philpapers.org/rec/FRAEE)
- [hempel1948] ○ Hempel & Oppenheim, "Studies in the logic of explanation", _Philosophy of Science_ 15(2), 1948
- [ich2019] ◐ [ICH E9(R1) Addendum on Estimands](https://en.wikipedia.org/wiki/ICH_E9\(R1\)_Addendum_On_Estimands_and_Sensitivity_Analyses_in_Clinical_Trials)
- [kaiser2017] ◐ [Kaiser & Krickel, "The metaphysics of constitutive mechanistic phenomena", _BJPS_ 68(3), 2017](https://academic.oup.com/bjps/article/68/3/745/2669661)
- [lundberg2021] ✓ [Lundberg, Johnson & Stewart, "What is your estimand?", _ASR_ 86(3), 2021](https://journals.sagepub.com/doi/abs/10.1177/00031224211004187)
- [mezard1987] ◐ Mézard, Parisi & Virasoro, _Spin Glass Theory and Beyond_, World Scientific, 1987, quenched versus annealed averages
- [robinson1950] ◐ [Robinson, "Ecological correlations and the behavior of individuals", _American Sociological Review_ 15(3), 1950](https://en.wikipedia.org/wiki/Ecological_correlation)
- [steinle1997] ◐ [Steinle, "Entering new fields: exploratory uses of experimentation", _Philosophy of Science_ 64, S65–S74, 1997](https://philpapers.org/rec/STEENF)
- [stevens1946] ◐ Stevens, "On the theory of scales of measurement", _Science_ 103, 1946, via [Wikipedia, Level of measurement](https://en.wikipedia.org/wiki/Level_of_measurement)
- [vanfraassen1980] ◐ van Fraassen, _The Scientific Image_, ch. 5; [the chapter text](https://www.fitelson.org/290/vanfraassen_pte.pdf)
- [woodward2003] ○ [Woodward, _Making Things Happen_, OUP, 2003](https://academic.oup.com/book/4324)
- [woodward2010] ◐ [Woodward, "Causation in biology…", _Biology & Philosophy_ 25, 2010](https://link.springer.com/article/10.1007/s10539-010-9200-z)
