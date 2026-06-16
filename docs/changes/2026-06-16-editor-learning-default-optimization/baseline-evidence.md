# Baseline Evidence: Editor Learning Default Optimization

## Status

captured before editing `skills/editor/SKILL.md`

## Baseline source

- Skill prompt inspected: `skills/editor/SKILL.md`
- Eval fixture updated first: `tests/evals/skills/editor/cases.yaml`
- Current prompt contract at capture time: expert editor and translator with default Chinese + English output, explicit target-language overrides, and notes only when explicitly requested.
- Prompt edit status at capture time: `skills/editor/SKILL.md` has no diff for this change.
- Evidence method: static prompt-contract inspection. No live model call was used.

## Current prompt behavior summary

The current `editor` prompt already has the expert-quality foundation this change must preserve:

- it edits with fidelity and restraint;
- it separates instruction, source, and target language roles;
- it defaults visible output to Chinese + English;
- it honors explicit target-language requests;
- it refuses misleading or materially unsupported transformations;
- it keeps default output copyable and minimal.

The current prompt does not provide default learning value. It explicitly says:

- ambiguous wording should add explanatory notes only when the user asks for notes;
- output should have no default assessment section;
- output should have no default `Why` or change-explanation section;
- notes appear only when the user explicitly asks for explanation, notes, or changes;
- note labels are `Note` / `说明`, not `Learning notes` / `学习要点`.

This means the baseline learning value for normal polish and translation requests is intentionally zero by design. That is the behavior this change supersedes.

## Prompt-contract evidence

| Current prompt location | Baseline behavior |
| --- | --- |
| `skills/editor/SKILL.md:33-35` | Preserves ambiguity and allows explanatory notes only when requested. |
| `skills/editor/SKILL.md:61-64` | Suppresses default assessment, default `Why`, and default explanatory notes. |
| `skills/editor/SKILL.md:68-72` | Uses `Note` / `说明` labels rather than learning-oriented labels. |
| `skills/editor/SKILL.md:105-115` | Defines note-bearing output only for explicit note requests. |

## Scenario baseline

| Scenario | Baseline behavior from current prompt | Learning value today | Gap against approved learning-default contract |
| --- | --- | --- | --- |
| `editor-learning-default-polish` | Returns Chinese and English deliverables only. | None by default. | Must add a post-deliverable `Learning notes` block with anchored substantive notes. |
| `editor-learning-principle-not-report` | Preserves uncertainty and avoids unsupported certainty, but does not teach the uncertainty principle unless asked. | None by default. | Must teach the reusable principle behind preserving warranted uncertainty. |
| `editor-learning-explicit-english-target` | Displays only English because explicit target-language requests are honored. | None by default. | Must keep English-only visible output while adding `Learning notes` unless suppressed. |
| `editor-learning-no-notes-override` | Omits notes because notes are already opt-in only. | None, matching suppression. | Must continue omitting notes, now because explicit suppression overrides the new default. |
| `editor-learning-ambiguous-brevity` | Likely keeps output short and omits notes because notes are opt-in. | None by default. | Must not infer suppression from `keep it short`; concise notes should still appear. |
| `editor-learning-response-language-notes` | Uses Chinese framing for requested notes, but labels them `说明` and only because the user asks. | Some opt-in explanation only. | Must label the default teaching block `学习要点`, place it after deliverables, and avoid bilingual duplication. |
| `editor-learning-english-instruction-chinese-source` | Uses English framing and edits Chinese source as Chinese before target rendering. | None by default unless notes are requested. | Must preserve the role model while adding English `Learning notes` by default. |
| `editor-learning-skip-trivial` | Corrects the typo and omits notes. | None by default. | Must still render `Learning notes` with exactly one concise fallback note. |
| `editor-learning-restraint` | Makes minimal or no edits and omits notes. | None by default. | Must keep restraint and add at most one restraint-oriented fallback note. |
| `editor-learning-brittle-rule` | Provides notes only because the user asks to explain improvement; brittle-rule handling is not explicit. | Opt-in only; quality depends on general restraint language. | Must avoid or qualify brittle rules and keep fallback notes concrete. |
| `editor-learning-dim-lighting-fidelity` | Preserves meaning and omits notes. | None by default. | Must ensure any learning note supports fidelity rather than justifying drift. |
| `editor-learning-chinese-output-only` | Omits notes because notes are opt-in; likely honors the Chinese output-only request. | None, matching suppression. | Must continue omitting notes specifically because `只要译文` is explicit suppression. |
| `editor-learning-chinese-no-explanation` | Omits notes because notes are opt-in; likely honors the Chinese no-explanation request. | None, matching suppression. | Must continue omitting notes specifically because `不用解释` is explicit suppression. |
| `editor-learning-pr-description` | Recognizes the indirect edit request and produces concise deliverables. | None by default. | Must include learning notes after deliverables for indirect editing requests too. |
| `editor-learning-integrity-boundary` | Refuses misleading transformation and offers accurate alternatives. | No default teaching note. | Must preserve the refusal; if a note appears, it must reference the concrete approval-vs-review integrity issue. |
| `editor-learning-boundary-no-source` | The description does not advertise broad coaching, but no explicit standalone coaching boundary exists. | Not applicable; no deliverable. | Must ask for source text and omit `Learning notes` when no deliverable is produced. |
| `editor-learning-russian-source-edit` | Accepts Russian source edit and includes edited source-language block plus Chinese and English targets. | None by default. | Must preserve source-edit behavior and add learning notes unless suppressed. |
| `editor-learning-russian-translation-only` | Does not add an optimized Russian block for translation-only requests. | None by default. | Must preserve translation-only behavior and add learning notes unless suppressed. |

## Baseline comparison summary

| Dimension | Current baseline | Required after change |
| --- | --- | --- |
| Learning value | Absent by default; present only when requested. | Present by default for non-empty, non-suppressed editing and translation requests. |
| Bloat risk | Low because notes are usually absent. | Must remain low through deliverable-first output, note caps, fallback notes, and no padding. |
| Over-editing risk | Low-to-moderate; prompt already says minimal change when text is good. | Must stay low by forbidding extra edits for teaching and by testing already-good/trivial-only cases. |
| Fidelity | Strong existing fidelity and restraint language. | Must be preserved; learning notes must not justify meaning drift or unsupported certainty. |
| Suppression | Effectively default because notes are opt-in. | Must become explicit-only suppression for output-only or no-explanation requests. |
| Response language | Existing labels and requested notes follow response language. | Must keep this and use `Learning notes` / `学习要点` labels. |

## Baseline conclusion

The current prompt is already a strong expert editor and translator, but it is deliberately deliverable-only by default. Users learn nothing from ordinary polish or translation requests unless they explicitly ask for explanation. M2 must add default, concise, concrete learning notes without weakening the existing fidelity, restraint, target-language, response-language, or integrity behavior.
