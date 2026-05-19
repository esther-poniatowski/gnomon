# Object candidate — Explanation

## Role

An explanation answers a why-question or how-question by linking an explanandum to an explanatory basis.

Its role is to show what accounts for the target phenomenon, result, or pattern.

*Example*: a causal account that explains a long shadow by citing the flagpole height and sun angle is an explanation.

*Explanation forms*:

- causal explanation
- mechanistic explanation
- functional explanation
- unificationist explanation
- contrastive explanation

## Properties

**Truth-apt**: Derivative. An explanation can be adequate or inadequate; explanatory claims inside it are truth-apt.

**Functional stratum**: Explanatory

**Internal structure**:

- **Explanandum.** Phenomenon, result, pattern, or claim to be explained.
- **Explanans.** Claims, model, mechanism, or contrast that accounts for the explanandum.
- **Type.** Causal, mechanistic, functional, unificationist, or contrastive form.
- **Link.** Dependence that makes the explanans answer the question.
- **Contrast** (context-dependent). Alternative outcome or foil.

## Encoding options

### Explanatory composite

**Category:** Composite object

**Specification:** Combine an explanandum `CLAIM` or `QUESTION`, explanans `CLAIM`s, and cited `MODEL` or `MECHANISM`s into a reified explanatory relation (e.g., why the shadow is long).

**Pros.**
- Preserves the difference between what explains and what needs explanation.
- Keeps the explanatory relation visible for causal, mechanistic, teleological, contrastive, and unificationist forms.

**Cons.**
- Requires a reified structure when explanation must be cited or evaluated.

### Argument subtype

**Category:** Subtype object

**Specification:** Use an `ARGUMENT` subtype that supports an explanandum `CLAIM` from premise `CLAIM`s (e.g., height and sun angle explain shadow length).

**Pros.**
- Reuses premise, conclusion, warrant, and backing structure.
- Works when explanation mainly supports an explanandum claim.

**Cons.**
- Can miss the asymmetry between argument and explanation.
- The flagpole-style asymmetry shows that support and explanation can run in opposite directions.

### Model reduction

**Category:** Reduction to another object

**Specification:** Use `MODEL` as carrier for the answer to a why-question (e.g., a causal model of the failure).

**Pros.**
- Fits compact mechanistic or causal accounts.
- Works when no separate explanans-explanandum object is needed.

**Cons.**
- Hides explanandum, explanans, and explanatory relevance if the relation is not explicit.

## Subtypes

Subtypes are meaningful along one dimension: the explanatory relation between explanans and explanandum.

| Label                      | Description                                            | Encoding                                                             | Assessment                                        |
| -------------------------- | ------------------------------------------------------ | -------------------------------------------------------------------- | ------------------------------------------------- |
| Causal explanation         | Explains by revealing causes or dependencies.          | `EXPLANATION` subtype linked to causal `MODEL` or `CLAIM`s.          | Stable when causal direction matters.             |
| Mechanistic explanation    | Explains through organized entities and activities.    | `EXPLANATION` subtype linked to `MECHANISM`.                         | Stable when productive organization matters.      |
| Structural explanation     | Explains by citing mathematical, formal, or organizational structure. | `EXPLANATION` subtype linked to `MODEL`, `CONCEPT`, or structural `CLAIM`s. | Stable when the explanandum follows from structure rather than causal production. |
| Functional explanation     | Explains by citing the function of a part or process.  | `EXPLANATION` subtype linked to role `CLAIM`s or `MODEL`.            | Useful when contribution to a system matters.     |
| Contrastive explanation    | Explains why one outcome occurred rather than another. | `EXPLANATION` subtype with foil relation.                            | Stable when the contrast class changes relevance. |
| Unificationist explanation | Explains by subsuming cases under a common pattern.    | `EXPLANATION` subtype linked to `MODEL`, `FRAMEWORK`, or `ARGUMENT`. | Useful when pattern reuse matters.                |
