# Implementation evidence

Observed on 2026-10-18 in the user-selected current workspace by `/root`. These are implementation checks, not review approval or final Verify. No private operational store was edited or copied.

## Baseline and boundaries

The manifest identifies the baseline commit and SHA-256 for 38 protected product/installer/test/CI files, plus the exact user-authored Core Engineering Principles. All match. Existing `tests/__pycache__/` is preserved. All 21 original source files have byte-identical snapshots, including pre-migration uncommitted reviewed drafts. The retired roots are absent and all 1,664 source blocks have explicit dispositions.

## Executed checks

| Command | Result |
| --- | --- |
| `PYTHONDONTWRITEBYTECODE=1 python -m unittest discover tests` | 36 passed |
| `PYTHONDONTWRITEBYTECODE=1 python tests/validate_skills.py` | All 14 skills passed; one grandfathering warning |
| `PYTHONDONTWRITEBYTECODE=1 python tests/check_readme_sync.py` | Passed |
| `python -B docs/changes/2026-10-18-rigorloop-v2-adoption/check_migration.py` | 21 snapshots, 1,664 dispositions, protected bytes and active links/fragments passed |
| `python -B docs/changes/2026-10-18-rigorloop-v2-adoption/check_migration_failures.py` | Disposable missing-snapshot, missing-destination and altered-retained-clause cases all rejected |
| `git diff --check` | Passed |
| `python -B docs/changes/2026-10-18-rigorloop-v2-adoption/cli_fixture.py --node "$HOME/.nvm/versions/node/v24.22.0/bin/node" --cli "$HOME/.npm/_npx/c7f770a95c02a193/node_modules/@xiongxianfei/rigorloop/dist/bin/rigorloop.js"` | Passed with package version checked as 2.0.0, Node 24.22.0 and SQLite 3.53.4 |

The cache location in the executed command is local evidence, not a portable setup path. The script accepts any inspected installation of the pinned package. The workflow guide provides portable npx setup instructions.

The CLI fixture first successfully ran `init codex --dry-run --json` and compared every destination path/file hash before and after, including an unrelated pre-existing skill. It then created/read/updated a fictional Change, rejected a stale revision, backed up and restored to a separate absent store, recovered the expected handoff, rejected the old incarnation's token and accepted the freshly inspected token. All fixture state was temporary and removed. No reviewer judgment or completion was created. Initial fixture-authoring errors (passing unsupported `--root` to init and reading backup integrity at the wrong response level) were corrected against actual output; the final complete fixture passed.

## Scenario walkthroughs

- SC-RL-001: the workflow guide routes non-trivial managed work through reviewed requirements, integrated design and delivery, implementation, one whole-change review and distinct Verify; completion and publication remain separate.
- SC-RL-002: plan navigation explicitly preserves historical unknown CI/PR outcomes. Resumption requires actual inspection and explicit disposition; no bulk import or promotion of old judgments.
- SC-RL-003: protected hashes prove unchanged product prompt, installer and test/CI bytes. The workflow guide separates product installation/invocation from maintainer Node/CLI setup. No installer rerun was needed for byte-identical behavior.
- SC-RL-004: this Git-held account, exact snapshots, attributed upstream reviews, rationale and manifest expose scope, basis, results and limitations without the live store. The disposable backup/restore fixture supports recovery; unavailable hosted CI and historical PR status remain explicit gaps. Isolated tasks and later managed reliance are additionally distinguished in the workflow guide.
- SC-RL-005: a reader can follow editor requirements to system Functions and portable-skill responsibility, then inspect exact historical sources and the requirement-level amendment map. Hash/link checking supports this walk; semantic adequacy remains for independent review.

## Warnings and limits

Nine grandfathered skills lack eval fixtures: communicator, doctor, email-drafter, fitness-coach, journaling, language-tutor, nvc, oscp-coach and study-planner. This existing warning is acknowledged; unchanged prompts do not require model smoke runs for this migration.

Advisory reviewer `/root/review_adoption` identified A1: the explicitly inherited `dim lighting` fidelity scenario was absent from the new system test intent. The author restored the named scenario and inherited expert/learning scenario classes. Current static fixtures also lack the named case; that pre-existing evidence gap remains visible and is not silently backfilled in this documentation-only scope. Whole-change review must reassess A1's correction.

Hosted CI, PR creation, merge/release, live-model output quality and browser rendering were not exercised. Product design coverage remains partial, as listed in the design index. External historical PR status was not rechecked. This evidence does not assert catalog-wide design completion.
