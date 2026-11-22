---
name: researchy-breakdown
description: Break something the learner needs to understand into small pieces, top-down from the reason they need it, then feed them one piece at a time and adjust from their feedback. Use for "/researchy-breakdown <thing>", "I don't understand X", "what do I need to know for X", or when a thesis step is blocked by missing knowledge.
argument-hint: "What you need to understand, and what for"
---

# Breakdown

Shared files for all researchy skills are in `~/.claude/skills/researchy/`
(if that folder is missing, use the `researchy/` folder beside this skill's own
folder). SHARED below means that folder; put the real path in any command.
Read `SHARED/CONVENTIONS.md` before doing anything else: it sets the language,
the file markers, how papers are found and graded, and how to work with the
learner.

The learner reads to get something done, not to finish a paper. So start from
the need and work down: what must be understood to do this, and what must be
understood for that, until each piece is small enough to read in one sitting.
Then the learner reads only those pieces.

The tree lives in `thesis/knowledge.md` (or `topics/<slug>-knowledge.md`
during topic search), in the learner's language.

## 1. Build the tree

1. State the need in one line: what the learner is trying to do, and why this
   knowledge is required for it. If you cannot say why, ask.
2. Split into sub-questions, top-down. Stop splitting a branch when a piece
   - can be read and understood in about thirty minutes, and
   - points at one specific place: a section of a paper, a textbook chapter,
     or a short explanation you can write.
3. Mark anything the learner already knows (ask if unsure; do not assume) and
   leave it out of the reading.
4. For each leaf, open the source before you point at it. A leaf that sends
   the learner to a passage you have not opened is a guess.
5. Order the leaves so that each comes after what it depends on.

Keep the tree small: at most three levels and about ten leaves. If it wants to
be bigger, the need is too broad; narrow it with the learner.

## 2. The loop

1. Give the learner the next one to three leaves. For each:
   - a short explanation first, five to ten lines, with a grade on each
     factual statement;
   - then where to read the original, if they want the full treatment.
2. The learner reads, then answers in one line. Any of these is enough:
   understood; stuck on something; this is not what I needed.
3. Update the tree from that answer:
   - understood: mark the leaf done, with their one line as the note;
   - stuck: split that leaf further, or add the missing piece before it;
   - not needed: remove the branch, and ask what the need really is.
4. Go to 1 until the need at the root is met. Then stop; do not keep teaching.

## Rules

- **The tree is your guess until the learner's feedback confirms it.** Expect
  to be wrong about what they know and what they need, and change it without
  defending it.
- **Do not require anything beyond the one-line answer.** No quizzes, no
  written summaries, no predictions. If the learner volunteers more, use it.
- **A side question** gets a short answer. If it is not needed for the root,
  add one line to `PARKED.md` and return to the tree.
- **Grades**: text you read in this session is `source-exists: <key>`; your
  own knowledge is `model-only`.

## File format

```markdown
# 需要:<一行,要做到什麼,為什麼需要這些知識>

- [x] **<子問題>**
  - [x] <葉子>:讀哪裡。筆記:<學習者的一句話>
  - [ ] <葉子>:讀哪裡。
- [ ] **<子問題>**
  - [ ] <葉子>:讀哪裡。

已經會的(略過):<清單>
```
