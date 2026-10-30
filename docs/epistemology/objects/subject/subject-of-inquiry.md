---
tags:
  - theory
index: "[Subject of inquiry](docs/epistemology/objects/subject/_index.md)"
aliases:
  - Subject of inquiry
---
# Subject of inquiry

> [!QUESTION] Goal: which objects does a research question study, and which of them change its possible answers?

The subject of inquiry is the first of the three [layers of specification](../question/question-specification.md#^three-layers) of a question. The layer covers the *subject* of a research question: the objects under study.

## Components of the subject

The subject of inquiry is written as a quadruple of components:
$$\Sigma=\langle S,P,X,D\rangle $$

The components are documented, field by field, in the [subject of a question](../../../specification/question-subject.md).

The four components fill a statement frame. The [epistemic aim](../task/epistemic-aim.md) selects the interrogative word of that frame: ^question-statement

> In [$S$] under [$D$], [interrogative word] [$P$] rather than [$X$]?

> [!WARNING] The domain $D$ holds only [restrictions](domain.md#^domain-restrictions) of the values that the target record and the background records admit about $S$.

## Selecting the specifications

**Inclusion criterion**: ^inclusion-test

> A specification is admitted only if its value *changes the possible answers* of the question, that is their type or their schema, or the *presuppositions* of the question.
> A specification that fails this test is at most an optional remark.

The possible answers and the presuppositions of a question are defined with the [answers of a question](../question/question.md#^answer-sets).

> [!QUOTE] Logic of questions, the source of the inclusion test
> A question is determined by the set of its possible answers [hamblin1958].
> A question presupposes every statement that must be true for it to have a true answer [belnap1976].

## Safeguards against rigidity

- **The type of a component can be fixed before its content.** The types of the components can be listed in advance, such as the types of target, the categories of phenomenon or the loci of a contrast, whereas their content cannot. A specification therefore restricts the type of a component and leaves its content free. The lists and the sentence frames are documented in the [subject of a question](../../../specification/question-subject.md).
- **The aim and the form of the question decide which components are required.** *Example*: a contrastive why-question requires a contrast $X$, as the note on the [contrast](contrast.md) states. The condition under which each component is required is documented with its field.
- **A specification may stay empty.** Characterizing the phenomenon is itself a discovery task [craver2013], and the descriptions that this task yields are revised or rejected [colaco2018]. A specification may therefore stay empty, and carry a [maturity](../status/statuses-and-acceptance.md#^maturity) that states whether its revision is expected. Whether an empty specification is a gap or a product of the inquiry is read from the aim, as the [attributes of a record](../question/question.md#^record-attributes) state.
- **Filling order.** The system $S$ and the phenomenon $P$ are specified together, since the partition of variables depends on $P$. The contrast $X$ is filled in two steps. Its locus can be typed as soon as the question schema is posed, as the [order of specification](../../processes/inquiry/specification-order.md) states, whereas its foils are specified afterwards, from the value space of $P$. The domain $D$ bounds all three.

## Precedent in quantitative methodology

Quantitative methodology already specifies questions through fixed slots. For example, a "theoretical estimand", the quantity that a study aims to learn, is stated outside any statistical model. It consists of a quantity defined for each unit and a target population [lundberg2021]. Clinical trials likewise define an estimand by five attributes [ich2019]. Each attribute maps onto a component of the subject of inquiry:

- population → reference class of the system $S$;
- endpoint → observable of the phenomenon $P$;
- treatment versus comparator → condition contrast in $X$;
- population-level summary → scope over instances in $P$;
- intercurrent events, the events after treatment that change the existence or the meaning of the outcome, such as stopping treatment → state restrictions in the domain $D$.

Both frameworks keep the question separate from any model. The [specification of a question](../question/question-specification.md) keeps its subject apart from its answers in the same way. Both frameworks, however, cover only questions about causal effects. The two frameworks therefore support the design of the slots, but not the option lists for capacities, mechanisms, and mathematical explanation.

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
> 	- the split of the specifications that a question admits about its target into a target record, which delimits $S$, and background records, which admit laws about it;
> 	- typed placeholders in the slots of a question, and the levels of commitment of the records that fill them.
> - **Absent from the literature:** a complete form for research questions.

Marks follow the [legend of reading marks](../../../../CONTRIBUTING.md#^reading-marks).

- [belnap1976] ◐ [Belnap & Steel, *The Logic of Questions and Answers*, Yale University Press, 1976](https://catalogue.bnf.fr/ark:/12148/cb353871722); presupposition and corrective answers checked through the [SEP entry on questions](https://plato.stanford.edu/entries/questions/); the division of a question into subject and request checked through Wiśniewski's summaries of the book
- [colaco2018] ◐ [Colaço, "Rip it up and start again", _SHPS A_ 72, 2018](https://www.sciencedirect.com/science/article/abs/pii/S003936811730211X)
- [craver2013] ◐ [Craver & Darden, *In Search of Mechanisms: Discoveries across the Life Sciences*, University of Chicago Press, 2013](https://press.uchicago.edu/ucp/books/book/chicago/I/bo16123713.html)
- [hamblin1958] ◐ [Hamblin, "Questions", *Australasian Journal of Philosophy* 36(3), 159–168, 1958](https://doi.org/10.1080/00048405885200211)
- [ich2019] ◐ [ICH E9(R1) Addendum on Estimands](https://en.wikipedia.org/wiki/ICH_E9\(R1\)_Addendum_On_Estimands_and_Sensitivity_Analyses_in_Clinical_Trials)
- [lundberg2021] ✓ [Lundberg, Johnson & Stewart, "What is your estimand?", _ASR_ 86(3), 2021](https://journals.sagepub.com/doi/abs/10.1177/00031224211004187)
