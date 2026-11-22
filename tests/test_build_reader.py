"""Tests for scripts/build_reader.py."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))

import build_reader  # noqa: E402

URL = "https://arxiv.org/html/1234.56789v1"
PAGE = f"""<html><body><nav>site menu</nav><article class="ltx_document">
<h1 class="ltx_title">T</h1><script>steal()</script>
<section id="S2"><p onclick="x()" style="color:red">A bid <math alttext="b_{{t}}"><semantics><mi>b</mi>
<annotation encoding="application/x-tex">b_{{t}}</annotation></semantics></math> &amp; more.</p>
<a href="{URL}#S2">self</a> <a href="https://example.org/x">out</a> <a href="javascript:alert(1)">bad</a>
<img src="https://example.org/pixel.png"><br></section>
</article><footer>site footer</footer></body></html>"""

GUIDE = f"""---
paper: "arXiv:1234.56789v1"
title: A Paper
authors: [Ann Author]
---
## Chapter 0: needed, but not explained in the paper

| Concept | Needed for | How the paper treats it | Priority |
|---|---|---|---|
| Dominant strategy | unit 1 | One clause | Learn first |
| Proof-of-work | unit 1 | A footnote | Can wait |

## Units, in reading order

1. **The model** — section 2 ([link]({URL}#S2))
   Needs: nothing.
   Before you read: who decides?

## Later units (from headings only; not yet read by the agent)

2. **Results** — section 5 ([link]({URL}#S5))
    Needs: unit 1.
"""


def test_extract_article_keeps_content_and_drops_active_markup():
    out = build_reader.extract_article(PAGE, URL)
    assert 'id="S2"' in out and "A bid" in out and "&amp; more" in out
    assert '<math alttext="b_{t}">' in out and "<mi>b</mi>" in out
    for gone in ("steal", "onclick", "style=", "<img", "annotation", "site menu", "site footer", "javascript:"):
        assert gone not in out, gone


def test_extract_article_rewrites_links():
    out = build_reader.extract_article(PAGE, URL)
    assert '<a href="#S2">self</a>' in out
    assert '<a target="_blank" rel="noopener" href="https://example.org/x">out</a>' in out
    assert "<a>bad</a>" in out


def test_parse_guide_reads_units_and_prerequisites():
    guide = build_reader.parse_guide(GUIDE)
    assert guide["title"] == "A Paper" and guide["authors"] == ["Ann Author"]
    assert guide["prereqs"] == [
        {"concept": "Dominant strategy", "neededFor": "unit 1", "first": True},
        {"concept": "Proof-of-work", "neededFor": "unit 1", "first": False},
    ]
    first, second = guide["units"]
    assert first == {"n": 1, "title": "The model", "anchor": "S2", "needs": "nothing.",
                     "question": "who decides?", "provisional": False}
    assert second["provisional"] is True and second["anchor"] == "S5" and second["needs"] == "unit 1."


def test_build_rejects_a_guide_anchor_missing_from_the_paper():
    try:
        build_reader.build(PAGE, GUIDE, "__TITLE__ __GUIDE_JSON__ __ARTICLE__", URL)
    except SystemExit as exc:
        assert "[2]" in str(exc)
    else:
        raise AssertionError("expected SystemExit")


def test_build_fills_the_template_and_escapes_script_end_in_json():
    guide = GUIDE.replace("who decides?", "what does </script> do?").split("## Later units")[0]
    page = build_reader.build(PAGE, guide, "<title>__TITLE__</title><script>__GUIDE_JSON__</script>__ARTICLE__", URL)
    assert "<title>A Paper Reader</title>" in page
    assert "<\\/script> do?" in page and "what does </script>" not in page
