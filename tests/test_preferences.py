import json
from pathlib import Path
import sys
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
from check_preferences import validate


class PreferencesTests(unittest.TestCase):
    def setUp(self):
        self.data = json.loads((Path(__file__).resolve().parents[1] / 'research.config.example.json').read_text(encoding='utf-8'))

    def test_defaults_require_no_personal_paths(self):
        self.assertTrue(validate(self.data))
        self.assertIsNone(self.data['output_directory'])
        self.assertIsNone(self.data['time_budget_minutes'])

    def test_short_budget_and_custom_platforms(self):
        self.data.update(preferred_platforms=['GitHub'], time_budget_minutes=5)
        self.assertTrue(validate(self.data))

    def test_invalid_values_are_rejected(self):
        for field, value in [('time_budget_minutes', -1), ('time_budget_minutes', True),
                             ('time_budget_minutes', float('nan')), ('preferred_platforms', []),
                             ('research_mode', 'always-upload'), ('output_directory', '')]:
            candidate = dict(self.data)
            candidate[field] = value
            with self.subTest(field=field, value=value), self.assertRaises(ValueError):
                validate(candidate)


if __name__ == '__main__':
    unittest.main()
