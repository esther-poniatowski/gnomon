# Audit Protocol

This file is the **operational contract**. It governs the mandatory workflow for every note edit and every section draft. No text is returned before this protocol completes.

---

## Critical warning

Do not use fluency, conventional mathematical tone, or resemblance to textbook prose as evidence of compliance. Standard patterns in textbooks and journal articles — nominalization, passive indirection, heavy compound terms, imperative openings, proofs before interpretation — are the primary failure modes to guard against, not acceptable defaults. Apply every check mechanically to every sentence, including:

- carried-over text from source notes (the single highest source of missed violations, because it already "sounds right")
- Markdown link texts (every link text is a sentence and must pass all checks independently)
- callout bodies and contribution bullets
- bold-label paragraphs

---

## Mandatory generation workflow

Execute every phase in order. Do not return output until Phase 7 passes.

---

### Phase 0 — Scope decision

Before drafting, decide exactly one of the following:

- **Derivation mode**: the full derivation belongs in this note; include setup, derivation, result, interpretation, and boundary cases
- **Pointer mode**: only a pointer belongs here; write a single linking sentence and cross-link to the source note

Do not mix both modes in the same note. If content currently exists in both modes, decide which to keep and delete the other.

---

### Phase 1 — Structure pass

Before drafting any prose, establish:

1. The central question (for `[!QUESTION]`)
2. The contribution bullets (for `[!QUOTE] Originality`): each must satisfy Operator 2 — **[mathematical object] + [active verb] + [result]**
3. The roadmap items (for `[!TIP] Roadmap`): each names a section's role in the reasoning chain, not a result
4. The assumptions (for `[!WARNING] Applicability`)
5. The block anchors required by downstream cross-references
6. Whether a summary table is needed (required when the note derives results across multiple cases)

Verify the contribution/roadmap separation: if a roadmap item states a result or novelty claim, move it to contributions. If a contribution bullet describes the reasoning path without stating a result, move it to the roadmap.

---

### Phase 2 — Draft pass

Write the body in dependency order within each section:

1. Purpose and problem statement
2. Setup and definitions
3. General derivation
4. Result statement
5. Interpretation
6. Specializations and examples
7. Failure modes and boundary cases

After completing each section, verify the section dependency chain: what does this section receive from the preceding section? If the answer is "nothing", reorder or add a missing connecting step.

---

### Phase 3 — Sentence audit

For every sentence in the draft — including sentences carried over from earlier drafts, link texts, callout bodies, and bold-label paragraphs — apply the following seven checks in order. Do not rely on whether the sentence "sounds wrong."

**Check 1 — Nominalization**
Identify every noun ending in `-tion`, `-ment`, `-ness`, `-ity`, `-ence`, `-ance`, `-al`, `-ing` used as a process noun. For each: is the verb form shorter or more direct? If yes, apply Operator 1. Check subject position specifically — process nominalizations as sentence subjects are not exempt.

**Check 2 — Abstract framing**
Does the sentence describe the act of establishing a result instead of stating the result? Does it contain a vague procedural nominalization without its operands? Does any noun phrase referring to a process leave its arguments implicit? Apply Operator 2 and the implicit-argument rule.

**Check 3 — Compound modifier**
Does any hyphenated pre-nominal modifier encode a prepositional or clausal relationship (`-dependent`, `-determined`, `-driven`, `-weighted`, `-modulated`)? Apply Operator 3. Does any sequence stack two or more such modifiers? Expand unconditionally.

**Check 4 — Imperative opening**
Does the sentence begin with `Define`, `Let`, `Assume`, `Write`, `Set`, or `Denote`? Rewrite in declarative form.

**Check 5 — Named symbol**
Does any symbol appear after a preposition, in a qualifier, in a condition, or in a monotonicity statement without its object name? Apply Operator 4.

**Check 6 — Link text**
For every Markdown link `[text](target)`: does the link text name (a) a container note, (b) a procedure or analysis, or (c) an abstract property nominalization? Apply Operator 5.

**Check 7 — Display reference**
Does the sentence immediately following a `$$…$$` block begin with `It`, `This`, `They`, or `These` without a descriptive noun phrase? Replace with a named reference.

---

### Phase 4 — Structural audit

After completing the draft, verify at paragraph and section level:

**Section dependency.** For each section after the first: what does it receive from the preceding section? If nothing, either the section is misplaced or a connecting step is missing.

**Paragraph dependency.** For each paragraph after the first in a section: would removing the preceding paragraph break this one? If not, a logical connector is missing or the preceding paragraph is redundant.

**Preview–conclusion redundancy.** If a section opens with a preview of the result and closes with a restatement of it, delete one. Do not state the same result at both ends of a section.

**Contributions–body redundancy.** Does any body paragraph restate a `[!QUOTE] Contributions` bullet without adding new interpretive content? If yes, delete the restatement or compress it to a back-reference.

**Takeaway justification.** Does a concluding paragraph add mechanistic implications, limiting cases, or connections to other results beyond the formal statement? If it only restates the result in words, delete it.

**Callout dispatch.** Does the `[!QUESTION]` body describe what the note achieves? (Move to Contributions.) Does a `[!TIP] Roadmap` item announce a result or novelty claim? (Move to Contributions.) Does a `[!QUOTE] Contributions` bullet describe the reasoning path without stating a result? (Move to Roadmap.)

---

### Phase 5a — Forbidden string search

Search the final Markdown text for each of the following strings outside code blocks. Any match requires revision before proceeding.

```
the role of
the nature of
the act of
it can be shown
it is possible to show
plays a role in
is responsible for
serves to
is involved in
Define
Let
Assume
Write
Set
Denote
Note that
Observe that
Recall that
More explicitly
Equivalently
This gives
Therefore:
Hence:
Then:
in ... ways
```

Additionally search for the pattern `the .* case` (the X case as a noun phrase) and rewrite to the prepositional form.

### Phase 5b — Semantic audit

Search for semantic equivalents of forbidden patterns even when the
literal string is absent. Revise any sentence that:

- places a process nominalization as the grammatical subject with an
  existence verb ("Differential amplification occurs when …")
- names a derivation procedure as the grammatical object of a note-
  or section-centered sentence
- uses a relation noun — comparison, coupling, independence, variation,
  modulation — without naming the operands
- uses a link text that names a procedure, container, or analysis rather
  than a result or object

---

### Phase 6 — Optional automated checks

If a project-local writing checker is configured, run it on all modified files
and fix all reported issues before proceeding.

Automated checks are supplementary. They can catch imperative openings,
forbidden phrases, procedural link text heuristics, bare-symbol patterns after
prepositions, and similar local violations, but they do not replace the manual
checks in Phase 3 and Phase 5.

---

### Phase 7 — Output gate

Return the text only when all of the following are true:

- Phase 3: no sentence fails any of the seven checks
- Phase 4: no structural redundancy or callout dispatch violation remains
- Phase 5: no forbidden string appears outside code blocks
- Phase 6: any configured automated checker reports no issues

If any condition is false, return to the appropriate phase and revise. Do not return partial output.

---

## Internal checklist (do not expose in output)

Internally maintain a per-sentence checklist during Phase 3 and a per-section checklist during Phase 4. Do not include these checklists in the final note unless explicitly requested by the user.

---

## Quality tiers for rules not in `style-hard-rules.md`

Rules from `note-template.md` and `math-pedagogy.md` (in the eutaxis math domain) that are not listed as hard blockers fall into the following tiers:

**Tier B — Structural blockers** (required when applicable; revise before output)
- Opening callout order
- Contributions vs. roadmap separation
- Applicability callout placement
- Proof placement (after interpretation)
- Formula interpretation sentence
- Object introduction by role before notation
- Anchors on first content line; no heading-slug links
- No duplicated derivation across notes
- Summary table for multi-case notes

**Tier C — Quality improvements** (revise unless there is a strong reason not to)
- Sentence length over 40 words
- Paragraph coherence and explicit connectors
- Bold-label consistency across sections
- Style homogeneity of takeaway formats
- Inline enumeration conversion to bulleted list
- Assumption motivation before formal statement
