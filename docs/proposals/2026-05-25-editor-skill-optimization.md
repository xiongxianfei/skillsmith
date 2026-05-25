# Proposal: Baseline-first optimization of the `editor` skill

## Status

accepted, amended by user direction on 2026-05-25

## Problem

The `editor` skill should provide a dependable editing and translation workflow. The original skill had a dense three-stage prompt, while the first accepted optimization changed it to narrow, intent-sensitive output. After PR handoff, the user clarified the preferred behavior: keep a structured three-stage workflow, but make it concise and explicit.

The current accepted output contract is:

1. optimize the input according to best writing practices and provide optimization reasons;
2. review language quality and translation readiness;
3. translate the optimized text into Chinese and English.

## Goals

1. Optimize `skills/editor/SKILL.md` so it consistently performs the amended three-stage workflow.
2. Establish and preserve baseline evidence before prompt changes.
3. Keep eval evidence for normal use, indirect trigger, integrity-boundary misuse, and bilingual technical translation.
4. Preserve multilingual value while making Chinese and English the default output translation pair.
5. Keep the pure-prompt boundary: no tools, scripts, generated artifacts, dependencies, or live-model CI.
6. Keep the prompt concise and under the validator hard line limit.

## Non-goals

1. Do not optimize every existing skill in this slice.
2. Do not pair `editor` with a high-risk skill such as `doctor` or `oscp-coach`.
3. Do not introduce a shared high-risk safety schema.
4. Do not add live model calls to CI.
5. Do not change repository-wide validator behavior unless the eval-fixture path cannot represent this skill change.
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
| Validator behavior | out of scope | Existing fixture path supports this change. |
| README sync helper changes | out of scope | The helper should be run, not changed. |

## Options considered

### Option 1: Do nothing

Keep the original or earlier branch prompt unchanged.

Disposition: rejected because it would not satisfy the user's amended workflow.

### Option 2: Keep the narrow-output branch contract

Return corrected text, rewritten text, or target-language translation only by default.

Disposition: rejected because the user now wants optimization reasons, language-quality assessment, and Chinese/English translations by default.

### Option 3: Restore the original dense prompt exactly

Revert to the old Chinese-language three-stage report.

Disposition: rejected because the amended workflow can be implemented more concisely and with clearer integrity boundaries.

### Option 4: Implement a concise three-stage workflow

Optimize the input with reasons, assess language quality, and translate the optimized text into Chinese and English.

Disposition: accepted.

## Recommended direction

Adopt Option 4.

The optimized `editor` skill should:

1. keep the existing trigger metadata and pure-prompt structure;
2. treat `$ARGUMENTS` as source text plus editing direction;
3. optimize for clarity, grammar, concision, structure, tone, terminology, and flow;
4. provide concise reasons for substantive optimization choices;
5. assess clarity, grammar, tone, terminology, ambiguity, fidelity, and readiness for translation;
6. translate the optimized text into Chinese and English;
7. refuse or redirect misleading transformations and only translate accurate wording.

## Expected behavior changes

1. A request like "fix this" returns optimized text, reasons, assessment, and Chinese/English translations.
2. A request like "make this PR description clearer" returns the same required sections with engineering-review wording.
3. A request like "optimize this release-note sentence and translate it" returns optimized technical wording plus Chinese and English versions.
4. A request to falsify meaning is handled as an integrity boundary and does not produce false translated wording.

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

No scripts, executable resources, installer behavior changes, or repository-wide validator changes are expected.

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
| The skill over-produces for quick edits. | The user explicitly requested the full workflow; keep reasons and assessments concise. |
| Translation output drifts from optimized meaning. | Require translations to be based on optimized text and aligned in technical meaning, tone, and formatting. |
| Integrity boundary gets lost in the structured workflow. | Keep a dedicated integrity boundary section in `SKILL.md` and eval evidence. |
| The prompt becomes long. | Keep a single concise `SKILL.md`; split only if approaching hard limits. |
| Prior verification becomes stale after amendment. | Mark previous verification stale and rerun review/verification for the amended contract. |

## Resolved decision: output workflow

The optimized `editor` skill MUST use the three-stage workflow by default:

1. optimized text plus optimization reasons;
2. language-quality assessment;
3. Chinese and English translations.

This supersedes earlier proposal language that preferred edited text only, conditional notes, or target-language-only translation as the default.

## Decision log

| Date | Decision | Reason | Alternatives rejected |
|---|---|---|---|
| 2026-05-25 | Start skill optimization with `editor` alone | Low-risk skill suitable for proving eval-first process | Batch with high-risk skills |
| 2026-05-25 | Require baseline behavior before editing | Needed to prove improvement rather than post-hoc test decoration | Edit first, test afterward |
| 2026-05-25 | Amend output workflow to three required stages | Explicit user direction after PR handoff | Narrow-output default |

## Readiness

This amended proposal is ready for renewed code review and verification once the spec, test spec, skill prompt, eval fixture, and evidence files all reflect the three-stage workflow.
