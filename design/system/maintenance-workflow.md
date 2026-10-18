# Maintenance system behavior

This file owns the logical capability and Functions. [Requirements](../requirements/rigorloop-v2-adoption.md) own their obligations and confirmation relationships; [architecture](../architecture/maintenance-workflow.md) owns allocation and realization.

### F-RL-001 — Maintain changes through an inspectable workflow

Maintainers and agents can determine the governing requirements, current work, unresolved issues, review standing, evidence and next permitted action. Reviewers can assess the delivered change without depending on inaccessible chat history. The capability covers engineering work and handoff; it excludes skill execution, hosting services and autonomous publication.

## Functions

F-RL-001 is realized by FN-RL-001 through FN-RL-004. These are logical process responsibilities, not new runtime services.

| Function | Inputs and conditions | Behavior and output | Failure and responsibility boundary |
| --- | --- | --- | --- |
| FN-RL-001 — Resolve applicable engineering obligations | Request, project governance, existing definitions and actual authorization; starting, resuming or reorganizing work | Determine managed versus isolated scope; select and reconcile requirement, behavior and architecture owners with source provenance; identify the next permitted stage and its actual review dependencies | Missing or conflicting authority or substantive content remains explicit and blocks dependent consolidation. Routing never supplies approval or edits product contracts implicitly. Ends at a scoped direction and selected basis. |
| FN-RL-002 — Maintain a resumable work account | Selected work, current handoff, attributable decisions and observed changes; a managed Change is selected or explicitly being created | Preserve current scope, authority, accepted bases, progress, issues, evidence references and next action; reconcile historical work before resuming | Unknown prior outcomes remain unknown. A concurrent update or interrupted response requires inspection before retry. Ends at an accurate account, not approval or verification. |
| FN-RL-003 — Assess obligations and delivered evidence | Exact subjects, governing basis, appropriate independent reviewer or verifier, applicable check results | Produce attributed judgments, findings, dispositions and separate final verification; detect changed or missing support before reuse | An author cannot independently approve their own subjects; stale support requires reassessment. Passing checks alone cannot approve a design. Ends at an actual scoped judgment. |
| FN-RL-004 — Retain and present selected evidence | Work account, judgments, source identities and sanitized supporting artifacts; migration, transfer, recovery or completion | Produce a sufficient reviewer-facing account, preserve source meaning and provenance, and retain recoverable operational state where needed; expose limitations and recovery prerequisites | Inaccessible or lost evidence is a gap, not a reconstructed approval. Relocation does not renew a historical judgment. Recovery never silently reuses stale update tokens. Ends at recoverable evidence and truthful access instructions. |

## Test intent

Walk managed and isolated work, legacy resumption with unknown evidence, stale updates, independent assessment, Git-only review, and recovery after local-state loss. The adoption proof map allocates concrete checks; this logical definition does not claim they have run.
