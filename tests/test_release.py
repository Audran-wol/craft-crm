"""Release packaging should be reproducible and contain only intended artifacts."""
import hashlib
from pathlib import Path
import runpy
import shutil
import tempfile
import unittest
import zipfile

ROOT = Path(__file__).resolve().parents[1]
MODULE = runpy.run_path(str(ROOT / 'scripts/package_release.py'))


class ReleaseTests(unittest.TestCase):
    def test_reproducible_and_clean_archive(self):
        with tempfile.TemporaryDirectory() as temp:
            first, digest, count = MODULE['build_archive'](ROOT, Path(temp) / 'one')
            second, second_digest, _ = MODULE['build_archive'](ROOT, Path(temp) / 'two')
            self.assertEqual(first.read_bytes(), second.read_bytes())
            self.assertEqual(digest, second_digest)
            self.assertEqual(digest, hashlib.sha256(first.read_bytes()).hexdigest())
            self.assertIn(digest, first.with_suffix('.zip.sha256').read_text())
            with zipfile.ZipFile(first) as archive:
                names = archive.namelist()
                self.assertEqual(len(names), count)
                self.assertIn('craft-crm/skills/craft-crm/SKILL.md', names)
                self.assertIn('craft-crm/tests/test_score_audit.py', names)
                self.assertFalse(any('__pycache__' in name or '/dist/' in name or '/.git/' in name for name in names))
                self.assertTrue(all(name.startswith('craft-crm/') and '..' not in Path(name).parts for name in names))

    def test_release_rejects_symlinked_file(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp) / 'source'
            shutil.copytree(ROOT, root, ignore=shutil.ignore_patterns('dist', '__pycache__'))
            path = root / 'skills/craft-crm/assets/icon.svg'
            path.unlink()
            try:
                path.symlink_to(ROOT / 'skills/craft-crm/assets/icon.svg')
            except (OSError, NotImplementedError) as error:
                self.skipTest(f'Symlink creation is unavailable: {error}')
            with self.assertRaises(ValueError):
                MODULE['release_files'](root)

    def test_release_version_required(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            (root / 'VERSION').write_text('latest')
            with self.assertRaises(ValueError):
                MODULE['build_archive'](root, root / 'dist')

    def test_release_rejects_output_inside_source_tree(self):
        for tree in MODULE['TREES']:
            with self.subTest(tree=tree), self.assertRaises(ValueError):
                MODULE['build_archive'](ROOT, ROOT / tree / 'release-output')

    def test_nested_generated_directories_are_excluded(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp) / 'source'
            shutil.copytree(ROOT, root, ignore=shutil.ignore_patterns('dist', '__pycache__'))
            for name in ('.git', 'dist', 'node_modules', '.venv', '__pycache__'):
                path = root / 'evaluations' / 'fixture' / name / 'do-not-ship.txt'
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_text('excluded')
            files = MODULE['release_files'](root)
            self.assertFalse(any(path.name == 'do-not-ship.txt' for path in files))

    def test_private_trial_results_are_not_published(self):
        files = MODULE['release_files'](ROOT)
        self.assertFalse(any(path.relative_to(ROOT).parts[:2] == ('evaluations', 'results') for path in files))
        self.assertIn(ROOT / 'LICENSE', files)


if __name__ == '__main__':
    unittest.main()
