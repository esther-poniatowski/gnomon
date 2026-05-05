# Structural quality

> [!INFO] Tier and axis
> **Tier 1 (framework-level desiderata) — structural axis.** This file fixes framework-level structural criteria that bind every aspect of the system. They are properties of *what the system is*, not properties of how layers compose (which are Tier 2). They cannot be overridden by architectural or aspect-specific decisions.

---

## Modularity and reusability ^t1-modularity

> [!INFO] Migrated to [reuse](_framework-criteria#^t1-reuse) and [addressability](_framework-criteria#^t1-addressability)

Specific epistemic achievements (one proof, one definition, one mechanism) must be able to support multiple questions without duplication. This entails:

- **addressability**: every epistemic content is referable by a stable identifier,
- **reuse**: the same object can participate in multiple inquiries, bundles, and outputs,
- **audience-independent stability**: expository notes are derived views, not primary stores.

*Source*: criteria-framework §Core requirements; problem-statement-approach §Approach.
