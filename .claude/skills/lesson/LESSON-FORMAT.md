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
## 預測
問題:把一個數的各次方對質數取模,會發生什麼事?
我的猜測:(the learner's guess, as written)

## 講解
- [model-only] If p is prime and p does not divide a, then a^(p-1) ≡ 1 (mod p).
- [source-exists: hardy-wright] ...

## 用我自己的話
(the learner's restatement, as written; copied unchanged to the card)

## 擱置
- 為什麼 Fourier transform 會出現在數論裡?
```

Write the content in the learner's language (see `CLAUDE.md`). The lesson keeps the process: what was guessed, what was explained, what was
set aside. The card keeps the result. `status: unfinished` marks a lesson the
learner left on purpose to follow another topic.
