---
tags:
  - index
project: gnomon
aliases:
  - Framework-level criteria
---
# Tier 1 — Framework-level criteria

These criteria fix the overall objectives and desiderata that the framework must achieve as a whole. They are the success conditions for the project and cannot be overridden by architectural or aspect-specific decisions.

> [!TIP] Reading order
> Criteria are grouped by conceptual theme. Within each group, foundational criteria appear before derived ones. Cross-group dependencies flow downward.

| Theme                                                                 | Description                                                                                                                                                                                          |
| --------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [Framework foundation](framework-foundations.md)                      | What the framework *is* as a system: the language–tooling integration, what inquiry content it records, and what its scope deliberately excludes (no version history, no run-time inference engine). |
| [Expressive depth](expressive-depth.md)                               | What the framework must capture, support, and admit to reflect research reasoning, with what range and at what depth.                                                                                |
| [Reasoning integrity](reasoning-integrity.md)                         | Whether the reasoning system is valid, well-formed, and recoverable.                                                                                                                                 |
| [Modular content organization](modular-content-organization.md)       | How content is structured across the corpus so that each piece is named, locatable, and held in a single canonical place.                                                                            |
| [Research activities and workflows](research-activities-workflows.md) | How distinct research activities are partitioned and disciplined at run time.                                                                                                                        |
| [Cost and Ergonomics](cost-ergonomics.md)                             | Which cost dimensions the framework must keep bounded and the scale at which it must remain usable.                                                                                                  |

The four irreducible tensions between these framework-level criteria are recorded separately in [Irreducible tensions](_tensions.md): each names two opposing criteria and the resolution pattern the architecture adopts.
