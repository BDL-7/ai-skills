import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1] / '.github/skills/agent-orchestration'
class AgentOrchestrationTests(unittest.TestCase):
    def test_entrypoint_and_required_references(self):
        self.assertTrue((ROOT / 'SKILL.md').read_text(encoding='utf-8').startswith('---\n'))
        for name in ('delegation-decision.md', 'assignment-contract.md', 'independent-review.md', 'safety-and-write-ownership.md'):
            self.assertTrue((ROOT / 'references' / name).is_file())
    def test_roles_safety_and_review_are_explicit(self):
        text = (ROOT / 'SKILL.md').read_text(encoding='utf-8')
        review = (ROOT / 'references/independent-review.md').read_text(encoding='utf-8')
        self.assertIn('never overlap write scopes', text); self.assertIn('fresh context', review)
    def test_scenarios_and_templates_cover_required_boundaries(self):
        for name in ('single-agent-task', 'parallel-read-only-investigation', 'implementation-and-independent-review', 'conflicting-agent-findings'):
            self.assertTrue((ROOT / 'examples' / name / 'README.md').is_file())
        self.assertIn('Stop conditions', (ROOT / 'templates/IMPLEMENTER_ASSIGNMENT.md').read_text(encoding='utf-8'))
if __name__ == '__main__': unittest.main()
