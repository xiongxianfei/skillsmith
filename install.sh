#!/usr/bin/env bash
# install.sh — install all Skillsmith skills into ~/.claude/skills/
#
# Usage:
#   curl -sSL https://raw.githubusercontent.com/xiongxianfei/Skillsmith/main/install.sh | bash
#   curl -sSL .../install.sh | bash -s -- --target .claude/skills   # project-level
set -euo pipefail

REPO_URL="https://github.com/xiongxianfei/Skillsmith"
SKILLS_DIR="${HOME}/.claude/skills"
TMP_DIR="$(mktemp -d)"

# Parse --target flag
while [[ $# -gt 0 ]]; do
    case "$1" in
        --target)
            SKILLS_DIR="$2"
            shift 2
            ;;
        *)
            echo "Unknown option: $1" >&2
            exit 1
            ;;
    esac
done

cleanup() { rm -rf "$TMP_DIR"; }
trap cleanup EXIT

echo "Cloning Skillsmith..."
git clone --depth=1 --quiet "$REPO_URL" "$TMP_DIR/Skillsmith"

mkdir -p "$SKILLS_DIR"

installed=0
for skill_dir in "$TMP_DIR/Skillsmith/skills"/*/; do
    skill_name="$(basename "$skill_dir")"
    target="$SKILLS_DIR/$skill_name"
    if [ -d "$target" ]; then
        rm -rf "$target"
    fi
    cp -r "$skill_dir" "$target"
    echo "  installed: $skill_name"
    installed=$((installed + 1))
done

echo ""
echo "$installed skill(s) installed to $SKILLS_DIR"
echo "Restart Claude Code to activate them."
