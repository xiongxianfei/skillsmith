# Editor Learning Default Optimization Test Spec

## Status

active

## Related spec and plan

- Spec: `specs/editor-learning-default-optimization.md`
- Plan: `docs/plans/2026-06-16-editor-learning-default-optimization.md`
- Architecture/ADRs: not applicable; plan-review R1 approved no separate architecture artifact for this pure prompt, eval fixture, and evidence slice.
- Reviews:
  - `docs/changes/2026-06-16-editor-learning-default-optimization/reviews/spec-review-r3.md`
  - `docs/changes/2026-06-16-editor-learning-default-optimization/reviews/plan-review-r1.md`
  - `docs/changes/2026-06-16-editor-learning-default-optimization/reviews/test-spec-approval-r1.md`

## Testing strategy

Use deterministic repository checks for static contracts and reviewer-readable evidence for model-behavior contracts.

- Unit: existing tests under `tests/` validate the skill validator, eval fixture schema, README sync helper, and CI contract. No new validator logic is planned.
- Integration: `python tests/validate_skills.py` validates the real `editor` skill and `tests/evals/skills/editor/cases.yaml`.
- End-to-end: not applicable because the skill remains a pure Markdown prompt with no executable app flow or live model CI.
- Smoke: run repository validation commands, `git diff --check`, and prompt line-count sanity check after prompt edits.
- Manual: baseline and post-change evidence compare representative prompts before and after the prompt change.
- Contract: inspect `skills/editor/SKILL.md` for frontmatter, pure-prompt boundary, output templates, suppression rules, learning-note rules, target-language behavior, and integrity boundaries.
- Migration: verify the old notes-on-request default is intentionally superseded while `name: editor`, `$ARGUMENTS`, `## Output Format`, copyable deliverables, default visible target languages, explicit target-language overrides, and pure Markdown compatibility remain stable.

## Requirement coverage map

| Requirement ID | Covered by | Level | Notes |
| --- | --- | --- | --- |
| R1 | T1, T15 | contract | Preserve the prior expert-quality contract except the superseded notes/default-teaching behavior. |
| R2 | T1, T15 | integration | Validator and static inspection prove no tools, scripts, generated assets, dependencies, or live-model CI. |
| R3-R5 | T2 | contract | Description remains editor/translator focused, mentions learning from edits, and avoids standalone coaching triggers. |
| R6-R8 | T4, T5, T7, T9, T10, T11, T12, T14 | manual | Default non-empty, non-suppressed requests include a post-deliverable, non-empty, non-interleaved learning block. |
| R9-R11 | T4, T8 | manual | English and Chinese labels are exact; other-language fallback is prompt-contract inspected. |
| R12-R13 | T4, T5, T11 | manual | Substantive notes use concrete anchoring and teach reusable principles. |
| R12a | T9, T10, T11, T12 | manual | Fallback notes reference concrete source condition, edit category, or integrity issue. |
| R14 | T8 | manual | Notes use response language only and are not duplicated bilingually. |
| R15-R16 | T4, T5, T10, T11, T12, T14 | manual | Learning notes preserve fidelity and do not justify drift, unsupported certainty, or misleading claims. |
| R17-R18 | T9, T10, T14 | manual | No extra edits for teaching; one note per substantive lesson, not per mechanical edit. |
| R19-R22 | T4, T9, T10, T14, T16 | manual, smoke | Note cap is a ceiling, not a target; line-count check guards prompt bloat. |
| R23 | T9 | manual | Trivial-only correction gets exactly one concise fallback note and no grammar lecture. |
| R24 | T10 | manual | Already-strong text stays minimally edited and gets at most one restraint note. |
| R25 | T11 | manual | Brittle-rule cases avoid or qualify unsafe lessons and use exactly one fallback when needed. |
| R26-R29 | T6, T7 | manual | Explicit suppression removes notes; ambiguous brevity keeps concise notes. |
| R30 | T13 | manual | Explicit learn-more requests may expand but remain anchored. |
| R31 | T5, T6 | manual | Explicit target-language requests control visible deliverables while notes remain unless suppressed. |
| R32 | T12 | manual | Integrity-boundary refusals remain truth-preserving and concise. |
| R33-R35a | T4, T5, T6, T9, T10 | manual | Default, explicit target, suppression, and fallback output templates are exercised. |
| R36 | T2 | contract | Prompt no longer says notes appear only when explicitly requested. |
| R37 | T3, T14 | manual | Baseline and post-change evidence compare learning value, bloat, over-editing, and fidelity. |
| R38 | T2-T14 | manual, integration | Eval fixture and evidence cover every required learning-default scenario class. |

## Example coverage map

| Example | Covered by | Notes |
| --- | --- | --- |
| E1 default polish includes learning notes | T4 | Default Chinese and English deliverables followed by anchored `Learning notes`. |
| E2 explicit English target still includes learning notes | T5 | English-only deliverable followed by learning notes unless suppressed. |
| E3 explicit suppression removes learning notes | T6 | `No notes` and output-only phrasing omit the block. |
| E4 ambiguous brevity does not suppress learning notes | T7 | `Keep it short` keeps concise learning notes. |
| E5 already-good text teaches restraint without padding | T10 | Minimal edits, `24 hours` preserved, at most one restraint note. |
| E6 trivial typo does not create a lesson quota | T9 | Typo fix, exactly one fallback note, no grammar lecture. |
| E7 already-strong text teaches restraint without padding | T10 | Same restraint behavior as E5, with explicit fallback-note assertion. |
| E8 integrity boundary preserves truth | T12 | Misleading approval request is refused or redirected accurately. |

## Edge case coverage

| Edge case | Covered by | Level | Notes |
| --- | --- | --- | --- |
| EC1 only translate into English | T5 | manual | Target-language-only is not no-notes suppression. |
| EC2 only output the translation | T6 | manual | Explicit output-only suppression removes notes. |
| EC3 keep it short | T7 | manual | Ambiguous brevity keeps concise notes. |
| EC4 Chinese `只要译文` | T6 | manual | Chinese output-only suppression removes notes. |
| EC5 Chinese `不用解释` | T6 | manual | Chinese no-explanation suppression removes notes. |
| EC6 Chinese instruction with English source | T8 | manual | Chinese labels and `学习要点`, English source edited as English. |
| EC7 English instruction with Chinese source | T8 | manual | English labels and `Learning notes`, Chinese source edited as Chinese. |
| EC8 typo-only source | T9 | manual | Exactly one concrete fallback note. |
| EC9 already-good source | T10 | manual | At most one restraint note and no invented edits. |
| EC10 brittle lesson | T11 | manual | Rule is qualified or replaced by one fallback note. |
| EC11 user asks for more explanation | T13 | manual | Expanded learning remains anchored. |
| EC12 misleading approval language | T12 | manual | Refusal or accurate alternative with truth-preserving note. |
| Empty or missing source text | T13 | manual | Asks for source and omits `Learning notes`. |
| Standalone coaching request without source | T13 | manual | Does not act as broad writing coach; asks for text. |
| Unsupported target language | T15 | manual | Existing editor target-language and integrity behavior remains governed by the prior expert spec. |

## Test cases

### T1. Skill structure remains valid and pure prompt

- Covers: R1, R2, AC2, AC3
- Level: integration
- Fixture/setup: `skills/editor/SKILL.md` after implementation.
- Steps:
  - Confirm frontmatter keeps `name: editor`.
  - Confirm no optional tool/runtime frontmatter is added.
  - Confirm `$ARGUMENTS` appears in the body.
  - Confirm `## Output Format` appears.
  - Run `python tests/validate_skills.py`.
- Expected result: The skill remains a valid pure Markdown prompt skill with no runtime dependencies.
- Failure proves: Implementation broke a repository skill contract or added out-of-scope runtime behavior.
- Automation location: `python tests/validate_skills.py`

### T2. Prompt contract advertises editor and translator with learning from edits

- Covers: R3, R4, R5, R36, R38, AC4, AC20
- Level: contract
- Fixture/setup: `skills/editor/SKILL.md`; `tests/evals/skills/editor/cases.yaml`.
- Steps:
  - Inspect the frontmatter description.
  - Confirm it identifies the skill as an expert professional editor and translator.
  - Confirm it mentions learning from edits to shared text.
  - Confirm it does not advertise standalone writing-coach triggers such as broad `help me improve my writing` without source text.
  - Search the prompt for obsolete rules saying notes appear only when explicitly requested.
  - Inspect `tests/evals/skills/editor/cases.yaml` for learning-default scenarios required by R38.
- Expected result: Static prompt and eval fixture reflect the new learning-default contract and remove the superseded notes-on-request default.
- Failure proves: Skill selection or prompt instructions still encode the rejected coaching scope or old notes behavior.
- Automation location: Manual contract inspection; `tests/evals/skills/editor/cases.yaml`; `python tests/validate_skills.py`

### T3. Baseline evidence is recorded before prompt edits

- Covers: R37, AC19
- Level: manual
- Fixture/setup: Current `skills/editor/SKILL.md` before M2 prompt edits; `docs/changes/2026-06-16-editor-learning-default-optimization/baseline-evidence.md`.
- Steps:
  - Before editing `skills/editor/SKILL.md`, record baseline behavior for the scenario classes listed in R38.
  - Record current learning value, expected to be absent or opt-in under the old contract.
  - Record bloat, over-editing, and fidelity observations for the same prompts planned for post-change evidence.
  - Confirm the evidence states that `skills/editor/SKILL.md` had no M1 diff when baseline was captured.
- Expected result: Baseline evidence exists and captures learning value from zero, not merely the fact that notes are absent.
- Failure proves: The change lacks before/after evidence and cannot support the improvement claim.
- Automation location: `docs/changes/2026-06-16-editor-learning-default-optimization/baseline-evidence.md`

### T4. Default substantive polish includes anchored learning notes

- Covers: R6-R8, R9, R12, R13, R15-R16, R19-R22, R33, R37-R38, E1, AC5, AC6, AC12, AC13, AC15, AC19, AC20
- Level: manual
- Fixture/setup: Eval scenario `editor-learning-default-polish` in `tests/evals/skills/editor/cases.yaml`.
- Steps:
  - Prompt: `Polish this:` followed by `We are committed to delivering excellent solutions for users and we will try to make the migration easy.`
  - Confirm Chinese and English final versions appear first.
  - Confirm an English-framed `Learning notes` block appears after both deliverables.
  - Confirm at least one note uses original-to-revised anchoring or an equivalent concrete reference.
  - Confirm the note teaches a reusable principle and does not say only `I improved clarity`.
  - Confirm the block has no more than three notes and is not padded.
- Expected result: The default output visibly teaches from substantive edits without interleaving or bloat.
- Failure proves: The core learning-default contract is not implemented.
- Automation location: `tests/evals/skills/editor/cases.yaml`; baseline and post-change evidence files.

### T5. Explicit target-language request keeps learning notes

- Covers: R6-R7, R12-R16, R26, R31, R34, R37-R38, E2, EC1, AC5, AC8, AC9, AC12, AC19, AC20
- Level: manual
- Fixture/setup: Eval scenario `editor-learning-explicit-english-target`.
- Steps:
  - Prompt: `Translate this into English:` followed by `这个方案比较稳，但上线后还是要观察错误率。`
  - Confirm only the English deliverable is visible when the target request is clear.
  - Confirm `Learning notes` appears after the English deliverable.
  - Confirm the note explains a transferable translation choice, such as preserving cautious uncertainty.
  - Confirm no visible Chinese deliverable is added merely because Chinese plus English is the default.
- Expected result: Target-language override controls visible deliverables while learning remains default-on.
- Failure proves: The implementation either ignores target-language overrides or treats them as no-notes suppression.
- Automation location: `tests/evals/skills/editor/cases.yaml`; evidence files.

### T6. Explicit suppression removes learning notes

- Covers: R26, R27, R31, R35, R37-R38, E3, EC2, EC4, EC5, AC8, AC10, AC19, AC20
- Level: manual
- Fixture/setup: Eval scenarios `editor-learning-no-notes-override`, `editor-learning-chinese-output-only`, and `editor-learning-chinese-no-explanation`.
- Steps:
  - Prompt one: `Just polish this. No notes.` followed by source text.
  - Prompt two: Chinese request using `只要译文`.
  - Prompt three: Chinese request using `不用解释`.
  - Confirm requested deliverables are produced.
  - Confirm no `Learning notes` / `学习要点` block appears.
  - Confirm target-language instructions are still honored.
- Expected result: Direct output-only or no-explanation suppression reliably removes the block.
- Failure proves: Explicit user intent is not respected or suppression examples are too English-centric.
- Automation location: `tests/evals/skills/editor/cases.yaml`; evidence files.

### T7. Ambiguous brevity keeps concise learning notes

- Covers: R6-R8, R19, R21, R22, R28, R29, R37-R38, E4, EC3, AC5, AC11, AC15, AC19, AC20
- Level: manual
- Fixture/setup: Eval scenario `editor-learning-ambiguous-brevity`.
- Steps:
  - Prompt: `Keep it short and polish this:` followed by source text.
  - Confirm the deliverable is concise.
  - Confirm a concise `Learning notes` block still appears.
  - Confirm the block is not padded and does not exceed the default cap.
- Expected result: Ambiguous brevity cues reduce verbosity but do not suppress default teaching.
- Failure proves: The implementation over-infers suppression from soft user intent.
- Automation location: `tests/evals/skills/editor/cases.yaml`; evidence files.

### T8. Mixed-language framing uses response language for notes only

- Covers: R6-R11, R14, R31, R33, R37-R38, EC6, EC7, AC5, AC6, AC7, AC8, AC20
- Level: manual
- Fixture/setup: Eval scenarios `editor-learning-response-language-notes`, `editor-learning-english-instruction-chinese-source`.
- Steps:
  - Use a Chinese instruction with English source text.
  - Use an English instruction with Chinese source text.
  - Confirm labels and learning notes use the response language.
  - Confirm Chinese-framed output labels the block `学习要点`.
  - Confirm English-framed output labels the block `Learning notes`.
  - Confirm notes are not duplicated bilingually by default.
  - Confirm source text is edited in its source language before target rendering.
- Expected result: Instruction/source/target language roles remain separate and notes follow response framing only.
- Failure proves: The learning change regressed the existing mixed-language role model.
- Automation location: `tests/evals/skills/editor/cases.yaml`; evidence files.

### T9. Trivial-only correction gets exactly one fallback note

- Covers: R6, R12a, R17-R18, R21-R23, R35a, R37-R38, E6, EC8, AC5, AC12, AC13, AC15, AC17, AC19, AC20
- Level: manual
- Fixture/setup: Eval scenario `editor-learning-skip-trivial`.
- Steps:
  - Prompt: `Polish this:` followed by `We shiped the docs yesterday.`
  - Confirm the typo is corrected.
  - Confirm deliverables appear before learning notes.
  - Confirm the `Learning notes` block appears by default.
  - Confirm the block contains exactly one concise fallback note.
  - Confirm the note identifies the correction as trivial or typo-only and says no broader writing pattern is worth teaching.
  - Confirm there is no full grammar lesson and no multi-note block.
- Expected result: Mandatory learning block remains visible without padding or over-explaining.
- Failure proves: The implementation either violates default teaching or turns trivial fixes into noise.
- Automation location: `tests/evals/skills/editor/cases.yaml`; evidence files.

### T10. Already-good text is minimally edited with at most one restraint note

- Covers: R6, R12a, R17-R22, R24, R35a, R37-R38, E5, E7, EC9, AC5, AC12, AC13, AC15, AC16, AC19, AC20
- Level: manual
- Fixture/setup: Eval scenario `editor-learning-restraint`.
- Steps:
  - Prompt: `Polish this:` followed by `The rollout is complete. We will monitor error rates for 24 hours and follow up if we see regressions.`
  - Confirm the wording is minimally changed or preserved.
  - Confirm `24 hours` is preserved.
  - Confirm the `Learning notes` block appears unless suppressed.
  - Confirm there is at most one restraint-oriented fallback note.
  - Confirm no unnecessary edit is introduced merely to create a lesson and the note count is not padded to three.
- Expected result: The implementation turns restraint into a teachable moment without over-editing.
- Failure proves: The highest-risk failure mode, editing to create lessons, is present.
- Automation location: `tests/evals/skills/editor/cases.yaml`; evidence files.

### T11. Brittle-rule teaching is qualified or avoided

- Covers: R12, R12a, R13, R15-R16, R21, R25, R37-R38, EC10, AC12, AC13, AC14, AC15, AC19, AC20
- Level: manual
- Fixture/setup: Eval scenario `editor-learning-brittle-rule`.
- Steps:
  - Use source text where a tempting lesson would be oversimplified, such as a passive-voice case where the actor is unknown or irrelevant.
  - Confirm the learning note does not teach an absolute rule such as `always use active voice`.
  - Confirm the note either qualifies the principle with context and exceptions or uses one fallback note saying no safe broad rule is worth teaching.
  - Confirm no meaning drift is justified by the teaching note.
- Expected result: Teaching carries epistemic restraint and avoids brittle writing rules.
- Failure proves: The learning layer introduces misleading instruction even if the deliverable is acceptable.
- Automation location: `tests/evals/skills/editor/cases.yaml`; evidence files.

### T12. Integrity-boundary request remains truth-preserving

- Covers: R6, R12a, R15-R16, R25, R32, R37-R38, E8, EC12, AC12, AC13, AC18, AC19, AC20
- Level: manual
- Fixture/setup: Eval scenario `editor-learning-integrity-boundary`.
- Steps:
  - Prompt asks to rewrite a customer review intent as customer approval.
  - Confirm the skill refuses or redirects the misleading transformation in the response language.
  - Confirm accurate alternatives are provided in visible target languages.
  - Confirm no output implies approval, consent, certainty, or attribution not present in the source.
  - If a learning note appears, confirm it references the concrete integrity issue and is concise.
- Expected result: Teaching never weakens the integrity boundary.
- Failure proves: The learning-default behavior can justify or hide misleading transformations.
- Automation location: `tests/evals/skills/editor/cases.yaml`; evidence files.

### T13. Boundary requests without normal deliverables are handled

- Covers: R5, R26, R30, EC11, empty input, standalone coaching request without source, AC4
- Level: manual
- Fixture/setup: Manual boundary prompts recorded in post-change evidence.
- Steps:
  - Prompt with no source text and ask the skill to polish.
  - Prompt with a standalone coaching request such as `How do I get better at writing emails?` and no source artifact.
  - Prompt with `explain more` or `help me learn more` plus source text.
  - Confirm missing-source and standalone coaching cases ask for source text and omit `Learning notes`.
  - Confirm learn-more with source may expand explanation but keeps it anchored to concrete edits.
- Expected result: The description and prompt do not expand into standalone coaching, while explicit learning requests with source remain supported.
- Failure proves: Trigger scope drift or unanchored coaching entered the implementation.
- Automation location: post-change evidence file; manual prompt-contract inspection.

### T14. Post-change evidence compares same scenario classes

- Covers: R6-R29, R31-R32, R37, R38, AC5-AC20
- Level: manual
- Fixture/setup: `docs/changes/2026-06-16-editor-learning-default-optimization/post-change-evidence.md`.
- Steps:
  - Record post-change behavior for the same scenario classes used in baseline.
  - Compare learning value, bloat, over-editing, and fidelity against baseline.
  - Confirm evidence covers default notes, explicit suppression, ambiguous suppression fallback, no-over-editing, trivial fallback, already-good restraint, brittle-rule qualification, translation notes, mixed-language framing, and integrity boundaries.
- Expected result: Post-change evidence proves learning value improved without unacceptable bloat, over-editing, or fidelity drift.
- Failure proves: The implementation has no reviewer-visible proof for the central product claim.
- Automation location: `docs/changes/2026-06-16-editor-learning-default-optimization/post-change-evidence.md`

### T15. Compatibility and migration remain bounded

- Covers: R1, R2, R31, R36, compatibility and migration claims, unsupported target-language boundary
- Level: contract
- Fixture/setup: `skills/editor/SKILL.md`, `README.md` if it mirrors editor behavior, and prior spec `specs/editor-expert-quality-optimization.md`.
- Steps:
  - Confirm the old notes-on-request text is removed or replaced only where this spec supersedes it.
  - Confirm default Chinese and English output remains unless explicit target languages override it.
  - Confirm explicit target-language-only output is preserved while adding notes unless explicitly suppressed.
  - Confirm no default assessment section, default `Why` section, or report-style stage output is added.
  - Confirm unsupported-language behavior remains governed by the prior expert spec.
  - Inspect README only if it duplicates editor description or output-contract text.
- Expected result: Migration is limited to the intended notes/default-teaching behavior.
- Failure proves: The change widened scope or regressed existing editor compatibility.
- Automation location: Manual contract inspection; `python tests/check_readme_sync.py` if README changes.

### T16. Repository validation and prompt-size smoke

- Covers: R2, R19-R22, performance expectations, AC2, AC3, AC15, AC21
- Level: smoke
- Fixture/setup: Repository after M1-M3 implementation.
- Steps:
  - Run `python tests/validate_skills.py`.
  - Run `python -m unittest discover tests`.
  - Run `python tests/check_readme_sync.py`.
  - Run `git diff --check`.
  - Run `wc -l skills/editor/SKILL.md`.
  - Record warnings, skipped checks, and prompt line count.
- Expected result: Required commands pass; prompt remains small enough for portable skill use; any warnings are reviewed and non-blocking.
- Failure proves: The change is not locally reproducible or violates repository compatibility.
- Automation location: shell commands listed above; implementation and verification evidence.

## Fixtures and data

- `tests/evals/skills/editor/cases.yaml` must be updated in M1 with learning-default scenarios, replacing obsolete expectations that default notes are absent.
- Required scenario IDs:
  - `editor-learning-default-polish`
  - `editor-learning-principle-not-report`
  - `editor-learning-explicit-english-target`
  - `editor-learning-no-notes-override`
  - `editor-learning-ambiguous-brevity`
  - `editor-learning-response-language-notes`
  - `editor-learning-skip-trivial`
  - `editor-learning-restraint`
  - `editor-learning-brittle-rule`
  - `editor-learning-integrity-boundary`
  - `editor-learning-chinese-output-only`
  - `editor-learning-chinese-no-explanation`
- `docs/changes/2026-06-16-editor-learning-default-optimization/baseline-evidence.md` records current behavior before prompt edits.
- `docs/changes/2026-06-16-editor-learning-default-optimization/post-change-evidence.md` records revised behavior after prompt edits.
- All examples should use fictional product, rollout, migration, documentation, PR, and customer-review text.

## Mocking/stubbing policy

No mocks or stubs are required. The repository checks are deterministic static checks. Prompt behavior evidence is manual/reviewer-readable and must not call live models from CI.

If a maintainer runs optional manual model smoke checks outside CI, the evidence should record the prompt, model or runtime surface, date, and short result summary. Optional smoke evidence cannot replace the deterministic checks or required baseline/post-change evidence.

## Migration or compatibility tests

- T1 and T15 verify the skill remains a portable Markdown prompt with stable `name: editor`, `$ARGUMENTS`, and `## Output Format`.
- T15 verifies the deliberate migration from notes-on-request to default `Learning notes` without changing unrelated editor behavior.
- T16 verifies repository-level validation still passes.
- PR notes should call out the user-visible output-contract change and the explicit suppression phrases.

## Observability verification

No logs, metrics, traces, audit events, or runtime telemetry are required.

Observable proof is through:

- M1 baseline evidence.
- M3 post-change evidence.
- Updated eval fixture scenarios.
- Validation command output recorded during implementation and verification.

## Security/privacy verification

- T12 verifies learning notes do not encourage misleading or false transformations.
- T13 verifies the skill does not request source-free coaching or invent content when source text is missing.
- T15 verifies no new tools, external services, generated assets, dependencies, credentials, private paths, or live model CI are introduced.
- Fixture examples must remain fictional or sanitized.
- Learning notes must not reveal hidden reasoning or unstated assumptions as facts.

## Performance checks

- T16 records `wc -l skills/editor/SKILL.md`.
- T4, T7, T9, T10, T11, and T14 check that learning notes are capped, concise, and not padded.
- No latency or runtime performance tests are applicable because the skill has no executable runtime.

## Manual QA checklist

- Default non-empty polish request includes `Learning notes` after deliverables.
- Default learning block is never empty.
- Substantive notes use concrete original-to-revised anchoring or equivalent concrete references.
- Fallback notes reference the source condition, edit category, or integrity issue.
- Explicit suppression removes learning notes in English and Chinese examples.
- Ambiguous brevity keeps concise notes.
- Explicit target-language requests still control visible deliverables.
- Mixed-language requests use response language for labels and notes only.
- Trivial-only and already-good cases produce one or fewer fallback notes as specified.
- Brittle-rule cases qualify or avoid unsafe principles.
- Integrity-boundary cases remain truthful.
- No assessment, default `Why`, stage report, bilingual note duplication, or standalone writing-coach mode appears.

## What not to test and why

- Do not add live model calls to CI; the spec explicitly keeps this slice deterministic and pure prompt.
- Do not test validator behavior changes; no validator change is in scope.
- Do not test installer behavior; install paths and packaging are unchanged.
- Do not test every language; the spec only requires response-language behavior, exact English/Chinese labels, and localized fallback where practical.
- Do not assert exact polished prose beyond safety-critical facts, labels, block presence, ordering, suppression, and meaning preservation; prompt outputs can vary while satisfying the contract.
- Do not require four learning notes; four is allowed only for longer text with genuinely distinct lessons.

## Uncovered gaps

None requiring return to spec or architecture. The remaining unautomated behavior is intentionally covered by eval fixture expectations plus baseline/post-change manual evidence because this repository does not run live model evals in CI.

## Next artifacts

1. M1 implementation: update `tests/evals/skills/editor/cases.yaml` and record `baseline-evidence.md` before editing `skills/editor/SKILL.md`.
2. M2 implementation: update `skills/editor/SKILL.md`, and README only if it mirrors changed editor behavior.
3. M3 implementation: record `post-change-evidence.md`, validation output, prompt line count, and handoff to code review.

## Follow-on artifacts

None yet.

## Readiness

Ready for implementation planning surface use. Implementation may start with M1 only: update eval fixtures and record baseline evidence before editing `skills/editor/SKILL.md`. Prompt implementation remains blocked until M1 baseline evidence is complete.
