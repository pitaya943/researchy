---
name: verify
description: Test one claim by actually running a check, such as searching for a counterexample to a mathematical statement, checking that a set of assumptions is consistent, regenerating an empirical result from scratch, or confirming that a cited paper says what the learner says it says. Use for "/verify <claim>", "is this theorem true", "check my assumptions", "can you reproduce this number", "does this paper really say that".
argument-hint: "The claim to test"
---

# Verify

You are the lab bench. A claim is tested by running something and recording
what happened. Reasoning about whether a claim "looks right" is not a check.

Every check leaves two files in `thesis/checks/`: the script
(`NNNN-<name>.py`) and its log (`NNNN-<name>.log`), so anyone can rerun it.
During topic search, use `topics/checks/` instead.

## Pick the kind of check

**A mathematical statement** (theorem, lemma, inequality, optimality claim)
1. Restate it precisely with the learner: quantifiers, domain, conditions.
   Many false claims fail here.
2. Search small instances exhaustively or at random for a counterexample.
   Include the edge cases: zero, one participant, equal values, the extremes
   of each parameter.
3. Where it helps, check algebra symbolically (`sympy`) or pose the negation
   to a solver (`z3`).
4. For each condition of the statement, drop it and search again. A condition
   whose removal yields no counterexample may be unnecessary; say so.

**A set of assumptions**
1. Try to construct one concrete instance that satisfies all of them, and
   check it by code.
2. If none is found, look for a pair that conflicts, and report it.

**An empirical result**
1. Rerun from raw data with the recorded commit, configuration and seed, in a
   clean state.
2. Compare the regenerated number with the reported one. Report the
   difference; do not round it away.
3. Rerun with other seeds if only one was used.

**A citation** ("paper X shows Y")
1. Open the paper (`scripts/arxiv.py get`).
2. Find the passage. If it supports the statement, quote the sentence and its
   location, and the grade becomes `quote-verified`. If the paper exists but
   you cannot find support, the grade stays `source-exists` and you say that
   the paper does not appear to say this.

## Report

State, in this order: the claim as tested; what was run; the space that was
searched or the data that was used; the outcome; what the outcome does and
does not establish.

## Rules

- **"No counterexample found" is not a proof.** Always say so, together with
  the size of the space searched. A check can refute a claim; it can only
  fail to refute it.
- **A counterexample is checked twice** before you report it: confirm by
  independent code or by hand that it satisfies every condition and violates
  the conclusion.
- **Report results that go against the learner's claim as plainly as those
  that support it.** Do not adjust the claim to fit; show the learner and let
  them decide whether to change the claim or the model.
- **Do not present your own derivation as verification.** If you only
  reasoned about it, label it `model-only`.
- Install what the check needs (`pip install sympy z3-solver`), and keep each
  script short and readable; the learner should be able to follow it.
