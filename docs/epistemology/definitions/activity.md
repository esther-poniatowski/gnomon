---
role: definition
status: wip
index: "[Definitions](docs/epistemology/definitions/_index.md)"
aliases:
  - Activity
  - Activities (mechanistic)
tags: []
source:
---
# Activity

> [!QUESTION] Goal: which sense of "activity" does a statement use, and how does an activity differ from a process, an interaction, an event, a function and a dynamic?

"Activity" carries four senses:

- a producer of change in a mechanism;
- an aspectual class of predicates;
- in neuroscience, a state variable;
- in an itinerary of inquiry, an epistemic act.

Only the first sense is specific to mechanistic explanation. This note fixes the relations of that sense to the neighboring terms.

## Senses

| Sense | Community | Definition | Examples | Source |
| --- | --- | --- | --- | --- |
| Mechanistic | new mechanistic philosophy | "Activities are the producers of change"; "Entities are the things that engage in activities", and an activity usually requires that its entities have properties of specific types | pushing, binding, opening, diffusing | [machamer2000] |
| Aspectual | philosophy of language, ancient philosophy | an atelic predicate, with the subinterval property; a Vendler activity, a process in the sense of Mourelatos, an *energeia* as opposed to a *kinēsis* | running, raining, computing | [vendler1957]; [mourelatos1978]; [aristotle_metaphysics]; [kenny1963] |
| State variable | neuroscience | the level of firing or of another signal of a neural population, such as the rate $r$ in $\dot r=-r+\phi(Wr+u)$, with an external input $u$ | "neural activity", "population activity" | — |
| Epistemic | philosophy of science, this method | an act of inquiry, typed by its inputs, its output and its norm in the [taxonomy of epistemic activities](activities/epistemic-activities.md) | formulating a question, fitting a model, testing a hypothesis | — |

A mechanistic activity carries four features [machamer2000] [machamer2004]:

- a location in space and time;
- a rate, a duration and an order relative to other activities;
- bearers, having the properties that enable the activity;
- productivity: the activity produces a change in its bearers or in other entities.

The number of bearers is not fixed: an activity may be unary, as bond breaking, or of indefinite arity, as equilibrating [illari2012].

Four positions divide the mechanistic literature on the status of activities:

| Position | Claim | Source |
| --- | --- | --- |
| Dualism | entities and activities are two irreducible categories | [machamer2000]; [machamer2004]; [illari2013] |
| Interactionism | activities reduce to interactions between parts, characterized by direct, invariant, change-relating generalizations | [glennan2002]; [glennan2017] |
| Synthesis | activities and interactions are complementary, and a mechanism requires both concepts | [tabery2004] |
| Process ontology | processes are primary, and entities are stabilized processes | [nicholson2018] |

The dualist position is opposed on the ground that the productivity of activities adds nothing to counterfactual dependence [psillos2004].

## Test cases

- **Raining is an activity in the aspectual sense only.** Raining has the subinterval property. However, no bearer engages in raining, so raining is not a mechanistic activity.
- **Computing is an activity in both senses.** Computing is atelic, and a mechanism of bearers carries out the computation. The process of computing differs from the [function computed](computation.md): the function is a static map.
- **Computing $f(3)$ is an accomplishment**, an event in the sense of the [vocabulary of process](process-event-history.md#^event), because it culminates in the output.
- **The neuroscientific sense names a variable.** In $\dot r=-r+\phi(Wr+u)$, the "activity" $r$ is a state variable. The terms of the equation name mechanistic activities: leaking ($-r$), integrating the inputs, and coupling through $W$.

> [!WARNING] The *energeia*–*kinēsis* passage of Aristotle
> The passage at *Metaphysics* Θ6, 1048b18–35, is absent from one branch of the manuscripts, and its authenticity is disputed.

## Distinctions

Each neighboring term differs from a mechanistic activity by one criterion:

| Term | Relation to a mechanistic activity | Criterion |
| --- | --- | --- |
| [Process](process-event-history.md#^process) | an activity is a process attributed to bearers and productive of change | a process needs neither a bearer nor productivity; raining is a process without bearer |
| [Interaction](interaction-and-cause.md#^action-interaction) | an interaction is an activity in which two or more distinct entities act on one another; when no two entities of an activity act on each other, the activity is an action | an activity may have one bearer, as a channel opening, or act in one direction, as one neuron inhibiting another without feedback |
| [Event](process-event-history.md#^event) | aspect is a separate attribute: a mechanistic activity is atelic, as diffusing, or telic, as binding or opening; one occurrence of a telic activity is an event | the quantization test of the vocabulary of process |
| [Function](function.md) | a function is the contribution of an activity to a [capacity](capacity-and-disposition.md) of the containing system | the same activity, pumping, has a function only relative to a system and a capacity [cummins1975] |
| [Dynamic](dynamic.md) | a dynamic is the global rule of change, and activities are its local components | a dynamic acts on the whole state; an activity changes the variables of its targets |
| Organization, in the [vocabulary of systems](system-constituent-environment.md) | an organization arranges several activities relative to one another | an activity is one local change; an organization is a property of an arrangement, such as a delayed feedback loop formed by two activities |
| [Mechanism](mechanism-and-mechanistic-model.md) | a mechanism is a set of entities and activities organized to produce a phenomenon | a single activity produces a change; a mechanism produces a phenomenon through organization |

## Consequences for a record

> [!NOTE] Proposal of this method
> The criterion of this section is a proposal of this method. This criterion does not state a standard of the literature.

- **A term of an additive decomposition of the dynamic is a candidate activity.** Given an interpretable decomposition $\dot x=\sum_{\ell\in L} f_\ell(x)$, an activity type is one term $f_\ell$. Its *bearers* and its *targets* are entities, never variables. The bearers are the constituents whose variables $f_\ell$ reads, and the targets are the constituents whose variables $f_\ell$ changes. Both are identified through the constituent kinds in the signatures of those variables. ^activity-term
- **An interaction is a term with mutual bearers and targets.** A term counts as an interaction when two distinct entities are each a bearer and a target of that term *for each other*. The term then reads the variables of each entity to change the variables of the other. Being both a bearer and a target is not enough, because an entity in the middle of a chain is both without acting on the entity that acts on it. *Example*: in the dynamic $\dot x=-x+W\phi(x)+u$ of a rate network, the coupling term $W\phi(x)$ is an interaction when $W$ connects some pair of neurons in both directions. The same term is a set of actions when $W$ is strictly feedforward, since no neuron then acts on a neuron that acts on it.
- **Productivity is tested by deletion or clamping.** A term is productive when deleting it, or clamping its output, changes the targets, in the interventionist sense [woodward2003]. The mutual manipulability of a part and the whole supplies the corresponding test of constitutive relevance [craver2007].
- **The decomposition is not unique.** Two sums of terms can define one dynamic, so the activities returned by the criterion depend on the decomposition chosen. Therefore, when a record states activities, it must also state the decomposition. The laws $L$ of an [answer](../answer-form.md) already state a decomposition when the answer is a [mechanism](../mechanism.md).

---
## Sources

Marks follow the [legend of reading marks](../../../CONTRIBUTING.md#^reading-marks).

- [aristotle_metaphysics] ◐ [Aristotle, *Metaphysics* Θ6, 1048b18–35](https://plato.stanford.edu/entries/aristotle-metaphysics/); authenticity of the passage disputed (Burnyeat, *Oxford Studies in Ancient Philosophy* 34, 2008)
- [craver2007] ◐ [Craver, *Explaining the Brain: Mechanisms and the Mosaic Unity of Neuroscience*, Clarendon Press, 2007](https://doi.org/10.1093/acprof:oso/9780199299317.001.0001)
- [cummins1975] ◐ [Cummins, "Functional analysis", *Journal of Philosophy* 72(20), 741–765, 1975](https://doi.org/10.2307/2024640)
- [glennan2002] ◐ [Glennan, "Rethinking mechanistic explanation", *Philosophy of Science* 69(S3), S342–S353, 2002](https://doi.org/10.1086/341857)
- [glennan2017] ◐ [Glennan, *The New Mechanical Philosophy*, Oxford University Press, 2017](https://doi.org/10.1093/oso/9780198779711.001.0001)
- [illari2012] ◐ [Illari & Williamson, "What is a mechanism? Thinking about mechanisms across the sciences", *European Journal for Philosophy of Science* 2(1), 119–135, 2012](https://doi.org/10.1007/s13194-011-0038-2); bond breaking is a unary activity, and equilibrating has indefinite arity
- [illari2013] ◐ [Illari & Williamson, "In defence of activities", *Journal for General Philosophy of Science* 44(1), 69–83, 2013](https://doi.org/10.1007/s10838-013-9217-5)
- [kenny1963] ◐ [Kenny, *Action, Emotion and Will*, Routledge & Kegan Paul, 1963](https://www.routledge.com/products/9780203711460)
- [machamer2000] ◐ [Machamer, Darden & Craver, "Thinking about mechanisms", *Philosophy of Science* 67(1), 1–25, 2000](https://doi.org/10.1086/392759); the two quoted sentences, p. 3, were checked through a secondary quotation only
- [machamer2004] ◐ [Machamer, "Activities and causation: the metaphysics and epistemology of mechanisms", *International Studies in the Philosophy of Science* 18(1), 27–39, 2004](https://doi.org/10.1080/02698590412331289242)
- [mourelatos1978] ◐ [Mourelatos, "Events, processes, and states", *Linguistics and Philosophy* 2(3), 415–434, 1978](https://doi.org/10.1007/BF00149015)
- [nicholson2018] ◐ [Nicholson & Dupré (eds.), *Everything Flows: Towards a Processual Philosophy of Biology*, Oxford University Press, 2018](https://doi.org/10.1093/oso/9780198779636.001.0001)
- [psillos2004] ◐ [Psillos, "A glimpse of the secret connexion: harmonizing mechanisms with counterfactuals", *Perspectives on Science* 12(3), 288–319, 2004](https://doi.org/10.1162/1063614042795426)
- [tabery2004] ◐ [Tabery, "Synthesizing activities and interactions in the concept of a mechanism", *Philosophy of Science* 71(1), 1–15, 2004](https://doi.org/10.1086/381409)
- [vendler1957] ◐ [Vendler, "Verbs and times", *Philosophical Review* 66(2), 143–160, 1957](https://doi.org/10.2307/2182371)
- [woodward2003] ◐ [Woodward, *Making Things Happen: A Theory of Causal Explanation*, Oxford University Press, 2003](https://doi.org/10.1093/0195155270.001.0001)
