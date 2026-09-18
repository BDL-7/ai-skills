"""Read-only inventory of paths that may inform project context."""
from __future__ import annotations
import argparse
from pathlib import Path

MARKERS = {"OpenSpec": ("openspec",), "BMAD": ("_bmad", "bmad"), "Spec Kit": ("specs", "constitution.md")}
def main() -> int:
    p = argparse.ArgumentParser(description="Inspect names and paths only; never reads source contents.")
    p.add_argument("--target", required=True, type=Path); args = p.parse_args()
    if not args.target.is_dir(): p.error("--target must be an existing directory")
    paths = [x.relative_to(args.target).as_posix() for x in args.target.rglob("*") if x.is_file()]
    context = [x for x in paths if x.startswith("docs/project-context/")]
    print("context files:", ", ".join(context) or "none")
    for name, markers in MARKERS.items():
        matches = [x for x in paths if any(m.lower() in x.lower() for m in markers)]
        print(f"{name}: {', '.join(matches) or 'not detected'}")
    print("generic Git evidence:", "present" if (args.target / ".git").exists() else "not detected")
    missing = [n for n in ("README.md", "INDEX.md", "PROJECT_STATE.md", "DECISIONS.md", "HANDOFF.md", "SOURCE_MANIFEST.md") if f"docs/project-context/{n}" not in context]
    print("gaps:", ", ".join(missing) or "none")
    return 0
if __name__ == "__main__": raise SystemExit(main())

