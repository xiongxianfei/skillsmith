# Skillsmith maintenance workflow design

## Status, basis and boundary

Design for the user's three-part engineering layout. Migration implementation and its acceptance evidence are recorded in the adoption handoff; independent final acceptance and publication are separate. Independent design and contributor-policy review standing is recorded in the [design review](../../docs/changes/2026-10-18-rigorloop-v2-adoption/reviews/design-review.md). This document owns responsibility, allocation and realization. Logical definitions now live in `design/system/maintenance-workflow.md`. The editor-focused [earlier architecture](../../docs/changes/2026-05-26-editor-expert-quality-optimization/sources/architecture/architecture.md) is a source to reconcile against later approved amendments, not blanket proof of current behavior.

The governing [adoption requirements](../requirements/rigorloop-v2-adoption.md) now include the requested layout and source-preservation obligation SR-RL-006; see the [requirement review](../../docs/changes/2026-10-18-rigorloop-v2-adoption/reviews/requirement-review.md) for exact assessment applicability. Earlier hashes and judgments describe earlier subjects. The architecture-level obligations are defined once in the companion [allocated requirements](../requirements/rigorloop-v2-adoption-allocation.md) and assessed with this design.

This design is a human/agent maintenance process realized by existing documents and the installed RigorLoop CLI. Its Modules are responsibility boundaries, not new services or Python packages. No product prompt, installer, validator or CI runtime change is proposed.

## Function allocation

Function definitions live in [maintenance system behavior](../system/maintenance-workflow.md). The table below owns primary Module allocation only. AR accountability stays with the allocated requirements.

| Function | Primary Module |
| --- | --- |
| FN-RL-001 | MOD-RL-001 |
| FN-RL-002 | MOD-RL-002 |
| FN-RL-003 | MOD-RL-003 |
| FN-RL-004 | MOD-RL-003 |

## Responsibility and Interface model

These three peer Modules have no parent/child hierarchy. Each has a distinct authority boundary; the same agent may perform authoring and coordination but independent review requires a different reviewer.

| Module | Accountable responsibility and state | Realization and exclusions |
| --- | --- | --- |
| MOD-RL-001 — Define maintenance obligations | Meaning, source order, scope and permitted evolution of governance, requirements, design and delivery intent | Maintainers and authoring skills edit Git-held owning definitions under review. Does not persist operational judgments on behalf of a reviewer or change product scope by installing tools. |
| MOD-RL-002 — Coordinate current work | Meaning and consistency of the current Change handoff, selected basis, pending work and issue state | `route` and supported v2 CLI tasks; CLI owns persistence in the local operational store. Does not originate reviewer judgments, invent authority or replace canonical definitions with database copies. |
| MOD-RL-003 — Assess and preserve evidence | Meaning of review/verification judgments, applicable support, selected evidence and historical acceptance accounts | Independent specialist reviewers, verifier and CLI recording/backup operations; Git-held handoff evidence where appropriate. Does not own the live work queue or treat a saved record as approval. |

The following Interfaces are process contracts, not new APIs. Each provider owns the complete stated outcomes; consumers cannot upgrade a result into stronger authority.

| Interface | Provider → consumers | Input and output contract | Consistency, failure and compatibility |
| --- | --- | --- | --- |
| IF-RL-001 — Inspect the governing basis | MOD-RL-001 → MOD-RL-002, MOD-RL-003 | Given scope and request, return owning document paths, exact inspected revisions/digests, constraints, selected definitions, source dispositions and unresolved conflicts | Tracked document contents carry meaning; filenames or Git ancestry do not imply approval. Changes to relied-on definitions require an applicability assessment. The selected layout migration reuses source obligations without inventing product behavior. |
| IF-RL-002 — Inspect the current handoff | MOD-RL-002 → MOD-RL-001, MOD-RL-003 | Given explicit project and Change identity, return goal/authority, selected basis, work, open issues, evidence, review standing, next action and current revision | Use supported context queries; never select a Change from private storage heuristics. Missing project identity, missing Change, incompatible store or ambiguous selection is reported. Revision conflicts are reconciled before mutation. |
| IF-RL-003 — Supply an attributed assessment | MOD-RL-003 → MOD-RL-002, MOD-RL-001 | Given exact subjects and basis, return actual reviewer, purpose, judgment, findings, disposition and applicability | Reviewers own judgments; coordination may record supplied facts but cannot manufacture them. Corrections require proportionate reassessment with complete affected scope. A successful save proves storage only. |
| IF-RL-004 — Supply handoff and recovery evidence | MOD-RL-003 → MOD-RL-002, external reviewers and successor agents | Given selected work and a transfer purpose, provide a sanitized acceptance/evidence account, referenced artifacts and, where operational continuity is needed, a supported backup with access instructions | A Git snapshot is historical, never a second live handoff. Unsupported restore/import or unavailable backup remains a gap. Recovering storage does not grant authority or renew judgments. |

## Development view: canonical locations

This table defines the user-selected target layout. The three `design/` roots separate engineering meaning; they are not a copy of RigorLoop's implementation or a requirement to introduce its full model hierarchy. The selected definition locations are implemented; the source-disposition record retains original identities and migration evidence. `docs/` continues to hold operating guidance, plans and historical evidence.

```text
design/
  requirements/   Needs, obligations, black-box Scenarios, acceptance, allocated requirements
  system/         Features, Functions, behavior, model-owned test intent
  architecture/   Modules, Interfaces, allocation, realization and explanatory views
docs/
  workflows.md    Contributor operating guide and links to canonical model owners
  plans/          Delivery intent and milestones
  changes/        Attributed decisions, source dispositions, reviews and historical evidence
```

| Subject | Canonical location and role | Mutation authority |
| --- | --- | --- |
| Durable governance | `CONSTITUTION.md`; `AGENTS.md` is concise agent guidance | Reviewed changes owned by MOD-RL-001; preserve the user's engineering principles |
| Project identity | `VISION.md`; README vision text derives from it | Existing vision ownership; only reconcile the argument-hint contradiction |
| Workflow entry points and artifact map | `docs/workflows.md`; contributor/setup references link to it | MOD-RL-001; replace superseded active stage instructions, preserve historical meaning |
| Requirements and Scenarios | `design/requirements/<subject>.md`; needs, obligations, black-box Scenarios and acceptance, with source-qualified IDs | MOD-RL-001; one current owner per obligation, with explicit supersession and source mapping |
| Logical behavior | `design/system/<subject>.md`; Features, Functions, behavior and model-owned test intent | MOD-RL-001; no Module or storage allocation hidden in logical behavior |
| Architecture | `design/architecture/<subject>.md`; Modules, Interfaces, Function allocation and realization | MOD-RL-001; no copied requirement statements that compete with requirement owners |
| Allocated obligations | `design/requirements/rigorloop-v2-adoption-allocation.md`, subordinate to the reviewed adoption SRs | Requirement ownership under MOD-RL-001; one accountable Module recorded per AR |
| Delivery intent | `docs/plans/<date>-<slug>.md` | MOD-RL-001; stable milestones and proof allocation, with references to current handoff |
| Current operational handoff | `.rigorloop/rigorloop.db`, using supported CLI tasks only | MOD-RL-002 owns work meaning; MOD-RL-003 owns supplied judgments and evidence meaning; CLI owns persistence |
| Stable project identity | Proposed tracked `.rigorloop.json`, schema version 1 with one generated UUID | Explicit setup for this repository; do not regenerate when switching branches/worktrees |
| Selected local attachments | `.rigorloop/artifacts/changes/`, CLI-managed | MOD-RL-003 supplies selected evidence; no manual private-store edits |
| Reviewer-facing evidence | `docs/changes/<dated-change-id>/`, including a concise `handoff.md` for managed transfers | MOD-RL-003; attributed snapshot of CLI context/judgments and selected checks, never a parallel mutable operational journal |
| Navigation and historical plans | `docs/plan.md`, `docs/plan-archive.md`, existing plans/reviews | Navigation references the relevant current owner. Preserve unknown legacy status and original records; no automatic reclassification as Done. |
| Product prompts, installation and validation | Existing `skills/`, `install.sh`, `tests/`, `.github/` | Existing owners and contracts; unchanged by this adoption |

The project map identifies the maintenance design and runtime boundary. README and CONTRIBUTING explain setup and link to the workflow guide instead of maintaining another full lifecycle. Exact current operational fields will not be copied back into plan bodies after every update. Archived plan handoffs retain their original meaning.

The migration preserves applicable obligations rather than preserving mixed document structure. Requirement examples and observable acceptance belong with requirements; logical sequencing and transformations belong with system behavior; deployment, persistence and implementation responsibility belong with architecture. Execution history and change-specific test plans belong with their historical change. After migration, new work amends the selected subject owner in `design/`; it does not recreate a `specs/` tree.

### Source-to-target migration design (historical input paths)

The inventory below covers all 16 current files in `specs/` and all five files in `docs/architecture/`. Each retained source is recorded by original repository path, Git revision/blob when tracked, and SHA-256 of the inspected bytes. The adoption's uncommitted drafts need explicit retained pre-migration bytes because Git history alone cannot recover them. The old roots are removed only after coverage and references are checked.

| Current sources | Current-model destination and disposition | Historical preservation |
| --- | --- | --- |
| `specs/rigorloop-v2-adoption.md`, `specs/rigorloop-v2-adoption-allocation.md` | Corresponding filenames in `design/requirements/`; move F-RL-001's Feature definition to `design/system/maintenance-workflow.md` and retain its requirement confirmation reference | Pre-migration draft snapshots under this adoption's `sources/`; prior review hashes stay unchanged |
| `docs/architecture/workflow.md` | Split logical definitions into `design/system/maintenance-workflow.md` and responsibility/realization into `design/architecture/maintenance-workflow.md` | Pre-migration source snapshot under this adoption's `sources/`; no old-path forwarding file |
| `specs/skill-quality-standard.md` | `design/requirements/skill-quality-standard.md`; behavior explanations needed for validation and authoring go to `design/system/skill-quality.md`; implementation boundaries go to shared `design/architecture/portable-skills.md` | Preserve original source identity and needed history under `docs/changes/2026-05-25-rigorloop-governed-skill-quality/` |
| `specs/editor-skill-optimization.md` | Explicitly superseded source; does not become a second current editor contract | Preserve with its `2026-05-25-editor-skill-optimization` change and mark navigation historical |
| `specs/editor-expert-quality-optimization.md`, `specs/editor-learning-default-optimization.md`, `specs/editor-source-plus-companion-language-optimization.md` | Reconcile into `design/requirements/editor.md` and `design/system/editor.md`; preserve effective obligations from all three, applying only their explicit supersession rules | Preserve provenance and source snapshots with their respective `2026-05-26-editor-expert-quality-optimization`, `2026-06-16-editor-learning-default-optimization` and `2026-06-16-editor-source-plus-companion-language-optimization` changes |
| `specs/restaurant-menu-advisor.md` | `design/requirements/restaurant-menu-advisor.md`, `design/system/restaurant-menu-advisor.md`; shared prompt/runtime boundary in `design/architecture/portable-skills.md` | Preserve source identity and necessary history with `2026-06-21-add-restaurant-menu-advisor` |
| `specs/flashcard-and-quiz-skills.md` | `design/requirements/flashcard-and-quiz-skills.md`, `design/system/flashcard-and-quiz-skills.md`; shared boundary in `design/architecture/portable-skills.md` | Preserve source identity and necessary history with `2026-07-04-flashcard-and-quiz-skills` |
| All seven `specs/*.test.md` files, paired with the seven product/quality sources above | Change-specific plan, coverage, case IDs and recorded status move intact to `docs/changes/<owning-change>/test-spec.md`; extract any reusable model-owned test intent to the relevant system definition, with source references | The existing owning change is retained for each file; no test execution or renewed approval is inferred from relocation |
| `docs/architecture/system/architecture.md` and its three `.mmd` diagrams | Reconcile pure-prompt responsibility and realization into `design/architecture/portable-skills.md`; effective editor logic into `design/system/editor.md`; any useful current views are derived from those owners | Retain original architecture and diagrams together under the expert-quality change's `sources/architecture/`, preserving relative relationships and labeling their historical scope |

The current editor chain demonstrates why a rename is insufficient: the learning amendment supersedes opt-in-only notes, and the source/companion amendment supersedes default visible Chinese-plus-English output and further adjusts note-count behavior. Source-qualified IDs such as `editor-expert-quality-optimization:R23` identify the original obligation, not a new global identity or compatibility alias. A clause-level map records the effective replacement and retained context. Neither latest filename nor current prompt text alone decides which requirement wins. An uncovered contradiction requires requirement-owner resolution before affected consolidation proceeds.

For each source, migration records an adoption-local `source-disposition.md` row for each substantive requirement, example, invariant, safety constraint, acceptance criterion and test-intent section: source identity/anchor, `retained`, `superseded`, `historical` or `unresolved`, target identity/anchor, and rationale/source of the disposition. Unresolved content blocks retirement of its current owner. Whole-source historical snapshots are marked non-current and preserve reviewable bytes; they are not parallel active contracts. Sources without globally unique IDs retain their original IDs with document qualification in the map.

The source-disposition map explains this transition; it is not a permanent runtime redirect table. Current navigation is rewritten to target owners. Old paths may remain in immutable quotations, original review subjects/hashes and clearly labeled historical provenance. Do not globally replace old paths inside evidence. Instead, add current navigation alongside the historical record where needed and retain original subject meaning.

### Boundary and relationship ownership

At migration, definitions are split by responsibility rather than copied:

- Requirements own IR/SR/AR statements, Scenarios, acceptance and confirmation references to Features/Functions. AR-to-Module accountability remains authored once with the AR.
- System definitions own Feature and Function meaning and Feature-to-Function realization. They link to requirement IDs without restating normative requirements as a second contract.
- Architecture owns Module/Interface definitions, Function-to-primary-Module allocation, data authority and realization. Views derive from these definitions and the referenced AR allocations.
- The maintenance table is separated accordingly: requirement confirmations, logical definitions and Module allocation now have their own owners.

The existing inventory does not define complete requirements for all 14 product skills. Migration accounts for the knowledge that exists; it must not manufacture approved requirements for undocumented skills or claim catalog-wide design completeness. Such gaps are explicitly listed in the target design index for later scoped work.

### Reference and retirement checks

The migration includes `CONSTITUTION.md`, `AGENTS.md`, `CLAUDE.md`, README, CONTRIBUTING, `docs/workflows.md`, project-map navigation, affected plans and linked design views. Update current source-order guidance to the new requirement/system/architecture owners in the same reviewed change. Preserve the user's engineering principles. Historical prose remains historical; its current clickable navigation must resolve where exposed.

Check repository-relative links and fragment anchors, source-qualified requirement references and diagram references. Search tracked files for retired paths and classify each surviving occurrence as intentional provenance or an error; an empty text search is not the objective. Verify `specs/` and `docs/architecture/` are absent, each of the 21 source files is dispositioned, every substantive clause is covered, and no shims or duplicate active definitions remain. Existing Python tests cannot establish this semantic preservation by themselves.

## Process view: routine work and transitions

For new non-trivial standard-workflow work after adoption, FN-RL-001 selects scope and existing definitions. FN-RL-002 creates or inspects a CLI-managed Change with actual authorization. Authors update owning Git definitions; independent assessors perform the applicable requirement, integrated design and delivery reviews. The recorded accepted basis points to exact subjects and actual review support. Implementation runs the allocated checks; one independent whole-change code-review gate precedes a distinct final Verify. Only supported successful final verification permits compact completion. PR delivery remains required by Skillsmith and is a separate authorized action.

An explicitly isolated task or small editorial correction can remain outside operational storage. Its output states the limited scope; it cannot claim full-workflow completion. When managed work later relies on it, the owning stage explicitly selects the output and obtains applicable review. This adoption's preparation and review artifacts are isolated work under the existing governance, not fabricated CLI records.

At each consequential transition, preserve unresolved issues and current evidence applicability. Use the inspected opaque revision for updates. On stale revision, read context again; on lost command response, inspect before retry; on storage incompatibility, stop affected recording without falling back to private-file edits. Unrelated work can continue if it does not depend on the missing state.

### Governance transition for this adoption

The old constitution remains authoritative throughout this adoption change's preparation, review and implementation. The proposed amendments take effect for new work after the adoption PR is accepted and merged. Local edits to a constitution file do not waive the review obligations governing their own delivery. The user's instruction to work in this workspace controls edit location; it does not imply push, merge or release authority.

The transition uses existing review responsibilities with explicit coverage, rather than pretending retired skill names remain installed:

| Current obligation | Concrete subject and required review coverage |
| --- | --- |
| Proposal review for contributor-policy change | The decision below, adoption scope, alternatives, vision fit, tradeoffs and governance transition; record an explicit policy/proposal assessment |
| Spec review | Approved adoption IR/SRs, Feature, Scenarios and acceptance criteria; the existing requirement review supplies the assessment but its mapping and unchanged applicability must be acknowledged |
| Architecture review | This logical/architecture design, its Interfaces, allocated obligations, state ownership and failure/recovery behavior; integrated design review supplies the assessment |
| Plan review and test specification | A subsequent delivery plan plus explicit change-local proof map under `docs/changes/<change-id>/`; review sequencing, coverage and recovery before implementation |
| Code review, rationale, verification and PR | Whole adoption diff, meaningful rationale and evidence, required checks, current governance compliance and authorized PR handoff |

A single independent reviewer may record the policy/proposal and integrated design assessments together if both purposes and actual conclusions are explicit. This is evidence reuse, not a claim that one approval automatically satisfies every gate. Missing required coverage remains outstanding.

### Adoption decision and alternatives

Selected direction: use the pinned v2 skills and CLI for new managed work, with the user-selected three-part `design/` model and portable product boundaries. Preserve applicable knowledge and source identities while removing obsolete current representations. This fits Skillsmith's vision because it improves reviewability without making product execution dependent on a vendor runtime.

Keeping only the old workflow would preserve familiarity but leave installed skills and governing instructions inconsistent. Keeping the old definition paths was previously selected, but the user has now explicitly required the three-part design model. A bulk folder rename would retain mixed responsibilities and editor contradictions. Copying RigorLoop's full tooling hierarchy or importing every historical operational record remains unnecessary. The selected approach consolidates current engineering definitions, preserves historical evidence and leaves operational-record import separate. It adds a source/coverage audit to migration, without adding product runtime dependencies.

Before touching a historical active entry, inspect its owner and available evidence. An old PR reference or presence on main does not prove final closeout. Unresolved entries remain visibly legacy/unverified with a source pointer; if work resumes under v2, create a current Change with explicit outstanding obligations and reassess prior support. No bulk import is selected for this adoption. Future qualified imports require their own inspected source and supported CLI maintenance procedure.

## Physical realization and evidence continuity

The selected development tool is `@xiongxianfei/rigorloop@2.0.0`, installed through its verified Codex adapter. Use a supported Node 24 build (`>=24.15.0 <25`) with SQLite 3.51.3 or later and Linux filesystem prerequisites. The current machine's Node upgrade and adapter installation are setup evidence only; implementation must inspect CLI capabilities in the intended environment. Product validation remains Python-based, and ordinary skill users need none of this tooling.

The `.rigorloop.json` identity is shared through Git. The `.rigorloop/` directory is ignored and remains local to a checkout. A fresh clone has definitions and selected historical evidence but no resumable operational store until one is deliberately created or restored. Keep per-checkout runtime stores distinct; do not symlink live databases between worktrees. Git-held adoption artifacts remain usable without access to runtime state.

For active managed-work transfer, FN-RL-004 writes a concise, sanitized `handoff.md` with the Change identity, governing subject revisions/digests, scope and authority, unresolved issues, actual reviewer attribution/judgments, validation commands/results, and references to necessary supporting artifacts. Mark its captured revision and snapshot status. A reviewer with only Git can inspect the delivered scope and support; a successor who needs to update the same operational Change also needs a supported backup. Do not commit raw runtime storage, credentials, unsanitized logs or a full private backup.

Use `rigorloop store backup` with an explicit external destination, through the pinned CLI and its current schema. Retain a backup at active-work transfer and before store maintenance. Report its path to the authorized recipient through the available handoff channel without making private machine paths part of public docs. Verify backup creation and inspect returned integrity metadata. Restore only after inspecting destination capabilities and expected store identity, with the supplied backup observation and explicit replacement authorization where applicable. Inspect context after restore and obtain fresh revision tokens before any update. Never copy a live WAL database manually.

If the local store is lost and no usable backup exists, Git evidence supports inspection, not reconstruction of current approvals. A successor records the gap, establishes a new explicit Change if needed, and obtains current assessments before relying on a basis. For completed work, the sanitized final acceptance account and selected proof remain in Git; complete runtime history is not required. No automatic backups, cloud storage or new synchronization service are introduced.

## Scenario view and acceptance intent

These are design walkthroughs derived from the requirements' black-box Scenarios and the Function/Interface definitions above; they are not executed acceptance tests.

| Scenario | Normal participation and result | Alternative and failure paths |
| --- | --- | --- |
| SC-RL-001 — Start work | FN-RL-001 resolves IF-RL-001; FN-RL-002 establishes IF-RL-002 for managed work; IF-RL-003 supplies actual review support before downstream reliance | An editorial/isolated task stops at its limited output. Conflicting guidance blocks dependent routing until MOD-RL-001 corrects it. |
| SC-RL-002 — Resume legacy work | FN-RL-001 selects applicable historical definitions; FN-RL-002 records explicit disposition and gaps; FN-RL-003 assesses current support | An unknown hosted result stays unknown. Unsupported import is not attempted. Review findings remain open until actually dispositioned. |
| SC-RL-003 — Use a product skill | FN-RL-001 respects product scope; FN-RL-003 checks the adoption diff and existing product checks | Any prompt/installer drift returns to its owner; product users continue the existing install or copy-paste path without Node or RigorLoop. |
| SC-RL-004 — Review or recover work | FN-RL-003 supplies IF-RL-003; FN-RL-004 supplies IF-RL-004 with review-visible proof and supported recovery where needed | Missing evidence or incompatible restore is reported. A Git snapshot does not masquerade as current context; failed checks prevent success claims. |
| SC-RL-005 — Find current engineering meaning | FN-RL-001 follows IF-RL-001 from the requirement owner to logical behavior and architectural accountability; FN-RL-004 retains historical source meaning through IF-RL-004 | Explicit supersession selects the effective obligation; an unresolved clause blocks affected consolidation. Historical test plans remain evidence, not current acceptance or operational state. |

The Logical view is the Function/Module/Interface model; the Development view is its location mapping; Process and Physical views explain the selected execution and persistence realization. The Scenario table projects those same definitions without adding another owner. These prose/table views are authored together in this document; no generated website or separate diagram system is needed. Independent review must assess whether a maintainer can locate an owner, identify the record writer, follow each Scenario's failure path and distinguish historical evidence from live state. A structural link check cannot prove comprehension or successful recovery.

## Implementation boundaries and remaining work

Implementation will migrate the 21 inventoried definition/proof/architecture files by the reviewed source map, amend current governance and references, configure the development-only project identity/ignore boundary, and establish the documented handoff convention. It will not alter product code, introduce database access in tests, indiscriminately delete historical evidence, or rewrite the user's local commits. Definition relocation is distinct from operational lifecycle closeout; unknown historical status remains unknown.

The amended design and delivery plan were independently reviewed before implementation. The remaining clause-level source-disposition work is an explicit migration proof obligation; the file-level design does not claim that consolidation has already occurred. Delivery planning must allocate proof for all six SRs and companion ARs, including definition/anchor preservation, absence of old roots, and a disposable CLI create/context/update and backup/restore exercise. Required project validation remains unchanged. Review covers the expanded policy direction and integrated design; no implementation or governance adoption is claimed by this document.
