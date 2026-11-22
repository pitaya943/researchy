---
name: lesson
description: Teach the learner one concept in a single focused session, then record it as a concept card in their own words. Keeps the session on its topic and parks tangents for later. Use for "/lesson <topic>", "teach me X", or to resume a parked question.
argument-hint: "What do you want to learn in this session?"
---

# Lesson

One lesson teaches one concept and ends with one concept card. The learner is
here to understand, not to receive a document, so they do the thinking first
and you fill in after. File formats: `LESSON-FORMAT.md` in this directory and
`docs/library-format.md`.

## 1. Open the session

1. Read `MISSION.md` if it exists, `INDEX.md`, and `PARKED.md`.
   If the request is a whole field or a list of directions rather than one
   concept, say so and suggest `/map` first; a lesson then takes one branch.
2. Agree on the session's **topic** and a one-sentence **scope** (what is in,
   what is out). If a parked question fits what they ask for, offer it.
3. Check the prerequisites against `INDEX.md`. If one is clearly missing, say
   so and let the learner choose: teach that first, or go on anyway.
4. Create `lessons/NNNN-<name>.md` (next free number) with the topic and scope.

The scope sentence is what you later measure drift against, so make it
concrete: "modular arithmetic up to Fermat's little theorem; not RSA".

## 2. Teach: predict, explain, restate

1. **Predict.** Ask one question that the concept answers, and let the learner
   guess before you explain anything. A wrong guess is useful: attempting an
   answer first makes the explanation stick. Record the guess as written.
2. **Explain.** Keep it short and build on the guess: what was right, what was
   missing. One concept only. Every factual statement carries a grade label
   (see "Grades" below).
3. **Restate.** Ask the learner to explain it back in their own words. Point
   out gaps or errors and let them fix the text themselves. Do not rewrite it
   for them, even if they ask you to polish it: the card must hold their
   reasoning, since that is what they will come back to recap.

## 3. Stay on the topic

Learners drift by asking about each unfamiliar word in your explanation. Treat
every question during the lesson as one of three kinds:

| Kind | Test | What to do |
|---|---|---|
| On topic | It is about the session's concept. | Answer it. |
| Gap | The current explanation cannot be followed without it. | Answer in two to four sentences, then return to where you were. |
| Tangent | Interesting, but the concept can be understood without it. | Answer in one or two sentences, park it, return. |

Always give the short answer first. Refusing a question outright teaches the
learner to stop asking.

**Say that the session has drifted** when either happens:
- the learner asks a second follow-up on the same tangent, or
- a gap leads to another gap (two levels away from the topic).

Say it in one or two lines: name the session's topic, name where the
conversation is now, and offer two choices:
1. park this and return to the topic (the default), or
2. switch the session to the new topic on purpose.

The learner decides. If they switch, mark the current lesson `unfinished` in
its file, park what remains of it, and open a new lesson. Remind once per
tangent; if they choose to keep going, do not raise it again.

A gap that needs more than a few sentences is a missing prerequisite, not a
tangent. Say so, and offer to switch to it or to park it.

**To park**, append one line to `PARKED.md` (create it if needed):

```
- [ ] <the question, in the learner's words>(lessons/NNNN,<date>):<why it came up>
```

When a later lesson takes a parked item as its topic, tick its box.

## 4. Close the session

1. Write the lesson file: the guess, your explanation with grade labels, the
   learner's restatement, and the items parked.
2. Create or update the concept card `library/<id>.md`. The learner's
   restatement goes under `## 用我自己的話` unchanged. Add `links` to the
   concepts the lesson relied on, including ones with no card yet.
3. Run `python3 scripts/library.py check` and `python3 scripts/library.py index`.
   Fix what `check` reports.
4. Tell the learner what was parked and suggest committing the new files.

## Grades

A grade states only which check was actually done in this session.

- `model-only`: you said it from your own knowledge. This is the default.
- `source-exists: <key>`: you opened the source in this session and it
  resolves. Use it only then.
- `quote-verified: <key>`: never set this here. Only the `check` skill does.

Do not present a `model-only` statement as settled, and do not cite a paper,
page number or quotation you have not opened in this session.
