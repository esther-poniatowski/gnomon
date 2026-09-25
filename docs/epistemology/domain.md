---
role: definition
status: stable
index: "[Epistemology](docs/epistemology/_index.md)"
aliases:
  - Specifying the domain of conditions
  - Domain of conditions
tags: []
source:
---
# Specifying the domain of conditions

> [!QUESTION] Goal: what must be fixed to specify the background conditions of an inquiry?

The domain of conditions is the fourth component of the [subject of inquiry](subject-of-inquiry.md).

The domain $D$ records the restrictions that the question imposes on the a priori specification of the system, possibly before any phenomenon is named. ^domain-restrictions

> [!NOTE] Conditions versus domain
> The domain $D$ fixes the *background* under which the system is studied [mackie1974]. The [conditions of the phenomenon](phenomenon.md#^conditions-byproducts) are instead circumstances whose relation to the behavior belongs to the characterization.

**Operational test**:

> Fact and foil share the domain $D$, so no factor in $D$ can distinguish the fact from the foil [lipton2004]. ^domain-test

By this test, a background factor moves from the domain $D$ into the conditions of $P$, or into the contrast $X$, once the question compares two of its values.

| Specification | When it is required | Options or frame | Examples | Source |
| ------------- | ------------------- | ---------------- | -------- | ------ |
| Restrictions | when the question narrows, for some quantity, the value set that the system specification admits | Per restriction: the quantity held and the value set that it is held to. When no single quantity carries a restriction, the entry names it and states its defining expression. A restriction on a variable also states its mode: `clamped` · `restricted` · `initial` · `stationary` · `without-event`. Each restriction carries a justification stating why the question is put only within those bounds. | connection probability between 0.05 and 0.2; the velocity field held stationary; more trainable parameters than training examples | target population [lundberg2021]; [ich2019] |
| Limit | only when the question concerns the limit system itself | the expression "[quantity] → [limit value]", with a justification stating why the question is about the limit system | network width → ∞ (kernel regime); number of spins $N\to\infty$ (thermodynamic limit) | limit systems [norton2012] |

- **Each entry of $D$ restricts a set of admitted values.** The slots of $S$ state the value sets that define the system. An entry of $D$ records only the *restriction* that the question chooses within one of those sets. An empty $D$ means that the question covers the whole reference class.
	
- **The domain $D$ need not contain every assumption endorsed during the analysis.** The question fixes $D$ before the answer is sought. The analysis introduces its own assumptions afterwards, for instance a mean-field approximation or a separation of time scales. [The answer records these assumptions as its idealizations](answer-form.md#^answer-elements). An answer that relies on such an assumption is valid for the question only where that idealization is accurate. ^analysis-assumptions
	
- **A clamped state variable is removed from the dynamics.** When the question clamps a variable, the rule that determines it is replaced by a fixed value. In a causal model, an intervention likewise replaces the structural equation of the targeted variable by a constant [pearl2009]. For the question, the clamped variable therefore acts as an input. *Example*: a voltage clamp turns the membrane potential into an exogenous variable.
	
- **A limit belongs to $D$ only when the question concerns the limit system.** A limit system counts as a system of its own, because it can have properties that no finite system has [norton2012]. *Example*: a question about the kernel regime of infinitely wide networks concerns such a limit system. When a limit only simplifies the analysis of finite systems, [the answer records the limit as an assumption](#^analysis-assumptions).

---
## Sources

Marks follow [the legend that states how each entry was checked](../../CONTRIBUTING.md#^reading-marks).

- [ich2019] ◐ [ICH E9(R1) Addendum on Estimands](https://en.wikipedia.org/wiki/ICH_E9\(R1\)_Addendum_On_Estimands_and_Sensitivity_Analyses_in_Clinical_Trials)
- [lipton2004] ◐ Lipton, _Inference to the Best Explanation_, 2nd ed., ch. 3; [Lipton, "Making a difference"](https://www.hps.cam.ac.uk/files/lipton-making-difference.pdf)
- [lundberg2021] ✓ [Lundberg, Johnson & Stewart, "What is your estimand?", _ASR_ 86(3), 2021](https://journals.sagepub.com/doi/abs/10.1177/00031224211004187)
- [mackie1974] ◐ Mackie, _The Cement of the Universe_, OUP, 1974, "causal field", via [PhilPapers](https://philpapers.org/rec/MACTCO-17)
- [norton2012] ◐ [Norton, "Approximation and idealization: why the difference matters", _Philosophy of Science_ 79(2), 2012](https://philpapers.org/rec/NORAAI)
- [pearl2009] ○ Pearl, _Causality_, 2nd ed., CUP, 2009, exogenous versus endogenous variables
