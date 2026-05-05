# Epistemic adequacy

> [!INFO] Tier and axis
> **Tier 1 (framework-level desiderata) — epistemic axis.** This file fixes what the framework must deliver in terms of *understanding*: the criteria distinguishing a reasoning system from a proof-checking system. They cannot be overridden by architectural or aspect-specific decisions.

---

## Intelligibility and understanding ^t1-intelligibility

> [!INFO] Migrated to [reasoning understandability](_framework-criteria#^t1-reasoning-understandability)

Reasoning moves must yield **genuine understanding**, not merely formal validity. This is the defining difference between a proof-checking system and a reasoning system. It requires three separable forms of justification to be representable simultaneously:

| Form                                      | Question answered                                                                | Determined by                                                                                                                                                                                                                                                                             | Examples                                                                                                                       |
| ----------------------------------------- | -------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------ |
| **Licencing** (inferential support)       | Why is the result *valid*, under which *warrant*?                                | The acceptability conditions of the operation itself: <br>- its **support** <br>- the **inferential pattern** it relies on                                                                                                                                                                | - a deduction is valid<br>- a statistics is significant                                                                        |
| **Strategic** (motivational support)      | Why is *this* move relevant now, rather than an admissible alternative?          | The macrostructure of the reasoning: <br>- the **gap** (what is currently lacking or blocked: the deficiency, obstacle, question)<br>- the **objective** (the local goal introduced to address the gap)<br>- the **rationale** (why it is the appropriate response now, over another one) | - it dissects a question into tractable parts<br>- it discriminates between two routes<br>- it isolates the decisive condition |
| **Explanatory** (intelligibility support) | Why does this move improve understanding, what cognitive change does it produce? | The cognitive **gain** the move contributes                                                                                                                                                                                                                                               | - it reveals the hidden mechanism<br>- it exposes a structural contrast  <br>- it shows *why* a phenomenon occurs              |

**Levels are stages in a reasoning.** A reasoning move is a state transition that carries the inquiry from a partial understanding to a greater articulation by a recognizable operation:

> problem state → diagnostic (gap) → strategic response (objective + rationale) → local transformation → newly intelligible state (gain)

The three levels are the minimal partition that lets a downstream reader reconstruct *why the inquiry advanced*, and not merely *that it did*.

**Independence of the levels.** The three classifications of a step are mutually independent, in the sense that no level determines another. Therefore, each must be recorded separately. 

*Examples*:

- The same step can be discriminative at the strategic level, case-splitting at the transformative level, and deductive at the licensing level; each classification varies independently of the others.
- A deductive move can address any kind of gap; a case-split can be licensed deductively, abductively, or heuristically.

> [!hint] Authoritative sources
> This decomposition draws on:
> - Toulmin's _claim–data–warrant–backing_ architecture
> - van Fraassen's analysis of _why-questions relative to contrast classes_
> - Polya's heuristic theory, the proof-strategic layer
> - Detlefsen's and Steiner's analyses of mathematical explanation: a proof that _convinces_ is not equivalent to a proof that _explains_, conviction follows from formal derivability while explanation requires that the inferential moves be grounded in the _distinguishing properties_ of the objects under consideration, and that the global structure be recoverable from local annotations.
