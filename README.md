# AI Skills

Reusable, repository-hosted skills for durable and safe AI-assisted work.

## Install and discover skills

This repository is a catalog: its skills live in `.github/skills/`. Codex discovers repository skills from `.agents/skills`, so copy a selected skill into the target repository before using it. For example, from this checkout in PowerShell:

```powershell
Copy-Item -Recurse .github\skills\project-context C:\path\to\target-repo\.agents\skills\project-context
```

For a user-wide installation, copy the skill to `~/.agents/skills/<skill-name>` instead. Restart Codex if a newly copied skill does not appear. Other tools may use different skill locations; inspect their documentation rather than assuming `.agents/skills` is universal.

| Skill | Intended use | Description |
| --- | --- | --- |
| [project-context](.github/skills/project-context/README.md) | Establish, import, maintain, hand off, or audit durable project knowledge | Framework-neutral project context for projects with or without BMAD, OpenSpec, Spec Kit, or agent memory. |
| [agent-orchestration](.github/skills/agent-orchestration/README.md) | Decide, delegate, coordinate, and review agent work | Framework-neutral guidance for single-agent and multi-agent work without requiring a specific model or framework. |

Each skill is invoked explicitly by name (for example, `$project-context`) or may be selected when its description matches the task.

