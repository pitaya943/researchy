#!/usr/bin/env python3
"""Library tooling: validate concept cards and build INDEX.md.

Data model (see docs/library-format.md):

* One concept = one Markdown file ``library/<id>.md`` with YAML frontmatter.
  The directory is flat on purpose: a concept usually belongs to several
  topics (many-to-many), and a folder tree can express only one of them.
* Classification (``topics``) and typed relations (``links``) live inside the
  card. INDEX.md is a *derived view* of them, rebuilt by this script and never
  edited by hand, so it cannot drift from the cards.
* A link may point at a concept that has no card yet. That is not an error:
  those targets are the "frontier", i.e. what is known to exist but has not
  been learned.

Usage:
    library.py check [--root DIR]            # exit 1 if any card is invalid
    library.py index [--root DIR] [--check]  # write INDEX.md, or verify it

Finding a card is deliberately not this script's job: the agent reads
INDEX.md and the cards directly (see .claude/skills/lookup).
"""
from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path

import yaml

# Check grades. A grade states only which check was actually performed:
#   quote-verified  the quoted text was found in the source
#   source-exists   the source resolves, its content was not compared
#   model-only      nothing was checked; the model said so
GRADES_NEEDING_SOURCE = {"quote-verified", "source-exists"}
GRADES = GRADES_NEEDING_SOURCE | {"model-only"}

# Only one direction of a relation is stored, so two cards cannot disagree.
# To see what points at a card, search library/ for "to: <id>".
LINK_TYPES = {"prerequisite", "special-case-of", "used-in", "related", "contrasts-with"}

ID_RE = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
CLAIM_RE = re.compile(r"^- \[([a-z-]+)(?:: ([\w.-]+))?\] \S")
REQUIRED_FIELDS = ("id", "title", "topics", "created")


@dataclass
class Card:
    path: Path
    meta: dict
    body: str
    problems: list[str] = field(default_factory=list)

    @property
    def id(self) -> str:
        return str(self.meta.get("id", self.path.stem))

    @property
    def title(self) -> str:
        return str(self.meta.get("title", self.id))

    @property
    def aliases(self) -> list[str]:
        return [str(a) for a in self.meta.get("aliases") or []]

    @property
    def topics(self) -> list[str]:
        return [str(t) for t in self.meta.get("topics") or []]

    @property
    def links(self) -> list[tuple[str, str]]:
        """(type, target id) pairs; malformed entries are reported by check."""
        out = []
        for link in self.meta.get("links") or []:
            if isinstance(link, dict) and "type" in link and "to" in link:
                out.append((str(link["type"]), str(link["to"])))
        return out

    @property
    def names(self) -> list[str]:
        """Every string a reader might type to mean this card."""
        return [self.id, self.title, *self.aliases]


def parse_card(path: Path) -> Card:
    text = path.read_text(encoding="utf-8")
    match = re.match(r"^---\n(.*?)\n---\n?(.*)$", text, re.DOTALL)
    if not match:
        return Card(path, {}, text, ["missing YAML frontmatter"])
    try:
        meta = yaml.safe_load(match.group(1)) or {}
    except yaml.YAMLError as exc:
        return Card(path, {}, match.group(2), [f"invalid YAML: {exc}"])
    if not isinstance(meta, dict):
        return Card(path, {}, match.group(2), ["frontmatter is not a mapping"])
    return Card(path, meta, match.group(2))


def load_library(root: Path) -> list[Card]:
    return [parse_card(p) for p in sorted((root / "library").glob("*.md"))]


def claim_lines(body: str) -> list[str]:
    """Bullets under the claims heading ('## 主張' or '## Claims'), up to the next heading."""
    lines, inside = [], False
    for line in body.splitlines():
        if line.startswith("## "):
            inside = line.strip() in ("## 主張", "## Claims")
        elif inside and line.startswith("- "):
            lines.append(line)
    return lines


def _check_card(card: Card) -> list[str]:
    problems = list(card.problems)
    if problems:  # unparseable: nothing else can be checked
        return problems
    meta = card.meta
    for name in REQUIRED_FIELDS:
        if not meta.get(name):
            problems.append(f"missing required field '{name}'")
    if not ID_RE.match(card.id):
        problems.append(f"id '{card.id}' must be lowercase words joined by '-'")
    if card.id != card.path.stem:
        # The file name is the stable address other cards link to.
        problems.append(f"id '{card.id}' does not match file name '{card.path.stem}'")
    for link in meta.get("links") or []:
        if not (isinstance(link, dict) and "type" in link and "to" in link):
            problems.append(f"link {link!r} needs 'type' and 'to'")
        elif link["type"] not in LINK_TYPES:
            problems.append(f"unknown link type '{link['type']}'")
        elif link["to"] == card.id:
            problems.append("card links to itself")
    sources = meta.get("sources") or {}
    for line in claim_lines(card.body):
        m = CLAIM_RE.match(line)
        if not m or m.group(1) not in GRADES:
            problems.append(f"claim without a valid grade label: {line[:60]}")
            continue
        grade, key = m.groups()
        if grade in GRADES_NEEDING_SOURCE and key not in sources:
            problems.append(f"'{grade}' claim cites unknown source '{key}': {line[:60]}")
    return problems


def _prerequisite_cycle(cards: list[Card]) -> list[str] | None:
    """Return one cycle of prerequisite edges, or None. Iterative-safe DFS."""
    graph = {c.id: [to for kind, to in c.links if kind == "prerequisite"] for c in cards}
    state: dict[str, int] = {}  # 1 = on the current path, 2 = finished
    path: list[str] = []

    def visit(node: str) -> list[str] | None:
        state[node] = 1
        path.append(node)
        for nxt in graph.get(node, []):
            if state.get(nxt) == 1:
                return path[path.index(nxt):] + [nxt]
            if nxt in graph and nxt not in state:
                found = visit(nxt)
                if found:
                    return found
        path.pop()
        state[node] = 2
        return None

    for node in sorted(graph):
        if node not in state:
            found = visit(node)
            if found:
                return found
    return None


def check(cards: list[Card]) -> list[str]:
    """All problems in the library, as 'file: message' strings."""
    problems = [f"{c.path.name}: {p}" for c in cards for p in _check_card(c)]
    # A name must identify one card, otherwise the by-name index is ambiguous.
    owners: dict[str, str] = {}
    for card in cards:
        for name in {n.casefold() for n in card.names}:
            if name in owners and owners[name] != card.id:
                problems.append(
                    f"{card.path.name}: name '{name}' is also used by '{owners[name]}'"
                )
            owners.setdefault(name, card.id)
    cycle = _prerequisite_cycle(cards)
    if cycle:
        problems.append("prerequisite cycle: " + " -> ".join(cycle))
    return problems


def frontier(cards: list[Card]) -> dict[str, list[str]]:
    """Link targets with no card yet -> ids of the cards that mention them."""
    known = {c.id for c in cards}
    missing: dict[str, list[str]] = {}
    for card in cards:
        for _, to in card.links:
            if to not in known:
                missing.setdefault(to, []).append(card.id)
    return missing


def build_index(cards: list[Card]) -> str:
    """Render INDEX.md. Output is deterministic so it can be diffed in CI."""
    ref = lambda c: f"[{c.title}](library/{c.id}.md)"  # noqa: E731
    out = [
        "# Library index",
        "",
        "<!-- Generated by scripts/library.py index. Do not edit by hand. -->",
        "",
        "## By topic",
        "",
    ]
    by_topic: dict[str, list[Card]] = {}
    for card in cards:
        for topic in card.topics:
            by_topic.setdefault(topic, []).append(card)
    for topic in sorted(by_topic):
        out.append(f"### {topic}")
        out += [f"- {ref(c)}" for c in sorted(by_topic[topic], key=lambda c: c.id)]
        out.append("")

    out += ["## By name", ""]
    names = sorted(
        ((name, card) for card in cards for name in [card.title, *card.aliases]),
        key=lambda pair: (pair[0].casefold(), pair[1].id),
    )
    out += [f"- {name}: {ref(card)}" for name, card in names]
    out.append("")

    out += ["## Frontier (mentioned, not yet learned)", ""]
    missing = frontier(cards)
    out += [f"- `{to}` (from {', '.join(sorted(set(src)))})" for to, src in sorted(missing.items())]
    out.append("")

    out += ["## By date", ""]
    dated = sorted(cards, key=lambda c: (str(c.meta.get("created", "")), c.id), reverse=True)
    out += [f"- {c.meta.get('created', '?')}: {ref(c)}" for c in dated]
    return "\n".join(out).rstrip() + "\n"


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    parser.add_argument("command", choices=["check", "index"])
    parser.add_argument("--root", type=Path, default=Path.cwd())
    parser.add_argument("--check", action="store_true", help="index: verify, do not write")
    args = parser.parse_args(argv)
    cards = load_library(args.root)

    if args.command == "check":
        problems = check(cards)
        print("\n".join(problems) if problems else f"{len(cards)} cards OK")
        return 1 if problems else 0

    target, rendered = args.root / "INDEX.md", build_index(cards)
    if args.check:
        current = target.read_text(encoding="utf-8") if target.exists() else ""
        if current != rendered:
            print("INDEX.md is out of date; run: scripts/library.py index")
            return 1
        return 0
    target.write_text(rendered, encoding="utf-8")
    print(f"wrote {target}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
