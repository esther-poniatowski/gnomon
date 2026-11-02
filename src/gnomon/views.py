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
        if isinstance(link, Mapping) and link.get("relation") == "subquestion-of" and link.get("question")
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
        node.children = [Node(other, records[other]) for other in assessments
                         if records[other].get("assesses") == key]
        return node

    def question(key: str) -> Node:
        shown.add(key)
        node = Node(key, records[key])
        node.children.extend(question(other) for other in questions
                             if other not in shown and key in narrowed(records[other]))
        node.children.extend(answer(other) for other in answers if records[other].get("answers") == key)
        node.children.extend(served(key))
        return node

    roots: list[Node] = []
    for key in _of_type(records, "problem"):
        node = Node(key, records[key])
        node.children.extend(question(other) for other in questions
                             if other not in shown and records[other].get("addresses") == key
                             and not narrowed(records[other]))
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
    ...                         [Node("quest.a.c", {"type": "question", "status": "posed"})])]), end="")
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
