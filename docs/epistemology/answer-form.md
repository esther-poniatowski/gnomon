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

The form of a candidate answer is derived from the [subject](subject-of-inquiry.md) and the [epistemic task](epistemic-task.md) of the inquiry, and constitutes one [layer of its specification](inquiry-specification.md).

> [!IMPORTANT] Conditions of satisfaction
> The tests that an answer must pass are stated before any candidate is evaluated [nosek2018]. These tests form the [conditions of satisfaction](satisfaction-conditions.md) of the answer.

> [!WARNING] The explanans is sought, not specified
> The answer form is distinct from the **subject of inquiry**. The subject of inquiry, as the initial research objective, usually *fixes* the system $S$, the phenomenon $P$, the contrast $X$ and the domain $D$. The *explanans* $E$ [hempel1948], in contrast, is generally *absent* from that objective. The inquiry attempts to discover the explanans, as a *component of the answer*.

## Form of the answer

A candidate answer proposes a model of the target system: ^answer-elements
$$M=\langle C,V,L,O,I,E\rangle $$
Each element is bounded by the specifications of the earlier layers.

| Element | When it is required | Content | Constraint on the element | Examples |
| ------- | ------------------- | ------- | ------------------------- | -------- |
| Statement | always | "[the claim of the answer]", as a reading | — | "unequal amplification of the activity modes makes the population synchronous rather than asynchronous" |
| Variant | when the members of the target declare different elements, and the answer accounts for only a subset of the class | the variant of the target that the answer accounts for, and one further variant for each of its parts with a narrower scope | the community that models its resources explicitly, where the account rests on the pools; the continuum realization | member schemas under one reference class [lundberg2021] |
| Constituents $C$ | always | the units that the answer treats as bearers | - either the [constituents declared for the system](target-system.md), or units defined by a stated map from them (e.g. coarse-graining, mode decomposition, aggregation, quotient by a symmetry); <br>- the organization $O$ and the terms $V$ range over these units | the excitatory and the inhibitory population (declared); the slow eigenmodes of the connectivity (derived) |
| Index sets | when a quantity of the answer is indexed by a set that the target does not declare | the set, its extent and its structure, in the format of a target system | a coarse-grained scale; a mode number | — |
| Variables | always, for each quantity that varies in the proposed model | each variable either references a quantity of the target, or carries its own signature, value set and construction in the same format | the population rate; the overlap with a stored pattern | — |
| Parameters | when the model holds a quantity fixed | the same content as for a variable, for each quantity that the model holds fixed while the phenomenon unfolds | the coupling strength; the adaptation timescale | — |
| Laws or structural relations $L$ | always | the dependences that link $V$ to the explanandum variable(s) $Y$ | - follow from the [laws of the system](target-system.md#^constituents), either exactly or, possibly in derived terms, within a limit recorded in the idealizations $I$; <br>- each law states its *warrant* (derived from those laws, derived in a limit, posited, fitted or measured) together with its grounds; <br>- as strong as the [modal strength](modal-strength.md) $\mu$ requires | the mean-field rate equations (derived in a limit); the stability condition that follows from them (derived); a transfer function obtained from recordings (fitted) |
| Organization $O$ | when the parts or the laws stand in a relation on which the phenomenon depends | per relation, the tuples that it connects and the laws that state it, in the format of a target system. The quantities that carry each relation are read from the expressions of those laws | - its constituents follow the [definition of a mechanism](mechanism.md) | a delayed feedback loop, in which excitation drives inhibition and is suppressed in return |
| Realizations | when the question bounds the explanans to the [link between two substrates](admissible-explanans.md) | per mapping, a quantity or law stated independently of any substrate, and the expression over the symbols of one substrate that realizes it [marr1982]; [bechtel2015] | the other elements of the answer declare both descriptions, so the mapping only names them | the membrane conductance that realizes a gating role |
| Idealizations $I$ | when the analysis introduces an assumption that the domain does not hold | the distortions that the analysis introduces to reach the laws $L$, and that bound the range over which the answer holds | - only assumptions absent from the [domain of conditions](domain.md#^analysis-assumptions) $D$; <br>- each with the [role that it plays](#^idealizations) (tractability, isolation or limit), the gain that it provides, and the range over which it holds | the mean-field limit (tractability: it closes the rate equations), valid for a large number of neurons; a model without adaptation (isolation: it removes a factor judged irrelevant to the oscillation) |
| Explanans $E$ | always, including for a nomological or a mathematical relation | the factors on which the answer rests:<br>- each stating its claim, the element on which it bears, the laws and relations that carry its effect, and the explanandum variable or manifestation that it accounts for;<br>- with the foils that it rules out, where [the question states a contrast](contrast.md), and no foil for the locus `none`;<br>- with the external systems to which it appeals, where the factor draws on the environment | - a claim about the terms: a *condition* on a quantity, a *property* of a structure or of a law, or a feature of the *organization*; <br>- separates the fact from each foil that it rules out, where [the question names a foil](contrast.md); <br>- bears the [requested relation](requested-relation.md) to the explanandum | the synaptic delay exceeds its critical value (condition); the connectivity has rank two (property of a structure); the transfer function saturates (property of a law) |


- **The explanans and the terms play different roles.** The terms $V$ supply the *vocabulary*. The explanans $E$ states the *claims* about that vocabulary on which the answer relies, including, where the question names a foil, the claims that separate the fact from it. *Example*: the synaptic delay is a term, and the explanans requires that this term exceed its critical value. A term may therefore appear in the laws $L$ without entering $E$. Such a term appears in the laws because the answer needs it to state a *dependence*, even when the term takes the same value for the fact and for a named foil.

- **The answer may re-individuate the system.** The [subject of inquiry](subject-of-inquiry.md) declares one decomposition of the system, under its original description. An answer may retain only some of the declared parts, or take other bearers (e.g. collective coordinates, modes, order parameters, effective units). An answer may do so because the parts of a system *result* from decomposition, a research strategy that can fail and be revised [bechtel1993]. By choosing its bearers, an answer adopts a *perspective* on the system. Such a perspective spans *several* levels of organization [wimsatt1994]. Different answers may thus adopt different perspectives, and several perspectives on one system, taken together, reveal its stable dependencies [massimi2022]. Because the bearers of an answer may differ from the declared ones, each constituent in $C$ states its map from the declared constituents, and each derived term likewise carries its definition. ^perspective

- **Derived terms change only the *vocabulary* of the answer.** A derived term is *defined* from the declared terms. Such a term can be eliminated by substituting its definition, so it proves no new claim about the declared terms [gupta2023]. A *rule stated in derived terms*, in contrast, may require a proof. If that proof holds only in a limit or under specific assumptions, then the answer records each such restriction among the idealizations $I$. ^derived-terms

- **Idealizations license the derivation and bound the claim.** An idealization is a distortion introduced on purpose, because the undistorted system is intractable [weisberg2007]. An idealization serves two functions. First, it lets the laws $L$ of the answer be derived from the [laws of the system](target-system.md#^constituents). Second, it restricts the range over which the answer holds. Each idealization names one of three roles: tractability, isolation or limit. For *tractability*, the idealization applies where the undistorted system admits no analysis. For *isolation*, the idealization removes a factor judged irrelevant. For a *limit*, the idealization exposes the behavior of a limit system. Each idealization also states the gain that it brings to the answer, since an assumption whose benefit cannot be named is not needed [weisberg2007]. Idealizations also differ in whether they can be removed. A controlled idealization is removed by *de-idealization*, in successive steps. Other idealizations are ineliminable: the model cannot be stated without these assumptions. For both kinds, the answer states the range over which the assumption holds, and the robustness test [checks whether the conclusion survives that idealization](satisfaction-conditions.md). ^idealizations

- **An answer names its explanans, including for a nomological or a mathematical relation.** The laws $L$ can reproduce the phenomenon by derivation without identifying its determinant. The answer must therefore name the property that makes the law, the structure or the derivation relevant (e.g. a symmetry, a conservation, a bound, a rank, a saturation). This requirement is essential for an answer that rests on a *constraint*: a fact more necessary than the ordinary laws, such as a symmetry or a conservation law [lange2016].

- **An answer names the members that it accounts for.** A class may hold members that declare different elements. An answer resting on a quantity that only some members carry accounts *only* for that subset. Such an answer names the variant that it accounts for. Each of its parts with a narrower scope names its own variant as well. A target system [declares its variants](target-system.md#^variants) by the same rule, as does [each entry of a phenomenon](phenomenon.md#^entries-hold-of-members). An answer naming no variant accounts for every member, so it may rest only on quantities that all of them carry. ^answer-names-its-members

- **An answer declares its model in the format of a target system.** The model is itself a system that stands in for the target: laws relate quantities that units bear and that take values over indices. The model is therefore declared with [the blocks and the keys of a target system](target-system.md). A quantity that the target already declares enters the model by reference. The value sets of the target format already carry every distinction that an answer draws, so no separate vocabulary is needed. Three elements, however, belong to the answer alone: the warrant of each proposed law, the idealizations of the analysis, and the factors of the explanans. A target system holds none of the three. ^answer-is-a-model

- **A link between two substrates is answered by a *mapping*.** A question that bounds the explanans to the link between two substrates asks how a role is realized. Neither of the two descriptions alone answers that question: the description specific to one substrate states the events without the role that they play, and the description independent of any substrate states the role without its carrier. The answer declares both descriptions in its ordinary blocks, since each of them consists of quantities and laws. The answer then states, per mapping, which expression over one substrate realizes which role. Only the mapping is new, so it occupies *one block* of the answer. ^link-is-a-mapping

- **A factor is a property, possibly stated in no record.** A factor rarely coincides with a declared element. Instead, the factor is a condition on such an element, or one of its properties. Such properties include a law that is invariant, additive or factorizing, a structure that is sparse or low-rank, and an arrangement that closes a feedback loop. Such a property is often *found* by the answer and absent from every earlier record. The answer therefore declares the property in its own model. A property of a law is declared as a law of the answer, and a property of a structure as a relation of its organization. A quantity that the property requires is declared in the answer as well. The factor then bears on the carrier of the property: a single element, or a family of elements. The key `holds`, in turn, states the property itself. Where the answer has found the property but cannot yet formalize it, `holds` stays open and a caveat states the gap. The record then keeps the finding without presenting it as a formula. ^factor-may-be-found

- **A factor states its *path* to the phenomenon.** A list of factors alone leaves unstated how each of them contributes: the same quantity may enter two accounts and support each of them for a different reason. A factor therefore states its claim and the element on which it bears. The factor also states the laws and [relations of the organization](target-system.md#^organization) that carry its effect, and the explanandum variable or manifestation that it accounts for. This chain consists of symbols that the records already declare, so a reader can follow it from the factor to the phenomenon. The steps that the chain leaves unstated, however, belong to the `procedure` of the factor. ^factor-states-its-chain

- **A factor supports the answer whether or not the question names a foil.** The answer relies on a determinant property that makes the phenomenon arise, whether the question names no foil or two. The case without a foil occurs in practice: three of the seven test inquiries state a [contrast](contrast.md) whose locus is `none`. For those three, an explanans defined as the difference between fact and foil cannot be filled. The claim of a factor therefore states the determinant on which the answer relies. The demand to separate fact from foil stays instead in the record of the contrast. Where a foil is named, a factor states which foils it rules out, and the contrast test compares that statement. ^explanans-is-not-only-contrastive

- **An answer may explain by the environment, and then names the external system on which it draws.** The external systems [pass the criterion for inclusion in the subject of inquiry](subject-of-inquiry.md#^inclusion-test). An answer may therefore explain the phenomenon by the structure of the inputs, or by the class of system that reads the outputs. Each factor that draws on the environment names the external system involved. The appeal then resolves to an [external system that the target declares](target-system.md). The answer reaches each quantity of that external system as a term under its own symbol, and never declares it a second time. ^explanans-appeals

- **The choice of terms determines [epistemic and pragmatic virtues](epistemic-pragmatic-virtues.md).** An answer may [pass the tests of admissibility and warrant](satisfaction-conditions.md) and still leave implicit the factors on which it rests. Its characteristic consequences then cannot be recognized without the full calculation [deregt2005]. The factors stay implicit because they may appear only in derived terms. Such factors express novel and robust behavior, yet remain deducible from the microscopic description [butterfield2011]. The retained terms therefore determine virtues such as economy, generality, structural transparency and intelligibility. *Example*: the question "how does a trained network solve this task?" is answered completely, in declared variables, by composing the local operations of every neuron across layers. The factors on which the answer rests, however, appear in a few collective coordinates of the population dynamics [vyas2020], in the eigenmodes of the connectivity, or in mean-field order parameters. An answer that re-individuates the system is therefore judged by the factors that it makes explicit. The [conditions of satisfaction](satisfaction-conditions.md) that the question already imposes perform that judgement.

## Specificities

The answer A to a why-question takes the form "$P$, in contrast to (the rest of) $X$ because $E$" [vanfraassen1980]. The answer statement fills that form with the elements of the model, in a sentence frame:

> In [S] under [D], [P] rather than [X], because [E], related to [Y] by [relation R] through [L], assuming [I].

*Example* of an explanatory answer:

- target system $S$: a network of excitatory and inhibitory neurons;
- background conditions $D$: under constant drive;
- explanandum $P$: synchronous oscillations at gamma frequency;
- contrast $X$: asynchronous activity under the same drive;
- explanans $E$: inhibitory feedback with a synaptic delay, destabilizing the asynchronous state;
- relation $R$ and laws $L$: a mathematical derivation, through the linear stability of the mean-field rate equations;
- idealizations $I$: the mean-field limit of infinitely many neurons.

For other aims, the statement delivers the [product of the aim](epistemic-aim.md) instead. *Examples*:

- a description states the values of $Y$ at the specified grain;
- a prediction states the value of $Y$ under a new condition, with its uncertainty.

When the [requested relation](requested-relation.md) is mechanistic or constitutive, the elements of the answer map onto the constituents of a [mechanism](mechanism.md):

| Constituent of a [mechanism](mechanism.md)                                       | Element of the answer                                                                                  |
| ---------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| components (entities)                                                              | the constituents $C$ of the answer, possibly other than those [declared for the system](target-system.md) |
| properties and states of the components                                            | the terms $V$                                                                                          |
| activities and interactions                                                        | the laws or structural relations $L$                                                                   |
| organization                                                                       | the organization $O$                                                                                   |
| the components, activities and organization that make the difference to $P$        | the explanans $E$                                                                                      |

In a reduced model, the components of the mechanism are the [re-individuated constituents](#^perspective): modes, collective coordinates or effective units, each carrying its defining map. The mechanism is then stated over those units, and the declared constituents appear only through that map.

For a nomological, statistical or mathematical relation, the organization $O$ stays empty, and the laws $L$ carry the law, the probabilistic dependence or the derivation.

---
## Sources

> [!NOTE] Status of the claims
> - **Established:** the account of each element of an answer, as cited.
> - **Proposals:**
> 	- the answer statement, combining the elements of the model with the subject of inquiry;
> 	- admitting derived terms and re-individuated constituents by their defining map;
> 	- the four kinds of factor (a condition on a quantity, a property of a structure, a property of a law, a feature of the organization);
> 	- requiring an explanans for every relation;
> 	- the mapping of the elements onto a mechanism, written in the [shared notation](notation.md).

Marks follow [the legend that states how each entry was checked](../../CONTRIBUTING.md#^reading-marks).

- [bechtel1993] ◐ [Bechtel & Richardson, _Discovering Complexity: Decomposition and Localization as Strategies in Scientific Research_, Princeton UP 1993; MIT Press 2010](https://direct.mit.edu/books/monograph/2860/Discovering-ComplexityDecomposition-and)
- [bechtel2015] ◐ [Bechtel & Shagrir, "The non-redundant contributions of Marr's three levels of analysis for explaining information-processing mechanisms", *Topics in Cognitive Science* 7(2), 2015](https://onlinelibrary.wiley.com/doi/10.1111/tops.12141)
- [butterfield2011] ◐ [Butterfield, "Less is different: emergence and reduction reconciled", _Foundations of Physics_ 41, 2011](https://philpapers.org/rec/BUTLID)
- [deregt2005] ◐ [de Regt & Dieks, "A contextual approach to scientific understanding", _Synthese_ 144, 2005](https://link.springer.com/article/10.1007/s11229-005-5000-4); criterion for intelligibility checked through secondary summaries
- [gupta2023] ✓ [Gupta & Mackereth, "Definitions", _SEP_, revised 2023](https://plato.stanford.edu/entries/definitions/), §2.3 on conservativeness and eliminability
- [hempel1948] ○ Hempel & Oppenheim, "Studies in the logic of explanation", _Philosophy of Science_ 15(2), 1948
- [lange2016] ◐ [Lange, _Because Without Cause: Non-Causal Explanations in Science and Mathematics_, OUP, 2016](https://global.oup.com/academic/product/because-without-cause-9780190269487), part I on explanations by constraint
- [lundberg2021] ✓ [Lundberg, Johnson & Stewart, "What is your estimand?", _ASR_ 86(3), 2021](https://journals.sagepub.com/doi/abs/10.1177/00031224211004187)
- [marr1982] ○ Marr, *Vision*, Freeman, 1982
- [massimi2022] ◐ [Massimi, _Perspectival Realism_, OUP, 2022](https://academic.oup.com/book/43074)
- [nosek2018] ◐ [Nosek, Ebersole, DeHaven & Mellor, "The preregistration revolution", _PNAS_ 115(11), 2018](https://www.pnas.org/doi/10.1073/pnas.1708274114)
- [vanfraassen1980] ✓ van Fraassen, _The Scientific Image_, ch. 5; [the chapter text](https://www.fitelson.org/290/vanfraassen_pte.pdf)
- [vyas2020] ◐ [Vyas, Golub, Sussillo & Shenoy, "Computation through neural population dynamics", _Annual Review of Neuroscience_ 43, 2020](https://www.annualreviews.org/content/journals/10.1146/annurev-neuro-092619-094115)
- [weisberg2007] ◐ [Weisberg, "Three kinds of idealization", _Journal of Philosophy_ 104(12), 2007](https://www.pdcnet.org/jphil/content/jphil_2007_0104_0012_0639_0659); de-idealization and ineliminable idealizations checked through [SEP, "Models in science"](https://plato.stanford.edu/entries/models-science/)
- [wimsatt1994] ◐ [Wimsatt, "The ontology of complex systems: levels of organization, perspectives, and causal thickets", _Canadian Journal of Philosophy_ 24(sup1), 1994](https://www.tandfonline.com/doi/abs/10.1080/00455091.1994.10717400)
