---
tags:
  - theory
  - wip
index: "[Epistemic activities](docs/epistemology/activities/_index.md)"
aliases:
  - Problem-posing activities
  - Problematization
  - Question formulation
  - Subject identification
  - Question decomposition (activity)
  - Question selection
---
# Problem-posing

> [!QUESTION] Goal: which activities turn a source into a problem and a problem into a question, and by which norm is each judged?

The activities of this family output the objects that open an inquiry: a problem, a question schema, an identified subject or a question. These objects are defined in the notes on the [epistemic problem](../inquiry/epistemic-problem.md) and on [problems and questions](../inquiry/question.md), together with the [levels of commitment](../inquiry/question.md#^commitment-levels) of a slot. Each activity of this family is typed by its [signature](epistemic-activities.md#^activity-criterion).

## Signatures

| Activity | Inputs | Output | Mode | Context |
| --- | --- | --- | --- | --- |
| `problematization` | `source` | `problem` | non-inferential | discovery |
| `constraint-specification` | `problem`, `background-model` | `problem` | deductive | discovery |
| `question-formulation` | `problem` | `question-schema` | non-inferential | discovery |
| `subject-identification` | `question-schema` | `identified-subject` | non-inferential | discovery |
| `question-decomposition` | `question` | `question` | deductive | discovery |
| `question-selection` | `question` (several) | `question` | non-inferential | discovery |

## Norms

| Activity | Operation | The test `norm.<activity-id>` passes when |
| --- | --- | --- |
| `problematization` | state the demand for a solution and the constraints that bind it, from a source such as an anomaly or a conflict between results | the demand and the constraints are stated, and each explicandum carries a pointer to its source [dewey1938] [nickles1981] [laudan1977] |
| `constraint-specification` | derive further conditions on any solution from the problem and from the admitted background laws | each constraint is traced to a source or to a background law [nickles1981] |
| `question-formulation` | turn a problem into a question whose slots are typed | the answer space is typed, and the presuppositions of the question are stated [hamblin1958] [belnap1976] [vanfraassen1980] |
| `subject-identification` | fix the referent of each slot of a question schema by a definite description and pointers | each slot refers to a record at commitment `identified` |
| `question-decomposition` | replace a question by subquestions whose answers help to answer it | erotetic implication holds: under the premises, each subquestion has a true answer if the question has one, and each answer to a subquestion narrows the answers to the question [wisniewski2013] [hintikka1999] [hintikka2007] |
| `question-selection` | choose the question to pursue among several candidates | each candidate is stated with its significance, its tractability and its dependence on other questions, and the candidates are compared on these grounds [laudan1977] |

## Distinctions

- **Problematization and constraint specification share their output and differ in their norm.** Problematization states the demand and the constraints visible in a source. Constraint specification adds conditions that follow from background laws. These conditions may remain implicit in the statement of a problem [nickles1981].
- **Question formulation and subject identification differ in commitment.** Formulation types each slot of the question by a placeholder. Identification fixes the referent of each slot. The quantities of each referent are declared later, by [delimitation](model-building.md).
- **Decomposition and selection both output a question, under different norms.** The norm of decomposition is a logical relation between a question and its subquestions. The norm of selection compares candidate questions on pragmatic grounds, since problems differ in importance [laudan1977].

## Relations to the method

- **Decomposition links a subquestion to its question.** The [governing criterion of a decomposition](../inquiry/question-decomposition.md#^governing-criterion) admits a serving question only when resolving it changes the status of the question that it serves.

The fields filled by these activities are documented in the [problem record](../../specification/problem.md), in the [question record](../../specification/question.md) and in the [subject of a question](../../specification/question-subject.md).

---
## Sources

Marks follow the [legend of reading marks](../../../CONTRIBUTING.md#^reading-marks).

- [belnap1976] ◐ [Belnap & Steel, *The Logic of Questions and Answers*, Yale University Press, 1976](https://search.worldcat.org/search?q=bn:0300019629); checked through library records and published reviews
- [dewey1938] ◐ [Dewey, *Logic: The Theory of Inquiry*, Henry Holt, 1938](https://search.worldcat.org/oclc/229987); ch. 6, "The pattern of inquiry": a problem is formulated from an indeterminate situation, checked through secondary summaries
- [hamblin1958] ◐ [Hamblin, "Questions", *Australasian Journal of Philosophy* 36(3), 159–168, 1958](https://philpapers.org/rec/HAMQ); the postulates that an answer is a statement and that the possible answers form an exhaustive set of mutually exclusive possibilities, checked through secondary summaries
- [hintikka1999] ◐ [Hintikka, *Inquiry as Inquiry: A Logic of Scientific Discovery*, Kluwer, 1999](https://doi.org/10.1007/978-94-015-9313-7)
- [hintikka2007] ◐ [Hintikka, *Socratic Epistemology: Explorations of Knowledge-Seeking by Questioning*, Cambridge University Press, 2007](https://doi.org/10.1017/CBO9780511619298)
- [laudan1977] ◐ [Laudan, *Progress and Its Problems: Towards a Theory of Scientific Growth*, University of California Press, 1977](https://www.ucpress.edu/books/progress-and-its-problems/paper); empirical and conceptual problems, and the weighting of problems by importance, checked through the publisher page and secondary summaries
- [nickles1981] ◐ [Nickles, "What is a problem that we may solve it?", *Synthese* 47(1), 85–118, 1981](https://doi.org/10.1007/BF01064267); §V, p. 109: a problem consists of the constraints on the solution plus the demand that a solution be found
- [vanfraassen1980] ◐ [van Fraassen, *The Scientific Image*, Clarendon Press, 1980](https://doi.org/10.1093/0198244274.001.0001); ch. 5: topic, contrast class and relevance relation of a why-question
- [wisniewski2013] ◐ [Wiśniewski, *Questions, Inferences, and Scenarios*, Studies in Logic 46, College Publications, 2013](https://philpapers.org/rec/WINQIA); erotetic implication of a question by a question and a set of declarative sentences
