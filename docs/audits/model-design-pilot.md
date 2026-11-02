---
tags:
  - audit
index: "[gnomon audits](docs/audits/_index.md)"
aliases:
  - Audit - Model design (Pilot)
---
# Audit - Model design (Pilot)

> [!QUESTION] Goal: do the records of the [decision on answers, models and bindings](../adr/answers-models-bindings.md) hold four contrasting inquiries, and which resolutions of the [synthesis](model-design-synth.md) do these inquiries ratify, amend or leave open?

The pilot migrates four worked inquiries to the revised answer, the model record and the binding, in the order of the goal `model-design` of the [project goals](../../TODO.md). Each finding below names the inquiry that raised it, the defect or the open point, and its resolution, adopted or proposed. The decision absorbs the adopted resolutions when the pilot ends, and this note is then retired with the other audits.

## Neural tangent kernel

The inquiry states a theorem about a formal class, so its route runs on the target and its answer declares a use instead of a binding.

- **The block of model knowledge restated the claim.** The block held an expression and a reading of the consequence, which the claim of the core already states. *Proposed resolution*: the block keeps the form of the consequence and the obligations that it discharges, and the consequence is the claim of the core. The migrated answer leaves the two fields of the block empty until the decision settles the point.
- **The constants of a bound belong to the manifestation.** The synthesis left open whether the constant of a bound is a feature of the manifestation or a derived phenomenon. The migrated phenomenon declares each constant as a feature of the manifestation that holds its bound, beside the bound, its horizon and its mode of convergence. *Adopted resolution*: a constant of a bound is a feature of its manifestation, so the answer introduces no quantity of its own.
- **The checks read no answer and no model.** The vocabulary check read neither record kind, so an undeclared symbol in a claim passed every test. *Adopted resolution*: the check reads both kinds. An answer resolves its symbols against the records on which its route runs and against the question that it answers, with its target system, its phenomenon and its backgrounds; a model resolves against its parents and its background.
- **The expressions had no connectives.** A claim and a domain conjoin conditions, and the syntax admitted no conjunction. *Adopted resolution*: the canonical operators gain `and`, `or` and `not`, written infix or as a call.
- **The checks of realizations read the former key.** The check of a link read `realizations` at the root of the answer, whereas the revised answer holds them in its claim. *Adopted resolution*: the check reads `claim.realizations`.

## Active matter

The inquiry explores the phases of a formal class, on a model derived from the target by an idealization that removes the noise and an approximation near onset.

- **A derived model of a formal target needs no binding.** The claim bears on a formal class, and the operations of the derived model carry its relation to the target, with their classes of error. *Adopted resolution*: the answer declares its use, the binding test is not applicable, and the robustness test reads the errors of the operations.
- **The answer classifies the operations against its target.** The model types its two operations against its parent: `idealize` and `approximate`. Against the stochastic target, the answer reads the removal of the noise as an idealization and the linearization near onset as a condition of its domain. *Adopted resolution*: this division ratifies the rule of ownership of the synthesis under the decision, since only an answer classifies an assumption against its target.
- **A catalogue is a claim, not a law of the model.** The former answer stated the catalogue of phases as a law of role `measurement`. The revised answer states it as its claim, which reaches the manifestation of the phenomenon. *Adopted resolution*: this ratifies the answer that holds claims only.
- **An operation is a unit that a ground names.** A ground of the answer names an operation of the model by its identifier, which the reference check did not resolve. *Adopted resolution*: a reference reaches a unit by its symbol or by its identifier, for the operations and the assumptions of a model, the grounds and the abstractions of an answer, and the steps and the rules of a design.
- **The checks of a derived model.** *Adopted resolution*: two checks join the synthesis checks: an expression of a derived model uses no symbol that an operation retires, and each operation states its bound when its error is controlled, its regime when it is an approximation, and its order when it is a singular limit.
- **The requirements of a model assume a root model.** The registry requires constituents, variables and laws of every model, whereas a derived model keeps the symbols of its parents visible and declares only those that its operations yield. The migrated model declares no constituent. *Open point*: the requirements of a derived model, to settle when the checks read the requirements of models.

