---
tags:
  - theory
index: "[Subject of inquiry](docs/epistemology/objects/subject/_index.md)"
aliases:
  - Domain of conditions
---
# Domain of conditions

> [!QUESTION] Goal: which restrictions does a question impose on admitted values, and how do they differ from the assumptions of an analysis?

The domain of conditions is the fourth component of the [subject of inquiry](subject-of-inquiry.md).

The domain $D$ records the restrictions that the question imposes on the values that the target record and the background records admit, possibly before any phenomenon is named. ^domain-restrictions

> [!NOTE] Conditions versus domain
> The domain $D$ holds the conditions held fixed, in the sense of a *causal field*: the circumstances that a causal question treats as fixed [mackie1974]. A condition is held fixed when the fact and its foils share it, as the operational test below states, and a quantity restricted by $D$ may still range over several values. The [conditions of the phenomenon](phenomenon.md#^conditions-byproducts) are instead circumstances whose relation to the behavior belongs to the characterization.

**Operational test**:

> Fact and foil share the domain $D$, so no factor in $D$ can distinguish the fact from the foil [lipton2004]. ^domain-test

By this test, a factor moves from the domain $D$ into the conditions of $P$, or into the contrast $X$, once the question compares two of its values.

The fields of the domain are documented in the [subject of a question](../../../specification/question-subject.md).

- **Each entry of $D$ restricts a set of admitted values.** The slots of $S$ state the value sets that define the system. An entry of $D$ records only the *restriction* that the question chooses within one of those sets. An empty $D$ means that the question covers the whole reference class.
	
- **The domain $D$ need not contain every assumption endorsed during the analysis.** The question fixes $D$ before the answer is sought. The analysis introduces its own assumptions afterwards, for instance a mean-field approximation, which replaces the interactions of each unit by their average, or a separation of time scales. The answer records each such assumption among its grounds, and classifies it as an [idealization](../answer/answer-form.md#^idealizations) of its target when the assumption distorts that target. An answer that relies on such an assumption is valid for the question only over the range where that idealization is accurate. ^analysis-assumptions
	
- **A clamped state variable is removed from the dynamics.** When the question clamps a variable, the rule that determines it is replaced by a fixed value. In a causal model, an intervention likewise replaces the structural equation of the targeted variable by a constant [pearl2009]. For the question, the clamped variable therefore acts as an input. *Example*: a voltage clamp turns the membrane potential into an exogenous variable. A parameter that the [course of the phenomenon](phenomenon.md#^course-and-occurrence) lists as varying can be clamped in the same way, since it changes along that course, whereas any other parameter is already fixed, so holding it states nothing.
- **A restriction on a variable selects courses, and its mode states the form of the selection.** A clamped variable leaves the dynamics, as the previous bullet states. The four other modes keep the rule that determines the variable, and admit only the courses produced by this rule and meeting the restriction. A restriction in these modes therefore conditions on the values of the variable, whereas clamping sets them by an intervention [pearl2009]. The four modes differ in the part of the [course](../../vocabulary/change/process-event-history.md#^course) that the restriction reads: ^restriction-modes
    - `initial`: the restriction reads only the value at the first point of the course, the [initial state](../../vocabulary/quantities/condition.md) $x_0$, and the rule determines every later value;
    - `stationary`: the restriction admits only the courses whose law is invariant under every shift along the course [grimmett2001]. For a variable without randomness, a stationary course is constant, such as a fixed point maintained by the rule itself, unlike a clamped value. For a random variable, a stationary course is one whose statistics do not change along the course, such as a turbulent flow whose statistics no longer drift;
    - `without-event`: the restriction admits only the courses on which a stated [event](../../vocabulary/change/process-event-history.md#^event) does not occur. *Example*: the courses of a population process on which the population does not go extinct by a given time [meleardvillemonais2012];
    - `restricted`: the restriction holds the variable within a stated set of values, in a form that none of the three modes above names.
	
- **A limit belongs to $D$ only when the question concerns the limit system.** When a limit only simplifies the analysis of finite systems, it is one of the [analysis assumptions](#^analysis-assumptions), recorded among the grounds of the answer as an idealization, as the [rule on limits](../../vocabulary/representations/idealization-and-abstraction.md#^limit-rule) decides.

- **The conditions of an inquiry take four places among its components.** The method classifies a [condition](../../vocabulary/quantities/condition.md) by its place alone, among the following four: ^condition-places

| Condition | Place in the inquiry |
| --- | --- |
| A restriction imposed by the question on admitted values, including clamped, initial or stationary states | the domain $D$ |
| A precipitating, inhibiting or modulating condition of the behavior, or a nonstandard circumstance | the [conditions of the phenomenon](phenomenon.md#^conditions-byproducts) |
| A constraint on the states that may hold together, including at the start and at the boundary | a law with the role *state-constraint*, in a [background record](../knowledge/background.md) or in an answer |
| An assumption introduced by the analysis, such as a mean-field limit | not a condition: the [idealizations of the answer](../answer/answer-form.md#^idealizations), unless the question is asked of the limit system itself, as the [rule on limits](../../vocabulary/representations/idealization-and-abstraction.md#^limit-rule) decides |

---
## Sources

Marks follow the [legend of reading marks](../../../../CONTRIBUTING.md#^reading-marks).

- [grimmett2001] ◐ [Grimmett & Stirzaker, *Probability and Random Processes*, 3rd ed., Oxford University Press, 2001](https://www.statslab.cam.ac.uk/~grg/books/prpcontents.html); §8.2, "Stationary processes", located through the table of contents; strong stationarity, the invariance of the joint laws under every shift, cited from standard knowledge
- [lipton2004] ◐ [Lipton, *Inference to the Best Explanation*, 2nd ed., Routledge, 2004](https://doi.org/10.4324/9780203470855); ch. 3, "The causal model", checked through [Lipton, "Making a difference", *Philosophica* 51, 39–54, 1993](https://www.hps.cam.ac.uk/files/lipton-making-difference.pdf)
- [mackie1974] ◐ Mackie, _The Cement of the Universe_, OUP, 1974, "causal field", via [PhilPapers](https://philpapers.org/rec/MACTCO-17)
- [meleardvillemonais2012] ◐ [Méléard & Villemonais, "Quasi-stationary distributions and population processes", *Probability Surveys* 9, 340–410, 2012](https://arxiv.org/abs/1112.4732); a process for which extinction is an absorbing state, checked through the abstract; the law of the process conditional on non-extinction cited from standard knowledge
- [pearl2009] ◐ [Pearl, *Causality: Models, Reasoning, and Inference*, 2nd ed., Cambridge University Press, 2009](https://doi.org/10.1017/CBO9780511803161); exogenous versus endogenous variables; conditioning on a value versus setting it by an intervention, cited from standard knowledge
