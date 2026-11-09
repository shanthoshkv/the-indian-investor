#!/usr/bin/env sh
# Symlink .agents/skills and .claude/skills to the canonical skills/ folders.
# Edit skills/ only. Re-run after adding a skill directory.
set -e
root="$(cd "$(dirname "$0")/.." && pwd)"
for dest in "$root/.agents/skills" "$root/.claude/skills"; do
  mkdir -p "$dest"
  for s in "$root"/skills/*/; do
    name="$(basename "$s")"
    link="$dest/$name"
    if [ -L "$link" ]; then continue; fi
    if [ -e "$link" ]; then echo "Path exists and is not a link: $link" >&2; exit 1; fi
    ln -s "${s%/}" "$link" && echo "Linked $link"
  done
done
