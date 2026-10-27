---
role: definition
status: wip
index: "[Definitions](docs/epistemology/definitions/_index.md)"
aliases:
  - Process, event and history
  - Process
  - Event
  - History
  - Course and grain
  - Occurrence class
tags: []
source:
---
# Process, event and history

> [!QUESTION] Goal: how are a state, a process and an event told apart, so that a record can state each one over a declared course?

A **history** is the trajectory of a system along a declared course, such as time. A **state**, a **process** and an **event** are three classes of predicates on the segments of that course [mourelatos1978]. The classes are told apart by one operation: a segment that satisfies the predicate is restricted to its parts. The definitions of this note reach this form by revising a standard definition until it covers "raining".

## Senses

| Term | Community | Definition | Source |
| --- | --- | --- | --- |
| Process | realist ontology | a sequence, ordered in time, of changes of state of one thing: a trajectory in its state space | [bunge1977] |
| Event | realist ontology | a change of state of a thing, represented by an ordered pair of states $\langle s,s'\rangle$ | [bunge1977] |
| Causal process | philosophy of causation | a process capable of transmitting a mark | [salmon1984] |
| Event | metaphysics of events | a particular individuated by its causes and effects; alternatively, the exemplification of a property by an object at a time | [davidson1969]; [kim1976] |
| State, process, event | aspectual semantics | three classes of situations: a state holds without change at each instant of a period; a process is homogeneous change; an event is a change that is complete only at its end | [mourelatos1978] |
| Activity, process | aspectual semantics | a predicate with the subinterval property: it holds of every part of a period of which it holds ("running", "raining") | [vendler1957]; [mourelatos1978]; [dowty1979] |
| Accomplishment, event | aspectual semantics | a predicate with a culmination, failing of the proper parts of a period of which it holds ("running a mile") | [vendler1957]; [mourelatos1978] |
| Quantized predicate | event semantics | a predicate that, when it holds of an entity, holds of no proper part of that entity; quantized predicates are telic, and some telic predicates are not quantized | [krifka1998] |
| Process | process ontology | an entity that persists and changes, as an object does | [stout1997]; [galton2009] |

## Test cases

The definition of a process as a trajectory of one thing fails on "raining" in three respects.

- **"Raining" has no single bearer.** "It is raining" places a feature without naming a particular that bears it [strawson1959]. Choosing the atmosphere as the system restores a bearer. However, this choice reverses the order of definition: the process defines the system. A field formalization avoids the reversal. The precipitation rate $r(x,t)$ is defined at each point $x$, and the region where it rains is the set where $r>0$.
- **A trajectory cannot mark the difference between a process and an event.** Every trajectory is bounded by its two end times. The distinction lies in the behavior of the predicate that describes the trajectory when the segment is restricted [vendler1957] [mourelatos1978].
- **A process can itself change.** "The rain is getting heavier" attributes a change to the process. One account concludes that processes are continuants [stout1997], and that conclusion is opposed [steward2013]. A formal reply keeps the occurrent view: raining is the accumulation of precipitation at a sustained non-zero rate $r$, and "getting heavier" is the process $\dot r>0$ on that rate.

A second test case, "computing", requires an abstract state space and an implementation map. Both are defined in the [vocabulary of computation](computation.md).

## Revised definitions

The definitions are stated relative to a **level of description**. The level fixes a state space $\mathcal{X}$. When the level is abstract, $\mathcal{X}$ is the codomain of the [implementation map](computation.md#^implementation-map) $\pi$.

The predicates range over the segments of a declared course, at a declared grain:

- **Course**: an ordered index set $\mathbb{T}$ along which the behavior unfolds, such as time, the steps of training, or an input parameter $\theta$ swept by the question. A **segment** is an interval $[a,b]\subseteq\mathbb{T}$. ^course
- **Grain**: the length $\delta>0$ below which the description resolves no segment. The grain is needed because closure under restriction fails on very short segments: a segment of walking shorter than one step does not count as walking.
- **History** (a token): a trajectory $\gamma:[t_0,t_1]\to\mathcal{X}$ over a segment of the course. ^history

Each predicate $\Pi$ on segments falls in at most one of three classes:

- **State** (a type): $\Pi$ holds of a segment if and only if it holds at every point of the segment, so a state needs no change. *Example*: "the network sits at its fixed point $x^*$". ^state-class
- **Process** (a type): $\Pi$ is closed under restriction to every sub-segment of length at least $\delta$, and it holds at no single point, because it requires change. If $\Pi(\gamma|_{[a,b]})$ holds and $[a',b']\subseteq[a,b]$ with $b'-a'\geq\delta$, then $\Pi(\gamma|_{[a',b']})$ holds. *Examples*: "the rate rises"; "it rains over the region", read as the increase of the precipitation accumulated over the region. A process is often identified by a rate or flux variable that stays non-zero. The condition $r>0$ is evaluated point by point, so on its own it is a state of the rate, and the process is the increase of the quantity accumulated at that rate. The bearer of a process, a system or a region of a field, may be specified after the process. ^process
- **Event** (a type): $\Pi$ is *quantized*: when it holds of a segment, it holds of no proper sub-segment [krifka1998]. The **culmination** of an event is the first point at which a terminal condition is reached. *Example*: for disjoint sets $\mathcal{A}$ and $\mathcal{B}$ of states, a transition from $\mathcal{A}$ to $\mathcal{B}$ holds of $[a,b]$ when $\gamma(a)\in\mathcal{A}$, $\gamma(b)\in\mathcal{B}$, and $\gamma(t)\notin\mathcal{A}\cup\mathcal{B}$ for $a<t<b$. The culmination is $b$, the first entry into $\mathcal{B}$. The event of realist ontology, the pair $\langle s,s'\rangle$, is this predicate restricted to singleton sets. ^event

A predicate in none of the three classes is restated as an **observable over a declared window** $[a,b]$, and the value of that observable enters a manifestation. Two examples fall in no class: ^window-observable

- "the mean rate over the window exceeds 5 Hz" can fail on a sub-window, so it is neither a state nor a process. The predicate can also hold of a proper sub-window, so it is not an event either. The predicate is restated as the mean rate over $[a,b]$;
- "the rate rises then falls" holds at no single point and fails on its rising sub-segment, so it is neither a state nor a process. A proper sub-segment around the peak also satisfies it, so it is not an event. The predicate is restated as the sign pattern of the slope over $[a,b]$.

| Class | Test on the sub-segments of a segment where $\Pi$ holds | Example |
| --- | --- | --- |
| State | $\Pi$ holds on every sub-segment, down to single points | the network sits at its fixed point |
| Process | $\Pi$ holds on every sub-segment of length at least $\delta$, and at no single point | the rate rises; the network relaxes toward its fixed point |
| Event | $\Pi$ holds on no proper sub-segment | the membrane potential climbs from rest to threshold; computing $f(3)$ |
| None | restated as an observable over a declared window | the mean rate over the window exceeds 5 Hz |

## Distinctions

- **A history is a token, whereas a state, a process and an event are types.** One history can satisfy several predicates of each class.
- **A state predicate differs from the state of a system.** The [state of a system](state-and-configuration.md) is the tuple of values of its variables at one point of the course. A state predicate holds of a segment when the state at each of its points satisfies the predicate.

> [!WARNING] Open question
> The metaphysical status of processes remains disputed: one account treats them as occurrents, unfolding in time, and another as continuants, persisting and changing [seibt2022] [rescher1996] [stout1997] [steward2013]. The occurrent definition of this note is an operational choice for modeling, and it does not settle the metaphysical question.

## Consequences for a record

- **A phenomenon declares its course and its occurrence class.** The [record of a phenomenon](../phenomenon.md) states its `course` in three fields. The `index` is a symbol of the index set along which the behavior unfolds, the `grain` is $\delta$, and `varies` lists the target parameters that change along this course. The record also states its `occurrence`, one of `state | process | event | not-applicable`.
- **A parameter of the target can change along the course of one phenomenon.** *Example*: the weights $W$ of a network are parameters of the target, and they change along the course of training, so a phenomenon of training lists $W$ in `course.varies`. The [role test of a quantity](variable-value-observable.md#^role-test) places such a quantity.
- **The category of a phenomenon reads as follows in the occurrence classes:**

| `phenomenon.category` | Reading in the occurrence classes | `occurrence` |
| --- | --- | --- |
| `particular-occurrence` | one token of a state, a process or an event, at a stated segment of the course | `state`, `process` or `event`, the class of the token |
| `regularity` | a dependence among occurrences, each of which carries its own class | `not-applicable` |
| `capacity` | a [disposition](capacity-and-disposition.md), held whether or not it is exercised | `not-applicable` |
| `structural-property` | a property of states or of a map, holding pointwise along the course | `state` |

- **A predicate in none of the classes enters a phenomenon through an observable.** The [observable over a window](#^window-observable) is declared among the explanandum variables of the [phenomenon](../phenomenon.md), and its manifestation constrains the value of that observable.
- **A process stated over a field requires an index set for space.** The bearer of "raining" is a region, so the record declares a spatial index set in the [target specification](../target-system.md), and the rate variable takes that index in its signature.

---
## Sources

Marks follow the [legend of reading marks](../../../CONTRIBUTING.md#^reading-marks).

- [bunge1977] ◐ [Bunge, *Treatise on Basic Philosophy*, vol. 3, *Ontology I: The Furniture of the World*, Reidel, 1977](https://doi.org/10.1007/978-94-010-9924-0); ch. 5, "Change"
- [davidson1969] ◐ [Davidson, "The individuation of events", in Rescher et al. (eds.), *Essays in Honor of Carl G. Hempel*, Reidel, 216–234, 1969](https://doi.org/10.1007/978-94-017-1466-2_11)
- [dowty1979] ◐ [Dowty, *Word Meaning and Montague Grammar*, Reidel, 1979](https://doi.org/10.1007/978-94-009-9473-7)
- [galton2009] ◐ [Galton & Mizoguchi, "The water falls but the waterfall does not fall: new perspectives on objects, processes and events", *Applied Ontology* 4(2), 71–107, 2009](https://doi.org/10.3233/AO-2009-0067)
- [kim1976] ◐ [Kim, "Events as property exemplifications", in Brand & Walton (eds.), *Action Theory*, Reidel, 159–177, 1976](https://doi.org/10.1007/978-94-010-9074-2_9)
- [krifka1998] ◐ [Krifka, "The origins of telicity", in Rothstein (ed.), *Events and Grammar*, Kluwer, 197–235, 1998](https://semantics.uchicago.edu/kennedy/classes/s07/events/krifka98[ms].pdf); quantization, §2.1, and telicity, read in the author's manuscript; page numbers of the published version checked through secondary sources
- [mourelatos1978] ◐ [Mourelatos, "Events, processes, and states", *Linguistics and Philosophy* 2(3), 415–434, 1978](https://doi.org/10.1007/BF00149015)
- [rescher1996] ◐ [Rescher, *Process Metaphysics: An Introduction to Process Philosophy*, SUNY Press, 1996](https://doi.org/10.1515/9781438417110)
- [salmon1984] ◐ [Salmon, *Scientific Explanation and the Causal Structure of the World*, Princeton University Press, 1984](https://press.princeton.edu/books/paperback/9780691101705/scientific-explanation-and-the-causal-structure-of-the-world); ch. 5, p. 148
- [seibt2022] ◐ [Seibt, "Process philosophy", *Stanford Encyclopedia of Philosophy*, substantive revision 26 May 2022](https://plato.stanford.edu/entries/process-philosophy/)
- [steward2013] ◐ [Steward, "Processes, continuants, and individuals", *Mind* 122(487), 781–812, 2013](https://doi.org/10.1093/mind/fzt080); argues against the view that processes are continuants
- [stout1997] ◐ [Stout, "Processes", *Philosophy* 72(279), 19–27, 1997](https://doi.org/10.1017/S0031819100056631)
- [strawson1959] ◐ Strawson, *Individuals: An Essay in Descriptive Metaphysics*, Methuen, 1959; feature-placing statements in ch. 6, §2, and ch. 7, checked through an online copy of the text
- [vendler1957] ◐ [Vendler, "Verbs and times", *Philosophical Review* 66(2), 143–160, 1957](https://doi.org/10.2307/2182371)
