# Portable skill architecture

## Scope and basis

Skillsmith combines practice skills with shared methods and tools for making better skills. It distributes authored Markdown prompts; an external assistant host interprets them. The shared platform supports authoring, evaluation and distribution. It is not a service called during skill invocation.

The [architecture index](README.md) identifies current C4 coverage and historical sources. Subject specifications hold behavior, constraints and design decisions together. The [quality standard](../../docs/skill-quality-standard.md) owns repository-wide authoring and evidence obligations.

Skill distribution uses **portable Agent Skills directory packages**. The Markdown entrypoint `skills/<name>/SKILL.md` owns behavior, with optional `references/`, `scripts/`, `assets/`, or custom directories. Explicitly documented local dependencies are allowed for optional or necessary operations when the selected host can access and execute them. Do not introduce hidden runtime dependencies, implicit permissions, generated prompt behavior, or external services. Validation remains in `tests/validate_skills.py`, installation in `install.sh`, and repository CI in `.github/`.

## Responsibility and allocation

The retained MOD/IF identifiers name responsibilities and contracts, not executable services.

| Responsibility | Owned information and realization | Boundary |
| --- | --- | --- |
| MOD-PROMPT — Author portable behavior | `skills/<name>/SKILL.md` and skill-local references/schemas; the [editor](editor-c4/architecture-spec.md) and [vocabulary](vocabulary-mastery-c4/architecture-spec.md) specifications describe invocation behavior | No generated prompt behavior, implicit tool permission or shared mutable learner state |
| MOD-QUALITY — Check required files and metadata | One Python validator for readable skill files, Agent Skills name/description constraints and supported optional metadata shape | Static success does not demonstrate host compatibility or model behavior |
| MOD-REVIEW — Assess skill quality | Reviewer findings about behavior, safety, evidence and tradeoffs, recorded in the PR | No invented model runs or author self-approval |

## Interfaces and data flow

| Interface | Flow and contract | Failure boundary |
| --- | --- | --- |
| IF-PROMPT — Skill invocation | Authored prompt plus user input → assistant host → user-visible response | Missing or unsafe input follows the skill's instructions; host capability does not grant additional permissions |
| IF-STATIC — Validation result | Repository files → required-file and metadata checks → contributor/reviewer | Missing/unreadable files or invalid defined metadata fail; body structure, host execution compatibility and behavioral quality require review |
| IF-SKILL-REVIEW — Behavior assessment | Changed prompt, requirements and actual evidence → reviewer findings → contributor | Unexecuted scenarios are expectations, not observed results |

## Realization and development view

`install.sh` copies complete skill directories to the selected destination. Agent Skills-compatible hosts may read bundled references and assets or invoke documented local scripts. Copying `SKILL.md` into a plain chat may provide only partial functionality; this is no longer the portability guarantee. Skillsmith supplies no application server, background worker, credential store or learner database. The host's implementation, privacy policies and retention are external and must not be invented by these designs.

`tests/validate_skills.py` supplies the single automated check for required files and Agent Skills metadata. `.github/workflows/validate.yml` runs that command. README synchronization and behavior assessment belong to review; older scenario declarations remain accessible through fixed Git references in the subject specifications. D2 is architecture tooling only; it adds no dependency to skill invocation or existing CI. Maintainers follow the [workflow guide](../../docs/workflows.md), using C4 for design.

## Behavior and evidence boundaries

Editor policy is detailed in its C4 specification: separate instructions from source, preserve meaning, select visible languages and ground learning notes in available evidence. Vocabulary policy is detailed in its specification: one lexical target, a shared sense map, two complete language versions and aligned recall tasks.

Other existing skill boundaries remain relevant even without dedicated C4 packages. Menu advice uses supplied evidence, qualifies allergy uncertainty, stops for active emergencies and only requests illustrative imagery when explicitly requested and supported by the host. Flashcard and quiz skills can share conversational source analysis while keeping distinct outputs; their schemas do not create an LMS integration or a scheduling service. Their original detailed contracts and test intent remain linked from the architecture index.

Future changes must inspect the owning prompt and relevant historical constraints, document the intended behavior in the relevant C4 specification, and supply evidence under the quality standard. Diagram validity and metadata checks do not establish linguistic accuracy, safety in execution or learning effectiveness.

## Retained design rationale

These decisions explain existing boundaries; they do not add new product behavior or transfer old approvals to the C4 designs.

- **Separate flashcard and quiz contracts:** retention practice and diagnostic assessment need different selection criteria, output shapes and quality checks. Both extract learning objectives and a knowledge map before generating artifacts. Combined requests reuse that analysis while retaining separate Markdown sections and JSON payloads, including a bounded fallback when composition is unavailable. Markdown supports human review; canonical JSON supports downstream export. Skill-local learning references preserve independent installation, and the JSON Schemas document outputs without claiming executable validation. See the [original learning-skill decisions](https://github.com/xiongxianfei/skillsmith/blob/00224740db8a8e18e10579d8b38377ef0c1b04cf/docs/proposals/2026-07-04-flashcard-and-quiz-skills.md#decision-log).
- **Portable menu visualization:** a text visual brief works without a required image tool or vendor API. Optional generated images are illustrations, never evidence of actual ingredients, portions, preparation or plating. Allergy uncertainty needs high-risk safety evidence because false reassurance can cause harm. See the [original menu decisions](https://github.com/xiongxianfei/skillsmith/blob/00224740db8a8e18e10579d8b38377ef0c1b04cf/docs/proposals/2026-06-21-add-restaurant-menu-advisor.md#decision-log).
- **Objective validation and separate review:** required-file and metadata checks are deterministic; trigger quality and safety require review. The earlier fixture/grandfathering system, README checker and formatting restrictions have been retired in favor of one required-file and metadata validator and manual review. See the [original quality decisions](https://github.com/xiongxianfei/skillsmith/blob/00224740db8a8e18e10579d8b38377ef0c1b04cf/docs/proposals/2026-05-25-rigorloop-governed-skill-quality.md#decision-log); the current [quality standard](../../docs/skill-quality-standard.md) owns the effective obligations.
