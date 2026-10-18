# RigorLoop v2 adoption requirements

## Status and scope

Requirement basis for the reviewed three-part design migration. See the review record for exact subject applicability and historical judgments. Independent review and applicability are recorded in the [requirement review](../../docs/changes/2026-10-18-rigorloop-v2-adoption/reviews/requirement-review.md). This is an isolated requirement-analysis output, not evidence of completed adoption. The current constitution and workflow remain governing until their amendments are reviewed and accepted through the existing process.

The requested outcome is to use RigorLoop v2.0.0 to improve Skillsmith's maintenance workflow. This change covers explicit workflow adoption, the documentation inconsistencies discovered during assessment, and the subsequently requested migration of engineering definitions from `specs/` and `docs/architecture/` into `design/requirements/`, `design/system/` and `design/architecture/`. Finish and review this migration design before moving existing artifacts. Product prompts, validation logic, installation behavior and catalog scope remain unchanged; behavioral changes need their own concrete requirements.

This document owns the proposed adoption requirements. Existing product requirements remain in their current owning specs. No new directory hierarchy, runtime database, or project configuration is created by this analysis.

## Request and governing basis

The source request in this conversation was: “Please use rigorloop v2.0.0 to refactor the repository.” The user subsequently authorized the Node upgrade, installation after removing the old adapter, and proceeding with the proposed adoption requirement analysis. This is authority to prepare the requirement basis; it is not review approval, merge authority, or a release request.

The user then directed: “We need to finish design work firstly. Remove specs/ to design/requirements/, design/architecture, design/system.” This selects the target model locations and prioritizes design completion. It supersedes the earlier design choice to retain the old definition paths, not the obligations to preserve meaning, evidence, product behavior and local work.

Applicable project sources:

- [Constitution](../../CONSTITUTION.md): source order, portable prompts, written requirements, review obligations, verification and PR handoff.
- [Vision](../../VISION.md): reusable prompt skills and simple, portable contributor tooling.
- [Skill quality standard](skill-quality-standard.md): required structure, optional-frontmatter policy, eval evidence, safety and deterministic validation.
- [Workflow guide](../../docs/workflows.md): current artifact ownership and the older lifecycle.
- [Contributor guidance](../../CONTRIBUTING.md), [project map](../../docs/project-map.md), and [plan index](../../docs/plan.md): current entry points and historical handoffs.

Version-pinned upstream basis:

- [RigorLoop v2 route](https://github.com/xiongxianfei/rigorloop/blob/v2.0.0/skills/route/SKILL.md).
- [RigorLoop v2 operational and installation contract](https://github.com/xiongxianfei/rigorloop/blob/v2.0.0/packages/rigorloop/README.md).
- [Requirement Analysis method](https://github.com/xiongxianfei/rigorloop/blob/v2.0.0/rem/methods/requirement-analysis.md) and [5W2H](https://github.com/xiongxianfei/rigorloop/blob/v2.0.0/rem/methods/5w2h.md).

The v2 package and its adapter are development tools. Installing them does not adopt their governance, migrate records, or approve engineering work.

## Observed baseline and reconciliation

Analysis initially started from remote main commit `3475b48e37d6f2b8ca14241bf60ab7755648753a` in an isolated worktree. At the user's explicit instruction to work directly in the current workspace, this draft was moved to the original workspace on local main at `e3ab8b3`. That local commit adds engineering principles to `AGENTS.md`; it remains intact and is part of the current working basis. Subsequent edits will use this workspace. This location change does not itself authorize pushing, merging or publishing.

| Request or finding | Disposition |
| --- | --- |
| Traceable, reviewable maintenance | Refine the constitution's existing maintenance need for v2; do not create a second product vision. |
| Portable Markdown, public skill behavior, installer compatibility and safety | Reuse existing constitution and skill-quality obligations unchanged. |
| v2 lifecycle and operational records | New migration obligations under the existing maintenance need. |
| Three-part `design/` layout and removal of `specs/` | Extend the same maintenance need with SR-RL-006 and SC-RL-005. Separate obligations, logical behavior and architecture by meaning; map all existing sources before migration. |
| `VISION.md` requires an argument hint | Correct lower-priority guidance to match the existing optional-frontmatter policy; do not change skill contracts. |
| `AGENTS.md` says 10 skills; baseline contains 14 | Remove the stale fixed count or derive it from the catalog, without duplicating another hand-maintained total. |
| Historical plans still list active closeout states | Classify with actual evidence; do not infer completion from age, presence on main, or installed tooling. |
| Nine grandfathered skills lack eval fixtures | Acknowledge the existing non-blocking warning. Broad eval backfill is outside this adoption change. |
| General repository refactoring | Defer until a specific problem, intended behavior and assessment criteria are established. |

## Requirement terms and identity

An Initial Requirement (IR) states a stakeholder need. A System Requirement (SR) states an assessable obligation derived from that need. A Feature is a durable stakeholder capability; a Scenario describes one concrete use of that capability. These identifiers are scoped to this adoption basis and remain stable if files or titles change.

### IR-RL-001 — Continue repository maintenance with trustworthy evidence

Maintainers and coding agents need to start, resume, review and verify Skillsmith changes using a consistent workflow, while preserving product compatibility, prior evidence and the authority of project governance.

This refines the existing constitution's maintenance intent. It does not replace that constitution. IR-RL-001 confirms Feature F-RL-001 and Scenarios SC-RL-001 through SC-RL-005 for this proposed basis; confirmation of their analysis relationships is not requirement approval.

| 5W2H question | Analysis |
| --- | --- |
| What | Installed v2 tooling and tracked v1-era guidance describe different maintenance workflows; mixed legacy documents also obscure the owners of current requirements, behavior and architecture. |
| Why | Conflicting routing can lose evidence, apply obsolete gates, or misrepresent approval and completion. |
| Who | Maintainers, contributors, coding agents and reviewers; product users depend on compatibility. |
| When | At explicit adoption and whenever subsequent work starts, resumes, reaches review or is handed off. No delivery deadline was supplied. |
| Where | Skillsmith's development workflow, engineering definitions and documented contributor entry points. |
| How | Adopt the selected v2 contract and the requested three-part design layout explicitly, retain established product rules, and reconcile prior state with evidence. Detailed design follows review. |
| How much | One adoption and definition-migration change; all existing spec/architecture sources are accounted for, without prompt rewrites, new product runtime, or fabricated approval conversion. |

Open questions: none at the need level. Detailed ownership and record-retention decisions remain design obligations below.

### Feature confirmation

IR-RL-001 confirms F-RL-001, defined in [maintenance system behavior](../system/maintenance-workflow.md).

## Stakeholder scenarios

All five scenarios are confirmed for analysis, owned by IR-RL-001, and exercise only F-RL-001. They describe observable outcomes without selecting internal architecture.

| ID | Actor, context and trigger | Interaction and expected outcome | Alternative, failure and recovery | Informs |
| --- | --- | --- | --- | --- |
| SC-RL-001 | Contributor starts a non-trivial change after adoption; current project guidance is available. | Contributor follows the documented entry point and obtains the applicable requirement basis, review obligations and next action. | A small editorial task retains its documented proportional path. Contradictory guidance is surfaced before dependent work proceeds and corrected by its owner. | SR-RL-001, SR-RL-004 |
| SC-RL-002 | Another agent resumes work whose earlier handoff or evidence was produced under the older workflow. | Agent inspects provenance, unfinished obligations and actual judgments, and can distinguish historical evidence from current authority. | Missing evidence remains unknown; the agent identifies the missing proof and preserves the original meaning rather than marking work complete. | SR-RL-002, SR-RL-005 |
| SC-RL-003 | A product user installs or copies a skill after the contributor workflow changes. | The user receives the same skill names, input and output contracts, safety boundaries and supported installation behavior. | The user can use portable prompts without installing the maintenance workflow. Product behavior drift blocks adoption acceptance and is corrected or scoped separately. | SR-RL-003 |
| SC-RL-004 | Reviewer receives a proposed adoption change with local validation evidence. | Reviewer can inspect the exact requirement basis, changed files, test results, warnings and review judgments. | A failing check, lost local record or unavailable CI result is stated as such. Work resumes from recoverable evidence; unsupported readiness claims are withdrawn. | SR-RL-001, SR-RL-002, SR-RL-005 |
| SC-RL-005 | Contributor needs to understand or revise a skill governed by several older documents after reorganization. | Contributor can find the current obligation, corresponding behavior and responsible implementation boundary, and trace each back to its source. | An explicit supersession is honored; an unresolved contradiction stays visible and blocks the affected consolidation. Historical test evidence remains attributable without being presented as current approval. | SR-RL-006 |

## System requirements

All SRs below have exactly one parent: IR-RL-001. Their statements and acceptance criteria are proposed obligations, not claims of satisfaction. Functions and allocated requirements are intentionally left to subsequent system and architecture design.

### SR-RL-001 — Publish one governing workflow

After adoption, current guidance MUST consistently identify the v2 dependency chain: requirement analysis, requirement review, system and architecture design, integrated design review, plan, delivery review, implementation with required checks, independent whole-change code review, and distinct final verification. Skillsmith MUST retain PR delivery to main. Passing installation, recording or schema checks MUST NOT imply approval, and final verification MUST remain distinct from external publication.

| What | Why | Who | When | Where | How | How much |
| --- | --- | --- | --- | --- | --- | --- |
| Reconcile conflicting lifecycle instructions | Prevent incorrect routing and completion claims | Contributors and reviewers | Adoption and subsequent changes | Current governance and contributor guidance | Amend owning guidance through current rules; retain proportional isolated work | One current chain; one independent whole-change code-review gate; separate final Verify |

Acceptance: inspect constitution, workflow guide, agent/contributor guidance and applicable templates together. No current instruction routes new work to retired stages. Historical examples are clearly historical. SC-RL-001 and SC-RL-004 can be walked through without inventing approval. The adoption review explicitly addresses the old constitution's proposal/spec/architecture/plan review obligations before those rules are amended; new stage names do not silently waive existing gates.

### SR-RL-002 — Separate current work from historical evidence

The adopted guidance MUST identify one authority for each current requirement, design, delivery plan and operational handoff. After adoption takes effect, new non-trivial work coordinated through the standard workflow MUST use a CLI-managed Change for current operational state; supported CLI operations MUST own its writes. An explicitly isolated skill task or small editorial correction MAY remain outside Change-managed coordination and MUST report its bounded scope without claiming full-workflow completion. Isolated output that later becomes a dependency of managed work MUST be explicitly adopted into that work's requirement or design basis and receive applicable review.

Historical files MUST retain provenance and original judgment meaning; they MUST NOT automatically become current approvals. Before historical work resumes under v2 coordination, its current handoff MUST explicitly identify outstanding obligations, evidence gaps and disposition of prior judgments. Archival work that is not resumed does not require bulk import. Active-index changes MUST cite evidence or explicitly preserve unknown status. Superseded current guidance MUST be reconciled without retaining competing active owners.

| What | Why | Who | When | Where | How | How much |
| --- | --- | --- | --- | --- | --- | --- |
| Define ownership and transition semantics | Prevent conflicting state and lost history | Maintainers and resuming agents | Adoption, resumption and record migration | Engineering definitions, operational records and historical references | Record explicit dispositions; use supported recording boundaries | Every affected owner has one current role; no bulk deletion or automatic approval conversion |

Acceptance: a reviewer can locate the current owner and retained historical source for each affected artifact type. Walk through a new non-trivial workflow change, an isolated requirement analysis, and a small editorial correction: the first has a CLI-managed Change; the latter two may remain isolated and make no full-workflow completion claim. If isolated output is subsequently used in managed delivery, its adoption and required review are observable in that work's basis. A historical record with unknown hosted review/CI remains unknown unless evidence resolves it. An unsupported legacy import is reported without conversion. SC-RL-002 demonstrates this distinction. Exact locations and any import qualification are reviewed design decisions, not settled by this document.

### SR-RL-003 — Preserve product contracts and local work

Adoption MUST preserve published skill names, metadata/body rules, input/output contracts, safety boundaries, installer commands and supported destinations. It MUST NOT add RigorLoop, Node, SQLite, network services or model calls as dependencies of ordinary product skill execution or existing Python validation. Unrelated local changes MUST remain intact.

| What | Why | Who | When | Where | How | How much |
| --- | --- | --- | --- | --- | --- | --- |
| Preserve existing product and worktree boundaries | Keep contributor tooling changes from breaking users or losing work | Product users and maintainers | Throughout adoption | Catalog, installer, checks and local work | Reuse current constitution and quality standard; compare actual diff | No intended product behavior change; no unrelated edits |

Acceptance: compare the adoption diff with its base for product files, installation guidance and validation behavior; any semantic change requires separate scope. Run the existing checks. No live-model evaluation is required because prompts are unchanged; static validation does not prove model output quality. SC-RL-003 remains valid. Preserve the independent `AGENTS.md` principles commit and any concurrent user work.

### SR-RL-004 — Make setup and policy guidance reproducible

Setup guidance MUST pin RigorLoop 2.0.0 and state its supported Node 24 range (`>=24.15.0 <25`) and applicable platform prerequisites. It MUST distinguish installing development tools from adopting project governance. Current documents MUST consistently follow the constitution's optional-frontmatter policy and MUST avoid stale hand-maintained catalog counts. No global Node upgrade MUST be required of ordinary skill users.

| What | Why | Who | When | Where | How | How much |
| --- | --- | --- | --- | --- | --- | --- |
| Explain repeatable setup and resolve observed policy drift | Prevent unsupported installations and contradictory contributor instructions | Workflow adopters and skill authors | Setup and contribution | Development setup and owning policy documents | Pin the package, explain preview/conflict behavior and derive summaries from owners | One documented supported version and no contradictory required argument hints |

Acceptance: a contributor can distinguish preview, actual installation, adoption and historical migration. Existing installation conflicts are surfaced rather than blindly overwritten. Inspect current guidance for mandatory `argument-hint` statements and stale fixed counts; historical evidence retains its original wording. Check README synchronization after any derived text changes.

### SR-RL-005 — Keep review evidence recoverable

The adoption MUST define how selected operational evidence survives local-state loss and remains available to another reviewer or agent. Completion evidence MUST include the delivered scope, actual judgments, validation results, warnings, unresolved issues and applicable recovery instructions. Ignored local storage alone MUST NOT be the only accessible basis for a PR readiness claim. Credentials and private local data MUST NOT be committed as evidence.

| What | Why | Who | When | Where | How | How much |
| --- | --- | --- | --- | --- | --- | --- |
| Make evidence usable across sessions and reviewer environments | Local SQLite records do not automatically travel with Git | Reviewers, maintainers and successor agents | Handoff, backup/recovery and completion | Selected operational evidence and reviewer-facing handoff | Choose supported backup/export or a sufficient reviewed acceptance account during design | Retain necessary proof and attribution, not every action; no invented retention deadline |

Acceptance: demonstrate SC-RL-004 with a reviewer who has the repository and declared handoff materials but not the author's live runtime store. The reviewer can find the scope, outcomes and limitations. Recovery of Change-managed runtime storage uses supported CLI operations; direct SQL editing or copying a live WAL database is not a documented recovery mechanism. Lost or unavailable evidence is marked as a gap.

### SR-RL-006 — Separate engineering definitions without losing meaning

The repository MUST use `design/requirements/` for needs, obligations, constraints, black-box Scenarios and acceptance criteria; `design/system/` for stakeholder Features, logical Functions, behavior and model-owned test intent; and `design/architecture/` for responsible Modules, Interfaces, allocation and realization. Allocated Requirements remain in the requirement model and reference their one accountable architectural Module. The `specs/` and `docs/architecture/` directories MUST be removed after their contents and references have been reconciled. No forwarding files, symlinks or duplicate current owners are introduced at the retired paths.

The migration MUST preserve every substantive obligation or record an explicit source-backed supersession, historical disposition or unresolved conflict. Requirement IDs MUST remain stable where the meaning is unchanged; repeated local IDs from different old documents MUST retain source qualification. Historical review hashes, quoted source paths and judgments MUST retain their original meaning. Current navigation MUST resolve to the new owner or an explicitly historical retained artifact. Existing test plans and evidence MUST NOT be mistaken for newly executed checks or deleted because they are not current system design.

| What | Why | Who | When | Where | How | How much |
| --- | --- | --- | --- | --- | --- | --- |
| Separate mixed engineering knowledge | Make current ownership and supersession understandable | Contributors, reviewers and maintainers | Design, migration and later changes | The three user-selected design directories and historical evidence | Reconcile by meaning, preserve identity/provenance and repair current references | Account for every existing spec, test-spec and architecture source; zero unintended product changes |

Acceptance: a source-to-destination inventory covers all existing `specs/*` and `docs/architecture/*` files. A clause-level disposition map accounts for requirements, examples, safety boundaries, acceptance and proof intent, including conflicting editor amendments. Each active obligation has one current owner; every retained historical artifact is clearly non-current. Current links, fragment references and source-order guidance resolve correctly. `specs/` and `docs/architecture/` are absent at migration completion. Scenario SC-RL-005 and existing project checks pass without product changes. The migration cannot be called complete while conflicts or unclassified substantive content remain.

## Remaining design decisions and boundaries

These are required downstream decisions, not unknown requirement meanings:

- Define subject-level files and relationships within the three selected design roots, while retaining suitable plan, operational-record and review-evidence locations. Resolve the migration inventory before deleting old roots.
- Define the transition boundary for existing work and the evidence-retention/recovery procedure. Do not assume the old filesystem records qualify for v2's supported import.
- Define the explicit governance amendment and review mapping that satisfies current rules before the new rules take effect.

No system Functions, architecture Modules, storage schemas or delivery milestones are approved here. The requested three design roots do not require copying RigorLoop's tooling, schemas or full model hierarchy into Skillsmith.

## Verification intent

The adoption must retain and run these existing checks:

```bash
python -m unittest discover tests
python tests/validate_skills.py
python tests/check_readme_sync.py
```

Review additionally covers the SR acceptance criteria, scenario walkthroughs, current-owner consistency, historical dispositions, product diff boundaries and evidence access. Do not claim these semantic obligations pass solely because the existing Python checks pass. Node or adapter installation checks are separate setup evidence and do not prove governance adoption.

Current delivery evidence and historical analysis are linked from the [adoption handoff](../../docs/changes/2026-10-18-rigorloop-v2-adoption/handoff.md).

## Confirmed logical behavior

The following relationships are authored here once; Function meanings live in the system model.

| Function | Confirming SRs |
| --- | --- |
| FN-RL-001 | SR-RL-001, SR-RL-003, SR-RL-004, SR-RL-006 |
| FN-RL-002 | SR-RL-001, SR-RL-002 |
| FN-RL-003 | SR-RL-001, SR-RL-003, SR-RL-005 |
| FN-RL-004 | SR-RL-002, SR-RL-005, SR-RL-006 |
