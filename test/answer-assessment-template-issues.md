---
tags:
  - examples
index: "[Theoretical modeling tests](test/_index.md)"
aliases:
  - Answer and assessment template issues
---
# Issues exposed by the answer and assessment trials

## Trial design

The suite uses one answer–assessment pair per epistemic aim. Five candidates are deliberately partial, so that an assessment must preserve valid local results while rejecting an overextended answer. The sixth candidate, the theorem on neural tangent dynamics, is the positive control: every applicable test and proof obligation passes.

| Aim | Candidate | Principal stress |
| --- | --- | --- |
| Exploration | [Catalogue of exceptional transitions](active-matter-phase-exploration/answer.yml) | a narrow discovered catalogue does not complete the declared search |
| Prediction | [Overshoot forecast from four elements](earth-system-tipping-cascades/answer.yml) | the forecast of a stylized model is not calibrated for the empirical target |
| Explanation | [Account through structured representations](grokking-delayed-generalization/answer.yml) | a transparent toy mechanism establishes neither an explanation that holds across the class nor a distribution of delays |
| Modal knowledge | [Theorem that feasibility implies stability](microbial-stable-coexistence/answer.yml) | sufficiency for one subclass must remain distinct from necessity over the full class |
| Description | [Snakes-and-ladders catalogue](swift-hohenberg-localized-states/answer.yml) | qualitative labels of features do not supply stability intervals resolved by coefficient |
| Model knowledge | [Uniform linearization theorem](neural-tangent-kernel-model-knowledge/answer.yml) | a successful theorem requires explicit hypotheses, bounds, horizons and modes of convergence |

## Global template issues

1. **Answer and assessment records are outside the validation pipeline.** `src/gnomon/vocabulary.py` excludes both record kinds from `RECORD_KINDS` and declares no answer blocks in `DECLARING`. The generated vocabularies therefore omit answer symbols, and the existing semantic checks do not inspect the new records.

2. **An answer cannot state its claim domain directly.** `variant` selects a target schema, but it cannot state the subclass that a theorem covers or a population of calibrated models. The field also cannot state a validity regime. The `idealization` block accepts only a deliberate *distortion*, so an ordinary hypothesis has no slot there either. Four answers therefore distribute their scope across several of their blocks, so the scope test must reconstruct a claim that no field owns.

3. **Nonexplanatory aims are forced into explanatory semantics.** The answer form requires an `explanans` for every aim and obliges each factor to `produce` an explanandum. Exploration and description instead return a catalogue, and prediction yields a forecast distribution. Their records can still identify the rules and the evidence that support those products, but the label *explanans factor* obscures the role of these items.

4. **Candidate values do not bind structurally to phenomenon outputs.** The answer can mention phenomenon symbols in laws and in `explanans.produces`. The variable references of an answer, however, are documented only for quantities of the target system. No block states that a candidate assigns a value to a phenomenon output. The Swift-Hohenberg catalogue and the bounds on neural tangent dynamics therefore assign values to outputs only indirectly, through laws.

5. **The gates of an assessment are implicit.** An assessment carries a verdict for each test but derives no overall disposition that states whether the answer satisfies the question. The gate on appraisal is equally implicit: appraisal is defined only for candidates that pass admissibility and warrant, yet the template requests one entry per preferred virtue and offers no `withheld` value. The grokking assessment must therefore state in a free-text field that its appraisal is withheld.

The five issues are defects of the framework, whereas the scientific reasons for each verdict belong to the individual cases and remain in their issue notes.
