---
tags:
  - theory
  - wip
index: "[Problem](docs/epistemology/objects/problem/_index.md)"
aliases:
  - Epistemic problem
  - Problem
  - Minimal problem
---
# Epistemic problem

> [!QUESTION] Goal: when does a situation of inquiry count as a problem, how is a problem stated so that its solution can be checked, and how does a problem differ from a question?

An **epistemic problem** is a demand for a result that the accepted knowledge does not yet deliver, together with the conditions that the result must meet [nickles1981] [laudan1977]. *Example*: some networks generalize long after they have fitted their training data, and no accepted account derives the duration of that delay. The demand is an account of the delay. One condition on the account is that it derive the delay from the admitted training laws.

A problem is relative to the accepted knowledge of an [inquiry](../../foundations/inquiry-and-state.md). The same demand ceases to be a problem once an accepted result meets it. The demand becomes a problem again when a revision withdraws that result.

## Senses

| Term | Community | Definition | Source |
| --- | --- | --- | --- |
| Problem | pragmatism | an indeterminate situation, made problematic by the inquiry that addresses it | [dewey1938] |
| Empirical and conceptual problems | philosophy of science | an empirical problem concerns the objects of a domain; a conceptual problem concerns a theory, such as an inconsistency within it or a tension with other accepted theories | [laudan1977] |
| Problem | philosophy of science | a demand that a result be found, together with the constraints that the result must satisfy | [nickles1981] |
| Problem to find, problem to prove | mathematical heuristics | a problem to find has an unknown, data and a condition; they correspond to the type of result, the accepted knowledge and the constraints below; a problem to prove has a hypothesis and a conclusion | [polya1945] |
| Problem and its solution | logic of problems | a task whose solution is a construction; one problem reduces to another when a method turns every solution of the second into a solution of the first | [kolmogorov1932]; [medvedev1955] |
| Evocation of a question | erotetic logic | a set of statements evokes a question when the set entails that the question has a true answer and entails none of its direct answers | [wisniewski1995] |

## Formal statement

A problem is the triple ^problem-triple

$$\pi=\langle K,\ d,\ \Phi\rangle .$$

Each component answers one question about the problem: relative to which knowledge, for which result, and under which conditions. The symbols are registered in the [notation](../../vocabulary/notation/notation.md).

### The accepted knowledge $K$

$K$ is the **accepted knowledge** of the inquiry, the component of its [state](../../foundations/inquiry-and-state.md#^state) relative to which the problem is posed: a finite belief base of claims accepted by an act, not a set closed under logical consequence [hansson1999]. The corpus of accepted knowledge plays the same role in the epistemology of inquiry [levi1980]. A conflict between $K$ and a publication whose claims are not accepted is asserted with a pointer to that publication, and the [types of problem](problem-types.md) classify it as a conflict: a datum not yet accepted that is improbable under $K$. The term *background* is reserved for the [background record](../knowledge/background.md) of a target, which holds the laws admitted about it. An admitted law is taken as a premise of the inquiry, and it need not belong to $K$.

The problem is stated with the two relations that the [state of an inquiry keeps apart](../../foundations/inquiry-and-state.md#^obtained-accepted). A claim $s$ is **obtained**, written $\mathrm{Obt}_{\mathcal{M}}(s)$, when the **available means** $\mathcal{M}$, the methods, data, instruments and proof techniques that can be applied, have yielded it. A claim is **accepted**, written $s\in K$, when the researcher has accepted it. A claim obtained but not yet accepted, such as a derived result that awaits its assessment, is a proposed candidate, a member of $H$.

> [!IMPORTANT] Problems to prove
> Under plain logical consequence, a set $K$ containing the laws of a formal model would already contain every theorem about that model, so no problem to prove could arise. A theorem enters $K$ only once the means have yielded it and the researcher has accepted it. Therefore, an unproven theorem remains a gap, and a problem to prove can exist.

### The proposed candidates $H$

Beside $K$, the inquiry holds a set $H$ of **proposed candidates**: answers put forward and not yet accepted, such as two rival accounts of the delay. A candidate enters $K$ only through the [act of acceptance](../status/statuses-and-acceptance.md#^acceptance-act) of the researcher, which its [assessment](../answer/satisfaction-conditions.md) informs without computing it. A claim without support can still serve as a premise: the researcher admits it as a working assumption under the warrant `posited`, and the admission does not make it a member of $K$. ^candidates

### The demand $d$

The demand states the result sought:

$$d=\langle\mathsf{type},\ \mathsf{req},\ \Xi\rangle .$$

- $\mathsf{type}$, the **type of result**: one of the [product types](../../processes/activities/epistemic-activities.md#^product-types), such as a phenomenon, a model, a consequence, an explanation or a concept.
- $\mathsf{req}$, the **request**: how many results, and of which completeness, the demand asks for. The request takes one of four values:
  - `one`: one result suffices (find one network that implements a given input–output map);
  - `all`: every result is required (characterize all the fixed points of a network);
  - `over-a-parameter`: a result for each value of a parameter (the fixed points as the gain varies);
  - `verdict`: a decision on candidates already proposed (is a proposed account of the delay correct?). In that case, the type of result is the type of the candidates. This value of the request is distinct from the verdict of a test, which an assessment returns.
- $\Xi$, the **explicanda**: the terms of the demand still in use without a definition. Each explicandum carries a pointer to the use that fixes its sense, such as "generalization" pointing to a threshold on the test loss [carnap1950_logical].

The request follows the distinction drawn in erotetic logic between the range of alternatives and the number and completeness of the alternatives that an answer must select [belnap1976].

### The constraints $\Phi$

The constraints are the conditions that any solution must meet, each with its source: a result, an admitted law or a publication [nickles1981]. Constraints come in two kinds:

- $\Phi_1$ applies to each candidate alone: *the account derives the delay from the admitted training laws*;
- $\Phi^*$ applies to the set of results: *the account is unique up to a change of parameters*.

## The question associated with a problem

Each problem defines an **associated question**: the question that asks for the demanded results, and only for them. ^associated-question

$$Q_\pi = \text{which } s \text{ of type } \mathsf{type} \text{ satisfies } \Phi_1,\ \text{under the request } \mathsf{req}\ ?$$

In words: the associated question asks for results of the demanded type that meet the conditions on each candidate. Its [possible answers](../question/question.md#^answer-sets) are propositions of the form "$s$ is a result of type $\mathsf{type}$ that satisfies $\Phi_1$". The request fixes how many such propositions a direct answer must assert, and how completely. Whether-questions and which-questions are both elementary questions, with the same subject and request, so this form covers both [belnap1976]. ^presuppositions

The associated question carries two kinds of presupposition:

- its **existence presupposition**: at least one result of the demanded type meets the conditions on each candidate;
- its **topic presupposition**, when the demand concerns a fact, such as an explanation of a phenomenon: the fact holds, as a why-question presupposes that its topic is true [vanfraassen1980].

The problem **exists** while its demand is unmet: no direct answer of $Q_\pi$ is in $K$, so that $a\notin K$ for every direct answer $a$. ^problem-existence

The problem has an **epistemic gap** when, in addition, the existence presupposition is in $K$, so that $K$ **evokes** the question: ^gap

$$\exists s\,\big(\mathsf{type}(s)\wedge\Phi_1(s)\big)\in K\qquad\text{and}\qquad a\notin K\ \text{ for every direct answer } a \text{ of } Q_\pi .$$

In words: the researcher has accepted that a result of the demanded type exists, and has accepted no direct answer that gives such a result. This pair of conditions is the **epistemic gap** of the problem. The condition adapts Wiśniewski's evocation, which uses logical entailment from the premises [wisniewski1995]. In both clauses, entailment from $K$ is replaced by membership of $K$. The second clause therefore departs further from evocation than a change of consequence relation: an answer that follows from $K$, or that a run has obtained without its being accepted, $\mathrm{Obt}_{\mathcal{M}}(a)$ with $a\notin K$, leaves the gap open.

*Example*: suppose that an accepted proof derives the existence of fixed points from the admitted dynamics of a class of recurrent networks, while no available analysis gives their number at a given gain. Under that supposition, $K$ evokes the question "how many fixed points does a network of the class have at each gain?".

## How a problem ends

A problem ends in one of three ways, and the [problem record](../../../specification/problem.md) fixes their record values. Two of the three ways have a formal condition: ^problem-outcomes

- **Solved**: a candidate of the demanded type meets the constraints and the request, and the researcher has accepted it, which moves it from $H$ into $K$.
- **Dissolved**: the revised accepted knowledge holds the negation of a presupposition of $Q_\pi$, its existence presupposition or its topic presupposition. No result of the demanded kind exists, so no solution is needed. *Example*: the delay appears only in a thresholded accuracy, while the test loss falls from the start of training. In that case, no delay of learning exists, and the problem of explaining it dissolves.
- **Abandoned**: the inquiry stops before the problem is solved or dissolved. No formal condition defines this outcome, which records a decision of the researcher.

## Every inquiring question presupposes a problem

A question asked in order to learn its answer presupposes that its asker lacks that answer. Epistemic analyses of questions build this lack into the meaning of a question: they read a question as the request "bring it about that I know …" [aqvist1965] [hintikka1976]. Attitudes directed at a question, such as inquiring into it, are incompatible with knowing its answer [friedman2013]. ^question-presupposes-problem

The question also presupposes that it has an answer. In the interrogative model of inquiry, a question may be *asked*, that is, put to a source, only once its presupposition is established [hintikka2007]. A question can be *posed* before that point, and its presuppositions then remain to be established, which is the condition of soundness among the [conditions of answerability](../question/conditions-of-answerability.md). Once its existence presupposition is in $K$, $K$ evokes the question.

Therefore, every inquiring question $Q$ carries a **minimal problem**: ^minimal-problem

$$\pi_Q=\langle K,\ d_Q,\ \Phi_Q\rangle .$$

The demand $d_Q$ takes the type of result and the request of $Q$. Its explicanda $\Xi_Q$ are the terms of $Q$ that enter by their anchored use rather than as typed slots. The constraints $\Phi_Q$ carry the remaining specifications of $Q$ as conditions on each candidate: its subject, its contrast and its [epistemic task](../task/epistemic-task.md). The associated question of $\pi_Q$ is therefore $Q$ itself. In words: the minimal problem of a question states that its answer is lacking, so it exists for every inquiring question. The minimal problem has an epistemic gap once the existence presupposition of $Q$ is in $K$.

> [!NOTE] Questions outside inquiry
> The asker of an examination question or of a rhetorical question already holds the answer. Such a question carries no minimal problem and serves no inquiry.

A question can also carry more than a gap. A question of the form "why does a claim hold *despite* an expectation drawn from another claim?" presupposes a conflict between the claim and the expectation. *Example*: "why do overparameterized networks generalize despite their capacity to memorize random labels?" presupposes a conflict between the observed generalization and the expectation drawn from capacity [zhang2017]. The [types of problem](problem-types.md) classify such obstacles.

## Problem and question

A problem and a question are distinct objects: ^problem-vs-question

| | Problem | Question |
| --- | --- | --- |
| States | a demand, the accepted knowledge relative to which the demand is unmet, and the constraints on a solution | a set of possible answers, and the request on how many of them an answer selects [hamblin1958] [belnap1976] |
| Possible answers are | results of a type (models, concepts, consequences …) | propositions; for the associated question, the propositions "$s$ is a result of type $\mathsf{type}$ that satisfies $\Phi_1$" |
| Number | one problem motivates one or several questions | one question serves one or several problems |

Two relations connect them:

- A question **serves** a problem when, given $K$, two conditions hold. First, the question has a true answer whenever the associated question $Q_\pi$ has one. Second, each answer to the question narrows the candidate answers of $Q_\pi$. Formally, $Q_\pi$ implies the question on the basis of $K$, in the sense of erotetic implication [wisniewski1995].
- A question **formulates** a problem when it serves the problem and a true complete answer to it yields a solution.

*Example*: "does the delay of generalization shrink when weight decay grows?" serves the problem of the delay, since each answer narrows the candidate accounts. The question "which mechanism, among those compatible with the training laws, fixes the duration of the delay?" formulates the problem.

## Subproblems

A problem $\pi_1$ **reduces** to a problem $\pi_2$ when a recorded method turns every solution of $\pi_2$ into a solution of $\pi_1$ [kolmogorov1932]. The method must be recorded: otherwise $\pi_1$ would reduce to every problem as soon as some solution of $\pi_1$ exists, known or not. The method must also be uniform, so that one procedure applies to every solution of $\pi_2$ [medvedev1955]. ^reduction

Reduction can be conjunctive: $\pi_1$ reduces to $\pi_2$ and $\pi_3$ together when the method needs a solution of each. *Example*: a property of every network of a class reduces to the same property for the linear networks of the class, together with a bound on the effect of the nonlinearity.

## Distinctions

- **A gap is not a problem, and a problem need not have a gap.** A problem exists while its demand is unmet, and it has a gap when the existence presupposition is also in $K$. The gap states a lack, whereas the problem adds the demand and its constraints, which fix the result that would fill the gap.
- **The explicanda of a problem and the placeholders of a question fix a term along two different dimensions.** An explicandum of a problem is *anchored*: a pointer fixes its use, and no type is given. A [placeholder](../question/question.md#^question-schema) is *typed*: its kind is fixed, and no referent is given. The level `identified` of a slot fixes both the type and the referent.
- **The request is not the aim.** The request fixes how many results, and how complete, the demand asks for. The [epistemic aim](../task/epistemic-aim.md) fixes the kind of knowledge that a question seeks.
- **"Epistemic problem" names the problem defined here.** The [epistemic task](../task/epistemic-task.md) of a question fixes the kind of knowledge that its answer must deliver. The task belongs to the question, not to the problem.

The fields by which a record states a problem are documented in the [problem record](../../../specification/problem.md).

---
## Sources

Marks follow the [legend of reading marks](../../../../CONTRIBUTING.md#^reading-marks).

- [aqvist1965] ◐ Åqvist, *A New Approach to the Logical Theory of Interrogatives. Part I: Analysis*, Filosofiska föreningen i Uppsala, 1965; a question as a command to bring it about that the speaker knows the answer, checked through [Harrah's review](https://doi.org/10.2307/2270810) and the [SEP entry on questions](https://plato.stanford.edu/entries/questions/)
- [belnap1976] ◐ [Belnap & Steel, *The Logic of Questions and Answers*, Yale University Press, 1976](https://catalogue.bnf.fr/ark:/12148/cb353871722); the subject of a question and its request, fixing the number and the completeness of the answers selected
- [carnap1950_logical] ◐ Carnap, *Logical Foundations of Probability*, University of Chicago Press, 1950, ch. 1; explicandum and explicatum, checked through the [Stanford Encyclopedia of Philosophy](https://plato.stanford.edu/entries/carnap/)
- [dewey1938] ◐ [Dewey, *Logic: The Theory of Inquiry*, Henry Holt, 1938](https://search.worldcat.org/oclc/229987); ch. 6; checked through secondary sources
- [friedman2013] ◐ [Friedman, "Question-directed attitudes", *Philosophical Perspectives* 27, 145–174, 2013](https://doi.org/10.1111/phpe.12026); attitudes directed at a question are incompatible with knowing its answer, checked through secondary sources
- [hamblin1958] ◐ [Hamblin, "Questions", *Australasian Journal of Philosophy* 36(3), 159–168, 1958](https://doi.org/10.1080/00048405885200211); checked through secondary sources
- [hansson1999] ◐ [Hansson, *A Textbook of Belief Dynamics: Theory Change and Database Updating*, Kluwer, 1999](https://doi.org/10.1007/978-94-007-0814-3); belief bases, as opposed to belief sets closed under consequence
- [hintikka1976] ◐ Hintikka, *The Semantics of Questions and the Questions of Semantics: Case Studies in the Interrelations of Logic, Semantics, and Syntax*, Acta Philosophica Fennica 28(4), North-Holland, 1976; the desideratum of a question, "bring it about that I know …"
- [hintikka2007] ◐ [Hintikka, *Socratic Epistemology: Explorations of Knowledge-Seeking by Questioning*, Cambridge University Press, 2007](https://doi.org/10.1017/CBO9780511619298); a question may be asked only once its presupposition is established
- [kolmogorov1932] ◐ Kolmogorov, "Zur Deutung der intuitionistischen Logik", *Mathematische Zeitschrift* 35, 58–65, 1932; problems, solutions and reducibility, checked through [Rodin's review of the calculus of problems](https://arxiv.org/abs/2307.09202)
- [laudan1977] ◐ [Laudan, *Progress and Its Problems: Towards a Theory of Scientific Growth*, University of California Press, 1977](https://www.ucpress.edu/books/progress-and-its-problems/paper); empirical and conceptual problems, checked through secondary sources
- [levi1980] ◐ Levi, *The Enterprise of Knowledge: An Essay on Knowledge, Credal Probability, and Chance*, MIT Press, 1980; the corpus of knowledge relative to which inquiry proceeds
- [medvedev1955] ◐ Medvedev, "Degrees of difficulty of mass problems", *Doklady Akademii Nauk SSSR* 104, 501–504, 1955; uniform reducibility of problems, checked through the Encyclopedia of Mathematics entry ["Finitary problem"](https://encyclopediaofmath.org/wiki/Finitary_problem)
- [nickles1981] ◐ [Nickles, "What is a problem that we may solve it?", *Synthese* 47(1), 85–118, 1981](https://doi.org/10.1007/BF01064267); a problem as a demand together with constraints, checked through a scanned copy of poor quality
- [polya1945] ◐ Pólya, *How to Solve It: A New Aspect of Mathematical Method*, Princeton University Press, 1945; the unknown, the data and the condition, and problems to find against problems to prove
- [vanfraassen1980] ◐ [van Fraassen, *The Scientific Image*, Clarendon Press, 1980](https://doi.org/10.1093/0198244274.001.0001); the topic of a why-question presupposed true; ch. 5, read in its abridged reprint, "The pragmatic theory of explanation", in Pitt (ed.), *Theories of Explanation*, Oxford University Press, 1988, 136–155 ([PDF](https://www.fitelson.org/290/vanfraassen_pte.pdf))
- [wisniewski1995] ◐ [Wiśniewski, *The Posing of Questions: Logical Foundations of Erotetic Inferences*, Kluwer, 1995](https://doi.org/10.1007/978-94-015-8406-7), ch. 5 on the evocation of questions; both definitions, evocation and erotetic implication, checked through [Wiśniewski, "Erotetic logic and explanation by abnormic hypotheses"](https://www.bu.edu/wcp/Papers/Logi/LogiWisn.htm)
- [zhang2017] ◐ [Zhang, Bengio, Hardt, Recht & Vinyals, "Understanding deep learning requires rethinking generalization", *International Conference on Learning Representations*, 2017](https://arxiv.org/abs/1611.03530)
