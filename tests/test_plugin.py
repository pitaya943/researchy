"""Checks on the layout of the plugin, so it keeps working once installed elsewhere."""
import re
from pathlib import Path

import yaml

SKILLS = Path(__file__).resolve().parent.parent / "plugin" / "skills"
SHARED = SKILLS / "researchy"


def skill_files():
    return sorted(SKILLS.glob("*/SKILL.md"))


def frontmatter(path):
    return yaml.safe_load(re.match(r"^---\n(.*?)\n---\n", path.read_text(encoding="utf-8"), re.S).group(1))


def test_every_skill_is_named_after_its_folder_and_prefixed():
    assert len(skill_files()) >= 13
    for path in skill_files():
        meta = frontmatter(path)
        assert meta["name"] == path.parent.name, path
        assert meta["name"] == "researchy" or meta["name"].startswith("researchy-"), path
        assert len(meta["description"]) > 40, path


def test_every_other_skill_reads_the_shared_conventions_first():
    for path in skill_files():
        if path.parent.name != "researchy":
            assert "SHARED/CONVENTIONS.md" in path.read_text(encoding="utf-8"), path


def test_no_skill_text_depends_on_this_repository_layout():
    # Installed skills live under ~/.claude/skills; paths into this repo would not exist there.
    banned = re.compile(r"(?<![\w/])(docs/|tests/|plugin/|\.claude/skills/(?!researchy/))|(?<![\w/])scripts/")
    for path in sorted(SKILLS.rglob("*.md")):
        for number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
            cleaned = line.replace("SHARED/scripts/", "").replace("~/.claude/skills/researchy/", "")
            assert not banned.search(cleaned), f"{path.relative_to(SKILLS)}:{number}: {line.strip()}"


def test_shared_files_that_skills_name_exist():
    named = set()
    for path in sorted(SKILLS.rglob("*.md")):
        named.update(re.findall(r"SHARED/([\w./-]+\.(?:md|py))", path.read_text(encoding="utf-8")))
    assert named, "expected skills to reference shared files"
    missing = sorted(name for name in named if not (SHARED / name).exists())
    assert missing == []


def test_commands_named_in_skill_text_are_real_skills():
    real = {p.parent.name for p in skill_files()}
    for path in sorted(SKILLS.rglob("*.md")):
        for name in re.findall(r"(?<![\w./-])/(researchy(?:-[a-z]+)?)\b", path.read_text(encoding="utf-8")):
            assert name in real, f"{path.relative_to(SKILLS)} names /{name}"
