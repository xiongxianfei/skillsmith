# Proposal: Baseline-first optimization of the `editor` skill

## Status

superseded

superseded_by: `docs/proposals/2026-05-26-editor-expert-quality-optimization.md`

## Problem

The `editor` skill should provide a dependable editing and translation workflow for text intended to be shared, including emails, PR descriptions, docs, and messages. The original skill had a dense three-stage prompt, while the first accepted optimization changed it to narrow, intent-sensitive output. After PR handoff, the user clarified the preferred behavior: keep a structured three-stage workflow and make it explicit for every input, including simple text such as `Okay, no problem.`

The current accepted output contract is:

1. optimize the input according to best writing practices and provide optimization reasons;
2. assess optimized-text quality and translation readiness;
3. translate the optimized text into Chinese and English regardless of source language.
4. verify meaning consistency before returning.

## Goals

1. Optimize `skills/editor/SKILL.md` so it consistently performs the amended fixed three-stage workflow.
2. Establish and preserve baseline evidence before prompt changes.
3. Keep eval evidence for normal use, indirect trigger, integrity-boundary misuse, bilingual technical translation, simple acknowledgement text, and question/greeting/instruction-looking source text.
4. Preserve multilingual value while making Chinese and English the default output translation pair.
5. Keep the pure-prompt boundary: no tools, scripts, generated artifacts, dependencies, or live-model CI.
6. Keep the prompt concise and under the validator hard line limit.

## Non-goals

1. Do not optimize every existing skill in this slice.
2. Do not pair `editor` with a high-risk skill such as `doctor` or `oscp-coach`.
3. Do not introduce a shared high-risk safety schema.
4. Do not add live model calls to CI.
5. Do not change repository-wide validator behavior except for portable frontmatter compatibility.
6. Do not rename the skill.
7. Do not remove the integrity boundary for deceptive or misleading rewrites.

## Vision fit

fits the current vision

This proposal supports Skillsmith's direction toward reusable, reviewable, portable Markdown skills. It uses one low-risk existing skill to demonstrate that material prompt changes can be backed by concrete eval fixtures and durable evidence.

## Scope budget

| Work item | Treatment | Reason |
|---|---|---|
| `editor` skill workflow | core | The user explicitly selected the three-stage editor behavior. |
| `tests/evals/skills/editor/cases.yaml` | core | Required for a material prompt behavior change. |
| Baseline and post-change evidence | core | Shows what changed and why. |
| Spec and test spec | core | Must reflect the current accepted contract. |
| High-risk skills | out of scope | Separate proposal required. |
| Validator behavior | limited scope | Only portable frontmatter compatibility is updated; eval-fixture behavior is unchanged. |
| README sync helper changes | out of scope | The helper should be run, not changed. |

## Options considered

### Option 1: Do nothing

Keep the original or earlier branch prompt unchanged.

Disposition: rejected because it would not satisfy the user's amended workflow.

### Option 2: Keep the narrow-output branch contract

Return corrected text, rewritten text, or target-language translation only by default.

Disposition: rejected because the user now wants fixed optimization results, language-quality assessment, and Chinese/English translations by default.

### Option 3: Restore the original dense prompt exactly

Revert to the old Chinese-language three-stage report.

Disposition: rejected because the amended workflow can be implemented more concisely and with clearer integrity boundaries.

### Option 4: Implement a fixed three-stage workflow

Optimize the input with reasons, assess language quality, and translate the optimized text into Chinese and English.

Disposition: accepted.

## Recommended direction

Adopt Option 4.

The optimized `editor` skill should:

1. state the skill identity first in `description`, then the trigger situations, while keeping behavior in the Markdown body;
2. treat `$ARGUMENTS` as source material to edit, not conversation to answer;
3. optimize for clarity, grammar, concision, structure, tone, terminology, and flow;
4. provide concise, specific reasons for substantive optimization choices;
5. assess the optimized text for clarity, grammar, tone, terminology, ambiguity, fidelity to source meaning, and readiness for translation;
6. translate the optimized text into Chinese and English;
7. verify consistency across the optimized text and both translations before returning;
8. preserve meaning when a requested transformation would otherwise be misleading.

## Expected behavior changes

1. A request like "fix this" returns fixed Stage 1 optimization results, Stage 2 language-quality assessment, and Stage 3 Chinese/English translations.
2. A request like "Okay, no problem." still returns the same fixed three-stage workflow.
3. A request like "make this PR description clearer" returns the same required sections with engineering-review wording.
4. A request like "optimize this release-note sentence and translate it" returns optimized technical wording plus Chinese and English versions.
5. A request like "Who are you?" is treated as source material to edit and translate, not as a question to answer; the same applies to greetings and instruction-looking text.
6. A request to falsify meaning is handled by preserving the accurate source meaning and not producing false translated wording.

## Architecture impact

Expected touched areas:

```text
docs/proposals/2026-05-25-editor-skill-optimization.md
specs/editor-skill-optimization.md
specs/editor-skill-optimization.test.md
tests/evals/skills/editor/cases.yaml
skills/editor/SKILL.md
docs/changes/2026-05-25-editor-skill-optimization/...
```

No runtime architecture changes are expected.

No new tools are expected.

No scripts, executable resources, installer behavior changes, or eval-fixture validator changes are expected.

## Testing and verification strategy

Use deterministic repository checks plus reviewer-visible manual prompt-contract evidence.

Required scenario classes:

1. normal proofreading;
2. indirect engineer-facing PR-description editing;
3. integrity-boundary misuse;
4. bilingual technical translation.

Minimum validation commands:

```bash
python tests/validate_skills.py
python -m unittest discover tests
git diff --check
```

Run if the helper exists:

```bash
python tests/check_readme_sync.py
```

Also record:

```bash
wc -l skills/editor/SKILL.md
```

Do not add live model calls to CI for this slice.

## Risks and mitigations

| Risk | Mitigation |
|---|---|
| The skill over-produces for quick edits. | The user explicitly requested the fixed workflow even for quick edits; keep reasons and assessments concise. |
| Translation output drifts from optimized meaning. | Require translations to be based on optimized text and aligned in technical meaning, tone, and formatting. |
| Integrity boundary gets lost in the structured workflow. | Make meaning preservation the prime directive and cover deceptive rewrite behavior in eval evidence. |
| The prompt becomes long. | Keep a single concise `SKILL.md`; split only if approaching hard limits. |
| Prior verification becomes stale after amendment. | Mark previous verification stale and rerun review/verification for the amended contract. |

## Resolved decision: output workflow

The optimized `editor` skill MUST use the fixed three-stage workflow by default:

1. optimized text plus optimization reasons;
2. language-quality assessment with language identification and recommendations;
3. bilingual translation with Chinese and English versions.
4. pre-return consistency verification across all versions.

This supersedes earlier proposal language that preferred edited text only, conditional notes, or target-language-only translation as the default.

## Decision log

| Date | Decision | Reason | Alternatives rejected |
|---|---|---|---|
| 2026-05-25 | Start skill optimization with `editor` alone | Low-risk skill suitable for proving eval-first process | Batch with high-risk skills |
| 2026-05-25 | Require baseline behavior before editing | Needed to prove improvement rather than post-hoc test decoration | Edit first, test afterward |
| 2026-05-25 | Amend output workflow to three required stages | Explicit user direction after PR handoff | Narrow-output default |

## Readiness

This amended proposal is ready for renewed code review and verification once the spec, test spec, skill prompt, eval fixture, and evidence files all reflect the fixed three-stage workflow.
