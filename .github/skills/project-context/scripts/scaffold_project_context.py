"""Safely scaffold missing project-context records (standard library only)."""
from __future__ import annotations
import argparse
from pathlib import Path

STANDARD = ("README.md", "INDEX.md", "PROJECT_STATE.md", "DECISIONS.md", "HANDOFF.md", "SOURCE_MANIFEST.md")
EXPANDED = ("ARCHITECTURE.md", "RISKS_ASSUMPTIONS_OPEN_QUESTIONS.md", "FRAMEWORK_INTEGRATION.md")

def template_dir() -> Path:
    return Path(__file__).resolve().parents[1] / "templates"

def main() -> int:
    parser = argparse.ArgumentParser(description="Create missing project-context files without network access.")
    parser.add_argument("--target", required=True, type=Path, help="Repository directory (required).")
    parser.add_argument("--dry-run", action="store_true", help="Report actions without writing.")
    parser.add_argument("--expanded", action="store_true", help="Include optional architecture, risks, and framework records.")
    parser.add_argument("--overwrite", action="store_true", help="Explicitly replace existing files.")
    args = parser.parse_args()
    if not args.target.is_dir():
        parser.error("--target must be an existing directory")
    destination = args.target / "docs" / "project-context"
    names = STANDARD + (EXPANDED if args.expanded else ())
    created = skipped = blocked = 0
    for name in names:
        output, source = destination / name, template_dir() / name
        if output.exists() and not args.overwrite:
            print(f"SKIP {output} (exists)"); skipped += 1; continue
        if not source.is_file():
            print(f"BLOCK {source} (template missing)"); blocked += 1; continue
        print(f"{'WOULD CREATE' if args.dry_run else 'CREATE'} {output}")
        if not args.dry_run:
            output.parent.mkdir(parents=True, exist_ok=True)
            output.write_text(source.read_text(encoding="utf-8"), encoding="utf-8")
        created += 1
    print(f"created={created} skipped={skipped} blocked={blocked} dry_run={args.dry_run}")
    return 2 if blocked else 0

if __name__ == "__main__":
    raise SystemExit(main())

