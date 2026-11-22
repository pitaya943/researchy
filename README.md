# researchy

A set of Claude Code skills that assist a graduate student through research:
learning a field, reading papers, finding and testing a problem, and doing the
work. It assists; it does not do the thinking. The agent takes the labour
(searching, fetching, ordering, checking, recording) and the learner does the
understanding, usually by answering before being told.

Every factual statement the agent records carries a grade that says how far it
was checked: `quote-verified`, `source-exists` or `model-only`.

## Skills

| Skill | Use |
|---|---|
| `/map <topic>` | Break a broad topic into branches small enough for one lesson. |
| `/lesson <topic>` | Learn one concept; ends with a card in your own words. Parks tangents. |
| `/read <arXiv ID>` | Read a paper with a guide ordered by what depends on what. |
| `/lookup <term>` | Recap something you learned before, from your own notes. |

## Layout

| Path | Holds |
|---|---|
| `library/` | Concept and paper cards (`docs/library-format.md`). `INDEX.md` is generated. |
| `lessons/` | One file per lesson: the guess, the explanation, what was parked. |
| `maps/` | Topic maps. |
| `guides/` | Reading guides for papers. |
| `papers/` | Downloaded papers. Not in git: most may be read but not redistributed. |
| `PARKED.md` | Questions set aside to learn later. |

## Scripts

```bash
python3 scripts/library.py check     # validate cards
python3 scripts/library.py index     # rebuild INDEX.md
python3 scripts/arxiv.py meta <id>   # confirm a paper exists; print its abstract
python3 scripts/arxiv.py get <id>    # download a paper to papers/<id>/
python3 -m pytest                    # run the tests
```
