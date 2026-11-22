"""Tests for scripts/library.py. Each test builds a small library in tmp_path."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "plugin" / "skills" / "researchy" / "scripts"))

import library  # noqa: E402

FERMAT = """---
id: fermat-little-theorem
title: Fermat's little theorem
aliases: [費馬小定理]
topics: [number-theory, cryptography]
links:
  - {type: special-case-of, to: euler-theorem}
  - {type: prerequisite, to: modular-arithmetic}
sources:
  hardy-wright: {ref: "ISBN 978-0199219865"}
learned_in: [lessons/0003-fermat.md]
created: 2026-11-21
---
## Claims
- [source-exists: hardy-wright] If p is prime and p does not divide a, then a^(p-1) = 1 mod p.
- [model-only] It is the case n = p of Euler's theorem.

## In my own words
Powers repeat with period p-1 under a prime modulus.
"""

MODULAR = """---
id: modular-arithmetic
title: Modular arithmetic
aliases: [模運算]
topics: [number-theory]
created: 2026-11-20
---
## Claims
- [model-only] Integers a and b are congruent mod n when n divides a - b.
"""


def make(tmp_path, **cards):
    (tmp_path / "library").mkdir()
    for name, text in cards.items():
        (tmp_path / "library" / f"{name.replace('_', '-')}.md").write_text(text, encoding="utf-8")
    return library.load_library(tmp_path)


def test_valid_library_has_no_problems(tmp_path):
    cards = make(tmp_path, fermat_little_theorem=FERMAT, modular_arithmetic=MODULAR)
    assert library.check(cards) == []


def test_link_to_missing_card_is_frontier_not_error(tmp_path):
    cards = make(tmp_path, fermat_little_theorem=FERMAT, modular_arithmetic=MODULAR)
    assert library.frontier(cards) == {"euler-theorem": ["fermat-little-theorem"]}
    assert library.check(cards) == []


def test_claim_without_grade_is_rejected(tmp_path):
    bad = MODULAR.replace("- [model-only] Integers", "- Integers")
    problems = library.check(make(tmp_path, modular_arithmetic=bad))
    assert any("without a valid grade" in p for p in problems)


def test_graded_claim_must_cite_a_declared_source(tmp_path):
    bad = MODULAR.replace("[model-only]", "[quote-verified: nowhere]")
    problems = library.check(make(tmp_path, modular_arithmetic=bad))
    assert any("unknown source 'nowhere'" in p for p in problems)


def test_id_must_match_file_name(tmp_path):
    problems = library.check(make(tmp_path, renamed=MODULAR))
    assert any("does not match file name" in p for p in problems)


def test_duplicate_name_across_cards_is_rejected(tmp_path):
    clash = MODULAR.replace("aliases: [模運算]", "aliases: [費馬小定理]")
    cards = make(tmp_path, fermat_little_theorem=FERMAT, modular_arithmetic=clash)
    assert any("also used by" in p for p in library.check(cards))


def test_prerequisite_cycle_is_rejected(tmp_path):
    loop = MODULAR.replace(
        "created:", "links:\n  - {type: prerequisite, to: fermat-little-theorem}\ncreated:"
    )
    cards = make(tmp_path, fermat_little_theorem=FERMAT, modular_arithmetic=loop)
    assert any("prerequisite cycle" in p for p in library.check(cards))


def test_index_lists_topics_names_and_frontier_and_detects_staleness(tmp_path):
    make(tmp_path, fermat_little_theorem=FERMAT, modular_arithmetic=MODULAR)
    root = ["--root", str(tmp_path)]
    assert library.main(["index", "--check", *root]) == 1  # no INDEX.md yet
    assert library.main(["index", *root]) == 0
    text = (tmp_path / "INDEX.md").read_text(encoding="utf-8")
    assert "### cryptography" in text
    assert "- 費馬小定理: [Fermat's little theorem]" in text
    assert "- `euler-theorem` (from fermat-little-theorem)" in text
    assert library.main(["index", "--check", *root]) == 0
    (tmp_path / "library" / "modular-arithmetic.md").unlink()
    assert library.main(["index", "--check", *root]) == 1


def test_claims_under_the_chinese_heading_are_checked_too(tmp_path):
    bad = MODULAR.replace("## Claims", "## 主張").replace("- [model-only] Integers", "- Integers")
    problems = library.check(make(tmp_path, modular_arithmetic=bad))
    assert any("without a valid grade" in p for p in problems)
