---
role: definition
status: wip
index: "[Epistemology](docs/epistemology/_index.md)"
aliases:
  - Order of specification
  - Controlled iteration
tags: []
source:
---
# Order of specification

> [!QUESTION] Goal: in which order is an inquiry specified, and how can an earlier choice be revised without circularity?

Specifying an inquiry appears circular at first. A question names a system and a phenomenon. Stating them seems to require a model of the system, while the choice of that model depends on the question. Three distinctions remove most of this circularity. The dependency that remains is handled by a revision governed by four conditions.

## Order of the stages

An inquiry is specified in five stages. Each stage takes the products of the earlier stages as given.

| Stage | Product | Level of commitment | Record |
| --- | --- | --- | --- |
| 1. Problem | the demand, its constraints and its explicanda | terms anchored by pointers | [problem](problem.md) |
| 2. Question schema | the questions that serve the problem, with typed placeholders, an aim and a contrast | slots typed | [question](subject-of-inquiry.md) |
| 3. Identified subject | the system and the phenomenon, each fixed by a definite description and pointers | slots `identified` | [target system](target-system.md), [phenomenon](phenomenon.md) |
| 4. Background and specified subject | the admitted laws, and the formal declarations of the system and the phenomenon | slots `specified` | [background](background.md) |
| 5. Candidate answers | the answers proposed to each question, and the models and bindings on which they rest | — | [answer form](answer-form.md), [model and binding](model-and-binding.md) |

The levels of commitment are defined in the note on [problems and questions](definitions/inquiry/problem-and-question.md#^commitment-levels). A change to an earlier stage, made after a later stage, is a revision. The [revision activities](definitions/activities/revision.md) type that change.

## Three distinctions that remove the circularity

**First, a question needs its terms identified, not specified.** A question can name the system and the phenomenon once their referents are fixed, before any model states their properties. The level `identified` fixes a referent by a definite description, as the [levels of commitment](definitions/inquiry/problem-and-question.md#^commitment-levels) state.

**Second, the model belongs to the background or to a model record, not to the subject.** Laws admitted in advance belong to the background. Constituents, laws and organizations proposed during the inquiry belong to a [model record](model-and-binding.md#^model-record), which every answer that rests on it cites. A phenomenon can be identified without the theory that explains it [bogen1988] [hacking1983]. The study of mechanisms accordingly characterizes the phenomenon before it builds any schema of a mechanism [craver2013].

**Third, an inquiry starts from a problem, not from a question** [dewey1938]. The first object of an inquiry is a [problem](definitions/inquiry/epistemic-problem.md): a demand that the accepted knowledge does not yet meet [nickles1981]. The questions are products of the second stage, derived from the problem, and they are typed before their terms are identified.

## The remaining dependency

One dependency survives the three distinctions. The boundary of the system and the observables kept depend on the question asked.

- The constituents of a mechanism are fixed relative to the phenomenon that the mechanism produces [craver2007].
- The relation that makes an answer relevant is fixed by the context of the question [vanfraassen1980].
- Delimiting a target system is already a step of modelling [elliottgraves2020].

The [inclusion criterion](subject-of-inquiry.md#^inclusion-test) bounds this dependency. A specification enters the subject only when it changes the types of the admissible answers or the presuppositions of the question. Therefore, only those specifications depend on the question, and every other specification can be fixed, or left out, without it.

## Controlled iteration

The remaining dependency is handled by mutual adjustment. Rules and inferences are amended against each other until they agree [goodman1955]. A system of knowledge improves through successive corrections that start from an initially affirmed system [chang2004]. ^controlled-iteration

The method imposes four conditions under which such an iteration is not circular:

1. **A starting point fixed independently of the outcome.** The first problem statement is written before any result is reconstructed, and it serves as the initially affirmed system from which corrections start.
2. **Provisional objects, with recorded revisions.** Every object carries a maturity, and every revision records its trigger.
3. **Tests that can fail.** A test that uses a provisional claim supports that claim only when the test could have returned a result against it [glymour1980].
4. **A convergence criterion.** The iteration stops when one full pass through the stages triggers no revision. The criterion detects that the iteration has stopped, and it does not guarantee that the iteration stops.

These four conditions are a proposal of this method, built from the sources above; no source states them in this form.

**Two senses of circularity.** Once records keep successive versions, each act reads versions that exist when the act runs and writes a later version, so the dependencies between versions have no cycle. This absence of cycle concerns the order of execution only, and it holds for a vicious iteration as well. An iteration is circular in *warrant* when a claim is supported by a test that uses the claim and could not have returned a result against it. Condition 3 excludes such a test [glymour1980]. Condition 3 is necessary for warrant, not sufficient: the 1980 formulation of bootstrap testing, which states it, also confirms hypotheses irrelevant to the evidence [christensen1983], and Glymour revised that formulation to exclude these cases [glymour1983]. Condition 1 serves a different purpose, since it keeps the problem statement independent of the results reconstructed under it. Versions serve conditions 2 and 4, since they make each revision traceable. A decomposition can contain cycles between questions, resolved by iteration, as the note on [question decomposition](question-decomposition.md#^cycles) states. Within one question, the [conditions of answerability](definitions/inquiry/conditions-of-answerability.md#^condition-dependencies) have no cycle, so these cycles arise between questions. A simultaneous dependency, such as two parameters identifiable only jointly, can also be resolved by a joint estimate instead of a sequence of versions. ^iteration-circularity

Two devices limit the revisions that an iteration requires:

- **Least commitment.** A choice is deferred until a condition requires it, so fewer choices need revision [weld1994]. A placeholder kept in a question schema is a deferred choice.
- **Recorded dependencies.** Each record keeps pointers to the versions from which it was derived. When a version is withdrawn, only the records that depend on it are marked for review. A truth-maintenance system revises beliefs in this way [doyle1979], and dependency-directed backtracking revises assumptions in the same way [stallman1977]. These pointers complement the trigger of condition 2: the trigger states why a revision occurred, and the pointers state which records the revision reaches. The [register of serving questions](question-decomposition.md#^register) records such dependencies, by the hypothesis on which each serving question is conditioned.

The records of gnomon do not keep versions yet. In particular, an itinerary step cannot reference a record at the state that the record had when the step ran, and the [project goals](../../TODO.md) list this missing reference as `as_of`.

## Restarting from existing results

A project can hold many results before any explicit question, when its work has followed topics rather than a problem. The specification of such a project combines two sources, in four steps:

1. **State the problem independently of the results.** The problem statement must be justified without the results, otherwise the reconstruction in step 2 only relabels the existing topics.
2. **Reconstruct the question that each result answers.** This step reconstructs a question from its answer, as a rational reconstruction of research [lakatos1971]. The reconstructed questions are grouped under candidate *principal questions*, as their *operative questions* [hintikka2007].
3. **Select the principal question.** The candidates retained are the principal questions that serve the problem, each with its coverage: the share of reconstructed questions that it groups. The researcher chooses one of them, by the [selection of questions](definitions/activities/problem-posing.md). The coverage informs that choice and does not decide it.
4. **Identify the subject.** Each placeholder is raised to the level `identified`, under the inclusion criterion.

A result that answers no operative question of the chosen principal question is set aside, not deleted. The share of results set aside measures how far the project has drifted from its problem.

---
## Sources

Marks follow the [legend of reading marks](../../CONTRIBUTING.md#^reading-marks).

- [bogen1988] ○ Bogen & Woodward, "Saving the phenomena", *Philosophical Review* 97(3), 303–352, 1988
- [chang2004] ◐ [Chang, *Inventing Temperature: Measurement and Scientific Progress*, Oxford University Press, 2004](https://doi.org/10.1093/0195171276.001.0001); epistemic iteration and the principle of respect
- [christensen1983] ○ Christensen, "Glymour on evidential relevance", *Philosophy of Science* 50(3), 471–481, 1983; the confirmation of hypotheses irrelevant to the evidence by the 1980 formulation of bootstrap testing
- [craver2007] ◐ [Craver, *Explaining the Brain*, Oxford University Press, 2007](https://philpapers.org/rec/CRAETB-2); constitutive relevance relative to a phenomenon
- [craver2013] ◐ [Craver & Darden, *In Search of Mechanisms*, University of Chicago Press, 2013](https://press.uchicago.edu/ucp/books/book/chicago/I/bo16123713.html); characterizing the phenomenon before building a schema
- [dewey1938] ◐ Dewey, *Logic: The Theory of Inquiry*, Henry Holt, 1938, ch. 6; checked through secondary sources
- [doyle1979] ○ Doyle, "A truth maintenance system", *Artificial Intelligence* 12(3), 231–272, 1979
- [elliottgraves2020] ◐ [Elliott-Graves, "What is a target system?", *Biology & Philosophy* 35:28, 2020](https://link.springer.com/article/10.1007/s10539-020-09745-3)
- [glymour1980] ○ Glymour, *Theory and Evidence*, Princeton University Press, 1980; bootstrap testing, which requires that a test could have yielded a negative instance
- [glymour1983] ○ Glymour, "Revisions of bootstrap testing", *Philosophy of Science* 50(4), 626–629, 1983
- [goodman1955] ○ Goodman, *Fact, Fiction, and Forecast*, Harvard University Press, 1955 (first edition Athlone, 1954); the mutual adjustment of rules and inferences
- [hacking1983] ◐ [Hacking, *Representing and Intervening*, Cambridge University Press, 1983](https://doi.org/10.1017/CBO9780511814563)
- [hintikka2007] ◐ [Hintikka, *Socratic Epistemology: Explorations of Knowledge-Seeking by Questioning*, Cambridge University Press, 2007](https://doi.org/10.1017/CBO9780511619298); principal and operative questions
- [lakatos1971] ○ Lakatos, "History of science and its rational reconstructions", *PSA 1970*, Boston Studies in the Philosophy of Science 8, 91–136, 1971
- [nickles1981] ◐ [Nickles, "What is a problem that we may solve it?", *Synthese* 47(1), 85–118, 1981](https://doi.org/10.1007/BF01064267); checked through a scanned copy of poor quality
- [stallman1977] ○ Stallman & Sussman, "Forward reasoning and dependency-directed backtracking in a system for computer-aided circuit analysis", *Artificial Intelligence* 9(2), 135–196, 1977
- [vanfraassen1980] ✓ van Fraassen, *The Scientific Image*, Clarendon Press, 1980, ch. 5; [the chapter text](https://www.fitelson.org/290/vanfraassen_pte.pdf)
- [weld1994] ○ Weld, "An introduction to least commitment planning", *AI Magazine* 15(4), 27–61, 1994
