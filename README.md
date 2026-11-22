# researchy

A set of Claude Code skills that assist a graduate student through research:
learning a field, reading papers, finding and testing a problem, and doing the
work. It assists; it does not do the thinking. The agent takes the labour
(searching, fetching, ordering, checking, recording) and the learner does the
understanding, usually by answering before being told.

Every factual statement the agent records carries a grade that says how far it
was checked: `quote-verified`, `source-exists` or `model-only`.

Design and the learning flow are described in `docs/overview.md`.

## Skills

| Skill | Use |
|---|---|
| **Phase A: find a topic** | |
| `/topic [candidate]` | Evaluate candidate topics one page at a time; keep or drop. |
| `/brainstorm <idea>` | Explore far-fetched ideas and links between distant fields, without judging them yet. |
| `/map <topic>` | Break a broad area into branches. |
| **Phase B: do the thesis** | |
| `/thesis` | Where the work stands and the one next step. |
| `/breakdown <need>` | Split what a step requires you to understand into small pieces; read one at a time. |
| `/gate [n]` | Check the current stage against the hard requirements in `docs/gates.md`. |
| `/verify <claim>` | Run a check: counterexample search, assumption consistency, rerun a result, confirm a citation. |
| `/review <file>` | A review by an outside reviewer who has not seen the conversation. |
| **Also available** | |
| `/lesson`, `/read`, `/lookup` | Learn one concept; read a whole paper with a guide; recap from your notes. |

## Layout

| Path | Holds |
|---|---|
| `library/` | Concept and paper cards (`docs/library-format.md`). `INDEX.md` is generated. |
| `lessons/` | One file per lesson: the guess, the explanation, what was parked. |
| `maps/` | Topic maps. |
| `thesis/` | The thesis: status of the nine gates, problem, model, claims, checks, results, draft, reviews. |
| `topics/` | The topic search: criteria, the candidate list, one page per evaluated candidate. |
| `guides/` | Reading guides for papers. |
| `ideas/` | Notes from brainstorms. Speculation unless marked otherwise. |
| `papers/` | Downloaded papers. Not in git: most may be read but not redistributed. |
| `PARKED.md` | Questions set aside to learn later. |

## Scripts

```bash
python3 scripts/library.py check     # validate cards
python3 scripts/library.py index     # rebuild INDEX.md
python3 scripts/arxiv.py meta <id>   # confirm a paper exists; print its abstract
python3 scripts/arxiv.py get <id>    # download a paper to papers/<id>/
python3 scripts/build_reader.py <id> # build the highlight-to-explain page for a paper
python3 -m pytest                    # run the tests
```
