# Project Context skill

## Summary

`project-context` creates a small, durable, reviewable record of what a project is, what is known, what has been decided, and what should happen next. It keeps that knowledge with the repository so a new contributor or agent can orient quickly without relying on a previous chat, private memory, or code alone.

## When to use this skill

Use it when you need to:

- establish context for a new or existing repository;
- turn supplied chats, notes, issues, pull requests, or specifications into reviewable project records;
- prepare a concise handoff after research, planning, implementation, validation, or review; or
- check whether project records have drifted from code, tests, delivery history, approved intent, or framework artifacts.

## What it produces

The default context layer is `docs/project-context/`:

| Record | Answers |
| --- | --- |
| `README.md` and `INDEX.md` | What is this context layer and where should I start? |
| `PROJECT_STATE.md` | What is the project purpose, current status, active work, risk, and next approved action? |
| `DECISIONS.md` | What was decided, by whom, why, and what supersedes it? |
| `HANDOFF.md` | What does the next contributor need to read, validate, avoid assuming, and do next? |
| `SOURCE_MANIFEST.md` | Which sources support the records, and how may they be handled? |

Architecture, risk, framework-integration, chat-summary, and reconciliation records are added only when useful. The skill maps to established documentation instead of overwriting it or creating a competing status system.

## How it works

1. **Bootstrap and discovery**: inspect the repository, detect existing records and relevant framework artifacts, then propose the smallest useful context set before writing.
2. **Historical source import**: register each supplied or authorized source, extract durable facts and questions into a reviewable summary, and propose separate record updates.
3. **Maintenance and handoff**: draft evidence-based updates after material work and keep the next-person handoff short and operational.
4. **Reconciliation and audit**: compare records with implementation, tests, Git history, approved sources, and framework artifacts; report mismatches without silently rewriting history.

## Evidence rules

Every material claim is labeled **Verified**, **Approved**, **Implemented**, **Proposed**, **Inferred**, **Unresolved**, or **Superseded**. These labels are not interchangeable:

- A chat is working context, not automatically an approved decision.
- Code shows current implementation, not necessarily approved intent.
- A passing test verifies the checks that ran, not every user need.
- Conflicting sources remain unresolved until the appropriate evidence or decision is available.

## Framework, memory, and safety boundaries

The skill works for plain Git projects and does not require BMAD, OpenSpec, Spec Kit, or agent memory. When framework artifacts are present, it treats them as project-specific sources and links them without installing, configuring, replacing, or modifying their framework. Agent memory can help recall, but is never assumed to be shared, complete, current, portable, or authoritative.

It uses only supplied or authorized sources. It does not copy raw chats, credentials, tokens, PHI, PII, sensitive laboratory data, confidential material, or proprietary content into Git by default.

## Quick start

Inspect first, then preview the standard records without writing:

```text
python scripts/inspect_project_context.py --target <repository>
python scripts/scaffold_project_context.py --target <repository> --dry-run
```

After review and approval, remove `--dry-run` to create only missing standard records. Use [SKILL.md](SKILL.md) for the operating model, [references](references/) for detailed guidance, [templates](templates/) for record formats, and [scripts](scripts/) for safe local helpers.

