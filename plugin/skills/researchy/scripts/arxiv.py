#!/usr/bin/env python3
"""Fetch an arXiv paper so the agent can open it instead of recalling it.

    arxiv.py meta ID [ID ...]   # title, authors, year, abstract for each ID
    arxiv.py get ID             # save papers/<ID>/paper.html and paper.txt

"Opened in this session" is what the `source-exists` grade means, and this
script is how a paper gets opened. Downloads go to papers/, which is ignored
by git: most arXiv papers are under a licence that lets you read them but not
redistribute them, so the text must not be committed or published.

Network access uses curl, because curl follows the session's proxy settings.
"""
from __future__ import annotations

import re
import subprocess
import sys
import xml.etree.ElementTree as ET
from html.parser import HTMLParser
from pathlib import Path

ATOM = {"a": "http://www.w3.org/2005/Atom"}
ID_RE = re.compile(r"^\d{4}\.\d{4,5}(v\d+)?$")
BLOCK_TAGS = {"p", "div", "section", "li", "br", "tr", "figcaption", "h1", "h5", "h6"}
SKIP_TAGS = {"script", "style", "nav", "footer", "header", "button"}


def _squash(text: str | None) -> str:
    return re.sub(r"\s+", " ", text or "").strip()


def parse_meta(atom_xml: str) -> list[dict]:
    """Parse an arXiv API response into one dict per paper."""
    papers = []
    for entry in ET.fromstring(atom_xml).findall("a:entry", ATOM):
        url = _squash(entry.findtext("a:id", "", ATOM))
        if "/abs/" not in url:  # the API returns an error entry for a bad ID
            continue
        papers.append({
            "id": url.split("/abs/")[-1],
            "title": _squash(entry.findtext("a:title", "", ATOM)),
            "authors": [_squash(a.findtext("a:name", "", ATOM))
                        for a in entry.findall("a:author", ATOM)],
            "year": _squash(entry.findtext("a:published", "", ATOM))[:4],
            "abstract": _squash(entry.findtext("a:summary", "", ATOM)),
        })
    return papers


class _ToText(HTMLParser):
    """arXiv's HTML (LaTeXML) to plain text.

    Each formula is replaced by its LaTeX source, which arXiv stores in the
    <math alttext="..."> attribute; the rendered MathML children are dropped.
    Section headings become Markdown headings so the text can be navigated.
    """

    def __init__(self) -> None:
        super().__init__()
        self.out: list[str] = []
        self.math = 0
        self.skip = 0

    def handle_starttag(self, tag, attrs):
        if tag in SKIP_TAGS:
            self.skip += 1
        if tag == "math":
            self.math += 1
            alt = dict(attrs).get("alttext")
            if self.math == 1 and alt:
                self.out.append(f"${alt}$")
        if tag in ("h2", "h3", "h4"):
            self.out.append("\n\n" + "#" * int(tag[1]) + " ")
        elif tag in BLOCK_TAGS:
            self.out.append("\n")

    def handle_endtag(self, tag):
        if tag in SKIP_TAGS:
            self.skip -= 1
        if tag == "math":
            self.math -= 1
        if tag in BLOCK_TAGS or tag in ("h2", "h3", "h4"):
            self.out.append("\n")

    def handle_data(self, data):
        if not self.math and not self.skip:
            self.out.append(data)


def html_to_text(html: str) -> str:
    parser = _ToText()
    parser.feed(html)
    text = re.sub(r"[ \t]+", " ", "".join(parser.out))
    return re.sub(r"\n\s*\n+", "\n\n", text).strip() + "\n"


def _curl(url: str) -> str:
    result = subprocess.run(
        ["curl", "-sS", "--fail", "--location", "--max-time", "90", url],
        capture_output=True, text=True,
    )
    if result.returncode != 0:
        raise SystemExit(f"could not fetch {url}: {result.stderr.strip()}")
    return result.stdout


def main(argv: list[str]) -> int:
    if len(argv) < 2 or argv[0] not in ("meta", "get"):
        print(__doc__)
        return 2
    ids = argv[1:]
    for arxiv_id in ids:
        if not ID_RE.match(arxiv_id):
            raise SystemExit(f"not an arXiv ID: {arxiv_id}")

    if argv[0] == "meta":
        xml = _curl("https://export.arxiv.org/api/query?max_results=100&id_list=" + ",".join(ids))
        found = parse_meta(xml)
        for paper in found:
            print(f"{paper['id']} | {paper['year']} | {paper['title']}")
            print(f"   authors: {', '.join(paper['authors'])}")
            print(f"   abstract: {paper['abstract']}")
        missing = [i for i in ids if not any(p["id"].startswith(i.split("v")[0]) for p in found)]
        for arxiv_id in missing:
            print(f"{arxiv_id} | NOT FOUND")
        return 1 if missing else 0

    arxiv_id = ids[0]
    target = Path("papers") / arxiv_id
    target.mkdir(parents=True, exist_ok=True)
    html = _curl(f"https://arxiv.org/html/{arxiv_id}")
    (target / "paper.html").write_text(html, encoding="utf-8")
    (target / "paper.txt").write_text(html_to_text(html), encoding="utf-8")
    print(f"saved {target}/paper.html and {target}/paper.txt")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
