---
role: definition
status: stable
index: "[Epistemology](docs/epistemology/_index.md)"
aliases:
  - Specifying the subject of inquiry
  - Subject of inquiry
tags: []
source:
---
# Specifying the subject of inquiry

> [!QUESTION] Goal: what must be fixed to specify what an inquiry is about?

This [layer of inquiry](inquiry-specification.md) names the objects under study: the subject of the research question, not the whole question.

## Components of the subject

The subject of inquiry can be represented as:
$$\Sigma=\langle S,P,X,D\rangle $$

| Component | When it is required | Role | Example | Canonical tradition |
| --------- | ------------------- | ---- | ------- | ------------------- |
| **[Target system](target-system.md) $S$** | always | System or portion of reality about which knowledge is sought, that the model represents | neuron | Philosophy of scientific models |
| **[Phenomenon](phenomenon.md) $P$** ("explanandum") | always, except for an exploratory question, which puts a search space in its place | Aspect about $S$ to be explained — a fact, event, pattern, property, behavior, etc. | firing rate | Hempel–Oppenheim |
| **[Contrast class](contrast.md) $X$** | for a contrastive why-question; implicit in a causal-effect question, where it is the comparator | Alternative(s) relative to which $P$ is puzzling — "why $P$ rather than $P'$?" | why spike rather than inactivity? | van Fraassen |
| **[Domain of conditions](domain.md) $D$** | when the question holds a condition fixed | Background conditions where the system is studied — regime, limit, parameter range, etc. | in vitro slice, injected current between 0 and 500 pA | "causal field" [mackie1974], "background conditions" [woodward2010]; "domain of validity" in physics |

Each component is developed in its own note, linked in the table.

Read together, the components fill a statement frame, whose interrogative word the [epistemic aim](epistemic-aim.md) selects: ^question-statement

> In [$S$] under [$D$], [interrogative word] [$P$] rather than [$X$]?

> [!WARNING] The domain $D$ holds only [restrictions of the a priori specification](domain.md#^domain-restrictions).

## Selecting the specifications

**Inclusion criterion**: ^inclusion-test

> A specification is admitted only if its value *changes the admissible answers* or the *presuppositions* of the question. 
> One that fails this test is at most an optional remark, so it is never mandatory. 

The specification follows from this split:

- **Closed option lists** fix the type of each component (target type, phenomenon category, contrast locus).
- **Framed free text** carries the content, inside a sentence frame with named slots.

> [!QUOTE] Logic of questions
> A question is known once the set of its possible answers is known [hamblin1958]. 
> A question presupposes every statement that must be true for it to have a true answer [belnap1976]. 

## Safeguards against rigidity

- **Type versus content.** Closed lists apply only to types; the content stays free text inside a frame.
- **Conditional requirements.** Whether a specification is mandatory is determined by the [epistemic aim](epistemic-aim.md) $A$ and the form of the question. The contrast $X$ is required for contrastive why-questions, the explanandum variable whenever the contrast takes its foils from the possible values of $Y$, and the conditions and byproducts only once they are known.
- **Open values with a maturity marker.** Every specification accepts "open", and each one may carry its own marker, among open, provisional and stabilized, beside the maturity of the inquiry as a whole. Characterizing the phenomenon is itself a discovery task [craver2013], and characterizations get revised or rejected [colaco2018].
- **Filling order.** The system $S$ and the phenomenon $P$ are specified together, since the partition of variables depends on $P$. The contrast $X$ follows from the value space of the phenomenon $P$. The conditions $D$ bound all three.

## Precedent in quantitative methodology

Quantitative methodology already specifies questions through fixed slots. A "theoretical estimand" (the quantity a study aims to learn) is stated outside any statistical model. It consists of a quantity defined for each unit and a target population [lundberg2021]. Clinical trials define an estimand by five attributes [ich2019]. These attributes map onto the proposal:

- population → reference class of the system $S$;
- endpoint → explanandum variable of the phenomenon $P$;
- treatment versus comparator → condition contrast in $X$;
- population-level summary → scope over instances in $P$;
- intercurrent events → state restrictions in the domain $D$.

Both frameworks keep the question separate from any model, which mirrors the separation between the subject of inquiry and the answer layer in the [inquiry specification](inquiry-specification.md). They cover only causal-effect questions. They therefore support the slot design, but not the option lists for capacities, mechanisms or mathematical explanation.

---
## Sources

> [!NOTE] What is established
> - **Established:** each list of types and each constraint cited above.
> - **Proposals:**
> 	- dividing a research question into its subject (this layer) and its epistemic task, by analogy with the subject and the request of a question;
> 	- using the logic-of-questions test to decide which specifications a question carries;
> 	- redistributing the scope and the new component of conditions $D$;
> 	- the structural-property category;
> 	- the state-space slots of $S$ with their scopes, the interface and the external systems;
> 	- the domain $D$ as a set of restrictions on the admitted value sets, with limits admitted only when the question concerns the limit system;
> 	- selection criteria for formal classes as well as empirical ones;
> 	- the index rows of $P$ (parts, profile, instances), read as operations on the indices of the recorded states;
> 	- the reference class generated by the other specifications, and the interface in place of a stated boundary;
> 	- the exploratory question as a change in which specifications are open, not a separate kind of question;
> 	- the search space of exploratory questions;
> 	- the variation test that separates the domain $D$ from the conditions of $P$;
> 	- the consistency conditions between specifications (target type with $\mu$, phenomenon category with $R$, foil status with the source of evidence).
> - **Absent from the literature:** a complete form for research questions.

Marks: ✓ the text itself was read · ◐ checked through an abstract, the publisher page or a secondary summary · ○ cited from standard knowledge, not fetched in this session.

- [belnap1976] ◐ Belnap & Steel, _The Logic of Questions and Answers_, Yale UP, 1976, via [SEP, Questions](https://plato.stanford.edu/entries/questions/); the subject/request distinction was checked only through a search-engine summary, not in the book
- [colaco2018] ◐ [Colaço, "Rip it up and start again", _SHPS A_ 72, 2018](https://www.sciencedirect.com/science/article/abs/pii/S003936811730211X)
- [craver2013] ◐ [Craver & Darden, _In Search of Mechanisms_, U. Chicago Press, 2013](https://press.uchicago.edu/ucp/books/book/chicago/I/bo16123713.html)
- [hamblin1958] ◐ [Hamblin, "Questions", _Australasian Journal of Philosophy_ 36(3), 1958](https://www.tandfonline.com/doi/abs/10.1080/00048405885200211)
- [ich2019] ◐ [ICH E9(R1) Addendum on Estimands](https://en.wikipedia.org/wiki/ICH_E9\(R1\)_Addendum_On_Estimands_and_Sensitivity_Analyses_in_Clinical_Trials)
- [lundberg2021] ✓ [Lundberg, Johnson & Stewart, "What is your estimand?", _ASR_ 86(3), 2021](https://journals.sagepub.com/doi/abs/10.1177/00031224211004187)
- [mackie1974] ◐ Mackie, _The Cement of the Universe_, OUP, 1974, "causal field", via [PhilPapers](https://philpapers.org/rec/MACTCO-17)
- [woodward2010] ◐ [Woodward, "Causation in biology…", _Biology & Philosophy_ 25, 2010](https://link.springer.com/article/10.1007/s10539-010-9200-z)
