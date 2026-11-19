"""Sanity check for the skill pack. Run from the repo root: python scripts/check_skills.py"""
import json, pathlib, re, sys

root = pathlib.Path(__file__).resolve().parent.parent
bad = []
json.loads((root / ".claude-plugin" / "plugin.json").read_text(encoding="utf-8"))
for f in sorted((root / "skills").glob("*/SKILL.md")):
    text = f.read_text(encoding="utf-8")
    m = re.match(r"---\r?\n(.*?)\r?\n---", text, re.S)
    if not m:
        bad.append(f"{f.parent.name}: no frontmatter")
        continue
    fm = m.group(1)
    if not re.search(rf"^name: {re.escape(f.parent.name)}\s*$", fm, re.M):
        bad.append(f"{f.parent.name}: name does not match folder")
    if not re.search(r"^description:", fm, re.M):
        bad.append(f"{f.parent.name}: no description")
print("\n".join(bad) or "skills ok")
sys.exit(1 if bad else 0)
