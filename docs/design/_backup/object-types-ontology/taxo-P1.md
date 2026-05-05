## Taxonomy - P1

## Families of objects

The architecture distinguishes at least the following families:

| Family                    | Role                                            | Examples                                                                                                      |
| ------------------------- | ----------------------------------------------- | ------------------------------------------------------------------------------------------------------------- |
| **Inquiry objects**       | What is being sought                            | `question`, `subquestion`, `objective`, `open_question`<br><br><br><br>                                       |
| **Domain objects**        | Content being reasoned about                    | `definition`, `concept`, `object`, `property`, `criterion`, `model`, `mechanism`, `taxonomy`                  |
| **Justificatory objects** | Why a proposition is valid, supporting material | `claim`, `lemma`, `theorem`, `corollary`, `proof`, `example`, `counterexample`, `argument_schema`, `evidence` |
| **Control objects**       | How inquiry is constrained and prioritized      | `assumption`, `scope`, `decision`, `status_record`, `issue`, `constraint`                                     |

Orthogonal classification:

- **epistemic acts**: question, proof, answer
- **logical constraints**: assumption, criterion, property
- **comparative structures**: taxonomy, comparison

## Object taxonomy

|Type|Distinction from Existing Types|
|---|---|
|`claim`|Proposition that is neither a full theorem nor an informal comment.|
|`conjecture`|Proposition under active investigation. Unlike `assumption`, it is not granted but targeted, and unlike a `theorem`, it lacks a proof.|
|`lemma` / `corollary`|Structurally subordinate results that serve as intermediaries in a proof chain. Conflating with `theorem` loses the dependency granularity within a proof.|
|`axiom` / `postulate`|Foundational statements accepted without proof — distinct from `assumption`, which is contextual and local to an argument, and from `definition`, which is stipulative rather than substantive.|
|`inference_rule` / `argument_schema`|Reusable logical or methodological pattern applied across multiple proofs. Externalizing these prevents silent repetition across proof objects.|
|`open_question`|Question explicitly deferred or unresolved, which must be tracked separately to avoid being silently absorbed into main problem resolution.|
|`model`|Formal structure (set, tuple, assignment of interpretations) that satisfies a set of axioms. Central in mathematical and theoretical frameworks, irreducible to definition or result.|
|`decision`|Explicit rationale that specifies why a concept / decomposition / assumption was preferred, accepted provisionally, rejected or postponed. It prevents cyclical re-analysis.|

## Functional distinctions

Several objects are distinguished because their relations differ.

**Claim / Result / Mechanism / Answer**:

- A **claim** is a proposition that may be supported or refuted, but does not necessarily have a proof object. It is the most general layer of assertion. → `answers`
- A **result** (theorem/lemma/corollary) is a proposition established or proposed, a formally derived statement with a proof object → `supports`
- A **mechanism** is an explanatory structure, often informal, that accounts for an observed phenomenon → `explains`
- An **answer** is a response (resolution claim) tied to a _specific question_ response to a specific problem → `depends_on`

These have entirely different relations, proof obligations and epistemic statuses. For example:

- a result may support several answers
- a mechanism may explain a result
- an answer may consist of a set of results + assumptions + limitations

**Problem / Question**:

- The **root question** is the global teleological anchor of the framework.
- A **sub-problem** is a formally derived decomposition, whose resolution is epistemically necessary for the parent.
- A **side question** is a tangential inquiry with no proven necessity link to the root.

**Comparison / Taxonomy**:

- A **taxonomy** is a global classification structure over a set of objects.
- A **comparison** is a relational judgment over a finite, explicitly enumerated set. Their fields, queries, and uses are disjoint.