# Source dispositions

## Scope and method

This migration preserves the exact 21 pre-migration sources below. SHA-256 values in [migration-manifest.json](migration-manifest.json) identify their bytes; tracked inputs also have the recorded baseline commit. Source paths below are historical identities, not current navigation. Snapshots, historical test plans and old reviews do not create another active contract or renew approval.

The manifest contains one disposition for every blank-line-delimited source block (including headings, tables and code). Each row identifies original source, zero-based paragraph index, digest, disposition, target and reason. Exact retained blocks carry `retained_text` checked against the current target. Reconciled blocks require semantic review; a passing script alone cannot establish preservation. This granular index complements the requirement-level editor map below and the current design index.

`retained` means content remains at its current owner. `reconciled` means the same surviving intent is consolidated or split by responsibility. `superseded` identifies an explicit later amendment. `historical` retains original context, delivery timing, examples/proof or past status without making it a current mandate. Original tests remain evidence with their old execution status. New system test intent links their cases; no tests have been claimed rerun by relocation.

## File inventory

| Original identity | Exact retained source | Current owner/disposition |
| --- | --- | --- |
| `specs/editor-expert-quality-optimization.md` | [editor-expert-quality-optimization.md](../2026-05-26-editor-expert-quality-optimization/sources/editor-expert-quality-optimization.md) | [design/requirements/editor.md](../../../design/requirements/editor.md) |
| `specs/editor-expert-quality-optimization.test.md` | [test-spec.md](../2026-05-26-editor-expert-quality-optimization/test-spec.md) | [docs/changes/2026-05-26-editor-expert-quality-optimization/test-spec.md](../2026-05-26-editor-expert-quality-optimization/test-spec.md) |
| `specs/editor-learning-default-optimization.md` | [editor-learning-default-optimization.md](../2026-06-16-editor-learning-default-optimization/sources/editor-learning-default-optimization.md) | [design/requirements/editor.md](../../../design/requirements/editor.md) |
| `specs/editor-learning-default-optimization.test.md` | [test-spec.md](../2026-06-16-editor-learning-default-optimization/test-spec.md) | [docs/changes/2026-06-16-editor-learning-default-optimization/test-spec.md](../2026-06-16-editor-learning-default-optimization/test-spec.md) |
| `specs/editor-skill-optimization.md` | [editor-skill-optimization.md](../2026-05-25-editor-skill-optimization/sources/editor-skill-optimization.md) | [docs/changes/2026-05-25-editor-skill-optimization/sources/editor-skill-optimization.md](../2026-05-25-editor-skill-optimization/sources/editor-skill-optimization.md) |
| `specs/editor-skill-optimization.test.md` | [test-spec.md](../2026-05-25-editor-skill-optimization/test-spec.md) | [docs/changes/2026-05-25-editor-skill-optimization/test-spec.md](../2026-05-25-editor-skill-optimization/test-spec.md) |
| `specs/editor-source-plus-companion-language-optimization.md` | [editor-source-plus-companion-language-optimization.md](../2026-06-16-editor-source-plus-companion-language-optimization/sources/editor-source-plus-companion-language-optimization.md) | [design/requirements/editor.md](../../../design/requirements/editor.md) |
| `specs/editor-source-plus-companion-language-optimization.test.md` | [test-spec.md](../2026-06-16-editor-source-plus-companion-language-optimization/test-spec.md) | [docs/changes/2026-06-16-editor-source-plus-companion-language-optimization/test-spec.md](../2026-06-16-editor-source-plus-companion-language-optimization/test-spec.md) |
| `specs/flashcard-and-quiz-skills.md` | [flashcard-and-quiz-skills.md](../2026-07-04-flashcard-and-quiz-skills/sources/flashcard-and-quiz-skills.md) | [design/requirements/flashcard-and-quiz-skills.md](../../../design/requirements/flashcard-and-quiz-skills.md) |
| `specs/flashcard-and-quiz-skills.test.md` | [test-spec.md](../2026-07-04-flashcard-and-quiz-skills/test-spec.md) | [docs/changes/2026-07-04-flashcard-and-quiz-skills/test-spec.md](../2026-07-04-flashcard-and-quiz-skills/test-spec.md) |
| `specs/restaurant-menu-advisor.md` | [restaurant-menu-advisor.md](../2026-06-21-add-restaurant-menu-advisor/sources/restaurant-menu-advisor.md) | [design/requirements/restaurant-menu-advisor.md](../../../design/requirements/restaurant-menu-advisor.md) |
| `specs/restaurant-menu-advisor.test.md` | [test-spec.md](../2026-06-21-add-restaurant-menu-advisor/test-spec.md) | [docs/changes/2026-06-21-add-restaurant-menu-advisor/test-spec.md](../2026-06-21-add-restaurant-menu-advisor/test-spec.md) |
| `specs/rigorloop-v2-adoption-allocation.md` | [rigorloop-v2-adoption-allocation.md](sources/rigorloop-v2-adoption-allocation.md) | [design/requirements/rigorloop-v2-adoption-allocation.md](../../../design/requirements/rigorloop-v2-adoption-allocation.md) |
| `specs/rigorloop-v2-adoption.md` | [rigorloop-v2-adoption.md](sources/rigorloop-v2-adoption.md) | [design/requirements/rigorloop-v2-adoption.md](../../../design/requirements/rigorloop-v2-adoption.md) |
| `specs/skill-quality-standard.md` | [skill-quality-standard.md](../2026-05-25-rigorloop-governed-skill-quality/sources/skill-quality-standard.md) | [design/requirements/skill-quality-standard.md](../../../design/requirements/skill-quality-standard.md) |
| `specs/skill-quality-standard.test.md` | [test-spec.md](../2026-05-25-rigorloop-governed-skill-quality/test-spec.md) | [docs/changes/2026-05-25-rigorloop-governed-skill-quality/test-spec.md](../2026-05-25-rigorloop-governed-skill-quality/test-spec.md) |
| `docs/architecture/system/architecture.md` | [architecture.md](../2026-05-26-editor-expert-quality-optimization/sources/architecture/architecture.md) | [docs/changes/2026-05-26-editor-expert-quality-optimization/sources/architecture/architecture.md](../2026-05-26-editor-expert-quality-optimization/sources/architecture/architecture.md) |
| `docs/architecture/system/diagrams/container-view.mmd` | [container-view.mmd](../2026-05-26-editor-expert-quality-optimization/sources/architecture/diagrams/container-view.mmd) | [docs/changes/2026-05-26-editor-expert-quality-optimization/sources/architecture/diagrams/container-view.mmd](../2026-05-26-editor-expert-quality-optimization/sources/architecture/diagrams/container-view.mmd) |
| `docs/architecture/system/diagrams/editor-workflow.mmd` | [editor-workflow.mmd](../2026-05-26-editor-expert-quality-optimization/sources/architecture/diagrams/editor-workflow.mmd) | [docs/changes/2026-05-26-editor-expert-quality-optimization/sources/architecture/diagrams/editor-workflow.mmd](../2026-05-26-editor-expert-quality-optimization/sources/architecture/diagrams/editor-workflow.mmd) |
| `docs/architecture/system/diagrams/system-context.mmd` | [system-context.mmd](../2026-05-26-editor-expert-quality-optimization/sources/architecture/diagrams/system-context.mmd) | [docs/changes/2026-05-26-editor-expert-quality-optimization/sources/architecture/diagrams/system-context.mmd](../2026-05-26-editor-expert-quality-optimization/sources/architecture/diagrams/system-context.mmd) |
| `docs/architecture/workflow.md` | [maintenance-workflow.md](sources/maintenance-workflow.md) | [design/architecture/maintenance-workflow.md](../../../design/architecture/maintenance-workflow.md) |

## Editor reconciliation

The expert-quality source explicitly superseded the earlier editor-skill-optimization proposal. The learning-default amendment retains expert constraints except where it changes note behavior. The source-plus-companion amendment retains fidelity and default learning while replacing visible-language defaults, hidden bilingual rendering and note-count guidance. The current editor contract contains the latest R1–R67 (original delivery conditions labeled), examples and acceptance plus source-qualified inherited detail. It is the sole current obligation owner.

R references in the target/rationale column below refer to the latest source-plus-companion contract unless explicitly source-qualified. Each earlier requirement is dispositioned, including proof intent and original-slice conditions. Older examples and acceptance records retain their exact formulations historically: their obsolete language/note defaults are not a second current contract. Current examples and acceptance cover the effective rules; reusable old scenario classes remain in system test intent.

| Source-qualified requirement | Disposition | Effective target | Reason |
| --- | --- | --- | --- |
| `editor-expert-quality-optimization:R1` | reconciled | [r1](../../../design/requirements/editor.md#r1) | Preserved meaning in consolidated contract: R1. |
| `editor-expert-quality-optimization:R2` | reconciled | [r2](../../../design/requirements/editor.md#r2) | Preserved meaning in consolidated contract: R2. |
| `editor-expert-quality-optimization:R3` | reconciled | [r3](../../../design/requirements/editor.md#r3) | Preserved meaning in consolidated contract: R3. |
| `editor-expert-quality-optimization:R4` | reconciled | [r4](../../../design/requirements/editor.md#r4) | Preserved meaning in consolidated contract: R4. |
| `editor-expert-quality-optimization:R5` | reconciled | [r7](../../../design/requirements/editor.md#r7) | Preserved meaning in consolidated contract: R7. |
| `editor-expert-quality-optimization:R6` | superseded | [r5](../../../design/requirements/editor.md#r5) | Explicit learning/default-language amendment replaces the changed portion; surviving intent is covered by R5 R6 R7. |
| `editor-expert-quality-optimization:R7` | reconciled | [r8](../../../design/requirements/editor.md#r8) | Preserved meaning in consolidated contract: R8. |
| `editor-expert-quality-optimization:R8` | reconciled | [r9](../../../design/requirements/editor.md#r9) | Preserved meaning in consolidated contract: R9. |
| `editor-expert-quality-optimization:R9` | reconciled | [r10](../../../design/requirements/editor.md#r10) | Preserved meaning in consolidated contract: R10. |
| `editor-expert-quality-optimization:R10` | reconciled | [r11](../../../design/requirements/editor.md#r11) | Preserved meaning in consolidated contract: R11. |
| `editor-expert-quality-optimization:R11` | reconciled | [r9](../../../design/requirements/editor.md#r9) | Preserved meaning in consolidated contract: R9 R20. |
| `editor-expert-quality-optimization:R12` | reconciled | [r20](../../../design/requirements/editor.md#r20) | Preserved meaning in consolidated contract: R20. |
| `editor-expert-quality-optimization:R13` | reconciled | [r20](../../../design/requirements/editor.md#r20) | Preserved meaning in consolidated contract: R20. |
| `editor-expert-quality-optimization:R14` | reconciled | [r21](../../../design/requirements/editor.md#r21) | Preserved meaning in consolidated contract: R21. |
| `editor-expert-quality-optimization:R15` | reconciled | [r12](../../../design/requirements/editor.md#r12) | Preserved meaning in consolidated contract: R12. |
| `editor-expert-quality-optimization:R16` | superseded | [r13](../../../design/requirements/editor.md#r13) | Explicit learning/default-language amendment replaces the changed portion; surviving intent is covered by R13 R14 R15 R16. |
| `editor-expert-quality-optimization:R17` | reconciled | [r22](../../../design/requirements/editor.md#r22) | Preserved meaning in consolidated contract: R22. |
| `editor-expert-quality-optimization:R18` | reconciled | [r22](../../../design/requirements/editor.md#r22) | Preserved meaning in consolidated contract: R22. |
| `editor-expert-quality-optimization:R19` | reconciled | [r24](../../../design/requirements/editor.md#r24) | Preserved meaning in consolidated contract: R24. |
| `editor-expert-quality-optimization:R20` | reconciled | [r33](../../../design/requirements/editor.md#r33) | Preserved meaning in consolidated contract: R33. |
| `editor-expert-quality-optimization:R21` | reconciled | [non-goals](../../../design/requirements/editor.md#non-goals) | Preserved meaning in consolidated contract: Non-goals. |
| `editor-expert-quality-optimization:R22` | reconciled | [editor-expert-quality-optimization-r22](../../../design/requirements/editor.md#editor-expert-quality-optimization-r22) | Retained source-qualified detail; later source/companion output and default notes govern any changed framing. |
| `editor-expert-quality-optimization:R23` | superseded | [r38](../../../design/requirements/editor.md#r38) | Explicit learning/default-language amendment replaces the changed portion; surviving intent is covered by R38 R49. |
| `editor-expert-quality-optimization:R24` | reconciled | [editor-expert-quality-optimization-r24](../../../design/requirements/editor.md#editor-expert-quality-optimization-r24) | Retained source-qualified detail; later source/companion output and default notes govern any changed framing. |
| `editor-expert-quality-optimization:R25` | reconciled | [r8](../../../design/requirements/editor.md#r8) | Preserved meaning in consolidated contract: R8. |
| `editor-expert-quality-optimization:R26` | reconciled | [r8](../../../design/requirements/editor.md#r8) | Preserved meaning in consolidated contract: R8. |
| `editor-expert-quality-optimization:R27` | reconciled | [editor-expert-quality-optimization-r27](../../../design/requirements/editor.md#editor-expert-quality-optimization-r27) | Retained source-qualified detail; later source/companion output and default notes govern any changed framing. |
| `editor-expert-quality-optimization:R28` | reconciled | [editor-expert-quality-optimization-r28](../../../design/requirements/editor.md#editor-expert-quality-optimization-r28) | Retained source-qualified detail; later source/companion output and default notes govern any changed framing. |
| `editor-expert-quality-optimization:R29` | reconciled | [error-and-boundary-behavior](../../../design/requirements/editor.md#error-and-boundary-behavior) | Preserved meaning in consolidated contract: Error and boundary behavior. |
| `editor-expert-quality-optimization:R30` | reconciled | [editor-expert-quality-optimization-r30](../../../design/requirements/editor.md#editor-expert-quality-optimization-r30) | Retained source-qualified detail; later source/companion output and default notes govern any changed framing. |
| `editor-expert-quality-optimization:R31` | reconciled | [r5](../../../design/requirements/editor.md#r5) | Preserved meaning in consolidated contract: R5 R6. |
| `editor-expert-quality-optimization:R32` | superseded | [r13](../../../design/requirements/editor.md#r13) | Explicit learning/default-language amendment replaces the changed portion; surviving intent is covered by R13 R14 R15 R16. |
| `editor-expert-quality-optimization:R33` | reconciled | [r31](../../../design/requirements/editor.md#r31) | Preserved meaning in consolidated contract: R31 R32 R34 R51. |
| `editor-expert-quality-optimization:R34` | superseded | [r22](../../../design/requirements/editor.md#r22) | Explicit learning/default-language amendment replaces the changed portion; surviving intent is covered by R22 R31 R34 R37. |
| `editor-expert-quality-optimization:R35` | superseded | [r22](../../../design/requirements/editor.md#r22) | Explicit learning/default-language amendment replaces the changed portion; surviving intent is covered by R22 R31 R34 R37. |
| `editor-expert-quality-optimization:R36` | reconciled | [r52](../../../design/requirements/editor.md#r52) | Preserved meaning in consolidated contract: R52. |
| `editor-expert-quality-optimization:R37` | superseded | [r54](../../../design/requirements/editor.md#r54) | Explicit learning/default-language amendment replaces the changed portion; surviving intent is covered by R54 R55 R56. |
| `editor-expert-quality-optimization:R38` | superseded | [r25](../../../design/requirements/editor.md#r25) | Explicit learning/default-language amendment replaces the changed portion; surviving intent is covered by R25 R26 R27. |
| `editor-expert-quality-optimization:R39` | reconciled | [r30](../../../design/requirements/editor.md#r30) | Preserved meaning in consolidated contract: R30. |
| `editor-expert-quality-optimization:R40` | reconciled | [r30](../../../design/requirements/editor.md#r30) | Preserved meaning in consolidated contract: R30. |
| `editor-expert-quality-optimization:R41` | reconciled | [accessibility-and-ux](../../../design/requirements/editor.md#accessibility-and-ux) | Preserved meaning in consolidated contract: Accessibility and UX. |
| `editor-expert-quality-optimization:R42` | reconciled | [r58](../../../design/requirements/editor.md#r58) | Preserved meaning in consolidated contract: R58. |
| `editor-expert-quality-optimization:R43` | reconciled | [test-intent](../../../design/system/editor.md#test-intent) | Reusable verification intent retained; original cases and execution status stay in the owning historical test plan. |
| `editor-expert-quality-optimization:R44` | reconciled | [test-intent](../../../design/system/editor.md#test-intent) | Reusable verification intent retained; original cases and execution status stay in the owning historical test plan. |
| `editor-expert-quality-optimization:R45` | historical | [Historical source](../2026-05-26-editor-expert-quality-optimization/sources/editor-expert-quality-optimization.md) | Original delivery-only condition; retained with its original change, not reissued by this migration. |
| `editor-expert-quality-optimization:R46` | historical | [Historical source](../2026-05-26-editor-expert-quality-optimization/sources/editor-expert-quality-optimization.md) | Original delivery-only condition; retained with its original change, not reissued by this migration. |
| `editor-expert-quality-optimization:R47` | reconciled | [r2](../../../design/requirements/editor.md#r2) | Preserved meaning in consolidated contract: R2. |
| `editor-expert-quality-optimization:R48` | historical | [Historical source](../2026-05-26-editor-expert-quality-optimization/sources/editor-expert-quality-optimization.md) | Original delivery-only condition; retained with its original change, not reissued by this migration. |
| `editor-expert-quality-optimization:R49` | historical | [Historical source](../2026-05-26-editor-expert-quality-optimization/sources/editor-expert-quality-optimization.md) | Original delivery-only condition; retained with its original change, not reissued by this migration. |
| `editor-learning-default-optimization:R1` | reconciled | [r8](../../../design/requirements/editor.md#r8) | Preserved meaning in consolidated contract: R8. |
| `editor-learning-default-optimization:R2` | reconciled | [r2](../../../design/requirements/editor.md#r2) | Preserved meaning in consolidated contract: R2. |
| `editor-learning-default-optimization:R3` | superseded | [r5](../../../design/requirements/editor.md#r5) | Explicit learning/default-language amendment replaces the changed portion; surviving intent is covered by R5. |
| `editor-learning-default-optimization:R4` | reconciled | [r5](../../../design/requirements/editor.md#r5) | Preserved meaning in consolidated contract: R5. |
| `editor-learning-default-optimization:R5` | reconciled | [editor-learning-default-optimization-r5](../../../design/requirements/editor.md#editor-learning-default-optimization-r5) | Retained source-qualified detail; later source/companion output and default notes govern any changed framing. |
| `editor-learning-default-optimization:R6` | reconciled | [r38](../../../design/requirements/editor.md#r38) | Preserved meaning in consolidated contract: R38 R44. |
| `editor-learning-default-optimization:R7` | reconciled | [r38](../../../design/requirements/editor.md#r38) | Preserved meaning in consolidated contract: R38. |
| `editor-learning-default-optimization:R8` | reconciled | [accessibility-and-ux](../../../design/requirements/editor.md#accessibility-and-ux) | Preserved meaning in consolidated contract: Accessibility and UX. |
| `editor-learning-default-optimization:R9` | reconciled | [editor-learning-default-optimization-r9](../../../design/requirements/editor.md#editor-learning-default-optimization-r9) | Retained source-qualified detail; later source/companion output and default notes govern any changed framing. |
| `editor-learning-default-optimization:R10` | reconciled | [editor-learning-default-optimization-r10](../../../design/requirements/editor.md#editor-learning-default-optimization-r10) | Retained source-qualified detail; later source/companion output and default notes govern any changed framing. |
| `editor-learning-default-optimization:R11` | reconciled | [editor-learning-default-optimization-r11](../../../design/requirements/editor.md#editor-learning-default-optimization-r11) | Retained source-qualified detail; later source/companion output and default notes govern any changed framing. |
| `editor-learning-default-optimization:R12` | reconciled | [r40](../../../design/requirements/editor.md#r40) | Preserved meaning in consolidated contract: R40. |
| `editor-learning-default-optimization:R12a` | reconciled | [editor-learning-default-optimization-r12a](../../../design/requirements/editor.md#editor-learning-default-optimization-r12a) | Retained source-qualified detail; later source/companion output and default notes govern any changed framing. |
| `editor-learning-default-optimization:R13` | reconciled | [r41](../../../design/requirements/editor.md#r41) | Preserved meaning in consolidated contract: R41. |
| `editor-learning-default-optimization:R14` | reconciled | [r39](../../../design/requirements/editor.md#r39) | Preserved meaning in consolidated contract: R39. |
| `editor-learning-default-optimization:R15` | reconciled | [r8](../../../design/requirements/editor.md#r8) | Preserved meaning in consolidated contract: R8 R26. |
| `editor-learning-default-optimization:R16` | reconciled | [r42](../../../design/requirements/editor.md#r42) | Preserved meaning in consolidated contract: R42 R51 R52. |
| `editor-learning-default-optimization:R17` | reconciled | [r42](../../../design/requirements/editor.md#r42) | Preserved meaning in consolidated contract: R42. |
| `editor-learning-default-optimization:R18` | reconciled | [editor-learning-default-optimization-r22](../../../design/requirements/editor.md#editor-learning-default-optimization-r22) | Retained source-qualified detail; later source/companion output and default notes govern any changed framing. |
| `editor-learning-default-optimization:R19` | superseded | [r46](../../../design/requirements/editor.md#r46) | Explicit learning/default-language amendment replaces the changed portion; surviving intent is covered by R46 R47. |
| `editor-learning-default-optimization:R20` | reconciled | [r47](../../../design/requirements/editor.md#r47) | Preserved meaning in consolidated contract: R47. |
| `editor-learning-default-optimization:R21` | reconciled | [r42](../../../design/requirements/editor.md#r42) | Preserved meaning in consolidated contract: R42 R46 R47. |
| `editor-learning-default-optimization:R22` | reconciled | [editor-learning-default-optimization-r22](../../../design/requirements/editor.md#editor-learning-default-optimization-r22) | Retained source-qualified detail; later source/companion output and default notes govern any changed framing. |
| `editor-learning-default-optimization:R23` | reconciled | [r43](../../../design/requirements/editor.md#r43) | Preserved meaning in consolidated contract: R43 R44. |
| `editor-learning-default-optimization:R24` | reconciled | [r8](../../../design/requirements/editor.md#r8) | Preserved meaning in consolidated contract: R8 R44. |
| `editor-learning-default-optimization:R25` | reconciled | [editor-learning-default-optimization-r25](../../../design/requirements/editor.md#editor-learning-default-optimization-r25) | Retained source-qualified detail; later source/companion output and default notes govern any changed framing. |
| `editor-learning-default-optimization:R26` | reconciled | [r36](../../../design/requirements/editor.md#r36) | Preserved meaning in consolidated contract: R36 R49. |
| `editor-learning-default-optimization:R27` | reconciled | [r36](../../../design/requirements/editor.md#r36) | Preserved meaning in consolidated contract: R36. |
| `editor-learning-default-optimization:R28` | reconciled | [r50](../../../design/requirements/editor.md#r50) | Preserved meaning in consolidated contract: R50. |
| `editor-learning-default-optimization:R29` | reconciled | [r38](../../../design/requirements/editor.md#r38) | Preserved meaning in consolidated contract: R38 R50. |
| `editor-learning-default-optimization:R30` | reconciled | [editor-learning-default-optimization-r30](../../../design/requirements/editor.md#editor-learning-default-optimization-r30) | Retained source-qualified detail; later source/companion output and default notes govern any changed framing. |
| `editor-learning-default-optimization:R31` | reconciled | [r31](../../../design/requirements/editor.md#r31) | Preserved meaning in consolidated contract: R31 R32 R38. |
| `editor-learning-default-optimization:R32` | superseded | [r54](../../../design/requirements/editor.md#r54) | Explicit learning/default-language amendment replaces the changed portion; surviving intent is covered by R54 R55 R56. |
| `editor-learning-default-optimization:R33` | superseded | [r28](../../../design/requirements/editor.md#r28) | Explicit learning/default-language amendment replaces the changed portion; surviving intent is covered by R28. |
| `editor-learning-default-optimization:R34` | superseded | [r31](../../../design/requirements/editor.md#r31) | Explicit learning/default-language amendment replaces the changed portion; surviving intent is covered by R31 R34. |
| `editor-learning-default-optimization:R35` | reconciled | [r49](../../../design/requirements/editor.md#r49) | Preserved meaning in consolidated contract: R49. |
| `editor-learning-default-optimization:R35a` | superseded | [r28](../../../design/requirements/editor.md#r28) | Explicit learning/default-language amendment replaces the changed portion; surviving intent is covered by R28 R44. |
| `editor-learning-default-optimization:R35b` | reconciled | [r48](../../../design/requirements/editor.md#r48) | Preserved meaning in consolidated contract: R48. |
| `editor-learning-default-optimization:R36` | historical | [Historical source](../2026-06-16-editor-learning-default-optimization/sources/editor-learning-default-optimization.md) | Original delivery-only condition; retained with its original change, not reissued by this migration. |
| `editor-learning-default-optimization:R37` | historical | [Historical source](../2026-06-16-editor-learning-default-optimization/sources/editor-learning-default-optimization.md) | Original delivery-only condition; retained with its original change, not reissued by this migration. |
| `editor-learning-default-optimization:R38` | reconciled | [test-intent](../../../design/system/editor.md#test-intent) | Reusable verification intent retained; original cases and execution status stay in the owning historical test plan. |

## Semantic boundaries and evidence

Requirement statements, examples, safety constraints and observable acceptance remain in `design/requirements/`. Logical sequencing, transformations and reusable test intent belong in `design/system/`. The portable prompt/validation/reviewer responsibilities and maintenance Modules/Interfaces belong in `design/architecture/`. Historical diagrams remain alongside their original architecture source, with no claim that outdated output/note policies are current.

The current editor contract explicitly retains precise wording, ambiguity handling, audience/tone, complete fidelity dimensions, concrete fallback references, exact learning-note labels, source-required coaching, grouping, safe generalization and user-requested expansion. No source meaning is inferred solely from the current prompt implementation.

Original review text, hashes and quoted source paths are preserved. Only exposed Markdown navigation is repaired to exact historical snapshots or current owners. Source snapshots themselves are never rewritten. Current repository guidance points to the three design roots; there are no forwarding files at retired paths.

The [migration audit](check_migration.py) checks snapshot bytes, complete paragraph coverage, destinations/anchors, exact retained text, protected product bytes and active links. Independent review owns semantic adequacy and may require correction of this mapping before acceptance.
