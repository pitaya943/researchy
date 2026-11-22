# Library format

The library is where learned concepts are kept so they can be found again.
It separates three things that serve different purposes:

| Thing | Path | Purpose |
|---|---|---|
| Concept card | `library/<id>.md` | The unit you come back to. One concept per file. |
| Lesson | `lessons/NNNN-<name>.md` | One teaching session. Creates or updates cards. |
| Learning record | `learning-records/` | Your recall-practice history. |
| Parked questions | `PARKED.md` | Tangents set aside during a lesson, to learn later. |

`INDEX.md` is generated from the cards by `SHARED/scripts/library.py index`.
Do not edit it by hand.

## Why the library is flat

A concept usually belongs to several topics. A Merkle tree is a data
structure, a cryptographic construction and a blockchain component. A folder
tree can file it under only one. So cards sit in one flat directory, each card
lists its own `topics`, and the by-topic view is derived.

## Concept card

```markdown
---
id: fermat-little-theorem          # stable address; equals the file name; never renamed
title: Fermat's little theorem     # display name; free to change
aliases: [費馬小定理, FLT]          # other names you might type, in any language
topics: [number-theory, cryptography]
links:
  - {type: special-case-of, to: euler-theorem}
  - {type: prerequisite, to: modular-arithmetic}
sources:
  hardy-wright: {ref: "ISBN 978-0199219865", locator: "ch. 6"}
learned_in: [lessons/0003-fermat-little-theorem.md]
created: 2026-11-21
---
## 主張
- [source-exists: hardy-wright] If p is prime and p does not divide a, then a^(p-1) ≡ 1 (mod p).
- [model-only] It is the case n = p of Euler's theorem.

## 用我自己的話
(Written by the learner, not the agent.)
```

Required fields: `id`, `title`, `topics`, `created`.

### Check grades

Every bullet under `## 主張` starts with a grade. A grade states only which
check was actually performed.

| Grade | Meaning | Needs a source key |
|---|---|---|
| `quote-verified: <key>` | The quoted text was found in the source. | yes |
| `source-exists: <key>` | The source resolves; its content was not compared. | yes |
| `model-only` | Nothing was checked. The model said so. | no |

None of these grades says that the source supports the claim. That judgement
stays with the learner. Filing a claim in the library never upgrades its grade.

### Link types

Types: `prerequisite`, `special-case-of`, `used-in`, `related`,
`contrasts-with`.

Only one direction is stored, so two cards cannot disagree. To see what points
at a card, search `library/` for `to: <id>`.

A link may point at a concept with no card yet. This is allowed: such targets
are listed in `INDEX.md` under "Frontier", the things you know exist but have
not learned.

## Paper cards

A paper read with `/researchy-read` gets a card too, in the same directory and format,
with `kind: paper` and an id such as `roughgarden-2021-tfm`. It adds two
sections that later feed gap-finding:

```markdown
## 假設
- [source-exists: self] Miners are myopic: they maximise revenue from the current block only. (section 3.2)

## 未解問題(作者自述)
- [source-exists: self] ... (section 6)
```

Each line gives the location in the paper. `self` is the paper itself, declared
under `sources` like any other source.

## Commands

```bash
python3 SHARED/scripts/library.py check            # validate every card
python3 SHARED/scripts/library.py index            # rebuild INDEX.md
python3 SHARED/scripts/library.py index --check    # fail if INDEX.md is stale
```

There is no search command. To find a card, read `INDEX.md` or use the
`/researchy-lookup` skill, which lets the agent search loosely.

`check` rejects: a missing required field, an `id` that differs from the file
name, an unknown link type, a claim without a grade, a graded claim citing an
undeclared source, one name used by two cards, and a cycle of `prerequisite`
links.
