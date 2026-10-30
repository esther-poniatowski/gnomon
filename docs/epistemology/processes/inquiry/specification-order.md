---
tags:
  - theory
  - wip
index: "[Course of an inquiry](docs/epistemology/processes/inquiry/_index.md)"
aliases:
  - Order of specification
  - Controlled iteration
---
# Order of specification

> [!QUESTION] Goal: in which order is an inquiry specified, and how can an earlier choice be revised without circularity?

Specifying an inquiry appears circular at first. A question names a system and a phenomenon. Stating them seems to require a model of the system, while the choice of that model depends on the question. Three distinctions remove most of this circularity. The dependency that remains is handled by a revision governed by four conditions.

## Order of the stages

An inquiry is specified in five stages. Each stage takes the products of the earlier stages as given.

| Stage | Product | Level of commitment | Record |
| --- | --- | --- | --- |
| 1. Problem | the demand, its constraints and its explicanda | terms anchored by pointers | [problem](../../../specification/problem.md) |
| 2. Question schema | the questions that serve the problem, with typed placeholders, the epistemic task as far as it is fixed, and the locus of each contrast | slots typed | [question](../../../specification/question.md) |
| 3. Identified subject | the system and the phenomenon, each fixed by a definite description and pointers | slots `identified` | [target system](../../../specification/target-system.md), [phenomenon](../../../specification/phenomenon.md) |
| 4. Background and specified subject | the admitted laws, and the formal declarations of the system, the phenomenon and the foils of the contrast, each written when a condition requires it | slots `specified`, on demand | [background](../../../specification/background.md) |
| 5. Candidate answers | the answers proposed to each question, and the models and bindings on which they rest, as products of the inquiry | — | [answer](../../../specification/answer.md), [model](../../../specification/model.md), [binding](../../../specification/binding.md) |

The levels of commitment are defined in the note on [questions](../../objects/question/question.md#^commitment-levels). A change to an earlier stage, made after a later stage, is a revision. The [revision activities](../activities/revision.md) type that change.

Two stages are read with a qualification:

- **Stage 2 types the contrast.** A schema states where the foils differ from the fact, in the outcome, in the system or in the conditions, which is the locus of the contrast. The foils themselves are specified later, from the value space of the phenomenon, as the [filling order of the subject](../../objects/subject/subject-of-inquiry.md) states.
- **Stage 4 is entered on demand.** A slot is raised to the level `specified` only when an open condition needs the definiteness of its term, as the [choice of the next act](choice-of-act.md#^specified-on-demand) states. Each slot therefore enters stage 4 when a condition first requires it, and a question does not pass through stage 4 as a whole.

## Stages and layers

A question is specified by three layers: its subject $\Sigma$, its epistemic task $T$ and the virtues $\mathcal{V}$ that it weighs, as the [specification of a question](../../objects/question/question-specification.md) states. The stages order the work of an inquiry, and the layers sort the decisions that specify one question. The table places each layer in the stages. ^stages-and-layers

| Layer | Stages at which it is fixed |
| --- | --- |
| Subject $\Sigma$: the target system $S$, the phenomenon $P$ and the conditions held fixed $D$ | typed as slots at stage 2, identified at stage 3, specified at stage 4 on demand |
| Subject $\Sigma$: the contrast $X$ | its locus typed at stage 2; its foils specified at stage 4, from the value space of $P$ once $P$ is specified |
| Epistemic task $T$ | its aim fixed at stage 2, since the aim selects the interrogative word; its other components fixed at stage 2 or left open on purpose, and narrowed later by a recorded revision |
| Virtues $\mathcal{V}$ | chosen with the question at stage 2 or later, and fixed before any candidate of stage 5 is assessed, since a [constitutive virtue](../../objects/task/epistemic-pragmatic-virtues.md#^virtue-standing) enters the admissibility tests |

Stage 1 belongs to no layer: the problem supplies the demand from which the questions of stage 2 derive. The answer type and the conditions of satisfaction are not a layer either: they follow from the three layers, so they are fixed component by component as the layers are, before any candidate of stage 5 is assessed. The candidate answers of stage 5 are products of the inquiry, and no layer of the specification contains them.

## Three distinctions that remove the circularity

**First, a question needs its terms identified, not specified.** A question can name the system and the phenomenon once their referents are fixed, before any model states their properties. The level `identified` fixes a referent by a definite description, as the [levels of commitment](../../objects/question/question.md#^commitment-levels) state.

**Second, the model belongs to the background or to a model record, not to the subject.** Laws admitted in advance belong to the background. Constituents, laws and organizations proposed during the inquiry belong to a [model record](../../../specification/model.md#^model-record), which every answer that rests on it cites. A phenomenon can be identified without the theory that explains it [bogen1988] [hacking1983]. The study of mechanisms accordingly characterizes the phenomenon before it builds any schema of a mechanism [craver2013].

**Third, an inquiry starts from a problem, not from a question.** Dewey describes inquiry as starting from an indeterminate situation, which it first formulates as a problem [dewey1938]. The first object of an inquiry is a [problem](../../objects/problem/epistemic-problem.md): a demand that the accepted knowledge does not yet meet [nickles1981]. The questions are products of the second stage, derived from the problem, and they are typed before their terms are identified.

## The remaining dependency

One dependency survives the three distinctions. The boundary of the system and the observables kept depend on the question asked.

- The constituents of a mechanism are fixed relative to the phenomenon that the mechanism produces [craver2007].
- The relation that makes an answer relevant is fixed by the context of the question [vanfraassen1980].
- Delimiting a target system is already a step of modelling [elliottgraves2020].

The [inclusion criterion](../../objects/subject/subject-of-inquiry.md#^inclusion-test) bounds this dependency. A specification enters the subject only when it changes the types of the admissible answers or the presuppositions of the question. Therefore, only those specifications depend on the question, and every other specification can be fixed, or left out, without it.

## Controlled iteration

The remaining dependency is handled by mutual adjustment. Rules and inferences are amended against each other until they agree [goodman1955]. A system of knowledge improves through successive corrections that start from an initially affirmed system [chang2004]. ^controlled-iteration

The method imposes four conditions under which such an iteration is not circular:

1. **A starting point fixed independently of the outcome.** The first problem statement is written before any result is reconstructed, and it serves as the initially affirmed system from which corrections start.
2. **Provisional objects, with recorded revisions.** Every object carries a maturity, and every revision records its trigger.
3. **Tests that can fail.** A test that uses a provisional claim supports that claim only when the test could have returned a result against it [glymour1980]. Glymour states this requirement within bootstrap testing, which tests a hypothesis with evidence interpreted through other parts of the same theory.
4. **A convergence criterion.** The iteration stops when one full pass through the stages triggers no revision. The criterion detects that the iteration has stopped, and it does not guarantee that the iteration stops.

These four conditions are a proposal of this method, built from the sources above; no source states them in this form.

**Two senses of circularity.** Once records keep successive versions, each act reads versions that exist when the act runs and writes a later version, so the dependencies between versions have no cycle. This absence of cycle concerns the order of execution only, and it holds for a vicious iteration as well. An iteration is circular in *warrant* when a claim is supported by a test that uses the claim and could not have returned a result against it. Condition 3 excludes such a test [glymour1980]. Condition 3 is necessary for warrant, not sufficient: the 1980 formulation of bootstrap testing, which states it, also confirms hypotheses irrelevant to the evidence [christensen1983], and Glymour revised that formulation to exclude these cases [glymour1983]. Condition 1 serves a different purpose, since it keeps the problem statement independent of the results reconstructed under it. Versions serve conditions 2 and 4, since they make each revision traceable. A decomposition can contain cycles between questions, resolved by iteration, as the note on [question decomposition](question-decomposition.md#^cycles) states. Within one question, the [conditions of answerability](conditions-of-answerability.md#^condition-dependencies) have no cycle, so these cycles arise between questions. A simultaneous dependency, such as two parameters identifiable only jointly, can also be resolved by a joint estimate instead of a sequence of versions. ^iteration-circularity

Two devices limit the revisions that an iteration requires:

- **Least commitment.** A choice is deferred until a condition requires it [weld1994], so fewer choices need revision. A placeholder kept in a question schema is a deferred choice, and a slot that enters stage 4 on demand is another.
- **Recorded dependencies.** Each record keeps pointers to the versions from which it was derived. When a version is withdrawn, only the records that depend on it are marked for review. A truth-maintenance system tracks dependencies in the same way, and relabels the dependent beliefs automatically [doyle1979]. Dependency-directed backtracking uses recorded dependencies to retract only the assumptions behind a contradiction [stallman1977]. These pointers complement the trigger of condition 2: the trigger states why a revision occurred, and the pointers state which records the revision reaches. The [register of serving questions](../../../procedures/inquiry/decomposing-a-question.md#^register) records such dependencies, by the hypothesis on which each serving question is conditioned.

Versions and recorded dependencies presuppose records that keep successive versions. Whether the records keep them is stated with the [itinerary record](../../../specification/itinerary.md#^record-versions).

The specification of a project that already holds many results before any explicit question is stated in the [procedure of restarting from existing results](../../../procedures/inquiry/restarting-from-results.md).

---
## Sources

Marks follow the [legend of reading marks](../../../../CONTRIBUTING.md#^reading-marks).

- [bogen1988] ◐ [Bogen & Woodward, "Saving the phenomena", *Philosophical Review* 97(3), 303–352, 1988](https://doi.org/10.2307/2185445)
- [chang2004] ◐ [Chang, *Inventing Temperature: Measurement and Scientific Progress*, Oxford University Press, 2004](https://doi.org/10.1093/0195171276.001.0001); epistemic iteration and the principle of respect
- [christensen1983] ◐ [Christensen, "Glymour on evidential relevance", *Philosophy of Science* 50(3), 471–481, 1983](https://doi.org/10.1086/289130); the confirmation of hypotheses irrelevant to the evidence by the 1980 formulation of bootstrap testing
- [craver2007] ◐ [Craver, *Explaining the Brain: Mechanisms and the Mosaic Unity of Neuroscience*, Oxford University Press, 2007](https://doi.org/10.1093/acprof:oso/9780199299317.001.0001); constitutive relevance relative to a phenomenon
- [craver2013] ◐ [Craver & Darden, *In Search of Mechanisms: Discoveries across the Life Sciences*, University of Chicago Press, 2013](https://press.uchicago.edu/ucp/books/book/chicago/I/bo16123713.html); characterizing the phenomenon before building a schema
- [dewey1938] ◐ [Dewey, *Logic: The Theory of Inquiry*, Henry Holt, 1938](https://search.worldcat.org/oclc/229987); ch. 6; checked through secondary sources
- [doyle1979] ◐ [Doyle, "A truth maintenance system", *Artificial Intelligence* 12(3), 231–272, 1979](https://doi.org/10.1016/0004-3702(79)90008-0)
- [elliottgraves2020] ◐ [Elliott-Graves, "What is a target system?", *Biology & Philosophy* 35(2), article 28, 2020](https://doi.org/10.1007/s10539-020-09745-3)
- [glymour1980] ◐ Glymour, *Theory and Evidence*, Princeton University Press, 1980; bootstrap testing, which requires that a test could have yielded a negative instance
- [glymour1983] ◐ [Glymour, "Revisions of bootstrap testing", *Philosophy of Science* 50(4), 626–629, 1983](https://doi.org/10.1086/289143)
- [goodman1955] ◐ Goodman, *Fact, Fiction, and Forecast*, Harvard University Press, 1955; first edition Athlone Press, 1954; the mutual adjustment of rules and inferences; checked through the [SEP entry on Goodman](https://plato.stanford.edu/entries/goodman/)
- [hacking1983] ◐ [Hacking, *Representing and Intervening: Introductory Topics in the Philosophy of Natural Science*, Cambridge University Press, 1983](https://doi.org/10.1017/CBO9780511814563)
- [nickles1981] ◐ [Nickles, "What is a problem that we may solve it?", *Synthese* 47(1), 85–118, 1981](https://doi.org/10.1007/BF01064267); checked through a scanned copy of poor quality
- [stallman1977] ◐ [Stallman & Sussman, "Forward reasoning and dependency-directed backtracking in a system for computer-aided circuit analysis", *Artificial Intelligence* 9(2), 135–196, 1977](https://doi.org/10.1016/0004-3702(77)90029-7)
- [vanfraassen1980] ◐ [van Fraassen, *The Scientific Image*, Clarendon Press, 1980](https://doi.org/10.1093/0198244274.001.0001); ch. 5, read in its abridged reprint, "The pragmatic theory of explanation", in Pitt (ed.), *Theories of Explanation*, Oxford University Press, 1988, 136–155 ([PDF](https://www.fitelson.org/290/vanfraassen_pte.pdf))
- [weld1994] ◐ [Weld, "An introduction to least commitment planning", *AI Magazine* 15(4), 27–61, 1994](https://www.cs.uky.edu/~sgware/reading/papers/weld1994introduction.pdf); deferring decisions, p. 34
