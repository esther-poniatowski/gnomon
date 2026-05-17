# Mathematical Pedagogy (High-Level)

This reference defines high-level argument and structure requirements for mathematical notes.
It does not cover sentence-level style, lexical bans, punctuation, or typesetting details.

## Scope

- In scope: section purpose, argument order, motivation, interpretive bridges, evidence support, and paragraph progression.
- Out of scope: local wording constraints, micro-style, punctuation mechanics, and formatting conventions.

## Enforcement Status in Hermeneia

| Guidance area | Primary rule ids |
| --- | --- |
| Section opens with purpose before formal machinery | `structure.section_opener_block_kind` |
| Assumptions are motivated before formal statement | `math.assumption_motivation_order` |
| Proof follows interpretive context (not immediate formal jump) | `math.proof_placement_context`, `math.proof_marker` |
| Non-trivial formulas are integrated into the argument | `math.display_followup_interpretation`, `math.consecutive_display_blocks_without_bridge` |
| Discourse transitions and clause articulation | `discourse.transition_quality`, `discourse.semicolon_connector` |
| Case and branch presentation uses explicit structure | `paragraph.inline_case_split`, `paragraph.inline_enumeration_overload` |
| Paragraph progression avoids restatement loops | `paragraph.topic_sentence`, `paragraph.sentence_redundancy`, `paragraph.paragraph_redundancy`, `paragraph.lexical_repetition`, `paragraph.reformulation_inflation` |
| Referential continuity across a paragraph | `paragraph.concept_reference_drift` |
| Qualitative claims are backed by explicit support | `audience.claim_calibration`, `audience.qualitative_claim_without_quant_support` |

## Core Audit Dimensions

1. **Section intent is visible**
State the section question, method, and reason before formal details.

2. **Argument order respects dependencies**
Introduce and interpret prerequisites before using them.

3. **Motivation comes before formalism**
Explain why an assumption, definition, or equation appears before presenting it.

4. **Formulas are integrated into reasoning**
After a key formula, state what it means and what it enables next.

5. **Discourse links are explicit**
Mark continuation, contrast, and consequence instead of relying on adjacency.

6. **Paragraphs advance the argument**
Each paragraph should add a distinct role: claim, support, consequence, boundary case, or synthesis.

7. **Claim strength matches support density**
As claim strength rises, nearby evidence should become more explicit.

## Structural Contracts

### Section Opening Contract

Start each section with:

1. Objective.
2. Method.
3. Reason for that method.

Do not open with raw formal material (definition/equation/proof marker) before this framing.

### Assumption Contract

State purpose before assumption.

Acceptable:
- “To ensure uniqueness, assume …”

Weak:
- “Assume …” with no nearby role explanation.

### Proof Placement Contract

Use this order:

1. Formal statement.
2. Interpretive bridge (meaning, scope, mechanism).
3. Proof.

Avoid immediate statement-to-proof jumps.

### Formula Integration Contract

After a non-trivial display formula, add one interpretive sentence that states its local argumentative role.

For consecutive display formulas, add one shared motivation sentence before the chain.

### Case Structure Contract

When the argument branches, represent cases as explicit case units under a clear lead-in.

### Claim Calibration Contract

Keep qualitative claims close to concrete support (bound, estimate, derivation step, theorem/citation anchor).

## Editorial Guidance (Not Fully Rule-Enforced)

- End each section and paragraph with a clear consequence for the next step.
- Label boundary cases by role (guard condition, limit regime, robustness check).
- Before a formal block, state why it appears at this point in the argument.
