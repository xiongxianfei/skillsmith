# Portable skill architecture

## Scope and basis

Skillsmith combines practice skills with shared methods and tools for making better skills. It distributes authored Markdown prompts; an external assistant host interprets them. The shared platform supports authoring, evaluation and distribution. It is not a service called during skill invocation.

The [architecture index](README.md) identifies current C4 coverage and historical sources. Subject specifications hold behavior, constraints and design decisions together. The [quality standard](../../docs/skill-quality-standard.md) owns repository-wide authoring and evidence obligations.

## Responsibility and allocation

The retained MOD/IF identifiers name responsibilities and contracts, not executable services.

| Responsibility | Owned information and realization | Boundary |
| --- | --- | --- |
| MOD-PROMPT — Author portable behavior | `skills/<name>/SKILL.md` and skill-local references/schemas; the [editor](editor-c4/architecture-spec.md) and [vocabulary](vocabulary-mastery-c4/architecture-spec.md) specifications describe invocation behavior | No generated prompt behavior, implicit tool permission or shared mutable learner state |
| MOD-QUALITY — Check repository structure | Python validators, README synchronization checks and static eval fixtures | Static success does not demonstrate model behavior |
| MOD-REVIEW — Assess skill quality | Reviewer findings about behavior, safety, evidence and tradeoffs, recorded in the PR | No invented model runs or author self-approval |

## Interfaces and data flow

| Interface | Flow and contract | Failure boundary |
| --- | --- | --- |
| IF-PROMPT — Skill invocation | Authored prompt plus `$ARGUMENTS` → assistant host → user-visible response | Missing or unsafe input follows the skill's instructions; host capability does not grant additional permissions |
| IF-STATIC — Validation result | Repository files → validation commands → contributor/reviewer | Errors and warnings remain distinct; missing fixtures and catalog drift are reported |
| IF-SKILL-REVIEW — Behavior assessment | Changed prompt, requirements and actual evidence → reviewer findings → contributor | Unexecuted scenarios are expectations, not observed results |

## Realization and development view

`install.sh` copies authored assets to the selected destination. Installed or copy-pasted skills run through the user's assistant host. Skillsmith supplies no application server, background worker, credential store or learner database. The host's implementation, privacy policies and retention are external and must not be invented by these designs.

`tests/validate_skills.py`, `tests/check_readme_sync.py`, unit tests and `tests/evals/skills/` supply deterministic checks and expected scenarios. `.github/workflows/validate.yml` runs repository checks. D2 is architecture tooling only; it adds no dependency to skill invocation or existing CI. Maintainers follow the [workflow guide](../../docs/workflows.md), using C4 for design.

## Behavior and evidence boundaries

Editor policy is detailed in its C4 specification: separate instructions from source, preserve meaning, select visible languages and ground learning notes in available evidence. Vocabulary policy is detailed in its specification: one lexical target, a shared sense map, two complete language versions and aligned recall tasks.

Other existing skill boundaries remain relevant even without dedicated C4 packages. Menu advice uses supplied evidence, qualifies allergy uncertainty, stops for active emergencies and only requests illustrative imagery when explicitly requested and supported by the host. Flashcard and quiz skills can share conversational source analysis while keeping distinct outputs; their schemas do not create an LMS integration or a scheduling service. Their original detailed contracts and test intent remain linked from the architecture index.

Future changes must inspect the owning prompt, fixtures and historical constraints, document the intended behavior in the relevant C4 specification, and supply evidence under the quality standard. Diagram validity and static fixtures do not establish linguistic accuracy, safety in execution or learning effectiveness.
