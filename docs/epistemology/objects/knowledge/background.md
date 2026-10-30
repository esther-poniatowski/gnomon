---
tags:
  - theory
  - wip
index: "[Knowledge](docs/epistemology/objects/knowledge/_index.md)"
aliases:
  - Background
---
# Background

> [!QUESTION] Goal: which laws does an inquiry admit about its target before it seeks an answer, on what grounds, and how do they relate to the accepted knowledge of the inquiry?

The background record states a body of laws admitted beforehand about one [target system](../subject/target-system.md), with their closure and the organization: the relations among the parts or among the laws. *Beforehand* means that the inquiry admits the law before it seeks its answer, not that the law is known independently of experience. The origin of the law does not change this sense: a law derived, posited, fitted or measured is admitted alike. The target-system record delimits the target: it fixes the referent and declares the quantities. The background record states claims about those quantities, and each such claim can be false of the system.

The fields of the record are documented in the [background record](../../../specification/background.md).

- **A law of a background states what it does for the target by its role.** A law of a record is an admitted general claim about declared quantities, which need not be a law statement in the sense of lawhood, as the [law of a record](../../vocabulary/regularities/law.md#^law-of-a-record) states. In a background, each law carries a role, which states what the law does for the target, such as evolution, state constraint, input–output, measurement or initial distribution. ^law-of-record

- **An admitted law is a premise of the inquiry, and it need not be accepted.** A law is *admitted* when the inquiry takes it as a premise, with a stated warrant. A claim is *accepted* when the researcher makes it a member of the accepted knowledge $K$ of the inquiry, a component of the [state of an inquiry](../../foundations/inquiry-and-state.md#^state). The two attitudes vary independently. A law measured in a publication that the inquiry accepts is both admitted and accepted. A posited law is admitted and not accepted. An accepted claim enters a background record only once a question admits it about its target. Therefore, the state of an inquiry holds the background of each target beside $K$, rather than inside it. ^admitted-not-accepted

- **A law is kept apart from the declarations because only a law can be false.** A declaration introduces a symbol and its value set, and asserts nothing about the system. A law asserts a dependence among declared quantities, so new evidence can refute it. Therefore, the two kinds of content change at different rates: the delimitation of a target stays fixed while the admitted laws are revised. Separate records let a question replace a body of laws without restating the quantities that enter those laws. ^law-is-a-claim

- **The laws are admitted as given.** The record keeps the laws that the inquiry admits as relevant to characterizing the system, before it seeks its answer. The inquiry may nevertheless seek new laws. The closure of a body of admitted laws separates a formal target from an empirical one, and it decides what a new law may be. For a formal target, the laws define the system, so a new law must be derivable from them, for instance an effective equation obtained in a mean-field limit, which replaces the interactions of each unit by their average. For an empirical target, a new law may be independent of the admitted ones, for instance a newly discovered plasticity mechanism. *Example*: the Edwards–Anderson spin glass consists of $N$ Ising spins $s_i\in\{-1,+1\}$ on the sites of a lattice, interacting through random couplings $J_{ij}$ between neighboring sites. The target record declares the spins, the site positions and the couplings. The background record admits the energy $H=-\sum_{\langle ij\rangle}J_{ij}s_is_j$ as a law, where $\langle ij\rangle$ ranges over the pairs of neighboring sites [edwards1975]. The symbols $H$ and $J_{ij}$ are quoted in the form declared by the records of this example, under the [exception for the symbols of a record](../../vocabulary/notation/notation.md), so they do not take the meanings that the registry gives these letters. ^laws

- **Every law is admitted before the answer is sought, and its warrant names the grounds.** The grounds differ between laws. A law derived from other laws holds only as long as those laws hold. A law that is posited, fitted or measured rests on a choice, a fit or an instrument, so new evidence revises such a law first. The warrant is therefore a property of the *law*. The warrant also propagates along dependence: a result resting on a measured law inherits the exposure of that law to revision. An answer built on the result inherits that exposure in turn. A [model](../../../specification/model.md#^model-elements) states the warrant of its own laws in the same vocabulary. A [candidate answer](../../../specification/answer.md#^answer-elements) cites each law on which it rests, of the background or of a model, among its grounds with the role `warrant`, so a chain of dependence can be read from end to end. ^law-warrant

- **A relation among parts is internal to the target.** The external systems of the target fix its boundary, so they hold no relation whose ends both lie inside the target. Therefore, such a relation is stated in the organization. The organization names the laws stating the relation and the ordered tuples along which it runs. Those laws supply the quantities that carry the relation, namely the quantities indexed by every place of the relation. The target declares these quantities, so the organization declares none of its own. The reach comes last in each tuple, so the order of the components gives the direction. A tuple of three or more components states a joint relation. No pair of ends can state such a relation: two populations may together change the growth of a third without either population affecting it alone. ^organization

- **A relation whose ends are laws names and orders those laws, without a carrying quantity.** In a mechanism, the activities are organized as well as the parts [machamer2000] [craver2007]. Two laws may therefore stand in a relation: for example, one law may run only after another has completed, or hold only while another holds. Such a relation puts the reach last. No expression carries such a relation, because no quantity is indexed by a law. A relation between laws adds content only where the law expressions leave the order open. Where the laws share an index, that index already fixes the order. *Example*: a distribution stated at step zero beside an evolution written over the later steps. For this reason, a relation between laws is rarely needed. ^law-ends

---
## Sources

Marks follow the [legend of reading marks](../../../../CONTRIBUTING.md#^reading-marks).

- [craver2007] ◐ [Craver, *Explaining the Brain: Mechanisms and the Mosaic Unity of Neuroscience*, Oxford University Press, 2007](https://doi.org/10.1093/acprof:oso/9780199299317.001.0001)
- [edwards1975] ◐ Edwards & Anderson, "Theory of spin glasses", _Journal of Physics F_ 5, 965, 1975, via [a 2025 review of the field](https://arxiv.org/html/2505.24432)
- [machamer2000] ◐ [Machamer, Darden & Craver, "Thinking about mechanisms", *Philosophy of Science* 67(1), 1–25, 2000](https://doi.org/10.1086/392759); mechanisms as entities and activities organized to produce a phenomenon, checked through the [SEP entry on mechanisms in science](https://plato.stanford.edu/entries/science-mechanisms/)
