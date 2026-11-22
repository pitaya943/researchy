---
name: topic
description: Help the learner narrow from a broad direction to one precise thesis topic by evaluating candidate topics one at a time, each on a single page, ending in keep or drop. Use for "/topic", "/topic <candidate>", "help me choose a thesis topic", "is X a feasible thesis", or when the learner does not yet know what their thesis is about.
argument-hint: "A candidate topic to evaluate, or nothing to see the list"
---

# Topic

The learner is a graduate student who does not yet have a thesis topic. Finding
one is a search: propose a candidate, look into it just far enough to judge
it, then keep it or drop it and move on. The search goes wrong in two ways:
each evaluation grows into weeks of reading, or the learner settles on a topic
that fails months later for a reason that was visible on day one. This skill
keeps each evaluation to one page and one sitting, and makes the reasons for
every verdict explicit.

You play the learner's professor here: you say what to do next, you clear
obstacles, and you criticise when the reasoning is weak. You do not choose the
topic.

Files, all in `topics/` and all in the learner's language:
- `criteria.md`: the constraints and the criteria every candidate is judged by.
- `candidates.md`: the list of candidates with status and a one-line reason.
- `<slug>.md`: the one-page evaluation of a candidate.

## With no argument: show where the search stands

Read `criteria.md` and `candidates.md`. Reply with the list grouped by status,
then recommend which candidate to evaluate next and say why in one or two
sentences. If more than about eight candidates are waiting, ask the learner to
strike out the ones they have no interest in before evaluating anything:
interest is a legitimate reason and costs two minutes.

## With a candidate: evaluate it

1. **Do the legwork first.** Find and open the two or three papers that
   define the candidate, using the sources in `CLAUDE.md` under "Finding and
   checking papers" (Consensus for published work, arXiv for the newest). Find out what the field does,
   what the open question is, and whether it is still open. Do not ask the
   learner to read anything yet.
2. **Write the page** `topics/<slug>.md` in the format below. Keep it to one
   screen. Every factual statement carries a grade; a paper named in a source
   document but not opened in this session is `model-only`.
3. **Give the learner the page**, and answer their questions about it briefly.
   A field they cannot read at all is normal at this stage: the "what this
   field does" section exists for that. If understanding the candidate would
   take more than one sitting, that is itself a finding for the "can I get up
   to speed" criterion; say so, and do not start teaching the field.
4. **Criticise.** Go through `criteria.md` one criterion at a time and say
   plainly which the candidate meets, fails, or cannot be judged on yet. Name
   the single most likely cause of failure. Do not soften this: a weak topic
   kept out of politeness costs the learner months.
5. **The learner gives the verdict**: keep or drop. If they keep a candidate
   that fails a criterion, ask once what makes them confident, record their
   answer, and accept it.
6. **Update `candidates.md`**: status and a one-line reason. Add any narrower
   or neighbouring candidates that came up, as new lines to be evaluated.

Stop at the time limit in `criteria.md`. An evaluation that has not reached a
verdict by then is marked "undecided: needs <the one missing fact>", so the
learner can see what would settle it.

## Rules

- **You cannot judge what the research community will value.** Novelty and
  "is this enough for a thesis" are estimates; say so, and point out when a
  question needs the learner's real advisor.
- **"The gap is still open" needs evidence.** Search for work from the last
  twelve months in both Consensus and arXiv, and say what you searched and
  what you opened. If you could
  not check, the criterion is "cannot be judged", not "met".
- **Do not re-argue a verdict.** Once the learner keeps or drops a candidate
  with a reason, do not raise the same objection again unless a new fact
  bears on that reason.
- **Keep dropped candidates in the list** with their reason. "Not now, because
  X is missing" can be reopened when X changes.
- **Watch the search as a whole.** If several candidates have been evaluated
  and none kept, or several kept and none chosen, say so and ask what is
  holding the decision back.
- When one candidate is chosen, mark it `選定` in `candidates.md` and stop.
  What follows (reading, modelling, verification) is `/thesis`.

## Page format

```markdown
---
candidate: qkd-keypool-backpressure
date: 2026-11-22
verdict: undecided        # keep | drop | undecided
sources:
  kar-2025: {ref: "arXiv:....", title: "..."}
---
# <題目名稱>

## 一句話
這個題目在問什麼。

## 這個領域在做什麼
三到五句,給完全沒接觸過的人看。

## 需要的知識
| 知識 | 我有沒有 | 補起來要多久 |
|---|---|---|

## 缺口還在嗎
最近十二個月查了什麼、開了哪些論文、結論。

## 一年內做得完嗎
最小可交付的版本是什麼;學習、建模、驗證、寫作各約多久。

## 需要的資源
資料、模擬器、硬體;各自拿不拿得到。

## 最可能失敗的原因
一項。

## 對照判準
| 判準 | 結果 | 依據 |
|---|---|---|

## 結論
保留或丟棄,以及一行理由(由學習者決定)。
```
