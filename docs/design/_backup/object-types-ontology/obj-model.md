---
tags:
  - backup
  - object-candidate
index: "[Object-kind candidates](_index.md)"
aliases:
  - Model (object candidate)
---
# Object candidate — Model

## Role

A model represents a target domain through a structured surrogate.

Its role is to support structured manipulation of the target without directly asserting claims about it.

*Example*: a causal graph that represents dependencies among variables is a model.

*Examples of uses*:

- organization
- idealization
- simulation
- classification
- comparison
- consequence generation

## Properties

**Truth-apt**: No

**Functional stratum**: Surrogate

**Internal structure**:

- **Target.** Domain or system represented by the model.
- **Elements.** Quantities, states, entities, or parameters used in the model.
- **Structure.** Relations, equations, rules, or constraints among variables.
- **Simplifications.** Features ignored, reduced, or idealized by the model.
- **Fit** (context-dependent). Link between model structure and target features.

> [!NOTE]
> In mathematical and theoretical frameworks, a model is a formal structure (set, tuple, assignment of interpretations) that satisfies a set of axioms.

## Encoding options

### Representational primitive

**Category:** Primitive object

**Specification:** Keep `MODEL` as the object that `CLAIM`, `ARGUMENT`, `EXPLANATION`, and `METHOD`s operate on, cite, test, or transform (e.g., a causal graph).

**Pros.**
- Preserves the difference between claims about a structure and the structure used for reasoning.
- Covers objects such as Bayesian networks, dynamical systems, formal grammars, utility functions, and physical models.

**Cons.**
- Needs a strict boundary from `ARGUMENT` when a model supports a specific conclusion.
- Needs internal factoring for formal, computational, causal, phenomenological, statistical, and taxonomic models.

### Claim and concept compound

**Category:** Reduction to another object

**Specification:** Replace the model with `CLAIM`s over `CONCEPT`s (e.g., variables are independent).

**Pros.**
- Fits thin axiomatic theories that function mainly as claim sets.

**Cons.**
- Loses the Tarskian distinction between a structure that satisfies claims and a claim about that structure.
- Flattens operations such as solving, simulating, instantiating, comparing, perturbing, and fitting.
- Fails when an operation targets the structure as a whole.

### Axiomatic characterization

**Category:** Composite object

**Specification:** Use `CLAIM` clusters for axioms and theorems, and link them through `CHARACTERIZES` to the `MODEL` that supplies satisfying structures (e.g., groups satisfying group axioms).

**Pros.**
- Separates the axiom set from the class of satisfying structures.
- Handles formal theories such as ZFC, where axioms are claims but intended interpretations behave as models.

**Cons.**
- Requires consistent use of the model node even when the text presents only axioms.

## Subtypes

Subtypes are meaningful along one dimension: the representational operation the model supports.

| Label                  | Description                                                                | Encoding                                                           | Assessment                                                       |
| ---------------------- | -------------------------------------------------------------------------- | ------------------------------------------------------------------ | ---------------------------------------------------------------- |
| Formal model           | Represents a structure through formal objects and satisfaction conditions. | `MODEL` subtype linked to axiomatic `CLAIM`s and `INTERPRETATION`. | Stable in mathematical contexts.                                 |
| Causal model           | Represents dependency or intervention structure.                           | `MODEL` subtype; `MECHANISM` covers productive explanation.        | Stable when interventions and direction matter.                  |
| Computational model    | Represents a target through executable simulation or algorithm.            | `MODEL` subtype linked to computational `METHOD`.                  | Stable when execution produces evidence or predictions.          |
| Phenomenological model | Represents observed patterns without deep causal structure.                | `MODEL` subtype linked to descriptive `CLAIM`s.                    | Useful when fit matters more than mechanism.                     |
| Statistical model      | Represents distributions, parameters, or data-generating assumptions.      | `MODEL` subtype linked to `EVIDENCE` and estimation `METHOD`.      | Stable when fit and uncertainty matter.                          |
| Classificatory model   | Represents a domain by classes and relations.                              | `MODEL` subtype or `CLASSIFICATION`.                               | Use `CLASSIFICATION` when class organization is the main object. |
