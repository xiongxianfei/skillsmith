# Proposal Review R3: Editor Expert Quality Optimization

## Status

changes-requested

## Material Findings

- `F-PROP-EDITOR-EXPERT-003`

## Recording Note

The pasted review requested `proposal-review-r2.md`, but that path already records an earlier approved review. This review is recorded as R3 to preserve chronological lifecycle history.

## Finding `F-PROP-EDITOR-EXPERT-003`: inverse mixed-language eval is missing

Severity: major

Location: `Testing and Verification Strategy` -> `Required eval scenarios`

The proposal makes language-role separation core: instruction language controls response framing, source language controls the editing pass, and the target output is fixed bilingual Chinese + English.

The concrete eval set covered Chinese instruction with English source text, but did not cover the inverse case: English instruction with Chinese source text. This left one of the two primary mixed instruction/source directions untested.

Required outcome: add one concrete eval scenario for English instruction with Chinese source text before accepting the proposal.

## Suggested Resolution

Add an eval scenario equivalent to:

```yaml
- id: editor-expert-english-instruction-chinese-source
  category: edge
  prompt: |
    Polish this and make it suitable for a PR description:

    这个 PR 修复了用户更新资料后缓存没有失效的问题，之前页面可能还会显示旧名字。
  expected_behavior:
    - Treats English as the instruction language and Chinese as the source language.
    - Frames labels, notes, refusals, or any explanation in English.
    - Edits the Chinese source in Chinese before rendering the bilingual pair.
    - Preserves the technical meaning: cache invalidation after user profile updates and stale display of the old name.
    - Provides Chinese and English versions.
    - Does not duplicate the Chinese source-language text outside the Chinese version.
    - Does not add assessment or default notes.
```

## Outcome

Proposal revision required before renewed proposal-review acceptance and spec update.
