# Baseline Evidence: Editor Expert Quality Optimization

## Status

captured before editing `skills/editor/SKILL.md`

## Baseline source

- Skill prompt inspected: `skills/editor/SKILL.md`
- Eval fixture updated first: `tests/evals/skills/editor/cases.yaml`
- Current prompt contract at capture time: fixed three-stage report with optimized text, `Why`, assessment, and Chinese + English output.
- Prompt edit status at capture time: `skills/editor/SKILL.md` has not been edited for the 2026-05-26 expert-quality optimization.

## Current prompt behavior summary

The current `editor` prompt advertises support for Chinese, English, and Russian and says it returns a fixed three-stage report:

1. optimized text plus reason;
2. source language and assessment;
3. Chinese and English output.

The workflow runs that uniform report for every input, including simple or already-good text. That means the current baseline conflicts with the new expert-quality contract in predictable ways:

- it adds default `Why` and assessment sections;
- it duplicates source-language content outside the final target-language blocks;
- it does not define instruction/source/target language roles before acting;
- it does not honor explicit target-language-only output;
- it describes specific supported languages instead of all-language source intake;
- it treats bilingual output as mandatory display rather than default output with explicit override.

## Scenario baseline

| Scenario | Baseline behavior from current prompt | Gap against approved expert contract |
|---|---|---|
| `editor-expert-professional-polish` | Runs Stage 1 optimization, Stage 2 assessment, and Stage 3 bilingual output. | Overproduces default `Why` and assessment; expected concise Chinese and English final versions only. |
| `editor-expert-restraint-already-good` | Runs the full report even when a light polish is requested. | Risks gratuitous rewriting and duplicates the edited English source outside the English target block. |
| `editor-expert-dim-lighting-fidelity` | Includes a verification step, but does not name the `dim lighting` drift risk or role-based target rendering. | Fidelity depends on generic verification rather than explicit meaning-preservation guardrails and cross-checking. |
| `editor-expert-chinese-instruction-english-source` | Treats all input as source material and has no explicit instruction/source role split. | May confuse Chinese instruction framing with English source editing; expected Chinese framing and English source-language editing. |
| `editor-expert-english-instruction-chinese-source` | Treats all input as source material and has no explicit instruction/source role split. | May frame around source language instead of English instruction language; expected English framing and Chinese source-language editing. |
| `editor-expert-explicit-english-only-target` | Always returns Chinese and English output regardless of explicit target request. | Violates explicit target-language-only override. |
| `editor-expert-code-switching` | Generic terminology preservation exists, but no explicit code-switching rule. | May localize intentional mixed technical terms instead of preserving them. |
| `editor-expert-russian-source-edit` | Description specifically names Russian support and always returns optimized text plus Chinese and English output. | Does not distinguish edited source-language block from target-language blocks under the new template. |
| `editor-expert-russian-translation-only` | Always optimizes first and includes optimized source text even for translation-only requests. | Violates the rule that translation-only non-Chinese/non-English source should not add an optimized source-language block by default. |
| `editor-expert-pr-description` | Recognizes editing and likely produces useful PR wording, but still uses the fixed report. | Overproduces assessment/Why and does not default to concise target-language deliverables. |
| `editor-expert-notes-only-when-asked` | Always includes a `Why` and assessment, regardless of request. | Notes are not gated to explicit request; output is report-like. |
| `editor-expert-ambiguity-without-notes` | Assessment may discuss ambiguity by default. | Adds commentary even when the user did not request notes. |
| `editor-expert-integrity-boundary` | Prime directive says misleading wording should use preserved-meaning output. | Does not require a brief response-language refusal plus accurate target-language alternatives. |

## Baseline conclusion

The current prompt has useful meaning-preservation language, but its fixed report structure and missing language-role model are the baseline behaviors this change is designed to replace. M2 must update `skills/editor/SKILL.md`; M3 must compare post-change behavior against these same scenario classes.
