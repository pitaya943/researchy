---
name: lookup
description: Find something the learner studied before, by name, alias or a vague memory of it, and show how it connects to other concepts in the library. Use for "/lookup <term>", "what did I learn about X", or "I forgot X".
argument-hint: "A concept name, or whatever you remember about it"
---

# Lookup

The learner is trying to recover something they already learned. Your job is
to return *their* record of it, not a fresh explanation.

## Steps

1. Run `python3 scripts/library.py lookup "<query>"` from the repository root.
   The format of cards is in `docs/library-format.md`.
2. If nothing matches, try once more with a shorter or translated form of the
   query (an English term for a Chinese one, a keyword from a phrase).
3. **On a hit**, read the card and reply with, in this order:
   - the learner's own summary (`## In my own words`), quoted as written;
   - each claim with its grade label kept exactly as on the card;
   - the connections: outgoing links, incoming links, and any target marked
     "no card yet";
   - the lesson files in `learned_in`, so they can reread how they learned it.
4. **On a miss** (exit code 2, `NOT IN LIBRARY`), say plainly that the library
   has no card for it. Then offer two choices: start a lesson on it, or answer
   now from your own knowledge with every statement marked `model-only`.
   Wait for the choice.
5. Append one line to `learning-records/lookups.log`:
   `<ISO date>\t<query>\t<card id or MISS>`. A card looked up often is a card
   that was forgotten; recall practice reads this log to review it sooner.

## Rules

- Never fill a gap in a card from your own knowledge without the `model-only`
  label. A confident unlabelled sentence is the failure this system exists to
  prevent.
- Never raise a grade during a lookup. Only the `check` skill changes grades.
- Do not edit the card. If the learner spots an error, record it as a note for
  the next lesson on that concept.
- If several cards match, list them with their match score and ask which one.
