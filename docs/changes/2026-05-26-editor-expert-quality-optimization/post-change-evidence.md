# Post-change Evidence: Editor Expert Quality Optimization

## Status

captured after M2 prompt implementation

## Evidence source

- Skill prompt inspected: `skills/editor/SKILL.md`
- Eval fixture inspected: `tests/evals/skills/editor/cases.yaml`
- Baseline comparison: `docs/changes/2026-05-26-editor-expert-quality-optimization/baseline-evidence.md`
- Evidence method: static prompt-contract inspection plus eval-fixture scenario comparison. No live model call was run or added to CI.

## Prompt contract summary

The optimized `editor` prompt now replaces the fixed three-stage report with a concise expert-editor contract:

- frontmatter describes expert professional editing and translation, default Chinese + English output, explicit target-language overrides, and common trigger contexts;
- the body defines expert editing as fidelity with restraint;
- non-negotiables separate instruction text from source text, accept source text in any detected language, edit source text before target rendering, preserve code-switching and domain terms, and refuse misleading transformations;
- workflow separates instruction, source, and target roles before editing;
- response language follows the instruction language when clear, otherwise the source language;
- target languages default to Chinese + English for non-empty source input and honor explicit target-language requests;
- integrity is checked before editing;
- meaning is resolved once and rendered into each visible target language;
- the output format removes default assessment, default `Why`, and duplicate source-language blocks;
- notes appear only when the user explicitly asks for explanation, notes, or changes;
- note-bearing and integrity-boundary templates repeat target-language blocks for every visible target language, defaulting to Chinese and English unless explicitly overridden.

## Scenario comparison

| Scenario | Baseline gap | Post-change evidence |
|---|---|---|
| `editor-expert-professional-polish` | Fixed report added default `Why` and assessment. | Prompt defaults to Chinese + English output, uses English response labels for English instructions, preserves uncertainty through the fidelity standard, and forbids default assessment, default `Why`, and default notes. |
| `editor-expert-restraint-already-good` | Fixed report risked gratuitous rewriting and duplicated English source content. | Prompt says strong edits are the smallest useful change, already-good text should be minimally changed, and Chinese/English source versions are not duplicated outside their target-language block. |
| `editor-expert-dim-lighting-fidelity` | Baseline relied on generic verification and did not name subtle drift risks. | Prompt requires preserving meaning, facts, logic, uncertainty, and tone; it resolves source meaning once and verifies visible target versions preserve the same meaning, which covers `dim lighting` versus `dimming light` drift. |
| `editor-expert-chinese-instruction-english-source` | Baseline had no explicit instruction/source role split. | Prompt separates instruction from source before editing, uses instruction language for labels/notes/refusals, edits source text in its source language, and defaults to Chinese + English target versions. |
| `editor-expert-english-instruction-chinese-source` | Baseline could frame around source language rather than English instruction language. | Prompt uses the instruction language for response framing when clear and edits Chinese source as Chinese before target-language rendering. |
| `editor-expert-explicit-english-only-target` | Baseline always returned Chinese and English output. | Prompt honors explicit target-language-only requests unless they conflict with meaning preservation or integrity, displays only the requested target, and keeps internal Chinese + English cross-checking where practical. |
| `editor-expert-code-switching` | Baseline had generic terminology preservation but no explicit code-switching rule. | Prompt explicitly preserves intentional code-switching, product names, API names, and domain terms unless localization is requested or the term is clearly wrong. |
| `editor-expert-russian-source-edit` | Baseline always ran optimized text plus bilingual report and described specific-language support. | Prompt accepts source text in any detected language as intake, includes an edited source-language block first only when a non-Chinese/non-English source edit/polish/rewrite/professionalize request is made, then repeats visible target-language blocks. |
| `editor-expert-russian-translation-only` | Baseline optimized first even for translation-only requests. | Prompt says not to add the edited source-language block for translation-only requests, while still rendering visible target-language versions by default. |
| `editor-expert-pr-description` | Baseline could improve PR wording but still produced report-like output. | Prompt description and workflow cover PR descriptions and professional editing; output rules keep the result concise without default assessment or default `Why`. |
| `editor-expert-notes-only-when-asked` | Baseline always included `Why` and assessment. | Prompt permits notes only when explicitly requested and places a single note after repeated visible target-language versions. |
| `editor-expert-ambiguity-without-notes` | Baseline could add assessment commentary by default. | Prompt requires preserving ambiguity or editing around it and adds explanatory notes only when the user asks for notes. |
| `editor-expert-integrity-boundary` | Baseline lacked a required brief refusal plus accurate target-language alternatives. | Prompt refuses misleading, false, deceptive, falsely attributed, or materially unsupported transformations, does the integrity check before editing, refuses in the response language, and repeats accurate alternatives for each visible target language. |

## Manual QA checklist result

| Check | Result | Evidence |
|---|---|---|
| Baseline evidence exists before prompt edit | pass | `baseline-evidence.md` was created during M1 before M2 edited `skills/editor/SKILL.md`. |
| Eval fixture includes required scenario classes | pass | `tests/evals/skills/editor/cases.yaml` includes 13 expert scenarios, including both mixed-language directions, explicit English-only target, code-switching, Russian edit/translation-only, notes, ambiguity, and integrity. |
| Default concise Chinese + English output | pass | `skills/editor/SKILL.md` defines default Chinese + English output and forbids assessment/default `Why`. |
| Already-good restraint and de-duplication | pass | Expert standard and output rules require smallest useful change and no duplicate source-language block for Chinese/English source edits. |
| Explicit English-only target | pass | Workflow honors explicit target-language-only requests and displays only requested targets. |
| `dim lighting` fidelity | pass | Meaning preservation and cross-checking are explicit; no prompt rule encourages semantic substitution. |
| Mixed-language role separation | pass | Workflow separates instruction/source/target roles and routes response framing and source editing separately. |
| Code-switching preservation | pass | Non-negotiables explicitly preserve intentional code-switching and domain terms. |
| Non-Chinese/non-English source edit versus translation-only | pass | Output format gates edited source-language block to edit/polish/rewrite/professionalize requests and excludes it for translation-only requests. |
| Notes only when asked | pass | Output format allows notes only for explicit explanation, notes, or changes requests. |
| Integrity boundary | pass | Non-negotiables and workflow require refusal plus accurate alternatives. |
| Prompt line count recorded | pass | `wc -l skills/editor/SKILL.md` returned 126 lines during M3 validation. |
| No unrelated scope expansion | pass | No live model CI, runtime tools, scripts, generated prompt assets, installer changes, validator changes, or unrelated skill prompt edits were introduced for M3. |

## Manual smoke note

No live weakest-model smoke was run in this milestone. The spec treats live model smoke as reviewer-visible evidence when available and forbids live model CI; this M3 evidence uses static prompt-contract inspection and deterministic repository validation instead. Because no model smoke was performed, the model-smoke-specific `dim lighting` execution requirement is not applicable here; the `dim lighting` scenario remains covered in the eval fixture and prompt-contract evidence.

## Post-change conclusion

The optimized prompt now addresses the baseline gaps on the same scenario surface: it removes the fixed report, adds language-role separation, preserves source-language editing before target rendering, defaults to concise Chinese + English output, honors explicit target-language overrides, gates notes to explicit requests, bounds non-Chinese/non-English source blocks, and adds an explicit integrity refusal path. Remaining proof is deterministic repository validation and downstream code review for M3.
