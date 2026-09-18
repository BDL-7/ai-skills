import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / '.github' / 'skills'

class RepositoryIntegrityTests(unittest.TestCase):
    def test_skills_have_required_frontmatter(self):
        for skill in SKILLS.glob('*/SKILL.md'):
            text = skill.read_text(encoding='utf-8')
            self.assertTrue(text.startswith('---\n'), skill)
            self.assertRegex(text, r'(?m)^name: .+', skill)
            self.assertRegex(text, r'(?m)^description: .+', skill)
    def test_internal_markdown_links_resolve(self):
        for path in SKILLS.rglob('*.md'):
            for link in re.findall(r'\[[^]]+\]\(([^)#]+)', path.read_text(encoding='utf-8')):
                self.assertTrue((path.parent / link).exists(), f'{path}: {link}')

if __name__ == '__main__':
    unittest.main()
