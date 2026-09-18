import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1] / ".github/skills/project-context"
SCRIPTS = ROOT / "scripts"
class ProjectContextTests(unittest.TestCase):
    def run_script(self, name, *args):
        return subprocess.run([sys.executable, SCRIPTS / name, *args], text=True, capture_output=True, check=False)
    def test_help_and_dry_run(self):
        with tempfile.TemporaryDirectory() as d:
            result = self.run_script("scaffold_project_context.py", "--target", d, "--dry-run")
            self.assertEqual(result.returncode, 0); self.assertIn("WOULD CREATE", result.stdout)
            self.assertFalse((Path(d) / "docs").exists())
    def test_scaffold_refuses_overwrite(self):
        with tempfile.TemporaryDirectory() as d:
            target = Path(d); self.run_script("scaffold_project_context.py", "--target", d)
            record = target / "docs/project-context/README.md"; record.write_text("keep", encoding="utf-8")
            result = self.run_script("scaffold_project_context.py", "--target", d)
            self.assertIn("SKIP", result.stdout); self.assertEqual(record.read_text(encoding="utf-8"), "keep")
    def test_validate_missing_and_inspect_framework(self):
        with tempfile.TemporaryDirectory() as d:
            target = Path(d); (target / "openspec").mkdir()
            self.assertEqual(self.run_script("inspect_project_context.py", "--target", d).returncode, 0)
            self.assertEqual(self.run_script("validate_project_context.py", "--target", d).returncode, 1)
    def test_stale_record_and_broken_link_warn_without_rewrite(self):
        with tempfile.TemporaryDirectory() as d:
            self.run_script("scaffold_project_context.py", "--target", d)
            state = Path(d) / "docs/project-context/PROJECT_STATE.md"
            state.write_text(state.read_text(encoding="utf-8") + "\n[missing](no-such-file.md)\n", encoding="utf-8")
            result = self.run_script("validate_project_context.py", "--target", d)
            self.assertEqual(result.returncode, 0); self.assertIn("broken link", result.stdout); self.assertIn("stale placeholder", result.stdout)
    def test_import_conflict_sensitive_source_and_handoff_guidance(self):
        text = (ROOT / "references/authority-and-evidence.md").read_text(encoding="utf-8")
        privacy = (ROOT / "references/privacy-retention-and-safety.md").read_text(encoding="utf-8")
        handoff = (ROOT / "templates/HANDOFF.md").read_text(encoding="utf-8")
        summary = (ROOT / "templates/CHAT_SUMMARY.md").read_text(encoding="utf-8")
        self.assertIn("sources disagree", text); self.assertIn("raw transcripts", privacy)
        self.assertIn("Must not be assumed", handoff); self.assertIn("Source metadata", summary)
    def test_package_links_and_frontmatter(self):
        self.assertTrue((ROOT / "SKILL.md").read_text(encoding="utf-8").startswith("---\n"))
        self.assertTrue((ROOT / "references/context-standard.md").is_file())
if __name__ == "__main__": unittest.main()
