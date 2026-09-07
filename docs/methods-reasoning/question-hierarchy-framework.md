---
tags:
  - reference
index: "[Methods for reasoning](_index.md)"
aliases:
  - Question hierarchy framework
---
# Question Hierarchy Framework

## Core Problem

> [!FAIL] Problem
> A precise research question does not automatically determine its route of resolution.

This problem is both:

- epistemic: what must be known in order for the final claim to be justified
- methodological: how to organize inquiry efficiently

**Goal**: achieve a **problem decomposition principle** to infer a set of intermediate questions whose resolution constitutes genuine progress toward a justified answer to the target question — not mere accumulation of related information.

## Approach

**Governing criterion** (applies at every step):

> A sub-question is admissible only if its resolution clearly changes the status of the main question: reducing the set of admissible answers, forcing a reformulation, or making a currently indistinguishable distinction visible.

This framework distinguishes two moments:

- **Planning-time decomposition**: analysis performed *before* substantial inquiry.
- **Inquiry-time revision**: local revision triggered by obstacles encountered *during* inquiry.

> [!CHECK]
> The framework is intentionally **operational**. It avoids explicit probability models, heavy graph machinery, and formal meta-structures whose maintenance would cost more than their practical benefit.

## Operational protocol

| Operation                                                                                                                           | Output                                |
| ----------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------- |
| Fix the target question: <br>- specify the answer-form<br>- specify the scope<br>- identify the missing conditions of answerability | A precise research target             |
| Identify the current blockage and classify its type                                                                                 | A statement of what prevents progress |
| Convert each missing condition into one or more candidate sub-questions that remove that blockage                                   | Candidate next steps                  |
| Classify each candidate as necessary, useful, or decorative                                                                         | Filtered next steps                   |
| Rank the retained sub-questions by diagnostic power, feasibility, and structural centrality                                         | Chosen next sub-question              |
| Record dependencies                                                                                                                 |                                       |
| Work on the highest-priority available sub-question                                                                                 | New result, failure, or clarification |
| When resistance appears, generate an abductive or constructive sub-question and revise locally (invalidate conditioned nodes)       | Updated register                      |
| Periodically verify whether the main question itself requires disambiguation, restriction, or conceptual replacement                | Stable inquiry direction              |

## Detailed steps

### 1. Fix the target question

Before any decomposition, the target question must be stabilized.

> [!QUESTION] What exactly is to be understood, shown, explained, characterized, or constructed?

#### Specify the answer-form

> [!QUESTION] What would count as a satisfactory answer to the main question?

Possible answer-forms:

- theorem
- formal criterion
- definition
- mechanism
- taxonomy
- counter-example
- predictive framework
- discriminating comparison between alternatives

#### Specify the scope

Determine the domain in which the question is posed:

- Which class of objects or models?
- Which regimes or assumptions?
- Which level of abstraction?
- Which type of evidence or reasoning is admissible?

#### Expose the conditions of answerability

> [!QUESTION] Under which conditions would an answer to the main question be justified?

Which of these conditions are currently missing? Each missing condition yields one or more candidate sub-questions.

| Condition type       | What must hold                                                              |
| -------------------- | --------------------------------------------------------------------------- |
| **Conceptual**       | The central notions must be precise enough for the intended use             |
| **Formal**           | The problem objects and relations must be represented in a usable framework |
| **Evidential**       | Relevant consequences can be observed, derived, or computed                 |
| **Identifiability**  | Distinct candidate answers can in principle be distinguished                |
| **Feasibility**      | The required analysis or derivation can actually be carried out             |
| **Interpretability** | The result can be read back in terms of the original question               |

---

### 2. Generate candidate sub-questions

#### Classify the blockage type

> [!QUESTION] What specifically prevents progress now?

A sub-question should should be created because it removes a specific obstacle to answering the main question.

**Operative sequence**:

1. Identify the current blockage: *What exactly blocks progress at this stage?*
2. State why this blockage prevents progress on the main question: *Why does this obstacle matter for the main question?*
3. Formulate the smallest sub-question whose resolution would remove or clarify that blockage: *What smaller question would remove it?*

**Common mappings from obstacles to sub-questions**:

| Obstacle           | Practical meaning                                                                    | Generated sub-question                                                                                                                                        |
| ------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Conceptual**     | A central notion is vague, overloaded, undefined or unstable                         | What notion is actually needed, and what constraints must it satisfy? How should the notion be defined so that it serves the research aim and be operational? |
| **Formal**         | No usable representation or framework exists                                         | What formal object or simplified setting captures the issue?                                                                                                  |
| **Formal**         | No measurable or computable criterion exists                                         | What valid proxy, observable, or derived quantity can be used?                                                                                                |
| **Discriminative** | Multiple incompatible interpretations coexist                                        | Which interpretation is relevant to the research aim, and what excludes the others?                                                                           |
| **Discriminative** | Several explanations or formalisms remain equally compatible                         | What would discriminate between them?                                                                                                                         |
| **Tractability**   | The problem is too hard or too broad in its full form                                | Which reduced setting preserves the core difficulty? What representation or reformulation makes the problem manageable?                                       |
| **Interpretive**   | A result is derivable or computable but its meaning for the main question is unclear | What is required for univocal interpretation? What relation is missing between the formal result and the target claim?                                        |

#### Distinguish three functional types of sub-questions

All sub-questions belong to one of three functional categories, which determine both how they are generated and how their validity is assessed.

| Type of sub-question | Trigger                                                                                                                                                                                                                                                                                                | Role                                                                    | Typical forms                                                                                                                                                                                                              | Validity                                                                                    |
| -------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- |
| **Analytic**         | During *planning-time*, a specific condition of answerability is currently missing                                                                                                                                                                                                                     | Remove explicit, already visible obstacles                              | - What precisely must be defined?<br>- What assumptions are required?<br>- What formalism is appropriate?<br>- What would count as discriminative evidence?                                                                | Unconditional — valid as long as the main question stands                                   |
| **Abductive**        | During *inquiry*, a resistance appears (see [revision triggers](#^revision-triggers))                                                                                                                                                                                                                  | Identify a hidden assumption, missing property, or inadequate formalism | - Which hidden assumption failed?<br>- What property was implicitly required?<br>- Which alternative formalism would restore tractability?<br>- What causes the mismatch between the formal result and the intended claim? | Conditional — valid only under the structural hypothesis $H_R$ that explains the resistance |
| **Constructive**     | The existing conceptual vocabulary is too coarse, it collapses distinctions that matter for the research aim:<br>- distinct situations yield the same answer<br>- all candidate notions require ad hoc corrections at boundary cases<br>- competing frameworks agree formally but diverge structurally | Expand the framework itself                                             | - Define a concept that separates phenomena currently conflated<br>- Construct a formal object that reveals the relevant distinction<br>- Identify a representation under which the question becomes tractable             | Semantic prerequisite — downstream sub-questions are undefined until this one is resolved   |

> [!WARNING]
> Questions generated by a specific failure should not silently acquire unconditional status. A derivational impasse often generates a local explanatory hypothesis. Once that hypothesis is overturned, downstream questions spawned by it often deserve reassessment.

---

### 3. Select and order sub-questions
#### Filter by relevance

Each candidate sub-question must be assigned one of three statuses:

| Status         | Criterion                                                                                                    |
| -------------- | ------------------------------------------------------------------------------------------------------------ |
| **Necessary**  | Without it, answering the main question would be impossible, invalid, or uninterpretable                     |
| **Useful**     | It is not strictly required, but it improves robustness, scope, or explanatory force                         |
| **Decorative** | It is adjacent or interesting, but its resolution does not materially affect the answer to the main question |

**Operational test**: For each candidate sub-question, ask:

- What would become impossible if this were resolved negatively?
- What would become supported if it were resolved positively?
- What would become newly distinguishable?

If the answer is materially empty, the sub-question is decorative and should be removed.

#### Prioritize by diagnostic power, feasibility, and structural centrality

 For each candidate sub-question, evaluate three aspects:

| Criterion                 | Guiding question                                                                                                                                                       |
| ------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Diagnostic power**      | If resolved, how sharply would it constrain the admissible answers to the main question (i.e. eliminate possibilities, falsify assumptions, or force a reformulation)? |
| **Feasibility**           | Can progress be made on it now with available tools, background knowledge, or simplified settings?                                                                     |
| **Structural centrality** | Does it concern a load-bearing assumption, concept, or mechanism — one whose falsification restructures the problem?                                                   |

**Priority rule**:

1. Prefer the available sub-question that is both highly constraining and reasonably tractable.
2. (more adversarial formulation) Prefer the sub-question whose least favorable plausible answer would still eliminate a substantial portion of the currently live possibilities.

Confirmatory evidence accumulates slowly; a single decisive negative result eliminates a structural hypothesis entirely. Sub-questions should be designed as potential falsifiers of assumptions, not as collectors of supporting evidence.

> [!NOTE]
> This qualitative prioritization is sufficient to retains the practical value of structural falsification without requiring heavy formal apparatus.
> This criterion corresponds to the notion of _strong tests_ in Popperian methodology and to _expected information gain_ in Bayesian terms.

---

### 4. Register sub-questions and track dependencies

| Sub-question | Type | Depends on   | Unlocks (effect on main question) | Status | Priority | Conditioned on |
| ------------ | ---- | ------------ | --------------------------------- | ------ | -------- | -------------- |
| $Q_1$        |      | —            | Definition of target notion       |        |          | —              |
| $Q_2$        |      | $Q_1$        | Comparison of candidate criteria  |        |          | —              |
| $Q_3$        |      | $Q_1$        | Toy model construction            |        |          | —              |
| $Q_4$        |      | $Q_2$, $Q_3$ | Discriminating predictions        |        |          | —              |

The column "Effect on main question" is decisive in filtering the candidates.

The relation "Depends on" should be interpreted in the broad operational sense:

- the earlier question must be answered before the later one is meaningful
- or before it becomes tractable
- or before its answer becomes interpretable

Column "Conditioned on" (optional) allows cascaded invalidation:

- For obstacle-removing sub-questions, it is left empty. 
- For failure-induced sub-questions, it names the structural hypothesis $H_R$ under which the sub-question was generated. When $H_R$ is later refuted, every sub-question conditioned on $H_R$ is immediately invalidated and must be reconsidered.
- For constructive sub-questions, it carries the marker **[vocabulary-expanding]**, indicating that downstream sub-questions presupposing the new vocabulary are semantically undefined until this node resolves.

This additional machinery may be restricted class of research situations:

- long theoretical projects with several branching derivational routes
- inquiries where failures generate many local explanatory hypotheses
- projects with substantial risk of continuing to work inside a locally invalidated conceptual frame
- collaborative settings where memory externalization matters

>[!NOTE]
>A full graph formalism is unnecessary in normal use. This lightweight dependency tracking is enough to record of dependency relations and to avoid common errors:
>- attempting validation before conceptual clarification
>- treating parallel-looking questions as independent when one presupposes the other
>- spending time on peripheral questions before load-bearing ones

The dependencies between questions and their priorization often reveals three levels:

|Level|Concerns|
|---|---|
|Foundational questions|definitions, assumptions, formalization, and criteria of success|
|Structural questions|mechanisms, derived properties, invariants, decomposition into cases, reduction to tractable regimes|
|Validation questions|empirical tests, simulations, comparisons, robustness, generalization|

---

### 5. Revise the framework during inquiry

#### Local revision

Inquiry often reveals latent obstacles that were not visible initially. Typical revision triggers: ^revision-triggers

| Trigger                         | Meaning                                                                                                |
| ------------------------------- | ------------------------------------------------------------------------------------------------------ |
| **Impasse in derivation**       | The current route fails, it presupposes a missing property or an inadequate formalism                  |
| **Empirical or formal anomaly** | A result contradicts the working view, some assumption or mechanism is false, incomplete, or too crude |
| **Conceptual tension**          | Two branches of the framework interfere, they rely on incompatible implicit assumptions                |
| **Interpretive ambiguity**      | A result is obtained but uninterpretable                                                               |
| **Counter-example**             | The current formulation is too general or misses a crucial constraint                                  |

**Revision procedure**:

1. **Record** the resistance in one sentence.
2. **State** what it suggests is missing, false, or misaligned.
3. **Formulate** one new sub-question that would repair, discriminate, or reconstruct.
	- If the resistance signals a false local explanatory structure: _abduce_ the simplest structural hypothesis $H_R$ consistent with the resistance and settled background knowledge, and add one abductive sub-question, labeled with $H_R$ in the "Conditioned on" column.
	- If the resistance signals vocabulary insufficiency: add a *constructive* sub-question.
4. **Invalidate** all sub-questions conditioned on any hypothesis that the resistance refutes.
5. **Remove or postpone** any older sub-question that has become secondary in light of the revision.

#### Global revision

Global reorganization is needed only if the main question itself turns out to be malformed.

Three main cases justify revision of $Q$ into a refined question $Q'$:

| Refinement type            | Description                                                                                                                 |
| -------------------------- | --------------------------------------------------------------------------------------------------------------------------- |
| **Disambiguation**         | $Q$ conflated two distinct questions; $Q'$ addresses one precisely                                                          |
| **Scope restriction**      | The original scope was too broad for the intended answerability conditions; $Q'$ narrows scope to where the conditions hold |
| **Conceptual replacement** | A central term  in $Q$ must be replaced by a more precise notion produced by constructive work                              |

When this happens:

- State the relation between $Q$ and $Q'$ explicitly.
- Assess prior sub-questions for continued relevance under $Q'$.

---

## Methodological failure modes

| Failure mode                                                                              | Description                                                                                                                                           |
| ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Decomposing by related themes**                                                         | Sub-questions mirror the literature or the topic rather than the epistemic structure of the problem                                                   |
| **Decomposing by workflow**                                                               | The inquiry is split into stages (e.g. literature review → data collection → experiment → interpretation) rather than into epistemic obstacles        |
| **Decomposing by available tools**                                                        | Questions are chosen because a method is available ("what can be done") not because they are needed ("what must be known")                            |
| **Decorative branching**                                                                  | Time is spent on interesting adjacent questions that do not affect the main answer                                                                    |
| **Treating all sub-questions as equally broad**                                           | All sub-questions are treated on equal footing and independent — no dependency structure emerges                                                      |
| **Validating prematurely**                                                                | Empirical or formal validation is attempted before concepts and criteria are clarified — produces formally correct but uninterpretable results        |
| **Vocabulary inertia**                                                                    | The current conceptual language is preserved even when it cannot express the needed distinctions                                                      |
| **No falsifying leverage**                                                                | No sub-question is capable of eliminating a central assumption or framework, resolving any of them leaves the admissible answer space for Q unchanged |
| **Revising the dependency register globally**                                             | New obstacles trigger complete reorganization even when local revision suffices — valid prior work is discarded unnecessarily                         |
| **Introducing failure-induced sub-questions without recording the structural hypothesis** | Sub-questions silently inherit unconditional validity; when $H_R$ is refuted, the invalidation propagates invisibly.                                  |

## Appendix: Warrant Structure

When the blockage type alone does not make the required sub-questions evident, the logical type of the target claim can sharpen decomposition by identifying the real deficiency. Each claim type imposes a characteristic justificatory burden, which determines the canonical sub-questions: **question type → justificatory burden → canonical sub-questions**.

*Use cases*: In theoretical research, especially involving derivations, definitions, or formal characterizations, researchers often know that a claim is under-specified but do not know what kind of burden of justification is missing. Obstacles are often not of the form "a term is vague" or "a formalism is missing" but rather "the justificatory burden of the target claim has not been articulated".

|Warrant|Establishes|Canonical sub-questions|
|---|---|---|
|**Conceptual adequacy**|The claim is well-formed and properly delimited|What are the essential traits? What are the inclusion/exclusion criteria? How does the notion differ from neighboring concepts? Is the definition adequate for its intended use?|
|**Ontological warrant**|The object or mechanism claimed is possible or real|What would count as an instance or witness? Could apparent evidence be generated by alternatives? What discriminates genuine existence from artefact?|
|**Structural adequacy**|The internal organization of the target object is correctly described|What formal object captures the structure? Which invariants are relevant? What transformations preserve the property?|
|**Causal warrant**|The invoked factors genuinely produce the phenomenon|Which factors covary? Which are causally efficacious? What interventions would change the outcome? Through which mechanism?|
|**Inferential warrant**|The conclusion genuinely follows from the assumptions|What exactly is to be shown? Which assumptions are necessary? What intermediate steps are required? What is the validity domain?|
|**Modal / regime warrant**|The conditions of validity, breakdown, or transition are correctly identified|Which parameters control the phenomenon? Are there thresholds? Which conditions are necessary, sufficient, or both?|
|**Epistemic warrant**|The method used to detect, measure, or validate the claim is trustworthy|What observable signatures indicate the target? Are they specific? What are the false positive and false negative risks? Does success reflect the intended property or a confound?|

**Compact synthesis**:

| Broad family                   | Central demand                                      | Typical question types                                                 |
| ------------------------------ | --------------------------------------------------- | ---------------------------------------------------------------------- |
| **What does it mean?**         | Clarify concepts and distinctions                   | Definition, taxonomy                                                   |
| **Is it there?**               | Establish reality, presence, or detectability       | Existence, identification                                              |
| **What is it like?**           | Describe form, structure, and measurable properties | Characterization, measurement, comparison                              |
| **Why or how does it happen?** | Establish mechanism or productive dependence        | Explanation, prediction                                                |
| **When does it hold?**         | Establish validity, limits, and transfer conditions | Derivation, boundary conditions, necessity/sufficiency, generalization |