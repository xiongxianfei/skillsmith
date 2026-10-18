# Architecture review checklist

Load this checklist when preparing review or developer handoff. It is a review aid, not automatic approval.

## Scope and evidence
- [ ] System purpose, owner, boundaries, actors and dependencies are understood.
- [ ] Required functionality and important quality attributes are documented with evidence or marked unknown.
- [ ] Each proposed technology or relationship is supported by requirements, code, or an explicit pending decision.
- [ ] Implemented, proposed, and unknown items are clearly differentiated.

## C4 and D2 consistency
- [ ] C1 contains people/software systems rather than implementation internals.
- [ ] C2 contains appropriately scoped runnable/deployable units and data stores.
- [ ] Stable element IDs and names agree across views; relationship directions and protocols are meaningful.
- [ ] Targeted dynamic/deployment views cover the important scenarios where warranted.
- [ ] Shared model definitions are not independently contradicted by view-specific edges.

## Delivery and operations
- [ ] Security boundaries, identity, data handling, resilience, observability and performance are addressed according to risk.
- [ ] Interface contracts and ownership needed for implementation are clear or assigned.
- [ ] Decisions, alternatives, consequences and unresolved risks are tracked.

## Verification and approval
- [ ] D2 formatting, validation, and test rendering were run, or missing tools were clearly disclosed.
- [ ] Generated SVGs were visually reviewed, or visual review was explicitly not performed.
- [ ] Diff is focused; unrelated design and IDs are preserved.
- [ ] Human reviewers are asked to decide specific open questions; no automated check is represented as approval.
