# Agent Orchestration skill

## Summary

`agent-orchestration` helps one primary agent decide when help is useful, give subagents safe bounded work, independently review outcomes, and return one evidence-based answer.

## When to use it

Use it for a bounded investigation, non-overlapping implementation, independent review, safe parallel work, agent handoff, redirection, or reconciliation. Do not use it merely to create activity: a small task should stay with the primary agent.

## Operating sequence

1. Decide whether delegation has a clear benefit.
2. Assign one objective and exact boundary to each agent.
3. Keep write ownership non-overlapping and preserve user changes.
4. Review material implementations with a fresh, neutral reviewer.
5. Reconcile claims using evidence and report one coherent result.

The package includes decision and safety references, assignment/review templates, and examples for single-agent, parallel scouting, implementation plus review, and conflicting findings. It is framework-neutral and supports any available agent capability without assuming a model, shared memory, or nested delegation.

## Ready-to-use assignment examples

Use the examples as a starting point, replacing bracketed fields with the actual task boundary:

- [Scout assignment](examples/assignment-prompts/SCOUT.md): a read-only investigation.
- [Implementer assignment](examples/assignment-prompts/IMPLEMENTER.md): one owned change set.
- [Independent reviewer packet](examples/assignment-prompts/REVIEWER.md): a fresh-context review.

Do not send all three automatically. Use the delegation decision reference first, and assign only the roles that materially improve the outcome.

