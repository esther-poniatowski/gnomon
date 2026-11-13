"""
Views generated from the records of a project, which present the state of its inquiry.

A view is computed from authored records by a declared rule, and is never authored itself, as
the boundary of computation of the decision against inference at run time admits. The operational
inquiry graph connects research products through their activities. The textual question tree
remains a separate hierarchy inspection command.

The question tree reads four relations that the records state:

- a question serves a problem through its field ``addresses``;
- a question narrows another one through a link of relation ``subquestion-of``;
- an answer answers a question through its field ``answers``, and an assessment assesses an
  answer through its field ``assesses``;
- a design serves a question or a problem through its field ``serves``.

The roots of the tree are the problem records. A question that addresses no problem record and
narrows no question forms a root of its own, so that every question of the project appears once.

See Also
--------
gnomon.cli : the command ``tree``, which prints the tree of a directory of records.
"""

from __future__ import annotations

from collections.abc import Iterable, Mapping
from dataclasses import dataclass, field
from typing import Any

from .act_comparisons import comparisons as act_comparisons
from .assembly import assembly_tables
from .assembly_graph import assembly_graph
from .completeness import (
    demand_met,
    narrowed,
    presupposition_denied,
    problem_questions,
    readable_obstacles,
)
from .exposure import exposure_rows
from .exposure_graph import exposure_graph
from .findings import where as field_path
from .inquiry_graph import inquiry_graph
from .itineraries import type_classes, type_holders
from .itinerary_progress import itinerary_progress_graph
from .latex import canonical_notations, declared_notations, to_latex
from .schemas import shared_vocabulary_options
from .source_state import source_state as records_source_state
from .stages import itinerary_stage
from .statement import compose_statement, load_statement_registry
from .vocabulary import formulas, upstream_of, visible_records

Records = Mapping[str, Mapping[str, Any]]


@dataclass
class Node:
    """One record of the tree, with the records that it governs."""

    identifier: str
    record: Mapping[str, Any]
    children: list[Node] = field(default_factory=list)

    def label(self) -> str:
        """Return the line of the node: its type, identifier, title and status."""
        kind = str(self.record.get("type") or "record")
        title = self.record.get("title")
        status = self.record.get("status")
        text = f"{kind} {self.identifier}"
        if title:
            text += f": {title}"
        if status:
            text += f" [{status}]"
        return text


def _of_type(records: Records, kind: str) -> list[str]:
    return sorted(key for key, record in records.items() if record.get("type") == kind)


def question_tree(records: Records) -> list[Node]:
    """Return the roots of the question tree of a set of records, keyed by identifier.

    Each problem governs the questions that address it and narrow no other question, each question
    its subquestions, its answers and the designs that serve it, and each answer its assessments.
    A question reached twice, by a cycle of links or by two parents, is shown once, under its
    first parent in identifier order.
    """
    questions = _of_type(records, "question")
    answers = _of_type(records, "answer")
    assessments = _of_type(records, "assessment")
    designs = _of_type(records, "design")
    shown: set[str] = set()

    def served(target: str) -> list[Node]:
        return [Node(key, records[key]) for key in designs if records[key].get("serves") == target]

    def answer(key: str) -> Node:
        node = Node(key, records[key])
        node.children = [
            Node(other, records[other])
            for other in assessments
            if records[other].get("assesses") == key
        ]
        return node

    def question(key: str) -> Node:
        shown.add(key)
        node = Node(key, records[key])
        node.children.extend(
            question(other)
            for other in questions
            if other not in shown and key in narrowed(records[other])
        )
        node.children.extend(
            answer(other) for other in answers if records[other].get("answers") == key
        )
        node.children.extend(served(key))
        return node

    roots: list[Node] = []
    for key in _of_type(records, "problem"):
        node = Node(key, records[key])
        node.children.extend(
            question(other)
            for other in sorted(problem_questions(key, records))
            if other not in shown
        )
        node.children.extend(served(key))
        roots.append(node)
    for key in questions:
        if key not in shown and not any(parent in records for parent in narrowed(records[key])):
            roots.append(question(key))
    for key in questions:  # questions left on a cycle of links
        if key not in shown:
            roots.append(question(key))
    return roots


def render_tree(roots: Iterable[Node]) -> str:
    """Return the tree as indented text, one record per line.

    >>> print(render_tree([Node("prob.a.b", {"type": "problem", "title": "Delay"},
    ...                         [Node("quest.a.c",
    ...                               {"type": "question", "status": "posed"})])]), end="")
    problem prob.a.b: Delay
      question quest.a.c [posed]
    """
    lines: list[str] = []

    def walk(node: Node, depth: int) -> None:
        lines.append("  " * depth + node.label())
        for child in node.children:
            walk(child, depth + 1)

    for root in roots:
        walk(root, 0)
    return "\n".join(lines) + ("\n" if lines else "")


# --- Views as generated records ------------------------------------------------------------------
#
# Each view below is a generated record: a mapping in a stable order, which `gnomon views` writes
# as YAML, and which the schema of the view, in `data/schemas/views/`, declares for a renderer
# such as Ekphrasis. Every cell of a table is a scalar, so that a renderer displays it as a table
# row; a tree or a graph is stated by a table of nodes and a table of edges.

#: The maturity that a record status states, for the records whose status is a maturity.
MATURITIES = tuple(value for value, _ in shared_vocabulary_options()[".maturity"])

#: The stages of a problem before it ends, posed or refined; a problem in either stage may close.
OPEN_PROBLEM_STATUSES = ("posed", "refined")


def _header(name: str, title: str, source_state: str, version: int) -> dict[str, Any]:
    return {
        "_schema": f"gnomon:view.{name}@{version}",
        "id": f"view.{name}",
        "type": "view",
        "title": title,
        "generated_by": "gnomon views",
        "source_state": source_state,
    }


def _source_state(records: Records, supplied: str | None) -> str:
    """Return the supplied shared state, or compute it for a directly built view."""
    return supplied if supplied is not None else records_source_state(records)


def _joined(values: Iterable[Any]) -> str:
    return ", ".join(sorted(str(v) for v in values))


def _undetermined(value: bool | None) -> str:
    return "undetermined" if value is None else ("yes" if value else "no")


def problem_state(records: Records, *, state: str | None = None) -> dict[str, Any]:
    """Return the state of each problem: its demand met, its answers and its obstacles.

    The demand met, the obstacles that the records show and a denied presupposition are computed by
    the completeness module; a problem whose demand is met while its status is still ``posed`` is
    marked, since the researcher may close it.
    """
    classes, holders = type_classes(), type_holders()
    problems, obstacles = [], []
    for key in _of_type(records, "problem"):
        problem = records[key]
        questions = problem_questions(key, records)
        answers = [a for a in _of_type(records, "answer") if records[a].get("answers") in questions]
        met = demand_met(problem, records, classes, holders)
        problems.append(
            {
                "problem": key,
                "title": str(problem.get("title") or ""),
                "status": str(problem.get("status") or ""),
                "result_type": str(problem.get("result_type") or ""),
                "request": str(problem.get("request") or ""),
                "demand_met": _undetermined(met),
                "presupposition_denied": _undetermined(presupposition_denied(problem, records)),
                "accepted": _joined(a for a in answers if records[a].get("status") == "accepted"),
                "candidates": _joined(
                    a
                    for a in answers
                    if records[a].get("status") in ("entertained", "hypothesized")
                ),
                "may_close": bool(met) and problem.get("status") in OPEN_PROBLEM_STATUSES,
            }
        )
        stated = {
            str(o.get("obstacle"))
            for o in problem.get("knowledge_obstacles") or []
            if isinstance(o, Mapping)
        }
        for obstacle, derived in sorted(
            readable_obstacles(problem, records, classes, holders).items()
        ):
            obstacles.append(
                {
                    "problem": key,
                    "obstacle": obstacle,
                    "stated": obstacle in stated,
                    "derived": derived,
                }
            )
    return {
        **_header("problem-state", "State of each problem", _source_state(records, state), 3),
        "problems": problems,
        "obstacles": obstacles,
    }


def next_act(
    diagnosis_document: Mapping[str, Any],
    source_state: str,
    records: Records | None = None,
) -> dict[str, Any]:
    """Return the conditions and acts from the diagnosis of ``gnomon status``.

    Each open condition separates the activities available now from the input requirements that
    must be satisfied before its other activities can run.
    """
    conditions, open_conditions, refuted = [], [], []
    for question in diagnosis_document.get("questions") or []:
        for route in question["routes"]:
            where = {"question": question["question"], "route": route["route"]}
            conditions += [
                {
                    **where,
                    "condition": c["condition"],
                    "state": c["state"],
                    "source": c["source"],
                }
                for c in route["conditions"]
            ]
            open_conditions += [
                {
                    **where,
                    "condition": o["condition"],
                    "required_predecessors": [
                        {
                            "activity": a["activity"],
                            "missing_inputs": a.get("missing") or [],
                            "required_inputs": a.get("required_inputs") or [],
                            "output_type": a.get("output_type") or "",
                            "produces_in": a.get("produces_in") or [],
                            "may_unblock": a.get("may_unblock") or [],
                        }
                        for a in o["acts"]
                        if not a["ready"]
                    ],
                    "ready_acts": [
                        {
                            "activity": a["activity"],
                            "required_inputs": a.get("required_inputs") or [],
                            "output_type": a.get("output_type") or "",
                            "produces_in": a.get("produces_in") or [],
                            "may_unblock": a.get("may_unblock") or [],
                            "conditional": bool(a.get("conditional")),
                        }
                        for a in o["acts"]
                        if a["ready"]
                    ],
                }
                for o in route["open"]
            ]
            refuted += [{**where, "condition": r["condition"]} for r in route["refuted"]]
    itineraries = diagnosis_document.get("itineraries") or {}
    signals = (
        [{"record": r, "signal": "impeached"} for r in itineraries.get("impeached") or []]
        + [{"record": r, "signal": "conditional"} for r in itineraries.get("conditional") or []]
        + [{"record": s, "signal": "judge anew"} for s in itineraries.get("judge_anew") or []]
    )
    revisions = [
        {
            "step": r["step"],
            "record": r["record"],
            "kind": r["kind"],
            "to_review": ", ".join(
                f"{d} via {r['reasons'][d]}" if d in (r.get("reasons") or {}) else d
                for d in sorted(r["to_review"])
            ),
        }
        for r in diagnosis_document.get("revisions") or []
    ]
    narrowings = [
        {
            "answer": n["answer"],
            "holds_on": n["holds_on"],
            "test": n["test"],
            "assessment": n["assessment"],
        }
        for n in diagnosis_document.get("narrowings") or []
    ]
    return {
        **_header("next-act", "Open conditions and ready acts", source_state, 8),
        "conditions": conditions,
        "open_conditions": open_conditions,
        "comparisons": act_comparisons(records or {}),
        "refuted": refuted,
        "revisions": revisions,
        "signals": signals,
        "narrowings": narrowings,
    }


def exposure(records: Records, *, state: str | None = None) -> dict[str, Any]:
    """Return, for each answer, the units that expose it to revision, as the exposure rule and the
    exposure of a derivation state, computed by the walk of :mod:`gnomon.exposure`."""
    rows = list(exposure_rows(records))
    return {
        **_header(
            "exposure",
            "Exposure of each answer to revision",
            _source_state(records, state),
            6,
        ),
        "graph": exposure_graph(records, rows),
        "exposures": rows,
    }


def assembly(records: Records, *, state: str | None = None) -> dict[str, Any]:
    """Return the assembly of each level: its components, parts, citations, gaps, limits and
    excluded parts, as the decision on the assembly of a level states and the module
    :mod:`gnomon.assembly` computes."""
    tables = assembly_tables(records)
    return {
        **_header("assembly", "Assembly of each level", _source_state(records, state), 3),
        "graph": assembly_graph(records, tables),
        **tables,
    }


def itinerary_progress(
    records: Records,
    impeached: set[str],
    conditional: set[str],
    *,
    state: str | None = None,
) -> dict[str, Any]:
    """Return each itinerary stage and its complete output-usability dependency graph."""
    return {
        **_header(
            "itinerary-progress",
            "Progress of each itinerary",
            _source_state(records, state),
            4,
        ),
        "itineraries": [
            {
                "itinerary": key,
                "addresses": str(records[key].get("addresses") or ""),
                "stage": itinerary_stage(records[key], records),
            }
            for key in _of_type(records, "itinerary")
        ],
        "graph": itinerary_progress_graph(records, impeached, conditional),
    }


def maturity_map(records: Records, *, state: str | None = None) -> dict[str, Any]:
    """Return the maturity of the marked fields of each record, and the default of each record.

    A field left unmarked takes the maturity that the status of its record states, when that status
    is a maturity, and ``provisional`` otherwise, as the maturity of a field specifies.
    """
    rows = []
    for key in sorted(records):
        record = records[key]
        if record.get("type") in ("itinerary", "view", "vocabulary"):
            continue
        status = record.get("status")
        rows.append(
            {
                "record": key,
                "field": "(default)",
                "maturity": status if status in MATURITIES else "provisional",
            }
        )
        for path, value in sorted((record.get("maturity") or {}).items()):
            rows.append({"record": key, "field": str(path), "maturity": str(value)})
    return {
        **_header("maturity", "Maturity of each record", _source_state(records, state), 2),
        "fields": rows,
    }


def question_tree_view(records: Records, *, state: str | None = None) -> dict[str, Any]:
    """Return the question tree as a table of nodes and a table of edges, for a renderer of
    trees."""
    nodes, edges = [], []

    def walk(node: Node, parent: str | None, depth: int) -> None:
        nodes.append(
            {
                "id": node.identifier,
                "kind": str(node.record.get("type") or ""),
                "title": str(node.record.get("title") or ""),
                "status": str(node.record.get("status") or ""),
                "depth": depth,
            }
        )
        if parent is not None:
            edges.append({"parent": parent, "child": node.identifier})
        for child in node.children:
            walk(child, node.identifier, depth + 1)

    for root in question_tree(records):
        walk(root, None, 0)
    return {
        **_header("question-tree", "Question tree", _source_state(records, state), 3),
        "nodes": nodes,
        "edges": edges,
    }


def inquiry_graph_view(records: Records, *, state: str | None = None) -> dict[str, Any]:
    """Return the operational inquiry graph of products, activities, and typed relations."""
    return {
        **_header(
            "inquiry-graph",
            "Operational inquiry graph",
            _source_state(records, state),
            1,
        ),
        "graph": inquiry_graph(records),
    }


def question_statements(records: Records, *, state: str | None = None) -> dict[str, Any]:
    """Return, for each question and question schema, its authored statement beside the one composed
    from its fields, with the slots of the frame that the fields leave unfilled."""
    registry = load_statement_registry()
    rows = []
    for key in sorted(
        k for k, r in records.items() if r.get("type") in ("question", "question-schema")
    ):
        question = records[key]
        composed = compose_statement(question, records, registry)
        rows.append(
            {
                "question": key,
                "aim": str((question.get("task") or {}).get("epistemic_aim") or ""),
                "authored": str(question.get("statement") or ""),
                "composed": composed.text,
                "gaps": ", ".join(composed.gaps),
            }
        )
    return {
        **_header(
            "question-statements",
            "Statement of each question",
            _source_state(records, state),
            3,
        ),
        "statements": rows,
    }


# Expression rendering combines the visible record closure, local operators and canonical notation.
# pylint: disable-next=too-many-locals
def expression_forms(records: Records, *, state: str | None = None) -> dict[str, Any]:
    """Return the LaTeX form of each expression of each record, composed from the notations of
    the symbols that the record sees and of the operators of its target system, as the module
    :mod:`gnomon.latex` states."""
    local: dict[str, dict[str, str]] = {}
    for record in records.values():
        if record.get("type") == "operators" and isinstance(record.get("target_system"), str):
            ops = local.setdefault(str(record["target_system"]), {})
            for op in record.get("operators") or []:
                if isinstance(op, Mapping) and op.get("symbol") and op.get("notation"):
                    ops.setdefault(str(op["symbol"]), str(op["notation"]))
    rows: list[dict[str, str]] = []
    for name in sorted(records):
        record = records[name]
        if record.get("type") in ("view", "vocabulary"):
            continue
        seen = [record, *visible_records(record, records), upstream_of(record, records)]
        seen += [upstream_of(other, records) for other in seen]
        targets = {str(r.get("id")) for r in seen if r and r.get("type") == "target-system"}
        if isinstance(record.get("target_system"), str):
            targets.add(str(record["target_system"]))
        operators = dict(canonical_notations())
        for target in sorted(targets):
            operators.update(local.get(target, {}))
        symbols = declared_notations(r for r in seen if r and r.get("type") != "operators")
        for _, place, text, _ in formulas(record):
            form = to_latex(text, operators, symbols)
            if form is not None:
                rows.append(
                    {
                        "record": name,
                        "field": field_path(place),
                        "expression": str(text),
                        "latex": form,
                    }
                )
    return {
        **_header(
            "expressions",
            "LaTeX form of each expression",
            _source_state(records, state),
            2,
        ),
        "expressions": rows,
    }


def all_views(
    records: Records,
    diagnosis_document: Mapping[str, Any],
    impeached: set[str],
    conditional: set[str],
) -> dict[str, dict[str, Any]]:
    """Return the views of a set of records, keyed by the name of each view.

    The diagnosis of the conditions of answerability, and the impeached and conditional records of
    the itineraries, are computed by the caller, which reads them per problem.
    """
    state = records_source_state(records)
    built = [
        problem_state(records, state=state),
        next_act(diagnosis_document, state, records),
        exposure(records, state=state),
        assembly(records, state=state),
        itinerary_progress(records, impeached, conditional, state=state),
        maturity_map(records, state=state),
        inquiry_graph_view(records, state=state),
        question_statements(records, state=state),
        expression_forms(records, state=state),
    ]
    return {str(view["id"]).removeprefix("view."): view for view in built}
