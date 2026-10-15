"""Guard cached templates and converters that only accept inline GEOIP/FINAL."""
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
CLASH = ROOT / 'Clash'


def entries(path):
    return [line for line in path.read_text().splitlines()
            if line and not line.startswith(('#', ';'))]


class RuleCompatibilityTest(unittest.TestCase):
    def test_inline_rules_only_use_supported_tail_types(self):
        inline = [line.split(',[]', 1)[1] for line in entries(CLASH / 'kclash.ini')
                  if line.startswith('ruleset=') and ',[]' in line]
        self.assertEqual(inline, ['GEOIP,CN', 'FINAL'])

    def test_cached_ai_rules_still_cover_google(self):
        google = set(entries(CLASH / 'Ruleset/Google.list'))
        ai = set(entries(CLASH / 'Ruleset/AiDomain.list'))
        self.assertTrue(google <= ai, 'Old templates have no separate Google provider')

    def test_new_template_prioritizes_dedicated_groups(self):
        lines = entries(CLASH / 'kclash.ini')
        groups = [line.split('=', 1)[1].split(',', 1)[0]
                  for line in lines if line.startswith('ruleset=')]
        self.assertLess(groups.index('📹 Youtube'), groups.index('🔎 Google'))
        self.assertLess(groups.index('🔎 Google'), groups.index('🇺🇲 美区AI'))
        for filename, expected in [('Kimi.list', 'DOMAIN-SUFFIX,kimi.com'),
                                   ('TwitterUnbreak.list', 'DOMAIN,syndication.twitter.com')]:
            self.assertEqual(entries(CLASH / 'Ruleset' / filename), [expected])
            self.assertTrue(any(line.endswith('/Ruleset/' + filename) for line in lines))


if __name__ == '__main__':
    unittest.main()
