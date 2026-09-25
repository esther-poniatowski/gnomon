---
role: definition
status: stable
index: "[Epistemology](docs/epistemology/_index.md)"
aliases:
  - Notation of the inquiry specification
  - Notation
tags: []
source:
---
# Notation of the inquiry specification

> [!QUESTION] Goal: which symbol denotes which quantity, across the notes of this method?

A single registry assigns every symbol of the method. One letter denotes one object, so that a formula reads the same in every note. ^registry

| Symbol                     | Denotes                                                    | Declared in                                          |
| -------------------------- | ---------------------------------------------------------- | ---------------------------------------------------- |
| $\Sigma$                   | the subject of inquiry, $\Sigma=\langle S,P,X,D\rangle$    | [subject of inquiry](subject-of-inquiry.md)          |
| $S$                        | the target system                                          | [target system](target-system.md)                    |
| $N$                        | the number of units of a kind in $S$                       | [target system](target-system.md)                    |
| $P$                        | the phenomenon, identified with the explanandum            | [phenomenon](phenomenon.md)                          |
| $Y$                        | an explanandum variable that expresses $P$                 | [phenomenon](phenomenon.md)                          |
| $X$                        | the contrast class, whose members are the foils            | [contrast](contrast.md)                              |
| $D$                        | the domain of conditions held fixed                        | [domain of conditions](domain.md)                    |
| $T$                        | the epistemic task, $T=\langle A,R,\mu,\lambda,\tau,\omega\rangle$ | [epistemic task](epistemic-task.md)                  |
| $A$                        | the epistemic aim                                          | [epistemic aim](epistemic-aim.md)                    |
| $R$                        | the requested relation                                     | [requested relation](requested-relation.md)          |
| $\mu$                      | the modal strength                                         | [modal strength](modal-strength.md)                  |
| $\lambda$                  | the admissible explanans                                 | [admissible explanans](admissible-explanans.md)         |
| $\tau$                     | the required accuracy                                      | [epistemic task](epistemic-task.md)                  |
| $\omega$                   | the proof obligations                                      | [epistemic task](epistemic-task.md)                  |
| $Q$                        | the question, $Q=\langle\Sigma,T\rangle$                   | [inquiry specification](inquiry-specification.md)    |
| $\Gamma$                   | the circumstances under which adequacy is judged           | [virtues](epistemic-pragmatic-virtues.md)            |
| $M$                        | a candidate answer, $M=\langle C,V,L,O,I,E\rangle$         | [answer form](answer-form.md)                        |
| $C$                        | the constituents: the units that the answer treats as bearers (in a mechanism, its components) | [answer form](answer-form.md); [mechanism](mechanism.md) |
| $V$                        | the terms: quantities, structures and properties           | [answer form](answer-form.md)                        |
| $L$                        | the laws and structural relations (in a mechanism, its activities and interaction rules) | [answer form](answer-form.md); [mechanism](mechanism.md) |
| $O$                        | the organization                                           | [answer form](answer-form.md); [mechanism](mechanism.md) |
| $I$                        | the idealizations of the analysis                          | [answer form](answer-form.md)                        |
| $E$                        | the explanans                                              | [answer form](answer-form.md)                        |
| $i$, $k$, $t$              | the index families of parts, of instances, and of the course, each admitting several indices | [phenomenon](phenomenon.md)                          |

- **A mechanism is written with the symbols of an answer.** A mechanism fills the fields of the answer form: its components are the constituents $C$, its activities and interaction rules are the laws $L$, and its organization is $O$. The [constituents of a mechanism](mechanism.md) therefore receive no private symbols. The [mapping onto the answer form](answer-form.md) states which aspect of a mechanism fills which field.

- **Subscripted and calligraphic letters stay free of the registry.** A letter that serves as an index, or that names a mathematical object local to one formula, does not enter the registry. Examples are the state space $\mathcal{X}_i$ of a component, its neighborhood $\mathcal{N}_i$, and a typed relation $\rho_k$ of an organization. The formula that introduces such a letter also fixes its meaning.

- **The records carry their own symbols, registered nowhere here.** A letter of the registry denotes a component of the method. By contrast, a [symbol of an inquiry](symbols-and-expressions.md) names a quantity of one studied system and is unique only within its record. A target system declaring $L$ for a length therefore collides with no entry of the registry.

- **The registry is a constraint on new notes.** A note that needs a symbol for a new quantity first adds a row to the registry, so that no letter denotes two quantities.
