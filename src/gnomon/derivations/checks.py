"""
The checks of one derivation record: its units, its interpretations, its orientations, its segments,
its kernel, its slots and its consequences.

The rules that these checks apply are declared in the registry of derivations, which the notes of
the theory own, and the specification of the derivation record lists them as its checks.

Functions
---------
unknown_units
    Return the units named inside a derivation that the record does not declare.
repeated_units
    Return the identifiers that several units of a derivation share.
restated_facts
    Return the root sought and the records of consequences that restate the record served.
unadmitted_pairs
    Return the interpretations whose kind their item does not admit.
mistyped_grounds
    Return the cited interpretations of the wrong kind, and the grounds of the wrong type.
cyclic_moves
    Return the cycles among the producers of a derivation.
cyclic_nesting
    Return the cycles of nested segments and of replaced soughts.
retrospective_orientations
    Return the orientations that cite an object established by their own unit or after it.
retrospective_licenses
    Return the warrants that cite a property of an object established by their move or after it.
ambiguous_purposes
    Return the orientations that state both or neither of a sought and a change.
unoriented_moves
    Return the non-routine moves and the segments that no orientation selects.
broken_bridges
    Return the moves of a segment that take what the segment neither takes nor yields.
failed_kernel
    Return a finding when a route to a consequence of the root sought avoids the kernel.
unreached_consequences
    Return the consequences stated by an object that no producer yields.
idle_moves
    Return the moves that yield nothing used.
unrecorded_consequences
    Return the consequences of the root sought that name no record.
unbound_slots
    Return the slots that no move binds, unless an impasse stops their route.
derivation_problems
    Return every finding of the checks of a derivation.
"""

from __future__ import annotations

from typing import Any, Mapping

from .. import findings as rules
from ..findings import Entry, Finding, finding
from .graph import (
    REFERENCE,
    UNIT_LISTS,
    Derivation,
    by_id,
    concerned,
    downstream,
    enclosing,
    entries,
    internal_fields,
    kind_of,
    load_registry,
    mapping,
    names,
    producers_of,
    reachable,
    root_sought,
    served_unit,
    units,
    values_at,
    where,
)


def unknown_units(record: Derivation) -> list[Finding]:
    """Return the units named inside a derivation that the record does not declare, or declares in
    a list that the field does not admit.

    A dotted reference names a unit of another record, and a value holding a space is prose, so
    neither is read here; the placeholder that the template of the field writes is left aside.

    >>> [f.text for f in unknown_units({"moves": [{"id": "m", "inputs": ["x"]}]})]
    ['moves.m.inputs: x names no unit among objects, posits']
    >>> record = {"moves": [{"id": "m", "warrant": {"applies_because": "p"}}]}
    >>> [f.text for f in unknown_units(record)]
    ['moves.m.warrant.applies_because: p names no unit among interpretations']
    """
    kinds = kind_of(record)
    found = []
    for path, admitted, placeholder in internal_fields():
        for locus, value in values_at(record, path):
            for name in names(value):
                if "." in name or " " in name.strip() or name == placeholder:
                    continue
                if kinds.get(name) in admitted:
                    continue
                found.append(
                    finding(
                        rules.DERIVATION_UNKNOWN_UNIT,
                        f"{where(locus)}: {name} names no unit among {', '.join(admitted)}",
                        *locus,
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
        for _, item in entries(record, name):
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


def _admitted_kinds(
    record: Derivation, ident: str, pairs: Mapping[str, Any]
) -> tuple[str, set[str]] | None:
    """Return the item that an interpretation of ``ident`` interprets and the kinds that it admits,
    or None when the unit is unknown or an object states no form. A unit of another record is an
    object or an expression, and admits the kinds of both."""
    if "." in ident:
        return "premise", set(pairs.get("object") or []) | set(pairs.get("expression") or [])
    objects = by_id(record, "objects")
    if ident in objects:
        form = objects[ident].get("form")
        if form not in ("object", "expression"):
            return None
        return str(form), set(pairs.get(form) or [])
    by_list = {
        "moves": "transformation",
        "features": "feature",
        "segments": "composite",
        "consequences": "composite",
    }
    for name, item in by_list.items():
        if ident in by_id(record, name):
            return item, set(pairs.get(item) or [])
    return None


def unadmitted_pairs(
    record: Derivation, registry: Mapping[str, Any] | None = None
) -> list[Finding]:
    """Return the interpretations whose kind their item does not admit.

    >>> record = {"moves": [{"id": "m"}],
    ...           "interpretations": [{"id": "i", "of": "m", "kind": "diagnostic"}]}
    >>> [f.text for f in unadmitted_pairs(record)]
    ['interpretations.i: a transformation admits no diagnostic interpretation']
    >>> record = {"interpretations": [{"of": "mod.a.b.x", "kind": "variation"}]}
    >>> [f.text for f in unadmitted_pairs(record)]
    ['interpretations.0: a premise admits no variation interpretation']
    """
    pairs = (registry or load_registry()).get("admitted_pairs") or {}
    found = []
    for i, entry in entries(record, "interpretations"):
        admitted = _admitted_kinds(record, str(entry.get("of")), pairs)
        kind = entry.get("kind")
        if admitted is None or not kind or kind in admitted[1]:
            continue
        found.append(
            finding(
                rules.DERIVATION_UNADMITTED_PAIR,
                f"interpretations.{entry.get('id') or i}: a {admitted[0]} admits no {kind}"
                " interpretation",
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
    """Return the fields that cite an interpretation of a kind that they do not admit, and the
    interpretations whose grounds cite no reference of the type that their kind requires.

    >>> record = {"interpretations": [{"id": "i", "kind": "process", "grounds": ["mod.a.b.law"]}],
    ...           "moves": [{"id": "m", "warrant": {"applies_because": "i"}}]}
    >>> [f.text for f in mistyped_grounds(record)]
    ['moves.m.warrant.applies_because: i is a process interpretation, not structural or magnitude']
    >>> [f.text for f in mistyped_grounds({"interpretations": [{"id": "i", "kind": "diagnostic"}]})]
    ['interpretations.i: a diagnostic interpretation cites no ground among moves, posits']
    """
    reg = registry or load_registry()
    kinds = {ident: str(e.get("kind")) for ident, e in by_id(record, "interpretations").items()}
    found = []
    for dotted, admitted in (reg.get("cited_kinds") or {}).items():
        for locus, value in values_at(record, tuple(str(dotted).split("."))):
            cited = str(value) if isinstance(value, str) else None
            if cited in kinds and kinds[str(cited)] not in admitted:
                found.append(
                    finding(
                        rules.DERIVATION_MISTYPED_GROUND,
                        f"{where(locus)}: {cited} is a {kinds[str(cited)]} interpretation, not"
                        f" {' or '.join(admitted)}",
                        *locus,
                        value=str(cited),
                    )
                )
    of_list = kind_of(record)
    for i, entry in entries(record, "interpretations"):
        required = (reg.get("ground_types") or {}).get(entry.get("kind")) or []
        classes = {REFERENCE if "." in g else of_list.get(g) for g in names(entry.get("grounds"))}
        if required and not classes & set(required):
            found.append(
                finding(
                    rules.DERIVATION_MISTYPED_GROUND,
                    f"interpretations.{entry.get('id') or i}: a {entry.get('kind')} interpretation"
                    f" cites no ground among {', '.join(required)}",
                    "interpretations",
                    Entry(i, entry),
                    "grounds",
                )
            )
    return found


def cyclic_moves(record: Derivation) -> list[Finding]:
    """Return one finding per cycle among the producers, in which a move or a segment takes what a
    later producer of the cycle yields.

    >>> record = {"moves": [{"id": "a", "inputs": ["x"], "outputs": ["y"]},
    ...                     {"id": "b", "inputs": ["y"], "outputs": ["x"]}]}
    >>> [f.text for f in cyclic_moves(record)]
    ['moves: the producers a -> b -> a depend on one another in a cycle']
    """
    producers = producers_of(record)
    after = {
        name: sorted(o for o, (ins, _) in producers.items() if outs & ins)
        for name, (_, outs) in producers.items()
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
                            f"moves: the producers {' -> '.join(cycle)} depend on one another in"
                            " a cycle",
                            "moves",
                            value=" -> ".join(cycle),
                        )
                    )
            elif state.get(nxt) is None:
                visit(nxt, [*trail, nxt])
        state[node] = 2

    for name in sorted(producers):
        if state.get(name) is None:
            visit(name, [name])
    return found


def _late(record: Derivation, unit: str, interpretation: str) -> set[str]:
    """Return the objects that an interpretation concerns and that a unit establishes, or that
    depend on it."""
    interpreted = {ident: str(e.get("of")) for ident, e in by_id(record, "interpretations").items()}
    if interpretation not in interpreted:
        return set()
    return concerned(record, interpreted[interpretation]) & downstream(record, unit)


def retrospective_orientations(record: Derivation) -> list[Finding]:
    """Return the orientations of a move or a segment whose occasion interprets an object that the
    unit yields, or that depends on it.

    >>> record = {"objects": [{"id": "y"}],
    ...           "moves": [{"id": "m", "inputs": ["x"], "outputs": ["y"]}],
    ...           "interpretations": [{"id": "i", "of": "y"}],
    ...           "orientations": [{"id": "o", "of": "m", "occasion": "i"}]}
    >>> [f.text for f in retrospective_orientations(record)]
    ['orientations.o.occasion: i interprets y, which m establishes or which depends on it']
    """
    found = []
    for i, orientation in entries(record, "orientations"):
        unit, occasion = orientation.get("of"), orientation.get("occasion")
        if not isinstance(unit, str) or not isinstance(occasion, str):
            continue
        late = _late(record, unit, occasion)
        if late:
            found.append(
                finding(
                    rules.DERIVATION_RETROSPECTIVE_ORIENTATION,
                    f"orientations.{orientation.get('id') or i}.occasion: {occasion} interprets"
                    f" {', '.join(sorted(late))}, which {unit} establishes or which depends on it",
                    "orientations",
                    Entry(i, orientation),
                    "occasion",
                    value=occasion,
                )
            )
    return found


def retrospective_licenses(record: Derivation) -> list[Finding]:
    """Return the warrants whose property interprets an object that their own move yields, or that
    depends on it, since the property is established before the move.

    >>> record = {"objects": [{"id": "y"}],
    ...           "moves": [{"id": "m", "inputs": ["x"], "outputs": ["y"],
    ...                      "warrant": {"applies_because": "i"}}],
    ...           "interpretations": [{"id": "i", "of": "y"}]}
    >>> [f.text for f in retrospective_licenses(record)]
    ['moves.m.warrant.applies_because: i interprets y, which the move establishes or depends on']
    """
    found = []
    for i, move in entries(record, "moves"):
        cited = mapping(move.get("warrant")).get("applies_because")
        if not isinstance(cited, str) or not move.get("id"):
            continue
        late = _late(record, str(move["id"]), cited)
        if late:
            found.append(
                finding(
                    rules.DERIVATION_RETROSPECTIVE_LICENSE,
                    f"moves.{move['id']}.warrant.applies_because: {cited} interprets"
                    f" {', '.join(sorted(late))}, which the move establishes or depends on",
                    "moves",
                    Entry(i, move),
                    "warrant",
                    "applies_because",
                    value=cited,
                )
            )
    return found


def _after_impasse(record: Derivation) -> set[str]:
    """Return the objects stating the answers of the soughts that replace a sought left by an
    impasse."""
    left = {str(i.get("sought")) for _, i in entries(record, "impasses") if i.get("sought")}
    successors = {
        ident for ident, s in by_id(record, "subordinate").items() if s.get("replaces") in left
    }
    return {
        str(c.get("from"))
        for _, c in entries(record, "consequences")
        if c.get("answers") in successors and c.get("from")
    }


def _diagnosed(record: Derivation) -> set[str]:
    """Return the objects that a diagnostic interpretation reads."""
    found: set[str] = set()
    for _, entry in entries(record, "interpretations"):
        if entry.get("kind") == "diagnostic":
            found |= concerned(record, str(entry.get("of")))
    return found


def _non_routine(record: Derivation, move: Mapping[str, Any], reg: Mapping[str, Any]) -> list[str]:
    """Return the features that make a move non-routine, as the record states them."""
    ident = str(move.get("id"))
    warrant = mapping(move.get("warrant"))
    inputs = set(names(move.get("inputs")))
    checks = [
        (record.get("kernel") == ident, "its declaration as kernel"),
        (
            any(s.get("introduced_by") == ident for _, s in entries(record, "slots")),
            "the slot that it introduces",
        ),
        (bool(inputs & units(record)["posits"]), "the posit that it uses"),
        (bool(inputs & _diagnosed(record)), "the diagnostic interpretation that it follows"),
        (bool(downstream(record, ident) & _after_impasse(record)), "the impasse that it follows"),
        (
            move.get("kind") in (reg.get("non_routine_kinds") or []),
            f"its kind {move.get('kind')}",
        ),
        (warrant.get("source") == "act-verdict", "the output of an act that it imports"),
        (
            bool(warrant.get("error")) and warrant.get("error") != "exact",
            f"its {warrant.get('error')} error",
        ),
    ]
    return [text for holds, text in checks if holds]


def unoriented_moves(
    record: Derivation, registry: Mapping[str, Any] | None = None
) -> list[Finding]:
    """Return the non-routine moves and the segments that no orientation selects.

    >>> [f.text for f in unoriented_moves({"moves": [{"id": "m", "kind": "take-limit"}]})]
    ['moves.m: the move is non-routine by its kind take-limit, and no orientation selects it']
    >>> [f.text for f in unoriented_moves({"segments": [{"id": "s"}]})]
    ['segments.s: no orientation selects the segment']
    """
    reg = registry or load_registry()
    oriented = {str(o.get("of")) for _, o in entries(record, "orientations")}
    found = []
    for i, move in entries(record, "moves"):
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
    for i, segment in entries(record, "segments"):
        if str(segment.get("id")) not in oriented:
            found.append(
                finding(
                    rules.DERIVATION_UNORIENTED_MOVE,
                    f"segments.{segment.get('id') or i}: no orientation selects the segment",
                    "segments",
                    Entry(i, segment),
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
    for i, orientation in entries(record, "orientations"):
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


def broken_bridges(record: Derivation) -> list[Finding]:
    """Return the moves of a segment that take an object which the segment neither takes nor yields
    through its moves, since a segment bridges its moves from its inputs to its outputs.

    >>> record = {"moves": [{"id": "a", "inputs": ["p"], "outputs": ["x"]},
    ...                     {"id": "b", "inputs": ["x", "q"], "outputs": ["y"]}],
    ...           "segments": [{"id": "s", "moves": ["a", "b"], "inputs": ["p"], "outputs": ["y"]}]}
    >>> [f.text for f in broken_bridges(record)]
    ['segments.s: the move b takes q, which the segment neither takes nor yields']
    """
    moves = by_id(record, "moves")
    found = []
    for i, segment in entries(record, "segments"):
        held = [m for m in names(segment.get("moves")) if m in moves]
        available = set(names(segment.get("inputs")))
        available |= {o for m in held for o in names(moves[m].get("outputs"))}
        for move in held:
            for missing in sorted(set(names(moves[move].get("inputs"))) - available):
                found.append(
                    finding(
                        rules.DERIVATION_BROKEN_BRIDGE,
                        f"segments.{segment.get('id') or i}: the move {move} takes {missing}, which"
                        " the segment neither takes nor yields",
                        "segments",
                        Entry(i, segment),
                        "inputs",
                        value=missing,
                    )
                )
    return found


def _root_consequences(record: Derivation) -> list[tuple[int, Mapping[str, Any]]]:
    """Return the consequences of the root sought, with their indices."""
    root = root_sought(record)
    return [(i, c) for i, c in entries(record, "consequences") if root and c.get("answers") == root]


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
    producers = producers_of(record)
    yielded: set[str] = set().union(*(outs for _, outs in producers.values()))
    premises: set[str] = set().union(*(ins for ins, _ in producers.values())) - yielded
    full = reachable(producers, premises)
    removed = {kernel} | enclosing(record, kernel)
    without = reachable({k: v for k, v in producers.items() if k not in removed}, premises)
    targets = [str(c.get("from")) for _, c in _root_consequences(record) if c.get("from")]
    return [
        finding(
            rules.DERIVATION_FAILED_KERNEL,
            f"kernel: a route from the premises reaches {target} without the kernel {kernel}",
            "kernel",
            value=target,
        )
        for target in targets
        if target in full and target in without
    ]


def unreached_consequences(record: Derivation) -> list[Finding]:
    """Return the consequences stated by an object that no move and no segment yields, so that no
    route of the derivation reaches them.

    >>> record = {"objects": [{"id": "x"}], "consequences": [{"id": "c", "from": "x"}]}
    >>> [f.text for f in unreached_consequences(record)]
    ['consequences.c: no move and no segment yields x']
    """
    yielded: set[str] = set().union(*(outs for _, outs in producers_of(record).values()))
    return [
        finding(
            rules.DERIVATION_UNREACHED_CONSEQUENCE,
            f"consequences.{c.get('id') or i}: no move and no segment yields {c.get('from')}",
            "consequences",
            Entry(i, c),
            "from",
            value=str(c.get("from")),
        )
        for i, c in entries(record, "consequences")
        if c.get("from") and str(c.get("from")) not in yielded
    ]


def unrecorded_consequences(record: Derivation) -> list[Finding]:
    """Return the consequences of the root sought that name no record stating them, when the record
    served states none either.

    >>> record = {"sought": {"id": "s"}, "consequences": [{"id": "c", "answers": "s"}]}
    >>> [f.text for f in unrecorded_consequences(record)]
    ['consequences.c: a consequence of the root sought names no record that states it']
    >>> served = {"serves": "bg.a.b.law", "consequences": [{"answers": "bg.a.b.law"}]}
    >>> unrecorded_consequences(served)
    []
    """
    if served_unit(record):
        return []
    return [
        finding(
            rules.DERIVATION_UNRECORDED_CONSEQUENCE,
            f"consequences.{c.get('id') or i}: a consequence of the root sought names no record"
            " that states it",
            "consequences",
            Entry(i, c),
            "record",
        )
        for i, c in _root_consequences(record)
        if not c.get("record")
    ]


def restated_facts(record: Derivation) -> list[Finding]:
    """Return the root sought declared by a derivation that serves a record, and the consequences
    naming the record served as their record, since the record served states both facts.

    >>> record = {"serves": "bg.a.b.law", "sought": {"id": "s"},
    ...           "consequences": [{"id": "c", "answers": "bg.a.b.law", "record": "bg.a.b.law"}]}
    >>> for f in restated_facts(record):
    ...     print(f.text)
    sought: the derivation serves bg.a.b.law, from which the root sought is read
    consequences.c.record: the record served already states the consequence
    """
    served = record.get("serves")
    if not isinstance(served, str) or not served.strip():
        return []
    found = []
    sought = record.get("sought")
    if isinstance(sought, Mapping) and any(v not in (None, "") for v in sought.values()):
        found.append(
            finding(
                rules.DERIVATION_RESTATED_FACT,
                f"sought: the derivation serves {served}, from which the root sought is read",
                "sought",
            )
        )
    for i, c in entries(record, "consequences"):
        if c.get("record") == served:
            found.append(
                finding(
                    rules.DERIVATION_RESTATED_FACT,
                    f"consequences.{c.get('id') or i}.record: the record served already states the"
                    " consequence",
                    "consequences",
                    Entry(i, c),
                    "record",
                    value=served,
                )
            )
    return found


def unbound_slots(record: Derivation) -> list[Finding]:
    """Return the slots that no move binds, unless an impasse stops the route that the slot opens:
    the unit introducing the slot then reaches the object of no consequence.

    >>> [f.text for f in unbound_slots({"slots": [{"symbol": "a"}]})]
    ['slots.a: no move binds the slot, and no impasse stops the route that it opens']
    """
    bound = {name for _, m in entries(record, "moves") for name in names(m.get("binds"))}
    stated = {str(c.get("from")) for _, c in entries(record, "consequences") if c.get("from")}
    stopped = bool(entries(record, "impasses"))
    found = []
    for i, slot in entries(record, "slots"):
        if not slot.get("symbol") or str(slot["symbol"]) in bound:
            continue
        opener = str(slot.get("introduced_by") or "")
        if stopped and not downstream(record, opener) & stated:
            continue
        found.append(
            finding(
                rules.DERIVATION_UNBOUND_SLOT,
                f"slots.{slot['symbol']}: no move binds the slot, and no impasse stops the route"
                " that it opens",
                "slots",
                Entry(i, slot),
            )
        )
    return found


def _targets(record: Derivation) -> set[str]:
    """Return the objects that an outcome or a cited interpretation concerns: the objects stating
    consequences and counterexamples, the outputs of the moves carrying a test of a posit, and the
    objects interpreted by the obstacle of an impasse, by the occasion of an orientation or by the
    property that a warrant cites."""
    interpreted = {ident: str(e.get("of")) for ident, e in by_id(record, "interpretations").items()}
    cited = {str(i.get("obstacle")) for _, i in entries(record, "impasses")}
    cited |= {str(o.get("occasion")) for _, o in entries(record, "orientations")}
    cited |= {
        str(mapping(m.get("warrant")).get("applies_because")) for _, m in entries(record, "moves")
    }
    found = {str(c.get("from")) for _, c in entries(record, "consequences") if c.get("from")}
    found |= {str(r.get("by")) for _, r in entries(record, "refutations") if r.get("by")}
    tested = values_at(record, ("posits", "tests", "by"))
    testing = {str(v) for _, v in tested if isinstance(v, str)}
    for move in testing & set(by_id(record, "moves")):
        found |= concerned(record, move)
    for name in cited & set(interpreted):
        found |= concerned(record, interpreted[name])
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
    producers = producers_of(record)
    found = []
    for i, move in entries(record, "moves"):
        ins, outs = set(names(move.get("inputs"))), set(names(move.get("outputs")))
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
        parent = {str(e.get("id")): str(e.get(key)) for _, e in entries(record, name) if e.get(key)}
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
        *restated_facts(record),
        *unadmitted_pairs(record),
        *mistyped_grounds(record),
        *cyclic_moves(record),
        *cyclic_nesting(record),
        *retrospective_orientations(record),
        *retrospective_licenses(record),
        *ambiguous_purposes(record),
        *unoriented_moves(record),
        *broken_bridges(record),
        *failed_kernel(record),
        *unreached_consequences(record),
        *idle_moves(record),
        *unrecorded_consequences(record),
        *unbound_slots(record),
    ]
