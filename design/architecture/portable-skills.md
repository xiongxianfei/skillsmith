# Portable skill architecture

## Scope and basis

This current architecture reconciles the preserved pure-prompt boundary with current editor amendments and existing catalog/validation implementation. It describes the documented editor, menu-advisor, learning-artifact and skill-quality subjects; it does not invent full design coverage for every catalog entry. [The design index](../README.md) identifies the remaining coverage boundary.

Normative contracts live in `design/requirements/`; logical Functions live in `design/system/`. The earlier editor architecture and diagrams remain historical source evidence under the expert-quality change, whose original bilingual-output pipeline is not the current editor contract.

## Responsibility and allocation

| Module | Responsibility and owned information | Primary Function allocation | Exclusions |
| --- | --- | --- | --- |
| MOD-PROMPT — Author portable prompt behavior | Authored skill instructions, output templates and local reference assets; the host interprets the plain Markdown | FN-ED-001–004, FN-MENU-001–003, FN-LEARN-001–004 | No hidden runtime generation, database, service or implicit tool permission |
| MOD-QUALITY — Check repository structure | Deterministic validator, fixture checks and catalog synchronization checks; checked-in fixtures/baseline | FN-QUALITY-001–002 | No live model CI or automatic claim of subjective prompt quality |
| MOD-REVIEW — Assess skill quality | Actual reviewer judgments over scope, behavior evidence, safety and tradeoffs | FN-QUALITY-003 | No author self-approval or transformation of static check success into behavioral proof |

These peer responsibilities introduce no new executable modules. Existing installation remains in `install.sh`, which copies authored assets to supported destinations and does not reinterpret prompt behavior. The installer is an existing adjacent boundary, not a new Function created by this document migration.

## Interfaces and data flow

| Interface | Provider → consumer | Contract and failures |
| --- | --- | --- |
| IF-PROMPT — Portable skill invocation | MOD-PROMPT → assistant host/user | `$ARGUMENTS` supplies instructions and content; authored metadata and body specify invocation/output/safety. The host's capabilities do not expand the required prompt contract. Missing/unsafe input follows the owning skill requirements. |
| IF-STATIC — Static validation result | MOD-QUALITY → contributor and MOD-REVIEW | Repository files yield objective errors/warnings and a process exit status. Missing fixtures or catalog drift are reported; passing does not establish model behavior. |
| IF-SKILL-REVIEW — Scoped behavior assessment | MOD-REVIEW → contributor | Actual evidence, scope and requirements yield attributed findings/judgment. Missing evidence or changed subjects invalidate unsupported confidence; reviewers cannot invent model runs. |

There is no cross-skill shared mutable state. Flashcard and quiz composition can reuse an in-conversation knowledge map while producing separate outputs. Menu imagery remains optional host-provided rendering on explicit request; no service or image asset becomes a required repository dependency. The editor operates from resolved meaning to the selected visible languages, without the old mandatory hidden Chinese/English cross-check.

## Realization and development view

`skills/<name>/SKILL.md` owns product behavior. Skill-local `references/` and schema assets are authored reference data, not a generation pipeline. `tests/validate_skills.py`, `tests/check_readme_sync.py`, unit tests and `tests/evals/skills/` implement current checks and recorded expected behavior. `.github/workflows/validate.yml` runs the existing deterministic Python commands. `install.sh` owns supported installation paths and copying semantics. This migration changes none of these bytes.

The physical deployment is an installed/copy-pasted Markdown skill consumed by a user's assistant host. No product database, network endpoint, background worker or credential store exists. RigorLoop's Node/SQLite maintenance tooling is a separate development concern described in [maintenance architecture](maintenance-workflow.md), not part of skill execution.

## Scenario and verification view

An editor request follows the editor system's role/meaning/render/check flow; a menu request follows evidence/choice/consistency behavior; a learning request follows objectives, distinct artifact generation and output checking. Each uses its own requirement contract through IF-PROMPT. A contributor changes authored assets, receives IF-STATIC results and obtains IF-SKILL-REVIEW where required. The ordinary outputs, failure boundaries and test intent live in their system owners rather than in duplicated architecture diagrams.

The original 36 unit tests and catalog/eval checks remain the executable evidence. Source migration, link integrity and unchanged product bytes are separately checked by the adoption audit. Neither this view nor its existence demonstrates a new live-model evaluation.
