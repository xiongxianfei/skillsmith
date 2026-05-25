# Explain Change: Editor skill optimization

## Current status

Implementation through M3 is ready for code review.

## M1 rationale

M1 adds the proof surface before prompt behavior changes. The approved spec requires `tests/evals/skills/editor/cases.yaml` and baseline evidence before editing `skills/editor/SKILL.md`.

The fixture records four reviewer-visible scenarios:

- simple proofreading;
- indirect PR-description editing;
- integrity-boundary misuse;
- targeted Russian translation.

The baseline evidence records the current prompt contract from `skills/editor/SKILL.md` without live model execution. The prompt currently requires a fixed three-stage report and Chinese-English bilingual translation, which is the behavior the later prompt optimization must improve.

## Later milestones

M2 updates only `skills/editor/SKILL.md`. It replaces the old fixed three-stage report with a shorter conditional workflow while preserving the skill name, `$ARGUMENTS`, `allowed-tools: ""`, and `## Output Format`.

The M2 prompt now defines default output modes for edited text, translation, conditional notes, and integrity-boundary handling. It also keeps Chinese, English, and Russian as the directly supported translation set and treats unsupported target languages as best effort outside the acceptance contract.

## M3 rationale

M3 records post-change evidence instead of changing prompt behavior again. The approved test spec requires reviewers to compare optimized behavior against the same four baseline scenarios before final implementation review.

The post-change evidence maps the optimized prompt contract to:

- simple proofreading;
- indirect PR-description editing;
- integrity-boundary misuse;
- targeted Russian translation;
- requested notes, explicit bilingual output, ambiguity, ambiguous pasted text, and unsupported-language boundary behavior.

The evidence confirms the prompt is shorter than the baseline: 74 lines after M2 versus 92 lines before the optimization. No length-increase justification is needed.

M3 also reruns the required validation set: skill validation, full unittest discovery, README sync, and whitespace checking.
