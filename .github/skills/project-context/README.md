# Project Context skill

`project-context` creates a small, durable, reviewable layer of project knowledge that lives with the repository rather than disappearing at the end of a chat or contributor session. It helps a new contributor or agent understand the project purpose, current state, decisions, evidence, risks, and next safe action without treating a chat, agent memory, or code alone as the complete record.

## What it is for

Use this skill to establish project context for a new or existing repository, import supplied historical material, update a handoff after material work, or audit records for drift. Its four workflows are:

- Bootstrap and discovery: inspect the repository, detect existing records, and propose the smallest useful context set before writing.
- Historical source import: turn supplied or authorized chats, notes, issues, PRs, or specifications into labeled, reviewable summaries and source-manifest entries.
- Maintenance and handoff: draft evidence-based updates after research, implementation, validation, or review.
- Reconciliation and audit: compare project records with implementation, tests, Git history, approved intent, and relevant framework artifacts.

The default durable output is `docs/project-context/`: `README.md`, `INDEX.md`, `PROJECT_STATE.md`, `DECISIONS.md`, `HANDOFF.md`, and `SOURCE_MANIFEST.md`. Architecture, risk, framework-integration, chat-summary, and reconciliation records are added only when the project needs them. Existing documentation structures are mapped rather than overwritten or duplicated.

## Evidence and framework boundaries

The skill keeps **Verified**, **Approved**, **Implemented**, **Proposed**, **Inferred**, **Unresolved**, and **Superseded** claims distinct. For example, a chat is not automatically an approved decision, code does not automatically prove approved intent, and a passing test proves only the checks that ran.

It is framework-neutral. Plain Git repositories are fully supported. When present, BMAD, OpenSpec, and Spec Kit artifacts are treated as project-specific sources and linked without replacing, installing, configuring, or modifying those frameworks. Agent memory may assist recall, but is never assumed to be shared, complete, current, or authoritative.

The skill does not copy raw chats, credentials, tokens, PHI, PII, sensitive laboratory data, confidential material, or proprietary content into Git by default. It also does not claim access to unsupplied chats, private memory, or external systems.

## Quick start

Inspect first, then use a dry run before creating files:

```text
python scripts/inspect_project_context.py --target <repository>
python scripts/scaffold_project_context.py --target <repository> --dry-run
```

After review and approval, remove `--dry-run` to create only missing standard records. See [SKILL.md](SKILL.md), [references](references/), [templates](templates/), [examples](examples/), and [scripts](scripts/) for the detailed operating model.

