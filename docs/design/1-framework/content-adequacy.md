# Content adequacy

> [!INFO] Tier and axis
> **Tier 1 (framework-level desiderata) — content axis.** This file fixes what the framework must *represent*: which aspects of research reasoning the system must capture and at what depth. The criteria collected here are success conditions for the project. They cannot be overridden by architectural or aspect-specific decisions.

---

## Epistemic adequacy ^t1-epistemic-adequacy

> [!INFO] Migrated to [research faithfulness](_framework-criteria#^t1-research-faithfulness)

The framework must capture genuine research reasoning. This entails three conditions:

- **Conceptual soundness**: the components must be well-defined with stable boundaries.
- **Logic of inquiry**: the framework must represent not only epistemic content but also the inferential progression that answers a given question.
- **Distinction of epistemic functions**: the framework must distinguish, at minimum:
	- the epistemic lack (what gap is being addressed)
	- the epistemic move (what operation is being performed)
	- the epistemic warrant (what licenses the operation)
	- the epistemic gain (what new content or intelligibility is produced)

*Source*: criteria-framework §Core requirements, §What must be represented.

---

## Expressivity across reasoning types ^t1-expressivity

> [!INFO] Migrated to [reasoning-types coverage](_framework-criteria#^t1-reasoning-types-coverage)

The framework must support multiple reasoning regimes without forcing them into a single mold:

- **mathematical proofs** (monotonic, rule-governed, deductive),
- **informal theoretical reasoning** (conceptual analysis, distinction-making, reformulation),
- **empirical arguments** (evidence-based, defeasible, probabilistic),
- **abductive and exploratory reasoning** (hypothesis generation, serendipitous discovery).

This includes supporting **partial specification**: concepts, arguments, and claims must be admissible as legitimate intermediate objects before their full formal characterization is available. See the gap identified against dependent type theory in [Internal Workings of Formal Reasoning Domains](vendor/gnomon/docs/references-methods/overview-formal-frameworks).

*Source*: criteria-framework §Core requirements; overview-formal-frameworks §What no existing domain provides.

---

## Non-arbitrary chaining ^t1-non-arbitrary

> [!INFO] Migrated to [goal-driven reasoning](_framework-criteria#^t1-goal-driven-reasoning)

Every reasoning step must be **motivated by an explicit goal**. No free or topical composition is admissible. Sub-questions and analyses must be justified by their contribution to the local target or to the root question.

Concretely, a step is admissible only if the following are all specified:

1. the current local target it addresses,
2. the inferential move it performs,
3. the principle that licenses that move,
4. the gap the move closes,
5. why this move is preferable at this point to at least one salient alternative.

*Source*: criteria-framework §Core requirements; criteria-G §Quality constraints (no blind step, no globally irrelevant step); workflow-1 §Justify each new object.

---

## Concrete analytical execution ^t1-concrete-execution

> [!INFO] Migrated to [concrete analytical execution](_framework-criteria#^t1-concrete-execution)

Reasoning chains must encode **actual epistemic work** (step-by-step proofs, computations, comparisons, constructions, conceptual analyses), not merely high-level dependencies or vague operations. Labels such as "derive", "explain", "decompose", "eliminate" are insufficient without the underlying operation and its operands.

*Source*: criteria-framework §Core requirements; criteria-framework §Insufficient fields.
