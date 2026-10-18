# RigorLoop v2 adoption delivery plan

## Purpose / big picture

Deliver the reviewed three-part engineering model and RigorLoop maintenance guidance without changing product prompts, installer behavior or existing validation. Work directly in the current workspace as requested. Preserve the user's committed engineering principles and existing untracked cache files.

## Current Handoff Summary

This adoption is delivered under the pre-adoption governance. Its current evidence and outcomes are in `docs/changes/2026-10-18-rigorloop-v2-adoption/handoff.md`; no v2 approvals are invented for preparation performed outside a managed Change. Future managed changes use the CLI handoff after adoption takes effect. The plan owns stable delivery intent, not an independently writable live status journal.

## Source artifacts

- Requirement basis: `specs/rigorloop-v2-adoption.md`, SHA-256 `54162a6af84886d584f482c47cba831293769197827487d491ced583ef83188f`, approved amendment review.
- Reviewed design: `docs/architecture/workflow.md`, SHA-256 `624e94dd6c5a396f85717befe03aa6e1951b4c8ed999956b9c2338426f6de233`.
- Allocated requirements: `specs/rigorloop-v2-adoption-allocation.md`, SHA-256 `cd6315a7bf8ceb430e795a7fc686b6467a6cb65b756674c2a9161faff96b5b50`.
- Review records: this change's requirement/design reviews. These old paths identify the reviewed pre-migration subjects; current navigation after migration is through `design/README.md` and the source-disposition record.
- Proof map: this change's `test-spec.md`, reviewed with this plan under the existing plan/test-spec responsibilities.

## Context and non-goals

There are 16 spec/test-spec and five architecture source files. Seven test specs describe historical delivery checks; four editor specs include explicit supersessions. The migration must preserve source bytes and meaning, not simply rename directories. No product skill, installer, original test or CI behavior changes; no forced historical completion, global search-and-replace of evidence, push, merge or release.

## Milestones

### M1. Preserve sources and establish migration proof

- Kind: implementation. Covers SR-RL-002/003/006 and AR-RL-006/007.
- Responsibility: definition and evidence owners. Dependency: independently reviewed delivery basis.
- Scope: snapshot all 21 sources and hash the unchanged product boundary; write a source/paragraph disposition manifest and repeatable migration audit.
- Proof TG-1: source snapshots match initial SHA-256; every paragraph has an explicit disposition, destination and rationale; no unexplained obligation is labeled historical. A deliberately missing source/destination or altered retained clause must fail the audit in a disposable copy.
- Completion: recoverable source bytes and a baseline against which later moves are checked. Expected pre-migration audit failure: retired roots still exist and destination definitions are absent.
- Recovery: restore only this task's moved files from verified snapshots. Do not reset the repository or revert user work. Evidence contributes to the final whole-change gate, not a milestone approval.

### M2. Reconcile and relocate engineering definitions

- Kind: implementation. Covers SR-RL-003/006 and all migration ARs. Dependency: M1.
- Scope: create requirement/system/architecture owners; consolidate editor obligations using explicit amendments; preserve source-qualified IDs; move seven historical test plans into their owning changes; retain original architecture/diagrams as historical sources. Separate the maintenance Feature/Functions from Module/Interface allocation.
- Proof TG-2: requirement-level editor disposition includes effective target clauses and rejected superseded defaults; retained source clauses match their targets or have a reviewed semantic mapping. All 21 source files and substantive content are accounted for. Current definitions have one owner; unknown product-design gaps remain explicit.
- Completion: `specs/` and `docs/architecture/` absent, current local links/fragments resolve, old-path occurrences are classified as provenance or corrected. Product-boundary hashes unchanged.
- Recovery: correct individual mappings or restore affected sources from M1 while preserving unrelated files. Do not claim completion while any migration conflict remains unresolved.

### M3. Align governance, setup and evidence handoff

- Kind: implementation. Covers SR-RL-001/002/004/005 and applicable ARs. Dependency: M2 canonical paths.
- Scope: update constitution, concise agent/contributor guidance, workflow guide, README and project map; correct optional argument hints and fixed skill count; retain existing engineering principles. Add tracked stable project identity and ignore local runtime state. Provide handoff and recovery instructions.
- Proof TG-3: verify managed/isolated task routing, old-to-new review coverage, source order and navigation; unknown historical lifecycle entries remain unknown. Run the pinned installer `init codex --dry-run --json` in a disposable project and compare the destination tree before/after: require a successful preview result and no destination writes. Separately run CLI create/context/update, stale-revision rejection, backup and restore; verify restored context and fresh revisions. A Git-only reader can inspect this change's selected evidence without a live store.
- Completion: coherent guidance, reproducible supported runtime exercise, no Node dependency in product execution or Python checks. Adoption rules take effect only through the accepted governance amendment; local edits do not waive this change's current gates.
- Recovery: fixture failures remain isolated; do not restore over a live store. Revert only newly authored setup/configuration if its design is invalid. Never hand-edit private storage or invent CLI judgments.

## Final review checkpoint

After all milestones and required corrections, obtain one independent whole-change Code Review of actual documents, migration proof, tests and configuration, then distinct final Verify. Review corrections return to their owner and receive affected reassessment. No mandatory per-milestone code-review gates. Record durable change rationale before final verification. PR delivery remains outstanding until actually authorized/prepared and performed; do not imply merge or release authority.

## Change-level verification and commands

TG-FINAL-1 combines TG-1/2/3: a maintainer can navigate effective editor obligations through behavior and architecture, inspect exact historical sources, and distinguish current handoff from evidence. Run:

```bash
PYTHONDONTWRITEBYTECODE=1 python -m unittest discover tests
PYTHONDONTWRITEBYTECODE=1 python tests/validate_skills.py
PYTHONDONTWRITEBYTECODE=1 python tests/check_readme_sync.py
python -B docs/changes/2026-10-18-rigorloop-v2-adoption/check_migration.py
git diff --check
```

Existing static eval checks do not prove model output quality. No live-model claim or test is needed when product prompts remain byte-identical. Capture exact fixture commands/results separately; qualification must be observed, not inferred from documentation. Report warnings and skipped hosted checks.

## Risks, dependencies and rationale

Main risks are silently losing inherited editor obligations, making historical approvals look current, broken relative links and a database-dependent handoff inaccessible to reviewers. Source snapshots, clause dispositions, explicit review attribution, current-link auditing and a Git-held acceptance account address those risks. Missing local Node/CLI capability blocks the fixture, not permission to weaken the required proof. Review the actual remainder of unresolved evidence before claiming completion. The selected source layout and review policy come from the reviewed design, not this plan.

## Readiness

Delivery review is recorded in the change directory. Its exact inspected subjects and judgment determine implementation readiness; this plan does not approve itself.
