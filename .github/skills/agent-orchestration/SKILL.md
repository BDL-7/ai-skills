---
name: agent-orchestration
description: Decide whether to delegate, assign bounded agent work, coordinate evidence, and arrange independent review. Use for requests involving primary agents, subagents, delegation, parallel work, or agent review.
---

# Agent Orchestration

The primary agent is the user's single point of contact. First establish the outcome, constraints, permissions, evidence, validation, and stop conditions. Keep work single-agent when delegation provides no material benefit.

When delegating, assign one bounded objective, exact scope, acceptance criteria, permitted actions, evidence, validation, deliverable, and stop conditions. Give each change set one write owner and never overlap write scopes. Scouts are read-only investigators; implementers own one change set; reviewers are independent and read-only. Do not permit nested delegation unless explicitly authorized.

Create independent reviewers as siblings with fresh context and a neutral review packet. Reconcile results with repository evidence, tests, configuration, or reproducible output, not confidence or memory. Stop redundant, complete, blocked, or out-of-scope agents promptly. Read [references/delegation-decision.md](references/delegation-decision.md) before delegating and use the matching template.

Do not expose raw transcripts or reasoning by default. Preserve user-owned changes and repository instructions. Do not commit, publish, deploy, delete, or otherwise change external state without explicit authorization.
