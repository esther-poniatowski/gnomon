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

> [!NOTE] Conditions versus Domain
> The domain $D$ fixes the *background* where the system is studied, possibly before any phenomenon is named. In contrast, the [conditions of the phenomenon](phenomenon.md#^conditions-byproducts) are circumstances whose relation to the behavior belongs to the characterization. 

**Operational test**: 

> Fact and foil share the domain $D$, so no factor in the domain $D$ can be the difference between fact and foil [lipton2004]. ^domain-test

A background factor moves from the domain $D$ into the conditions of $P$, or into the contrast $X$, once the question compares two of its values.

| Specification | When it is required | Options or frame | Examples | Source |
| ------------- | ------------------- | ---------------- | -------- | ------ |
| Parameter restrictions | when the question holds a parameter below its admitted values | "[parameter of $S$ or of an external system] ∈ [subset of its admitted values]" | connection probability between 0.05 and 0.2; latent dimension of the inputs fixed at 10 | "causal field" [mackie1974]; "background conditions" [woodward2010] |
| State restrictions | when the question holds a state variable below its value set | "[state variable] clamped at [value]" · "[state variable] ∈ [restricted range]" · initial states in [set] · stationary states only · trajectories without [event] | membrane potential clamped at −70 mV; weights initialized at small norm; training runs that do not diverge | intervention as replacement of an equation [pearl2009]; intercurrent events [ich2019] |
| Limit | only when the question concerns the limit system itself | "[quantity] → [limit value]" | network width → ∞ (kernel regime); number of spins $N\to\infty$ (thermodynamic limit) | limit systems [norton2012] |

- **Each entry of $D$ restricts a set of admitted values.** The slots of $S$ state the value sets that define the system, whereas $D$ records only the restriction chosen for the question. An empty $D$ means that the question covers the whole reference class.
	
- **The domain $D$ does not need to contain every assumption endorsed during the analysis.** The question fixes $D$ before the answer is sought, and the analysis introduces its own assumptions afterwards, for instance a mean-field approximation or a separation of time scales. These assumptions belong to the [answer layer](answer-form.md#^answer-elements): the answer records them as its idealizations. An answer that relies on such an assumption holds for the question only as far as the assumption holds. ^analysis-assumptions
	
- **A clamped state variable leaves the dynamics.** Clamping replaces the rule that determines the variable by a fixed value, as an intervention replaces the structural equation of its variable [pearl2009]. For the question, the clamped variable acts as an input. *Example*: a voltage clamp turns the membrane potential into an exogenous variable.
	
- **A limit belongs to $D$ only when the question concerns the limit system.** A limit system can have properties that no finite system has [norton2012]. *Example*: a question about the kernel regime of infinitely wide networks concerns such a limit system. When the limit only simplifies the analysis of finite systems, it is one of the [assumptions introduced by the analysis](#^analysis-assumptions).

---
## Sources

Marks: ✓ the text itself was read · ◐ checked through an abstract, the publisher page or a secondary summary · ○ cited from standard knowledge, not fetched in this session.

- [ich2019] ◐ [ICH E9(R1) Addendum on Estimands](https://en.wikipedia.org/wiki/ICH_E9\(R1\)_Addendum_On_Estimands_and_Sensitivity_Analyses_in_Clinical_Trials)
- [lipton2004] ◐ Lipton, _Inference to the Best Explanation_, 2nd ed., ch. 3; [Lipton, "Making a difference"](https://www.hps.cam.ac.uk/files/lipton-making-difference.pdf)
- [mackie1974] ◐ Mackie, _The Cement of the Universe_, OUP, 1974, "causal field", via [PhilPapers](https://philpapers.org/rec/MACTCO-17)
- [norton2012] ◐ [Norton, "Approximation and idealization: why the difference matters", _Philosophy of Science_ 79(2), 2012](https://philpapers.org/rec/NORAAI)
- [pearl2009] ○ Pearl, _Causality_, 2nd ed., CUP, 2009, exogenous versus endogenous variables
- [woodward2010] ◐ [Woodward, "Causation in biology…", _Biology & Philosophy_ 25, 2010](https://link.springer.com/article/10.1007/s10539-010-9200-z)
