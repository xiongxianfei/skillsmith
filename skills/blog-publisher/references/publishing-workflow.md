# Publishing workflow

Use this reference for repository inspection, validation and delivery. Commands come from the selected project; examples here do not configure a destination or grant permissions.

## Discover the project contract

Inspect the worktree, remotes, branch, repository instructions, existing posts, content schema, build scripts and deployment documentation. Check available context before asking the user for missing configuration. Establish:

| Concern | Evidence to find |
|---|---|
| Target | Selected repository, checkout and public site origin. |
| Content | Post directory, Markdown/MDX or other format, required fields, author records and stable URL convention. |
| Visibility | How Drafts and Published posts are represented; whether dates affect visibility; local/private preview behavior. |
| Build | Runtime version, lockfile, install and validation commands, generated output location. |
| Delivery | Direct push or PR policy, publishing branch, workflow/provider, approval gates and observable deployment identity. |
| Public surfaces | Post page, listings, feed, sitemap, search, related recommendations and image URLs, where implemented. |

Do not create a second configuration system when the repository already supplies this information. Do not copy local machine paths into a portable skill. On a new machine, clone only after the intended repository and access are established. Preserve unrelated changes and reconcile with the remote without discarding work or force-pushing.

Full publication needs a host capable of editing the repository, running the build, authenticating to Git/hosting, observing deployment and checking HTTP responses. A text-only host can prepare writing but cannot truthfully report validation or deployment. Use existing connectors or command-line tools; no specific vendor tool is mandatory.

## Prepare the post and assets

1. Select draft, new publication or revision mode from the user's intent. Inspect existing content to avoid duplicate posts and URL collisions.
2. Follow the actual schema. Preserve the existing slug/URL and initial publication date when revising; add a revision date only if supported. Do not change dates to simulate scheduling unless the project implements it.
3. Follow existing numbering and navigation conventions. If the layout generates H2 numbers or a contents list, do not duplicate them in the source.
4. Keep screenshots and diagrams alongside their post when supported. Inspect images before inclusion, add useful alternative text and captions, and use descriptive asset names. Use the framework's established image pipeline; Markdown and MDX may handle imports differently.
5. Check draft privacy at source and output boundaries. A public repository exposes committed drafts even on non-default branches. Files copied directly from a public/static asset folder can ship without a post route. Content queries alone may not prevent compilation from emitting assets.

If the project has no safe draft mechanism, keep the requested draft outside its publishable source tree and explain the preview limitation. Do not invent an ignored frontmatter flag and assume it protects content. Do not make a repository private, change access settings or provision preview hosting as an incidental content edit.

## Validate and render

Use the declared runtime and dependency versions and the repository's required checks. This may include type checks, content validation, tests, a production build and a draft-output guard. Run dependency installation only when needed. Inspect failures rather than weakening validation.

Review the generated route, metadata, internal links, heading anchors, code fences and images. Confirm that image URLs resolve to actual images, not just HTTP-success fallback pages. Inspect the rendered post at a narrow and wide viewport when changing layout-sensitive content or screenshots. Verify only behavior actually exercised; a build is not a visual or accessibility audit.

For a draft, use a loopback local preview or an already authorized access-controlled preview. An unlisted URL or `noindex` tag is not access control. Confirm the preview banner/status where applicable and exclusion from the production routes and public data/asset outputs. Build scans are defense in depth, not proof that every possible transformed secret is absent.

If development and production share a content cache, a build may invalidate a running preview. Restart only the known project server if necessary; do not kill unrelated processes or expose the preview to a public interface.

## Deliver through the existing release route

Review the scoped diff before committing. Stage only intended content and assets. Follow the authorized branch policy: direct publication may push to the publishing branch; a protected route may require a PR and review first. Stop at the authorized review boundary. A merged commit may have a different identity from the PR head, especially after squash merge.

For GitHub Actions, ordinary publishing usually needs repository write access (or permission to contribute a branch/PR), visibility into workflow results and the project's build environment. Workflow dispatch or merging needs its corresponding permission and authorization only when used. Credentials alone never establish publication intent.

When an existing CI workflow owns server deployment, it holds the server credentials and trusted-host configuration. Content authors do not need a local VPS key for routine writing. Do not copy server keys into the skill, repository, prompts or examples, or request new infrastructure permissions merely to publish content.

Record the pushed or merged commit and identify the deployment run for that exact revision. Watch it to completion; do not assume the newest run is yours. If a later release supersedes it, identify what is actually serving and check whether it includes the intended revision. Do not redeploy just to force a marker to match an older commit.

On failure, inspect the logs without exposing secrets and determine whether activation occurred or recovery restored the previous release. Fix a concrete content/build problem within scope. Do not repeatedly retry an unexplained transfer failure or switch releases without an authorized recovery policy. Report whether the post is unpublished, pending, restored or live with a verification problem.

## Verify what readers receive

- Request the canonical post URL and confirm the intended title and revised content; status 200 alone is insufficient.
- Fetch newly added or changed images and verify image responses. Check important internal links and relevant topic/recommendation links.
- Confirm inclusion or intended removal in the site's implemented listing, feed, sitemap and search outputs. Do not require features the project does not have.
- Compare the deployed revision to provider metadata or an existing release marker. A revision-specific request can help distinguish cached metadata. If no identity mechanism exists, report the content checks and that exact release identity was not independently established; do not provision one incidentally.
- Verify remaining Draft exclusion through the build guard and, when checking HTTP privacy, a known actual Draft route. An invented nonexistent URL proves nothing about real drafts. Use the project's expected status, commonly 404.

Unpublishing removes content from a new release but cannot retract Git history, retained releases, downloaded search indexes, feed readers or third-party caches. Do not promise erasure.

Report actual checks and remaining limitations, not just a successful push. For an explicitly local draft or PR-only delivery, report that mode and stop before public deployment.
