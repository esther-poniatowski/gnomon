# Operational quality

> [!INFO] Tier and axis
> **Tier 1 (framework-level desiderata) — operational axis.** This file fixes what the framework must allow operationally: the tolerances and capabilities the system must provide so that it remains usable, validatable, and implementable at research scale. They cannot be overridden by architectural or aspect-specific decisions.

---

## Partial formalization tolerance ^t1-partial-formalization

> [!INFO] Migrated to [partial formalization tolerance](_framework-criteria#^t1-partial-formalization)

The framework must support **partial formalization**: not every layer, field, or constraint is mandatory for every object. The criteria must specify, for each aspect, which properties are mandatory, which are optional, and what formal guarantees degrade under relaxation.

Without this, the framework is forced into a binary choice: either fully formal (prohibitively heavy) or fully informal (unvalidatable). Neither is compatible with actual research practice.

*Source*: architecture-2-audit §Formalization overhead vs. usability (identified as missing); overview-formal-frameworks §What no existing domain provides (identified as a genuine gap).

---

## Human and machine usability ^t1-dual-usability

The framework must be readable, writable, and controllable by humans **and** amenable to automation by deterministic programs and AI agents. Concretely this means:

- the representation supports multiple projections (formal, pedagogical, audit, automation) from the same underlying structure,
- the annotation burden scales with the desired guarantees, not with the framework itself,
- schema validation is mechanical and does not require human judgment.

*Source*: criteria-framework §Core requirements; workflow-2 §Phase 5 (narrative compression).

---

## Implementation feasibility and scale ^t1-feasibility

> [!INFO] Migrated to [system scale](_framework-criteria#^t1-system-scale). The annotation-cost clause is absorbed by [human action cost](_framework-criteria#^t1-human-action-cost) and [partial formalization](_framework-criteria#^t1-partial-formalization).

The framework must not impose excessive overhead, over-engineering, or heavy formalism relative to the research task it supports. It must scale to wide research projects (many questions, many objects, many versions, many contributors). This is a hard constraint, not an aspiration: the audit in architecture-2-audit explicitly flags the five-layer architecture as exceeding what antecedent formalisms require for the same use cases.

*Source*: criteria-framework §Core requirements; architecture-2-audit §Risks of overengineering.
