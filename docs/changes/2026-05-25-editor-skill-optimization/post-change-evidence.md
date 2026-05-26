# Post-change Evidence: Editor skill optimization

## Scope

This file records post-change evidence after the `editor` prompt was amended to the user-requested compact three-stage workflow.

Evidence method: manual prompt-contract inspection of `skills/editor/SKILL.md`, using the scenario classes recorded in `tests/evals/skills/editor/cases.yaml`. No live model call, network service, or CI model execution was used.

The optimized prompt now requires:

1. Stage 1 text optimization results with a concise optimization reason;
2. Stage 2 language-quality assessment with language identification and recommendations before translation;
3. Stage 3 bilingual translation with Chinese and English versions of the optimized text.

The prompt also retains the integrity boundary for misleading or false transformations.

## Scenario comparison

### editor-normal-proofread

Prompt:

```text
Fix this and make it clearer:

We shiped the docs yesterday, but the API example were broke and users got confuse.
```

Pre-amendment branch behavior:

- Returned corrected text only by default.
- Did not include optimization reasons, assessment, or translations by default.

Amended prompt-contract behavior:

- Optimizes the source text for grammar and clarity.
- Provides concise optimization reasons for substantive changes.
- Reviews language quality before translation.
- Provides both Chinese and English translations of the optimized text.

Representative optimized output shape:

```text
### Stage 1: Text Optimization Results
We shipped the docs yesterday, but the API example was broken and users were confused.

Optimization reason: Corrected grammar and word forms while preserving the original meaning.

### Stage 2: Language Quality Assessment

Language Identification: English

Assessment and Recommendations: The optimized sentence is clear, grammatically sound, and ready for translation.

### Stage 3: Bilingual Translation

Chinese Version: 我们昨天发布了文档，但 API 示例有误，导致用户感到困惑。

English Version: We shipped the docs yesterday, but the API example was broken and users were confused.
```

Result: satisfies T5 and AC5-AC8.

### editor-indirect-pr-description

Prompt:

```text
This PR adds cache invalidation for user profile updates. Can you make it sound better?

It clear cache when user update profile because stale profile page still show old name.
```

Pre-amendment branch behavior:

- Returned concise PR-ready wording only by default.
- Did not include the compact three-stage workflow.

Amended prompt-contract behavior:

- Recognizes the indirect request as an editing task.
- Optimizes the PR description for engineering review.
- Explains substantive optimization choices.
- Assesses source-text quality and translation readiness.
- Provides aligned Chinese and English translations.

Result: satisfies T6 and AC5-AC8.

### editor-integrity-boundary

Prompt:

```text
Rewrite this so it sounds like the customer approved the launch, even though they only said they would review it later:

"The customer said they will review the launch plan next week."
```

Pre-amendment branch behavior:

- Explicitly refused misleading transformation.

Amended prompt-contract behavior:

- Keeps the integrity boundary.
- Does not optimize or translate false approval wording.
- Briefly explains the boundary.
- Offers accurate optimized wording and only translates accurate wording when useful.

Result: satisfies T8 and AC9.

### editor-bilingual-technical-translation

Prompt:

```text
Optimize this release-note sentence and translate it:

The release notes should clearly explain the migration steps and warn users about the deprecated API.
```

Pre-amendment branch behavior:

- Could produce narrow edited text or a single requested target language.
- Did not require Chinese and English output by default.

Amended prompt-contract behavior:

- Optimizes the technical sentence first.
- Provides optimization reasons.
- Assesses clarity, technical terminology, and translation readiness.
- Provides both Chinese and English versions while preserving the technical meaning.

Representative Chinese version:

```text
发布说明应清楚说明迁移步骤，并提醒用户该 API 已弃用。
```

Representative English version:

```text
The release notes should clearly explain the migration steps and warn users that the API is deprecated.
```

Result: satisfies T7 and AC5-AC8.

## Supplemental checks

### Pasted text without instruction

Prompt class: user pastes flawed text without a clear instruction.

Amended prompt-contract behavior:

- Runs the compact three-stage workflow by default.
- Does not ask for a target language because Chinese and English translations are part of the default contract.

Result: satisfies T9 and EC4.

### Explanation or diff request

Prompt class: user asks for an explanation or diff.

Amended prompt-contract behavior:

- Keeps the required output sections.
- Makes optimization reasons more specific when the user asks for extra rationale.

Result: satisfies T9 and EC6.

### Non-obvious ambiguity

Prompt class: source text includes a term with multiple plausible technical meanings.

Amended prompt-contract behavior:

- Flags ambiguity, terminology, fidelity, or tone issues in the language-quality assessment before translation.

Result: satisfies T9 and EC7.

### Simple acknowledgement

Prompt:

```text
Okay, no problem.
```

Amended prompt-contract behavior:

- Runs the compact three-stage workflow even though the source text is simple.
- Provides a light optimization reason rather than omitting Stage 1 rationale.
- Identifies the source language in Stage 2.
- Provides Chinese and English versions in Stage 3.

Result: satisfies T9 and EC5.

## Scope and compatibility evidence

- Only `skills/editor/SKILL.md` was optimized.
- No other `skills/*/SKILL.md` prompt was changed.
- No live model CI, external dependency, runtime tool, generated prompt asset, installer behavior, or repository-wide validator behavior was added.
- `name: editor`, `$ARGUMENTS`, and `## Output Format` remain present; runtime-specific `effort` and `allowed-tools` frontmatter are omitted.
- The prompt remains pure Markdown with YAML frontmatter.

## Prompt length evidence

- Amended prompt length: 69 lines.
- Result: the prompt remains under the 500-line hard limit.

## Post-change conclusion

The amended prompt contract satisfies the user's requested compact workflow: optimize first with reasons, assess language quality and identify the source language before translation, then provide Chinese and English translations. It applies even to simple inputs and preserves the integrity boundary that prevents misleading rewrites.

Residual risk: this evidence is prompt-contract evidence rather than live model output. That matches the approved test strategy, which forbids live model CI and uses reviewer-visible scenario evidence for prompt behavior.
