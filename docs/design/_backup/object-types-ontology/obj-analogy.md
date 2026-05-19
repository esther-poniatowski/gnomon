# Object candidate — Analogy

## Role

An analogy maps a source domain to a target domain by aligning entities, relations, or operations.

An analogy supports tentative reasoning about the target by transferring structure from the source.

An analogy suggests claims without proving them. Its warrant comes from shared structure, not from deductive necessity or frequency.

An analogy can:

- support arguments
- motivate conjectures
- guide examples
- expose conceptual structure

*Examples*:

- the Bohr atom model maps atomic structure to a planetary system,
- an electrical-circuit analogy maps fluid flow to current, pressure to voltage, and hydraulic resistance to electrical resistance.

## Properties

**Truth-apt**: No. An analogy is a mapping; the claims it suggests are truth-apt.

**Functional stratum**: Comparative

**Internal structure**:

- **Source.** Domain or structure used as the familiar side.
- **Target.** Domain or structure to be understood.
- **Mapping.** Correspondences between source and target elements.
- **Transfer.** Features or claims licensed by the mapping.
- **Limits.** Points where the analogy breaks or becomes misleading.

## Encoding options

### Mapping composite

**Category:** Composite object

**Specification:** Reify the mapping between source-side `MODEL` or `CONCEPT`s and target-side `MODEL` or `CONCEPT`s (e.g., atom to solar system), then let analogical `ARGUMENT`s cite that mapping.

**Pros.**
- Preserves reusable mapping across domains independent of any one inference.
- Supports evaluation by structural depth, scope, relevance, disanalogy, and failure conditions.

**Cons.**
- Requires a mapping object or structured relation vocabulary.

### Analogical argument subtype

**Category:** Subtype object

**Specification:** Treat analogy as a subtype of `ARGUMENT`; the argument links premise `CLAIM`s to a conclusion `CLAIM` (e.g., shared orbit structure supports a target claim).

**Pros.**
- Works when the mapping only licenses a conclusion.

**Cons.**
- Buries reusable mapping content inside argument structure.
- Makes it harder for several analogical arguments to cite the same mapping.
- Fails when the mapping has use outside support for one conclusion.

### Structural mapping claim

**Category:** Subtype object

**Specification:** Use a `CLAIM` for the assertion that two structures correspond (e.g., current corresponds to water flow), and require analogical `ARGUMENT`s to cite that claim as warrant or backing.

**Pros.**
- Keeps mappings persistent and cross-referenceable.

**Cons.**
- Makes correspondence structure propositional even when it functions as a reusable map.
- Can obscure source domain, target domain, scope, and breakdown conditions unless these properties stay explicit.

### Model relation

**Category:** Composite object

**Specification:** Link a transferred `MODEL` to either a reified `ANALOGY` or a structural-mapping `CLAIM`, and keep the licensing `ARGUMENT` separate from the transferred model (e.g., water-flow model applied to circuits).

**Pros.**
- Captures cases where a model transfers structure across domains.

**Cons.**
- Does not make analogy a subtype of model.
- Needs an explicit link between the transferred model structure and the analogy that licenses it.

## Subtypes

Subtypes are meaningful along one dimension: the function of the cross-domain mapping.

| Label | Description | Encoding | Assessment |
| --- | --- | --- | --- |
| Structural analogy | Preserves relations among source and target elements. | `ANALOGY` composite between source and target `MODEL` or `CONCEPT`s. | Core case. Keep as subtype if mapping depth guides evaluation. |
| Model-transfer analogy | Reuses a source `MODEL` to structure a target domain. | `ANALOGY` linked to transferred `MODEL` and licensing `ARGUMENT`. | Useful when the transferred model remains addressable. |
| Heuristic analogy | Guides search without licensing a final claim. | `ANALOGY` linked to `QUESTION`, `METHOD`, or `STRATEGY`. | Better as subtype when it opens inquiry rather than supports a conclusion. |
| Illustrative analogy | Clarifies a target without independent inferential force. | `ANALOGY` with low commitment or annotation on an `EXPLANATION`. | Often reducible to example-like exposition. |
