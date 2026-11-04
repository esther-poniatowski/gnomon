"""
The checks of a derivation record: its units, its interpretations, its orientations, its kernel and
its slots.

A derivation names its own units by bare identifiers and the premises held by other records by
dotted references. The checks of this module read the bare identifiers only; the reference check
of :mod:`gnomon.vocabulary` resolves the dotted ones. The dependence of a derivation is read from
the inputs and the outputs of its moves and of its segments: a move or a segment yields its outputs
once all of its inputs are available, so a segment bridges the routine moves that the record
omits. The rules that these checks apply are declared in the registry of derivations, which the
notes of the theory own.

Functions
---------
load_registry
    Return the registry of the rules of a derivation.
unknown_units
    Return the units named inside a derivation that the record does not declare.
repeated_units
    Return the identifiers that several units of a derivation share.
unadmitted_pairs
    Return the interpretations whose kind their item does not admit.
mistyped_grounds
    Return the warrants and the diagnostic interpretations that cite a ground of the wrong type.
cyclic_moves
    Return the cycles among the moves of a derivation.
retrospective_orientations
    Return the orientations that cite an object established by their own move or after it.
unoriented_moves
    Return the non-routine moves that no orientation selects.
ambiguous_purposes
    Return the orientations that state both or neither of a sought and a change.
failed_kernel
    Return a finding when a route to a consequence of the root sought avoids the kernel.
unrecorded_consequences
    Return the consequences of the root sought that name no record.
unbound_slots
    Return the slots that no move binds, in a derivation that ends in no impasse.
derivation_problems
    Return every finding of the checks of a derivation.
"""

from __future__ import annotations

from functools import cache
from pathlib import Path
from typing import Any, Iterable, Iterator, Mapping

import yaml

from . import findings as rules
from .findings import Entry, Finding, finding

#: The registry of the rules of a derivation.
REGISTRY = Path(__file__).parent / "data" / "registries" / "derivations.yml"

#: The lists of a derivation whose entries are units named by the key ``id``.
UNIT_LISTS: tuple[str, ...] = (
    "subordinate",
    "objects",
    "posits",
    "moves",
    "orientations",
    "interpretations",
    "features",
    "segments",
    "consequences",
)

#: The fields that name a unit of the record, as (list, key, admitted lists). The key ``kernel``
#: and the root of the record use the list ``""``. A key holding a list names one unit per entry.
INTERNAL: tuple[tuple[str, str, tuple[str, ...]], ...] = (
    ("subordinate", "replaces", ("subordinate",)),
    ("slots", "introduced_by", ("moves", "posits")),
    ("moves", "inputs", ("objects", "posits")),
    ("moves", "outputs", ("objects",)),
    ("moves", "binds", ("slots",)),
    ("", "kernel", ("moves",)),
    ("orientations", "of", ("moves", "segments")),
    ("orientations", "determines", ("sought", "subordinate")),
    ("orientations", "occasion", ("interpretations",)),
    ("interpretations", "of", ("objects", "moves", "features", "segments", "consequences")),
    ("features", "at", ("objects",)),
    ("segments", "serves", ("sought", "subordinate")),
    ("segments", "moves", ("moves",)),
    ("segments", "inputs", ("objects", "posits")),
    ("segments", "outputs", ("objects",)),
    ("segments", "within", ("segments",)),
    ("consequences", "answers", ("sought", "subordinate")),
    ("consequences", "from", ("objects",)),
    ("consequences", "principle", ("interpretations",)),
    ("impasses", "sought", ("sought", "subordinate")),
    ("impasses", "obstacle", ("interpretations",)),
    ("refutations", "target", ("posits", "consequences")),
    ("refutations", "by", ("objects", "posits")),
)

Derivation = Mapping[str, Any]


@cache
def load_registry(source: Path | None = None) -> dict[str, Any]:
    """Return the registry of the rules of a derivation, read once."""
    loaded: dict[str, Any] = yaml.safe_load((source or REGISTRY).read_text(encoding="utf-8")) or {}
    return loaded


def _entries(record: Derivation, name: str) -> list[tuple[int, Mapping[str, Any]]]:
    """Return the entries of a list of the record that are mappings, with their indices."""
    found = record.get(name)
    if not isinstance(found, list):
        return []
    return [(i, item) for i, item in enumerate(found) if isinstance(item, Mapping)]


def _mapping(value: Any) -> Mapping[str, Any]:
    """Return ``value`` when it is a mapping, and an empty mapping otherwise."""
    return value if isinstance(value, Mapping) else {}


def _names(value: Any) -> list[str]:
    """Return the identifiers that a field holds: one for a string, one per entry for a list."""
    values = value if isinstance(value, list) else [value]
    return [str(v) for v in values if isinstance(v, str) and v.strip()]


def _is_internal(name: str) -> bool:
    """Tell whether a name designates a unit of the record rather than a dotted reference or a
    placeholder of a template."""
    return "." not in name and not name.isupper() and not name.replace("-", "").isupper()


def units(record: Derivation) -> dict[str, set[str]]:
    """Return the identifiers declared by each list of a derivation, with ``sought`` for the root
    and ``slots`` for the symbols of its slots.

    >>> sorted(units({"sought": {"id": "s"}, "moves": [{"id": "m"}]})["moves"])
    ['m']
    """
    declared = {
        name: {str(item.get("id")) for _, item in _entries(record, name) if item.get("id")}
        for name in UNIT_LISTS
    }
    root = record.get("sought")
    declared["sought"] = (
        {str(root["id"])} if isinstance(root, Mapping) and root.get("id") else set()
    )
    declared["slots"] = {
        str(item.get("symbol")) for _, item in _entries(record, "slots") if item.get("symbol")
    }
    return declared


def _kind_of(record: Derivation) -> dict[str, str]:
    """Return the list that declares each identifier of a unit of the record."""
    return {ident: name for name, idents in units(record).items() for ident in idents}


def unknown_units(record: Derivation) -> list[Finding]:
    """Return the units named inside a derivation that the record does not declare, or declares in
    a list that the field does not admit.

    >>> [f.text for f in unknown_units({"moves": [{"id": "m", "inputs": ["x"]}]})]
    ['moves.m.inputs: x names no unit among objects, posits']
    """
    kinds = _kind_of(record)
    found = []
    for list_name, key, admitted in INTERNAL:
        places: Iterable[tuple[tuple[Any, ...], Any]]
        if not list_name:
            places = [((key,), record.get(key))]
        else:
            places = [
                ((list_name, Entry(i, item), key), item.get(key))
                for i, item in _entries(record, list_name)
            ]
        for path, value in places:
            for name in _names(value):
                if not _is_internal(name) or kinds.get(name) in admitted:
                    continue
                where = ".".join(
                    str(p.item.get("id") or p.index) if isinstance(p, Entry) else str(p)
                    for p in path
                )
                found.append(
                    finding(
                        rules.DERIVATION_UNKNOWN_UNIT,
                        f"{where}: {name} names no unit among {', '.join(admitted)}",
                        *path,
                        value=name,
                    )
                )
    return found


def repeated_units(record: Derivation) -> list[Finding]:
    """Return the identifiers that several units of a derivation share.

    >>> [f.text for f in repeated_units({"objects": [{"id": "x"}], "moves": [{"id": "x"}]})]
    ['x: the identifier names several units, in objects and moves']
    """
    seen: dict[str, list[str]] = {}
    root = record.get("sought")
    if isinstance(root, Mapping) and root.get("id"):
        seen.setdefault(str(root["id"]), []).append("sought")
    for name in UNIT_LISTS:
        for _, item in _entries(record, name):
            if item.get("id"):
                seen.setdefault(str(item["id"]), []).append(name)
    return [
        finding(
            rules.DERIVATION_REPEATED_UNIT,
            f"{ident}: the identifier names several units, in {' and '.join(places)}",
            value=ident,
        )
        for ident, places in seen.items()
        if len(places) > 1
    ]


def _item_of(record: Derivation, ident: str) -> str | None:
    """Return the item that an interpretation of ``ident`` interprets, or None when the unit is
    unknown or an object states no form."""
    for _, obj in _entries(record, "objects"):
        if obj.get("id") == ident:
            form = obj.get("form")
            return str(form) if form in ("object", "expression") else None
    by_list = {
        "moves": "transformation",
        "features": "feature",
        "segments": "composite",
        "consequences": "composite",
    }
    for name, item in by_list.items():
        if any(entry.get("id") == ident for _, entry in _entries(record, name)):
            return item
    return None


def unadmitted_pairs(
    record: Derivation, registry: Mapping[str, Any] | None = None
) -> list[Finding]:
    """Return the interpretations whose kind their item does not admit.

    >>> record = {"moves": [{"id": "m"}],
    ...           "interpretations": [{"id": "i", "of": "m", "kind": "diagnostic"}]}
    >>> [f.text for f in unadmitted_pairs(record)]
    ['interpretations.i: a transformation admits no diagnostic interpretation']
    """
    pairs = (registry or load_registry()).get("admitted_pairs") or {}
    found = []
    for i, entry in _entries(record, "interpretations"):
        item = _item_of(record, str(entry.get("of")))
        kind = entry.get("kind")
        if item is None or not kind or kind in (pairs.get(item) or []):
            continue
        found.append(
            finding(
                rules.DERIVATION_UNADMITTED_PAIR,
                f"interpretations.{entry.get('id') or i}: a {item} admits no {kind} interpretation",
                "interpretations",
                Entry(i, entry),
                "kind",
                value=str(kind),
            )
        )
    return found


def mistyped_grounds(
    record: Derivation, registry: Mapping[str, Any] | None = None
) -> list[Finding]:
    """Return the warrants that cite a property of a kind not licensing a move, and the diagnostic
    interpretations whose grounds name no move and no posit.

    >>> record = {"interpretations": [{"id": "i", "kind": "process"}],
    ...           "moves": [{"id": "m", "warrant": {"applies_because": "i"}}]}
    >>> [f.text for f in mistyped_grounds(record)]
    ['moves.m.warrant.applies_because: i is a process interpretation, not structural or magnitude']
    """
    reg = registry or load_registry()
    licensing_order = [str(k) for k in reg.get("licensing_kinds") or []]
    licensing = set(licensing_order)
    kinds = {str(e.get("id")): str(e.get("kind")) for _, e in _entries(record, "interpretations")}
    found = []
    for i, move in _entries(record, "moves"):
        warrant = move.get("warrant")
        cited = warrant.get("applies_because") if isinstance(warrant, Mapping) else None
        if isinstance(cited, str) and cited in kinds and kinds[cited] not in licensing:
            found.append(
                finding(
                    rules.DERIVATION_MISTYPED_GROUND,
                    f"moves.{move.get('id') or i}.warrant.applies_because: {cited} is a"
                    f" {kinds[cited]} interpretation, not {' or '.join(licensing_order)}",
                    "moves",
                    Entry(i, move),
                    "warrant",
                    "applies_because",
                    value=cited,
                )
            )
    declared = units(record)
    grounding = set().union(*(declared[name] for name in reg.get("diagnostic_grounds") or []))
    for i, entry in _entries(record, "interpretations"):
        if entry.get("kind") == "diagnostic" and not set(_names(entry.get("grounds"))) & grounding:
            found.append(
                finding(
                    rules.DERIVATION_MISTYPED_GROUND,
                    f"interpretations.{entry.get('id') or i}: a diagnostic interpretation cites no"
                    " move and no posit whose failure it reveals",
                    "interpretations",
                    Entry(i, entry),
                    "grounds",
                )
            )
    return found


def _producers(record: Derivation, *, segments: bool) -> dict[str, tuple[set[str], set[str]]]:
    """Return the inputs and the outputs of each move, and of each segment when asked."""
    found = {
        str(m.get("id")): (set(_names(m.get("inputs"))), set(_names(m.get("outputs"))))
        for _, m in _entries(record, "moves")
        if m.get("id")
    }
    if segments:
        found.update(
            {
                str(s.get("id")): (set(_names(s.get("inputs"))), set(_names(s.get("outputs"))))
                for _, s in _entries(record, "segments")
                if s.get("id")
            }
        )
    return found


def cyclic_moves(record: Derivation) -> list[Finding]:
    """Return one finding per cycle among the moves, in which a move takes what a later move of the
    cycle yields.

    >>> record = {"moves": [{"id": "a", "inputs": ["x"], "outputs": ["y"]},
    ...                     {"id": "b", "inputs": ["y"], "outputs": ["x"]}]}
    >>> [f.text for f in cyclic_moves(record)]
    ['moves: the moves a -> b -> a depend on one another in a cycle']
    """
    moves = _producers(record, segments=False)
    after = {
        name: sorted(o for o, (ins, _) in moves.items() if outs & ins)
        for name, (_, outs) in moves.items()
    }
    found: list[Finding] = []
    state: dict[str, int] = {}
    reported: set[frozenset[str]] = set()

    def visit(node: str, trail: list[str]) -> None:
        state[node] = 1
        for nxt in after[node]:
            if state.get(nxt) == 1:
                cycle = [*trail[trail.index(nxt) :], nxt]
                if frozenset(cycle) not in reported:
                    reported.add(frozenset(cycle))
                    found.append(
                        finding(
                            rules.DERIVATION_CYCLE,
                            f"moves: the moves {' -> '.join(cycle)} depend on one another in a"
                            " cycle",
                            "moves",
                            value=" -> ".join(cycle),
                        )
                    )
            elif state.get(nxt) is None:
                visit(nxt, [*trail, nxt])
        state[node] = 2

    for name in sorted(moves):
        if state.get(name) is None:
            visit(name, [name])
    return found


def _downstream(record: Derivation, move: str) -> set[str]:
    """Return the objects that a move yields, and every object that depends on them through the
    moves of the record."""
    moves = _producers(record, segments=False)
    reached = set(moves.get(move, (set(), set()))[1])
    changed = True
    while changed:
        changed = False
        for name, (ins, outs) in moves.items():
            if name != move and ins & reached and not outs <= reached:
                reached |= outs
                changed = True
    return reached


def _concerned(record: Derivation, ident: str) -> set[str]:
    """Return the objects that a unit concerns: an object itself, the outputs of a move or of a
    segment, the object of a feature, or the object that states a consequence."""
    for _, obj in _entries(record, "objects"):
        if obj.get("id") == ident:
            return {ident}
    for name in ("moves", "segments"):
        for _, entry in _entries(record, name):
            if entry.get("id") == ident:
                return set(_names(entry.get("outputs")))
    for _, feature in _entries(record, "features"):
        if feature.get("id") == ident:
            return set(_names(feature.get("at")))
    for _, consequence in _entries(record, "consequences"):
        if consequence.get("id") == ident:
            return set(_names(consequence.get("from")))
    return set()


def retrospective_orientations(record: Derivation) -> list[Finding]:
    """Return the orientations of a move whose occasion interprets an object that the move yields,
    or that depends on it.

    >>> record = {"objects": [{"id": "y"}],
    ...           "moves": [{"id": "m", "inputs": ["x"], "outputs": ["y"]}],
    ...           "interpretations": [{"id": "i", "of": "y"}],
    ...           "orientations": [{"id": "o", "of": "m", "occasion": "i"}]}
    >>> [f.text for f in retrospective_orientations(record)]
    ['orientations.o.occasion: i interprets y, which the move m establishes or which depends on it']
    """
    moves = {str(m.get("id")) for _, m in _entries(record, "moves")}
    interpreted = {
        str(e.get("id")): str(e.get("of")) for _, e in _entries(record, "interpretations")
    }
    found = []
    for i, orientation in _entries(record, "orientations"):
        move, occasion = orientation.get("of"), orientation.get("occasion")
        if move not in moves or not isinstance(occasion, str) or occasion not in interpreted:
            continue
        late = _concerned(record, interpreted[occasion]) & _downstream(record, str(move))
        if late:
            found.append(
                finding(
                    rules.DERIVATION_RETROSPECTIVE_ORIENTATION,
                    f"orientations.{orientation.get('id') or i}.occasion: {occasion} interprets"
                    f" {', '.join(sorted(late))}, which the move {move} establishes or which"
                    " depends on it",
                    "orientations",
                    Entry(i, orientation),
                    "occasion",
                    value=occasion,
                )
            )
    return found


def _non_routine(record: Derivation, move: Mapping[str, Any], reg: Mapping[str, Any]) -> list[str]:
    """Return the features that make a move non-routine, as the record states them."""
    ident = move.get("id")
    warrant = _mapping(move.get("warrant"))
    posits = units(record)["posits"]
    features = []
    if move.get("kind") in (reg.get("non_routine_kinds") or []):
        features.append(f"its kind {move.get('kind')}")
    if warrant.get("error") and warrant.get("error") != "exact":
        features.append(f"its {warrant.get('error')} error")
    if any(s.get("introduced_by") == ident for _, s in _entries(record, "slots")):
        features.append("the slot that it introduces")
    if set(_names(move.get("inputs"))) & posits:
        features.append("the posit that it uses")
    if record.get("kernel") == ident:
        features.append("its declaration as kernel")
    return features


def unoriented_moves(
    record: Derivation, registry: Mapping[str, Any] | None = None
) -> list[Finding]:
    """Return the non-routine moves that no orientation selects.

    >>> [f.text for f in unoriented_moves({"moves": [{"id": "m", "kind": "take-limit"}]})]
    ['moves.m: the move is non-routine by its kind take-limit, and no orientation selects it']
    """
    reg = registry or load_registry()
    oriented = {str(o.get("of")) for _, o in _entries(record, "orientations")}
    found = []
    for i, move in _entries(record, "moves"):
        features = _non_routine(record, move, reg)
        if features and str(move.get("id")) not in oriented:
            found.append(
                finding(
                    rules.DERIVATION_UNORIENTED_MOVE,
                    f"moves.{move.get('id') or i}: the move is non-routine by"
                    f" {' and '.join(features)}, and no orientation selects it",
                    "moves",
                    Entry(i, move),
                )
            )
    return found


def ambiguous_purposes(record: Derivation) -> list[Finding]:
    """Return the orientations that state both or neither of the sought that they determine and
    the change that they bring about.

    >>> [f.text for f in ambiguous_purposes({"orientations": [{"id": "o"}]})]
    ['orientations.o: the purpose states neither a sought that it determines nor a change']
    """
    found = []
    for i, orientation in _entries(record, "orientations"):
        determines, change = orientation.get("determines"), orientation.get("change")
        if bool(determines) == bool(change):
            text = (
                "states both a sought that it determines and a change"
                if determines
                else "states neither a sought that it determines nor a change"
            )
            found.append(
                finding(
                    rules.DERIVATION_AMBIGUOUS_PURPOSE,
                    f"orientations.{orientation.get('id') or i}: the purpose {text}",
                    "orientations",
                    Entry(i, orientation),
                )
            )
    return found


def _reachable(producers: Mapping[str, tuple[set[str], set[str]]], start: set[str]) -> set[str]:
    """Return what the premises ``start`` make available, a producer firing once all of its inputs
    are available."""
    reached = set(start)
    changed = True
    while changed:
        changed = False
        for ins, outs in producers.values():
            if ins <= reached and not outs <= reached:
                reached |= outs
                changed = True
    return reached


def _root_targets(record: Derivation) -> list[str]:
    """Return the objects that state the consequences of the root sought."""
    root = record.get("sought")
    root_id = root.get("id") if isinstance(root, Mapping) else None
    return [
        str(c.get("from"))
        for _, c in _entries(record, "consequences")
        if root_id and c.get("answers") == root_id and c.get("from")
    ]


def _enclosing(record: Derivation, move: str) -> set[str]:
    """Return the segments that hold a move, with every segment that encloses them."""
    within = {str(s.get("id")): s.get("within") for _, s in _entries(record, "segments")}
    found = {
        str(s.get("id")) for _, s in _entries(record, "segments") if move in _names(s.get("moves"))
    }
    frontier = set(found)
    while frontier:
        parents = {str(within[s]) for s in frontier if within.get(s)} - found
        found |= parents
        frontier = parents
    return found


def failed_kernel(record: Derivation) -> list[Finding]:
    """Return a finding when a route from the premises to a consequence of the root sought avoids
    the declared kernel: the kernel test, a necessary condition only.

    The premises are the inputs that no move and no segment yields. Removing the kernel removes
    every segment that holds it, since such a segment bridges the kernel among its moves.

    >>> record = {"sought": {"id": "s"}, "kernel": "a",
    ...           "moves": [{"id": "a", "inputs": ["p"], "outputs": ["y"]},
    ...                     {"id": "b", "inputs": ["p"], "outputs": ["y"]}],
    ...           "consequences": [{"id": "c", "answers": "s", "from": "y"}]}
    >>> [f.text for f in failed_kernel(record)]
    ['kernel: a route from the premises reaches y without the kernel a']
    """
    kernel = record.get("kernel")
    if not isinstance(kernel, str) or not kernel:
        return []
    producers = _producers(record, segments=True)
    yielded = set().union(*(outs for _, outs in producers.values())) if producers else set()
    premises = (
        set().union(*(ins for ins, _ in producers.values())) - yielded if producers else set()
    )
    full = _reachable(producers, premises)
    removed = {kernel} | _enclosing(record, kernel)
    without = _reachable({k: v for k, v in producers.items() if k not in removed}, premises)
    return [
        finding(
            rules.DERIVATION_FAILED_KERNEL,
            f"kernel: a route from the premises reaches {target} without the kernel {kernel}",
            "kernel",
            value=target,
        )
        for target in _root_targets(record)
        if target in full and target in without
    ]


def unrecorded_consequences(record: Derivation) -> list[Finding]:
    """Return the consequences of the root sought that name no record stating them.

    >>> record = {"sought": {"id": "s"}, "consequences": [{"id": "c", "answers": "s"}]}
    >>> [f.text for f in unrecorded_consequences(record)]
    ['consequences.c: a consequence of the root sought names no record that states it']
    """
    root = record.get("sought")
    root_id = root.get("id") if isinstance(root, Mapping) else None
    return [
        finding(
            rules.DERIVATION_UNRECORDED_CONSEQUENCE,
            f"consequences.{c.get('id') or i}: a consequence of the root sought names no record"
            " that states it",
            "consequences",
            Entry(i, c),
            "record",
        )
        for i, c in _entries(record, "consequences")
        if root_id and c.get("answers") == root_id and not c.get("record")
    ]


def unbound_slots(record: Derivation) -> list[Finding]:
    """Return the slots that no move binds, in a derivation that ends in no impasse.

    >>> [f.text for f in unbound_slots({"slots": [{"symbol": "a"}]})]
    ['slots.a: no move binds the slot, and the derivation ends in no impasse']
    """
    if _entries(record, "impasses"):
        return []
    bound = {name for _, m in _entries(record, "moves") for name in _names(m.get("binds"))}
    return [
        finding(
            rules.DERIVATION_UNBOUND_SLOT,
            f"slots.{s.get('symbol')}: no move binds the slot, and the derivation ends in no"
            " impasse",
            "slots",
            Entry(i, s),
        )
        for i, s in _entries(record, "slots")
        if s.get("symbol") and str(s.get("symbol")) not in bound
    ]


def recorded_descents(records: Iterable[Mapping[str, Any]]) -> dict[str, str]:
    """Return, for each record that a consequence of a derivation names, that derivation.

    >>> recorded_descents([{"type": "derivation", "id": "derivation.a.b",
    ...                     "consequences": [{"record": "mod.a.m.law"}]}])
    {'mod.a.m.law': 'derivation.a.b'}
    """
    return {
        str(consequence.get("record")): str(record.get("id"))
        for record in records
        if record.get("type") == "derivation"
        for _, consequence in _entries(record, "consequences")
        if consequence.get("record")
    }


def unrecorded_descents(record: Mapping[str, Any], descents: Mapping[str, str]) -> list[Finding]:
    """Return the laws marked ``derived`` whose descent is recorded nowhere: no derivation states
    the law as a consequence, and the law names no published origin holding its derivation.

    >>> law = {"symbol": "bound", "warrant": "derived"}
    >>> [f.text for f in unrecorded_descents({"id": "bg.a.b", "laws": [law]}, {})]
    ['laws.bound: the law is marked derived, and no derivation or origin records its descent']
    >>> unrecorded_descents({"id": "bg.a.b", "laws": [law]}, {"bg.a.b.bound": "derivation.a.c"})
    []
    """
    found = []
    for i, law in _entries(record, "laws"):
        if law.get("warrant") != "derived" or law.get("origin"):
            continue
        if f"{record.get('id')}.{law.get('symbol')}" in descents:
            continue
        found.append(
            finding(
                rules.DERIVATION_UNRECORDED_DESCENT,
                f"laws.{law.get('symbol') or i}: the law is marked derived, and no derivation or"
                " origin records its descent",
                "laws",
                Entry(i, law),
                "warrant",
            )
        )
    return found


def _targets(record: Derivation) -> set[str]:
    """Return the objects that an outcome or a cited interpretation concerns: the objects stating
    consequences and counterexamples, and the objects interpreted by the obstacle of an impasse, by
    the occasion of an orientation or by the property that a warrant cites."""
    interpreted = {
        str(e.get("id")): str(e.get("of")) for _, e in _entries(record, "interpretations")
    }
    cited = {str(i.get("obstacle")) for _, i in _entries(record, "impasses")}
    cited |= {str(o.get("occasion")) for _, o in _entries(record, "orientations")}
    cited |= {
        str(_mapping(m.get("warrant")).get("applies_because")) for _, m in _entries(record, "moves")
    }
    found = {str(c.get("from")) for _, c in _entries(record, "consequences") if c.get("from")}
    found |= {str(r.get("by")) for _, r in _entries(record, "refutations") if r.get("by")}
    for name in cited & set(interpreted):
        found |= _concerned(record, interpreted[name])
    return found


def idle_moves(record: Derivation) -> list[Finding]:
    """Return the moves that yield only what they take, and the moves whose outputs reach, through
    the moves and the segments, no outcome and no interpretation that the record cites.

    >>> record = {"sought": {"id": "s"},
    ...           "objects": [{"id": "x"}, {"id": "y"}, {"id": "z"}],
    ...           "moves": [{"id": "a", "inputs": ["p"], "outputs": ["x"]},
    ...                     {"id": "b", "inputs": ["p"], "outputs": ["z"]}],
    ...           "consequences": [{"id": "c", "answers": "s", "from": "x"}]}
    >>> [f.text for f in idle_moves(record)]
    ['moves.b: the outputs of the move reach no outcome and no cited interpretation']
    """
    targets = _targets(record)
    if not targets:
        return []
    producers = _producers(record, segments=True)
    found = []
    for i, move in _entries(record, "moves"):
        ins, outs = set(_names(move.get("inputs"))), set(_names(move.get("outputs")))
        if outs and outs <= ins:
            text = "the move yields only what it takes"
        else:
            reached = set(outs)
            changed = True
            while changed:
                changed = False
                for p_ins, p_outs in producers.values():
                    if p_ins & reached and not p_outs <= reached:
                        reached |= p_outs
                        changed = True
            if reached & targets:
                continue
            text = "the outputs of the move reach no outcome and no cited interpretation"
        found.append(
            finding(
                rules.DERIVATION_IDLE_MOVE,
                f"moves.{move.get('id') or i}: {text}",
                "moves",
                Entry(i, move),
            )
        )
    return found


def cyclic_nesting(record: Derivation) -> list[Finding]:
    """Return the cycles of the segments that enclose one another, and of the subordinate soughts
    that replace one another.

    >>> record = {"segments": [{"id": "a", "within": "b"}, {"id": "b", "within": "a"}]}
    >>> [f.text for f in cyclic_nesting(record)]
    ['segments: a -> b -> a enclose one another in a cycle']
    """
    found = []
    for name, key in (("segments", "within"), ("subordinate", "replaces")):
        parent = {
            str(e.get("id")): str(e.get(key)) for _, e in _entries(record, name) if e.get(key)
        }
        reported: set[frozenset[str]] = set()
        for start in sorted(parent):
            trail = [start]
            while trail[-1] in parent and parent[trail[-1]] not in trail:
                trail.append(parent[trail[-1]])
            if trail[-1] in parent and parent[trail[-1]] in trail:
                loop = trail[trail.index(parent[trail[-1]]) :]
                if frozenset(loop) in reported:
                    continue
                reported.add(frozenset(loop))
                path = " -> ".join([*loop, loop[0]])
                verb = "enclose" if name == "segments" else "replace"
                found.append(
                    finding(
                        rules.DERIVATION_CYCLIC_NESTING,
                        f"{name}: {path} {verb} one another in a cycle",
                        name,
                        value=path,
                    )
                )
    return found


def derivation_problems(record: Derivation) -> list[Finding]:
    """Return every finding of the checks of a derivation, in the order of the checks."""
    return [
        *repeated_units(record),
        *unknown_units(record),
        *unadmitted_pairs(record),
        *mistyped_grounds(record),
        *cyclic_moves(record),
        *cyclic_nesting(record),
        *retrospective_orientations(record),
        *ambiguous_purposes(record),
        *unoriented_moves(record),
        *failed_kernel(record),
        *idle_moves(record),
        *unrecorded_consequences(record),
        *unbound_slots(record),
    ]


def exposed_units(record: Derivation) -> Iterator[tuple[str, str]]:
    """Yield the units of a derivation that expose its consequences, each with its reason: the
    posits that no test confirms, and the moves whose warrant is not exact.

    >>> record = {"posits": [{"id": "p", "tests": [{"kind": "empirical", "verdict": "supports"}]}],
    ...           "moves": [{"id": "m", "warrant": {"error": "controlled"}}]}
    >>> list(exposed_units(record))
    [('p', 'posit not confirmed'), ('m', 'controlled warrant')]
    """
    reg = load_registry()
    confirming = set(reg.get("confirming_tests") or [])
    certified = reg.get("confirming_computation")
    for _, posit in _entries(record, "posits"):
        confirmed = any(
            t.get("verdict") == "supports"
            and (
                t.get("kind") in confirming
                or (t.get("kind") == "computation" and t.get("standard") == certified)
            )
            for _, t in _entries(posit, "tests")
        )
        if not confirmed and posit.get("id"):
            yield str(posit["id"]), "posit not confirmed"
    for _, move in _entries(record, "moves"):
        warrant = _mapping(move.get("warrant"))
        error = warrant.get("error")
        if error and error != "exact" and move.get("id"):
            yield str(move["id"]), f"{error} warrant"
