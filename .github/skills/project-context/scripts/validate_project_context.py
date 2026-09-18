"""Mechanical validation only; does not claim factual correctness."""
from __future__ import annotations
import argparse, re
from pathlib import Path
REQUIRED = ("README.md", "INDEX.md", "PROJECT_STATE.md", "DECISIONS.md", "HANDOFF.md", "SOURCE_MANIFEST.md")
STATUSES = ("Verified", "Approved", "Implemented", "Proposed", "Inferred", "Unresolved", "Superseded")
def main() -> int:
    p = argparse.ArgumentParser(description="Check project-context structure, metadata, and local Markdown links.")
    p.add_argument("--target", required=True, type=Path); args = p.parse_args(); root = args.target / "docs" / "project-context"
    failures = warnings = 0
    for name in REQUIRED:
        path = root / name
        if not path.is_file(): print(f"FAIL missing {path}"); failures += 1; continue
        text = path.read_text(encoding="utf-8")
        if "Purpose:" not in text and "# " not in text: print(f"WARN purpose missing {name}"); warnings += 1
        if not any(s in text for s in STATUSES): print(f"WARN status label missing {name}"); warnings += 1
        if "YYYY-MM-DD" in text: print(f"WARN stale placeholder date {name}"); warnings += 1
        for link in re.findall(r"\[[^]]+\]\(([^)#]+)", text):
            if not (path.parent / link).exists(): print(f"WARN broken link {name}: {link}"); warnings += 1
    print(f"PASS mechanical checks complete; warnings={warnings} failures={failures}. Factual correctness is not validated.")
    return 1 if failures else 0
if __name__ == "__main__": raise SystemExit(main())

