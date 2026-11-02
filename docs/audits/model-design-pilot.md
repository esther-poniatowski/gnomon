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
