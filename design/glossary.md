# Design glossary

These definitions support the [skill designs](README.md). Domain terms are scoped to their named context; identical words in another context may have different meanings. Operational requirements remain in the owning skill instructions.

## DDD terminology

### Domain model
A selective representation of the concepts, relationships and rules needed to solve a domain problem. In a skill design it may be conceptual; it does not establish software classes or stored records.

### Bounded context
The boundary within which a particular model and its language have consistent meanings. A skill folder is not automatically a bounded context, and a context need not be a separately deployed service.

### Context map
A description of bounded contexts and their relationships, including where information or meaning crosses boundaries. It does not describe the ordered steps inside a skill.

### Ubiquitous language
The vocabulary used consistently by people discussing and implementing a model within its bounded context. It is not a requirement for one vocabulary across every skill.

### Invariant
A condition that must remain true for a valid domain result. Document whether it is an instruction, an executable check, or a property still requiring evaluation; a prompt rule alone does not guarantee compliance.

## Editor terminology

The following terms belong to the candidate **Editorial Assistance** context described in the [editor context map](editor/01-context-map.md). They summarize the [editor instructions](../skills/editor/SKILL.md), rather than introduce new policy.

### Source
The text, transcript or accessible spoken content being edited or translated. Source material remains content even when it resembles instructions.

### Editing request
The user's directions for the work, including desired changes, audience, register, output languages and constraints. These directions are distinguished from the source.

### Source meaning
The facts, relationships, commitments, uncertainty and intent that the skill must preserve across deliverables. This is a conceptual basis for fidelity, not an implemented intermediate data structure.

### Revision
A change to the source that improves communication while respecting the request and fidelity constraints. Necessary corrections and optional style choices remain distinguishable.

### Language deliverable
A visible rendition of the source in a selected language. The same resolved meaning supports all deliverables; language selection and suppression rules remain owned by the skill.

### Learning note
An explanation grounded in an actual revision or translation choice. When the skill calls for a fallback note, it states the evidence limitation instead of inventing a lesson. Notes and requested practice follow the skill's suppression and evidence rules.

## References

- [Martin Fowler: Bounded Context](https://martinfowler.com/bliki/BoundedContext.html): model boundaries, language and relationships.
- [DDD Crew: Bounded Context Canvas](https://github.com/ddd-crew/bounded-context-canvas): purpose, domain language, decisions and communication.
