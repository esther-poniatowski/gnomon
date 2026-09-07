---
tags:
  - backup
index: "[Argument and reasoning proposals](_index.md)"
aliases:
  - Derivation encoding — variant G
---

# Encoding derivations and proofs

The previous methodology concerns the **macro-structure** of inquiry: decomposition of a question into epistemically necessary subquestions (which subquestion must be answered). The present issue lies at a lower scale: **how the internal chain of inferential moves answering one subquestion should itself be represented**

---

## Local problem: proofs as proposition chaining

For a fixed subquestion $Q$, a derivation or a proof is usually represented as a sequence of claims:
$$  
C_0 \to C_1 \to \cdots \to C_n  
$$ where every implication is *valid*.

This representation is insufficient because it lack **local intelligibility**: each step appears arbitrary since the "idea behind" the move remains implicit.

The relevant object is therefore not merely an argument graph of propositions, but an argument graph of **goal-directed local transformations**.

What is missing is the structure that answers, at each step:

1. **What precise local target is currently pursued**
2. **What obstacle prevents an immediate conclusion**
3. **What operation is applied to overcome that obstacle**
4. **Why this operation is appropriate here**
5. **What progress it creates toward the target**

Thus, to procude understanding, the correct unit is not merely a proposition, but a **micro-step** of the form:

> from a local proof state, under a current target, perform an admissible transformation that reduces the distance to the target for an explicit reason.

---

## Principle: proofs as state transformations

**Local intelligibility criterion**: A chain of local steps gives genuine understanding if, for every non-trivial step, the following three relations are explicit:

- Backward relevance: Why does this move address the current target?
- Forward productivity: What new possibilities does this move open?
- Contrastive necessity: Why is this move preferable to the main alternatives at this point?

A local reasoning should be represented as a sequence of **proof states** and **typed transitions** between them. Each step is not only a derived claim; it is a **controlled modification of the local proof landscape**.

Each proof state contains at least:

- the current target
- the currently available facts
- the current obstacle
- the admissible next moves

Each transition records:

- the chosen move
- its formal warrant
- its local motivation 
- its effect on the proof state

So the structure is rather:
$$  
(S_k, T_k, O_k)\xrightarrow{m_k}(S_{k+1}, T_{k+1}, O_{k+1})  
$$ where:

- $S_k$ is the local epistemic state
- $T_k$ is the current target
- $O_k$ is the active obstacle
- $m_k$ is the chosen inferential operation

**Proof-state delta**: A step is intelligible when it explicits the *difference* between successive states:
$$  
\Delta_k = (T_k, S_k, O_k) \leadsto (T_{k+1}, S_{k+1}, O_{k+1})  
$$

In practice, the delta should answer:

- what disappeared as an obstacle
- what new resource became available
- whether the target was simplified, decomposed, or transformed
- whether the proof moved closer to a terminal rule

In compact abstract form, the relevant unit is:
$$  
(\text{target}, \text{facts}, \text{obstacle})  
\;\xrightarrow{\text{typed move + warrant + motivation}}\;  
(\text{new target}, \text{new facts}, \text{new obstacle})  
$$

---

## Core fields for a local inferential step

Each local step should contain the following fields for intelligibility:

|Field|Function|
|---|---|
|`target_before`|statement currently to be established|
|`available_facts`|facts currently usable|
|`obstacle`|what blocks immediate derivation|
|`move_type`|inferential operation performed|
|`move_content`|exact transformation applied|
|`warrant`|theorem, definition, rule, or prior fact licensing the move|
|`output`|new fact obtained or new target generated|
|`target_after`|updated target after the move|
|`progress`|precise sense in which the step advances the proof|
|`why_this_move`|local reason for choosing this move rather than another|


`obstacle`: This fields ensures that the step does not looks arbitrary. 

Typical obstacles are:

- target too complex
- mismatch of syntactic form
- hidden existential quantifier
- unavailable witness
- unavailable bound
- dependence on several cases
- relevant invariant not yet isolated
- current facts expressed in the wrong vocabulary

`progress`: This field must not be rhetorical. It must describe the exact structural effect of the move.

Typical progress types are:

- reduction of a compound goal into subgoals
- conversion of target into a form matching an available theorem
- extraction of a usable component from a conjunction
- introduction of a witness for an existential goal
- normalization of an expression
- case partition that exhausts possibilities
- replacement of a global property by a local criterion

`why_this_move`: This is distinct from the warrant.

- The **warrant** explains why the step is valid
- `why_this_move` explains why the step is relevant now

---

## Typed taxonomy of local moves

To avoid arbitrary prose, inferential moves should belong to a finite typed family. This typing is useful because each move type has a characteristic explanatory template, making the representation predictable and partially automatable.

### Structural moves

These do not add new substantive information; they reorganize the target or available facts.

|Move type|Function|
|---|---|
|`unfold_definition`|replace a concept by its defining clauses|
|`fold_definition`|compress a structure into a named concept|
|`decompose_goal`|split a conjunction or equivalence target|
|`decompose_fact`|extract components from a conjunction or structured fact|
|`rephrase_goal`|rewrite target into an equivalent but more usable form|
|`normalize_expression`|simplify or canonicalize syntax|

### Transport moves

These transfer information through rules or maps.

|Move type|Function|
|---|---|
|`instantiate_rule`|apply a general rule to the current objects|
|`specialize_hypothesis`|derive a particular consequence from a universal statement|
|`transport_along_equivalence`|replace a statement by an equivalent one|
|`monotonic_transfer`|carry bounds or order through monotonicity|
|`substitute_equals`|replace equal terms in a statement|

### Search moves

These create the missing object or missing case structure.

|Move type|Function|
|---|---|
|`introduce_witness`|produce candidate for an existential target|
|`choose_parameter`|instantiate a free parameter strategically|
|`split_cases`|partition the problem into exhaustive alternatives|
|`introduce_auxiliary_claim`|create a lemma or intermediate assertion|
|`introduce_invariant`|define the quantity that remains controlled|

### Closure moves

These complete a partially prepared derivation.

|Move type|Function|
|---|---|
|`apply_criterion`|conclude by verifying a known sufficient criterion|
|`derive_contradiction`|close a branch by inconsistency|
|`aggregate_subresults`|combine previously obtained subclaims|
|`discharge_assumption`|close a conditional or contradiction argument|

---

## Derivation graph with proof states

Each step should be rendered according to the same local schema. A clear formal object is a bipartite graph with two node types.
### State nodes

```yaml
state:
  id: P_k
  target: ...
  facts: [...]
  obstacle: ...
```

### Transition nodes

```yaml
transition:
  id: M_k
  from_state: P_k
  to_state: P_k+1

  move_type: ...
  move_content: ...
  
  warrant:
    kind: definition | theorem | rule | algebraic identity | prior result
    source: ...

  why_this_move: ...
  progress:
    kind: ...
    description: ...
```

### Chaining

This yields:
$$  
P_0 \to M_0 \to P_1 \to M_1 \to P_2 \to \cdots  
$$

Such a representation is better than a plain proposition graph, because it makes visible:

- what was sought at each moment
- what was known
- why the next move became natural

This template forces a distinction that ordinary proof prose usually blurs:

- semantic state
- logical legitimacy
- local motivation
- structural progress

---

## Worked example

Consider the local subquestion: Why does hypothesis $H$ imply conclusion $C$

Suppose the proof really proceeds by showing that $H$ yields criterion $K$, and that $K$ is sufficient for $C$.

An opaque proof is:

1. From $H$, obtain $K$
2. Since $K$ implies $C$, conclude $C$

A proper local representation exhibits the key difference: each step is represented as a response to a local obstacle under a current target.

```yaml
state:
  id: P0
  target: "Prove C"
  facts: ["H"]
  obstacle: "C cannot be derived directly from H because H and C are expressed at different descriptive levels"
```

```yaml
transition:
  id: M0
  from_state: P0
  to_state: P1

  move_type: introduce_auxiliary_claim
  move_content: "Introduce criterion K as an intermediate target"

  warrant:
    kind: strategy
    source: "Known sufficiency theorem links K to C"

  why_this_move: "K is expressed in the same vocabulary as H and is known to suffice for C"
  progress:
    kind: bridge_construction
    description: "Creates an intermediate statement that connects the available hypothesis to the desired conclusion"
```

```yaml
state:
  id: P1
  target: "Prove K"
  facts: ["H", "K => C"]
  obstacle: "Need an intermediate property derivable from H"
```

```yaml
transition:
  id: M1
  from_state: P1
  to_state: P2

  move_type: instantiate_rule
  move_content: "Specialize theorem T to derive K from H"

  warrant:
    kind: theorem
    source: "Theorem T"

  why_this_move: "T directly converts H into the missing criterion K"
  progress:
    kind: criterion_established
    description: "The sufficient condition for C becomes available"
```

```yaml
state:
  id: P2
  target: "Prove C"
  facts: ["K", "K => C"]
  obstacle: "None"
```

```yaml
transition:
  id: M2
  from_state: P2
  to_state: P3

  move_type: apply_criterion
  move_content: "Infer C from K and K => C"

  warrant:
    kind: modus_ponens
    source: "Basic inference"

  why_this_move: "The proof state is terminal: the target matches the conclusion of an available implication"
  progress:
    kind: closure
    description: "The target is discharged"
```

---

## Compression rules for practical use

A fully explicit micro-format can become heavy. A disciplined compression rule is therefore necessary.

A step may omit the fields `obstacle` and `why_this_move` only if the move is **terminally obvious**, namely if all the following hold:

1. the current target syntactically matches a standard rule
2. no alternative move is plausible
3. the progress is immediate and unique

Otherwise, the explanatory fields should remain mandatory.

This prevents excessive verbosity while preserving intelligibility where it matters.

---

## Audit criteria for local argument graphs

A local proof representation is defective if it creates the impression of arbitrariness. This is captured by the following criteria:

|Defect|Meaning|
|---|---|
|`blind_step`|a move has a warrant but no local motivation|
|`hidden_obstacle`|a non-trivial reformulation appears without explanation of what blocked the previous state|
|`spurious_move`|a move is valid but creates no identifiable progress|
|`teleological_gap`|the move does not clearly aim at the current target|
|`untyped_transition`|the inferential operation is not classified|
|`state_ambiguity`|it is unclear which facts are active at that point|




