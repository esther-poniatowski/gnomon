---
tags:
  - definition
  - wip
index: "[Problems and questions](docs/epistemology/definitions/inquiry/_index.md)"
aliases:
  - Epistemic problem
  - Problem
  - Minimal problem
---
# Epistemic problem

> [!QUESTION] Goal: when does a situation of inquiry count as a problem, how is a problem stated so that its solution can be checked, and how does a problem differ from a question?

An **epistemic problem** is a demand for a result that the accepted knowledge does not yet deliver, together with the conditions that the result must meet [nickles1981] [laudan1977]. *Example*: some networks generalize long after they have fitted their training data, and no accepted account derives the duration of that delay. The demand is an account of the delay. One condition on the account is that it derive the delay from the admitted training laws.

A problem is relative to a state of knowledge. The same demand ceases to be a problem once an accepted result meets it. The demand becomes a problem again when a revision withdraws that result.

## Senses

| Term | Community | Definition | Source |
| --- | --- | --- | --- |
| Problem | pragmatism | an indeterminate situation, made problematic by the inquiry that addresses it | [dewey1938] |
| Empirical and conceptual problems | philosophy of science | an empirical problem concerns the objects of a domain; a conceptual problem concerns a theory, such as an inconsistency within it or a tension with other accepted theories | [laudan1977] |
| Problem | philosophy of science | a demand that a result be found, together with the constraints that the result must satisfy | [nickles1981] |
| Problem to find, problem to prove | mathematical heuristics | a problem to find has an unknown, data and a condition; they correspond to the type of result, the background and the constraints below; a problem to prove has a hypothesis and a conclusion | [polya1945] |
| Problem and its solution | logic of problems | a task whose solution is a construction; one problem reduces to another when a method turns every solution of the second into a solution of the first | [kolmogorov1932]; [medvedev1955] |
| Evocation of a question | erotetic logic | a set of statements evokes a question when the set entails that the question has a true answer and entails none of its direct answers | [wisniewski1995] |

## Formal statement

A problem is the triple ^problem-triple

$$\pi=\langle K,\ d,\ \Phi\rangle .$$

Each component answers one question about the problem: relative to which knowledge, for which result, and under which conditions. The symbols are registered in the [notation](../../language/notation.md).

### The background $K$

$K$ is the **background**: the finite set of accepted claims relative to which the problem is posed. In a research project, $K$ holds the accepted records of the project and the claims of the publications that these records cite. A conflict with a publication that no record cites is asserted with a pointer to it, which brings that publication into the scope of $K$. A finite set of this kind is a *belief base*, as opposed to a set closed under logical consequence [hansson1999]. The corpus of accepted knowledge plays the same role in the epistemology of inquiry [levi1980].

The background is paired with the **available means** $\mathcal{M}$: the methods, data, instruments and proof techniques that can be applied. The expression $K\vdash_{\mathcal{M}} s$ reads: *the claim $s$ has been obtained from $K$ by applying means of $\mathcal{M}$, and an assessment has accepted it*. The reading is actual, not dispositional: a claim that the means could yield, but have not yet yielded, is not obtained. A claim obtained but not yet accepted, such as a derived result that awaits its assessment, is a proposed candidate, a member of $H$.

> [!IMPORTANT] Claims obtained and accepted with the means
> Under plain logical consequence, a background containing the laws of a formal model already "contains" every theorem about that model, so no proof problem could arise. Relative to the means, a claim counts as known only once the available means have yielded it and an assessment has accepted it. Therefore, an unproven theorem remains a gap. Obtaining claims with the means is also *not explosive*: a local inconsistency in $K$ does not yield every claim.

### The proposed candidates $H$

Beside the background, the inquiry holds a set $H$ of **proposed candidates**: answers put forward and not yet accepted, such as two rival accounts of the delay. A candidate enters $K$ only when its assessment accepts it. A claim without support enters $K$ only by a recorded decision of the researcher, as a working assumption under the warrant `posited`. ^candidates

### The demand $d$

The demand states the result sought:

$$d=\langle\mathsf{type},\ \mathsf{req},\ \Xi\rangle .$$

- $\mathsf{type}$, the **type of result**: one of the [product types](../activities/epistemic-activities.md#^product-types), such as a phenomenon, a model, a consequence, an explanation or a concept.
- $\mathsf{req}$, the **request**: how many results, and of which completeness, the demand asks for. The request takes one of four values:
  - `one`: one result suffices (find one network that implements a given input–output map);
  - `all`: every result is required (characterize all the fixed points of a network);
  - `over-a-parameter`: a result for each value of a parameter (the fixed points as the gain varies);
  - `verdict`: a decision on candidates already proposed (is a proposed account of the delay correct?). In that case, the type of result is the type of the candidates.
- $\Xi$, the **explicanda**: the terms of the demand still in use without a definition. Each explicandum carries a pointer to the use that fixes its sense, such as "generalization" pointing to a threshold on the test loss [carnap1950_logical].

The request follows the distinction drawn in erotetic logic between the range of alternatives and the number and completeness of the alternatives that an answer must select [belnap1976].

### The constraints $\Phi$

The constraints are the conditions that any solution must meet, each with its source: a result, an admitted law or a publication [nickles1981]. Constraints come in two kinds:

- $\Phi_1$ applies to each candidate alone: *the account derives the delay from the admitted training laws*;
- $\Phi^*$ applies to the set of results: *the account is unique up to a change of parameters*.

## The question associated with a problem

Each problem defines an **associated question**: the question that asks for the demanded results, and only for them. ^associated-question

$$Q_\pi = \text{which } s \text{ of type } \mathsf{type} \text{ satisfies } \Phi_1,\ \text{under the request } \mathsf{req}\ ?$$

In words: the associated question asks for results of the demanded type that meet the conditions on each candidate. The request fixes how many results an answer must give, and how complete they must be. A whether-question is a which-question over two alternatives, so this form covers it [belnap1976]. ^presuppositions

The associated question carries two kinds of presupposition:

- its **existence presupposition**: at least one result of the demanded type meets the conditions on each candidate;
- its **topic presupposition**, when the demand concerns a fact, such as an explanation of a phenomenon: the fact holds, as a why-question presupposes that its topic is true [vanfraassen1980].

The problem **exists** while its demand is unmet: no direct answer of $Q_\pi$ has been obtained and accepted, so that $K\nvdash_{\mathcal{M}} a$ for every direct answer $a$. ^problem-existence

The problem has an **epistemic gap** when, in addition, its background establishes the existence presupposition, so that the background **evokes** the question: ^gap

$$K\vdash_{\mathcal{M}} \exists s\,\big(\mathsf{type}(s)\wedge\Phi_1(s)\big)\qquad\text{and}\qquad K\nvdash_{\mathcal{M}} a\ \text{ for every direct answer } a \text{ of } Q_\pi .$$

In words: the accepted knowledge establishes that a result of the demanded type exists, and no such result has yet been obtained and accepted. This pair of conditions is the **epistemic gap** of the problem. The condition adapts Wiśniewski's evocation, which uses logical entailment [wisniewski1995]. Entailment is replaced by what the available means have obtained and an assessment has accepted. The second clause therefore states that no direct answer has been obtained and accepted, which departs further from evocation than a change of consequence relation: an answer that follows from $K$, or that a run has produced without an assessment, leaves the gap open.

*Example*: suppose that the admitted dynamics of a class of recurrent networks guarantee that fixed points exist, while no available analysis gives their number at a given gain. Under that supposition, the background evokes the question "how many fixed points does a network of the class have at each gain?".

## How a problem ends

A problem ends in one of three ways, and the [problem record](../../inquiry/problem.md) fixes their record values. Two of the three ways have a formal condition: ^problem-outcomes

- **Solved**: a candidate of the demanded type meets the constraints and the request, and its assessment has moved it from $H$ into $K$.
- **Dissolved**: the revised background yields the negation of a presupposition of $Q_\pi$, its existence presupposition or its topic presupposition. No result of the demanded kind exists, so no solution is needed. *Example*: the delay appears only in a thresholded accuracy, while the test loss falls from the start of training. In that case, no delay of learning exists, and the problem of explaining it dissolves.
- **Abandoned**: the inquiry stops before the problem is solved or dissolved. No formal condition defines this outcome, which records a decision of the researcher.

## Every inquiring question presupposes a problem

A question asked in order to learn its answer presupposes that its asker lacks that answer. Epistemic analyses of questions build this lack into the meaning of a question: they read a question as the request "bring it about that I know …" [aqvist1965] [hintikka1976]. Attitudes directed at a question, such as inquiring into it, are incompatible with knowing its answer [friedman2013]. ^question-presupposes-problem

The question also presupposes that it has an answer. In the interrogative model of inquiry, a question may be *asked*, that is, put to a source, only once its presupposition is established [hintikka2007]. A question can be *posed* before that point, and its presuppositions then remain to be established, which is the condition of soundness among the [conditions of answerability](conditions-of-answerability.md). Once the background establishes its existence presupposition, the background evokes the question.

Therefore, every inquiring question $Q$ carries a **minimal problem**: ^minimal-problem

$$\pi_Q=\langle K,\ d_Q,\ \Phi_Q\rangle .$$

The demand $d_Q$ takes the type of result and the request of $Q$. Its explicanda $\Xi_Q$ are the terms of $Q$ that enter by their anchored use rather than as typed slots. The constraints $\Phi_Q$ carry the remaining specifications of $Q$ as conditions on each candidate: its subject, its contrast and its [epistemic task](../../epistemic-task/epistemic-task.md). The associated question of $\pi_Q$ is therefore $Q$ itself. In words: the minimal problem of a question states that its answer is lacking, so it exists for every inquiring question. The minimal problem has an epistemic gap once the background establishes the existence presupposition of $Q$.

> [!NOTE] Questions outside inquiry
> The asker of an examination question or of a rhetorical question already holds the answer. Such a question carries no minimal problem and serves no inquiry.

A question can also carry more than a gap. A question of the form "why does a claim hold *despite* an expectation drawn from another claim?" presupposes a conflict between the claim and the expectation. *Example*: "why do overparameterized networks generalize despite their capacity to memorize random labels?" presupposes a conflict between the observed generalization and the expectation drawn from capacity [zhang2017]. The [types of problem](problem-types.md) classify such obstacles.

## Problem and question

A problem and a question are distinct objects: ^problem-vs-question

| | Problem | Question |
| --- | --- | --- |
| States | a demand, the background relative to which the demand is unmet, and the constraints on a solution | a set of possible answers, and the request on how many of them an answer selects [hamblin1958] [belnap1976] |
| Possible answers are | results of a type (models, concepts, consequences …) | propositions |
| Number | one problem motivates one or several questions | one question serves one or several problems |

Two relations connect them:

- A question **serves** a problem when, given the background, two conditions hold. First, the question has a true answer whenever the associated question $Q_\pi$ has one. Second, each answer to the question narrows the candidate answers of $Q_\pi$. Formally, $Q_\pi$ implies the question on the basis of $K$, in the sense of erotetic implication [wisniewski1995].
- A question **formulates** a problem when it serves the problem and a true complete answer to it yields a solution.

*Example*: "does the delay of generalization shrink when weight decay grows?" serves the problem of the delay, since each answer narrows the candidate accounts. The question "which mechanism, among those compatible with the training laws, fixes the duration of the delay?" formulates the problem.

## Subproblems

A problem $\pi_1$ **reduces** to a problem $\pi_2$ when a recorded method turns every solution of $\pi_2$ into a solution of $\pi_1$ [kolmogorov1932]. The method must be recorded: otherwise $\pi_1$ would reduce to every problem as soon as some solution of $\pi_1$ exists, known or not. The method must also be uniform, so that one procedure applies to every solution of $\pi_2$ [medvedev1955]. ^reduction

Reduction can be conjunctive: $\pi_1$ reduces to $\pi_2$ and $\pi_3$ together when the method needs a solution of each. *Example*: a property of every network of a class reduces to the same property for the linear networks of the class, together with a bound on the effect of the nonlinearity.

## Distinctions

- **A gap is not a problem, and a problem need not have a gap.** A problem exists while its demand is unmet, and it has a gap when its background also establishes the existence presupposition. The gap states a lack, whereas the problem adds the demand and its constraints, which fix the result that would fill the gap.
- **The explicanda of a problem and the placeholders of a question fix a term along two different dimensions.** An explicandum of a problem is *anchored*: a pointer fixes its use, and no type is given. A [placeholder](problem-and-question.md#^question-schema) is *typed*: its kind is fixed, and no referent is given. The level `identified` of a slot fixes both the type and the referent.
- **The request is not the aim.** The request fixes how many results, and how complete, the demand asks for. The [epistemic aim](../../epistemic-task/epistemic-aim.md) fixes the kind of knowledge that a question seeks.
- **"Epistemic problem" names the problem defined here.** The [epistemic task](../../epistemic-task/epistemic-task.md) of a question fixes the kind of knowledge that its answer must deliver. The task belongs to the question, not to the problem.

## Consequences for a record

- **A problem record states its demand, its constraints and its explicanda.** The fields are specified in the [problem record](../../inquiry/problem.md).
- **A typed demand makes the existence of a problem checkable over the records.** Over the accepted records of an inquiry, the problem exists when no accepted record of the demanded type gives a direct answer of $Q_\pi$. This condition is also the second condition of the gap.

---
## Sources

Marks follow the [legend of reading marks](../../../../CONTRIBUTING.md#^reading-marks).

- [aqvist1965] ○ Åqvist, *A New Approach to the Logical Theory of Interrogatives*, Filosofiska Studier, Uppsala, 1965; a question as the imperative "let it be the case that I know …"
- [belnap1976] ○ Belnap & Steel, *The Logic of Questions and Answers*, Yale University Press, 1976; the subject of a question and its request, fixing the number and the completeness of the answers selected
- [carnap1950_logical] ◐ Carnap, *Logical Foundations of Probability*, University of Chicago Press, 1950, ch. 1; explicandum and explicatum, checked through the [Stanford Encyclopedia of Philosophy](https://plato.stanford.edu/entries/carnap/)
- [dewey1938] ◐ Dewey, *Logic: The Theory of Inquiry*, Henry Holt, 1938, ch. 6; checked through secondary sources
- [friedman2013] ◐ [Friedman, "Question-directed attitudes", *Philosophical Perspectives* 27, 145–174, 2013](https://doi.org/10.1111/phpe.12026); attitudes directed at a question are incompatible with knowing its answer, checked through secondary sources
- [hamblin1958] ◐ [Hamblin, "Questions", *Australasian Journal of Philosophy* 36(3), 159–168, 1958](https://doi.org/10.1080/00048405885200211); checked through secondary sources
- [hansson1999] ○ Hansson, *A Textbook of Belief Dynamics*, Kluwer, 1999; belief bases, as opposed to belief sets closed under consequence
- [hintikka1976] ○ Hintikka, *The Semantics of Questions and the Questions of Semantics*, Acta Philosophica Fennica 28(4), 1976; the desideratum of a question, "bring it about that I know …"
- [hintikka2007] ◐ [Hintikka, *Socratic Epistemology: Explorations of Knowledge-Seeking by Questioning*, Cambridge University Press, 2007](https://doi.org/10.1017/CBO9780511619298); a question may be asked only once its presupposition is established
- [kolmogorov1932] ◐ Kolmogorov, "Zur Deutung der intuitionistischen Logik", *Mathematische Zeitschrift* 35, 58–65, 1932; problems, solutions and reducibility, checked through [Rodin's review of the calculus of problems](https://arxiv.org/abs/2307.09202)
- [laudan1977] ◐ [Laudan, *Progress and Its Problems*, University of California Press, 1977](https://www.ucpress.edu/books/progress-and-its-problems/paper); empirical and conceptual problems, checked through secondary sources
- [levi1980] ○ Levi, *The Enterprise of Knowledge*, MIT Press, 1980; the corpus of knowledge relative to which inquiry proceeds
- [medvedev1955] ◐ Medvedev, "Degrees of difficulty of mass problems", *Doklady Akademii Nauk SSSR* 104, 501–504, 1955; uniform reducibility of problems, checked through the Encyclopedia of Mathematics entry ["Finitary problem"](https://encyclopediaofmath.org/wiki/Finitary_problem)
- [nickles1981] ◐ [Nickles, "What is a problem that we may solve it?", *Synthese* 47(1), 85–118, 1981](https://doi.org/10.1007/BF01064267); a problem as a demand together with constraints, checked through a scanned copy of poor quality
- [polya1945] ○ Pólya, *How to Solve It*, Princeton University Press, 1945; the unknown, the data and the condition, and problems to find against problems to prove
- [vanfraassen1980] ✓ van Fraassen, *The Scientific Image*, Clarendon Press, 1980, ch. 5; the topic of a why-question presupposed true; [the chapter text](https://www.fitelson.org/290/vanfraassen_pte.pdf)
- [wisniewski1995] ◐ [Wiśniewski, *The Posing of Questions: Logical Foundations of Erotetic Inferences*, Kluwer, 1995](https://doi.org/10.1007/978-94-015-8406-7), ch. 5 on the evocation of questions; both definitions, evocation and erotetic implication, checked through [Wiśniewski, "Erotetic logic and explanation by abnormic hypotheses"](https://www.bu.edu/wcp/Papers/Logi/LogiWisn.htm)
- [zhang2017] ○ Zhang, Bengio, Hardt, Recht & Vinyals, "Understanding deep learning requires rethinking generalization", *International Conference on Learning Representations*, 2017
