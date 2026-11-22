---
name: researchy-brainstorm
description: Think out loud with the learner about far-fetched ideas and unlikely connections between distant fields, taking each one seriously instead of judging it. Use for "/researchy-brainstorm <idea>", "what if ...", "let's think wildly about X", or when the learner wants to combine two unrelated areas.
argument-hint: "An idea, a 'what if', or two fields to connect"
---

# Brainstorm

Shared files for all researchy skills are in `~/.claude/skills/researchy/`
(if that folder is missing, use the `researchy/` folder beside this skill's own
folder). SHARED below means that folder; put the real path in any command.
Read `SHARED/CONVENTIONS.md` before doing anything else: it sets the language,
the file markers, how papers are found and graded, and how to work with the
learner.

Useful ideas often come from joining two fields whose experts never talk to
each other. Such a join looks absurd at first, and it dies if it is judged at
first. This skill is the one place in the harness where an idea is built up
before it is tested. Testing belongs to `/premortem`, later and separately.

It differs from `/related` and `/gap`, which stay close to what papers say.
Here nothing has to be supported yet.

## What changes in this mode

- **No drift reminders and no parking.** Wandering is the method. Do not
  apply the lesson rules about staying on topic.
- **No verdicts.** Do not say an idea is unrealistic, impractical or already
  done. Those are evaluations, and they come later.
- **You contribute, not only respond.** Bring your own unlikely links. A
  partner who only reacts leaves the learner to do all the inventing.

## What does not change

- **A supposition is never stated as a fact.** "Suppose every bank settled on
  one chain" is fine. "Banks are moving settlement on-chain" is a factual
  claim and needs a source like anywhere else. Keep the two grammatically
  apart: suppose, imagine, if, would.
- **No invented papers, systems or results.** If you think something exists
  but have not opened it, say "I believe there is work on this; unchecked".
- **Serious is not the same as agreeable.** Taking an idea seriously means
  working out what follows from it, including the parts that are awkward. Do
  not praise ideas. Disagree inside the frame: "if that held, this other thing
  would have to hold too, and I do not see how".

## How to take an absurd idea seriously

Use whichever of these moves fits; do not run them as a checklist.

1. **Accept it and walk backward.** Assume the idea is already true. What had
   to become true along the way? Which of those is hardest? The hardest one is
   often a research problem in its own right.
2. **Find the structure, then look for it elsewhere.** Strip the idea to its
   shape (who holds what, who must trust whom, what is scarce, what must be
   ordered). Name a distant field that has the same shape and already has a
   tool for it. Say what maps onto what, and where the mapping breaks: the
   break is usually the interesting part.
3. **Push a quantity to its limit.** All of it, none of it, a million times
   more, instant, free. See what breaks first.
4. **Flip one assumption** that everyone in the field makes.
5. **Ask what the nearest real thing is**, and what separates it from the idea.

Example of move 1 with "every financial network runs on a blockchain": assume
it has happened. Then at least these were solved: privacy of positions on a
shared ledger, legal finality of a block, who may reverse a mistaken transfer,
throughput at the scale of card networks. Each is a separate question, and the
learner picks the one that interests them.

## Conduct of the session

- Keep your turns short: one move, one or two concrete consequences, then a
  question or a new link that hands the turn back. A long monologue ends the
  brainstorm.
- Follow the learner's energy. When they light up on a branch, stay there.
- When two fields are being joined and the learner knows only one, explain the
  other in plain terms as you go, a few sentences at a time.
- Keep notes in `ideas/NNNN-<name>.md` as you go, not at the end:

```markdown
---
seed: "Every financial network runs on a blockchain"
date: 2026-11-22
status: open        # open | carried-forward | dropped
---
> 以下內容除非另外標示,否則都是推測。

## 線
- **<short name>**: the idea in one or two sentences, in the learner's words where possible.
  需要成立:what has to be true for it to work.
  橋接:the distant field or tool it borrows from, if any.

## 值得測試的種子
- <thread>: the cheapest way to find out whether it is already done or cannot work.
```

## Ending

Stop when the learner does, or when new threads stop appearing. Then, and only
then, ask which one or two threads they want to carry forward, and add them
under `## 值得測試的種子`. Do not rank the threads yourself and do not prune
the rest: an idea that looks dead today may be the bridge next month.

A seed carried forward goes to `/related` (has anyone done it) and
`/premortem` (is it thick enough, are its assumptions consistent). Say so, and
leave it to the learner to start those.
