---
name: researchy
description: Show what the researchy toolkit does and which of its skills fits the learner's situation, and set a project up for it on first use. Use for "/researchy", "what can researchy do", "which skill should I use", "how do I start", or when a graduate student asks for help with a thesis and it is unclear where they are.
argument-hint: "Nothing, or a sentence about where you are in your research"
---

# researchy

researchy helps a graduate student get from "I do not know what my thesis is
about" to a finished draft. This skill is the front door: it works out where
the learner is and points at the one skill to use next. This folder also holds
what the other skills share.

SHARED below means this skill's own folder. Read `SHARED/CONVENTIONS.md`
before doing anything else.

## Steps

1. Look at the project: is there a `topics/` folder, a `thesis/status.md`?
2. If neither exists, this is a first use. Add `papers/` to `.gitignore`
   (create the file if needed), then ask the learner one question: do they
   already have a thesis topic?
3. Reply with where they are and the one skill to use next, from this table.
   Give the command and one sentence on what will happen. Do not list every
   skill unless they ask.

| Situation | Skill |
|---|---|
| No topic yet | `/researchy-topic` |
| An idea, unsure whether it can be a thesis | `/researchy-topic <idea>` |
| Wants to think freely, combine distant fields | `/researchy-brainstorm <idea>` |
| A field too broad to be a topic | `/researchy-map <field>` |
| Topic chosen, unsure what to do next | `/researchy-thesis` |
| Blocked because something is not understood | `/researchy-breakdown <what, and what for>` |
| A claim, theorem, result or citation to test | `/researchy-verify <claim>` |
| Thinks a stage of the thesis is finished | `/researchy-gate` |
| Wants an outside reviewer's reading | `/researchy-review <file>` |
| Wants to know whether a checker can be trusted | `/researchy-calibrate <checker>` |
| Learn one concept thoroughly; read one whole paper; recap notes | `/researchy-lesson`, `/researchy-read`, `/researchy-lookup` |

4. If they ask what the toolkit can and cannot do, answer from
   `SHARED/GUIDE.md`, briefly, and tell them that file is the full guide.

## What is in this folder

| File | Use |
|---|---|
| `CONVENTIONS.md` | Rules every skill follows |
| `GUIDE.md` | The user guide |
| `gates.md` | The nine gates a thesis passes, with required conditions |
| `criteria-template.md` | Starting point for a project's `topics/criteria.md` |
| `library-format.md` | Format of concept and paper cards |
| `SHARED/scripts/` | `arxiv.py`, `library.py`, `build_reader.py` |
