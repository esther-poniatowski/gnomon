"""
Findings reported by the checks of gnomon, and the catalogue of their rules.

A finding names the kind of defect by its rule, the place of the defect inside its record by a
field path, and the defect itself by the message that the text output prints. The path converts to
a JSON Pointer, the locus; the discriminator separates two findings of one rule at one locus. The
record that holds the defect is supplied by the caller, which knows the file it read, so a check
never names a file.

An entry of a list keyed by an identifier is located by the pointer of the list, and its identifier
opens the discriminator; whatever lies below the entry follows in the discriminator. Reordering the
list therefore keeps the identity of each finding. An entry of an unkeyed list, or an entry that
carries no identifier, keeps its index in the pointer.

See Also
--------
gnomon.sarif : the writer of a findings log.
"""

from __future__ import annotations

import re
from dataclasses import dataclass
from typing import Any, Iterable, Mapping

#: The form of a rule identifier: lowercase components separated by ``/``.
RULE_ID = re.compile(r"[a-z0-9][a-z0-9._-]*(?:/[a-z0-9][a-z0-9._-]*)+")


@dataclass(frozen=True)
class Rule:
    """One kind of defect, with its stable identifier and a one-line description.

    Raises
    ------
    ValueError
        If the identifier is not lowercase components separated by ``/``.
    """

    id: str
    description: str

    def __post_init__(self) -> None:
        if not RULE_ID.fullmatch(self.id):
            raise ValueError(f"malformed rule identifier: {self.id!r}")


_CATALOGUE: list[Rule] = []


def _rule(identifier: str, description: str) -> Rule:
    """Declare one rule of the catalogue."""
    rule = Rule(identifier, description)
    _CATALOGUE.append(rule)
    return rule


# --- Itineraries ----------------------------------------------------------------------------------

ITINERARY_UNADDRESSED = _rule(
    "itinerary/unaddressed", "The itinerary addresses no problem or question record."
)
ITINERARY_REPEATED_STEP = _rule("itinerary/repeated-step", "Several steps share one identifier.")
ITINERARY_UNKNOWN_ACTIVITY = _rule(
    "itinerary/unknown-activity", "A step names no registered activity."
)
ITINERARY_UNFILLED_INPUT = _rule(
    "itinerary/unfilled-input", "The inputs of a step do not fill an input of its activity in number."
)
ITINERARY_UNACCEPTED_INPUT = _rule(
    "itinerary/unaccepted-input", "A step gives an input of a type that its activity does not take."
)
ITINERARY_MISTYPED_STEP_INPUT = _rule(
    "itinerary/mistyped-step-input", "An input names a step that produces another type."
)
ITINERARY_INPUT_WITHOUT_PRODUCER = _rule(
    "itinerary/input-without-producer", "An input of a type that no record holds names no step."
)
ITINERARY_UNRESOLVED_INPUT = _rule(
    "itinerary/unresolved-input", "An input names neither a step nor a record."
)
ITINERARY_MISTYPED_RECORD_INPUT = _rule(
    "itinerary/mistyped-record-input", "An input names a record that does not hold its type."
)
ITINERARY_MISTYPED_OUTPUT = _rule(
    "itinerary/mistyped-output", "The output type of a step is not the output of its activity."
)
ITINERARY_MISTYPED_OUTPUT_RECORD = _rule(
    "itinerary/mistyped-output-record",
    "The output reference of a step names a record that does not hold the output type.",
)
ITINERARY_FOREIGN_NORM = _rule(
    "itinerary/foreign-norm", "The norm of a step is not the test of its activity."
)
ITINERARY_UNKNOWN_VERDICT = _rule("itinerary/unknown-verdict", "The verdict of a step is not admitted.")
ITINERARY_MISMATCHED_MODE = _rule(
    "itinerary/mismatched-mode", "The mode of a step is not admitted, or not the mode of its activity."
)
ITINERARY_CYCLE = _rule("itinerary/cycle", "The references between the steps form a cycle.")

# --- Activity registry ----------------------------------------------------------------------------

REGISTRY_UNKNOWN_PRODUCT_TYPE = _rule(
    "registry/unknown-product-type",
    "An activity names a type that the product-type registry does not declare.",
)
REGISTRY_UNADMITTED_MODE = _rule(
    "registry/unadmitted-mode", "An activity proceeds by a mode that the vocabulary does not admit."
)
REGISTRY_FOREIGN_NORM = _rule(
    "registry/foreign-norm", "The norm of an activity is not the test named after that activity."
)

# --- Completeness and consistency of records ------------------------------------------------------

COMPLETENESS_UNMET_REQUIREMENT = _rule(
    "completeness/unmet-requirement", "A record leaves unfilled a specification that it always carries."
)
COMPLETENESS_UNMET_COMMITMENT = _rule(
    "completeness/unmet-commitment",
    "A record leaves unfilled a specification that its level of commitment requires.",
)
COMPLETENESS_MISMATCHED_OCCURRENCE = _rule(
    "completeness/mismatched-occurrence",
    "A phenomenon takes an occurrence class that its category does not admit.",
)
COMPLETENESS_UNADMITTED_PLACEHOLDER = _rule(
    "completeness/unadmitted-placeholder", "A subject slot holds a placeholder of a type not admitted."
)
COMPLETENESS_MISFIT_PLACEHOLDER = _rule(
    "completeness/misfit-placeholder", "A subject slot holds a placeholder of a type that it does not await."
)
COMPLETENESS_UNDESCRIBED_PLACEHOLDER = _rule(
    "completeness/undescribed-placeholder", "A placeholder of a subject slot carries no description."
)
COMPLETENESS_UNRESOLVED_SLOT = _rule(
    "completeness/unresolved-slot", "A subject slot holds neither a record identifier nor a placeholder."
)
COMPLETENESS_UNKNOWN_SLOT_RECORD = _rule(
    "completeness/unknown-slot-record", "A subject slot names an identifier that no record carries."
)
COMPLETENESS_MISTYPED_SLOT_RECORD = _rule(
    "completeness/mistyped-slot-record", "A subject slot names a record of another kind than it awaits."
)
COMPLETENESS_UNIDENTIFIED_SLOT_RECORD = _rule(
    "completeness/unidentified-slot-record",
    "A subject slot names a record that carries no identification.",
)
COMPLETENESS_UNADDRESSED_PROBLEM = _rule(
    "completeness/unaddressed-problem", "A question addresses no problem record."
)
COMPLETENESS_LINK_NOT_QUESTION = _rule(
    "completeness/link-not-question", "A link of a question names no question record."
)
COMPLETENESS_SELF_LINK = _rule("completeness/self-link", "A question is linked to itself.")
COMPLETENESS_UNKNOWN_LINK_RECORD = _rule(
    "completeness/unknown-link-record", "A link of a question passes through no existing record."
)
COMPLETENESS_NOT_BACKGROUND = _rule(
    "completeness/not-background", "A question admits a background that is no background record."
)
COMPLETENESS_FOREIGN_BACKGROUND = _rule(
    "completeness/foreign-background",
    "A question admits a background that describes another target than its own.",
)
COMPLETENESS_UNSTATED_FUNCTION_SENSE = _rule(
    "completeness/unstated-function-sense",
    "A question requests a functional relation without its sense of function.",
)
COMPLETENESS_MALFORMED_CREDENCE = _rule(
    "completeness/malformed-credence", "A credence holds neither a value nor a basis."
)
COMPLETENESS_CREDENCE_OUT_OF_RANGE = _rule(
    "completeness/credence-out-of-range", "The value of a credence is no number between 0 and 1."
)
COMPLETENESS_CREDENCE_WITHOUT_BASIS = _rule(
    "completeness/credence-without-basis", "A credence states no basis."
)
COMPLETENESS_UNMET_AIM = _rule(
    "completeness/unmet-aim", "The records leave open a specification that the aim of the question requires."
)
COMPLETENESS_CONTRADICTORY_ACCURACY = _rule(
    "completeness/contradictory-accuracy",
    "A question lists a match while declaring that accuracy does not apply.",
)
COMPLETENESS_UNREALIZED_LINK = _rule(
    "completeness/unrealized-link",
    "The question asks for a link, and the answer maps no quantity onto its realization.",
)
COMPLETENESS_INCOMPLETE_REALIZATION = _rule(
    "completeness/incomplete-realization", "A realization names what it realizes without saying by what."
)
COMPLETENESS_UNJUSTIFIED_EXPLANANS_BOUND = _rule(
    "completeness/unjustified-explanans-bound",
    "The bound on the explanans states an axis without a justification.",
)
COMPLETENESS_UNSTATED_STANDING = _rule(
    "completeness/unstated-standing", "A virtue that the question weighs states no standing."
)
COMPLETENESS_RESTRICTION_CONTENT = _rule(
    "completeness/restriction-content",
    "A domain restriction carries both or neither of a value set and an expression.",
)
COMPLETENESS_ANONYMOUS_RESTRICTION = _rule(
    "completeness/anonymous-restriction", "A domain restriction names neither a quantity nor itself."
)
COMPLETENESS_RESTRICTION_WITHOUT_VARIABLE = _rule(
    "completeness/restriction-without-variable",
    "A domain restriction states how it holds a quantity that is no variable.",
)
COMPLETENESS_UNDECIDED_BOUNDARY = _rule(
    "completeness/undecided-boundary",
    "An external system neither writes its constraint nor declares it absent.",
)
COMPLETENESS_INADMISSIBLE_VALUE = _rule(
    "completeness/inadmissible-value", "A closed field holds a value that its vocabulary does not admit."
)

# --- Symbols and operators ------------------------------------------------------------------------

VOCABULARY_MISTYPED_SYMBOL = _rule(
    "vocabulary/mistyped-symbol", "A symbol was read by YAML as a value of another type than a string."
)
VOCABULARY_SPLIT_EXPRESSION = _rule(
    "vocabulary/split-expression", "An expression was split into fragments by the serializer."
)
VOCABULARY_CORRUPTED_NOTATION = _rule(
    "vocabulary/corrupted-notation", "A notation holds a control character left by an escape."
)
VOCABULARY_MISPLACED_SHARING = _rule(
    "vocabulary/misplaced-sharing", "An external system shares something other than a declared quantity."
)
VOCABULARY_UNFIXED_PARAMETER = _rule(
    "vocabulary/unfixed-parameter", "A parameter is indexed by an interval, along which it would vary."
)
VOCABULARY_DOUBLY_DEFINED = _rule(
    "vocabulary/doubly-defined", "A quantity carries both an expression and a condition."
)
VOCABULARY_UNOWNED_QUANTITY = _rule(
    "vocabulary/unowned-quantity", "A quantity names an owner that is no declared external system."
)
VOCABULARY_UNSELECTED_CONDITION = _rule(
    "vocabulary/unselected-condition", "A quantity fixed by a condition states no selection rule."
)
VOCABULARY_VACUOUS_SHARED = _rule(
    "vocabulary/vacuous-shared", "A quantity marks `shared` while taking no signature."
)
VOCABULARY_MISMATCHED_ARITY = _rule(
    "vocabulary/mismatched-arity", "A call passes a number of arguments that its operator does not take."
)
VOCABULARY_UNRESOLVED = _rule(
    "vocabulary/unresolved", "A reference or a formula identifier resolves to no declaration."
)
VOCABULARY_OVERREACHING_ENTRY = _rule(
    "vocabulary/overreaching-entry",
    "An entry asserts of every member what only the members of one variant carry.",
)
VOCABULARY_MISATTRIBUTED_APPEAL = _rule(
    "vocabulary/misattributed-appeal", "An explanans appeals to something that is no external system."
)
VOCABULARY_UNBORNE_VARIANT = _rule(
    "vocabulary/unborne-variant", "A variant is carried by no declaration or law, and no maturity admits it."
)
VOCABULARY_MISNAMED_VARIANT = _rule(
    "vocabulary/misnamed-variant", "A variant mark names a variant that the target does not declare."
)
VOCABULARY_UNORDERED_INTERACTION = _rule(
    "vocabulary/unordered-interaction", "A relation names no ordered product of declared kinds."
)
VOCABULARY_RELATION_ENDS = _rule(
    "vocabulary/relation-ends", "A relation names both or neither of the parts and the laws it runs between."
)
VOCABULARY_SHORT_RELATION = _rule(
    "vocabulary/short-relation", "A relation among laws orders fewer than two of them."
)
VOCABULARY_UNKNOWN_RELATION_LAW = _rule(
    "vocabulary/unknown-relation-law", "A relation among laws names no law of the record."
)
VOCABULARY_MISROUTED_INTERACTION = _rule(
    "vocabulary/misrouted-interaction",
    "The laws stating a relation name no quantity indexed by every one of its places.",
)
VOCABULARY_UNUSED_DECLARATION = _rule(
    "vocabulary/unused-declaration", "A declared quantity is mentioned by no other field of its problem."
)

#: Every rule a check of gnomon can report, in the order of declaration.
RULES: tuple[Rule, ...] = tuple(_CATALOGUE)


# --- Findings and their locus ---------------------------------------------------------------------

Segment = str | int


@dataclass(frozen=True)
class Finding:
    """One defect: its rule, its place inside the record, and its message.

    Attributes
    ----------
    rule : Rule
        The kind of defect.
    path : tuple of str or int
        The segments of the locus, keys and indices; empty for the whole record.
    text : str
        The message of the text output.
    discriminator : str
        What separates two findings of one rule at one locus, derived from this finding alone;
        empty when the locus suffices.
    """

    rule: Rule
    path: tuple[Segment, ...]
    text: str
    discriminator: str = ""

    @property
    def locus(self) -> str:
        """The JSON Pointer of :attr:`path`, empty for the whole record."""
        return pointer(self.path)


def token(segment: Segment) -> str:
    """Return the JSON Pointer token of one segment (RFC 6901).

    An index takes its decimal form. In a key, ``~`` becomes ``~0`` before ``/`` becomes ``~1``,
    since the reverse order would turn ``/`` into ``~01``.

    >>> token("a/b"), token("c~1d"), token(3)
    ('a~1b', 'c~01d', '3')
    """
    if isinstance(segment, int):
        return str(segment)
    return segment.replace("~", "~0").replace("/", "~1")


def pointer(path: Iterable[Segment]) -> str:
    """Return the JSON Pointer of a field path; the empty path yields the empty string.

    >>> pointer(("relations", 2, "target"))
    '/relations/2/target'
    >>> pointer(("",)), pointer(())
    ('/', '')
    """
    return "".join("/" + token(segment) for segment in path)


@dataclass(frozen=True)
class Key:
    """An entry of a keyed list, named by its identifier rather than by its position."""

    identifier: str


@dataclass(frozen=True, eq=False)
class Entry:
    """An entry of a list, given by its index and its content.

    :func:`finding` names it by its identifier when its list is keyed and it carries one, and by
    its index otherwise.
    """

    index: int
    item: Any


#: A field path whose list entries are still given with their content, as :func:`finding` takes it.
Place = tuple[Segment | Key | Entry, ...]


#: The keys that identify the entries of a keyed list, by name of the list; the first key holding a
#: non-empty string identifies the entry.
IDENTIFIER_KEYS: Mapping[str, tuple[str, ...]] = {
    "steps": ("id",),
    "activities": ("id",),
    "restrictions": ("name", "of"),
}

#: The keys identifying the entries of every other keyed list.
DEFAULT_IDENTIFIER_KEYS: tuple[str, ...] = ("symbol", "name")

#: The lists whose entries carry no identifier, so that each keeps its index.
UNKEYED: frozenset[str] = frozenset({"links", "realizations", "virtues"})


def member(name: str | None, entry: Entry) -> Key | int:
    """Return the segment naming ``entry`` of the list called ``name``.

    >>> member("variables", Entry(4, {"symbol": "u"}))
    Key(identifier='u')
    >>> member("virtues", Entry(1, {"virtue": "economy"})), member("laws", Entry(2, {"role": "x"}))
    (1, 2)
    """
    if name is None or name in UNKEYED or not isinstance(entry.item, Mapping):
        return entry.index
    for key in IDENTIFIER_KEYS.get(name, DEFAULT_IDENTIFIER_KEYS):
        value = entry.item.get(key)
        if isinstance(value, str) and value.strip():
            return Key(value)
    return entry.index


def finding(
    rule: Rule, text: str, *segments: Segment | Key | Entry, value: str | None = None
) -> Finding:
    """Return the finding of ``rule`` at the field path ``segments``.

    The segments run from the root of the record. Up to the first keyed entry they form the locus;
    from that entry on, its identifier and every later segment form the discriminator, followed by
    ``value``, the offending content when several findings may share the place. The parts of the
    discriminator are joined by ``/``, each escaped as a pointer token.

    >>> found = finding(VOCABULARY_UNRESOLVED, "t", "variables", Entry(0, {"symbol": "u"}), "signature", 1)
    >>> found.locus, found.discriminator
    ('/variables', 'u/signature/1')
    >>> finding(ITINERARY_CYCLE, "t", "steps", value="a -> b -> a").discriminator
    'a -> b -> a'
    """
    path: list[Segment] = []
    parts: list[str] = []
    name: str | None = None
    for segment in segments:
        resolved = member(name, segment) if isinstance(segment, Entry) else segment
        if isinstance(resolved, Key):
            parts.append(resolved.identifier)
        elif parts:
            parts.append(str(resolved))
        else:
            path.append(resolved)
        name = resolved if isinstance(resolved, str) else None
    if value is not None:
        parts.append(value)
    return Finding(rule, tuple(path), text, "/".join(token(part) for part in parts))


def texts(findings: Iterable[Finding]) -> list[str]:
    """Return the messages of ``findings``, in order: the lines of the text output."""
    return [found.text for found in findings]
