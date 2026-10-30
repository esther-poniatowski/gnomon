---
tags:
  - theory
index: "[Subject of inquiry](docs/epistemology/subject/_index.md)"
aliases:
  - Subject of inquiry
---
# Subject of inquiry

> [!QUESTION] Goal: what must be fixed to specify the objects that an inquiry studies?

The subject of inquiry is one of the four [layers of specification](../inquiry/inquiry-specification.md) of a research objective. The layer covers the *subject* of a research question: the objects under study.

## Components of the subject

The subject of inquiry is written as a quadruple of components:
$$\Sigma=\langle S,P,X,D\rangle $$

The components are documented, field by field, in the [subject of a question](../../specification/question-subject.md).

The four components fill a statement frame. The [epistemic aim](../epistemic-task/epistemic-aim.md) selects the interrogative word of that frame: ^question-statement

> In [$S$] under [$D$], [interrogative word] [$P$] rather than [$X$]?

> [!WARNING] The domain $D$ holds only [restrictions](domain.md#^domain-restrictions) of the a priori specification.

## Selecting the specifications

**Inclusion criterion**: ^inclusion-test

> A specification is admitted only if its value *changes the types of the admissible answers*, that is the schema of the admissible answers, or the *presuppositions* of the question.
> A specification that fails this test is at most an optional remark.

Each admitted specification divides into two parts:

- **Closed option lists** fix the type of each component (target type, phenomenon category, contrast locus).
- **Framed free text** states the content, inside a sentence frame with named slots.

> [!QUOTE] Logic of questions, the source of the inclusion test
> A question is determined by the set of its possible answers [hamblin1958].
> A question presupposes every statement that must be true for it to have a true answer [belnap1976].

## Safeguards against rigidity

- **Type versus content.** Closed lists restrict only the types, so the content remains free text inside a frame.
- **Conditional requirements.** The [epistemic aim](../epistemic-task/epistemic-aim.md) $A$ and the form of the question determine which specifications are mandatory:
    - the contrast $X$, for contrastive why-questions;
    - the explanandum variable, whenever the contrast takes its foils from the possible values of $Y$;
    - the conditions and byproducts, only once they are known.
- **Empty values with a maturity marker.** Every specification may stay empty while it is not filled. Whether an empty specification is a gap or a product of the inquiry is read from the [requirements of the epistemic aim](../../specification/question-task.md#^required-by-aim), never from the record. The marker of each specification is documented under the [maturity of a field](../../specification/maturity.md). Empty values are admitted because characterizing the phenomenon is itself a discovery task [craver2013], and because the descriptions that this task yields are revised or rejected [colaco2018].
- **Filling order.** The system $S$ and the phenomenon $P$ are specified together, since the partition of variables depends on $P$. The contrast $X$ is then specified from the value space of $P$. The domain $D$ bounds all three.

## Precedent in quantitative methodology

Quantitative methodology already specifies questions through fixed slots. For example, a "theoretical estimand", the quantity that a study aims to learn, is stated outside any statistical model. It consists of a quantity defined for each unit and a target population [lundberg2021]. Clinical trials likewise define an estimand by five attributes [ich2019]. Each attribute maps onto a component of the subject of inquiry:

- population → reference class of the system $S$;
- endpoint → explanandum variable of the phenomenon $P$;
- treatment versus comparator → condition contrast in $X$;
- population-level summary → scope over instances in $P$;
- intercurrent events → state restrictions in the domain $D$.

Both frameworks keep the question separate from any model. The [inquiry specification](../inquiry/inquiry-specification.md) separates its subject from the answer layer in the same way. Both frameworks, however, cover only questions about causal effects. The two frameworks therefore support the design of the slots, but not the option lists for capacities, mechanisms, and mathematical explanation.

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
> 	- the exploratory question, read as a change in *which specifications the inquiry produces*;
> 	- the search space of exploratory questions;
> 	- the variation test that separates the domain $D$ from the conditions of $P$;
> 	- the consistency conditions between specifications (target type with $\mu$, phenomenon category with $R$, foil status with the source of evidence);
> 	- the split of the a priori specification into a target record, which delimits $S$, and background records, which admit laws about it;
> 	- typed placeholders in the slots of a question, and the levels of commitment of the records that fill them.
> - **Absent from the literature:** a complete form for research questions.

Marks follow the [legend of reading marks](../../../CONTRIBUTING.md#^reading-marks).

- [belnap1976] ◐ Belnap & Steel, _The Logic of Questions and Answers_, Yale UP, 1976, via [SEP, Questions](https://plato.stanford.edu/entries/questions/). The subject/request distinction was checked only through a summary returned by a search engine.
- [colaco2018] ◐ [Colaço, "Rip it up and start again", _SHPS A_ 72, 2018](https://www.sciencedirect.com/science/article/abs/pii/S003936811730211X)
- [craver2013] ◐ [Craver & Darden, _In Search of Mechanisms_, U. Chicago Press, 2013](https://press.uchicago.edu/ucp/books/book/chicago/I/bo16123713.html)
- [hamblin1958] ◐ [Hamblin, "Questions", _Australasian Journal of Philosophy_ 36(3), 1958](https://www.tandfonline.com/doi/abs/10.1080/00048405885200211)
- [ich2019] ◐ [ICH E9(R1) Addendum on Estimands](https://en.wikipedia.org/wiki/ICH_E9\(R1\)_Addendum_On_Estimands_and_Sensitivity_Analyses_in_Clinical_Trials)
- [lundberg2021] ✓ [Lundberg, Johnson & Stewart, "What is your estimand?", _ASR_ 86(3), 2021](https://journals.sagepub.com/doi/abs/10.1177/00031224211004187)
