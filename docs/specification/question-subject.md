---
tags:
  - specification
index: "[Specification](docs/specification/_index.md)"
aliases:
  - Subject of a question
  - Specifying the subject of inquiry
  - Specifying the contrast
  - Specifying the domain of conditions
---
# Subject of a question

> [!QUESTION] Goal: what does a researcher write in the `subject` block of a question record?

The grounds of the components are stated in the note on the [subject of inquiry](../epistemology/objects/subject/subject-of-inquiry.md).

## Components of the subject

| Component | When it is required | Role | Example | Canonical tradition |
| --------- | ------------------- | ---- | ------- | ------------------- |
| **[Target system](../epistemology/objects/subject/target-system.md) $S$** | always | System or portion of reality about which knowledge is sought, and which the model represents | neuron | Philosophy of scientific models |
| **[Background](../epistemology/objects/knowledge/background.md)** of $S$ | when the question rests on laws of $S$ admitted before it seeks its answer | Bodies of laws about $S$ admitted by the question; they qualify $S$ and add no fifth component to $\Sigma$ | the leaky integration of each neuron, admitted with the network | laws of succession and coexistence [winther2020] |
| **[Phenomenon](../epistemology/objects/subject/phenomenon.md) $P$** (the explanandum, under the aim explanation) | always, except for an exploratory question, where a search space replaces it | Behavior of $S$ that the question concerns (e.g. a fact, event, pattern, property, behavior) | firing rate | covering-law explanation [hempel1948] |
| **[Contrast class](../epistemology/objects/subject/contrast.md) $X$** | for a contrastive why-question, and implicit as the comparator in a question about a causal effect | Alternative(s) relative to which $P$ is puzzling — "why $P$ rather than $P'$?" | why spike rather than inactivity? | contrastive why-questions [vanfraassen1980] |
| **[Domain of conditions](../epistemology/objects/subject/domain.md) $D$** | when the question holds a condition fixed | Conditions held fixed under which the system is studied (e.g. regime, limit, parameter range) | in vitro slice, injected current between 0 and 500 pA | "causal field" [mackie1974], "background conditions" [woodward2010], and "domain of validity" in physics |

- **Placeholders before records.** The target-system slot and the phenomenon slot of a question accept a record identifier or a typed placeholder. The type of a placeholder fits its slot: the target-system slot awaits a `system`, and the phenomenon slot a `phenomenon`. A question whose slots hold placeholders is a [question schema](../epistemology/objects/question/question.md#^question-schema). A slot that names a record requires the record to reach at least the commitment `identified`, as the [levels of commitment](../epistemology/objects/question/question.md#^commitment-levels) define it. Each record of a target or of a phenomenon declares its own commitment, `identified` or `specified`. ^placeholder-slots

## Contrast

The grounds of the contrast fields are stated in the note on the [contrast](../epistemology/objects/subject/contrast.md). ^contrast-fields

| Specification | When it is required | Options or frame | Examples | Source |
| ------------- | ------------------- | ---------------- | -------- | ------ |
| Locus | for a contrastive why-question | other outcome (same system and conditions, other value of $P$) · other system ($P$ absent) · other condition (same system, different setting or intervention) | synchronous rather than asynchronous activity (outcome); this network rather than a network without inhibitory neurons (system); a strong rather than a weak stimulus (condition) | [vanfraassen1980]; [lipton2004]; potential outcomes $Y_i(d)$ vs $Y_i(d')$ [lundberg2021] |
| Foil set | for a contrastive why-question, with the other values of the explanandum variable as default | per foil, the expressions over the declared observables that hold in that case, with a reading | asynchronous activity (listed); every other oscillation frequency (rule) | [woodward2003] |
| Compatibility | never stated on its own: the locus fixes it | exclusive · compatible (fact and foil co-occur in different systems) | synchronous versus asynchronous activity of one network (exclusive); Smith versus Jones contracting paresis (compatible) | [vanfraassen1980]; [lipton2004] |
| Foil status | with a foil set | observed (a realized comparison case) · counterfactual | a recorded control network (observed); the same network trained on another task (counterfactual) | [lipton2004] |

- **A condition foil may reuse an entry of the conditions of $P$.** A condition foil (i.e. the same system in another setting) often names such an entry, for instance an inhibiting circumstance. The foil then refers to that entry, so the circumstance is described only once.

## Domain of conditions

The grounds of the domain fields are stated in the note on the [domain of conditions](../epistemology/objects/subject/domain.md). ^domain-fields

| Specification | When it is required | Options or frame | Examples | Source |
| ------------- | ------------------- | ---------------- | -------- | ------ |
| Restrictions | when the question narrows, for some quantity, the value set that the system specification admits | Per restriction: the quantity held and the value set that it is held to. When no single quantity carries a restriction, the entry names it and states its defining expression. A restriction on a variable also states its mode: `clamped` · `restricted` · `initial` · `stationary` · `without-event`. Each restriction carries a justification stating why the question is put only within those bounds. | connection probability between 0.05 and 0.2; the velocity field held stationary; more trainable parameters than training examples | target population [lundberg2021]; [ich2019] |
| Limit | only when the question concerns the limit system itself | the expression "[quantity] → [limit value]", with a justification stating why the question is about the limit system | network width → ∞ (kernel regime); number of spins $N\to\infty$ (thermodynamic limit) | limit systems [norton2012] |

---
## Sources

Marks follow the [legend of reading marks](../../CONTRIBUTING.md#^reading-marks).

- [hempel1948] ○ Hempel & Oppenheim, "Studies in the logic of explanation", _Philosophy of Science_ 15(2), 1948
- [ich2019] ◐ [ICH E9(R1) Addendum on Estimands](https://en.wikipedia.org/wiki/ICH_E9\(R1\)_Addendum_On_Estimands_and_Sensitivity_Analyses_in_Clinical_Trials)
- [lipton2004] ◐ Lipton, _Inference to the Best Explanation_, 2nd ed., ch. 3; [Lipton, "Making a difference"](https://www.hps.cam.ac.uk/files/lipton-making-difference.pdf)
- [lundberg2021] ✓ [Lundberg, Johnson & Stewart, "What is your estimand?", _ASR_ 86(3), 2021](https://journals.sagepub.com/doi/abs/10.1177/00031224211004187)
- [mackie1974] ◐ Mackie, _The Cement of the Universe_, OUP, 1974, "causal field", via [PhilPapers](https://philpapers.org/rec/MACTCO-17)
- [norton2012] ◐ [Norton, "Approximation and idealization: why the difference matters", _Philosophy of Science_ 79(2), 2012](https://philpapers.org/rec/NORAAI)
- [vanfraassen1980] ✓ van Fraassen, _The Scientific Image_, ch. 5, read in [the chapter text](https://www.fitelson.org/290/vanfraassen_pte.pdf)
- [winther2020] ◐ [Winther, "The structure of scientific theories", _SEP_, revised 2020](https://plato.stanford.edu/entries/structure-scientific-theories/), §3.1.1 on the state-space approach
- [woodward2003] ○ [Woodward, _Making Things Happen_, OUP, 2003](https://academic.oup.com/book/4324)
- [woodward2010] ◐ [Woodward, "Causation in biology…", _Biology & Philosophy_ 25, 2010](https://link.springer.com/article/10.1007/s10539-010-9200-z)
