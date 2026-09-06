---
tags:
  - backup
  - architecture
index: "[Superseded design proposals](_index.md)"
aliases:
  - Operational framework audit
---
# Operational Framework for Research Reasoning

---
## Major Conceptual Flaws

### The Question-to-Goal Mapping is Unrepresented and Foundational

The framework's first active transition — mapping a Question to a Goal — is treated as primitive and unproblematic. This is the framework's most serious omission. Consider:

- "Is $f$ bijective?" → Goal: "Prove bijectivity"
- "Why does the model fail to generalize?" → Goal: "Compare representations"

These mappings are not logical consequences of the Questions — they are _research judgments_: the choice to pursue bijectivity via direct proof rather than via contradiction, or to diagnose generalization failure via representational comparison rather than distributional shift analysis. These are the intellectually decisive moves in research reasoning. By positioning them outside the framework, the architecture systematically excludes precisely what makes reasoning _intelligent_ rather than _procedural_.

**Consequence**: the framework represents reasoning-once-decomposed, not reasoning-as-it-occurs. This is epistemically inadequate for the stated objective.

### The Two-Graph Architecture Lacks a Synchronization Semantics

The framework posits two interacting graphs:

- **Goal graph**: Questions → Goals → Subgoals
- **Execution graph**: Objects → Operations → New objects

In line with the previous concern, "Interaction" between these graphs is stated but never formalized. Specifically:

- Which nodes in the execution graph correspond to which nodes in the goal graph?
- When a Work Unit produces a Result, how does this propagate to the goal graph (i.e., mark a Goal as satisfied)?
- When an operation application fails, does this trigger goal revision, schema revision, or object revision?

Without a formal inter-graph correspondence (a functor, a mapping, or at minimum an explicit relation), the two-graph claim is architectural decoration rather than structural specification.

---

### Operation Schema "Primitiveness" is Asserted, Not Derived

The claim that operation schemas are primitive — and that this guarantees termination of regress — is a definitional fiat, not a structural result. The schemas listed include:

- Apply theorem
- Construct object
- Compute measure

None of these is uniformly primitive. "Apply theorem" may require sub-proofs of applicability conditions. "Construct object" may require multi-step inductive arguments. "Compute measure" may require algorithmic subroutines whose correctness requires proof.

**What is actually happening**: the framework relocates the regress problem rather than resolving it. The regress terminates at operation schemas by _defining_ them as terminal, not by deriving their terminality from structural properties. This is a circularity: regress is avoided because the framework stipulates a level at which it stops, without providing a principled criterion for what belongs at that level.

A genuine termination guarantee would require either:

- A well-foundedness condition on operation schemas (e.g., reduction to a fixed computational basis)
- An explicit axiom system with stratification proof

Neither is present.

---

### The Goal Graph Lacks a Well-Foundedness Condition

The framework asserts that "planning schemas are finite" as the basis for avoiding infinite regress at the planning level. This is insufficient. Finite schemas can still generate infinite goal trees. Consider:

> **Reduction schema**: Prove $P$ → Prove $P_1$, Prove $P_2$

If $P_1$ or $P_2$ re-invokes the reduction schema, the goal graph may be infinite or cyclic. The framework provides no acyclicity constraint, no measure of progress, and no proof that the goal graph is a DAG. Without this, the anti-regress claim is unsubstantiated.

---

### Epistemic Gain is Not Formally Represented

Requirement R1 mandates explicit representation of "epistemic gain." The framework's output layer consists of new **epistemic objects** — Results, Answers, derived Claims. These are propositional. But epistemic gain — the change in what is _understood_, not merely what is _asserted_ — is not propositional.

Understanding involves:

- Grasping _why_ a proposition holds (not merely that it holds)
- Capacity for inferential transfer to structurally similar cases
- Recognition of the _scope_ and _limits_ of a result

None of these are representable as epistemic objects within the framework. The framework produces outputs but has no epistemic state model — no representation of the reasoner's doxastic or comprehension state before and after a Work Unit. The gap between "Result produced" and "understanding achieved" is never closed.

This is the deepest philosophical failure: the framework cannot distinguish between a proof-checking system (which verifies validity) and a reasoning system (which produces understanding). The stated objective — "inferential moves yield genuine understanding, not just validity" — is not satisfied by the architecture.

==TODO: Partially addresssed by new fields and roles in `PlanningSchema`==

---

## Hidden Assumptions

### Research Reasoning is Goal-Initiated

The framework assumes reasoning originates in an explicit Question and is organized around Goal pursuit. This excludes:

- **Exploratory reasoning**: noticing an anomaly without a prior question
- **Abductive leaps**: generating hypotheses from unexpected observations
- **Serendipitous discovery**: reasoning whose direction is determined by what is found, not what was sought

These are not marginal cases — they constitute a substantial portion of actual research practice. A framework that cannot represent "I noticed $X$ unexpectedly and this changed the direction of the investigation" is epistemically incomplete for empirical research reasoning.

### Planning and Execution are Separable

The strict layering assumes planning (schema selection, goal decomposition) occurs prior to and independently of execution (operation applications). This is false in research practice. Operation failures routinely cause:

- Goal revision (the goal turns out to be malformed)
- Schema revision (the chosen decomposition is inappropriate)
- Question reformulation (the original question was ambiguous)

The framework has no feedback mechanism between the execution graph and the goal graph. It represents reasoning as a downward cascade (Question → Goal → Subgoal → Work Unit → Application), but actual reasoning involves upward revision at every level. The architecture is **acyclic by assumption** in a domain that is **inherently cyclic**.

### Epistemic Objects Have Stable Identity

The framework treats "Question," "Answer," "Model," "Evidence" as persistent objects with stable identity across reasoning. In practice, Questions are reformulated, Models are refined, and Evidence is reinterpreted as understanding develops. The framework has no identity revision mechanism — no way to represent that the question being answered at the end is not the question that was asked at the beginning, and that this revision is itself a reasoning act.

### A Fixed Type System for Epistemic Objects Exists

Operation schemas specify "input roles" and "output roles," and "admissibility conditions" govern their application. This presupposes that epistemic objects are typed — that a "theorem" is distinguishable from a "model" at the level of schema admissibility. But the framework does not specify this type system. Without it, admissibility conditions are semantically empty, and the execution graph cannot be constructed without implicit ad hoc typing decisions.

---

## Unacknowledged Tensions

### Expressivity vs. Non-Arbitrariness

Requirement R5 demands expressivity across all reasoning types. 
Requirement R4 demands that sequences of operations be generated by explicit goals and planning schemas, not by free composition. 

These are in fundamental tension:

- Expressive power requires that the framework accommodate reasoning patterns not anticipated by the schema inventory. 
- Non-arbitrariness requires that operations be schema-governed. 

Either the schema inventory is closed (and expressivity is bounded) or it is open (and non-arbitrariness is nominal).

The framework does not resolve this tension — it acknowledges "schema explosion" as a risk but provides no mechanism for schema governance.

### Formalization Overhead vs. Usability

R6 requires usability during real research and support for partial formalization. 
R1–R5 collectively require explicit representation of deficiency, objective, rationale, execution, and epistemic gain for each reasoning progression, plus selection and instantiation of planning schemas and operation schemas. 

For a moderately complex mathematical proof, the annotation burden would be substantial. These requirements are in irreducible tension. The framework does not specify what "partial formalization" means structurally — which layers are optional, which constraints can be relaxed, and what properties are lost under relaxation.

### Representation vs. Generation

The framework oscillates between two incompatible objectives:

1. **Representing** completed reasoning (post-hoc annotation)
2. **Generating** or **guiding** reasoning (operative framework during research)

Planning schemas behave like generative procedures (they decompose goals into subgoals). But epistemic objects are representational artifacts. If the framework is a _representation_ system, planning schemas need only record decompositions that occurred. If it is a _generation_ system, planning schemas must be operationally complete and decidably applicable — a far stronger requirement. The architecture conflates these two modes without acknowledging the distinction.

---

## Risks of Overengineering

The five-layer architecture (Epistemic Objects, Goals, Planning Schemas, Operation Schemas, Operation Applications) introduces:

- **Five distinct ontological categories** requiring independent maintenance
- **Two interacting graphs** without synchronization semantics
- **A schema inventory** of unbounded size
- **Typed epistemic objects** without a specified type theory

For the use cases described (mathematical proofs, informal reasoning, empirical research), this architecture exceeds what is demonstrably necessary. Specifically:

- Mathematical proof is already handled by natural deduction or sequent calculus, which achieves motivated, structured reasoning with a far smaller ontological commitment. Introduction and elimination rules encode _why_ a step is introduced without requiring a separate planning layer.
- Informal reasoning is handled with lower overhead by Toulmin's model (Claim, Grounds, Warrant, Backing, Qualifier, Rebuttal), which captures justificatory structure without imposing goal decomposition.
- Empirical reasoning is partially handled by argumentation frameworks (Dung, 1995), which represent defeasibility explicitly — a feature entirely absent from the proposed framework.

The proposed framework reinvents components of proof theory, AI planning (STRIPS/PDDL precondition-effect-action structures), and argumentation theory without acknowledging these antecedents or demonstrating what it adds beyond them.

---

## Alternative Decompositions

### Collapse Goals and Questions

The Question/Goal distinction adds a layer without clear structural necessity. A typed epistemic object with an `operational_mode` attribute (epistemic target vs. procedural objective) would reduce the ontological commitment by one layer while preserving the distinction. This also makes the Q→G mapping explicit: it becomes an attribute instantiation, not a mysterious external judgment.

### Introduce an Epistemic State Layer

Rather than producing epistemic objects as outputs, Work Units should produce **epistemic state transitions**: pairs $(S, S')$ where $S$ and $S'$ are epistemic states (sets of objects + their justificatory relations). This makes epistemic gain formally representable as the difference $S' \setminus S$ and the new justificatory structure over that difference.

### Introduce Feedback Edges

The goal graph and execution graph should be replaced by a single **bidirectional reasoning graph** with typed edges:

- **Forward edges**: goal decomposition, operation application
- **Revision edges**: goal revision triggered by operation failure, schema revision triggered by planning failure, question reformulation triggered by object revision

This collapses the two-graph architecture into one while adding the feedback structure that actual research reasoning requires.

### Specify a Schema Governance Mechanism

Rather than an open schema inventory, define a **schema calculus**: a small set of primitive schema constructors (sequential composition, parallel decomposition, conditional branching, iterative refinement) from which domain-specific schemas are derived. This bounds the schema space structurally and prevents ad hoc proliferation.

### Separate Representation from Guidance

Explicitly bifurcate the framework into:

- A **representational sublanguage** (post-hoc annotation of completed reasoning)
- A **generative sublanguage** (operative during reasoning, allowing partial specification)

Define precisely what properties are guaranteed in each mode and what the minimal intersection is.

---

## Prioritized Recommendations

1. **Formally specify the type system** for epistemic objects before any other elaboration. Without it, admissibility conditions and input/output roles are semantically vacuous.
    
2. **Replace the regress termination claim** with a structural well-foundedness proof: either reduce operation schemas to a fixed computational basis, or impose a DAG constraint on the goal graph with a progress measure.
    
3. **Introduce an epistemic state model** to make epistemic gain formally representable. Without it, the framework cannot satisfy its own primary objective.
    
4. **Add revision semantics**: feedback edges from execution failures to goal and schema revision. A framework without revision cannot represent research reasoning — only the successful retrospective of it.
    
5. **Audit against existing formalisms** (natural deduction, PDDL, Toulmin, Dung argumentation) and demonstrate what the proposed architecture adds that these do not already provide. The burden of novelty has not been discharged.
    
6. **Define the partial formalization boundary** precisely: which layers are mandatory, which are optional, and what formal guarantees degrade under relaxation.

