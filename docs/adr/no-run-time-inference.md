---
tags:
  - decision
index: "[Architecture decisions](docs/adr/_index.md)"
aliases:
  - No inference at run time
---
# No inference at run time

> [!QUESTION] Goal: which results may a tool of `gnomon` compute from the records, and which results must the researcher author?

The tools of `gnomon` read records and compute: they resolve symbols, collect the symbol table of a problem, and find the cycles among the steps of an itinerary. Two further computations are specified: the [comparison](../epistemology/answer/model-and-binding.md#^comparison) of a binding with data, which the [decision on answers, models and bindings](answers-models-bindings.md) states is computed, and the [open conditions](../epistemology/inquiry/next-act.md#^open-condition) of a question. Several proposals would let a tool go further and derive claims that the records do not state: a logic-programming layer, a reasoner that classifies records, an engine that computes the acceptance of arguments. The [decision on expression syntax](expression-syntax.md) already excludes proving the claims of an inquiry. No decision drew the boundary between computing over records and inferring.

## Decision

The tools of `gnomon` record and validate authored reasoning, and never infer. ^no-inference

A tool may compute a value that a declared rule fixes from authored records. The rule is declared in package data or in a method note, two runs on the same records return the same value, and the value is reported or written to a generated output, never into an authored record. ^admitted-computation

A tool never adds a claim, a relation or a record kind that no record states. A tool never evaluates whether a warrant holds, and never decides whether an answer is accepted. The verdict of a warrant test, the state of a condition and the acceptance of an answer are authored, with pointers to the records that support them. A tool may check that an authored verdict respects a declared rule, such as the [rules on the reports of a comparison](../epistemology/answer/satisfaction-conditions.md#^fidelity-reads-reports). ^excluded-inference

## Constraints that decide the boundary

- **A verdict on a warrant depends on content that no grammar fixes.** Whether a test was severe, or a definition eliminable, is judged by the researcher, so the [itinerary](../epistemology/inquiry/itinerary.md) records the verdict of each norm and its check reads only whether the verdict is admitted.
- **A derived claim needs an author.** A claim produced by an engine changes the claims that the records warrant without any edit to them, so no [revision](revision-accountability.md#^traceable-revision) traces the change.
- **A computed value must be reproducible from the records.** A comparison is [recomputed, never edited](../epistemology/answer/model-and-binding.md#^comparison-recomputed), so its rule and its inputs fix its output.

## Options weighed

| Option | Benefit | Reason it is not taken alone |
| ------ | ------- | ---------------------------- |
| A logic-programming layer, such as backward chaining in Prolog [kowalski1974] | Queries over the relations derive facts that no record states | A derived fact has no author and no revision trace, and the relations that the layer would query are already authored, so a traversal of them answers the same queries |
| A description-logic reasoner for classification, satisfiability and entailment [baader2003] | The kind of a record and the consistency of the corpus follow from declared properties | The kind of a record is authored, and a classification would change it without any edit. The static constraints of description logics stay admitted as checks, such as the [typed ends of a relation](closed-typed-relations.md#^typed-ends) |
| An argumentation engine computing grounded, preferred or stable acceptance [dung1995] | The status of each answer follows from its attacks and supports | The assessment decides acceptance, and a computed status would change whenever an attack is added. The authored relations `supports` and `defeats` stay admitted |
| An engine that updates the records resting on a revised record | Each dependent stays consistent with its premises | The update edits authored records, whereas the [decision on revision accountability](revision-accountability.md#^flag-not-edit) leaves each dependent to the researcher |
| No computation over records beyond resolution | No boundary to state | The comparison, the open conditions and the lookup of dependents each require a computation fixed by a declared rule |
| Computations fixed by declared rules over authored records, and nothing else | Every computed value is reproducible, and every judgment has an author | A computation that needs a judgment stays manual, even where an engine could propose a result |

## Consequences

- A traversal of authored relations, such as a lookup of the records resting on a unit, is a computation fixed by a rule. Its result is reported and never stored as a relation that a record asserts.
- The visible symbols of a derived model are a [set operation over declarations](../audits/model-design-synth.md#^div-content), so a tool may compute them.
- The command `gnomon status` is to list the open conditions computed from the recorded states of the conditions, never from a state that it infers.
- An inference engine stays outside `gnomon`, as a separate tool reading the records. Its outputs enter the records only as authored content, with their origin.

---
## Sources

Marks follow the [legend of reading marks](../../CONTRIBUTING.md#^reading-marks). A mark ◐ records a check of the bibliographic record.

- [baader2003] ◐ Baader, Calvanese, McGuinness, Nardi & Patel-Schneider (eds.), *The Description Logic Handbook: Theory, Implementation, and Applications*, Cambridge University Press, 2003
- [dung1995] ◐ Dung, "On the acceptability of arguments and its fundamental role in nonmonotonic reasoning, logic programming and n-person games", *Artificial Intelligence* 77(2), 321–357, 1995
- [kowalski1974] ◐ Kowalski, "Predicate logic as programming language", in *Proceedings of the IFIP Congress 74*, North-Holland, 569–574, 1974
