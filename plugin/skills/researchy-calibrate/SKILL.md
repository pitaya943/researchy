---
name: researchy-calibrate
description: Measure whether a checker actually catches errors, by planting known defects in a copy of a document and seeing which ones the checker finds and what it flags on a clean copy. Use for "/researchy-calibrate review", "/researchy-calibrate gate", "/researchy-calibrate verify", "can I trust the review", "does the check actually work", and before the learner starts relying on a checker for a new kind of document.
argument-hint: "Which checker (review, gate or verify), and optionally the file to test it on"
---

# Calibrate

Shared files for all researchy skills are in `~/.claude/skills/researchy/`
(if that folder is missing, use the `researchy/` folder beside this skill's own
folder). SHARED below means that folder; put the real path in any command.
Read `SHARED/CONVENTIONS.md` before doing anything else: it sets the language,
the file markers, how papers are found and graded, and how to work with the
learner.

A check that has never been seen to fail tells you nothing when it passes.
Before the learner relies on `/researchy-review`, `/researchy-gate` or `/researchy-verify`, find out what
each one catches and what it misses, by giving it documents whose defects you
already know.

Results go to `thesis/calibration/LEDGER.md` (or `topics/calibration/` before
a thesis exists), in the learner's language.

## Steps

1. **Choose the document.** Use the file the learner names, or the most
   recent file of the kind the checker works on. If the learner has nothing
   yet, use `fixture/clean.md` in this skill's own folder, with the seeds in
   `fixture/seeds.json`.
2. **Make the copies in a scratch directory**, never in `thesis/`:
   - one **control**, unchanged;
   - one copy per **seeded defect**, each with exactly one defect.
   Give the files neutral names (`doc-a.md`, `doc-b.md`, ...) in an order that
   does not reveal which is the control.
3. **Choose the defects** to match what the checker is supposed to catch. Use
   three to five, of different kinds. Write each down before running anything:
   what was changed, and what a correct report would say.

   | Checker | Defects to plant |
   |---|---|
   | review | a conclusion larger than the evidence; a number that contradicts a table or formula; a condition dropped from a theorem; a comparison with the direction reversed; a citation that does not say what is claimed |
   | gate | one required element removed (an assumption without a source, a claim with no falsifying observation, a result with no seed recorded) |
   | verify | a false variant of a true statement with a known small counterexample; a set of assumptions with one contradictory assumption added |

   Make each defect the kind a real author makes by accident. A defect that no
   one would write tests nothing.
4. **Run the checker on each copy in a fresh context**: one subagent per copy,
   given only the checker's instructions and that one file. It must not see
   the seed list, the other copies, or this conversation. Do not hint that the
   file may contain a planted defect.
5. **Score** from the reports:
   - **caught**: the report names the planted defect, at its location;
   - **missed**: it does not;
   - **false alarm**: on the control, anything reported as a serious problem.
     Minor remarks on the control are not false alarms; list them anyway.
   When a report is vague about whether it found the defect, count it as
   missed.
6. **Append to the ledger**: date, checker, document, each defect with caught
   or missed, false alarms on the control, and one line on what kind of error
   this checker cannot be trusted to find.
7. **Delete the scratch copies.** Confirm that nothing under `thesis/` or
   `topics/` was changed.

## Rules

- **Report the misses first.** They are the useful result.
- **A few seeds give a rough picture, not a rate.** With three to five defects
  say "caught 2 of 3", never a percentage.
- **A good score does not transfer.** It covers this checker, on this kind of
  document, for these kinds of defect. Say so in the ledger.
- **Never plant a defect in the learner's real files**, and never leave a
  seeded copy where it could be mistaken for the real one.
- If a checker misses a kind of defect, say what to do about it: check that
  kind by hand, add an explicit instruction to the checker's skill, or run
  `/researchy-verify` on those claims.
- Calibrate again after a checker's skill file changes.
- **Say what it will cost before running.** Each copy is a separate subagent;
  the first run used about 85,000 tokens per copy. Tell the learner the number
  of copies and let them decide.
- **Check how the checker ranks what it finds**, not only whether it finds it.
  In the first run the reviewer caught a dropped condition but ranked it below
  routine remarks. Record in the ledger whether each caught defect was treated
  as serious.

## Ledger format

```markdown
## 2026-11-22 · review · fixture/clean.md

| 植入的缺陷 | 結果 | 報告怎麼說 |
|---|---|---|
| 結論超出證據 | 抓到 | ... |
| 數字與公式矛盾 | 漏掉 | ... |

對照組的誤報:無。
這個檢查器目前不能依賴它找出:...
範圍:只代表這一類文件與這幾種缺陷。
```
