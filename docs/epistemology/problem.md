---
role: definition
status: wip
index: "[Epistemology](docs/epistemology/_index.md)"
aliases:
  - Specifying the problem
  - Problem record
tags: []
source:
---
# Specifying the problem

> [!QUESTION] Goal: what must be fixed about a research problem before any question is posed to serve it?

The problem record states a research problem: a demand that a result be found, with the constraints that a result must satisfy to count as a solution [nickles1981]. A problem fixes no set of answers, so it is not yet a question. The distinction between the two is defined in the note on the [epistemic problem](definitions/epistemic-problem.md#^problem-vs-question), and the levels of commitment of a question in the note on [problems and questions](definitions/problem-and-question.md#^commitment-levels). When a problem record exists, the questions serving the problem name it in their field `addresses`. One problem can motivate several questions.

| Specification | When it is required | Options or frame | Examples | Source |
| ------------- | ------------------- | ---------------- | -------- | ------ |
| Statement | always | "[the result sought], [the obstacle to obtaining it]", as a reading | "overparameterized networks fit their training data long before they generalize, and no account states what produces the delay" | — |
| Kind | always | empirical, when the problem concerns the objects of a domain · conceptual, when it concerns the consistency of a theory or its fit with other theories | the delay before generalization (empirical); two accounts of representation that assign incompatible roles to one quantity (conceptual) | [laudan1977]; [senses of problem](definitions/epistemic-problem.md) |
| Demand | always | "[the result required of a solution]" | an account that names the determinants of the delay and derives its duration from them | [nickles1981] |
| Constraints | when a condition beyond the demand delimits the solutions | per constraint, a name, the condition that a solution must satisfy, and the source that imposes it: a result, an admitted law or a publication | a solution derives the delay from the admitted training laws; a solution separates delayed generalization from persistent memorization | [nickles1981] |
| Explicanda | when the statement uses a term before any record fixes its sense | per term, the term as used and a pointer to the data, the result or the publication that fixes its use | "generalization", pointing to the threshold on the test loss | [carnap1950_logical] |
| Sources | when a publication, a data set or an anomaly raises the problem | per source, a pointer | the article that reports the delay | — |
| Significance | when a solution would change other work | the consequences of a solution for other work | whether the time to generalize can be predicted from the early training | — |

- **A constraint carries its source, so the constraint can be checked.** A constraint excludes some candidate solutions before any of them is proposed. A constraint drawn from an admitted law is checked against the [background record](background.md) that admits the law. A constraint drawn from a publication is checked against that publication. Constraints derived from background laws are added by the activity `constraint-specification`, typed among the [problem-posing activities](definitions/activities/problem-posing.md). ^constraint-source

- **An explicandum names a term still to be made exact by the inquiry.** A problem is often stated in terms whose sense is fixed only by their use, such as "generalization" or "representation". The record keeps the term with a pointer to that use. A later record replaces the explicandum by an exact concept, as an explication replaces an explicandum by an explicatum [carnap1950_logical]. *Example*: the explicandum "representation geometry" is replaced by a kernel over the inputs, declared in a phenomenon at commitment `specified`. ^explicanda

- **A problem ends in one of three ways.** A problem is `solved` when an accepted answer to its questions meets the demand under the constraints. A problem is `dissolved` when a revision shows that its demand rests on a false presupposition, so no solution is needed. A problem is `abandoned` when the inquiry stops without either outcome.

*Example*: the [problem of delayed generalization](../../examples/grokking-delayed-generalization/problem.yml) is an empirical problem, with two constraints and one explicandum, and its question names the problem in its field `addresses`.

---
## Sources

Marks follow the [legend of reading marks](../../CONTRIBUTING.md#^reading-marks).

- [carnap1950_logical] ◐ Carnap, *Logical Foundations of Probability*, University of Chicago Press, 1950, ch. 1; explicandum, explicatum and the four requirements on an explication, checked through the [Stanford Encyclopedia of Philosophy](https://plato.stanford.edu/entries/carnap/)
- [laudan1977] ◐ [Laudan, *Progress and Its Problems: Towards a Theory of Scientific Growth*, University of California Press, 1977](https://www.ucpress.edu/books/progress-and-its-problems/paper); the distinction between empirical and conceptual problems, checked through secondary sources
- [nickles1981] ◐ [Nickles, "What is a problem that we may solve it?", *Synthese* 47(1), 85–118, 1981](https://doi.org/10.1007/BF01064267); pp. 109–112, a problem as constraints together with a demand, checked through a scanned copy of poor quality
