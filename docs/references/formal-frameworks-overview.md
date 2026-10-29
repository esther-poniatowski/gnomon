---
tags:
  - reference
index: "[References](docs/references/_index.md)"
aliases:
  - Formal reasoning domains overview
---

# Internal Workings of Formal Reasoning Domains

## Organizational Schema

For each domain, four questions are addressed with technical precision:

1. **Knowledge model** — what constitutes the epistemic state; what entities are primitive
2. **Epistemic entities** — the typed objects the formalism manipulates
3. **State evolution** — how the knowledge state changes under reasoning
4. **Step selection** — the mechanism by which the next reasoning step is determined

Six domains are covered: proof theory, dependent type theory, classical AI planning, hierarchical task network planning, argumentation theory, and belief revision / dynamic epistemic logic.

## Comparative Analysis Across Domains

| Domain                | Epistemic State                   | Reasoning Step                     | Step Selection Mechanism                  | Handles "Why"                       |
| --------------------- | --------------------------------- | ---------------------------------- | ----------------------------------------- | ----------------------------------- |
| Natural deduction     | Context $\Gamma$, goal $\phi$     | Rule application                   | External (human / heuristic search)       | Intro/elim semantics only           |
| Dependent type theory | Typed context $\Gamma$, goal type | Tactic application                 | Goal-directed refinement                  | No — pragmatics external            |
| STRIPS/PDDL           | Ground atom set                   | Action application                 | Heuristic forward/backward search         | Causal links only                   |
| HTN planning          | World state + task network        | Decomposition / execution          | Method matching + precondition filter     | Decomposition tree                  |
| Dung / ASPIC+         | Argumentation framework           | Argument construction              | Dialogue protocol + strategy              | Warrant / backing                   |
| AGM revision          | Deductively closed belief set     | Expansion / contraction / revision | Rational postulates (no procedural model) | Minimal change principle            |
| DEL                   | Kripke model over worlds          | Announcement / action              | Event model application                   | Epistemic gain as world elimination |

## What No Existing Domain Provides

No existing formalism simultaneously provides:

1. **Stratified justification** — encoding of "why" at each granularity from strategic orientation to atomic derivation
2. **Partial specification tolerance** — admitting incompletely specified concepts and arguments as legitimate intermediate objects
3. **Unified validity conditions** — a single semantic framework that can accommodate both monotonic proof-theoretic steps and defeasible argumentative steps without forcing a choice between them
4. **Procedural epistemic gain** — a formal representation of the transition from not-understanding to understanding, not merely from not-knowing to knowing
