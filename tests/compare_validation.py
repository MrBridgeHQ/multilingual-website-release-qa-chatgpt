#!/usr/bin/env python3
"""Compare frozen synthetic observations to the oracle without modifying evidence."""
import argparse
import hashlib
import json
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
STATES = ('PASS', 'FAIL', 'BLOCKED', 'NOT_RUN', 'NOT_APPLICABLE')


def read(path):
    return json.loads(path.read_text(encoding='utf-8'))


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def counts(cases):
    found = Counter(case['status'] for case in cases)
    return {state: found[state] for state in STATES}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('mode', choices=['inspect', 'create'])
    parser.add_argument('--baseline', type=Path, required=True)
    parser.add_argument('--fixed', type=Path, required=True)
    parser.add_argument('--oracle', type=Path, default=ROOT / 'tests/oracle/expected-defects.json')
    parser.add_argument('--freeze', type=Path, required=True)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    if args.output.exists() or args.output.is_symlink():
        raise SystemExit('Output must be a new directory')
    if not args.output.parent.is_dir():
        raise SystemExit('Output parent does not exist')
    baseline, fixed, oracle, freeze = map(read, (args.baseline, args.fixed, args.oracle, args.freeze))
    for entry in freeze['files']:
        target = (ROOT / entry['path']).resolve()
        if not target.is_relative_to(ROOT) or not target.is_file():
            raise SystemExit('Frozen file missing or outside repository: ' + entry['path'])
        if digest(target) != entry['sha256'] or target.stat().st_size != entry['bytes']:
            raise SystemExit('Frozen file changed: ' + entry['path'])
    baseline_relative = args.baseline.resolve().relative_to(ROOT).as_posix()
    if not any(item['path'] == baseline_relative for item in freeze['files']):
        raise SystemExit('Baseline results are not in the freeze manifest')
    before = {case['id']: case for case in baseline['cases']}
    after = {case['id']: case for case in fixed['cases']}
    if len(before) != len(baseline['cases']) or len(after) != len(fixed['cases']):
        raise SystemExit('Duplicate case identifiers')
    if set(before) != set(after):
        raise SystemExit('Baseline and corrected case matrices differ')
    for case_id in before:
        first, second = before[case_id], after[case_id]
        for field in ('journey_id', 'language', 'profile'):
            if first[field] != second[field]:
                raise SystemExit('Retest configuration mismatch: ' + case_id + ' / ' + field)
    ticket_cases = {}
    for ticket in baseline['tickets']:
        for case_id in ticket['case_ids']:
            ticket_cases.setdefault(case_id, []).append(ticket['id'])
    comparisons = []
    known_cases = set()
    for defect in oracle['defects']:
        known_cases.update(defect['case_ids'])
        observed = []
        for case_id in defect['case_ids']:
            case = before.get(case_id)
            observed.append({'case_id': case_id, 'status': case['status'] if case else 'MISSING',
                             'ticket_ids': ticket_cases.get(case_id, []),
                             'evidence_ids': case['evidence_ids'] if case else [],
                             'retest_status': after[case_id]['status'] if case_id in after else 'MISSING'})
        detected = all(item['status'] == 'FAIL' and item['ticket_ids'] and item['evidence_ids'] for item in observed)
        comparisons.append({'oracle_id': defect['id'], 'title': defect['title'],
                            'detected': bool(detected), 'observations': observed})
    controls = oracle['control_cases']
    actual_failures = {key for key, case in before.items() if case['status'] == 'FAIL'}
    control_failures = sorted(case_id for case_id in controls if before.get(case_id, {}).get('status') == 'FAIL')
    controls_not_passed = sorted(case_id for case_id in controls if before.get(case_id, {}).get('status') != 'PASS')
    unexpected_failures = sorted(actual_failures - known_cases)
    transitions = [{'case_id': key, 'from': before[key]['status'], 'to': after[key]['status'],
                    'ticket_ids': ticket_cases.get(key, [])} for key in sorted(actual_failures)]
    control_passes = sum(after.get(key, {}).get('status') == 'PASS' for key in controls)
    summary = {
        'created_at': datetime.now(timezone.utc).isoformat(),
        'comparison_type': 'Deterministic comparison after independent baseline freeze',
        'inputs': {name: {'path': path.resolve().relative_to(ROOT).as_posix(), 'sha256': digest(path)}
                   for name, path in [('baseline', args.baseline), ('fixed', args.fixed), ('oracle', args.oracle), ('freeze', args.freeze)]},
        'freeze_files_verified': len(freeze['files']),
        'baseline': {'planned': len(before), 'counts': counts(baseline['cases']), 'tickets': len(baseline['tickets'])},
        'fixed': {'planned': len(after), 'counts': counts(fixed['cases']), 'tickets': len(fixed['tickets'])},
        'defects': comparisons,
        'detected': sum(item['detected'] for item in comparisons),
        'expected_defects': len(comparisons),
        'missed': [item['oracle_id'] for item in comparisons if not item['detected']],
        'unexpected_failed_cases': unexpected_failures,
        'control_false_failures': control_failures,
        'controls_not_passed': controls_not_passed,
        'control_cases': len(controls),
        'fixed_control_passes': control_passes,
        'transitions': transitions,
        'fail_to_pass': sum(item['to'] == 'PASS' for item in transitions),
        'limitations': [
            'Manifestation matching uses case identifiers, ticket linkage, and collected evidence; it does not prove a shared root cause.',
            'Unexpected failures require investigation and are not automatically false positives.',
            'The oracle describes this synthetic fixture only; this is not a measurement of general defect recall.',
            'Agent separation was procedural on a shared filesystem.',
        ],
    }
    summary['checks_passed'] = not (summary['missed'] or unexpected_failures or controls_not_passed) and all(item['to'] == 'PASS' for item in transitions) and control_passes == len(controls)
    print(json.dumps(summary, ensure_ascii=False, indent=2))
    if args.mode == 'create':
        args.output.mkdir()
        with (args.output / 'comparison.json').open('x', encoding='utf-8') as handle:
            json.dump(summary, handle, ensure_ascii=False, indent=2)
            handle.write('\n')
        lines = ['# Synthetic fixture comparison', '',
                 f"Frozen input files verified: {summary['freeze_files_verified']}.", '',
                 f"Observed detection: {summary['detected']}/{summary['expected_defects']} seeded defects.",
                 f"Control false failures: {len(control_failures)}/{len(controls)}.",
                 f"Observed FAIL to PASS transitions: {summary['fail_to_pass']}/{len(transitions)}.", '',
                 '| Case | Baseline | Corrected | Original tickets |', '| --- | --- | --- | --- |']
        for item in transitions:
            lines.append('| ' + ' | '.join([item['case_id'], item['from'], item['to'], ', '.join(item['ticket_ids'])]) + ' |')
        lines += ['', '## Limits', ''] + ['- ' + note for note in summary['limitations']]
        with (args.output / 'comparison.md').open('x', encoding='utf-8') as handle:
            handle.write('\n'.join(lines) + '\n')
    if not summary['checks_passed']:
        raise SystemExit(1)


if __name__ == '__main__':
    main()
