# Explain Change: Editor skill optimization

## Summary

This branch now reflects the amended `editor` skill contract requested after PR handoff. The skill uses a required three-stage workflow:

1. optimize the input according to writing best practices and provide optimization reasons;
2. review language quality and translation readiness;
3. translate the optimized text into Chinese and English.

The prompt remains a pure Markdown skill with no tools, scripts, live model CI, installer changes, or validator changes.

## Problem

The earlier branch version optimized `editor` for narrow, intent-sensitive output. That version returned corrected or rewritten text only by default and translated only into the requested target language.

The user then clarified that the desired workflow should include optimization reasons, language-quality assessment, and Chinese/English translation as the default behavior. That amended request made the earlier spec, test spec, evidence, and verification report stale.

## Decision trail

| Decision point | Outcome | Why |
|---|---|---|
| Original proposal | Optimize `editor` alone with baseline-first evidence | Low-risk first slice for the skill-quality process. |
| Original implementation | Narrow conditional output contract | Previously accepted by spec/review/verify, later superseded. |
| User amendment | Require three-stage workflow | Explicit instruction after PR handoff. |
| Current implementation | Update skill and related docs to amended contract | Avoid stale governance artifacts that contradict the prompt. |
| Architecture | Still no separate architecture artifact | No runtime, installer, dependency, data-flow, generated asset, or CI behavior changed. |

## Diff rationale by area

| File | Change | Reason | Evidence |
|---|---|---|---|
| `skills/editor/SKILL.md` | Requires optimized text, optimization reasons, language-quality assessment, Chinese translation, and English translation. | Implements the amended user workflow. | Validator; line count; post-change evidence. |
| `tests/evals/skills/editor/cases.yaml` | Updates expected behavior to require the full workflow and bilingual Chinese/English output. | Keeps eval evidence aligned with the prompt contract. | `python tests/validate_skills.py`. |
| `specs/editor-skill-optimization.md` | Replaces narrow-output requirements with the amended three-stage contract. | Makes the governing behavior explicit and testable. | R1-R27 and AC1-AC15. |
| `specs/editor-skill-optimization.test.md` | Remaps tests to T1-T10 for the three-stage workflow. | Keeps proof surfaces aligned with amended requirements. | Manual evidence and validation commands. |
| `baseline-evidence.md` | Records the original baseline and the pre-amendment branch behavior that no longer satisfied the user's amended request. | Preserves why the post-PR update was needed. | Scenario comparison. |
| `post-change-evidence.md` | Records prompt-contract evidence for the amended workflow. | Shows how the prompt now satisfies each scenario class. | T5-T10 evidence. |
| `docs/proposals/2026-05-25-editor-skill-optimization.md` | Adds an amendment section. | Prevents the accepted proposal from contradicting the amended direction. | User amendment. |
| `docs/plans/2026-05-25-editor-skill-optimization.md` | Marks earlier M2/M3 contract as superseded by amendment and routes to renewed review. | Keeps lifecycle state honest after changing a previously verified PR. | Current handoff summary. |
| `change.yaml`, `review-log.md`, `docs/plan.md`, `verify-report.md` | Records that prior verification is stale and renewed review/verification are needed. | Avoids claiming branch-ready based on old evidence. | Local validation after amendment. |

## Skill behavior rationale

The revised skill keeps the existing trigger metadata because the skill still handles polishing, proofreading, refining, and translation for Chinese, English, and Russian source text. The body now makes the output contract explicit:

- `### 1. Optimized Text`: edited source text.
- `### 2. Optimization Reasons`: concise reasons for substantive changes.
- `### 3. Language Quality Assessment`: clarity, grammar, tone, terminology, ambiguity, and readiness for translation.
- `### 4. Chinese Translation`: Chinese version of the optimized text.
- `### 5. English Translation`: English version of the optimized text.

The integrity boundary remains because the amended workflow should not optimize or translate false or misleading claims.

## Tests and proof

| Test/proof ID | Surface | What it proves |
|---|---|---|
| T1 | `tests/evals/skills/editor/cases.yaml` plus validator | Eval fixture has required normal, indirect-trigger, and misuse coverage. |
| T2 | `baseline-evidence.md` | Baseline and pre-amendment branch behavior are recorded. |
| T3-T4 | `skills/editor/SKILL.md` plus validator/manual review | Metadata, pure-prompt boundary, `## Output Format`, and three-stage workflow exist. |
| T5-T8 | `post-change-evidence.md` | Normal proofreading, PR editing, bilingual technical translation, and integrity boundary are covered. |
| T9 | `post-change-evidence.md` | Pasted text, explanation requests, and ambiguity behavior are covered. |
| T10 | Validation commands and line count | Repository validation passes and the prompt remains below the hard line limit. |

## Validation evidence after amendment

- `python tests/validate_skills.py` passed.
- `python -m unittest discover tests` passed.
- `python tests/check_readme_sync.py` passed.
- `git diff --check` passed.
- `wc -l skills/editor/SKILL.md` reported 71 lines.

Hosted CI status is not claimed here.

## Review resolution summary

Historical material findings resolved before the original implementation:

- `F-PROP-EDITOR-001`: accepted; direct translation coverage was added.
- `F-SPEC-EDITOR-001`: accepted; unsupported-language behavior was bounded in the earlier contract.
- `F-SPEC-EDITOR-002`: accepted; downstream artifact order was corrected.

The user amendment supersedes part of the earlier narrow-output contract. It does not reopen those historical review findings, but it requires renewed code review and final verification for the amended implementation.

## Alternatives rejected

- Keep the old verified narrow-output prompt: rejected because it contradicts the user's amended requested workflow.
- Revert exactly to the original dense Chinese prompt: rejected because the amended workflow can be implemented concisely while preserving pure-prompt portability.
- Add live model CI: rejected by scope and existing test strategy.
- Change validator behavior: rejected as unnecessary; the existing eval fixture path still represents the material skill change.

## Scope control

- No other skill prompt was optimized.
- No high-risk skill was changed.
- No runtime tool, script, dependency, generated prompt asset, installer behavior, or live model CI was added.
- The skill name, frontmatter structure, `$ARGUMENTS`, and pure-prompt boundary remain intact.

## Risks and follow-ups

Risk: the amended workflow intentionally produces more output than the earlier narrow-output contract. The mitigation is to keep reasons and assessments concise.

Follow-up stage: renewed code review and final verification should run for the amended contract before claiming branch-ready or PR-ready again.
