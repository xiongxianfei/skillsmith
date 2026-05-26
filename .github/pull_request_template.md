## Summary

<!-- What does this PR add or change? One sentence per skill or change. -->

## Checklist

### For new skills
- [ ] Skill directory follows the pattern `skills/<skill-name>/SKILL.md`
- [ ] `description` is in English and under 250 characters
- [ ] Optional frontmatter such as `argument-hint`, `effort`, or `allowed-tools` is omitted unless an accepted proposal/spec requires it
- [ ] `$ARGUMENTS` appears in the prompt body
- [ ] `## Output Format` section is present
- [ ] No emojis in the Output Format section
- [ ] New or materially changed skill includes eval scenarios for normal use, indirect trigger, and edge/safety/failure/non-trigger/misuse behavior
- [ ] High-risk skill changes include safety notes, scope boundaries, refusal or escalation behavior, and a safety or misuse eval case
- [ ] CI validation passes (`python tests/validate_skills.py`)
- [ ] Skill added to the README skills table
- [ ] Skill added to the install commands in README

### For bug fixes / improvements
- [ ] Describe what was wrong and why the fix is correct
- [ ] Include a minimal reproduction in the PR description or linked issue
- [ ] Classify skill prompt changes as material or editorial
- [ ] Add regression coverage or explain why automated coverage is not practical
- [ ] Update docs, templates, or validator rules if this bug exposed a repeatable pattern
- [ ] CI validation still passes

## Test plan

<!--
How did you verify this works?
- Example inputs/outputs for prompt changes
- Eval scenario files or reviewer-visible scenario notes for new/materially changed skills
- Manual model smoke evidence for high-risk, behavior-heavy, or model-specific claims
- Validator/test command output
- Linked issue with reproduction, if applicable
-->
