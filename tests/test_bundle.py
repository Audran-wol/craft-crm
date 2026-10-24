"""Mutate disposable copies so broken releases fail with useful diagnostics."""
import json
from pathlib import Path
import runpy
import shutil
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / 'skills/craft-crm'
validate = runpy.run_path(str(SKILL / 'scripts/validate_bundle.py'))['validate']


class BundleTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name) / 'craft-crm'
        shutil.copytree(SKILL, self.root)

    def assert_invalid(self, message):
        result = validate(self.root)
        self.assertFalse(result['valid'])
        self.assertTrue(any(message in error for error in result['errors']), result)

    def alter_sources(self, mutation):
        path = self.root / 'references/sources.json'
        content = json.loads(path.read_text())
        mutation(content)
        path.write_text(json.dumps(content))

    def test_current_bundle(self):
        self.assertTrue(validate(self.root)['valid'])

    def test_missing_required_file(self):
        (self.root / 'assets/icon.svg').unlink()
        self.assert_invalid('missing assets/icon.svg')

    def test_malformed_json(self):
        (self.root / 'references/sources.json').write_text('{')
        self.assert_invalid('invalid JSON')

    def test_wrong_source_shape(self):
        self.alter_sources(lambda c: c.update(sources=[None]))
        self.assert_invalid('must be an object')

    def test_missing_source_url_does_not_crash(self):
        self.alter_sources(lambda c: c['sources'][0].pop('url'))
        self.assert_invalid('invalid url')

    def test_duplicate_source_id(self):
        self.alter_sources(lambda c: c['sources'][1].update(id=c['sources'][0]['id']))
        self.assert_invalid('duplicate source ID')

    def test_duplicate_source_url(self):
        self.alter_sources(lambda c: c['sources'][1].update(url=c['sources'][0]['url'] + '/'))
        self.assert_invalid('duplicate source URL')

    def test_source_url_requires_host(self):
        self.alter_sources(lambda c: c['sources'][0].update(url='https:relative'))
        self.assert_invalid('absolute HTTPS URL')

    def test_bad_source_date(self):
        self.alter_sources(lambda c: c['sources'][0].update(reviewed_at='2026-02-30'))
        self.assert_invalid('ISO date')

    def test_unknown_source_reference(self):
        with (self.root / 'SKILL.md').open('a') as file:
            file.write('\nSee S99.\n')
        self.assert_invalid('unknown source S99')

    def test_broken_local_link(self):
        with (self.root / 'SKILL.md').open('a') as file:
            file.write('\n[missing](references/absent.md)\n')
        self.assert_invalid('broken local link')

    def test_escaping_local_link(self):
        with (self.root / 'SKILL.md').open('a') as file:
            file.write('\n[outside](../outside.md)\n')
        self.assert_invalid('escapes skill')

    def test_symlink_cannot_import_outside_instructions(self):
        file = self.root / 'references/examples.md'
        file.unlink()
        try:
            file.symlink_to(ROOT / 'README.md')
        except (OSError, NotImplementedError) as error:
            self.skipTest(f'Symlink creation is unavailable: {error}')
        self.assert_invalid('local regular file')

    def test_missing_frontmatter(self):
        (self.root / 'SKILL.md').write_text('# Missing metadata\n')
        self.assert_invalid('missing YAML frontmatter')

    def test_invalid_invocation_metadata(self):
        path = self.root / 'agents/openai.yaml'
        path.write_text(path.read_text().replace('$craft-crm', 'some skill'))
        self.assert_invalid('must mention $craft-crm')

    def test_invalid_icon_path(self):
        path = self.root / 'agents/openai.yaml'
        path.write_text(path.read_text().replace('./assets/icon.svg', '../outside.svg'))
        self.assert_invalid('invalid icon path')

    def test_malformed_metadata_container(self):
        path = self.root / 'agents/openai.yaml'
        path.write_text(path.read_text().replace('"interface": {', '"interface": ['))
        self.assert_invalid('invalid JSON')

    def test_metadata_fields_under_wrong_parent(self):
        path = self.root / 'agents/openai.yaml'
        content = json.loads(path.read_text())
        content.update(content.pop('interface'))
        path.write_text(json.dumps(content))
        self.assert_invalid('interface must be an object')

    def test_unsafe_svg(self):
        (self.root / 'assets/icon.svg').write_text('<svg xmlns="http://www.w3.org/2000/svg" onload="alert(1)"><script>1</script></svg>')
        self.assert_invalid('embedded script')
        self.assert_invalid('executable SVG attribute')

    def test_audit_template_cannot_start_with_passes(self):
        path = self.root / 'assets/audit-template.json'
        content = json.loads(path.read_text())
        content['gates'][0]['status'] = 'pass'
        path.write_text(json.dumps(content))
        self.assert_invalid('blank gates must be unknown')

    def test_audit_template_weights(self):
        path = self.root / 'assets/audit-template.json'
        content = json.loads(path.read_text())
        content['dimensions'][0]['weight'] = 100
        path.write_text(json.dumps(content))
        self.assert_invalid('incorrect weights')


if __name__ == '__main__':
    unittest.main()
