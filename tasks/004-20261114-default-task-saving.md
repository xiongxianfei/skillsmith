# Save task briefs by default and rename the legacy task

## Background

Task requests previously returned chat drafts unless saving was explicitly requested. Make saving the normal behavior in both repository and installed task-writer copies, and give the legacy simplification task a numbered filename.

## Input

- [skills/task-writer/SKILL.md](../skills/task-writer/SKILL.md): repository skill before this change.
- Installed skill: `/home/xiongxianfei/.codex/skills/task-writer/SKILL.md`.
- [Renamed simplification task](003-20261114-simplify-repository.md): historical record whose contents must remain unchanged.
- [AGENTS.md](../AGENTS.md): contribution and validation rules.
- [Issue #63](https://github.com/xiongxianfei/skillsmith/issues/63): intended outcome and acceptance examples recorded before edits.

## Output

- Modify both task-writer copies to save Markdown briefs by default and return a concise link.
- Rename `tasks/simplify-repository.md` to `tasks/003-20261114-simplify-repository.md` without changing its contents.
- Create this task record as `tasks/004-20261114-default-task-saving.md`.

Acceptance: ordinary task requests save; explicit preview/chat-only requests do not; unavailable or prohibited writes produce an unsaved draft with an explanation; filenames never overwrite another task; task creation does not execute the underlying work.

## Rules

Preserve explicit user destinations, repository naming conventions, existing task filenames unless a rename is requested, unrelated workspace changes, and execution boundaries. Default to `tasks/NNN-YYYYMMDD-short-name.md` in the current workspace when no destination or convention is supplied. Do not commit, push or merge without authorization.

## Approach

Use an isolated branch from refreshed main for repository skill edits. Update contradictory chat-only and filename guidance together, synchronize the installed copy, rename the original workspace task, and check metadata, relative links, file identity and representative acceptance scenarios. Keep historical task results intact.

## Progress checklist

- [x] Record intended behavior and acceptance examples in an issue.
- [x] Update both skill copies consistently.
- [x] Rename the legacy task without altering contents.
- [x] Validate metadata, links, diff and instruction scenarios.
- [x] Save this task with actual results.

## Execution result

Repository skill changes are uncommitted on `improve/task-default-saving`, based on refreshed main at `c75eb98`, in sibling worktree `../skillsmith-task-default-saving`. The [updated skill](../../skillsmith-task-default-saving/skills/task-writer/SKILL.md) and installed skill have identical contents. The original checkout's repository skill remains unchanged; the rename and this task record are saved in that original checkout. Unrelated changes were preserved.

Validation:

- `python tests/validate_skills.py` using the isolated worktree's script: all 29 skills passed.
- Skill-creator `quick_validate.py` against both updated skill directories: both passed.
- `git diff --check` in the isolated worktree: passed.
- Byte comparison before and after renaming: identical contents.
- Instruction review covers ordinary saves, explicit preview requests, missing task directories, filename collisions, prohibited writes and the separate execution boundary. This is manual instruction review, not observed model testing.
- No references requiring repair to the old task filename were found before creating this historical record.
- The renamed task retains pre-existing references to retired `../docs/workflows.md`; the rename does not change link resolution. Its historical content was deliberately preserved.

Functional suites and live-model evaluations were skipped for this small instruction change. Metadata checks do not establish model quality or host compatibility. No commit, push, PR or merge was performed; issue #63 records the intended change.
