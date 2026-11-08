"""
What a filled inquiry must carry, read from the registry that declares it.

The requirements that govern a record are declared in two registries rather than restated here:

- the values a closed field admits, listed per record kind in ``data/vocabularies.yml``;
- the general ones, listed per record kind under ``always`` in ``data/requirements.yml``;
- the ones a level of commitment imposes on a target system or a phenomenon, under
  ``by_commitment``;
- the ones a value of a closed field imposes, such as the protocol of an experiment, under
  ``by_value``;
- the ones an epistemic aim adds, and the general ones the inquiry produces, under ``by_aim``. An
  inquiry that produces a phenomenon cannot be asked to state that phenomenon in advance, so
  those paths may stay empty.

An empty value means that a field is not filled. Whether an empty field is a gap or a value that
the inquiry will produce is read from the registry, never from the record.

A third kind is neither: a consistency between fields, such as an accuracy marked inapplicable
while outputs are listed for matching. No aim decides those, so each is its own check.

The specification notes document the same requirements and are checked against the registry, so no
check here reads a document.

Modules
-------
paths
    Read a record by the path of a field, and tell an empty field from a filled one.
requirements
    Check the specifications that the requirement registry demands of a record.
values
    Check each closed field against the values of the vocabulary registry.
subjects
    Check the occurrence class and the evidential status of a phenomenon, and the boundaries of a
    target system.
questions
    Check the slots, the references, the task and the domain of a question.
assessments
    Check an assessment, and give the disposition of the record that it assesses.
problems
    Read the state of a problem: its demand, its presuppositions and its obstacles.
answers
    Check the operations, the bound outputs and the status pairs of an answer.

See Also
--------
data/requirements.yml : the registry these functions read.
"""

from __future__ import annotations

from .answers import (
    STATUS_PAIRS,
    incomplete_operations,
    inherited_presuppositions,
    misdirected_interventions,
    misdirected_requirements,
    misdirected_rival,
    misheld_existence,
    misheld_presuppositions,
    mismatched_status_pairs,
    unbound_outputs,
    unclassified_operations,
    unstated_domain,
)
from .assessments import (
    disposition,
    malformed_credence,
    misdirected_assessment,
    premature_appraisal,
)
from .maturity import misplaced_maturity
from .paths import (
    DATA,
    REQUIREMENT_REGISTRY,
    VOCABULARY_REGISTRY,
    at,
    is_empty,
    is_unfilled,
    path_segments,
)
from .problems import (
    demand_met,
    mismatched_request,
    misstated_obstacles,
    presupposition_denied,
    readable_obstacles,
    unsupported_outcome,
    unsupported_question_dissolution,
)
from .questions import (
    SLOT_PLACEHOLDERS,
    SUBJECT_SLOTS,
    contradictory_accuracy,
    malformed_restrictions,
    misstated_limit,
    quantity_symbols,
    unanchored_explicandum,
    unbounded_aim,
    unjustified_explanans_bound,
    unrealized_link,
    unresolved_question_references,
    unresolved_slots,
    unstated_function_sense,
    unstated_standing,
    varying_symbols,
)
from .requirements import (
    COMMITMENT_LEVELS,
    always_required,
    block_requirements,
    commitment_requirements,
    record_kinds,
    requirements_by_aim,
    requirements_by_commitment,
    requirements_by_presence,
    requirements_by_value,
    unmet_by_aim,
    unmet_by_presence,
    unmet_by_value,
    unmet_commitment,
    unmet_general,
)
from .subjects import (
    mismatched_evidence,
    mismatched_occurrence,
    occurrence_by_category,
    target_types_by_evidential_status,
    unbounded_censoring,
    undecided_boundaries,
)
from .values import (
    admitted_values,
    inadmissible_values,
    placeholder_types,
    result_aims,
    vocabularies,
)

__all__ = [
    "COMMITMENT_LEVELS",
    "DATA",
    "REQUIREMENT_REGISTRY",
    "SLOT_PLACEHOLDERS",
    "STATUS_PAIRS",
    "SUBJECT_SLOTS",
    "VOCABULARY_REGISTRY",
    "admitted_values",
    "always_required",
    "at",
    "block_requirements",
    "commitment_requirements",
    "contradictory_accuracy",
    "demand_met",
    "disposition",
    "inadmissible_values",
    "incomplete_operations",
    "inherited_presuppositions",
    "is_empty",
    "is_unfilled",
    "malformed_credence",
    "malformed_restrictions",
    "misdirected_assessment",
    "misdirected_interventions",
    "misdirected_requirements",
    "misdirected_rival",
    "misheld_existence",
    "misheld_presuppositions",
    "mismatched_evidence",
    "mismatched_occurrence",
    "mismatched_request",
    "mismatched_status_pairs",
    "misplaced_maturity",
    "misstated_limit",
    "misstated_obstacles",
    "occurrence_by_category",
    "path_segments",
    "placeholder_types",
    "premature_appraisal",
    "presupposition_denied",
    "quantity_symbols",
    "readable_obstacles",
    "record_kinds",
    "requirements_by_aim",
    "requirements_by_commitment",
    "requirements_by_presence",
    "requirements_by_value",
    "result_aims",
    "target_types_by_evidential_status",
    "unanchored_explicandum",
    "unbound_outputs",
    "unbounded_aim",
    "unbounded_censoring",
    "unclassified_operations",
    "undecided_boundaries",
    "unjustified_explanans_bound",
    "unmet_by_aim",
    "unmet_by_presence",
    "unmet_by_value",
    "unmet_commitment",
    "unmet_general",
    "unrealized_link",
    "unresolved_question_references",
    "unresolved_slots",
    "unstated_domain",
    "unstated_function_sense",
    "unstated_standing",
    "unsupported_outcome",
    "unsupported_question_dissolution",
    "varying_symbols",
    "vocabularies",
]
