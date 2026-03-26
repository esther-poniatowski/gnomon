# Research Workflow

Staged pipeline definitions for mathematical research. The workflow separates
reasoning tasks into discrete phases with human control points.

Four passes cover the main pipeline stages:

| Pass | Responsibility |
| --- | --- |
| **Architect** | Scope, dependency hygiene, logical role |
| **Derivation** | Mathematical proofs and arguments |
| **Writing** | Pedagogical prose conversion |
| **Audit** | Contract and coherence verification |

The audit protocol ([audit-protocol.md](audit-protocol.md)) governs the mandatory
workflow for every note edit and every section draft. Quality enforcement phases
(linting, audit prompt usage) reference eutaxis as an external tool.

See `docs/design/methods/procedural-workflows.md` for the full workflow framework.
