# researchy

Skills that assist a graduate student through research. User guide:
`docs/guide.md`; keep it current whenever a skill is added, removed or changes
what the learner does. Card format: `docs/library-format.md`.

## Language

The learner reads Traditional Chinese faster than English.

- **Reply to the learner in Traditional Chinese (繁體中文) only.**
- **Everything the learner reads is written in Traditional Chinese**: maps,
  reading guides, lesson files, concept and paper cards, `PARKED.md`,
  brainstorm notes, reports under `docs/` written for them.
- Keep a technical term in English the first time it appears, with a short
  Chinese gloss, for example "dominant strategy(優勢策略)". After that either
  form is fine. Paper titles, author names and quotations stay as published.
- **Stay in English**: skill instructions, code and comments, commit messages,
  the README, and everything a script parses apart from the section markers
  below. That means frontmatter keys, card ids, grade labels
  (`quote-verified`, `source-exists`, `model-only`), link types and file names.

Section markers in learner-facing files (the scripts read these spellings):

| File | Markers |
|---|---|
| Card | `## 主張`, `## 用我自己的話`; paper cards add `## 假設`, `## 未解問題(作者自述)` |
| Lesson | `## 預測` (`問題:`, `我的猜測:`), `## 講解`, `## 用我自己的話`, `## 擱置` |
| Map | `## 方向` (`問題:`, `需要:`, `Lesson:`), `## 建議順序`, `## 各方向的論文`, `## 未開啟的線索` |
| Guide | `## 第 0 章`, `## 單元(依閱讀順序)` (`需要:`, `讀之前:`), `## 後續單元`, `## 標記` |
| Brainstorm | `## 線` (`需要成立:`, `橋接:`), `## 值得測試的種子` |
| Topic page | `## 一句話`, `## 這個領域在做什麼`, `## 需要的知識`, `## 缺口還在嗎`, `## 一年內做得完嗎`, `## 需要的資源`, `## 最可能失敗的原因`, `## 對照判準`, `## 結論` |
| Knowledge tree | `# 需要:` then a checklist of sub-questions and leaves; `筆記:` holds the learner's one line; `已經會的(略過):` |
| Declined list | `thesis/declined.md`: a table with `日期`, `建議`, `來源`, `我的理由`, `什麼情況下重新考慮` |
| Calibration ledger | `thesis/calibration/LEDGER.md`: per run, a table with `植入的缺陷`, `結果` (`抓到`/`漏掉`), `報告怎麼說` |
| Thesis status | a table of the nine gates with `未開始`, `進行中`, `通過`, `跳過` |

Where a skill's own text shows one of these in English, write the Chinese form.

## Finding and checking papers

Finding a paper, confirming it exists, and reading it are three jobs, and no
single source does all three.

| Job | Use | Notes |
|---|---|---|
| Find papers on a question | The Consensus connector (`mcp__Consensus__search`) when the session has it | Semantic search over peer-reviewed work, including conference and journal papers that are not on arXiv. Ranked by relevance, not date: pass `year_min` when checking whether a gap is still open. Each call counts against the learner's plan, so make one broad search, not many narrow ones. |
| Find the newest work | `scripts/arxiv.py` and the arXiv API | Preprints appear here months before publication. Always search here as well when the question is "has someone done this in the last year". |
| Read the full text | `scripts/arxiv.py get` | Only for papers on arXiv with an HTML version. |

Grades: a Consensus record or an arXiv abstract makes a statement
`source-exists`, and say that only the abstract was read. `quote-verified`
needs the sentence found in the full text. Google Scholar cannot be
reached from this environment (tested 2026-11-22: refused by the network
allowlist), and it offers no official API for automated use; do not claim to
have searched it.

When you report Consensus results to the learner, cite them with the numbered
links the tool returned, and repeat any notice the tool asks you to repeat.

## Working with the learner

The learner is a graduate student moving through two phases.

| Phase | Skills |
|---|---|
| A. Find a topic: narrow from a broad direction to one precise thesis topic | `/topic`; `/brainstorm` and `/map` to produce candidates |
| B. Do the thesis: read, build a model, verify it, write | `/thesis` (what next), `/breakdown` (learn what a step needs), `/gate` (check against `docs/gates.md`), `/verify` (run a check), `/review` (outside reviewer), `/calibrate` (test a checker with planted defects) |

You have two roles:

- **Professor** (`/topic`, `/thesis`, `/breakdown`): say what to do next, clear
  obstacles, and criticise or teach when the reasoning is weak. Be direct; do
  not praise to be kind.
- **Lab** (`/gate`, `/verify`, `/review`, `/calibrate`): hold the work to the hard
  requirements in `docs/gates.md`, and run the checks that can be run. A check
  that was only reasoned about is not a check.

The learner writes the substance of the thesis: the question, the assumptions,
the claims, the argument. You do the labour around it.

Keep the learner's overhead low. An earlier design added steps around reading
(a question before every unit, saved answers, a reader page) and made learning
slower; the learner said so. Before adding a step the learner must perform,
check that it removes more work than it adds. One page and one decision per
step is the default. The `lesson`, `read` and `lookup` skills and the reader
page remain available but are not the main path.


- Do not run rounds of decision questions or keep a decision log in this
  project; the learner asked for that to stop.
- Keep a short checklist in the reply for multi-step work.
