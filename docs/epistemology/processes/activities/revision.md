---
tags:
  - theory
  - wip
index: "[Epistemic activities](docs/epistemology/processes/activities/_index.md)"
aliases:
  - Revision activities
  - Belief revision (activity)
  - Theory change
  - Framework revision
---
# Revision

> [!QUESTION] Goal: which activities change the attitude or the status of existing records, and by which norm is each judged?

The activities of this family output a **change of knowledge state**: a change of the attitude or of the status of existing records, motivated by verdicts. A new model is never such an output, as the [partition of the families](epistemic-activities.md#^families) states. Each activity of this family is typed by its [signature](epistemic-activities.md#^activity-criterion).

## Signatures

| Activity | Inputs | Output | Mode | Context |
| --- | --- | --- | --- | --- |
| `belief-revision` | `verdict \| credence \| ranking` | `knowledge-state-change` | deductive | justification |
| `theory-change` | `verdict` (several) | `knowledge-state-change` | non-inferential | justification |
| `framework-revision` | `verdict` (several) | `knowledge-state-change` | non-inferential | both |

## Norms

| Activity | Operation | The test `norm.<activity-id>` passes when |
| --- | --- | --- |
| `belief-revision` | expand, contract or revise the accepted knowledge $K$, once the researcher accepts or retracts a claim in response to a verdict, a credence or a ranking | the change is minimal: it satisfies the postulates of base revision, the axioms that a rational change of a belief base must satisfy, among them that a claim of the base is given up only when it contributes to the conflict being removed [hansson1999] |
| `theory-change` | replace a theory, or modify the auxiliary hypotheses that protect its core, in response to anomalies | the successor explains the previous successes of its predecessor, predicts novel facts, and has some of these predictions corroborated [lakatos1970] |
| `framework-revision` | replace the framework that fixes how questions are posed and answered | the external question of adopting the framework is settled as a practical decision, by stated pragmatic criteria [carnap1950_empiricism] |

## Distinctions

- **The norm of belief revision is base revision.** The postulates of Alchourrón, Gärdenfors and Makinson (AGM) govern belief sets, closed under logical consequence [alchourron1985] [gardenfors1988]. The accepted knowledge $K$ of an inquiry is a belief base: a finite set of accepted claims, not closed under consequence. The method therefore adopts the postulates of base revision, which keep apart a claim accepted for itself and a claim that only follows from accepted claims [hansson1999].
- **Revision of beliefs and change of theory differ in their unit.** Belief revision changes a set of claims in response to one input claim. Theory change concerns structured wholes, such as a hard core protected by a belt of auxiliary hypotheses [lakatos1970]. Theory change has no accepted set of postulates comparable to those of belief revision.
- **The norm of theory change is contested.** The norm adopted here requires corroborated novel predictions [lakatos1970]. On a rival account, the successor must resolve some recognized anomaly and preserve much of the problem-solving ability of its predecessor [kuhn1962]. On another, the new conceptual system must have greater explanatory coherence than the old one [thagard1992].
- **Theory change and framework revision differ in the question settled.** A theory changes inside a framework, under the standards of that framework. A framework changes by a decision about which framework to adopt, a question external to every framework [carnap1950_empiricism].

## Relations to the method

- **A revision changes the attitude of an answer.** The content of the answer stays fixed, whereas the attitude of the inquiry toward it moves among entertaining, hypothesizing, accepting and retracting it. Accepting or retracting is a decision of the researcher, informed by the verdicts, the disposition and the credence of the assessment, as the [act of acceptance](../../foundations/inquiry-and-state.md#^acceptance-act) states, and the revision records that decision.
- **The warrant of a law fixes the order of revision.** When new evidence arrives, posited, fitted or measured laws are revised first, as the [warrant of a background law](../../objects/knowledge/background.md#^law-warrant) states.
- **Formal models of epistemic change are surveyed in this method.** The [formal models of belief change](../../../references/belief-revision-dynamic-epistemic-logic.md) state how an epistemic state changes under new information.

The field that records the attitude of an answer is documented in the [answer record](../../../specification/answer.md).

---
## Sources

Marks follow the [legend of reading marks](../../../../CONTRIBUTING.md#^reading-marks).

- [alchourron1985] ◐ [Alchourrón, Gärdenfors & Makinson, "On the logic of theory change: partial meet contraction and revision functions", *Journal of Symbolic Logic* 50(2), 510–530, 1985](https://doi.org/10.2307/2274239); full meet contraction gives up more claims than needed and motivates partial meet contraction; from standard knowledge, not checked at the page
- [carnap1950_empiricism] ◐ [Carnap, "Empiricism, semantics, and ontology", *Revue Internationale de Philosophie* 4(11), 20–40, 1950](https://plato.stanford.edu/entries/carnap/); an external question, about a framework itself, is a practical question of deciding among frameworks, checked through the SEP entry, §7
- [gardenfors1988] ◐ [Gärdenfors, *Knowledge in Flux: Modeling the Dynamics of Epistemic States*, MIT Press, 1988](https://nantilus.univ-nantes.fr/vufind/Record/PPN002033690)
- [hansson1999] ◐ [Hansson, *A Textbook of Belief Dynamics: Theory Change and Database Updating*, Kluwer, 1999](https://doi.org/10.1007/978-94-007-0814-3); belief bases, as opposed to belief sets closed under consequence, and the postulates of base revision
- [kuhn1962] ◐ [Kuhn, *The Structure of Scientific Revolutions*, University of Chicago Press, 1962](https://en.wikipedia.org/wiki/The_Structure_of_Scientific_Revolutions); ch. 12, conditions on a candidate paradigm; from standard knowledge, not checked at the page
- [lakatos1970] ◐ [Lakatos, "Falsification and the methodology of scientific research programmes", in Lakatos & Musgrave (eds.), *Criticism and the Growth of Knowledge*, Cambridge University Press, 91–196, 1970](https://doi.org/10.1017/CBO9781139171434.009); the three conditions of sophisticated falsification, checked through reproductions of the text
- [thagard1992] ◐ [Thagard, *Conceptual Revolutions*, Princeton University Press, 1992](https://wellcomecollection.org/works/cja3cv87)
