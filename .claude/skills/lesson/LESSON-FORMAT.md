# Lesson file format

`lessons/NNNN-<name>.md`, numbered in the order lessons were started.

```markdown
---
topic: Fermat's little theorem
scope: "State and use the theorem for prime moduli; not Euler's theorem, not RSA."
date: 2026-11-21
status: finished            # or: unfinished
cards: [fermat-little-theorem]
---
## Prediction
Question: What happens to the powers of a number when you reduce them mod a prime?
My guess: (the learner's guess, as written)

## Explanation
- [model-only] If p is prime and p does not divide a, then a^(p-1) ≡ 1 (mod p).
- [source-exists: hardy-wright] ...

## In my own words
(the learner's restatement, as written; copied unchanged to the card)

## Parked
- Why does the Fourier transform show up in number theory?
```

The lesson keeps the process: what was guessed, what was explained, what was
set aside. The card keeps the result. `status: unfinished` marks a lesson the
learner left on purpose to follow another topic.
