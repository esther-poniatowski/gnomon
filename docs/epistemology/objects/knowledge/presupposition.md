---
tags:
  - theory
  - wip
index: "[Knowledge](docs/epistemology/objects/knowledge/_index.md)"
aliases:
  - Presupposition of a claim
  - Presupposition
  - Undischarged commitment
---
# Presupposition of a claim

> [!QUESTION] Goal: which commitments does a claim take for granted without asserting them, and how does an inquiry keep track of them?

A claim asserts its content, and it also takes some commitments for granted. *Example*: the claim that the delay scales as the inverse of the slowest positive rate takes for granted that a positive rate exists. Such a commitment is not a premise of the claim, and the claim does not state it. A commitment of this kind is a deferred obligation of the inquiry: the records state it and track its discharge, so that no claim absorbs it silently.

## Presupposition and ground

**A claim presupposes a statement when the claim and its denial both require that statement.** The test is the negation test of the semantic tradition: the presuppositions of a sentence are also presuppositions of its negation [beaver2021]. When a presupposition fails, the claim and its denial both lack a truth value, as Strawson argued against Russell for a definite description that refers to nothing [strawson1950] [beaver2021]. ^presupposition-test

A ground differs by that test. A [ground](grounds-and-dependence.md) supports the truth of the claim, so its failure leaves the denial of the claim open. A presupposition supports the claim and its denial alike, so its failure leaves neither of them true. *Example*: the delay scales as the inverse of the slowest positive rate, and the denial of that claim, both require that a positive rate exists. Therefore, the existence of that rate is a presupposition, whereas the relaxation law from which the scaling follows is a ground.

The same notion governs a question. A question presupposes every statement entailed by all of its direct answers [belnap1976], and a corrective answer denies such a presupposition, as the [forms of an answer](../answer/answer-form.md) state.

## Strengths of a commitment

A presupposition takes one of three strengths, ordered from the weakest:

- **local role**: the function of a term in the claim, such as a quantity taken as an attribute of a system; a local role commits the claim alone;
- **provisional commitment**: a statement of the background supporting the claim, such as the capacity of a system to bear that attribute; a provisional commitment binds the inquiry until a record establishes it;
- **axiom**: a statement of the whole corpus, such as every system of a class bearing that attribute; a law of a [background](background.md) or a concept record holds it for every inquiry admitting that record.

**A commitment is promoted only by an authored change.** A local role does not become a provisional commitment, nor a provisional commitment an axiom, because a tool infers it. The researcher raises the strength in the record, as the [rule against inference](../../../adr/no-run-time-inference.md#^no-inference) requires. ^strength-promotion

## Discharge

A presupposition is **discharged** when it names the record that holds it: a law, an answer, a concept, or a consequence of a derivation. An undischarged presupposition of the strength provisional commitment or axiom is a debt of the inquiry. The claim stays exposed to that debt, in the same way as it stays exposed to its premises under the [exposure rule](grounds-and-dependence.md#^weakest-link). A local role needs no discharge, since it commits the claim alone. ^presupposition-discharge

An axiom is held by a record of the whole corpus. Therefore, a presupposition of that strength names a law of a background or a concept record, and no other kind of record.

## Presupposition and existence

A presupposition of existence states a claim that can be false, such as the existence of a positive rate. Such a presupposition records no ontological status, so it agrees with the [decision on records neutral on existence](../../../adr/neutral-records-on-existence.md#^no-ontological-field). A record states such a presupposition with the binder `exists`, over the symbols that the claim names.

---
## Sources

> [!NOTE] Status of the claims
> - **Established:** the negation test of presupposition, the lack of a truth value when a presupposition fails, and the presuppositions of a question, as cited.
> - **Proposals:**
> 	- the distinction between a presupposition and a ground by the negation test;
> 	- the three strengths of a commitment, and their promotion by an authored change only;
> 	- the discharge of a presupposition by the record that holds it, and the exposure of a claim to its undischarged presuppositions.

Marks follow the [legend of reading marks](../../../../CONTRIBUTING.md#^reading-marks).

- [beaver2021] ◐ [Beaver, Geurts & Denlinger, "Presupposition", *The Stanford Encyclopedia of Philosophy*, substantive revision 2021](https://plato.stanford.edu/entries/presupposition/); §1.2 and §2, the negation test, and the Frege–Strawson view that a sentence whose presupposition fails lacks a truth value; the author line checked through a summary of the page
- [belnap1976] ◐ [Belnap & Steel, *The Logic of Questions and Answers*, Yale University Press, 1976](https://catalogue.bnf.fr/ark:/12148/cb353871722); a question modeled by its direct answers, and a presupposition entailed by every direct answer
- [strawson1950] ○ Strawson, "On referring", *Mind* 59(235), 320–344, 1950; a sentence with a definite description that refers to nothing lacks a truth value
