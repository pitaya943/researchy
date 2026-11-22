#!/usr/bin/env python3
"""Build the highlight-to-explain reading page for one paper.

    build_reader.py ID      # e.g. 2106.01340v3

Joins papers/<ID>/paper.html (from arxiv.py get) with guides/<ID without
version>.md and writes papers/<ID>/reader.html. The output holds the paper's
full text, so it stays under papers/ (ignored by git) and is meant for a
private page only.
"""
from __future__ import annotations

import html
import json
import re
import sys
from html.parser import HTMLParser
from pathlib import Path

import yaml

# Removed together with everything inside them.
DROP = {"script", "style", "nav", "button", "form", "input", "iframe", "object", "embed",
        "link", "meta", "img", "svg", "annotation", "annotation-xml", "base"}
VOID = {"br", "hr", "col", "wbr"}
DROP_ATTRS = {"style", "src", "srcset", "target", "rel"}


class _Article(HTMLParser):
    """Copy the <article> of an arXiv HTML page, keeping only inert markup.

    Scripts, styles, images, forms and event handlers are removed. Links to
    the paper's own anchors are made relative so they stay inside the page;
    other links must be https and open in a new tab. Each formula keeps its
    MathML (browsers render it) but loses the duplicate TeX annotation.
    """

    def __init__(self, own_url: str) -> None:
        super().__init__(convert_charrefs=True)
        self.own_url = own_url
        self.out: list[str] = []
        self.inside = 0   # depth inside <article>
        self.dropping = 0  # depth inside a dropped element

    def _attrs(self, attrs) -> str:
        kept = []
        for name, value in attrs:
            if name.startswith("on") or name in DROP_ATTRS or value is None:
                continue
            if name == "href":
                if value.startswith(self.own_url + "#"):
                    value = value[len(self.own_url):]
                elif value.startswith("https://"):
                    kept.append('target="_blank" rel="noopener"')
                elif not value.startswith("#"):
                    continue
            kept.append(f'{name}="{html.escape(value, quote=True)}"')
        return (" " + " ".join(kept)) if kept else ""

    def handle_starttag(self, tag, attrs):
        if tag == "article":
            self.inside += 1
            if self.inside == 1:
                return
        if not self.inside:
            return
        if self.dropping or tag in DROP:
            if tag not in VOID:
                self.dropping += 1
            return
        self.out.append(f"<{tag}{self._attrs(attrs)}>")

    def handle_startendtag(self, tag, attrs):
        if self.inside and not self.dropping and tag not in DROP:
            self.out.append(f"<{tag}{self._attrs(attrs)}>" if tag in VOID else f"<{tag}{self._attrs(attrs)}></{tag}>")

    def handle_endtag(self, tag):
        if not self.inside:
            return
        if self.dropping:
            if tag not in VOID:
                self.dropping -= 1
            return
        if tag == "article":
            self.inside -= 1
            if self.inside == 0:
                return
        if tag not in VOID:
            self.out.append(f"</{tag}>")

    def handle_data(self, data):
        if self.inside and not self.dropping:
            self.out.append(html.escape(data, quote=False))


def extract_article(page_html: str, own_url: str) -> str:
    parser = _Article(own_url)
    parser.feed(page_html)
    return "".join(parser.out)


UNIT_RE = re.compile(r"^(\d+)\. \*\*(.+?)\*\* — (.*)$")
ANCHOR_RE = re.compile(r"\]\(https://arxiv\.org/html/[^#)]+#([^)]+)\)")


def parse_guide(text: str) -> dict:
    """Read a reading guide (see guides/) into the data the page needs."""
    front, body = re.match(r"^---\n(.*?)\n---\n(.*)$", text, re.DOTALL).groups()
    meta = yaml.safe_load(front)

    prereqs = []
    chapter0 = body.split("## Chapter 0", 1)[1].split("\n## ", 1)[0] if "## Chapter 0" in body else ""
    for line in chapter0.splitlines():
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) == 4 and cells[0] not in ("Concept", "") and not set(cells[0]) <= {"-"}:
            prereqs.append({"concept": cells[0], "neededFor": cells[1], "first": cells[3].lower() == "learn first"})

    units, section = [], ""
    for line in body.splitlines():
        if line.startswith("## "):
            section = line[3:]
        match = UNIT_RE.match(line)
        if match:
            anchor = ANCHOR_RE.search(match.group(3))
            units.append({"n": int(match.group(1)), "title": match.group(2), "anchor": anchor.group(1) if anchor else "",
                          "needs": "", "question": "", "provisional": section.startswith("Later units")})
        elif units and line.strip().startswith("Needs:"):
            units[-1]["needs"] = line.strip()[len("Needs:"):].strip()
        elif units and line.strip().startswith("Before you read:"):
            units[-1]["question"] = line.strip()[len("Before you read:"):].strip()
    return {"paper": meta["paper"], "title": meta["title"], "authors": meta["authors"], "prereqs": prereqs, "units": units}


def build(page_html: str, guide_text: str, template: str, own_url: str) -> str:
    guide = parse_guide(guide_text)
    article = extract_article(page_html, own_url)
    missing = [u["n"] for u in guide["units"] if u["anchor"] and f'id="{u["anchor"]}"' not in article]
    if missing:
        raise SystemExit(f"guide units point at anchors the paper does not have: {missing}")
    # "</" inside a JSON string would end the <script> element early.
    data = json.dumps(guide, ensure_ascii=False).replace("</", "<\\/")
    return (template.replace("__TITLE__", html.escape(guide["title"] + " Reader"))
            .replace("__GUIDE_JSON__", data).replace("__ARTICLE__", article))


def main(argv: list[str]) -> int:
    if len(argv) != 1 or not re.match(r"^\d{4}\.\d{4,5}(v\d+)?$", argv[0]):
        print(__doc__)
        return 2
    paper_id = argv[0]
    folder = Path("papers") / paper_id
    guide_path = Path("guides") / (paper_id.split("v")[0] + ".md")
    template = (Path(__file__).parent / "reader_template.html").read_text(encoding="utf-8")
    page = build((folder / "paper.html").read_text(encoding="utf-8"), guide_path.read_text(encoding="utf-8"),
                 template, f"https://arxiv.org/html/{paper_id}")
    (folder / "reader.html").write_text(page, encoding="utf-8")
    print(f"wrote {folder / 'reader.html'} ({len(page) // 1024} KiB)")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
