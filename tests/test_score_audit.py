"""Exercise evidence and scope invariants, including the command-line interface."""
import copy
import json
from pathlib import Path
import runpy
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / 'skills/craft-crm/scripts/score_audit.py'
TEMPLATE = ROOT / 'skills/craft-crm/assets/audit-template.json'
evaluate = runpy.run_path(str(SCRIPT))['evaluate']


def complete_audit():
    data = json.loads(TEMPLATE.read_text())
    data.update(scope='Synthetic test fixture only', evidence_date='2026-10-22')
    for gate in data['gates']:
        gate.update(status='pass', evidence='Synthetic observed outcome')
    for dimension in data['dimensions']:
        dimension.update(score=4, evidence='Synthetic observed outcome')
    return data


class AuditTests(unittest.TestCase):
    def setUp(self):
        self.audit = complete_audit()

    def test_complete_audit(self):
        result = evaluate(self.audit)
        self.assertEqual(result['status'], 'ready')
        self.assertTrue(result['ready_within_reviewed_scope'])
        self.assertEqual(result['score'], 100)
        self.assertEqual(result['evidence_coverage_percent'], 100)

    def test_failed_and_unknown_gates_block_perfect_score(self):
        for status in ('fail', 'unknown'):
            with self.subTest(status=status):
                self.audit['gates'][0]['status'] = status
                result = evaluate(self.audit)
                self.assertEqual(result['score'], 100)
                self.assertFalse(result['ready_within_reviewed_scope'])
                self.assertEqual(result['status'], 'not_ready')

    def test_human_summary_distinguishes_findings_from_crash(self):
        self.audit['gates'][0]['status'] = 'unknown'
        with tempfile.TemporaryDirectory() as temp:
            path = Path(temp) / 'audit.json'
            path.write_text(json.dumps(self.audit))
            result = subprocess.run([sys.executable, str(SCRIPT), str(path), '--format', 'text'], capture_output=True, text=True)
            self.assertEqual(result.returncode, 1)
            self.assertTrue(result.stdout.startswith('NOT READY'))
            self.assertIn('not a script crash', result.stdout)
            self.assertEqual(result.stderr, '')

    def test_human_summary_for_ready_review(self):
        with tempfile.TemporaryDirectory() as temp:
            path = Path(temp) / 'audit.json'
            path.write_text(json.dumps(self.audit))
            result = subprocess.run([sys.executable, str(SCRIPT), str(path), '--format', 'text'], capture_output=True, text=True)
            self.assertEqual(result.returncode, 0)
            self.assertTrue(result.stdout.startswith('READY WITHIN REVIEWED SCOPE'))

    def test_missing_dimension_is_unverified_not_a_pass(self):
        self.audit['dimensions'][0]['score'] = None
        result = evaluate(self.audit)
        self.assertFalse(result['ready_within_reviewed_scope'])
        self.assertEqual(result['evidence_coverage_percent'], 75)
        self.assertEqual(result['score'], 75)

    def test_low_score_blocks_even_with_all_gates_passed(self):
        for dimension in self.audit['dimensions']:
            dimension['score'] = 3
        self.assertFalse(evaluate(self.audit)['ready_within_reviewed_scope'])

    def test_weighted_arithmetic(self):
        self.audit['dimensions'][0]['score'] = 2
        self.assertEqual(evaluate(self.audit)['score'], 87.5)

    def test_excluded_dimension_renormalizes_weights(self):
        self.audit['dimensions'][0].update(applicable=False, score=None, reason='Outside this review scope')
        result = evaluate(self.audit)
        self.assertEqual(result['score'], 100)
        self.assertEqual(result['applicable_weight'], 75)
        self.assertTrue(result['ready_within_reviewed_scope'])

    def test_gate_exclusion_requires_reason(self):
        self.audit['gates'][0].update(status='not_applicable', reason='')
        with self.assertRaises(ValueError):
            evaluate(self.audit)
        self.audit['gates'][0]['reason'] = 'No pre-existing behavior in this new-build fixture'
        self.assertTrue(evaluate(self.audit)['ready_within_reviewed_scope'])

    def test_all_gates_excluded_is_invalid(self):
        for gate in self.audit['gates']:
            gate.update(status='not_applicable', reason='Excluded')
        with self.assertRaises(ValueError):
            evaluate(self.audit)

    def test_all_dimensions_excluded_is_invalid(self):
        for dimension in self.audit['dimensions']:
            dimension.update(applicable=False, score=None, reason='Excluded')
        with self.assertRaises(ValueError):
            evaluate(self.audit)

    def test_gate_evidence_required_for_pass_and_fail(self):
        for status in ('pass', 'fail'):
            self.audit['gates'][0].update(status=status, evidence=' ')
            with self.assertRaises(ValueError):
                evaluate(self.audit)

    def test_scoring_evidence_required(self):
        self.audit['dimensions'][0]['evidence'] = ''
        with self.assertRaises(ValueError):
            evaluate(self.audit)

    def test_invalid_scores(self):
        for value in (-1, 5, 2.5, True, '4'):
            with self.subTest(value=value):
                self.audit['dimensions'][0]['score'] = value
                with self.assertRaises(ValueError):
                    evaluate(self.audit)

    def test_weights_cannot_be_changed(self):
        self.audit['dimensions'][0]['weight'] = 99
        with self.assertRaises(ValueError):
            evaluate(self.audit)

    def test_duplicate_gate_is_invalid(self):
        self.audit['gates'][-1] = copy.deepcopy(self.audit['gates'][0])
        with self.assertRaises(ValueError):
            evaluate(self.audit)

    def test_duplicate_dimension_is_invalid(self):
        self.audit['dimensions'][-1] = copy.deepcopy(self.audit['dimensions'][0])
        with self.assertRaises(ValueError):
            evaluate(self.audit)

    def test_unfilled_template_is_invalid(self):
        with self.assertRaises(ValueError):
            evaluate(json.loads(TEMPLATE.read_text()))

    def test_excluded_dimension_cannot_keep_score(self):
        self.audit['dimensions'][0].update(applicable=False, reason='Excluded')
        with self.assertRaises(ValueError):
            evaluate(self.audit)

    def test_cli_exit_codes_and_machine_readable_output(self):
        with tempfile.TemporaryDirectory() as temp:
            path = Path(temp) / 'audit.json'
            for label, content, expected in (
                ('complete', json.dumps(self.audit), 0),
                ('incomplete', json.dumps(dict(self.audit, gates=[dict(g, status='unknown') for g in self.audit['gates']])), 1),
                ('malformed', '{', 2),
                ('wrong_shape', '[]', 2),
                ('bad_id', json.dumps(dict(self.audit, gates=[dict(g, id=[]) for g in self.audit['gates']])), 2),
            ):
                with self.subTest(label=label):
                    path.write_text(content)
                    result = subprocess.run([sys.executable, str(SCRIPT), str(path)], capture_output=True, text=True)
                    self.assertEqual(result.returncode, expected, result.stderr)
                    json.loads(result.stdout if expected < 2 else result.stderr)
            result = subprocess.run([sys.executable, str(SCRIPT), str(path.parent / 'absent')], capture_output=True, text=True)
            self.assertEqual(result.returncode, 2)
            self.assertIn('error', json.loads(result.stderr))


if __name__ == '__main__':
    unittest.main()
