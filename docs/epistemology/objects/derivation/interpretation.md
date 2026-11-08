---
tags:
  - theory
  - wip
index: "[Derivation](docs/epistemology/objects/derivation/_index.md)"
aliases:
  - Interpretation in a derivation
  - Interpretation of a derivation
---
# Interpretation in a derivation

> [!QUESTION] Goal: which meanings does a derivation assign to its formal items, and on what does each meaning rest?

An **interpretation** assigns a meaning to an item of a derivation. A derivation recording only its transformations states that its consequences follow, but not the meaning of those consequences. Physicists use mathematics to make meaning, and differently from mathematicians [redish2015]. The interpretations of a derivation record that meaning, item by item. Interpretations differ along two independent axes: the item interpreted, and the kind of meaning assigned. Each kind of meaning rests on its own kind of ground.

## Item interpreted

Five kinds of item bear an interpretation:

| Item | Definition | Example |
| --- | --- | --- |
| **object** | a symbol, a quantity, or one term of an expression | "this term is the rate of dissipation" |
| **expression** | an equation, an inequality, or a condition | "the solvability condition states that no forcing acts along the neutral mode" |
| **transformation** | a move: a change of representation, a limit, a projection | "the transform passes to the basis of the normal modes" |
| **feature of the calculation** | an event exhibited by the calculation: a divergence, a secular term, a zero mode, a change of sign, a crossing | "the secular term signals a missing slow drift" |
| **composite** | a segment, or a consequence with the moves supporting it | "this segment shows that the coupling between the two fields drives the instability" |

A feature of the calculation is an event exhibited at one object of the calculation, as a variable or a parameter varies. Five events are distinguished: ^feature-kinds

| Event | Definition | Example of a diagnostic reading |
| --- | --- | --- |
| **divergence** | an expression grows without bound in magnitude as a variable or a parameter approaches a value, finite or infinite | the outer expansion diverges as the distance to the wall vanishes, which marks a boundary layer |
| **secular term** | a correction term of a perturbation expansion grows without bound with an independent variable, usually time, until it becomes as large as a term of lower order, so that the expansion ceases to be asymptotic there [bender1999] | the secular term signals a missing slow drift |
| **zero mode** | a linear operator of the calculation has the eigenvalue zero, and a zero mode is an eigenvector for that eigenvalue | in a first-order linear flow, the amplitudes along the modes of zero rate stay constant, so they do not relax |
| **change of sign** | a quantity or a coefficient passes through zero and takes the opposite sign | the decay rate of the perturbation changes sign, so the stability posited fails beyond that value of the parameter |
| **crossing** | two quantities, neither identically zero, become equal, such as two eigenvalues or two rates, or a quantity reaches a threshold fixed by a premise | the slowest positive rate crosses the next one, so the gap that licensed the dominance of the slowest mode closes |

The events exclude one another. A growth without bound that meets the definition of a secular term is recorded as a secular term, not as a divergence, and a passage of one quantity through zero is a change of sign, not a crossing.

## Kind of meaning

Eight kinds of meaning differ by their content and by their ground:

| Kind | Content | Ground | Example |
| --- | --- | --- | --- |
| **referential** | the denotation of the item in a model, a background or the derivation | the declared symbols cited | the envelope is the amplitude of the pattern |
| **form** | a pattern of symbols in the item, read as a conceptual schema | the shape of the expression | two terms set equal read as two influences in balance |
| **process** | the mechanism or the relation described by the item | the laws or the relations of the organization cited | the equation weighs injection against dissipation |
| **structural** | the mathematical structure of the item | a named property | the transform diagonalizes an operator invariant under translation |
| **magnitude** | the relative size of the parts of the item: the dominant terms, the separated scales, the order of a correction | an expression of the ordering | the correction is of order $\varepsilon^{2}$ on times of order $\varepsilon^{-2}$ |
| **variation** | the change of a consequence when an item varies within a declared family | the stated variation and its effect | when the delay vanishes, the asynchronous state is stable |
| **analogical** | the form of a known object in the item, with a transfer of its behavior | the known law, design or source cited, with the shared features, the differing features, and the features of unknown correspondence | the spread of activity is analogous to diffusion, so its front should widen as the square root of time |
| **diagnostic** | the revelation carried by a feature of the calculation: the failure of an earlier move or posit, or a singular limit | the move, the posit or the limit revealed | the divergence marks the breakdown of the outer expansion |

Each kind rests on its sources as follows:

- **Form.** A **symbolic form** associates a pattern of symbols in an equation with a simple conceptual schema [sherin2001].
- **Magnitude.** A separation of scales uses scale in its [descriptive sense](../../vocabulary/quantities/scale-and-level.md), an extent and a resolution. A magnitude never concerns a scale of measurement.
- **Variation.** An explanatory proof rests on a characterizing property of an object of its theorem: a property unique to that object within a family [mancosu2023]. When that property varies, a deformation of the original proof proves each related theorem [steiner1978] [mancosu2023]. Therefore, a variation bears on a composite and not on a single move. A counterfactual about a mathematical object raises the difficulties of countermathematicals [mancosu2023]. A variation within a declared family avoids those difficulties. On a quantity of a model, a variation states the effect of an intervention [woodward2003].
- **Analogy.** An analogy has three parts. The positive part holds the shared features, the negative part holds the features known to differ, and the neutral part holds the features of unknown correspondence. The neutral part carries the predictions of the analogy [hesse1966].
- **Diagnosis.** A singular limit behaves otherwise than every system near it [batterman2002]. The breakdown of an expansion often signals such a limit, and a diagnostic interpretation records that signal.

## Pairs of item and kind

Not every kind of meaning applies to every item. The following pairs are admitted, and no other pair is admitted: ^admitted-pairs

| Item | referential | form | process | structural | magnitude | variation | analogical | diagnostic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| object | ✓ | | ✓ | ✓ | ✓ | | ✓ | |
| expression | | ✓ | ✓ | ✓ | ✓ | | ✓ | |
| transformation | | | ✓ | ✓ | ✓ | | ✓ | |
| feature of the calculation | | | | | | | | ✓ |
| composite | | | ✓ | ✓ | | ✓ | ✓ | |

A feature of the calculation takes only a diagnostic meaning, since it is an event of the reasoning and not an object of the model. A variation bears only on a composite, as the account of Steiner requires.

## Single homes

Three rules give each meaning one home among the units of a derivation:

- **The diagnostic interpretation is the home of a failure.** Three units cite the diagnostic interpretation of a failure, and none restates the failure: the [orientation](orientation.md) answering it, the [impasse](consequences-and-understanding.md) left by it, and the counterexample revealed by it.
- **A property licensing a move is stated once.** A structural or magnitude interpretation established before a move is cited by the [warrant](move.md#^applies-because) of that move, as the property that makes the warrant apply.
- **A referential meaning stays within the records.** A referential interpretation cites symbols of a model, of a background or of the derivation. A claim that a symbol of a model stands for a quantity of the target belongs to a [binding](../answer/model-and-binding.md#^map-versus-binding). The binding licenses that inference.

## Scope of a check

A check reads the ground of an interpretation, never its content. The check verifies three facts:

- the item interpreted exists;
- the pair of item and kind is admitted;
- the ground cites references of the type required by the kind.

The researcher judges whether the meaning is correct, as the [rule against inference](../../../adr/no-run-time-inference.md#^no-inference) requires.

---
## Sources

> [!NOTE] Status of the claims
> - **Established:**
> 	- meaning made with mathematics in physics, and symbolic forms;
> 	- the variation of a characterizing property and the deformations of a proof, and the difficulties of countermathematicals;
> 	- difference-making under intervention;
> 	- the positive, negative and neutral analogy, and singular limits, as cited;
> 	- secular terms in a perturbation expansion, as cited.
> - **Proposals:**
> 	- the five events of a feature of the calculation, and their precedence;
> 	- the two axes of interpretation: the five kinds of item and the eight kinds of meaning, with the ground of each kind;
> 	- the admitted pairs of item and kind;
> 	- the three single homes: of a failure, of a licensing property, and of a referential meaning.

Marks follow the [legend of reading marks](../../../../CONTRIBUTING.md#^reading-marks).

- [batterman2002] ○ [Batterman, *The Devil in the Details: Asymptotic Reasoning in Explanation, Reduction, and Emergence*, Oxford University Press, 2002](https://doi.org/10.1093/0195146476.001.0001); singular limits
- [bender1999] ◐ [Bender & Orszag, *Advanced Mathematical Methods for Scientists and Engineers I: Asymptotic Methods and Perturbation Theory*, Springer, 1999](https://doi.org/10.1007/978-1-4757-3069-2), first published by McGraw-Hill, 1978; ch. 11, "Multiple-scale analysis", pp. 544–576, the secular term of a naive expansion, pp. 545–551, checked through the [chapter record](https://econpapers.repec.org/RePEc:spr:sprchp:978-1-4757-3069-2_11) and the [article on multiple-scale analysis](https://en.wikipedia.org/wiki/Multiple-scale_analysis), which cites those pages
- [hesse1966] ○ [Hesse, *Models and Analogies in Science*, University of Notre Dame Press, 1966](https://philpapers.org/rec/REMAA); revised edition of the Sheed and Ward edition, London, 1963; positive, negative and neutral analogy
- [mancosu2023] ◐ [Mancosu, Poggiolesi & Pincock, "Mathematical explanation", *The Stanford Encyclopedia of Philosophy*, revised 2023](https://plato.stanford.edu/entries/mathematics-explanation/); §2.2.1, the deformations of a proof under a variation of its characterizing property, and the countermathematicals that threaten counterfactual accounts
- [redish2015] ◐ [Redish & Kuo, "Language of physics, language of math: disciplinary culture and dynamic epistemology", *Science & Education* 24(5–6), 561–590, 2015](https://doi.org/10.1007/s11191-015-9749-7); meaning made with mathematics in physics, checked through the [abstract](https://arxiv.org/abs/1409.6272)
- [sherin2001] ◐ [Sherin, "How students understand physics equations", *Cognition and Instruction* 19(4), 479–541, 2001](https://doi.org/10.1207/S1532690XCI1904_3); symbolic forms, each associating a conceptual schema with a pattern of symbols, checked through secondary summaries
- [steiner1978] ◐ Steiner, "Mathematical explanation", *Philosophical Studies* 34, 1978; the characterizing property of an explanatory proof, checked through [Mancosu, Poggiolesi & Pincock](https://plato.stanford.edu/entries/mathematics-explanation/)
- [woodward2003] ○ [Woodward, *Making Things Happen: A Theory of Causal Explanation*, Oxford University Press, 2003](https://doi.org/10.1093/0195155270.001.0001); difference-making under intervention
