# Spec Review R1: Editor skill optimization

## Result

- Skill: spec-review
- Review status: changes-requested
- Material findings: F-SPEC-EDITOR-001, F-SPEC-EDITOR-002
- Recording status: recorded
- Recording blocker: none
- Review record: `docs/changes/2026-05-25-editor-skill-optimization/reviews/spec-review-r1.md`
- Review log: `docs/changes/2026-05-25-editor-skill-optimization/review-log.md`
- Review resolution: `docs/changes/2026-05-25-editor-skill-optimization/review-resolution.md`
- Open blockers: F-SPEC-EDITOR-001, F-SPEC-EDITOR-002
- Immediate next stage: empty until spec revision

## Findings

## Finding F-SPEC-EDITOR-001

- Finding ID: F-SPEC-EDITOR-001
- Severity: major
- Location: `specs/editor-skill-optimization.md`, `EC9`
- Evidence: The accepted proposal preserves translation value for Chinese, English, and Russian and adds a targeted Russian translation eval. The current spec edge case says a user asking for a target language outside Chinese, English, or Russian should be translated "if the model can reasonably do so," while also saying the change does not expand trigger metadata. That creates an untestable and partially out-of-scope behavior surface.
- Required outcome: Keep this slice's translation contract bounded to the languages and targeted-Russian scenario accepted by the proposal, or explicitly specify how unsupported target languages behave without requiring implementation to guess.
- Safe resolution path: Replace `EC9` with a bounded behavior such as: "User asks for a target language outside Chinese, English, or Russian. The skill may provide a best-effort translation only if it can do so confidently, but this behavior is not part of the acceptance contract; otherwise it asks a concise clarification or says the optimized contract covers Chinese, English, and Russian." Do not add new acceptance criteria for unsupported languages in this slice.
- needs-decision rationale: none

## Finding F-SPEC-EDITOR-002

- Finding ID: F-SPEC-EDITOR-002
- Severity: major
- Location: `specs/editor-skill-optimization.md`, `Next artifacts`
- Evidence: The spec lists `specs/editor-skill-optimization.test.md` immediately after spec review and puts the execution plan after approved spec and test spec. The project workflow guide routes non-trivial work through planning before `test-spec`, and the user previously clarified that the next repository stage after spec review should be `plan`, not `test-spec`.
- Required outcome: Align the spec's downstream artifact sequence with the repository workflow so downstream agents do not skip plan review.
- Safe resolution path: Replace `Next artifacts` with: `1. spec-review for this spec. 2. Execution plan for the accepted editor optimization slice. 3. plan-review. 4. specs/editor-skill-optimization.test.md after plan review.` Keep this spec at draft until a clean spec-review rerun approves it.
- needs-decision rationale: none

## Review Dimensions

| Review dimension | Verdict | Notes |
|---|---|---|
| requirement clarity | concern | Core requirements are clear, but EC9 creates an ambiguous unsupported-language behavior. |
| normative language | concern | Most MUST/SHOULD/MAY language is testable enough; EC9's "if the model can reasonably do so" is not. |
| completeness | pass | Normal, indirect, translation, misuse, empty input, ambiguity, rollback, and validation behavior are covered. |
| testability | concern | Accepted scenarios are testable; unsupported-language behavior is not currently bounded for tests. |
| examples | pass | Examples match the proposal and cover the key behavior modes. |
| compatibility | concern | Runtime compatibility is handled, but downstream artifact routing conflicts with local workflow. |
| observability | pass | Baseline, post-change evidence, eval fixtures, and validation output are specified. |
| security/privacy | pass | Sanitized eval data and integrity-boundary behavior are specified. |
| non-goals | pass | Scope excludes high-risk skills, live model CI, tools, renaming, and broad validator changes. |
| acceptance criteria | pass | Acceptance criteria cover the intended output contract and validation commands. |

## Eventual test-spec readiness

conditionally-ready after spec revision. The behavior contract is mostly testable, but `test-spec` should wait until F-SPEC-EDITOR-001 and F-SPEC-EDITOR-002 are resolved and a clean spec-review rerun approves the spec.

## Stop condition

Revise the spec to bound unsupported-language translation behavior and correct the downstream artifact order, then rerun `spec-review`.
