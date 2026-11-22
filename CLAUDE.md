# researchy (toolkit repository)

This repository is the researchy toolkit: Claude Code skills that assist a
graduate student through a thesis. It is installed into `~/.claude/skills/`
and used from the learner's own project; it is not where research is done.

## Layout

| Path | Holds |
|---|---|
| `plugin/skills/researchy/` | The entry skill and everything the skills share: `CONVENTIONS.md`, `GUIDE.md`, `gates.md`, templates, `scripts/` |
| `plugin/skills/researchy-*/` | One skill each |
| `tests/` | Tests for the scripts and for the layout of the plugin |

Install: copy `plugin/skills/.` into `~/.claude/skills/`. The README has the
commands and the cloud setup script.

## Rules for changing the toolkit

- **Skills must work from any project.** A skill may refer to its own folder,
  to SHARED (`~/.claude/skills/researchy/`) and to paths inside the learner's
  project. It must not refer to this repository's layout (`plugin/`, `tests/`).
  `tests/test_plugin.py` checks this.
- **Rules that hold for every skill go in `CONVENTIONS.md`**, not here: a
  learner's project never loads this file.
- **Keep `plugin/skills/researchy/GUIDE.md` current** whenever a skill is
  added, removed, renamed or changes what the learner does. It is written for
  the learner, in Traditional Chinese.
- **Keep the learner's overhead low.** Before adding a step the learner must
  perform, check that it removes more work than it adds.
- Run `python3 -m pytest` before committing.
- Skill instructions, code, commit messages and this file are in English.

## Working with the maintainer

- Reply in Traditional Chinese (繁體中文) only.
- Do not run rounds of decision questions or keep a decision log.
- Keep a short checklist in the reply for multi-step work.
