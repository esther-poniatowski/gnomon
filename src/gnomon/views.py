"""
Views generated from the records of a project, which present the state of its inquiry.

A view is computed from authored records by a declared rule, and is never authored itself, as
the boundary of computation of the decision against inference at run time admits. The question
tree is the first view: it replaces a research root record, which would restate the problems and
the questions of a project.

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

from dataclasses import dataclass, field
from typing import Any, Iterable, Mapping

from .completeness import demand_met, presupposition_denied, readable_obstacles
from .exposure import exposure_rows
from .findings import where as field_path
from .itineraries import type_classes, type_holders
from .latex import canonical_notations, declared_notations, to_latex
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


def narrowed(question: Mapping[str, Any]) -> list[str]:
    """Return the questions that a question narrows, through its links ``subquestion-of``.

    >>> narrowed({"links": [{"question": "quest.a.b", "relation": "subquestion-of"},
    ...                     {"question": "quest.a.c", "relation": "presupposes"}]})
    ['quest.a.b']
    """
    return [
        str(link["question"])
        for link in question.get("links") or []
        if isinstance(link, Mapping)
        and link.get("relation") == "subquestion-of"
        and link.get("question")
    ]


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
            for other in questions
            if other not in shown
            and records[other].get("addresses") == key
            and not narrowed(records[other])
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
MATURITIES = ("open", "provisional", "stabilized")

#: The stages of a problem before it ends, posed or refined; a problem in either stage may close.
OPEN_PROBLEM_STATUSES = ("posed", "refined")


def _header(name: str, title: str, version: int = 1) -> dict[str, Any]:
    return {
        "_schema": f"gnomon:view.{name}@{version}",
        "id": f"view.{name}",
        "type": "view",
        "title": title,
        "generated_by": "gnomon views",
    }


def _joined(values: Iterable[Any]) -> str:
    return ", ".join(sorted(str(v) for v in values))


def _undetermined(value: bool | None) -> str:
    return "undetermined" if value is None else ("yes" if value else "no")


def problem_state(records: Records) -> dict[str, Any]:
    """Return the state of each problem: its demand met, its answers and its obstacles.

    The demand met, the obstacles that the records show and a denied presupposition are computed by
    the completeness module; a problem whose demand is met while its status is still ``posed`` is
    marked, since the researcher may close it.
    """
    classes, holders = type_classes(), type_holders()
    problems, obstacles = [], []
    for key in _of_type(records, "problem"):
        problem = records[key]
        questions = {q for q in _of_type(records, "question") if records[q].get("addresses") == key}
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
        **_header("problem-state", "State of each problem"),
        "problems": problems,
        "obstacles": obstacles,
    }


def next_act(diagnosis_document: Mapping[str, Any]) -> dict[str, Any]:
    """Return the open conditions and the ready acts, flattened from the diagnosis of ``gnomon
    status``."""
    conditions, acts, refuted = [], [], []
    for question in diagnosis_document.get("questions") or []:
        for route in question["routes"]:
            where = {"question": question["question"], "route": route["route"]}
            conditions += [
                {**where, "condition": c["condition"], "state": c["state"], "source": c["source"]}
                for c in route["conditions"]
            ]
            acts += [
                {
                    **where,
                    "condition": o["condition"],
                    "activity": a["activity"],
                    "ready": a["ready"],
                    "missing": "; ".join(a.get("missing") or []),
                }
                for o in route["open"]
                for a in o["acts"]
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
    return {
        **_header("next-act", "Open conditions and ready acts"),
        "conditions": conditions,
        "acts": acts,
        "refuted": refuted,
        "revisions": revisions,
        "signals": signals,
    }


def exposure(records: Records) -> dict[str, Any]:
    """Return, for each answer, the units that expose it to revision, as the exposure rule and the
    exposure of a derivation state, computed by the walk of :mod:`gnomon.exposure`."""
    return {
        **_header("exposure", "Exposure of each answer to revision", version=2),
        "exposures": list(exposure_rows(records)),
    }


def itinerary_progress(
    records: Records, impeached: set[str], conditional: set[str]
) -> dict[str, Any]:
    """Return the steps of each itinerary in the order of their dependencies, with their verdicts.

    A step is ``impeached`` when a failed norm lies upstream of its output, ``conditional`` when a
    pending one does, and ``sound`` otherwise. The edges between steps are listed for a renderer of
    graphs.
    """
    steps_rows, edges = [], []
    for key in _of_type(records, "itinerary"):
        own = f"{key}."
        steps = {
            str(s.get("id")): s for s in records[key].get("steps") or [] if isinstance(s, Mapping)
        }
        after = {
            name: sorted(
                {
                    str(i.get("ref"))[len(own) :]
                    for i in s.get("inputs") or []
                    if isinstance(i, Mapping) and str(i.get("ref")).startswith(own)
                }
                & set(steps)
            )
            for name, s in steps.items()
        }
        order: list[str] = []
        while len(order) < len(steps):
            ready = [
                n for n in sorted(steps) if n not in order and all(p in order for p in after[n])
            ]
            order += ready or [n for n in sorted(steps) if n not in order][:1]
        for name in order:
            step = steps[name]
            output = str((step.get("output") or {}).get("ref") or "")
            state = (
                "impeached"
                if output in impeached
                else "conditional" if output in conditional else "sound"
            )
            steps_rows.append(
                {
                    "itinerary": key,
                    "step": name,
                    "activity": str(step.get("activity") or ""),
                    "verdict": str((step.get("norm") or {}).get("verdict") or ""),
                    "output": output,
                    "state": state,
                }
            )
            edges += [{"itinerary": key, "from": parent, "to": name} for parent in after[name]]
    return {
        **_header("itinerary-progress", "Progress of each itinerary", version=2),
        "itineraries": [
            {
                "itinerary": key,
                "addresses": str(records[key].get("addresses") or ""),
                "stage": itinerary_stage(records[key], records),
            }
            for key in _of_type(records, "itinerary")
        ],
        "steps": steps_rows,
        "edges": edges,
    }


def maturity_map(records: Records) -> dict[str, Any]:
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
    return {**_header("maturity", "Maturity of each record"), "fields": rows}


def question_tree_view(records: Records) -> dict[str, Any]:
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
    return {**_header("question-tree", "Question tree"), "nodes": nodes, "edges": edges}


def question_statements(records: Records) -> dict[str, Any]:
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
    return {**_header("question-statements", "Statement of each question"), "statements": rows}


def expression_forms(records: Records) -> dict[str, Any]:
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
        **_header("expressions", "LaTeX form of each expression"),
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
    built = [
        problem_state(records),
        next_act(diagnosis_document),
        exposure(records),
        itinerary_progress(records, impeached, conditional),
        maturity_map(records),
        question_tree_view(records),
        question_statements(records),
        expression_forms(records),
    ]
    return {str(view["id"]).removeprefix("view."): view for view in built}
