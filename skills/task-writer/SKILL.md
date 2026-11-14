---
name: task-writer
description: >
  Write lightweight, actionable task briefs for everyday or repository work.
  Use when asked to create a task, write a task brief, or turn an idea into
  actionable work such as "make this into a task." Do not turn a request to
  perform the work directly into a task-writing exercise.
---

# Task Writer

Produce a task that is clear enough to start and specific enough to finish.
Treat “20% effort, 80% result” as a simplicity principle, not a measured promise:
keep essential constraints and verification, and omit process that does not
help someone do the work.

## Write the task

- Use the request and available context. When the goal is clear, draft directly.
  Ask only when a missing fact materially changes the outcome, scope, or ability
  to proceed; ask the smallest useful question, not a planning questionnaire.
  State reasonable assumptions and keep consequential unknowns visible.
- Prefer one useful task. Split only when there are independent outcomes.
  Add detail only where it affects execution or verification; avoid speculative
  requirements, workshops, or extra artifacts.
- For repository work, read available local instructions, the task template,
  and existing numbering before choosing a format or destination. Follow those
  conventions instead of the default below; preserve existing records and edits.
- For file inputs and outputs, display repository-relative paths and link existing
  files relative to the saved task's location.
- Never invent deadlines, owners, sources, approvals, facts, or completed work.
- Save the task as a Markdown file by default, in the user's requested language,
  and return a concise link to the saved file. Honor explicit “show first,”
  “chat only,” or “do not save” requests without writing. If writing is unavailable
  or prohibited (including Plan mode), return the draft and explain that it was
  not saved; never claim a save succeeded without verifying it.
- Creating a task alone does not authorize executing the underlying work;
  honor any separate execution request.

## Task filenames

Use the user's requested destination, then existing repository directory and
naming conventions; otherwise save in the current workspace using
`tasks/NNN-YYYYMMDD-short-name.md`, for example
`tasks/001-20261114-task-naming.md`.

- Use the next number after the highest numbered task in the destination directory,
  starting at `001`, padded to at least three digits. Do not reset numbering by date.
- Use the task creation date as `YYYYMMDD` and a short lowercase, hyphenated name,
  usually two to four words. The date is not a deadline.
- Preserve existing task filenames when updating content or status. Do not rename
  old tasks merely to adopt this convention unless the user requests a rename.
- Before saving, inspect the destination and recheck filename availability;
  never overwrite another task. Create `tasks/` when needed and writing is permitted.
  If the destination cannot be inspected, return a chat draft with a provisional
  filename and explain that it was not saved.

## Default format

Use a concrete action and intended outcome as the title, followed by these seven
sections in order. Each may be brief; do not pad small tasks to fill the format.

- **Background:** the originating request, problem, and intended benefit, with
  enough context to understand the task independently.
- **Input:** specific materials the reader can use directly: linked files or
  document sections, direct source URLs, pasted text, or supplied data, each with
  its purpose. Include short essential facts inline. State missing or inaccessible
  inputs and whether they block progress; avoid vague references such as
  “relevant documentation.”
- **Output:** concrete deliverables and observable acceptance criteria. For file
  work, specify **create, modify, or delete**, the exact path, and intended change.
  Label new paths as planned; for other work, name the result without inventing files.
- **Rules:** relevant constraints, exclusions, and behavior to preserve. Link
  shared rules rather than repeating them. If there are no additional constraints,
  say so briefly instead of inventing requirements.
- **Approach:** the intended method, important decisions, dependencies, and how
  the result will be verified. Keep actual changes and deviations in Execution
  result; use the checklist to track actions rather than repeat the explanation.
- **Progress checklist:** a few observable actions with `- [ ]` boxes, including
  an appropriate check of the result. Annotate blockers with what is needed next.
- **Execution result:** actual changes, linked deliverables when available,
  verification evidence, deviations, failures, justified skips, and remaining work.

## Lifecycle

Before execution, keep actions unchecked and Execution result as “Pending
execution and verification.” During execution, update only actions supported by
completion evidence and annotate blockers. At completion or handoff, record actual
results and outstanding work; leave unfinished actions unchecked. Claim completion
only when the acceptance criteria are met and results are recorded. Do not invent
checks or perform the underlying work merely to populate this section.

Before returning, check that the deliverables meet the goal, the checklist can
produce and verify them, and assumptions and pending work remain distinguishable
from known facts and completed work. Remove detail that does not help execution.

## Conditional example

For everyday tasks with non-file deliverables, or an explicit request for the
worked everyday example, read [the everyday example](references/everyday-example.md).
Otherwise, use the core instructions and applicable local template without loading
that reference. The example illustrates the format; its meal constraints do not
apply to other tasks.
