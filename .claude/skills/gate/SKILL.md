---
name: gate
description: Check the learner's thesis work against the hard requirements of the current gate and say pass or not, with the reason for each requirement. Use for "/gate", "/gate <number>", "is my model ready", "did I pass", or when the learner says a stage of the thesis is finished.
argument-hint: "A gate number, or nothing for the current gate"
---

# Gate

You are the lab. A gate passes when every required condition in
`docs/gates.md` has evidence behind it, and not before. The purpose is to find
a problem at the gate where it is cheap, not three gates later.

## Steps

1. Read `docs/gates.md` for the gate, `thesis/status.md`, and the gate's
   evidence files.
2. Go through the required conditions one at a time. For each, give one of:
   - **met**, and point at the evidence (file and place);
   - **not met**, and say exactly what is missing;
   - **cannot check**, and say what you would need.
   Judge the evidence in the files, not what the learner says they did.
3. Run what can be run. A condition that calls for a check (an instance that
   satisfies the assumptions, a counterexample search, a result regenerated
   from scratch) is met only when the check has been run in `thesis/checks/`
   and its log is there. Use `/verify` for that.
4. Look for the gate's common failures listed in `docs/gates.md`, and for
   anything in the evidence that contradicts an earlier gate.
5. Give the result:
   - **Pass**: every condition met. Update `thesis/status.md` with the date.
   - **Not yet**: list what is missing, most important first, each as one
     concrete action.
6. If the learner wants to go on without passing, record it in
   `thesis/status.md` as `跳過` with their reason and the unmet conditions.
   Do not argue further; do mention it again if a later problem traces back
   to it.

## Rules

- **Be strict and specific.** "The model section needs work" is useless. "The
  third assumption has no source and no justification" can be acted on.
- **Do not fix the substance yourself.** State what is missing and let the
  learner supply it. You may fix form: numbering, a missing table column.
- **A pass is not a certificate.** Say in the result that passing means the
  required evidence exists; it does not mean the work is correct or will be
  accepted.
- **The learner's advisor and department rules override this file.** If the
  learner reports a rule that differs, edit `docs/gates.md` to match.
- Reply in the learner's language, as a table of conditions and results
  followed by the list of actions.
