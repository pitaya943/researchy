---
name: read
description: Help the learner read a research paper in an order they can follow. Builds a reading guide that reorders the paper by what depends on what, lists what the paper assumes the reader already knows, and follows citations without losing the place. Use for "/read <arXiv ID or paper>", "help me read this paper", or when the learner follows a citation into another paper.
argument-hint: "An arXiv ID, or the sentence and citation you are following"
---

# Read

A paper is ordered to persuade experts, not to teach: the introduction uses
terms that are defined three sections later, and background the authors take
for granted is never explained. The learner's difficulty is mostly this
ordering, plus not knowing in advance which parts matter. So you do the
labour (fetch, cut into units, order them, locate passages) and the learner
does the reading, in the original text.

Do not ask the learner what question they want the paper to answer. Before
reading they usually cannot say; the questions come out of the reading.

## 1. Open the paper

1. `python3 scripts/arxiv.py get <id>` saves the paper under `papers/<id>/`
   (not in git). For a paper that is not on arXiv, ask the learner to put the
   file in `papers/`.
2. If `guides/<id>.md` exists, use it and go to step 3.

## 2. Build the reading guide

Write `guides/<id>.md`. Follow the layout of an existing guide in `guides/`.

1. **Read before you write.** Build a unit only from text you have read in
   this session. List the sections you read in full and the ones you know
   only by heading in `agent_read`, and keep the two visibly apart in the
   guide. A unit invented from a heading is a guess presented as structure.
2. **Cut into units.** A unit is one thing to understand: a definition, an
   assumption, a claim, a proof, an experiment. Give each its location
   (section, definition or theorem number, link).
3. **Find what each unit needs.** A need is either another unit, a concept
   with a card in `INDEX.md`, or a concept that is in neither.
4. **Chapter 0.** List every concept of the third kind: needed, and not
   explained in the paper. Say where it is first needed and how the paper
   treats it, and split "learn first" from "can wait". This is what stops the
   learner meeting a step they cannot yet do.
5. **Order the units** so that every unit comes after what it needs. Say
   where and why this differs from the paper's order.
6. **Give each unit a question** for the learner to answer before reading it.
   Ask; do not answer. Answering in the guide removes the reason to read.

The guide points at the paper. It never restates the paper's content, and it
never contains passages copied from it.

### The reader page (optional)

`python3 scripts/build_reader.py <id>` joins the paper and its guide into
`papers/<id>/reader.html`: the paper's text with a card before each unit, and
an Explain button on any selected passage. Publish it as a private artifact
with capabilities `{"sample": {}, "db": {}}`.

The page contains the paper's full text. Check the paper's licence first. If
it is not a Creative Commons licence, tell the learner that the page is a
private reading copy and must never be shared, and publish only if they agree.

What the learner asks on the page is saved in the artifact's `marks`
collection, and their answers to the unit questions in `guesses`. Read both
back with `ArtifactData` at the start of a reading session: the marks are the
places they did not follow.

## 3. Read with the learner

The learner reads one unit at a time in the original. For each unit: they
answer its question first, read, then say what was different from their guess.

When they do not follow something, record it under `## Marks` in the guide:
the location, their words, and what happened to it. A mark is handled like a
question in a lesson: answer a gap briefly and return; park a tangent in
`PARKED.md`. Any statement you add from your own knowledge is `model-only`.

### Following a citation

When the learner leaves the paper to follow a citation, keep a stack so they
can get back:

1. Push: write the sentence they came from and its location under `## Marks`.
   That sentence is the question; do not ask them to phrase one.
2. Open the cited paper (`arxiv.py get`). Find the passage that supports the
   sentence and show the learner where it is. Do not build a full guide for a
   paper opened only to follow one citation.
3. The learner reads that passage and writes one sentence: what the basis of
   the original statement turned out to be.
4. Pop: return to the recorded location in the first paper.

If no passage in the cited paper supports the sentence, say so plainly. That
is a finding about the first paper, and worth a mark.

At a depth of more than two papers, say that the reading has drifted and offer
to park the rest, exactly as a lesson does.

## 4. Close

1. Create a paper card `library/<id>.md` (format in `docs/library-format.md`,
   "Paper cards"). You fill in the assumptions and the open problems the
   authors state, each with its location; the learner writes
   `## In my own words`.
2. Concepts learned along the way get their own concept cards, linked from
   the paper card.
3. Run `python3 scripts/library.py check` and `index`.

## Grades

- A statement taken from text you read in this session: `source-exists: <key>`.
- A statement from your own knowledge: `model-only`.
- `quote-verified` is set only by the `check` skill.
