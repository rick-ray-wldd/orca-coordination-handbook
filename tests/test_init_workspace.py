import importlib.util
import json
from pathlib import Path
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('initializer', ROOT / 'scripts/init_workspace.py')
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


class InitializerTests(unittest.TestCase):
    def test_both_locales_with_spaces_and_matching_rules(self):
        for language in ('en', 'zh-TW'):
            with self.subTest(language=language), tempfile.TemporaryDirectory() as tmp:
                dest = Path(tmp) / 'private assistant with spaces'
                module.initialize(dest, language)
                self.assertEqual(len(list((dest / 'templates').iterdir())), 14)
                self.assertEqual((dest / 'AGENTS.md').read_bytes(), (dest / 'CLAUDE.md').read_bytes())
                config = json.loads((dest / 'coordination/routing.json').read_text())
                self.assertEqual(config['default_domain'], 'triage')
                self.assertTrue(all(d['primary'] != d['reviewer'] for d in config['domains'].values()))
                self.assertTrue((dest / 'receipts/dispatch-log.md').is_file())
                self.assertIn('*', (dest / '.gitignore').read_text())

    def test_refuses_existing_directory_without_changes(self):
        with tempfile.TemporaryDirectory() as tmp:
            dest = Path(tmp) / 'existing'; dest.mkdir()
            sentinel = dest / 'keep.txt'; sentinel.write_text('keep')
            with self.assertRaises(ValueError): module.initialize(dest, 'en')
            self.assertEqual(list(dest.iterdir()), [sentinel])
            self.assertEqual(sentinel.read_text(), 'keep')

    def test_refuses_existing_file(self):
        with tempfile.TemporaryDirectory() as tmp:
            dest=Path(tmp)/'file';dest.write_text('keep')
            with self.assertRaises(ValueError):module.initialize(dest,'en')
            self.assertEqual(dest.read_text(),'keep')

    def test_refuses_broken_symlink(self):
        with tempfile.TemporaryDirectory() as tmp:
            dest=Path(tmp)/'link'
            try:dest.symlink_to(Path(tmp)/'absent',target_is_directory=True)
            except OSError:self.skipTest('Symlinks unavailable')
            with self.assertRaises(ValueError):module.initialize(dest,'en')
            self.assertTrue(dest.is_symlink())

    def test_refuses_public_repo_destination(self):
        dest=ROOT/'never-create-private-work-here'
        with self.assertRaises(ValueError):module.initialize(dest,'en')
        self.assertFalse(dest.exists())

    def test_unknown_locale_creates_nothing(self):
        with tempfile.TemporaryDirectory() as tmp:
            dest=Path(tmp)/'new'
            with self.assertRaises(ValueError):module.initialize(dest,'not-a-locale')
            self.assertFalse(dest.exists())


if __name__ == '__main__':unittest.main()
