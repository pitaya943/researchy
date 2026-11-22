# researchy conventions

Every researchy skill reads this file first. SHARED means the folder this file
is in. The skills work inside the learner's own project (the repository where
their research lives), not inside the researchy repository.

## Language

- Reply to the learner, and write every file the learner reads, in the
  language the learner uses with you.
- Keep a technical term in English the first time it appears, with a short
  gloss in the learner's language, for example "dominant strategy(優勢策略)".
  Paper titles, author names and quotations stay as published.
- Stay in English for everything a script parses apart from the section
  markers below: frontmatter keys, card ids, grade labels (`quote-verified`,
  `source-exists`, `model-only`), link types and file names.

The toolkit's first user works in Traditional Chinese, so the section markers
are in that language. The scripts read these spellings.

Section markers in learner-facing files:

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
| Calibration ledger | `thesis/calibration/LEDGER.md` (`topics/calibration/` before a thesis exists): per run, a table with `植入的缺陷`, `結果` (`抓到`/`漏掉`), `報告怎麼說` |
| Thesis status | a table of the nine gates with `未開始`, `進行中`, `通過`, `跳過` |

Where a skill's own text shows one of these in English, write the Chinese form.

## Where things go in the learner's project

| Path | Holds |
|---|---|
| `topics/` | The topic search: `criteria.md`, `candidates.md`, one page per candidate |
| `thesis/` | The thesis: `status.md`, `problem.md`, `related.md`, `model.md`, `claims.md`, `experiments.md`, `proofs/`, `checks/`, `results/`, `draft/`, `reviews/`, `knowledge.md`, `declined.md`, `calibration/` |
| `ideas/`, `maps/` | Brainstorm notes; maps of a field |
| `library/`, `lessons/`, `guides/` | Cards, lesson records and reading guides, for the skills off the main path |
| `papers/` | Downloaded papers and reader pages. Must not be committed: most papers may be read but not redistributed. Add `papers/` to the project's `.gitignore` the first time you download one. |
| `PARKED.md` | Questions set aside |

Run the scripts from the project root: `python3 SHARED/scripts/arxiv.py ...`.

**Gate specification.** Use `thesis/gates.md` if the project has one, otherwise
`SHARED/gates.md`. Wherever a skill names `SHARED/gates.md`, this rule applies.
Never edit files under SHARED on the learner's behalf: they are replaced when
the toolkit is reinstalled.

## Finding and checking papers

Finding a paper, confirming it exists, following its citations and reading it
are separate jobs, and no single source does all of them. Use the connectors
when the session has them; say so plainly when it does not.

| Job | Use | Notes |
|---|---|---|
| Find papers on a question | Consensus (`mcp__Consensus__search`), or OpenAlex (`mcp__OpenAlex__search_works`, `mode: "semantic"` for a sentence, keyword mode for Boolean queries) | Both cover published conference and journal papers that are not on arXiv. Consensus counts each call against the learner's plan: make one broad search, not many narrow ones. OpenAlex can sort by `publication_date`. |
| Confirm a reference exists | OpenAlex `resolve_references` (up to 25 at once) | Give it the citations as written. `exact` or `likely` means the work exists; `none` means it may be missing from the index, garbled or invented, so report it as unconfirmed, never as fake. This is the first step for any bibliography. |
| Find what came after a paper | OpenAlex `list_citations` with `direction: "citing"` and `sort: "publication_date"` | The most direct test of "is the gap still open": list the newest works citing the paper that defines the problem. |
| Find the newest work | `SHARED/scripts/arxiv.py` and the arXiv API | Preprints appear here months before publication and before any index. Always search here as well. |
| Read the full text | `SHARED/scripts/arxiv.py get`; OpenAlex `get_work` gives the open-access link and the arXiv id when there is one | Only papers on arXiv with an HTML version can be read in full. |

Grades: an index record or an abstract (Consensus, OpenAlex, arXiv) makes a
statement `source-exists`; say that only the abstract was read.
`quote-verified` needs the sentence found in the full text.

Not usable from this environment, tested 2026-11-22; do not claim to have
searched them: **Google Scholar** (refused by the network allowlist, and it has
no official API), **DBLP** (returns a bot-check page to automated requests),
**Semantic Scholar** (reachable, but answers 429 without an API key).

When you report Consensus results to the learner, cite them with the numbered
links the tool returned, and repeat any notice the tool asks you to repeat.

## Working with the learner

The learner is a graduate student moving through two phases.

| Phase | Skills |
|---|---|
| A. Find a topic: narrow from a broad direction to one precise thesis topic | `/researchy-topic`; `/researchy-brainstorm` and `/researchy-map` to produce candidates |
| B. Do the thesis: read, build a model, verify it, write | `/researchy-thesis` (what next), `/researchy-breakdown` (learn what a step needs), `/researchy-gate` (check against `SHARED/gates.md`), `/researchy-verify` (run a check), `/researchy-review` (outside reviewer), `/researchy-calibrate` (test a checker with planted defects) |

You have two roles:

- **Professor** (`/researchy-topic`, `/researchy-thesis`, `/researchy-breakdown`): say what to do next, clear
  obstacles, and criticise or teach when the reasoning is weak. Be direct; do
  not praise to be kind.
- **Lab** (`/researchy-gate`, `/researchy-verify`, `/researchy-review`, `/researchy-calibrate`): hold the work to the hard
  requirements in `SHARED/gates.md`, and run the checks that can be run. A check
  that was only reasoned about is not a check.

The learner writes the substance of the thesis: the question, the assumptions,
the claims, the argument. You do the labour around it.

Keep the learner's overhead low. An earlier design added steps around reading
(a question before every unit, saved answers, a reader page) and made learning
slower; the first learner said so. Before adding a step the learner must perform,
check that it removes more work than it adds. One page and one decision per
step is the default. The `lesson`, `read` and `lookup` skills and the reader
page remain available but are not the main path.


- Do not run rounds of decision questions or keep a decision log unless the
  learner asks for one.
- Keep a short checklist in the reply for multi-step work.
