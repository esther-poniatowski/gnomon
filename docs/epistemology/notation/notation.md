---
tags:
  - theory
index: "[Notation](docs/epistemology/notation/_index.md)"
aliases:
  - Notation of the inquiry specification
  - Notation
---
# Notation of the inquiry specification

> [!QUESTION] Goal: which symbol denotes which quantity, across the notes of this method?

A single registry assigns every symbol of the method. One letter denotes one object, so that a formula reads the same in every note. ^registry

| Symbol                     | Denotes                                                    | Declared in                                          |
| -------------------------- | ---------------------------------------------------------- | ---------------------------------------------------- |
| $\pi$                      | an epistemic problem, $\pi=\langle K,d,\Phi\rangle$         | [epistemic problem](../inquiry/epistemic-problem.md) |
| $K$                        | the background of a problem: the accepted claims relative to which it is posed | [epistemic problem](../inquiry/epistemic-problem.md) |
| $H$                        | the proposed candidates, not yet accepted                  | [epistemic problem](../inquiry/epistemic-problem.md) |
| $d$                        | the demand of a problem, $d=\langle\mathsf{type},\mathsf{req},\Xi\rangle$ | [epistemic problem](../inquiry/epistemic-problem.md) |
| $\Xi$                      | the explicanda of a demand                                 | [epistemic problem](../inquiry/epistemic-problem.md) |
| $\Phi$                     | the constraints of a problem, $\Phi_1$ on each candidate and $\Phi^*$ on the set of results | [epistemic problem](../inquiry/epistemic-problem.md) |
| $\Sigma$                   | the subject of inquiry, $\Sigma=\langle S,P,X,D\rangle$    | [subject of inquiry](../subject/subject-of-inquiry.md)          |
| $S$                        | the target: the system, or the class of systems, that the inquiry is about | [target system](../subject/target-system.md)                    |
| $N$                        | the number of units of a kind in $S$                       | [target system](../subject/target-system.md)                    |
| $P$                        | the phenomenon, identified with the explanandum            | [phenomenon](../subject/phenomenon.md)                          |
| $Y$                        | an explanandum variable that expresses $P$                 | [phenomenon](../subject/phenomenon.md)                          |
| $X$                        | the contrast class, whose members are the foils            | [contrast](../subject/contrast.md)                              |
| $D$                        | the domain of conditions held fixed                        | [domain of conditions](../subject/domain.md)                    |
| $T$                        | the epistemic task, $T=\langle A,R,\mu,\lambda,\tau,\omega\rangle$ | [epistemic task](../epistemic-task/epistemic-task.md)                  |
| $A$                        | the epistemic aim                                          | [epistemic aim](../epistemic-task/epistemic-aim.md)                    |
| $R$                        | the requested relation                                     | [requested relation](../epistemic-task/requested-relation.md)          |
| $\mu$                      | the modal strength                                         | [modal strength](../epistemic-task/modal-strength.md)                  |
| $\lambda$                  | the admissible explanans                                 | [admissible explanans](../epistemic-task/admissible-explanans.md)         |
| $\tau$                     | the required accuracy                                      | [epistemic task](../epistemic-task/epistemic-task.md)                  |
| $\omega$                   | the proof obligations                                      | [epistemic task](../epistemic-task/epistemic-task.md)                  |
| $Q$                        | the question, $Q=\langle\Sigma,T\rangle$                   | [inquiry specification](../inquiry/inquiry-specification.md)    |
| $\Gamma$                   | the circumstances under which adequacy is judged           | [virtues](../epistemic-task/epistemic-pragmatic-virtues.md)            |
| $h$                        | a candidate answer, a member of the set $H$ of proposed candidates | [epistemic problem](../inquiry/epistemic-problem.md#^candidates) |
| $M$                        | a model, $M=\langle C,V,L,O\rangle$, which grounds the answers whose route runs on it | [model and binding](../../specification/model.md#^model-elements) |
| $C$                        | the constituents: the units that the model treats as bearers (in a mechanism, its components) | [model and binding](../../specification/model.md#^model-elements); [mechanism](../answer/mechanism.md) |
| $V$                        | the terms of the model: its variables and parameters       | [model and binding](../../specification/model.md#^model-elements) |
| $L$                        | the laws and structural relations of the model (in a mechanism, its activities and interaction rules) | [model and binding](../../specification/model.md#^model-elements); [mechanism](../answer/mechanism.md) |
| $O$                        | the organization of the model                              | [model and binding](../../specification/model.md#^model-elements); [mechanism](../answer/mechanism.md) |
| $I$                        | the idealizations among the grounds of an answer, each relative to the target of the answer | [answer form](../answer/answer-form.md#^idealizations)         |
| $E$                        | the explanans: the factors of the block of an explanation  | [answer form](../answer/answer-form.md#^explanation-block)     |
| $i$, $k$, $t$              | the index families of parts, of instances, and of the course, each admitting several indices | [phenomenon](../subject/phenomenon.md)                          |

- **A mechanism is written with the symbols of a model.** A mechanistic model fills the fields of the [model record](../../specification/model.md#^model-elements): its components are the constituents $C$, its activities and interaction rules are the laws $L$, and its organization is $O$. The [constituents of a mechanism](../answer/mechanism.md) therefore receive no private symbols. The [mapping onto the answer form](../answer/answer-form.md) states which aspect of a mechanism fills which field.

- **Subscripted letters, calligraphic letters and names set in sans-serif stay free of the registry.** Such a symbol serves as an index, or names a mathematical object local to one note. The formula that introduces the symbol also fixes its meaning. *Examples*:
    - the state space $\mathcal{X}_i$ of a component, and its neighborhood $\mathcal{N}_i$;
    - a typed relation $\rho_k$ of an organization;
    - the composition $\mathsf{Comp}(\sigma)$ of a system $\sigma$.

- **Bold letters are not used.** A structure or a class of structures is named in sans-serif, as the classes of models $\mathsf{M}_p$ and $\mathsf{M}$ of a [structuralist theory](../definitions/representations/theory.md).

- **The records carry their own symbols, registered nowhere here.** A letter of the registry denotes a component of the method. By contrast, a [symbol of an inquiry](../../specification/expressions.md) names a quantity of one studied system and is unique only within its record. A target system declaring $L$ for a length therefore collides with no entry of the registry.

- **The registry is a constraint on new notes.** A note that needs a symbol for a new quantity first adds a row to the registry, so that no letter denotes two quantities.
