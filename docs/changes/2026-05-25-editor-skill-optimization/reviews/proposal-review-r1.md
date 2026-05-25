# Proposal Review R1: Editor skill optimization

## Review status

changes-requested

## Reviewed artifact

`docs/proposals/2026-05-25-editor-skill-optimization.md`

## Summary

The proposal is directionally sound and close to acceptance. It correctly keeps the first optimization slice limited to `editor`, requires baseline behavior before edits, puts output contract before workflow, and adds a concision gate.

One material testability gap blocks acceptance before revision: translation is part of the proposed behavior change, but no direct translation eval is included.

## Findings

### F-PROP-EDITOR-001

Severity: major

Location: `Testing and Verification Strategy`

Finding: The proposal says the optimized skill should preserve multilingual editing and translation value, and specifically expects targeted translation such as "translate this into Russian" to produce Russian output without automatic Chinese-English bilingual output. The proposed eval set covers proofreading, PR-description polishing, and an integrity-boundary misuse case, but not targeted translation.

Required outcome: Add a direct translation eval, or explicitly remove translation behavior from this slice. Because translation is already in the goals and expected behavior, the safer resolution is to add a fourth eval.

## Open question decision

Do not include default change notes for every edit.

The optimized `editor` skill should include notes only when the user asks for notes, the edit is substantial, the source contains a non-obvious ambiguity or fidelity concern, translation choices materially affect meaning, or the request triggers an integrity boundary.

For simple proofreading, polishing, rewriting, and targeted translation, the default should be the edited or translated text only.

## Non-material recommendations

- Make `python tests/check_readme_sync.py` conditional unless the helper exists.
- Add targeted translation behavior to the review checklist.
- Keep the output contract explicit in the spec with separate default output modes.

## Decision

Revise before acceptance.

After adding the translation eval, recording the conditional-notes decision, and making the README sync command conditional, the proposal may be marked accepted and ready for spec.
