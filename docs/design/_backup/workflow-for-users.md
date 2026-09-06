---
tags:
  - backup
  - aspect
index: "[Superseded design proposals](_index.md)"
aliases:
  - User workflow proposal
---
# Workflow for users
## Workflow - 1

1. **Start from questions**. Each research session should be anchored to:
    
    - one target question
    - one explicit intended output
    - one boundary declaration
    
2. **Build minimal answer subgraphs**. For a target question, the system should construct the smallest subgraph that supports an answer. This is a methodological analogue of dependency minimization in software systems. A subgraph is minimal if it contains only the objects that are epistemically necessary for answering the target question, and no extraneous nodes. For instance:
    
    - necessary definitions
    - active assumptions
    - relevant claims
    - needed proofs or proof fragments
    - examples only if required  
    
3. **Justify each new object**. When a new object is created, it should also answer:
    
    - why does this object exist
    - which question does it serve
    - what existing gap does it fill
    - what would break if it were absent

## Workflow - 2

### 1. Start from the main research question

The root object should be a **question node**, not a conclusion node.

This is important because understanding is organized around problem resolution.

Example:

```yaml
question:
  id: Q1
  content: "Why does phenomenon E occur under condition A?"
  role: root
```

---

### 2. Decompose the root question into answerable subquestions

A subquestion should correspond to one of the following forms:

- definitional clarification
- criterion identification
- causal condition
- necessary condition
- sufficient condition
- exclusion of rival explanations
- construction of an object
- proof of an invariant
- empirical discriminant

This step yields a **question tree**.

---

### 3. For each subquestion, construct a local argument graph

Each local graph should connect:

- premises
- inferential moves
- intermediate claims
- answer claim

At this stage, validity is central.

---

### 4. Add the explanatory layer

For each step, annotate:

- local target
- strategic role
- conceptual effect
- rejected alternatives

This stage converts a proof trace into an intelligible argument.

---

### 5. Add narrative compression

Once the full graph exists, multiple projections become possible:

- **formal projection**: only claims and warrants
- **pedagogical projection**: claims, goals, and conceptual effects
- **audit projection**: uncertain steps, hidden assumptions, unsupported nodes
- **automation projection**: machine-tractable dependencies and rule applications

A single underlying structure can thus support both human understanding and partial automation.

## Workflow 3

1. Represent the root problem as an explicit question
2. Decompose the question into answerable subquestions
3. Build a typed graph of claims, questions, methods, obstacles, and examples
4. Represent each inferential step with:
    
    - inputs
    - output
    - operation
    - warrant
    - local goal
    - strategic role
    - gap closed
    - conceptual effect
    - considered alternatives
    
5. Enforce structural constraints that forbid blind or irrelevant steps
6. Derive several projections from the same graph for proof, pedagogy, audit, and automation