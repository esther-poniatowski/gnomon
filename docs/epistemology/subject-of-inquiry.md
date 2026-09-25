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

> [!QUESTION] Goal: what must be fixed to specify the objects that an inquiry studies?

The subject of inquiry is one of the [four layers that specify a research objective](inquiry-specification.md). The layer covers the *subject* of a research question: the objects under study.

## Components of the subject

The subject of inquiry is written as a quadruple of components:
$$\Sigma=\langle S,P,X,D\rangle $$

| Component | When it is required | Role | Example | Canonical tradition |
| --------- | ------------------- | ---- | ------- | ------------------- |
| **[Target system](target-system.md) $S$** | always | System or portion of reality about which knowledge is sought, and which the model represents | neuron | Philosophy of scientific models |
| **[Phenomenon](phenomenon.md) $P$** ("explanandum") | always, except for an exploratory question, where a search space replaces it | Aspect of $S$ to be explained (e.g. a fact, event, pattern, property, behavior) | firing rate | covering-law explanation [hempel1948] |
| **[Contrast class](contrast.md) $X$** | for a contrastive why-question, and implicit as the comparator in a question about a causal effect | Alternative(s) relative to which $P$ is puzzling — "why $P$ rather than $P'$?" | why spike rather than inactivity? | contrastive why-questions [vanfraassen1980] |
| **[Domain of conditions](domain.md) $D$** | when the question holds a condition fixed | Background conditions under which the system is studied (e.g. regime, limit, parameter range) | in vitro slice, injected current between 0 and 500 pA | "causal field" [mackie1974], "background conditions" [woodward2010], and "domain of validity" in physics |

The four components fill a statement frame. The [epistemic aim](epistemic-aim.md) selects the interrogative word of that frame: ^question-statement

> In [$S$] under [$D$], [interrogative word] [$P$] rather than [$X$]?

> [!WARNING] The domain $D$ holds only [restrictions of the a priori specification](domain.md#^domain-restrictions).

## Selecting the specifications

**Inclusion criterion**: ^inclusion-test

> A specification is admitted only if its value *changes the admissible answers* or the *presuppositions* of the question.
> A specification that fails this test is at most an optional remark.

Each admitted specification divides into two parts:

- **Closed option lists** fix the type of each component (target type, phenomenon category, contrast locus).
- **Framed free text** states the content, inside a sentence frame with named slots.

> [!QUOTE] Logic of questions, the source of the inclusion test
> A question is determined by the set of its possible answers [hamblin1958].
> A question presupposes every statement that must be true for it to have a true answer [belnap1976].

## Safeguards against rigidity

- **Type versus content.** Closed lists restrict only the types, so the content remains free text inside a frame.
- **Conditional requirements.** The [epistemic aim](epistemic-aim.md) $A$ and the form of the question determine which specifications are mandatory:
    - the contrast $X$, for contrastive why-questions;
    - the explanandum variable, whenever the contrast takes its foils from the possible values of $Y$;
    - the conditions and byproducts, only once they are known.
- **Open values with a maturity marker.** Every specification accepts the value "open". Each specification may also carry its own maturity marker (open, provisional, or stabilized), beside the marker that applies to the inquiry as a whole. Open values are admitted because characterizing the phenomenon is itself a discovery task [craver2013], and because the descriptions that this task yields are revised or rejected [colaco2018].
- **Filling order.** The system $S$ and the phenomenon $P$ are specified together, since the partition of variables depends on $P$. The contrast $X$ is then specified from the value space of $P$. The domain $D$ bounds all three.

## Precedent in quantitative methodology

Quantitative methodology already specifies questions through fixed slots. For example, a "theoretical estimand", the quantity that a study aims to learn, is stated outside any statistical model. It consists of a quantity defined for each unit and a target population [lundberg2021]. Clinical trials likewise define an estimand by five attributes [ich2019]. Each attribute maps onto a component of the subject of inquiry:

- population → reference class of the system $S$;
- endpoint → explanandum variable of the phenomenon $P$;
- treatment versus comparator → condition contrast in $X$;
- population-level summary → scope over instances in $P$;
- intercurrent events → state restrictions in the domain $D$.

Both frameworks keep the question separate from any model. The [specification of an inquiry separates its subject from the answer layer](inquiry-specification.md) in the same way. Both frameworks, however, cover only questions about causal effects. The two frameworks therefore support the design of the slots, but not the option lists for capacities, mechanisms, and mathematical explanation.

---
## Sources

> [!NOTE] Status of the claims
> - **Established:** each list of types and each constraint that carries a citation.
> - **Proposals:**
> 	- dividing a research question into the subject of inquiry and the epistemic task, by analogy with the subject and the request that the logic of questions distinguishes;
> 	- using the test drawn from the logic of questions to decide which specifications a question carries;
> 	- redistributing the scope, and introducing the domain of conditions $D$ as a new component;
> 	- the phenomenon category `structural-property`;
> 	- the slots of the state space of $S$ with their scopes, the exogenous variables and the external systems;
> 	- the domain $D$ as a set of restrictions on the admitted value sets, with limits allowed only when the question concerns the limit system;
> 	- selection criteria for formal classes as well as empirical ones;
> 	- the signature of an observable and the scope of the claim, read as operations on the indices of the recorded states;
> 	- the reference class generated by the other specifications, and the boundary read from the shared variables;
> 	- the exploratory question, read as a change in *which specifications are open*;
> 	- the search space of exploratory questions;
> 	- the variation test that separates the domain $D$ from the conditions of $P$;
> 	- the consistency conditions between specifications (target type with $\mu$, phenomenon category with $R$, foil status with the source of evidence).
> - **Absent from the literature:** a complete form for research questions.

Marks follow [the legend that states how each entry was checked](../../CONTRIBUTING.md#^reading-marks).

- [belnap1976] ◐ Belnap & Steel, _The Logic of Questions and Answers_, Yale UP, 1976, via [SEP, Questions](https://plato.stanford.edu/entries/questions/). The subject/request distinction was checked only through a summary returned by a search engine.
- [colaco2018] ◐ [Colaço, "Rip it up and start again", _SHPS A_ 72, 2018](https://www.sciencedirect.com/science/article/abs/pii/S003936811730211X)
- [craver2013] ◐ [Craver & Darden, _In Search of Mechanisms_, U. Chicago Press, 2013](https://press.uchicago.edu/ucp/books/book/chicago/I/bo16123713.html)
- [hamblin1958] ◐ [Hamblin, "Questions", _Australasian Journal of Philosophy_ 36(3), 1958](https://www.tandfonline.com/doi/abs/10.1080/00048405885200211)
- [hempel1948] ○ Hempel & Oppenheim, "Studies in the logic of explanation", _Philosophy of Science_ 15(2), 1948
- [ich2019] ◐ [ICH E9(R1) Addendum on Estimands](https://en.wikipedia.org/wiki/ICH_E9\(R1\)_Addendum_On_Estimands_and_Sensitivity_Analyses_in_Clinical_Trials)
- [lundberg2021] ✓ [Lundberg, Johnson & Stewart, "What is your estimand?", _ASR_ 86(3), 2021](https://journals.sagepub.com/doi/abs/10.1177/00031224211004187)
- [mackie1974] ◐ Mackie, _The Cement of the Universe_, OUP, 1974, "causal field", via [PhilPapers](https://philpapers.org/rec/MACTCO-17)
- [vanfraassen1980] ✓ van Fraassen, _The Scientific Image_, ch. 5, read in [the chapter text](https://www.fitelson.org/290/vanfraassen_pte.pdf)
- [woodward2010] ◐ [Woodward, "Causation in biology…", _Biology & Philosophy_ 25, 2010](https://link.springer.com/article/10.1007/s10539-010-9200-z)
