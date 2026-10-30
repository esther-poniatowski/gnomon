---
tags:
  - specification
index: "[Specification](docs/specification/_index.md)"
aliases:
  - Operator record
---
# Operator record

> [!QUESTION] Goal: what does a researcher write in each field of the operator record of a problem, and when is each field required?

One file per problem holds the operators that its records declare, filled from `src/gnomon/data/templates/operators.yml`. The file names the target system of the problem, so a reader reaches the sets over which the operators are typed.

| Specification | When it is required | Form | Examples |
| ------------- | ------------------- | ---- | -------- |
| Operators | when a formula of any record of the problem uses an operator beyond the canonical set | one entry per operator | the restriction of a field to a region; the Jacobian of a community at equilibrium; the empirical neural tangent kernel |
| Operators: name | with every operator | the result that the operator computes, in words and with no symbol or formula | "the restriction of a field to a region" |
| Operators: symbol | with every operator | an identifier, unique across the problem and distinct from every declared quantity | `restrict`, `community_jacobian`, `ntk` |
| Operators: notation | when the operator prints as more than its symbol | a LaTeX template in single quotes, `#0` for the indices that a binder consumes and `#1`, `#2` for its arguments | `'\nabla \cdot #1'`; `'\operatorname{spec}( #1 )'` |
| Operators: for any (type variables of the operator) | when the operator is general over the sets on which it acts | the type variables that its signature and values may name, so that a general operator is typed once for all its call sites | `[S]` for an adjoint, typed `maps(S, S)` to `maps(S, S)`; `[S, n]` for an inner product of two vectors |
| Operators: signature | with every operator | the set expression of each argument, in order | `["maps(Om, pow(reals, 3))"]` |
| Operators: values | with every operator | the set expression in which its result lies | `"maps(Om, reals)"`; `reals` |

- **One operator vocabulary serves one problem.** Every record of a problem reads the same operator file. A phenomenon, its target and its questions therefore draw on one set, and no record redeclares an operator that a sibling declares. An operator is typed over sets that any record of the problem may declare. The operator file is therefore read against the *whole problem*. ^one-operator-file

- **A problem declares the mathematics that it adds.** Each problem lists in its `operators.yml` the operators that its records use beyond the canonical set. These local operators resolve only within that problem. The restriction of a field to a region, or the Jacobian of a community at equilibrium, belongs to the *problem* that uses it. The canonical set therefore holds only the operators that every inquiry can assume. ^local-operators
