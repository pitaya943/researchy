"""Tests for the parsing parts of scripts/arxiv.py (no network)."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "plugin" / "skills" / "researchy" / "scripts"))

import arxiv  # noqa: E402

ATOM = """<?xml version="1.0"?>
<feed xmlns="http://www.w3.org/2005/Atom">
  <entry>
    <id>http://arxiv.org/abs/2106.01340v3</id>
    <published>2021-06-02T17:48:32Z</published>
    <title>Transaction Fee
      Mechanism Design</title>
    <summary>  Demand for blockchains
      is larger than supply. </summary>
    <author><name>Tim Roughgarden</name></author>
  </entry>
  <entry>
    <id>http://arxiv.org/api/errors#incorrect_id_format_for_9999</id>
    <title>Error</title>
  </entry>
</feed>"""


def test_parse_meta_reads_fields_and_squashes_whitespace():
    assert arxiv.parse_meta(ATOM) == [{
        "id": "2106.01340v3",
        "title": "Transaction Fee Mechanism Design",
        "authors": ["Tim Roughgarden"],
        "year": "2021",
        "abstract": "Demand for blockchains is larger than supply.",
    }]


def test_parse_meta_drops_error_entries():
    assert len(arxiv.parse_meta(ATOM)) == 1


def test_html_to_text_keeps_latex_and_headings_and_drops_scripts():
    html = (
        "<nav>menu</nav><h2>2 Preliminaries</h2>"
        '<p>A bid <math alttext="b_{t}"><mi>b</mi><mi>t</mi></math> per unit size.</p>'
        "<script>alert(1)</script><p>Next.</p>"
    )
    text = arxiv.html_to_text(html)
    assert "## 2 Preliminaries" in text
    assert "A bid $b_{t}$ per unit size." in text
    assert "menu" not in text and "alert" not in text
    assert "bt" not in text  # rendered MathML children are not duplicated


def test_main_rejects_something_that_is_not_an_arxiv_id():
    try:
        arxiv.main(["get", "../../etc/passwd"])
    except SystemExit as exc:
        assert "not an arXiv ID" in str(exc)
    else:
        raise AssertionError("expected SystemExit")
