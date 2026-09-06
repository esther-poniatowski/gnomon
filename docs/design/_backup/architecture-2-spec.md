---
tags:
  - backup
  - architecture
index: "[Superseded design proposals](_index.md)"
aliases:
  - Operational framework specification
---
# Operational Framework for Research Reasoning

## Layers

A local inferential progression can be represented by **several layers**:

| Level                                                                                                                                                                                                                                                                                       | Objects                                                                                                     | Relations                                                                                                                                             |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Epistemic layer**: structures the inquiry.<br>Core epistemic nodes, that inquiry consumes, manupilates, produces and establishes.<br>They answer what entities exist in the graph.                                                                                                        | - `Question`<br>- `SubQuestion`<br>- `Answer`<br>- `Concept`<br>- `Criterion`<br>- `Evidence`<br>- `Method` | - `decomposes_into`<br>- `answers`                                                                                                                    |
| **Control layer**: structures the reasoning, organizes the intelligible progression.<br>They explain **why** an execution block is the right next move in the inquiry, and connect **why** to **how**.<br>                                                                                  | - `ReasoningStep` (?)<br>- `Goal`<br>- `Planning Schemas`                                                   | - `addresses`<br>- `advances`<br>- `prepares`<br>- `branches_into`<br>- `merges_from`<br>- `refines`<br>- `completes`<br>- `revises`<br>- `qualifies` |
| **Execution layer**: organizes the actual epistemic labor.<br>They explain **how** to produce knowledge.<br>Role is narrow: they define admissible kinds of transformation (what kinds of epistemic work are possible) and perform legitimate transformations (what exactly was performed). | - `WorkUnit` (?)<br>- `OperationSchema`<br>- `OperationApplication`                                         | - `implements`<br>- `uses`<br>- `produces`<br>- `verifies`<br>- `computes`<br>- `derives`<br>- `constructs`                                           |

---

### Epistemic Objects

These represent the **knowledge state**. They are **not reasoning steps**.

These objects:

- persist across reasoning
- are consumed and produced

_Examples_:

| Object        | Description                                                                                   | Attributes                                                                                                                                                    |
| ------------- | --------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Question**  | Explicit epistemic target. It defines the gap to be resolved.                                 | - the content being asked<br>- conditions of answerability<br>- decomposition into subquestions<br>- relevance to a parent question<br>- expected answer type |
| **Answer**    | Candidate resolution of a question. It records the epistemic gain (not merely a proposition). | - the resolved content<br>- the question it answers<br>- degree or status of acceptance<br>- scope and assumptions<br>- the warrant by which it is accepted   |

---

### Goals

Goals represent **what must be achieved** at a given stage. They are **operational**, not epistemic.

_Examples_:

- answer question
- compute descriptor
- test hypothesis
- compare structures
- prove lemma

A goal may target a question, an object construction, or a transformation:

| Subtype                | Task                                                                                                                    | Example                                                                                     |
| ---------------------- | ----------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- |
| **Question goals**     | Answer a question.<br>These correspond directly to Question objects.                                                    | Determine whether representations differ                                                    |
| **Derivational goals** | Produce a required object.<br>They are operational goals.<br>These do not necessarily correspond to explicit questions. | - compute covariance<br>- derive equation<br>- construct counterexample                     |
| **Structural goals**   | Transform the reasoning state.<br>These are meta-goals. They restructure the inquiry.<br>                               | - reduce problem<br>- split cases<br>- introduce auxiliary object<br>- reformulate question |

To avoid redundancy, goals should not be independent top-level objects. Instead:

- Goal = Question + Objective type  
    or
- Goal = operational wrapper around Question

Thus:

```
Goal {
    target: Question | Object
    objective: ObjectiveType
    success_condition: Condition
}
```

---

### Planning Schemas

Planning schemas define **how to structure reasoning**. They organize work into an intelligible episode and refine tasks to advance on the question.

They decompose or reformulate **what must be achieved** and **why**, not how it is executed.

A **planning schema** performs a **goal transformation**: Goal → Subgoals

A planning shcema carries a **contextual strategic decision**: given a local epistemic state and a deficiency, select and instantiate a planning schema. It is primarily **strategic** and **integrative** (not computational or demonstrative).

Planning schemas define:

- context: current goal + local epistemic state in which the step occurs 
- target gap: what is missing or blocked (epistemic obstacle)
- objective: what local subgoals introduced to address that deficiency (goal decomposition, subgoal templates, dependency structure)
- rationale: why this local route is relevant
- gain: how the obtained result advances the inquiry, what has become intelligible, answerable, or decidable

_Examples_:

- Reduction schema: prove equivalence → prove two implications
- Comparison schema: compare structures → extract representations | compute descriptors | align | compare | evaluate
- Elimination schema: evaluate competing hypotheses → derive predictions | test predictions | eliminate inconsistent hypotheses

| Attributes                          | Role                                                                                                                                                                                              | Content                                                                                                                                                                                                                                                                                                                                                                                                 |
| ----------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Local epistemic state**           | What is already available at this point. It specifies the context of the step.                                                                                                                    | - active question and current goal<br>- established results<br>- available concepts and distinctions<br>- accepted constraints                                                                                                                                                                                                                                                                          |
| **Diagnosed insufficiency**         | Why the current state is not sufficient. It is exactly what makes the next move intelligible.<br>It answers: *what is missing here?*                                                              | Typical forms:<br>- direct derivation is blocked<br>- the target is too coarse and must be decomposed<br>- the relevant concept remains ambiguous<br>- several alternatives remain open<br>- the available evidence underdetermines the answer<br>- the current formulation hides the relevant structure                                                                                                |
| **Strategic objective of the step** | What local subgoals are introduced in response to that insufficiency. It is the purpose of the move.<br>It answers: *what is this step trying to achieve locally?*                                | Typical forms:<br>- reduce the target to a known criterion<br>- isolate the decisive distinction<br>- construct an intermediate object<br>- split the problem into exhaustive cases<br>- move from extensional description to mechanism<br>- eliminate a competing interpretation<br>- reformulate the question in a tractable representation                                                           |
| **Generative rationale**            | Why this particular step is the appropriate one. It is the idea of the move. It encodes its strategic logic.                                                                                      | - “Since the target concerns uniqueness, the relevant structure is injectivity”<br>- “Since the phenomenon varies across contexts, the key task is to separate invariant from context-specific structure”<br>- “Because the definition is opaque, a decomposition into necessary components is required”<br>- “Because the obstruction comes from global coupling, a local factorization is introduced” |
| **Epistemic gain**                  | What exactly has become available after the step. This gain is the true output of the step. The ontology must allow reasoning steps to produce multiple kinds of epistemic gain, not just claims. | - a question is answered<br>- a subquestion is generated<br>- a distinction is clarified<br>- a candidate is excluded<br>- a mechanism is identified<br>- a representation is made tractable<br>- a criterion is established<br>- a partial answer is obtained<br>- a route toward the answer is opened                                                                                                 |

The epistemic function of an reasoning step takes values such as: ^epistemic-functions

| Type                     | Role                                                                           | Distinctive property                                     | Use                                                                                    |
| ------------------------ | ------------------------------------------------------------------------------ | -------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| **Derivational move**    | Produces content by necessity from prior accepted content.                     | Truth-preserving or rule-governed consequence            | - proofs  <br>- formal derivations  <br>- definitional consequences                    |
| **Evidential move**      | Produces support from observation, experiment, data, or measurement.           | Empirical bearing on a claim                             | - statistical tests  <br>- experimental findings  <br>- observations                   |
| **Explanatory move**     | Introduces a structure that makes a phenomenon intelligible.                   | Answers "how" or "why", not merely "whether"             | - mechanisms  <br>- causal accounts<br>- generative models                             |
| **Interpretive move**    | Clarifies the meaning, scope, or reading of a statement or concept.            | Semantic or conceptual disambiguation                    | - conceptual analysis  <br>- reformulation  <br>- distinction making                   |
| **Decompositional move** | Breaks a question or claim into constituent conditions, cases, or subproblems. | Exposes internal dependency structure                    | - necessary conditions  <br>- case splits  <br>- subquestion generation                |
| **Integrative move**     | Combines several partial results into a higher-level answer.                   | Synthesis across previously separate items               | - assembling subanswers  <br>- unifying local results  <br>- cross-case generalization |
| **Eliminative move**     | Narrows the space of candidates by exclusion.                                  | Progress by ruling out rather than directly establishing | - contradiction  <br>- falsification  <br>- exclusion of alternatives                  |
| **Heuristic move**       | Introduces a plausible direction of inquiry without yet fully justifying it.   | Search guidance rather than immediate warrant            | - conjecture generation  <br>- analogy  <br>- exploratory hypothesis                   |
| **Methodological move**  | Justifies a procedure, criterion, or mode of analysis.                         | Governs how inquiry should proceed                       | - choice of model  <br>- admissibility criteria  <br>- decomposition criteria          |
| **Critical move**        | Tests, weakens, qualifies, or limits an earlier result.                        | Reflexive control of overclaiming                        | - robustness checks  <br>- boundary conditions  <br>- counterexample analysis          |

---

### Operation Schemas

Operation schemas are **primitive executable units**. They perform work and change knowledge.
They are **goal-agnostic**: they ignore why they are used.

An **operation schema** performs a **state transformation**: Epistemic State → Epistemic State
These are **object-level transformations**: it consumes objects and produces objects.

No regress: operation schemas do not decompose into further planning schemas.

Operation schemas define what kinds of epistemic work are admissible. Each schema has fixed semantics: **signatures** that define its exact computational and epistemic role.

- name: identity of the operation type
- input roles: required operands, with types
- output roles: produced objects, with types
- admissibility conditions
- transformation semantics: what the operation does
- success condition: what counts as correct completion
- license kind: deductive, empirical, methodological, definitional, interpretive...
- explanation template: how the operation contributes intelligibility

_Examples_:

- Apply theorem
- Construct object
- Compute measure
- Compare structures
- Rewrite expression
- Split cases

_Example_: `ApplyTheorem`

- Inputs: theorem T, objects A,B
- Output: derived claim C

---

### Operation Applications

Operation applications are the **atomic execution of concrete epistemic work** that are genuinely executable or inspectable. They apply `OperationSchema` to concrete objects.

An operation application represents one primitive epistemic transformation licensed by a known operation schema. 

Operation applications instantiate:

- schema: nature of the operation being applied
- inputs: list of objects, bound operands
- rule: theorem, definition, protocol, criterion (why this application is admissible) 
- content: formal expression or structured text
- outputs: list of objects, products created or established

Critically, `inputs` and `outputs` are not untyped bags, but precise **role-indexed bindings** determined by the schema. 

*Example* for a "comparison" operation: `left: Structure`, `right: Structure`, `comparison_metric: ComparisonMetric`, `alignment_rule`

Thus, a derivation or proof is a graph of operation applications drawn from a proof-operation library.

*Examples*: instantiate a definition, rewrite an expression, invoke a theorem, verify a condition, split in cases...

*Example*:  "Proving kernel triviality" may be represented by several operations:

1. `Assume`
    
    - input: target statement “show kernel is trivial”
    - output: local assumption $f(x)=0$
    
2. `ApplyDefinition`
    
    - input: definition of $f$, assumption $f(x)=0$
    - output: equation system $E$
    
3. `RewriteExpression`
    
    - input: $E$
    - output: simplified system $E'$
    
4. `SolveSystem`
    
    - input: $E'$
    - output: result $x=0$
    
5. `ApplyDefinition`
    
    - input: kernel definition, result $x=0$
    - output: judgment “kernel is trivial”

---

### Work Units

Work units are:

- **composite subgraph of operation applications** that encodes how the work is carried out,
- solving one local executable goal.

WorkUnit = Goal + OperationGraph + Result

They are the first unit in the framework that record **actual analysis** rather than strategic orientation. Its internal structure is graph-theoretic, not rhetorical.

A work unit defines:

- goal: what local executable target must be achieved
- entry conditions: conditions under which execution may start
- operation graph: explicit chain of suboperations
- exposed outputs: products made available to outer structures
- verification: how completion, correctness or adequacy is checked

No regress: work units stop at operation schemas.

*Examples*: Its nature depends on the domain:

- in mathematics: derivation, proof fragment, case split, construction
- in informal theoretical inquiry: conceptual distinction, comparison of cases, elimination of alternatives, evidential synthesis,  interpretation of a formal result, mechanistic decomposition

---

## Reasoning Structure

The a full reasoning process is not a bare sequence or list of steps. The framework must encode the **articulation** of the progression: **hierarchical dependency graph of oriented reasoning episodes**.

**Full reasoning**:

Question (defines an epistemic target)
↓  
Goal  
↓  
Planning schema (selects a local strategic response to a deficiency relative to that target)
↓  
Subgoals  
↓  
Work units (realizes that response by a connected executable subgraph)
↓  
Operation applications (executes work, applies a typed primitive schema)
↓  
New epistemic objects

The reasoning process is the **interaction** between two graphs:

- Goal graph: `Question`/`Goal` → `PlanningSchema` → `Subquestions`/`Subgoals`
- Execution graph: `Objects` → `OperationSchemas` / `OperationApplications` → `New objects`
- `WorkUnit` is the bridge: it realizes one goal by one execution subgraph

Nesting is possible when execution itself requires new strategic orientation. If an `OperationApplicaton` still requires a nontrivial new idea, it may trigger a nested `PlanningSchema`.

This system avoid infinite regress because:

- operation schemas are primitive
- planning schemas are finite
- work units are instances

Thus, execution terminates.

---

## Granularity 

Criteria are principled and non-ad hoc.

| Object                 | Corresponds to                                                                                                                                                                                                                                     | Creation conditions                                                                                                                                                                                                                                                                                                                                                                          |
| ---------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `PlanningSchema`       | One object = one **local epistemic intention**, one **strategic idea** that reorients the inquiry, one **coherent episode of reasoning** governed by one guiding idea.                                                                             | When the argument introduces a genuinely new local orientation that changes the strategic idea:<br>- a new obstacle is diagnosed<br>- a new subgoal is introduced<br>- a new strategic route is chosen<br>- the problem is reformulated<br>- a new case distinction becomes relevant<br>- a new criterion is identified as decisive<br>- a local result is integrated and a new phase begins |
| `WorkUnit`             | One object = one coherent piece of actual analysis whose method is stable.<br>Characteristics:<br>	- composite by definition<br>	- contains a graph of operation applications<br>	- grouped because they jointly realize one local executable goal | Change of concrete analytical method:<br>- the concrete goal changes<br>- the method changes<br>- a new theorem or procedure is invoked<br>- the argument branches into cases<br>- a new intermediate construction is introduced<br>- symbolic execution gives way to interpretation, or conversely                                                                                          |
| `OperationApplication` | Characteristics:<br>	- atomic by convention of the framework<br>	- one application of one primitive schema<br>	- no internal decomposition required by the ontology                                                                                |                                                                                                                                                                                                                                                                                                                                                                                              |

---

## Examples

### Mathematical Proof

- Question: Is $f$ bijective?
- Goal: Prove bijectivity of $f$
- Planning schema (decomposes goal): Apply `ReduceBijectivityFiniteDim`
- Planning schema:
	- reduce to injectivity
	- prove dimension equality
- Subgoal: Prove injectivity
- Work unit:
	- Assume $f(x)=0$
	- Apply definition
	- Solve system
	- Conclude kernel trivial
- Operation applications: execute the proof steps
- Result: Injectivity proven

### Informal Research Reasoning

- Question: Why does model fail to generalize?
- Goal: Determine whether representations differ across contexts
- Planning schema: Compare representations
- Subgoals:
	- extract representations
	- compute descriptors
	- align spaces
	- compare descriptors
	- evaluate criterion
- Operation applications
	- SelectSubset
	- ComputeDescriptor
	- AlignStructures
	- CompareStructures
	- EvaluateCriterion
- Result: Answer

WARNING: The same conceptual idea may exist at two levels, but each instance is either goal-level or object-level. This is normal and not problematic.

*Example*: `SplitCases`

- Is this an operation or a planning schema?
- Answer: It depends on its role.
- If splitting cases requires producing explicit subquestions → planning schema
- If splitting cases requires producing explicit case objects → operation

---

## Distinctions

### Goals vs. Questions

|           | **Question**                                                                                                           | **Goal**                                                                                                                                 |
| --------- | ---------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------- |
| Nature    | **Epistemic objects** with semantic content                                                                            | **Operational roles** assigned to epistemic objects, **tasks**, contextual and procedural objectives                                     |
| Role      | What is being asked, **what is unknown**  <br>                                                                         | What must be achieved at a given stage of reasoning, **what must be done**                                                               |
| Stability | Stable notes in the knowledge graph: original questions remain unchanged                                               | Dynamic reasoning states: evolve during reasoning                                                                                        |
| Examples  | - Why does the model fail to generalize?<br>- Is $f$ injective?<br>- What is the mechanism underlying this phenomenon? | - answer this question<br>- reduce this question to subquestions<br>- test a hypothesis<br>- establish a lemma<br>- compute a descriptor |

Relations:

- the same question can appear in different goals
- not all goals map to questions

*Example*: Mathematical proof

- Question: Is $f$ bijective?
- Possible goals: Only some of these correspond to explicit questions.
	- reduce bijectivity to injectivity
	- prove injectivity
	- compute kernel
	- apply theorem

### Answer vs. Claim

The distinction is not intrinsically necessary. It depends on whether the system is designed to be **strictly question-indexed**.

**Option A: eliminate Claim, keep only Answer**: This is the purest option if the framework is strongly erotetic and inquiry-centered.

Under this design:

- every accepted informational content appears only as an **answer**
- an answer is always indexed to a **question**
- no free-floating proposition exists in the ontology: every informational unit is tied to an explicit epistemic role, no object is stored without a known problem that it resolves.

**Option B: distinguish Claim from Answer**: This becomes necessary if the framework must represent non-erotetic propositions, that are not anchored as answers to explicit questions. Such as:

- assumptions
- axioms
- intermediate lemmas
- conjectures
- observations
- constraints
- hypotheses not yet attached to a fully formulated question

Under this design:

- **Claim** = propositional content that can be asserted, evaluated, supported, attacked
- **Answer** = claim plus an explicit relation to a question that it resolves

Then the relation is:

- every answer has a claim-like content
- not every claim is an answer

---

## Potential risks and Open questions

The following issues remain unresolved:

- Granularity stability:
    - What defines primitive schemas?
    - Risk of schema explosion
- Planning schema completeness:
    - Are planning schemas enumerable?
    - How to prevent ad-hoc schema proliferation?
- Usability:
    - Will researchers tolerate the overhead?
    - How much formalization is required?
- Expressivity:
    - Can all reasoning types be encoded?
    - Risk of forcing unnatural reasoning
- Implementation complexity:
    - Graph complexity
    - maintenance cost
    - Versioning of reasoning graphs