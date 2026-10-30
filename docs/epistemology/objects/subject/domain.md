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
	
- **The domain $D$ need not contain every assumption endorsed during the analysis.** The question fixes $D$ before the answer is sought. The analysis introduces its own assumptions afterwards, for instance a mean-field approximation or a separation of time scales. The answer records each such assumption among its grounds, and classifies it as an [idealization](../answer/answer-form.md#^idealizations) of its target when the assumption distorts that target. An answer that relies on such an assumption is valid for the question only over the range where that idealization is accurate. ^analysis-assumptions
	
- **A clamped state variable is removed from the dynamics.** When the question clamps a variable, the rule that determines it is replaced by a fixed value. In a causal model, an intervention likewise replaces the structural equation of the targeted variable by a constant [pearl2009]. For the question, the clamped variable therefore acts as an input. *Example*: a voltage clamp turns the membrane potential into an exogenous variable.
	
- **A limit belongs to $D$ only when the question concerns the limit system.** A limit system counts as a system of its own, because it can have properties that no finite system has [norton2012]. *Example*: a question about the kernel regime of infinitely wide networks concerns such a limit system. When a limit only simplifies the analysis of finite systems, the answer records the limit among its grounds, as one of the [analysis assumptions](#^analysis-assumptions). That assumption is an idealization with the motive `limit`, as the [rule on limits](../../../specification/answer.md#^limit-rule) states.

- **The conditions of an inquiry take four places among its components.** The method classifies a [condition](../../vocabulary/quantities/condition.md) by its place alone, among the following four: ^condition-places

| Condition | Place in the inquiry |
| --- | --- |
| A restriction imposed by the question on admitted values, including clamped, initial or stationary states | the domain $D$ |
| A precipitating, inhibiting or modulating condition of the behavior, or a nonstandard circumstance | the [conditions of the phenomenon](phenomenon.md#^conditions-byproducts) |
| A constraint on the states that may hold together, including at the start and at the boundary | a law with the role *state-constraint*, in a [background record](../knowledge/background.md) or in an answer |
| An assumption introduced by the analysis, such as a mean-field limit | not a condition: the [idealizations of the answer](../answer/answer-form.md#^idealizations), unless the question is asked of the limit system itself, as the [rule on limits](../../../specification/answer.md#^limit-rule) decides |

---
## Sources

Marks follow the [legend of reading marks](../../../../CONTRIBUTING.md#^reading-marks).

- [lipton2004] ◐ [Lipton, *Inference to the Best Explanation*, 2nd ed., Routledge, 2004](https://doi.org/10.4324/9780203470855); ch. 3, "The causal model", checked through [Lipton, "Making a difference", *Philosophica* 51, 39–54, 1993](https://www.hps.cam.ac.uk/files/lipton-making-difference.pdf)
- [mackie1974] ◐ Mackie, _The Cement of the Universe_, OUP, 1974, "causal field", via [PhilPapers](https://philpapers.org/rec/MACTCO-17)
- [norton2012] ◐ [Norton, "Approximation and idealization: why the difference matters", _Philosophy of Science_ 79(2), 2012](https://philpapers.org/rec/NORAAI)
- [pearl2009] ◐ [Pearl, *Causality: Models, Reasoning, and Inference*, 2nd ed., Cambridge University Press, 2009](https://doi.org/10.1017/CBO9780511803161); exogenous versus endogenous variables
