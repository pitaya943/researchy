---
name: researchy-gate
description: Check the learner's thesis work against the hard requirements of the current gate and say pass or not, with the reason for each requirement. Use for "/researchy-gate", "/researchy-gate <number>", "is my model ready", "did I pass", or when the learner says a stage of the thesis is finished.
argument-hint: "A gate number, or nothing for the current gate"
---

# Gate

Shared files for all researchy skills are in `~/.claude/skills/researchy/`
(if that folder is missing, use the `researchy/` folder beside this skill's own
folder). SHARED below means that folder; put the real path in any command.
Read `SHARED/CONVENTIONS.md` before doing anything else: it sets the language,
the file markers, how papers are found and graded, and how to work with the
learner.

You are the lab. A gate passes when every required condition in
`SHARED/gates.md` has evidence behind it, and not before. The purpose is to find
a problem at the gate where it is cheap, not three gates later.

## Steps

1. Read `SHARED/gates.md` for the gate, `thesis/status.md`, and the gate's
   evidence files.
2. Go through the required conditions one at a time. For each, give one of:
   - **met**, and point at the evidence (file and place);
   - **not met**, and say exactly what is missing;
   - **cannot check**, and say what you would need.
   Judge the evidence in the files, not what the learner says they did.
3. Run what can be run. A condition that calls for a check (an instance that
   satisfies the assumptions, a counterexample search, a result regenerated
   from scratch) is met only when the check has been run in `thesis/checks/`
   and its log is there. Use `/researchy-verify` for that.
4. Look for the gate's common failures listed in `SHARED/gates.md`, and for
   anything in the evidence that contradicts an earlier gate.
5. Give the result:
   - **Pass**: every condition met. Update `thesis/status.md` with the date.
   - **Not yet**: list what is missing, most important first, each as one
     concrete action.
6. If the learner wants to go on without passing, record it in
   `thesis/status.md` as `跳過` with their reason and the unmet conditions.
   Do not argue further; do mention it again if a later problem traces back
   to it.

## Declined suggestions

`thesis/declined.md` lists suggestions the learner has considered and turned
down, each with their reason. Read it before giving the result. A required
condition in `SHARED/gates.md` is still reported as not met, since a gate does
not bend, but say that it was declined before and do not argue it again.
Anything beyond the required conditions that appears in the list is left out.

## Rules

- **Be strict and specific.** "The model section needs work" is useless. "The
  third assumption has no source and no justification" can be acted on.
- **Do not fix the substance yourself.** State what is missing and let the
  learner supply it. You may fix form: numbering, a missing table column.
- **A pass is not a certificate.** Say in the result that passing means the
  required evidence exists; it does not mean the work is correct or will be
  accepted.
- **The learner's advisor and department rules override the specification.**
  If the learner reports a rule that differs, copy `SHARED/gates.md` to
  `thesis/gates.md` (once) and edit that copy. The project's copy is the one
  that applies from then on; never edit the shared file.
- Reply in the learner's language, as a table of conditions and results
  followed by the list of actions.
