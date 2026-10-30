---
tags:
  - definition
  - wip
index: "[Representations](docs/epistemology/definitions/representations/_index.md)"
aliases:
  - Framework
  - Conceptual framework
  - Linguistic framework
  - Formalism
  - Modelling framework
---
# Framework

> [!QUESTION] Goal: what does a framework fix that a theory does not, and which cognate notions does the term overlap?

A **framework** fixes the terms available to state laws, and asserts no law itself. Three senses of the term are standard:

- a linguistic framework fixes a vocabulary;
- an analytic framework fixes the elements of a domain and their general relations;
- a formalism fixes a calculus and a class of admissible model forms.

## Senses

| Sense | Community | Definition | Source |
| --- | --- | --- | --- |
| Linguistic framework | logical empiricism | a system of linguistic forms that introduces a kind of entity, together with rules for speaking of it; a question asked within the framework is *internal*, and a question about adopting the framework is *external* and practical | [carnap1950_empiricism] |
| Analytic framework | institutional analysis | the most general level of analysis: it identifies the elements and the general relations to be considered by an inquiry; it hosts several theories, each hosting several models | [ostrom2005] |
| Formalism, or modelling framework | mathematical modelling, philosophy of science | a calculus together with a class of admissible model forms, asserting no law about a target until it is bound to that target | [humphreys2004]; [knuuttila2016] |

Two notions name the forms of a formalism: a computational template is a mathematical form reused across domains [humphreys2004], and a model template is such a form transferred between disciplines [knuuttila2016]. Three formalisms recur in the theory of neural networks:

- the neural tangent kernel: the training of a network by gradient descent is described by a kernel that stays fixed in the limit of infinite width [jacot2018];
- tensor programs: a language expresses the computations of many architectures, and their Gaussian-process behavior at initialization is derived in the limit of infinite width [yang2019];
- the dynamical mean-field theory of random recurrent networks: the network is reduced to a self-consistent equation for one unit, exact as the number of units grows [sompolinsky1988].

Three cognate notions overlap the analytic sense. Each notion adds commitments left open by a framework in that sense:

| Notion | Content beyond the elements and relations | Source |
| --- | --- | --- |
| Disciplinary matrix | symbolic generalizations, metaphysical commitments, values and exemplars shared by a community | [kuhn1970] |
| Research programme | a hard core protected from refutation by a belt of auxiliary hypotheses, and a heuristic for revising the belt | [lakatos1970] |
| Research tradition | ontological and methodological commitments shared by a succession of theories | [laudan1977] |

## Distinctions

- **A framework, a theory and a model are ordered by generality.** A framework names the elements and relations [ostrom2005]. A theory makes general claims about the relations among some of those elements [ostrom2005]. A model fixes the values and forms needed to apply a theory to one case [ostrom2005]. The test is the kind of content: a framework asserts no empirical law. ^generality-order
- **A formalism asserts no law until it is bound to a target.** The consequences of a formalism hold of the model class fixed by its assumptions, such as infinite width or random connectivity. Binding the formalism to a target, such as a finite network trained on a task, turns those consequences into claims that can be false of the target. *Example*: the neural tangent kernel predicts a training trajectory for every network of its class. The kernel makes no claim about one finite network until a record claims that this network lies close to the limit.
- **An internal question presupposes the framework, whereas an external question is about it.** "Is there a prime number greater than 100?" is internal to the framework of numbers. "Are there numbers?" is external, and it reduces to the practical choice of adopting the framework [carnap1950_empiricism].

## Consequences for a record

- **The inquiry specification of this method is a framework for inquiries, not a framework of a domain.** An analytic framework names the elements of one domain, such as the actors and the rules of an institution [ostrom2005]. The inquiry specification names the elements of an *inquiry*: the target, the phenomenon, the question and its answers. A domain enters the specification only as the subject of an inquiry, so the specification is a meta-level framework. Therefore, the [generality order](#^generality-order) does not place the theories and models of a research problem below the specification. The records of an inquiry hold them, in background records and in candidate answers.
- **A formalism enters a record once it is bound to the target.** A law derived within a formalism that holds in a limit, such as the neural tangent kernel, carries the [warrant](../../subject/background.md#^law-warrant) `derived-in-a-limit`, and the [rule on limits](../../../specification/answer.md#^limit-rule) places the limit that binds the formalism to the target.
- **A question about the vocabulary of a record is external.** The usefulness of a declaration decides whether a record should declare a new kind of entity. The record itself cannot settle that question.

---
## Sources

Marks follow the [legend of reading marks](../../../../CONTRIBUTING.md#^reading-marks).

- [carnap1950_empiricism] ◐ [Carnap, "Empiricism, semantics, and ontology", *Revue Internationale de Philosophie* 4(11), 20–40, 1950](https://www.jstor.org/stable/23932367)
- [humphreys2004] ◐ [Humphreys, *Extending Ourselves: Computational Science, Empiricism, and Scientific Method*, Oxford University Press, 2004](https://academic.oup.com/book/11160); computational templates, construction assumptions and the correction set, checked through the publisher description and secondary sources
- [jacot2018] ◐ [Jacot, Gabriel & Hongler, "Neural tangent kernel: convergence and generalization in neural networks", *Advances in Neural Information Processing Systems* 31, 8571–8580, 2018](https://arxiv.org/abs/1806.07572); checked through the abstract
- [knuuttila2016] ◐ [Knuuttila & Loettgers, "Model templates within and between disciplines: from magnets to gases – and socio-economic systems", *European Journal for Philosophy of Science* 6(3), 377–400, 2016](https://doi.org/10.1007/s13194-016-0145-1); the transfer of the Ising model between disciplines, checked through the abstract; the definition of a model template was not checked; a correction appeared in vol. 13, art. 4, 2023
- [kuhn1970] ◐ [Kuhn, *The Structure of Scientific Revolutions*, 2nd ed., enlarged, University of Chicago Press, 1970](https://press.uchicago.edu/ucp/books/book/chicago/S/bo13179781.html); "Postscript—1969"
- [lakatos1970] ◐ [Lakatos, "Falsification and the methodology of scientific research programmes", in Lakatos & Musgrave (eds.), *Criticism and the Growth of Knowledge*, Cambridge University Press, 91–196, 1970](https://doi.org/10.1017/CBO9781139171434.009)
- [laudan1977] ◐ [Laudan, *Progress and Its Problems: Towards a Theory of Scientific Growth*, University of California Press, 1977](https://www.ucpress.edu/books/progress-and-its-problems/paper)
- [ostrom2005] ◐ [Ostrom, *Understanding Institutional Diversity*, Princeton University Press, 2005](https://doi.org/10.1515/9781400831739); ch. 1, section "Institutional Frameworks, Theories, and Models", p. 27
- [sompolinsky1988] ◐ [Sompolinsky, Crisanti & Sommers, "Chaos in random neural networks", *Physical Review Letters* 61(3), 259–262, 1988](https://doi.org/10.1103/PhysRevLett.61.259); checked through the abstract
- [yang2019] ◐ [Yang, "Tensor programs I: wide feedforward or recurrent neural networks of any architecture are Gaussian processes", *Advances in Neural Information Processing Systems* 32, 2019](https://arxiv.org/abs/1910.12478); checked through the abstract and the proceedings page
