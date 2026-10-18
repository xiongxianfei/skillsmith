# Design index

Skillsmith ships portable Markdown prompts. This design separates what the product or maintenance process must do, its logical behavior, and where responsibilities are realized. Requirements own obligations; system design explains behavior; architecture assigns responsibility. A filename or old review does not establish current acceptance.

| Subject | Requirements | System behavior | Architecture |
| --- | --- | --- | --- |
| Skill quality and evidence | [Quality standard](requirements/skill-quality-standard.md) | [Quality process](system/skill-quality.md) | [Portable skills](architecture/portable-skills.md) |
| Editor | [Consolidated editor contract](requirements/editor.md) | [Editing and translation](system/editor.md) | [Portable skills](architecture/portable-skills.md), [editor view](architecture/views/editor.md) |
| Restaurant menu advisor | [Menu contract](requirements/restaurant-menu-advisor.md) | [Evidence and choices](system/restaurant-menu-advisor.md) | [Portable skills](architecture/portable-skills.md) |
| Flashcards and quizzes | [Learning contracts](requirements/flashcard-and-quiz-skills.md) | [Learning behavior](system/flashcard-and-quiz-skills.md) | [Portable skills](architecture/portable-skills.md) |
| Repository maintenance | [Adoption requirements](requirements/rigorloop-v2-adoption.md), [allocated obligations](requirements/rigorloop-v2-adoption-allocation.md) | [Maintenance behavior](system/maintenance-workflow.md) | [Maintenance architecture](architecture/maintenance-workflow.md) |

## Reading and changing the model

Start with the relevant requirements, then follow behavior and allocation. Original IDs remain source-qualified; for example, `editor-expert-quality-optimization:R24` is distinct from the latest editor contract's R24. The historical [migration dispositions](https://github.com/xiongxianfei/skillsmith/blob/230c4de32289abc8a883bab86ba744e9f4009d32/docs/changes/2026-10-18-rigorloop-v2-adoption/source-disposition.md) explain which clauses survive and which explicit amendments replace older behavior. Original test plans and sources remain accessible through immutable Git history. Additional local snapshots under ignored `docs/changes/` are evidence, not committed duplicate definitions. Existing records already tracked on `main` remain unchanged.

Use [the workflow guide](../docs/workflows.md) to change these owners. Plans describe delivery intent and concrete checks; they do not define a second product contract.

Focused architecture views live under `architecture/views/`. They explain selected relationships using the owning requirements, system behavior and architecture definitions, with links back to those sources. The [editor view](architecture/views/editor.md) is the first example; its logical processing flow remains in the system definition.

## Coverage limits

The migrated inventory does not contain complete requirements or detailed system designs for communicator, doctor, email-drafter, fitness-coach, journaling, language-tutor, nvc, oscp-coach, study-planner or vocabulary-mastery. Their prompts remain the observed implementation, subject to the shared quality standard and constitution. This migration does not invent approved designs for them or claim that all catalog design work is finished. A future material change must establish the missing subject contract before implementation.

The maintenance process and product design models describe accepted intent and observed boundaries; satisfaction depends on current reviews and evidence. See the [adoption handoff](https://github.com/xiongxianfei/skillsmith/pull/37) for the actual migration assessment.
