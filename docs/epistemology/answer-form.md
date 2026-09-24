---
role: definition
status: stable
index: "[Epistemology](docs/epistemology/_index.md)"
aliases:
  - Specifying the answer form
  - Answer form
tags: []
source:
---
# Specifying the answer form

> [!QUESTION] Goal: what form must an answer take, given the specified subject and task?

This [layer of inquiry](inquiry-specification.md) derives the form of a candidate answer from the [subject of inquiry](subject-of-inquiry.md) and the [epistemic task](epistemic-task.md). 

> [!IMPORTANT] Conditions of satisfaction
> The tests that a candidate must then pass are stated in advance, before any candidate is evaluated [nosek2018]: they form its [conditions of satisfaction](satisfaction-conditions.md).

> [!WARNING] The explanans is sought, not specified
> This layer should be distinguished from the **subject of inquiry**. In particular, the *explanans* $E$ (Hempel–Oppenheim) is generally *not part of the initial research objective*, alongside the system $S$, the phenomenon $P$, the contrast $X$ and the domain $D$. Usually, the latter are *fixed by the subject of inquiry*, whereas the explanans $E$ is a *component of the answer* that the inquiry is attempting to discover.

## Form of the answer

An answer can be described as a model: ^answer-elements
$$M=\langle C,V,L,O,I,E\rangle $$
Each element is bounded by the specifications of the earlier layers.

| Element | When it is required | Content | Constraint on the element | Examples |
| ------- | ------------------- | ------- | ------------------------- | -------- |
| Statement | always | "[what the answer says]", as a reading | "unequal amplification of the activity modes makes the population synchronous rather than asynchronous" | — |
| Variant | when the target holds members that differ in what they declare, and the answer accounts for one of them | the variant of the target the answer is about; a part of the answer narrower still names its own | the resource-explicit community, where the account rests on the pools; the continuum realization | member schemas under one reference class [lundberg2021] |
| Constituents $C$ | always | the units that the answer treats as bearers | - either the [constituents declared for the system](target-system.md), or units defined by a stated map from them (e.g. coarse-graining, mode decomposition, aggregation, quotient by a symmetry); <br>- the organization $O$ and the terms $V$ are stated over these units | the excitatory and the inhibitory population (declared); the slow eigenmodes of the connectivity (derived) |
| Index sets | when a quantity of the answer is indexed by a set the target does not declare | the set, its extent and its structure, as a target system declares one | a coarse-grained scale; a mode number | — |
| Variables | always, for what varies in the proposed model | each either referencing a quantity the target declares or carrying its own signature, value set and construction, as a target system declares one | the population rate; the overlap with a stored pattern | — |
| Parameters | when the model holds a quantity fixed | the same, for what the model holds fixed while the phenomenon unfolds | the coupling strength; the adaptation timescale | — |
| Laws or structural relations $L$ | always | the dependences that link $V$ to the explanandum variable(s) $Y$ | - either derivable from the [laws of the system](target-system.md#^constituents), or possibly in derived terms and within a limit recorded in the idealizations $I$; <br>- each one states its *warrant* — derived from those laws, derived in a limit, posited, fitted or measured — and what that warrant rests on; <br>- as strong as the [modal strength](modal-strength.md) $\mu$ requires | the mean-field rate equations (derived in the mean-field limit); the stability condition derived from them (derived); a transfer function fitted to recordings (fitted) |
| Organization $O$ | when the parts or the laws stand in a relation the phenomenon depends on | per relation, the tuples it runs along and the laws that state it, as a target system states its organization; what carries the relation is read from their expressions | - its constituents follow the [definition of a mechanism](mechanism.md) | the excitatory–inhibitory loop: excitation drives inhibition, inhibition suppresses excitation, with a delay |
| Realizations | when the question bounds the explanans to the [link between two substrates](admissible-explanans.md) | per mapping, the substrate-independent quantity or law it realizes and the expression over substrate-specific symbols that realizes it | both descriptions are declared in the blocks above, so the mapping names them rather than restating either | the membrane conductance that realizes a gating role | [marr1982]; [bechtel2015] |
| Idealizations $I$ | when the analysis introduces an assumption that the domain does not hold | the distortions that the analysis introduces to reach the laws $L$, and that bound where the answer holds | - only assumptions absent from the [domain of conditions](domain.md#^analysis-assumptions) $D$; <br>- each with the [role it plays](#^idealizations) — tractability, isolation or limit — what it buys, and the range over which it holds | the mean-field limit (tractability: it closes the rate equations), holding for large networks; a network without adaptation (isolation: it removes a factor judged irrelevant to the oscillation) |
| Explanans $E$ | always, including for a nomological or a mathematical relation | the load-bearing factors the answer relies on;<br>- each stating what it asserts, what it is a property of or a condition on, the laws and relations carrying its effect, and the explanandum variable or manifestation it accounts for;<br>- of one kind: a *condition* on a quantity, a property of a *structure*, a property of a *law*, or a property of the *organization*;<br>- with the foils it rules out, where [the question states a contrast](contrast.md), and none where its locus is `none`;<br>- with the external systems it appeals to, where the factor draws on the environment | - a claim about the terms: a *condition* on a quantity, a *property* of a structure or of a law, or a feature of the *organization*; <br>- differs between [fact and foil](contrast.md); <br>- bears the [requested relation](requested-relation.md) to the explanandum | the synaptic delay exceeds the critical delay (condition); the connectivity has rank two (property of a structure); the transfer function saturates (property of a law) |


- **The explanans and the terms play different roles.** The terms $V$ supply the *vocabulary*, whereas the explanans $E$ states which *claims* about that vocabulary make the difference between fact and foil. *Example*: the synaptic delay is a term; the explanans is the condition that this delay exceeds the critical value. A term may therefore appear in the laws $L$ without entering $E$: the answer needs it to state a *dependence*, although it takes the same value in the case of the fact and in the case of the foil.
	
- **The answer may re-individuate the system.** The [subject of inquiry](subject-of-inquiry.md) declares one decomposition of the system, through the prism under which the system was first defined. An answer may retain only some parts of the system, or treat other units as its bearers: collective coordinates, modes, order parameters, effective units. Decomposing a system into parts is a research strategy that can fail and be revised, rather than a fact read off the system [bechtel1993]. Perspectives cut across levels of organization instead of sitting within one [wimsatt1994], and a plurality of perspectives on one system makes its stable dependencies visible [massimi2022]. Therefore, the constituents $C$ of the answer carry the map from the declared constituents, as derived terms carry theirs. ^perspective
	
- **Derived terms change the vocabulary of the answer, not its content.** A derived term is *defined* from the declared ones, so can be eliminated by substituting its definition, and it proves no new claim about the declared terms [gupta2023]. In contrast, a *rule stated in derived terms* might require a proof. If such a derivation holds only in a limit or under specific assumptions, then the limit or assumptions must be recorded among the idealizations $I$. ^derived-terms

- **Idealizations license the derivation and bound the claim.** An idealization is a distortion introduced on purpose, because the undistorted system is intractable [weisberg2007]. It plays two parts: it licenses the passage from the [laws of the system](target-system.md#^constituents) to the laws $L$ of the answer, and it restricts the range over which the answer holds. Each one states which of three roles it serves — tractability, where the undistorted system resists analysis; isolation, where it removes a factor judged irrelevant; or limit, where it exposes the behavior of a limit system — and what the answer gains by it, since an assumption whose benefit cannot be named is one the answer does not need [weisberg2007]. A controlled idealization is removed by successive de-idealization, whereas others cannot be dropped without dismantling the model. In both cases, the answer states the range where the assumption holds, and the [robustness test](satisfaction-conditions.md) asks whether the conclusion survives it. ^idealizations

- **Naming an explanans is required, including for a nomological or a mathematical relation.** A derivation can reproduce the phenomenon without locating what produces it. Therefore, the answer must explicitly name the property that makes this law, this structure or this derivation the relevant one. *Examples*: a symmetry, a conservation, a bound, a rank, a saturation. This requirement is essential for explanations that involve a constraint rather than a causal condition, since their explanans is a fact more necessary than the ordinary laws, such as a symmetry or a conservation law [lange2016].

- **An answer says which members it accounts for.** A class may hold members that differ in what they declare, and an answer resting on a quantity only some of them have accounts for those members and not the class. It names that variant, and a part of it narrower still names its own, as the [target](target-system.md#^variants) and the [phenomenon](phenomenon.md#^entries-hold-of-members) do. An answer naming none accounts for every member, and may then rest on no quantity that only some of them carry — which is the same rule the laws of a target already obey, read on the answer's side. ^answer-names-its-members

- **A proposed answer is a model, and a model is a system.** What a candidate proposes is a system standing in for the target: units bearing quantities, quantities taking values over indices, and laws relating them. Its model is therefore declared with the blocks and the keys [a target system uses](target-system.md), and a quantity the target already declares is referenced rather than restated. A parallel vocabulary would have had to draw its own distinctions, and the ones it drew restated what the value sets already carried. What remains the answer's own is what a target has no reason to hold: the warrant of each proposed law, the idealizations the analysis introduced, and the factors the answer relies on. ^answer-is-a-model

- **A link is answered by a mapping, not by a third description.** A question bounding the explanans to the link between substrates asks how a role is realized, and neither description alone answers it: the substrate-specific one states what happens without saying which role it plays, and the substrate-independent one states the role without saying what carries it. The answer declares both in its ordinary blocks, since each is a set of quantities and laws like any other, and then states per mapping what realizes what. Only the mapping is new, which is why it is one block and not a second model. ^link-is-a-mapping

- **A factor is a property, and the property may be one nothing has stated.** What does the explanatory work is rarely a declared element itself: it is a condition on one, or a property of one — a law that is invariant, additive or factorizing, a structure that is sparse or low-rank, an arrangement that closes a feedback loop. Such a property is often what the answer *finds*, and until it is found no record names it. The answer therefore declares it, in the model it declares: a property of a law is a law of the answer, a property of a structure is a relation of its organization, and a quantity it needs is a quantity it declares. The factor then bears on what the property is a property of, which may be several elements where it is a property of a family, and `holds` states it. Where the answer has found the property and cannot yet formalize it, `holds` is open and a caveat says so, which records the finding without dressing it as a formula. ^factor-may-be-found

- **A factor states how it reaches the phenomenon, not only that it is relied on.** Naming what an answer relies on leaves the work the factor does unstated: the same quantity may be load-bearing in two accounts for different reasons. A factor therefore states what it asserts of the model, what it bears on, the laws and the [relations](target-system.md#^organization) that carry its effect onward, and the explanandum variable or manifestation it accounts for. The chain is made of symbols the records already declare, so a reader follows it from the factor to the phenomenon, and the procedure carries what the chain leaves unsaid. ^factor-states-its-chain

- **A factor is load-bearing whether or not anything is contrasted with it.** A determinant property that makes the phenomenon arise is what the answer relies on, and it is that in a question with no foil as much as in one with two: three of the seven inquiries state a [contrast](contrast.md) whose locus is `none`, and an explanans defined as what differs between fact and foil could not be filled for any of them. The claim therefore states what the answer relies on, and the contrastive demand is carried by the record that carries the contrast: where a foil is named, a factor says which foils it rules out, which is what the contrast test compares. ^explanans-is-not-only-contrastive

- **An answer may explain by the environment, and names which part of it.** The external systems pass the [inclusion test](subject-of-inquiry.md#^inclusion-test): an answer may explain the phenomenon by the structure of the inputs, or by the class of system that reads the outputs. A factor drawing on one names it, so the appeal resolves to an external system [the target declares](target-system.md) rather than resting on a paragraph. A quantity that system owns is reached as a term instead, under its own symbol, so the two are never written twice. ^explanans-appeals

- **The choice of terms determines [epistemic and pragmatic virtues](epistemic-pragmatic-virtues.md).** An answer may pass [admissibility and warrant](satisfaction-conditions.md), yet its load-bearing factors may stay hidden: its characteristic consequences cannot be recognized without the full calculation [deregt2005]. The load-bearing factors might appear only in derived terms, carrying novel and robust behavior while remaining deducible from the micro-description [butterfield2011]. Therefore, the retained terms determine virtues such as economy, generality, structural transparency, intelligibility. *Example*: "how does a trained network solve this task?" is answered completely, in declared variables, by the composition of the local operations of every neuron across layers. However, the load-bearing factors appear in a few collective coordinates of the population dynamics [vyas2020], the eigenmodes of the connectivity, or mean-field order parameters. A re-individuation is therefore judged by what it makes explicit, and not by a tier of its own: the [conditions of satisfaction](satisfaction-conditions.md) that the question already imposes carry it.

## Specificities

For a why-question (i.e. "$P$, in contrast to (the rest of) $X$ because $E$" [vanfraassen1980], whose schema writes the answer A), the answer statement fills a sentence frame with these elements:

> In [S] under [D], [P] rather than [X], because [E], related to [Y] by [relation R] through [L], assuming [I].

*Example* of an explanatory answer:

- target system $S$: a network of excitatory and inhibitory neurons,
- background conditions $D$: under constant drive;
- explanandum $P$: synchronous oscillations at gamma frequency;
- contrast $X$: asynchronous activity under the same drive;
- explanans $E$: inhibitory feedback with a synaptic delay, destabilizing the asynchronous state;
- relation $R$ and laws $L$: a mathematical derivation, through the linear stability of the mean-field rate equations;
- idealizations $I$: the mean-field limit of infinitely many neurons.

For other aims, the statement delivers the [product of the aim](epistemic-aim.md) instead. *Examples*: a description states the values of $Y$ at the stated grain; a prediction states the value of $Y$ under a new condition, with its uncertainty.

When the [requested relation](requested-relation.md) is mechanistic or constitutive, the answer form maps to the constituents of a  [mechanism](mechanism.md):

| Constituent of a [mechanism](mechanism.md)                                       | Element of the answer                                                                                  |
| ---------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| components (entities)                                                              | the constituents $C$ of the answer, which need not be those [declared for the system](target-system.md) |
| properties and states of the components                                            | the terms $V$                                                                                          |
| activities and interactions                                                        | the laws or structural relations $L$                                                                   |
| organization                                                                       | the organization $O$                                                                                   |
| the components, activities and organization that make the difference to $P$        | the explanans $E$                                                                                      |

In a reduced model, the components of the mechanism are the [re-individuated constituents](#^perspective): modes, collective coordinates or effective units, each carrying its defining map. The mechanism is then stated over those units, and the declared constituents appear only through that map.

For a nomological, statistical or mathematical relation, the organization $O$ stays empty, and the laws $L$ carry the law, the probabilistic dependence or the derivation. 

---
## Sources

> [!NOTE] What is established
> - **Established:** the account of each element of an answer, as cited.
> - **Proposals:** the answer statement that combines the elements of the answer with the subject of inquiry; admitting derived terms and re-individuated constituents by their defining map; the three kinds of term (quantity, structure, property); requiring an explanans for every relation; the mapping of the elements onto a mechanism, written in the [shared notation](notation.md).

Marks: ✓ the text itself was read · ◐ checked through an abstract, the publisher page or a secondary summary · ○ cited from standard knowledge, not fetched in this session.

- [bechtel1993] ◐ [Bechtel & Richardson, _Discovering Complexity: Decomposition and Localization as Strategies in Scientific Research_, Princeton UP 1993; MIT Press 2010](https://direct.mit.edu/books/monograph/2860/Discovering-ComplexityDecomposition-and)
- [butterfield2011] ◐ [Butterfield, "Less is different: emergence and reduction reconciled", _Foundations of Physics_ 41, 2011](https://philpapers.org/rec/BUTLID)
- [deregt2005] ◐ [de Regt & Dieks, "A contextual approach to scientific understanding", _Synthese_ 144, 2005](https://link.springer.com/article/10.1007/s11229-005-5000-4); criterion for intelligibility checked through secondary summaries
- [gupta2023] ✓ [Gupta & Mackereth, "Definitions", _SEP_, revised 2023](https://plato.stanford.edu/entries/definitions/), §2.3 on conservativeness and eliminability
- [lange2016] ◐ [Lange, _Because Without Cause: Non-Causal Explanations in Science and Mathematics_, OUP, 2016](https://global.oup.com/academic/product/because-without-cause-9780190269487), part I on explanations by constraint
- [massimi2022] ◐ [Massimi, _Perspectival Realism_, OUP, 2022](https://academic.oup.com/book/43074)
- [nosek2018] ◐ [Nosek, Ebersole, DeHaven & Mellor, "The preregistration revolution", _PNAS_ 115(11), 2018](https://www.pnas.org/doi/10.1073/pnas.1708274114)
- [vanfraassen1980] ✓ van Fraassen, _The Scientific Image_, ch. 5; [the chapter text](https://www.fitelson.org/290/vanfraassen_pte.pdf)
- [vyas2020] ◐ [Vyas, Golub, Sussillo & Shenoy, "Computation through neural population dynamics", _Annual Review of Neuroscience_ 43, 2020](https://www.annualreviews.org/content/journals/10.1146/annurev-neuro-092619-094115)
- [weisberg2007] ◐ [Weisberg, "Three kinds of idealization", _Journal of Philosophy_ 104(12), 2007](https://www.pdcnet.org/jphil/content/jphil_2007_0104_0012_0639_0659); de-idealization and ineliminable idealizations checked through [SEP, "Models in science"](https://plato.stanford.edu/entries/models-science/)
- [wimsatt1994] ◐ [Wimsatt, "The ontology of complex systems: levels of organization, perspectives, and causal thickets", _Canadian Journal of Philosophy_ 24(sup1), 1994](https://www.tandfonline.com/doi/abs/10.1080/00455091.1994.10717400)
