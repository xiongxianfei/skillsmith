# Skillsmith maintenance workflow

## Purpose and authority

This guide tells a maintainer how to develop a reviewed change and where its knowledge belongs. [CONSTITUTION.md](../CONSTITUTION.md) owns policy; [VISION.md](../VISION.md) owns product identity. [Requirements](../design/requirements/rigorloop-v2-adoption.md), [logical behavior](../design/system/maintenance-workflow.md) and [architecture](../design/architecture/maintenance-workflow.md) explain the adopted process.

The v2 policy takes effect when this adoption is accepted and merged. This adoption finishes under prior governance, with attributed reviews and evidence in [its handoff](https://github.com/xiongxianfei/skillsmith/pull/37). Installing adapters does not approve or complete a change.

## Choose the scope

After adoption, new non-trivial standard-workflow work uses a CLI-managed Change. Begin with `route`: inspect the request, authority, accepted basis, outstanding issues and current next action. Create a Change only for authorized work, using the explicit project root and a stable Change ID.

An explicitly isolated skill invocation or small editorial correction may stay outside the store. Report its limited scope and checks; do not claim full-workflow completion. If managed delivery later relies on that output, select it into the appropriate requirement or design basis and obtain applicable review.

Historical work is not bulk imported. On resumption, inspect its actual state, preserve unknown hosted CI or review status, and record outstanding obligations and applicability of old judgments. An old “approved” or “branch-ready” note is not current whole-change approval.

## Stages and gates

| Work | Required outcome before downstream reliance |
| --- | --- |
| `requirement-analysis`, `requirement-review` | Observable obligations and Scenarios, with independent requirement assessment |
| `system-design`, `architecture-design`, `design-review` | Logical behavior and responsibility/Interface allocation, assessed together independently |
| `plan`, `delivery-review` | Stable milestones, dependency/recovery intent and concrete verification allocation, independently assessed |
| `implement` | All authorized milestones and scoped checks completed; issues remain visible |
| `code-review` | One independent whole-change gate covering the entire delivered scope; corrections reassessed within that gate |
| `verify` | Distinct final assessment of current basis, applicable reviews, evidence and remaining obligations |
| `pr` | Separately authorized publication/handoff through the repository's PR-to-main process |

Use supporting exploration/research to resolve uncertainty at its owning stage. A change to an obligation returns to requirements; a change to logical behavior returns to system design; allocation or Interface changes return to architecture design. No mandatory code-review gate is added per milestone. Optional interim advice does not advance formal approval.

Reviews identify the actual reviewer, subjects, findings and applicability. The reviewer must not be the author of the subjects being approved. A saved record proves persistence, not independence, engineering correctness or permission. Keep final Verify separate from authoring and Code Review; never repair something and silently verify your own correction.

## Artifact ownership

| Meaning | Owner |
| --- | --- |
| Durable policy and product identity | `CONSTITUTION.md`, `VISION.md` |
| Needs, obligations, Scenarios, acceptance and allocated requirements | `design/requirements/` |
| Features, Functions, behavior and model-owned test intent | `design/system/` |
| Modules, Interfaces, allocation and realization | `design/architecture/` |
| Stable delivery intent and proof allocation | `docs/plans/<date>-<slug>.md`; detailed proof maps may remain in local ignored `docs/changes/` |
| Current managed goal, authority, selected basis, work, issues, judgments and next action | Supported CLI context for the explicitly selected Change |
| Local workflow records | Ignored `docs/changes/<id>/`; files already tracked on `main` remain historical |
| Reviewer-visible acceptance/evidence account | PR description with exact subjects, actual judgments, checks, limitations and accessible source references |
| Navigation and prior plan history | `docs/plan.md`, `docs/plan-archive.md` |

Start at the [design index](../design/README.md). Amend an existing owner rather than adding a competing definition. Immutable source history and PR evidence support review without local records or the operational store; they are not a second writable work queue. Historical source/test documents retain their original scope and do not certify current code.

## Maintainer setup

The pinned tool is `@xiongxianfei/rigorloop@2.0.0`. Its package requires Node `>=24.15.0 <25`, a qualified SQLite `>=3.51.3` build and Linux filesystem primitives. Safe installation requires accessible `/proc/self/fd` descriptors and hard-link support. These are maintenance prerequisites; product prompt use, `install.sh` and Python validation do not require Node or RigorLoop.

With nvm already installed, select the qualified Node version used for this adoption:

```bash
nvm install 24.22.0
nvm use 24.22.0
node -p 'JSON.stringify({node:process.versions.node,sqlite:process.versions.sqlite})'
npx --yes @xiongxianfei/rigorloop@2.0.0 init codex --dry-run --json
npx --yes @xiongxianfei/rigorloop@2.0.0 init codex
npx --yes @xiongxianfei/rigorloop@2.0.0 capabilities --root .
```

Preview makes no destination writes, acquires no archive and reserves no later result. Inspect conflicts before the real install. `--force` replaces whole destination skill directories and retains originals at reported private locations outside discovery; it is not a merge. Symlinks/unsafe paths or intervening changes stop affected installation. Inspect partial results before retrying. Replacing an earlier workflow is a separate explicit operation; consult installed help rather than deleting unrelated skills.

Codex adapters go into ignored `.agents/skills/`. The repository tracks `.rigorloop.json` with schema version 1 and one stable project UUID; reuse it across checkouts. `.rigorloop/` is ignored and contains operational state and selected attachments. Do not regenerate identity to bypass a missing or incompatible store.

## Read and update current work

Use the pinned command above for each CLI invocation (or an executable confirmed to be version 2.0.0). Read installed help and the packaged `targeted-recording-v2` and `rigorloop-records-v4` schemas before constructing JSON.

```bash
npx --yes @xiongxianfei/rigorloop@2.0.0 change context --root . --change CHANGE_ID --format json
npx --yes @xiongxianfei/rigorloop@2.0.0 change update --root . --change CHANGE_ID --input - --format json < update.json
```

Creation supplies intent, request, authority, activity and next action with `expected_revision: null`. Updates use the opaque revision returned by fresh inspection. Never invent a token, edit private storage, or equate an empty comparison list with unchanged engineering files. Only actual reviewers supply judgments.

On stale revision, reread context and reconcile the intended change. After interruption or lost output, inspect before retrying; the first mutation may have committed. Incompatible or unavailable storage blocks affected recording and must be reported. Do not fall back to SQL or private-file editing.

## Transfer and recovery

Before transfer, save necessary current evidence and unresolved issues through supported tasks. Keep new detailed workflow records local under ignored `docs/changes/`. Publish a sanitized account in the PR: scope, exact basis, attributed review/verification outcomes, checks, limitations and how to obtain necessary operational continuity. Label it an inspection-time snapshot, not current authority. Do not add new `docs/changes/` files to Git or move workflow logs into another tracked directory. Existing tracked historical records are preserved until separately scoped removal. A clean checkout must navigate durable definitions without depending on local records. Do not commit secrets or the private runtime store.

When continuity is needed, use `store backup` with the separately versioned `store-maintenance-v1` schema. The output path must be absent and outside the live runtime directory. Example input:

```json
{"schema_version":1,"interface":"store-maintenance-v1","input":{"scope":{"changes":"all"},"output":"../skillsmith-backup","actor":{"id":"maintainer","role":"human"}}}
```

Pass that input to `npx --yes @xiongxianfei/rigorloop@2.0.0 store backup --root . --input - --format json`. Retain its returned integrity value and access instructions privately. Restore requires the backup path and integrity, explicit observed target state, `replace`, actor and reason. Inspect installed `store restore --help` and its schema; preview before restoring an existing store. Do not copy a live WAL database manually.

Restore creates a fresh store incarnation. Read context and use its new revisions before continuing; recovered storage does not renew approval or grant authority. Capabilities reports interrupted maintenance; only its supported observed-state finish/rollback procedure may resolve it. If no usable backup exists, record lost evidence as a gap instead of reconstructing approvals. The adoption's historical [disposable fixture](https://github.com/xiongxianfei/skillsmith/blob/230c4de32289abc8a883bab86ba744e9f4009d32/docs/changes/2026-10-18-rigorloop-v2-adoption/cli_fixture.py) exercises preview, stale-update rejection and backup/restore without touching the project store.

## Validation and handoff

Run `python tests/validate_skills.py` for every change. Run targeted tests appropriate to affected behavior; use `python -m unittest discover tests` and `python tests/check_readme_sync.py` when their surfaces are affected. Report warnings, skipped checks, unresolved questions and limitations. Static fixture validation does not prove model output quality.

Final completion, PR, merge and release are separate outcomes. Preserve useful selected evidence and deferred work without treating it as a waiver of mandatory acceptance.
