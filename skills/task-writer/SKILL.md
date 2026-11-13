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
  Keep small tasks short; add detail only where it affects execution or checking
  the result. Do not add speculative requirements, workshops, or extra artifacts.
- For repository work, read available local instructions, the task template,
  and existing numbering before choosing a format or destination. Follow those
  conventions instead of the default below; preserve existing records and edits.
  If relevant files are inaccessible, say so rather than claiming to have read them.
- Use linked, repository-relative paths for existing file inputs and outputs,
  with link targets relative to the task's saved location. Label proposed new
  paths as planned. For everyday work, use concrete information and deliverables
  such as a comparison, message, decision, or schedule; do not invent file paths
  to fill a section.
- Never invent deadlines, owners, sources, approvals, facts, or completed work.
  Keep unfinished actions unchecked. If recording earlier work, mark it complete
  only when supported by available evidence; label unperformed checks as pending.
- Return Markdown in chat by default, in the user's requested language. Save
  only when requested and permitted. If asked to show the task first, show the
  draft before writing files or implementing it. Creating a task alone does not
  authorize executing the underlying work; honor any separate execution request.

## Default format

Use a concrete action and intended outcome as the title, followed by:

- **Goal:** why the work matters and important supplied constraints.
- **Input:** available information, references, or files and their purpose.
  State any needed input that is still missing instead of inventing it.
- **Output:** concrete deliverables and observable criteria for being done.
- **Checklist:** a few useful actions with `- [ ]` boxes, including an appropriate
  check of the result. Describe planned verification without claiming it passed.

Before returning, check that the deliverables meet the goal, the checklist can
produce and verify them, and assumptions and pending work remain distinguishable
from known facts and completed work. Remove detail that does not help execution.

## Everyday example

Request: “Write a task to plan three vegetarian dinners for two, each under
30 minutes, with one shopping list.”

```markdown
# Plan three quick vegetarian dinners for two

## Goal
Make dinner easier with three vegetarian meals, each taking at most 30 minutes.

## Input
Three dinners for two people; vegetarian; 30-minute limit per dinner.

## Output
A three-meal plan and one combined shopping list with quantities for two.
Done when each meal has preparation steps and an estimated total time within
the limit, and the list covers the ingredients for all three dinners.

## Checklist

- [ ] Choose three vegetarian meals and estimate their total preparation times.
- [ ] Combine their ingredients into one shopping list for two people.
- [ ] Check portions, ingredient coverage, and each meal's 30-minute limit.
```
