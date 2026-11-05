---
tags:
  - theory
index: "[Knowledge](docs/epistemology/objects/knowledge/_index.md)"
aliases:
  - Presupposition of a claim
  - Presupposition
  - Undischarged commitment
---
# Presupposition of a claim

> [!QUESTION] Goal: which commitments does a claim take for granted without asserting them, and where does an inquiry record each one?

A claim asserts its content, and it also takes some commitments for granted. *Example*: the claim that the delay scales as the inverse of the slowest positive rate takes for granted that a positive rate exists. The claim does not assert that commitment, and a claim denying the scaling takes it for granted as well. An inquiry records each such commitment once and tracks its discharge, so that no claim absorbs it silently.

## Presupposition and ground

**The negation test diagnoses a presupposition.** A statement that a sentence and its negation both take for granted is a presupposition of the sentence [beaver2021]. The test is a diagnostic and not a definition, since a negation can deny a presupposition, as in "the king of France is not bald, since there is no king of France" [beaver2021]. ^presupposition-test

**A question presupposes the statements that all of its direct answers entail.** A direct answer is a complete and just sufficient answer to a question, and a question presupposes every statement entailed by all of its direct answers [belnap1976]. Therefore, when a presupposition of a question is false, every direct answer is false. Only a corrective answer is then correct, since it denies the presupposition, as the [forms of an answer](../answer/answer-form.md) state.

A ground differs from a presupposition by the effect of its failure. A [ground](grounds-and-dependence.md) supports the truth of the claim, so its failure leaves the claim without that support, and the negation of the claim may then be true. The failure of a presupposition leaves neither the claim nor its negation correct. *Example*: the relaxation law from which the scaling follows is a ground of the claim, whereas the existence of a positive rate is a presupposition.

A presupposition also differs from a ground of the role `condition`. A condition restricts the claim to the situations that satisfy it, so a situation outside the condition leaves the claim intact for the situations inside it. A presupposition bears on the terms of the claim instead. When it fails, a term of the claim refers to no object, and the claim describes no situation. Strawson held that a sentence whose definite description refers to nothing then makes no statement [strawson1950]. The method does not rely on that contested view: it records the failure as the failure of the answer, and assigns no truth value.

## Homes of a presupposition

Each presupposition has one home among the records:

- **The presuppositions of a question.** The question records them, in its field `presuppositions`, in its links of relation `presupposes`, or in the evidential status of its phenomenon, as the [question record](../../../specification/question.md) states. Every direct answer inherits them, so no claim restates them.
- **The existence that a condition presupposes.** A quantity defined by a condition presupposes a value satisfying that condition, as the [presupposition of existence](../../../specification/expressions.md#^condition-presupposes-existence) states. Every claim naming the quantity inherits that existence, so no claim restates it.
- **The further presuppositions of a claim.** A claim records the commitments that its own terms incur beyond the two homes above.
- **A presupposition that another answer establishes.** A relation of kind `presupposes` links the answer to the answer that establishes the commitment.

## Discharge

**A presupposition is discharged by the statement that establishes it.** A presupposition of a claim names that statement: a law of a [background](background.md) or of a model, or a consequence of a [derivation](../derivation/derivation.md). A concept discharges no presupposition, since its gloss fixes a meaning and asserts no property of its instances, as the [boundary of a concept](../../../specification/concept.md#^concept-boundary) states. An undischarged presupposition is a debt of the inquiry, and the answer stays exposed to it. A discharged presupposition passes on the exposure of the statement that holds it, as the [exposure rule](grounds-and-dependence.md#^weakest-link) states. ^presupposition-discharge

A presupposition is discharged by an authored change of the record only, since no tool infers that a statement holds a commitment, as the [rule against inference](../../../adr/no-run-time-inference.md#^no-inference) requires.

## Presupposition and existence

A presupposition of existence states a claim that can be false, such as the existence of a positive rate. Such a presupposition records no ontological status, so it agrees with the [decision on records neutral on existence](../../../adr/neutral-records-on-existence.md#^no-ontological-field). The binders `forall` and `exists` quantify over the indices of a declared index set, so an existence over an index set is stated with `exists`. An existence over another domain, such as the spectrum of an operator, is carried by the condition of the quantity that it introduces.

---
## Sources

> [!NOTE] Status of the claims
> - **Established:** the negation test as a diagnostic of presupposition, and the negation that denies a presupposition; the presuppositions of a question as the statements entailed by all of its direct answers, as cited.
> - **Contested, and not relied on:** the lack of a statement, or of a truth value, when a presupposition fails [strawson1950] [beaver2021].
> - **Proposals:**
> 	- the distinction of a presupposition from a ground and from a condition by the effect of its failure;
> 	- the four homes of a presupposition;
> 	- the discharge of a presupposition by a statement, and the exposure of an answer to its undischarged presuppositions.

Marks follow the [legend of reading marks](../../../../CONTRIBUTING.md#^reading-marks).

- [beaver2021] ◐ [Beaver, Geurts & Denlinger, "Presupposition", *The Stanford Encyclopedia of Philosophy*, substantive revision 2021](https://plato.stanford.edu/entries/presupposition/); §1.2 and §2, the negation test as a diagnostic, the negation that denies a presupposition, and the Frege–Strawson view that a sentence whose presupposition fails lacks a truth value; the author line checked through a summary of the page
- [belnap1976] ◐ [Belnap & Steel, *The Logic of Questions and Answers*, Yale University Press, 1976](https://catalogue.bnf.fr/ark:/12148/cb353871722); a question modeled by its direct answers, and a presupposition entailed by every direct answer
- [strawson1950] ○ Strawson, "On referring", *Mind* 59(235), 320–344, 1950; a sentence with a definite description that refers to nothing makes no statement
