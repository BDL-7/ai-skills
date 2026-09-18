---
name: project-context
description: Establish, import, maintain, hand off, or reconcile durable project knowledge without assuming a development framework. Use when asked for project context, a handoff, context audit, historical import, or context records.
---

# Project Context

Create a small, reviewable, version-controlled context layer that survives chats and contributors. Start by confirming the repository and reading its instructions, existing documentation, and context records. Do not assume access to prior chats, memory, external systems, or unsupplied source material.

Choose the smallest applicable internal workflow:

1. **Bootstrap and discovery** — inspect first, propose a dry run, then create missing records only.
2. **Historical source import** — use only supplied/authorized sources, add a manifest entry, label claims, and require review before publishing durable claims.
3. **Maintenance and handoff** — show proposed record changes after material work; obtain required approval before writing.
4. **Reconciliation and audit** — compare records with evidence, report conflicts, and never silently rewrite history.

Use the exact labels **Verified**, **Approved**, **Implemented**, **Proposed**, **Inferred**, **Unresolved**, and **Superseded**; never collapse them. Prefer `docs/project-context/` but map to established documentation instead of duplicating it. Read [references/context-standard.md](references/context-standard.md) and the workflow-specific reference before acting. Use the stdlib scripts for safe scaffolding, inspection, and mechanical validation.

Do not copy raw chats, credentials, tokens, PHI, PII, sensitive laboratory data, confidential material, or proprietary content into Git by default. Do not install or modify BMAD, OpenSpec, Spec Kit, or another framework unless specifically requested.

