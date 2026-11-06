# Post composition and example requests

Read this when composing a new post or restructuring one. Start from a representative post in the target repository. Do not paste a universal frontmatter block: metadata names, status values, authors, dates and image imports vary between projects.

## Useful writing shape

Use a concrete title and a short description of the reader's problem. Adapt these sections to the lesson rather than forcing every post into the same outline:

```markdown
Introduce the problem, its context and the useful outcome.

## The problem

Explain the trigger and constraints from the supplied evidence.

## What changed and why it works

Show a focused example and explain the mechanism, prerequisites and tradeoffs.

## How we checked it

Describe checks actually performed, observed results and limitations.

## Applying the lesson

Explain what readers should adapt and when the approach may not fit.
```

Use supported frontmatter, existing relevant tags and the site's date conventions. Do not label a proposed test as completed. Keep commands copyable; distinguish literal commands from placeholders and explain the effects of destructive operations. Link related public posts rather than inaccessible private repository documents.

Screenshots should demonstrate a specific behavior, with descriptive alt text and a caption identifying the relevant state or viewport. Inspect them for private material. Small screenshots may need a native full-size image link; verify both the displayed and linked assets. Diagrams should explain relationships or flow, not imply unimplemented components.

## Example requests and expected handling

These are usage examples and design expectations, not results of model evaluations. The repository must be selected through the user's actual context.

| Request | Expected handling |
|---|---|
| “Publish a post in this blog about the cache bug we just fixed. Use the test results above.” | Ground the explanation in the supplied evidence, validate and use the authorized release route; verify the resulting live post or report a pending review gate. |
| “Turn these notes into a post. We use direct publication so I can review it on the website.” | Treat the stated preference as publication intent for this task; still honor branch protections and project release rules. |
| “Update the existing deployment guide to explain the tested rollback. Keep its URL.” | Preserve the URL and initial publication date; revise supported update metadata. Deploy when requested or established by the user's live-update convention. |
| “Write a draft only; let me review the rendered version locally.” | Keep it excluded from public output, render locally if possible and return the preview. Do not push it to a public deployment path. |
| “Interesting result—we should remember that.” | Do not create or publish a post solely because the finding is interesting. |
| “Publish this,” with several unrelated repositories available. | Resolve the intended blog from context; ask if it remains ambiguous before choosing an external destination. |
| “Open a PR for this post; don't merge it.” | Validate, open the scoped PR and report its review status. Do not call it live or merge it. |

If a deployment fails, report the failed step and known release state instead of presenting an older public page as proof of success. If permissions or rendering tools are missing, deliver the work that can be completed and identify the specific remaining prerequisite.
