# researchy

A toolkit of Claude Code skills that assists a graduate student through a
thesis: finding a topic, then reading, modelling, verifying and writing. It
assists; it does not do the thinking. The agent takes the labour (searching,
fetching, checking, recording) and the student writes the substance.

Every factual statement the agent records carries a grade that says how far it
was checked: `quote-verified`, `source-exists` or `model-only`.

The user guide is `plugin/skills/researchy/GUIDE.md` (in Traditional Chinese).

## Install

The toolkit is installed into `~/.claude/skills/` and used from your own
research project. Your topics, thesis and notes stay in your repository.

```bash
git clone https://github.com/pitaya943/researchy.git
```

```bash
mkdir -p ~/.claude/skills && cp -r researchy/plugin/skills/. ~/.claude/skills/
```

```bash
pip install pyyaml pytest sympy z3-solver
```

Paper search uses the Consensus and OpenAlex connectors and the arXiv API.
Without the connectors only arXiv is searched.

Then, in your project, run `/researchy`.

### Claude Code on the web

Use this as the environment's setup script, and allow the hosts `github.com`,
`arxiv.org` and `export.arxiv.org`:

```bash
#!/bin/bash
# Python packages used by the researchy scripts and checks.
pip install --quiet pyyaml pytest sympy z3-solver \
  || echo "researchy: Python packages were not installed"
# Install the researchy skills where Claude Code reads user-level skills.
rm -rf /tmp/researchy-src
git clone -q --depth 1 https://github.com/pitaya943/researchy.git /tmp/researchy-src \
  && mkdir -p "${HOME:-/root}/.claude/skills" \
  && cp -r /tmp/researchy-src/plugin/skills/. "${HOME:-/root}/.claude/skills/" \
  || echo "researchy skills were not installed"
```

## Skills

| Skill | Use |
|---|---|
| `/researchy` | Where am I, and which skill do I use next. |
| **Phase A: find a topic** | |
| `/researchy-topic [candidate]` | Evaluate candidate topics one page at a time; keep or drop. |
| `/researchy-brainstorm <idea>` | Explore far-fetched ideas and links between distant fields, without judging them yet. |
| `/researchy-map <field>` | Break a broad area into branches. |
| **Phase B: do the thesis** | |
| `/researchy-thesis` | Where the work stands and the one next step. |
| `/researchy-breakdown <need>` | Split what a step requires you to understand into small pieces; read one at a time. |
| `/researchy-gate [n]` | Check the current stage against the nine gates. |
| `/researchy-verify <claim>` | Run a check: counterexample search, assumption consistency, rerun a result, confirm a citation. |
| `/researchy-review <file>` | A review by an outside reviewer who has not seen the conversation. |
| `/researchy-calibrate <checker>` | Plant known defects in a copy of a document to see what a checker catches and misses. |
| **Also available** | |
| `/researchy-lesson`, `/researchy-read`, `/researchy-lookup` | Learn one concept; read a whole paper with a guide; recap from your notes. |

## Repository layout

| Path | Holds |
|---|---|
| `plugin/skills/researchy/` | The entry skill and what the skills share: conventions, the guide, the gate specification, templates, scripts |
| `plugin/skills/researchy-*/` | One skill each |
| `tests/` | Tests for the scripts and the plugin layout |

```bash
python3 -m pytest
```
