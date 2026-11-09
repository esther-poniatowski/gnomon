---
tags:
  - theory
index: "[Knowledge](docs/epistemology/objects/knowledge/_index.md)"
aliases:
  - Relations between research units
  - Incompatibility between answers
  - Contrast between answers
  - Warrant class of a relation
---
# Relations between research units

> [!QUESTION] Goal: which relations connect the units of an inquiry, what does each one mean, and how does a revision of one unit reach the units related to it?

A **relation between research units** connects records of one inquiry, or units inside them, such as an answer and the law on which it rests. It differs from two other kinds of relation. A relation in the object domain connects parts of the target system, such as the coupling between two populations, and a [background record](background.md) states it. A citation between documents connects notes of a workspace, whatever their content, and the vocabulary of that workspace types it. The [relation registry](../../../../src/gnomon/data/registries/relations.yml) declares the relations between research units, and this note owns their senses.

## Senses

| Term | Community | Definition | Source |
| --- | --- | --- | --- |
| Contradictories | logic | two propositions that cannot both be true and cannot both be false | [parsons2025] |
| Contraries | logic | two propositions that cannot both be true, and can both be false | [parsons2025] |
| Rebutting defeater | defeasible reasoning | a reason for believing the denial of a conclusion, as opposed to an undercutting defeater, which is a reason for doubting that the premises support the conclusion | [pollock1987] |
| Contrast | rhetorical structure theory | two situations comprehended as the same in many respects, differing in a few, and compared on those differences | [mann1988] |
| Antithesis | rhetorical structure theory | a presented situation incompatible with another, so that the reader favors the other | [mann1988] |
| Evocation of a question | erotetic logic | a set of declarative sentences evokes a question when it entails that some direct answer is true, and entails no single direct answer | [wisniewski2001] |
| Revision | provenance of data | a derivation whose resulting entity is a revised version of an original entity | [moreau2013] |
| Circular definition | theory of definitions | a definition whose definiens uses the defined term; a descriptive or explicative definition need not be non-circular | [gupta2023] |

## Relations of the method

The relations admitted between answers, between questions and between concepts are defined below. The relations that one record states by a field of its own, such as the question that an answer answers, are declared in the registry with the field that carries them.

- **Incompatibility.** A set of answers is `incompatible-with` when their claims cannot all be true over the domain that they share, whereas the claims of each proper subset can. The relation covers contradictories and contraries alike, so it is symmetric. Two answers form the smallest such set. Three or more answers can be incompatible together although any two of them are compatible, as three results whose conjunction is a paradox, so the relation holds of a set, not of pairs. ^incompatibility
- **Rebuttal.** An answer that rebuts another denies its claim, which is a rebutting defeater of that claim [pollock1987]. The fact about content is the incompatibility of the two claims, which `incompatible-with` states. Which answer was put forward against which is an event of the inquiry, which the [itinerary](../../processes/activities/epistemic-activities.md#^itinerary) records by its steps. A defence of an answer is no relation of its own. Defending an answer reinstates it by attacking its attacker, and the [decision against inference at run time](../../../adr/no-run-time-inference.md#^excluded-inference) excludes an engine computing such a reinstatement. A defence is therefore written as a `defeats` or an `incompatible-with` aimed at the attacker. ^rebuttal
- **Competition.** Two candidate answers to one atomic question compete, and the field `answers` that both carry already states it, so no relation is added. Competitors need not be incompatible: under a request that claims no completeness, two possible answers can both be true. ^competition
- **Contrast.** Two answers `contrasts-with` each other when they are comparable in many respects and differ in a stated respect, named by a quantity that both claims name, and both may hold [mann1988]. A pair that is incompatible is therefore not stated as a contrast. ^contrast
- **Instance.** An answer `exemplifies` a concept, or a more general answer, when its claim is a case that falls under the concept or under the general claim. The relation records an existing case, which an exposition may present as an illustration of the concept or of the general answer, as the form abstraction and instance of an elaboration does [mann1988]. A case that tests or establishes a claim is stated otherwise: a witness or a construction by a ground of the answer that it establishes, a counterexample by `defeats` or `incompatible-with`, and a boundary case by `tests`. ^instance
- **Motivation.** The motivation of a question is read where it arises. The records from which a question arises logically, in the sense of evocation [wisniewski2001], are the inputs of the step that formulated the question. The question that motivates the selection of a pattern of a phenomenon is stated by the field `pattern_selection.motivated_by` of that phenomenon. The rhetorical relation of motivation, which aims to raise the desire of a reader to act, concerns a presentation and belongs to `ekthesis`. ^motivation
- **Supersession.** A newer unit `revises` an earlier one when it replaces it, and the earlier unit stays unchanged [moreau2013]. Between answers, the relation `revises` is written on the newer answer, since the earlier one is never edited. A unit inside a record, such as one law of a background record, is superseded by a step of the itinerary. That step names the unit by its dotted identifier, and records the kind and the trigger of the revision. ^supersession
- **Co-definition.** A set of concepts is `co-defined-with` when the definition of each depends on the definitions of the others, and the set is admitted together [gupta2023]. A cycle of definitional dependence is admitted only among the members of one such set, as the [legitimate mutual constraint](../../../proposals/definitions-framework.md) describes it. ^co-definition

## Arity

A relation is **binary** or holds of a **set**. A binary relation connects a source and a target, and may carry an attribute that qualifies the pair, such as the respect of a contrast or the shared record of a link between questions. A set relation is symmetric and holds of two or more members, and its set is minimal: no proper subset of it is declared with the same relation. Incompatibility and co-definition hold of sets. Two other cases that exceed a pair are already stated without a set relation. The grounds that support a claim only together form a minimal set inside the answer, which its [dependence](../../../specification/answer.md) states. An attack on the inference from a ground to a claim, an undercut, targets the ground of role `warrant` by its identifier. ^arity

## Warrant classes and the transmission of a revision

A relation along which a revision is transmitted carries a **warrant class**, which decides the kinds of revision that flag the dependent at its other end. The warrant of an edge is a mode of inference, and each mode falls in one class, following the [split between explicative and ampliative inference](../../processes/activities/epistemic-activities.md#^explicative-ampliative): ^warrant-classes

- `monotonic`, for a deductive mode, since a deductive conclusion survives every addition to its premises [pollock1987];
- `defeasible`, for an ampliative mode, inductive, abductive, analogical, error-statistical or model-based, since new information can defeat its conclusion;
- `constitutive`, for a non-inferential dependence of meaning, where the dependent cannot be interpreted without the unit that it uses, as an answer cannot without its question.

| Class | Kinds of revision that flag the dependent |
| --- | --- |
| `monotonic` | retraction, narrowing of the scope, correction, taxonomic restructure |
| `constitutive` | the four kinds above, and reorientation |
| `defeasible` | all six kinds |

A deductive conclusion is flagged by a narrowing of the scope of a premise. Monotonicity protects it against added premises, not against a premise holding over less, and the conclusion loses its support outside the narrowed domain. A relation whose ends hold an entry of their own, such as an incompatibility, flags the record that holds the entry by every kind except a retraction, so that the entry is judged again. The class of an edge is fixed by its relation, written on its entry, or read from the dependent. An edge without a stated class counts as defeasible, so that an omitted field never lowers the set of flags. ^transmission

## Cycles

Each relation states whether its graph may hold a cycle:

| Relation | Cycle | Reason |
| --- | --- | --- |
| `revises`, `subquestion-of`, the descent of a model, the subsumption of concepts | forbidden | a lineage is ordered in time, and a part, a parent or a broader concept precedes the unit that it contains, produces or subsumes |
| the dependence of a definition on another | forbidden, except among the members of one co-definition | a circular definition is admitted only when declared |
| `supports`, `presupposes` between answers, the grounds and the requirements of a law, the uses of a derivation | judged | a cycle of grounds is circular in warrant only if its [tests cannot fail](../../processes/inquiry/specification-order.md#^iteration-circularity) |
| `presupposes` between questions | judged | a mutual presupposition makes the two presuppositions equivalent |
| `enables`, `defeats` | admitted | cycles between questions are resolved by iteration, and two answers may attack each other |

The relations whose cycles are judged form one graph of claims, so a cycle is found when it passes through several of them, such as a support, a ground and the requirement of a law. Each edge of that graph runs from the dependent unit to the unit on which it depends. A support therefore runs from the supported answer to the supporting one, the reverse of the direction in which the relation is written. A symmetric relation has no direction, so it holds no cycle; it is irreflexive, and it is written once for each pair or set. ^cycles

## Distinctions

- **A relation between research units differs from a typed citation between documents.** A citation between notes of a workspace may connect a decision to another decision, and may carry properties of a presentation, such as which end comes first in a text. A relation of this note connects units of research only, and carries no property of a presentation, which belongs to `ekthesis`.
- **Incompatibility differs from defeat.** `defeats` is directed and denies a ground of the other answer or the application of one of its laws, as the [relations between answers](grounds-and-dependence.md#^defeat) state, whereas incompatibility is symmetric and bears on the claims themselves.

---
## Sources

> [!NOTE] Status of the claims
> - **Established:** contradictories and contraries, rebutting and undercutting defeaters, contrast and antithesis as rhetorical relations, the evocation of a question, revision as a derivation of a revised version, and circular definitions, as cited.
> - **Proposals:**
> 	- incompatibility as a relation of a minimal set of answers, and rebuttal resolved into incompatibility;
> 	- competition read from the shared question, and contrast with a stated respect;
> 	- motivation read from the inputs of a step or from the selection of a pattern;
> 	- supersession written on the newer unit, and co-definition as a set exempting its cycles;
> 	- the three warrant classes, read from the mode of inference, and the kinds of revision that each class transmits;
> 	- the policy of cycles of each relation.

Marks follow the [legend of reading marks](../../../../CONTRIBUTING.md#^reading-marks).

- [gupta2023] ✓ [Gupta & Mackereth, "Definitions", _SEP_, revised 2023](https://plato.stanford.edu/entries/definitions/), §2.8 on circular definitions
- [mann1988] ◐ [Mann & Thompson, "Rhetorical Structure Theory: toward a functional theory of text organization", *Text* 8(3), 243–281, 1988](https://doi.org/10.1515/text.1.1988.8.3.243); the relations Contrast, Antithesis and Motivation, checked through the [definitions of the RST website](https://www.sfu.ca/rst/01intro/definitions.html)
- [moreau2013] ◐ [Moreau & Missier (eds.), *PROV-DM: The PROV Data Model*, W3C Recommendation, 30 April 2013](https://www.w3.org/TR/prov-dm/); §5.2.2 on revision
- [parsons2025] ◐ [Parsons & Ciola, "The Traditional Square of Opposition", _SEP_, revised 2025](https://plato.stanford.edu/entries/square/); the definitions of contradictories and contraries
- [pollock1987] ◐ [Pollock, "Defeasible reasoning", *Cognitive Science* 11(4), 481–518, 1987](https://doi.org/10.1207/s15516709cog1104_4); rebutting and undercutting defeaters, checked through the [SEP entry on defeasible reasoning](https://plato.stanford.edu/entries/reasoning-defeasible/), §1.1 and §4.1
- [wisniewski2001] ◐ Wiśniewski, "Questions and inferences", *Logique & Analyse* 173–175, 5–43, 2001; evocation of questions, pp. 5–19 read, Definition 8 on p. 17
