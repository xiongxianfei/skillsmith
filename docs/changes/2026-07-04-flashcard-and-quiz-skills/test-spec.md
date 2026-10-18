# Test Spec: Flashcard And Quiz Generator Skills

## Status

active

## Related spec and plan

- Spec: `specs/flashcard-and-quiz-skills.md`
- Plan: `docs/plans/2026-07-04-flashcard-and-quiz-skills.md`
- Architecture/ADRs: not applicable; `docs/changes/2026-07-04-flashcard-and-quiz-skills/reviews/spec-review-r1.md` records `architecture-not-required`.

## Input artifact identities

| Input | Path | Status / Review state | Identity |
| --- | --- | --- | --- |
| Proposal | `docs/proposals/2026-07-04-flashcard-and-quiz-skills.md` | accepted | Proposal review R1 approved with no material findings. |
| Spec | `specs/flashcard-and-quiz-skills.md` | approved | Spec review R1 approved with no material findings. |
| Plan | `docs/plans/2026-07-04-flashcard-and-quiz-skills.md` | active | Plan review R1 approved with no material findings. |
| Architecture | not applicable | architecture-not-required | Spec review R1 records no architecture artifact required for this pure-prompt slice. |

## Testing strategy

Use deterministic local checks plus reviewer-visible prompt inspection and manual smoke evidence. The automated proof surface is contract oriented: eval fixture validation, skill structural validation, README synchronization, unit discovery, and whitespace checks. No live model calls, external export integrations, AnkiConnect, LMS APIs, schema-validator CI, or network services are part of this proof map.

M1 proves eval fixture coverage before skill prompt implementation. M2 proves skill structure, references, schemas, README sync, and no forbidden integration. M3 records prompt-inspection and manual smoke evidence before code-review.

## Requirement coverage map

| Requirement ID | Covered by | Level | Notes |
| --- | --- | --- | --- |
| R1-R4 | T7, T8, CMD2 | integration | Skill structural validation plus prompt inspection. |
| R5-R7 | T1, T2, T3, T4, T5, T6 | contract | Trigger boundary evals across both fixtures. |
| R8-R20 | T7, T8, T9, T10, T11 | manual | Prompt inspection and manual smoke evidence for workflow and output contracts. |
| R21-R25 | T12, T13 | integration | Reference files and schema-reference-only boundary. |
| R26 | T6, T11 | manual | Both-output fallback proof. |
| R27-R30 | T1-T6, CMD1, CMD2 | integration | Eval fixture validation and full validator after skills exist. |
| R31-R32 | T14, CMD4 | integration | README sync and contributor-doc inspection where changed. |
| R33-R35 | T13, T15, CMD2, CMD6 | integration | No forbidden integration, no validator/CI change, line count awareness. |

## Example coverage map

| Example | Covered by | Notes |
| --- | --- | --- |
| E1 | T1, T9 | Flashcard normal eval plus manual smoke. |
| E2 | T2, T10 | Quiz normal eval plus manual smoke. |
| E3 | T5 | Non-trigger scenario. |
| E4 | T6, T11 | Both-output trigger and fallback proof. |
| E5 | T3, T4 | Unsupported or inferred material boundary. |

## Edge case coverage

| Edge case | Covered by | Notes |
| --- | --- | --- |
| EC1 generic summary | T5 | Neither-skill trigger evidence. |
| EC2 Anki without count | T1, T9 | Default behavior inspection. |
| EC3 MCQs with feedback | T2, T10 | MCQ and rationale proof. |
| EC4 both outputs | T6, T11 | Composition/fallback proof. |
| EC5 short source for advanced output | T3, T4 | Unsupported material boundary. |
| EC6 direct integration request | T13, T15 | No external API or executable integration. |
| EC7 high-stakes guarantee | T15 | Boundary inspection. |

## Validation commands

| Command ID | Command | Classification | Owner | Owning milestone | First required milestone | Failure behavior | Zero-test behavior | Evidence artifact | Safe mode / side-effect boundary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CMD1 | `python -c 'from pathlib import Path; from tests.validate_skills import validate_cases_file; [(_ := validate_cases_file(name, Path(f"tests/evals/skills/{name}/cases.yaml")), (_).errors and (_ for _ in ()).throw(AssertionError(_.errors))) for name in ("flashcard-generator", "quiz-generator")]; print("direct eval fixture validation passed")'` | existing/configured | implementer | M1 | M1 code-review | Fails if either fixture is malformed. | Not applicable. | `docs/changes/2026-07-04-flashcard-and-quiz-skills/baseline-evidence.md` | Local read-only validation; no network or external side effects. |
| CMD2 | `python tests/validate_skills.py` | existing/configured | implementer | M2 | M2 code-review | Fails on skill structure, eval policy, or stale grandfathering. | Not applicable. | change metadata validation ledger | Local read-only validation; no network or external side effects. |
| CMD3 | `python -m unittest discover tests` | existing/configured | implementer | M1 | M1 code-review | Fails on repository unit/helper test failure. | Fails if unittest reports failures or errors; zero discovered tests would be treated as investigation-required. | change metadata validation ledger | Local test execution only. |
| CMD4 | `python tests/check_readme_sync.py` | existing/configured | implementer | M2 | M2 code-review | Fails on README skill table or command sync drift. | Not applicable. | change metadata validation ledger | Local read-only validation. |
| CMD5 | `git diff --check` | existing/configured | implementer | M1 | M1 code-review | Fails on whitespace errors. | Not applicable. | change metadata validation ledger | Local diff inspection only. |
| CMD6 | `wc -l skills/flashcard-generator/SKILL.md skills/quiz-generator/SKILL.md` | existing/configured | implementer | M2 | M2 code-review | Flags prompt size for reviewer inspection; does not by itself fail unless over spec limit. | Not applicable. | change metadata validation ledger | Local read-only command. |

## Milestone proof map

| Milestone | Required test IDs | Manual proof IDs | Command IDs | Evidence artifacts | Required before | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| M1 | T1-T6 | none | CMD1, CMD3, CMD5 | `docs/changes/2026-07-04-flashcard-and-quiz-skills/baseline-evidence.md` | code-review M1 | Full validator is deferred until skill directories exist. |
| M2 | T7, T8, T12, T13, T14, T15 | none | CMD2, CMD3, CMD4, CMD5, CMD6 | change metadata validation ledger | code-review M2 | Creates skill prompts, references, schemas, and README sync. |
| M3 | T9, T10, T11, T13, T15 | MP1, MP2, MP3, MP4 | CMD2, CMD3, CMD4, CMD5 | `docs/changes/2026-07-04-flashcard-and-quiz-skills/post-change-evidence.md` | code-review M3 | Records prompt-inspection and manual smoke evidence before final implementation review. |

## Test cases

T1. Flashcard eval fixture coverage
- Covers: R5, R7, R27-R30, E1, EC2
- Level: integration
- Command IDs: CMD1
- Fixture/setup: `tests/evals/skills/flashcard-generator/cases.yaml`
- Steps: Add normal Anki, indirect trigger, cloze/contrast, source-grounding boundary, non-trigger, and both-output scenarios.
- Expected result: Fixture validates and expected behavior covers atomicity, source grounding, canonical JSON, no broad prompts, and trigger boundaries.
- Failure proves: Flashcard skill lacks pre-implementation eval proof.
- Evidence artifact: `docs/changes/2026-07-04-flashcard-and-quiz-skills/baseline-evidence.md`
- Automation location: `tests.validate_skills.validate_cases_file`
- Required by milestone: M1

T2. Quiz eval fixture coverage
- Covers: R6, R7, R16-R20, R27-R30, E2, EC3
- Level: integration
- Command IDs: CMD1
- Fixture/setup: `tests/evals/skills/quiz-generator/cases.yaml`
- Steps: Add diagnostic quiz, indirect trigger, MCQ distractor quality, unsupported material, non-trigger, and both-output scenarios.
- Expected result: Fixture validates and expected behavior covers blueprint, learning objectives, rationales, feedback, MCQ quality, and trigger boundaries.
- Failure proves: Quiz skill lacks pre-implementation eval proof.
- Evidence artifact: `docs/changes/2026-07-04-flashcard-and-quiz-skills/baseline-evidence.md`
- Automation location: `tests.validate_skills.validate_cases_file`
- Required by milestone: M1

T3. Flashcard unsupported material boundary
- Covers: R11, R12, R29, E5, EC5
- Level: integration
- Command IDs: CMD1
- Fixture/setup: Flashcard fixture edge scenario.
- Steps: Include a prompt asking for related facts beyond a short source note.
- Expected result: Expected behavior requires source grounding, inference marking or avoidance, no fabricated unsupported details, and answerable prompts.
- Failure proves: Source-grounding boundary is not review-visible before prompt implementation.
- Evidence artifact: `tests/evals/skills/flashcard-generator/cases.yaml`
- Automation location: fixture validation plus reviewer inspection.
- Required by milestone: M1

T4. Quiz unsupported material boundary
- Covers: R11, R18, R29, E5, EC5
- Level: integration
- Command IDs: CMD1
- Fixture/setup: Quiz fixture edge scenario.
- Steps: Include a prompt asking for advanced questions from a short source note.
- Expected result: Expected behavior rejects unsupported advanced facts as source-grounded and avoids ambiguous questions.
- Failure proves: Quiz source-grounding boundary is not review-visible before prompt implementation.
- Evidence artifact: `tests/evals/skills/quiz-generator/cases.yaml`
- Automation location: fixture validation plus reviewer inspection.
- Required by milestone: M1

T5. Neither-skill trigger boundary
- Covers: R7, R30, E3, EC1
- Level: integration
- Command IDs: CMD1
- Fixture/setup: At least one non-trigger scenario in the eval fixtures.
- Steps: Include generic summary or rewrite requests.
- Expected result: Expected behavior states neither new skill should trigger.
- Failure proves: Trigger boundary may over-select for unrelated text tasks.
- Evidence artifact: eval fixture files.
- Automation location: fixture validation plus reviewer inspection.
- Required by milestone: M1

T6. Both-output trigger boundary
- Covers: R26, R30, E4, EC4
- Level: integration
- Command IDs: CMD1
- Fixture/setup: Both-output scenario in one or both fixtures.
- Steps: Include "Create flashcards and a quiz" prompt.
- Expected result: Expected behavior requires separate contracts and separate canonical JSON payloads.
- Failure proves: Combined requests may collapse into an unapproved broad skill behavior.
- Evidence artifact: eval fixture files.
- Automation location: fixture validation plus reviewer inspection.
- Required by milestone: M1

T7. Flashcard prompt contract inspection
- Covers: R1, R3-R5, R8-R15, R35
- Level: manual
- Command IDs: CMD2, CMD6
- Fixture/setup: `skills/flashcard-generator/SKILL.md`
- Steps: Inspect frontmatter, `$ARGUMENTS`, `## Output Format`, objective extraction, knowledge map, card types, validation checks, and output sections.
- Expected result: Prompt matches spec and line count is within approved limits.
- Failure proves: Flashcard prompt does not implement the behavioral contract.
- Evidence artifact: M2 review notes or change metadata.
- Automation location: prompt inspection and validator.
- Required by milestone: M2

T8. Quiz prompt contract inspection
- Covers: R2-R4, R6, R8-R11, R16-R20, R35
- Level: manual
- Command IDs: CMD2, CMD6
- Fixture/setup: `skills/quiz-generator/SKILL.md`
- Steps: Inspect frontmatter, `$ARGUMENTS`, `## Output Format`, objective extraction, quiz blueprint, MCQ rules, validation checks, and output sections.
- Expected result: Prompt matches spec and line count is within approved limits.
- Failure proves: Quiz prompt does not implement the behavioral contract.
- Evidence artifact: M2 review notes or change metadata.
- Automation location: prompt inspection and validator.
- Required by milestone: M2

T9. Flashcard manual smoke
- Covers: R9-R15, E1
- Level: manual
- Command IDs: none
- Fixture/setup: Fictional idempotency note from the proposal.
- Steps: Run or inspect expected output behavior for Anki-style flashcards.
- Expected result: Output includes objectives, knowledge map or compact equivalent, atomic source-grounded cards, canonical JSON, and no broad summary cards.
- Failure proves: Prompt may pass structure but fail intended learning behavior.
- Evidence artifact: `docs/changes/2026-07-04-flashcard-and-quiz-skills/post-change-evidence.md`
- Automation location: manual smoke or prompt-inspection proof.
- Required by milestone: M3

T10. Quiz manual smoke
- Covers: R16-R20, E2, EC3
- Level: manual
- Command IDs: none
- Fixture/setup: Fictional idempotency note from the proposal.
- Steps: Run or inspect expected output behavior for diagnostic quiz and MCQ quality.
- Expected result: Output includes blueprint, objectives, mixed cognitive levels, answer key, rationales, feedback, and clear MCQ distractors.
- Failure proves: Prompt may pass structure but fail intended diagnostic behavior.
- Evidence artifact: `docs/changes/2026-07-04-flashcard-and-quiz-skills/post-change-evidence.md`
- Automation location: manual smoke or prompt-inspection proof.
- Required by milestone: M3

T11. Both-output fallback proof
- Covers: R26, E4, EC4
- Level: manual
- Command IDs: none
- Fixture/setup: Combined flashcard and quiz request.
- Steps: Inspect prompt behavior or smoke output for separate sections and separate JSON payloads.
- Expected result: Shared objectives/knowledge map may be reused, but outputs remain contract-separated.
- Failure proves: Fallback collapses into an unapproved combined skill.
- Evidence artifact: `docs/changes/2026-07-04-flashcard-and-quiz-skills/post-change-evidence.md`
- Automation location: manual smoke or prompt-inspection proof.
- Required by milestone: M3

T12. Reference file and schema presence
- Covers: R21-R25
- Level: integration
- Command IDs: CMD2
- Fixture/setup: New skill directories.
- Steps: Confirm local learning-design references, skill-specific quality references, and schema files exist.
- Expected result: Files exist and are referenced by skill prompts as needed.
- Failure proves: Progressive-disclosure assets are missing.
- Evidence artifact: M2 diff and validation ledger.
- Automation location: prompt inspection plus validator for referenced files where applicable.
- Required by milestone: M2

T13. Reference-schema-only and no-integration boundary
- Covers: R25, R33, AC10, AC12, EC6
- Level: manual
- Command IDs: CMD2
- Fixture/setup: Full M2 diff.
- Steps: Inspect for absence of validator changes, CI changes, direct AnkiConnect/LMS API calls, runtime dependencies, non-empty tool permissions, and executable schema validation.
- Expected result: Schemas are reference contracts only and no forbidden integration is added.
- Failure proves: First slice exceeded approved architecture and implementation scope.
- Evidence artifact: M2 review notes or post-change evidence.
- Automation location: reviewer inspection plus git diff.
- Required by milestone: M2

T14. README synchronization
- Covers: R31, AC3, AC11
- Level: integration
- Command IDs: CMD4
- Fixture/setup: README after adding skill directories.
- Steps: Run README sync helper.
- Expected result: Skill table and slash-command lists include both new skills.
- Failure proves: Public docs drifted from installed skills.
- Evidence artifact: change metadata validation ledger.
- Automation location: `tests/check_readme_sync.py`
- Required by milestone: M2

T15. High-stakes and privacy boundary inspection
- Covers: R32-R34, EC7
- Level: manual
- Command IDs: CMD2
- Fixture/setup: New prompts, references, evals, and docs.
- Steps: Inspect for no guarantees, source-grounding boundaries, sanitized examples, no secrets, and no private paths.
- Expected result: Skills preserve uncertainty and privacy boundaries.
- Failure proves: Learning skills could overclaim or expose unsafe examples.
- Evidence artifact: M2/M3 review notes or post-change evidence.
- Automation location: manual inspection plus validator.
- Required by milestone: M2

## Fixtures and data

Fixtures use fictional or sanitized short notes about idempotency, authentication/authorization, retries, and OAuth. No secrets, private local paths, unpublished personal data, or real high-stakes exam content are allowed.

## Mocking/stubbing policy

No external services are called. Eval fixtures are static reviewer evidence and do not run live model calls. Manual smoke may use a capable local assistant host, but absence of live model execution does not block deterministic validation.

## Migration or compatibility tests

No data migration applies. Compatibility proof is README sync, validator pass, no installer changes, no CI changes, no existing skill changes, and no runtime dependency changes.

## Observability verification

No runtime observability applies. Review evidence must identify which requirement, fixture, prompt section, or command proves each behavior.

## Security/privacy verification

T15 verifies no secrets, private paths, unpublished personal data, direct external-service use, or high-stakes guarantee language. Fixtures remain fictional or sanitized.

## Performance checks

No runtime performance checks apply. CMD6 supports prompt length awareness.

## Manual QA checklist

- MP1: Inspect flashcard output workflow for objective extraction, knowledge map, atomicity, and canonical JSON.
- MP2: Inspect quiz output workflow for blueprint, cognitive distribution, MCQ quality, answer key, rationales, and feedback.
- MP3: Inspect unsupported-material handling for inference marking and no fabricated source-grounded claims.
- MP4: Inspect both-output fallback for separate contracts and JSON payloads.

## What not to test and why

- Do not test AnkiConnect, LMS APIs, QTI, H5P, Moodle, or external export tools; they are out of scope.
- Do not test executable JSON Schema validation; schemas are reference-only in this slice.
- Do not run live model calls in CI; static eval fixtures and manual evidence are the accepted proof surfaces.
- Do not test existing skills except through broad validator and unit discovery to detect accidental drift.

## Uncovered gaps

None requiring return to spec or architecture. Future executable schema validation, direct integrations, sync tooling, or high-stakes exam-prep policy require separate proposal/spec work.

## Next artifacts

1. `test-spec-review` result.
2. Implementation M1.
3. Code-review M1.
4. Implementation M2.
5. Code-review M2.
6. Implementation M3.
7. Code-review M3.
8. Explain-change, verify, and PR handoff after implementation gates close.

## Follow-on artifacts

None yet

## Readiness

Active proof surface after `docs/changes/2026-07-04-flashcard-and-quiz-skills/reviews/test-spec-review-r1.md`. Implementation may start with M1 only after that review is approved and recorded.
