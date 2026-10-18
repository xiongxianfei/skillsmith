# RigorLoop v2 adoption allocated requirements

## Status and ownership

Architecture-level obligations, amended for the selected three-part engineering layout; see the [integrated design review](../../docs/changes/2026-10-18-rigorloop-v2-adoption/reviews/design-review.md) for assessment applicability. Implementation and satisfaction remain pending. This companion belongs to the requirement model governed by [the amended adoption requirements](rigorloop-v2-adoption.md). It adds no new stakeholder need or System Requirement; AR-RL-006 and AR-RL-007 derive from the new SR-RL-006. Module and Function definitions are allocated in [the workflow design](../architecture/maintenance-workflow.md); logical meanings live in `design/system/maintenance-workflow.md`.

Each AR below has one parent SR and one accountable Module. The allocation is authored only here; the design refers to it rather than duplicating it. Statements and acceptance are proposed obligations, not satisfaction claims. The tables account for What, Why, Who, When, Where, How and How much for every AR.

## AR-RL-001 — Publish the effective stage and authority rules

Parent: SR-RL-001. Accountable Module: MOD-RL-001.

The definition owner MUST publish the effective lifecycle and its governance transition at the current owning guidance, with distinct review, verification and publication responsibilities. Adoption preparation MUST retain the existing review obligations until its amendments take effect.

| What | Why | Who | When | Where | How | How much |
| --- | --- | --- | --- | --- | --- | --- |
| Remove conflicting active routing | Prevent self-approving migration | Maintainers and definition authors | Adoption and subsequent routing | Constitution and linked workflow guidance | Explicit effective boundary and old-to-new review coverage | One current lifecycle and no implicit waiver |

Acceptance: inspect current guidance and the adoption review map together; each current obligation has an actual owning assessment before it is replaced. Confirm isolated work cannot claim full workflow completion.

## AR-RL-002 — Preserve explicit work-state authority

Parent: SR-RL-002. Accountable Module: MOD-RL-002.

The coordination owner MUST write managed handoffs only through supported CLI tasks using inspected current revisions. New or resumed work MUST retain explicit basis selection, unresolved issues and historical dispositions. Navigation and stable plans MUST NOT become competing writable current handoffs.

| What | Why | Who | When | Where | How | How much |
| --- | --- | --- | --- | --- | --- | --- |
| Maintain one current work account | Avoid stale or conflicting continuation | Coordinating agents | Creation, transition, resumption and retry | Selected project and Change | Explicit scope, supported tasks and revision reconciliation | One current owner per Change; retain every unresolved material issue |

Acceptance: demonstrate managed versus isolated routing and a stale/interrupted update response without blind replay. Inspect a legacy resumption example whose unknown prior outcome remains unknown.

## AR-RL-003 — Assess the preserved product boundary

Parent: SR-RL-003. Accountable Module: MOD-RL-003.

The evidence owner MUST compare the adoption diff against the selected baseline and report any product contract change or unrelated edit. Readiness MUST NOT be claimed when adoption changes product behavior without separately reviewed scope.

| What | Why | Who | When | Where | How | How much |
| --- | --- | --- | --- | --- | --- | --- |
| Detect product and local-work drift | Protect existing users and user changes | Reviewer and verifier | Whole-change review and final verification | Actual diff and current product checks | Scoped file/behavior comparison and existing validation | Zero intended product behavior changes; acknowledge existing warnings |

Acceptance: skill, installer and validator behavior are unchanged; check results and preserved user work are reported. Runtime tooling is absent from ordinary skill execution and Python validation dependencies.

## AR-RL-004 — Document reproducible maintainer setup

Parent: SR-RL-004. Accountable Module: MOD-RL-001.

The definition owner MUST provide version-pinned maintainer setup, runtime/platform prerequisites, conflict and preview behavior, and distinguish installation from adoption. Contributor-facing policy MUST follow canonical optional-frontmatter and catalog ownership.

| What | Why | Who | When | Where | How | How much |
| --- | --- | --- | --- | --- | --- | --- |
| Make supported setup and policy discoverable | Prevent incompatible tooling and stale instructions | Maintainers and contributors | Onboarding or upgrade | Workflow guide with concise entry-point links | Pin v2.0.0, state prerequisites and derive summaries from owners | One setup authority; no duplicated catalog count or mandatory argument hint |

Acceptance: documentation names the exact package and supported environment; the installer preview has no destination writes; active documents agree on optional metadata. Product users are not directed to install maintenance dependencies.

## AR-RL-005 — Retain sufficient transferable evidence

Parent: SR-RL-005. Accountable Module: MOD-RL-003.

The evidence owner MUST provide a sanitized Git-held account sufficient to inspect delivered scope and judgments without the live store. When operational continuation is required, it MUST also identify a supported backup/recovery path, distinguish missing state from acceptance, and obtain fresh context after recovery.

| What | Why | Who | When | Where | How | How much |
| --- | --- | --- | --- | --- | --- | --- |
| Preserve inspectable and recoverable proof | Git does not carry ignored local state | Reviewers, verifier and successor agents | Active transfer, maintenance and completion | Selected Git evidence and private supported backup | Attributed snapshots, backup integrity and supported restore | Necessary judgments, issues and proof; no secrets or full private store in Git |

Acceptance: a Git-only reviewer can inspect scope, basis, outcomes, warnings and limitations; a disposable backup/restore exercise recovers selected context using fresh revision tokens. Missing or unusable backup is surfaced without inventing recovered approvals.

## AR-RL-006 — Reconcile current engineering owners

Parent: SR-RL-006. Accountable Module: MOD-RL-001.

The definition owner MUST classify current requirements, system behavior and architecture into the three selected roots, preserving identity and one current owner per meaning. It MUST account for substantive source clauses and apply explicit supersession evidence before retiring old paths. Current guidance, references and fragments MUST resolve to the selected owner without old-path shims.

| What | Why | Who | When | Where | How | How much |
| --- | --- | --- | --- | --- | --- | --- |
| Separate and reconcile engineering meanings | A folder rename can preserve contradictions and duplicate owners | Definition authors and reviewers | Before retirement of old definition roots | Three design roots and current navigation | File inventory, clause dispositions, source-qualified IDs and explicit supersession | All inventoried sources and substantive clauses covered; no unresolved retirement or duplicate current owner |

Acceptance: migration maps every source to its destinations and dispositions, resolves the editor amendment chain explicitly, repairs current links/anchors and removes `specs/` and `docs/architecture/` without shims. Product behavior and test execution remain unchanged.

## AR-RL-007 — Preserve migration evidence without renewing approval

Parent: SR-RL-006. Accountable Module: MOD-RL-003.

The evidence owner MUST retain original source identities, historically relied-on bytes and judgment meaning while exposing new navigation. Uncommitted reviewed drafts MUST have recoverable pre-migration snapshots. Historical proof plans and snapshots MUST be labeled non-current, and changed subjects MUST receive applicable reassessment rather than inheriting approval from a moved filename.

| What | Why | Who | When | Where | How | How much |
| --- | --- | --- | --- | --- | --- | --- |
| Keep migration provenance and proof interpretable | Rewrites can invalidate hashes or make old judgments look current | Reviewers and evidence maintainers | Migration, reassessment and historical access | Change-local source snapshots, test plans and review records | Preserve original subject/hash and bytes; add current navigation separately | All evidence relied on for the migration remains attributable; no invented re-verification |

Acceptance: a reviewer can inspect the original source supporting a retained or superseded clause, including uncommitted drafts, and distinguish current definitions from historical source/test plans. Historical subject hashes are not globally rewritten. A moved test plan is not reported as a newly executed test.

## Coverage and limits

The parent SRs remain authoritative for the full obligations. ARs narrow accountability where the design introduces a boundary; they do not repeat every system-level constraint. No additional hierarchy, service, product runtime or custom persistence API is required. Review assesses these obligations together with their allocated Functions, Interfaces and realization before delivery planning.
