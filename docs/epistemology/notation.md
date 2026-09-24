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

Every note of this module draws its symbols from the table below. One letter denotes one thing, so that a formula can be read without knowing which note it comes from. ^registry

| Symbol                     | Denotes                                                    | Declared in                                          |
| -------------------------- | ---------------------------------------------------------- | ---------------------------------------------------- |
| $\Sigma$                   | the subject of inquiry, $\Sigma=\langle S,P,X,D\rangle$    | [subject of inquiry](subject-of-inquiry.md)          |
| $S$                        | the target system                                          | [target system](target-system.md)                    |
| $N$                        | the number of units of a kind in $S$                       | [target system](target-system.md)                    |
| $P$                        | the phenomenon, which is the explanandum                   | [phenomenon](phenomenon.md)                          |
| $Y$                        | an explanandum variable that expresses $P$                 | [phenomenon](phenomenon.md)                          |
| $X$                        | the contrast class, whose members are the foils            | [contrast](contrast.md)                              |
| $D$                        | the domain of conditions held fixed                        | [domain of conditions](domain.md)                    |
| $T$                        | the epistemic task, $T=\langle A,R,\mu,\lambda,\tau\rangle$ | [epistemic task](epistemic-task.md)                  |
| $A$                        | the epistemic aim                                          | [epistemic aim](epistemic-aim.md)                    |
| $R$                        | the requested relation                                     | [requested relation](requested-relation.md)          |
| $\mu$                      | the modal strength                                         | [modal strength](modal-strength.md)                  |
| $\lambda$                  | the admissible explanans                                 | [admissible explanans](admissible-explanans.md)         |
| $\tau$                     | the required accuracy                                      | [epistemic task](epistemic-task.md)                  |
| $Q$                        | the question, $Q=\langle\Sigma,T\rangle$                   | [inquiry specification](inquiry-specification.md)    |
| $\Gamma$                   | the circumstances under which adequacy is judged           | [virtues](epistemic-pragmatic-virtues.md)            |
| $M$                        | a candidate answer, $M=\langle C,V,L,O,I,E\rangle$         | [answer form](answer-form.md)                        |
| $C$                        | the constituents: the units the answer treats as bearers, which are the components of a mechanism | [answer form](answer-form.md); [mechanism](mechanism.md) |
| $V$                        | the terms: quantities, structures and properties           | [answer form](answer-form.md)                        |
| $L$                        | the laws and structural relations, which are the activities and interaction rules of a mechanism | [answer form](answer-form.md); [mechanism](mechanism.md) |
| $O$                        | the organization                                           | [answer form](answer-form.md); [mechanism](mechanism.md) |
| $I$                        | the idealizations of the analysis                          | [answer form](answer-form.md)                        |
| $E$                        | the explanans                                              | [answer form](answer-form.md)                        |
| $i$, $k$, $t$              | the index families of parts, of instances, and of the course, each admitting several indices | [phenomenon](phenomenon.md)                          |

- **A mechanism is written with the symbols of an answer.** A mechanistic answer is an answer, so its components are the constituents $C$, its activities and interaction rules are the laws $L$, and its organization is the organization $O$. The [mechanism](mechanism.md) note therefore declares no private symbols, and the [mapping of a mechanism onto an answer](answer-form.md) states which aspect fills which field, instead of translating one alphabet into another.

- **Subscripted and calligraphic letters stay free of the registry.** A letter that indexes or that names a mathematical object local to one formula does not enter the table: the state space $\mathcal{X}_i$ of a component, its neighborhood $\mathcal{N}_i$, a typed relation $\rho_k$ of an organization. These are read inside the formula that introduces them.

- **The records carry their own symbols, registered nowhere here.** A letter of this table denotes a component of the method, whereas [a symbol declared by an inquiry record](symbols-and-expressions.md) denotes a quantity of one studied system and is unique within that record alone. A target system declaring $L$ for a length therefore collides with no entry above.

- **The registry is a constraint on new notes.** A note that needs a quantity without a symbol adds a row here before using a letter, so that the letter is not already taken elsewhere.
