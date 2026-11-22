---
name: map
description: Break a broad or vague topic into a short map of branches, each small enough for one lesson, grounded in sources opened in this session. Use for "/map <topic>", "what are the directions in X", "where do I start with X", or when a lesson topic is too large for one concept.
argument-hint: "A broad topic or research area"
---

# Map

A lesson teaches one concept. A request like "what are the research directions
in X" is not one concept: it is a request for the layout of a field. A map
gives that layout and nothing more, so the learner can choose where to start.
It is an outline of what could be learned, not a record of what has been
learned, so it never creates concept cards.

## Steps

1. Read `MISSION.md` if it exists, `INDEX.md`, and any existing file in
   `maps/` on the same topic (update it; do not make a second one).
2. If the purpose is unclear, ask one question: what the learner wants the map
   for (choosing a thesis topic, reading one paper, general orientation). The
   answer decides which branches matter. Do not ask more than one.
3. **Find anchor sources.** Search for two to four high-trust sources that
   themselves organise the field: a survey, the paper that defined the
   problem, lecture notes by a researcher in the area. Open each one. A field
   layout recalled from memory is where invented papers and wrong attributions
   come from, so the branches must be read off sources, not off memory.
4. **Draft four to eight branches.** For each branch write:
   - a name;
   - the question it studies, in one sentence a newcomer can read;
   - a grade label, with the source it was read from;
   - what the learner needs first (other branches, or outside concepts).
   Two levels deep at most. If a branch needs its own sub-branches, it gets its
   own map later.
5. **Suggest an order**: which branch to learn first and why, in two or three
   sentences. Mark which branches are needed for the learner's purpose and
   which are optional.
6. Write `maps/<name>.md` in the format below. Show the learner the map and
   let them pick a branch; that branch becomes the topic of a `/lesson`.

## Rules

- State the question each branch asks, not its answers. The answers belong to
  the lessons, where the learner predicts before being told.
- A branch read from an opened source is `source-exists: <key>`. A branch you
  added from your own knowledge is `model-only`; keep it, but say so.
- A paper counts as a source only if you opened it in this session. Give its
  identifier (arXiv ID or DOI) so it can be checked.
- A paper you saw only in search results, or could not open, goes under
  `## 未開啟的線索` with its identifier and title as the search showed them.
  A lead supports no grade: the branch it sits under stays `model-only`.
- If no source can be opened at all (network rules, paywall), say so at the
  top of the map and in your reply. Do not quietly fall back to memory.
- Keep the map to one screen. A map that takes a session to read has become a
  lesson.
- When a lesson on a branch finishes, tick the branch and add the lesson path.

## File format

`maps/<name>.md`:

```markdown
---
topic: Transaction fee mechanism design
purpose: "Orientation before choosing what to read first"
date: 2026-11-21
sources:
  roughgarden-2021: {ref: "arXiv:2106.01340", title: "Transaction Fee Mechanism Design"}
---
## 方向
- [ ] **誘因性質(incentive properties)** [source-exists: roughgarden-2021]
  問題:一個手續費機制能防住哪些參與者?
  需要:基本的拍賣理論。
  Lesson:(尚無)

## 建議順序
...

## 未開啟的線索
- arXiv:2111.03151 "Foundations of Transaction Fee Mechanism Design" (branch: Incentive properties)
```
