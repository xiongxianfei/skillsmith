# Simplify repository guidance and maintenance

## Background

Keep Skillsmith a straightforward collection of skills. Replace its separate quality framework with official OpenAI and Anthropic guidance, remove vision documents and installer tooling, and retain useful validation. Describe the project simply without emphasizing portability.

## Input

- [README.md](../README.md), [AGENTS.md](../AGENTS.md), and [docs/workflows.md](../docs/workflows.md): project description, usage, agent conduct and contribution rules.
- `VISION.md`, `docs/vision/strategic-positioning.md`, `docs/skill-quality-standard.md`, and `install.sh`: material to retire.
- [tests/validate_skills.py](../tests/validate_skills.py) and [.github/workflows/validate.yml](../.github/workflows/validate.yml): existing metadata validation and CI.
- [design/architecture/README.md](../design/README.md): skill designs and shared architecture references.
- [OpenAI skill guidance](https://learn.chatgpt.com/docs/build-skills) and [Anthropic authoring guidance](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices): external authoring references.

## Output

- **Delete** `VISION.md`, `docs/vision/strategic-positioning.md`, `docs/skill-quality-standard.md`, and `install.sh`.
- **Modify** `README.md`: retain a short project description and skill catalog; replace installation instructions with a sentence telling users to download a complete skill folder into their host's skill directory. Preserve relevant migration information.
- **Modify** `AGENTS.md` and `docs/workflows.md`: link official guidance, remove retired requirements and portability positioning, and retain concise repository conduct and contribution instructions.
- **Modify** `.github/pull_request_template.md`: remove the installation-example checklist requirement.
- **Modify** `design/architecture/README.md`, `design/architecture/portable-skills.md`, and `design/architecture/vocabulary-mastery-c4/architecture-spec.md`: repair retired references and remove redundant portability framing while preserving useful design decisions.
- **Retain** skill-specific designs, metadata validation and CI, and functional tests for executable skill scripts. Inspection found no justified test deletion.

Acceptance: active documentation has no broken links or instructions relying on deleted files; official sources replace the separate authoring standard; skill behavior and useful regression coverage remain intact.

## Rules

Follow [AGENTS.md](../AGENTS.md) and the [workflow guide](../docs/workflows.md), with the user's explicit simplification decisions replacing the retired policies. Preserve existing uncommitted changes, skill behavior, safety boundaries and actual compatibility obligations. Apply vendor guidance to its intended host. Do not recreate the quality standard elsewhere or add new tooling or documentation layers. This task record is saved at the user's explicit request.

## Approach

Use an isolated checkout branched from latest `main` to protect the dirty workspace. Remove obsolete material, update references, and inspect the final diff for unrelated changes. Run metadata validation and retained functional suites; check affected local links and a representative skill's supporting resources. Keep implementation and verification evidence in the PR.

## Progress checklist

- [x] Remove vision documents, separate quality standard, and installer.
- [x] Simplify guidance, remove portability emphasis, and repair references.
- [x] Preserve skill designs, functional tests, and metadata-validation CI.
- [x] Run validation and functional tests; inspect links and diff.
- [x] Record implementation and results in a draft PR.
- [ ] Complete PR review and merge; no approval or merge is recorded here.

## Execution result

Implemented in [draft PR #59](https://github.com/xiongxianfei/skillsmith/pull/59), commit `6707967ff83bb8fd71b9f61f6398bf5174c6cfdc`, on branch `improve/simplify-repository`. The implementation used the separate `../skillsmith-simplify` worktree based on latest `main`. The original workspace's existing edits were preserved; this task file is saved in that original workspace and is not part of the implementation commit.

The implementation changed 11 files, with 70 insertions and 467 deletions. The email skill migration note was retained. No skill code, diagrams, test scripts or CI configuration changed.

Verification performed in the implementation worktree:

| Command or check | Result |
| --- | --- |
| `python tests/validate_skills.py` | All 27 skills passed |
| `python -m unittest discover -s tests -p 'test_*.py' -v` | 32 tests passed |
| `python -m unittest discover -s skills/city-itinerary-builder/tests -p 'test_*.py' -v` | 8 tests passed |
| `python -m unittest discover -s skills/travel-planner/scripts -p 'test_*.py' -v` | 8 tests passed |
| Local Markdown link targets in changed documents and vocabulary skill | 75 checked; none missing |
| Search for references to deleted paths | No remaining matches |
| `git diff --check` | Passed |

No warnings or failures were reported by these checks. Diagram rendering and live-model evaluation were skipped because diagrams and skill behavior were unchanged. These checks do not establish model quality or host compatibility. At implementation handoff, the PR was draft and unmerged; remote CI and independent review were not verified.
