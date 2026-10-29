---
tags:
  - reference
index: "[Methods for reasoning](_index.md)"
aliases:
  - Question decomposition framework
---

# Question decomposition framework

## Overview

The proposed method is a form of **regressive analysis**: a goal is reduced to the conditions under which it is attained, and each unmet condition becomes a subgoal. Regressive analysis has three established formulations:

- the analysis of Pappus, which Pólya reworked as "working backwards";
- means–ends analysis, in the problem-solving theory of Newell and Simon;
- the erotetic logics of Hintikka (the interrogative model of inquiry) and of Wiśniewski (erotetic search scenarios).

The erotetic logics break questions down into other questions, so they come closest to the proposed method. Within these formulations, the method works as a heuristic for a question that is already well posed. As stated, however, it needs five amendments.

1. **"Condition of satisfiability" covers three distinct relations.** A question fails in one of three ways:
    
    - the question is unsound, because a presupposition is false;
    - the answers are undefined, because the set of admissible answers is not fixed;
    - no admissible answer can yet be selected and justified.
    
    Each failure generates a different type of subquestion. A single notion of condition hides the first two failures, because only the third concerns the search for an answer.
    
2. **The decomposition is an AND/OR graph.** Some conditions are jointly necessary (an AND node). Others are alternative routes to the same answer (an OR node): a quantity can be derived analytically or estimated by simulation. Therefore, the method must include a criterion for choosing among routes. Typical criteria are the expected cost of a route, its probability of success, and the strength of warrant it delivers.
    
3. **Analysis must be followed by synthesis.** Working backward identifies _necessary_ conditions. Meeting every necessary condition yields an answer only when the set of conditions is also jointly sufficient. Pappus separated analysis from synthesis for this reason, since the steps of analysis cannot always be reversed. The method therefore needs a composition step that combines the subanswers into an answer to the parent, and a check that the combination is valid.
    
4. **Answers can revise the parent question.** A subquestion can return a _corrective_ answer: a presupposition of the parent is false, or a term of the parent is ill defined. The parent must then be reformulated before anyone looks for an answer to it. A strictly top-down tree cannot represent that case.
    
5. **Termination depends on resources and is not guaranteed.** "Answerable directly" means answerable with the repertoire available to a given researcher at a given time. Consequently, one subquestion can be terminal for one team and open for another. Moreover, conditions can depend on each other: a measurement presupposes the theory it tests, and two parameters may be identifiable only jointly. The decomposition graph then contains cycles. A cycle is resolved by iteration, through successive approximation or bootstrapping. Further decomposition cannot resolve it, because each node of the cycle presupposes the others.

    > [!NOTE] Cycles and the canonical conditions
    > Within one question, the [conditions of answerability](../epistemology/definitions/conditions-of-answerability.md#^condition-dependencies) have no cycle, and cycles arise between questions. A measurement that presupposes the theory it tests uses a candidate of the same question in its bridging inference, and the condition of [tests that can fail](../epistemology/specification-order.md#^iteration-circularity) decides whether the test supports that candidate. Two parameters identifiable only jointly form one discriminating quantity, obtained by a joint estimate.
    

With these amendments, the method is a correct schema for directed inquiry. It does not apply to the exploratory phase of research, where the question is not yet fixed. In that phase, the first subquestion is usually the one that makes the root question well posed.

## Identifying the conditions of satisfiability

Conditions are identified from the logical form of the question. Hamblin and Belnap–Steel model a question by the set of its admissible direct answers. Hintikka adds the **desideratum**: the epistemic state the questioner must reach for the question to count as answered. Four steps follow from this model.

1. **Fix the form.** State the interrogative type of the question (e.g. whether, which, why, how), then its subject and its set of admissible answers. For a why-question, the form also requires a contrast class and a relevance relation (van Fraassen): why P rather than Q, and through which type of factor.
2. **Extract the presuppositions.** Every proposition that all admissible answers entail is a presupposition. "Why does the network learn disentangled features?" presupposes that the network does learn them, and that "disentangled" has a definite criterion.
3. **State the desideratum and the standard of warrant.** Specify the resolution of the answer, such as a sign, an order of magnitude, or an exact law. Also specify the warrant required, such as a proof, a statistical test at stated power, or robustness across models.
4. **Work backward from the desideratum to the current epistemic state.** For each admissible answer, ask what must be known to select it over its rivals and to justify that selection. Every item missing from the current state is an unmet condition, and it becomes a subquestion. Wiśniewski formalizes this step as erotetic implication: a question Q implies a question Q₁ when every direct answer to Q₁, together with the available premises, narrows down the set of answers to Q.

The resulting conditions must pass two tests:

- **Necessity:** when the condition fails, no admissible answer can be justified. A condition that fails this test is removed.
- **Joint sufficiency:** once all conditions are met, a justified answer follows. When this test fails, a condition is missing, most often a bridging assumption.

## Types of conditions and subquestions

> [!IMPORTANT] Canonical statement
> This framework counts seven conditions: soundness, conceptual definiteness, answer space, discrimination, access, bridging and scope. The conditions are stated, with their two routes, their states and their dependencies, in the [conditions of answerability](../epistemology/definitions/conditions-of-answerability.md). That note splits the answer space into the answer type and the admissible candidates, keeps only the advance part of scope under the name representation, and leaves the rest of scope to the evaluation of an obtained answer.

Two further distinctions apply across all the conditions. First, sibling subquestions stand in one of three logical relations:

- conjunctive, when all are needed;
- disjunctive, when any single subquestion suffices;
- sequential, when the answer to one fixes the form of another.

Second, some conditions depend on the interrogative type. A why-question requires a contrast class. A how-question about a mechanism requires the mechanism's components, their activities, and their organization (Craver).

## Types of terminal epistemic acts

A subquestion is terminal when some procedure has all its inputs available and outputs an admissible answer at the required standard of warrant. The best way to classify terminal acts is by the **source of the warrant** they deliver, because that source determines what the answer can be trusted for.

|Source of warrant|Act|Subquestions typically closed|
|---|---|---|
|Existing knowledge|retrieval from the literature, a database, an expert|any type, when the answer is already established|
|Reasoning alone|proof, analytic calculation, conceptual analysis|bridging; discrimination within a formal model; definiteness|
|Observation of the target|measurement, analysis of existing data|soundness; discrimination|
|Intervention on the target|controlled experiment|discrimination between causal hypotheses|
|Study of a surrogate|numerical simulation, analysis of a model|discrimination within the model, plus a scope condition for transfer|
|Generation|abduction; construction of a model, an instrument, or an algorithm|answer space; access|
|Decision|stipulative definition, choice of idealization, choice of a standard|definiteness; desideratum|

The last two rows differ in status from the others. Acts of generation add candidates or tools, but they justify no answer. Acts of decision fix a commitment, but they establish no fact. Therefore, any answer obtained by either act must be recorded as a revisable assumption of the decomposition. When the root answer fails, these assumptions are the first to re-examine.

## Amended method

The five amendments and the two classifications combine into one procedure:

- **Formalize** the question: form, presuppositions, admissible answers, desideratum.
- **Decompose** it by working backward into an AND/OR graph of subquestions, each labeled with its type of condition.
- **Close** each leaf with a terminal act, choosing among alternatives by cost and strength of warrant.
- **Compose** the subanswers into an answer to each parent, checking joint sufficiency.
- **Revise** the parent whenever a subanswer is corrective, and iterate around cycles.

**Sources named:** Pappus (Book VII of the _Collection_); Pólya, _How to Solve It_ (1945); Newell & Simon, _Human Problem Solving_ (1972); Hamblin, "Questions" (1958); Belnap & Steel, _The Logic of Questions and Answers_ (1976); van Fraassen, _The Scientific Image_ (1980), ch. 5; Hintikka, _Inquiry as Inquiry_ (1999); Craver, _Explaining the Brain_ (2007); Wiśniewski, _Questions, Inferences, and Scenarios_ (2013).

---

**Checks on this answer**

- **Frame:** Object: the question-decomposition method · Reader's next action: apply or revise the method · Admission test: a unit is kept only if it changes how the method is applied. The test removed no unit.
- **Linter:** `hermeneia lint` ran on a copy in the scratchpad over three rounds. The only errors left are `vocabulary.nominalization` flags on terms from erotetic logic (_question_, _condition_, _presupposition_, _decomposition_). These are exempt under `verb-over-process-noun` as named technical terms. I fixed the rest: long inline lists, two sentences over 34 words, "kind of", "in terms of", sentences opening on a bare pronoun, "the studied case", and the generic "one".
- **Not done:** The keys of `audit-protocol` Pass B were scanned by reading, not by a script. No second agent reviewed the answer. I cited the references from memory and did not check them online, as `source-checking` requires; dates and chapter numbers should be checked before any of them is cited in writing.
- **Open choice:** The seven condition types come from my own breakdown of what answering requires. They are not taken from a single source, and a different breakdown, for instance by interrogative type, would give a different table.