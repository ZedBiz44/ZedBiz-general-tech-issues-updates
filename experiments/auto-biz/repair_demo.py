"""Synthetic repair demonstration using unchanged public Shopify reference data.

Outputs JSON and Markdown only. Not a store importer or customer repair result.
"""
import copy
import csv
import hashlib
import json
from pathlib import Path

from catalog_probe import inspect

ALLOWED = {'Variant Price', 'Variant Grams', 'Title', 'Vendor'}


def digest(rows):
    return hashlib.sha256(json.dumps(rows, sort_keys=True, ensure_ascii=False).encode()).hexdigest()


def apply_reviewed(rows, changes, expected_digest):
    if digest(rows) != expected_digest:
        raise ValueError('Input differs from the reviewed version; review again.')
    result = copy.deepcopy(rows)
    seen = set()
    for change in changes:
        index, column = change['index'], change['column']
        if column not in ALLOWED or not change.get('source'):
            raise ValueError('Unapproved field or missing source reference.')
        if not isinstance(index, int) or not 0 <= index < len(result):
            raise ValueError('Record not found.')
        if (index, column) in seen:
            raise ValueError('Conflicting repeat change.')
        seen.add((index, column))
        if column not in result[index] or result[index][column] != change['before']:
            raise ValueError('Expected original value does not match.')
        if not isinstance(change['after'], str):
            raise ValueError('CSV field values must remain text.')
        result[index][column] = change['after']
    return result


def rejected(fn):
    try:
        fn()
    except ValueError:
        return True
    raise AssertionError('Expected the change to be rejected.')


def run():
    root = Path(__file__).resolve().parent
    source = root / 'evidence' / 'shopify-apparel-original.csv'
    source_bytes = source.read_bytes()
    with source.open(encoding='utf-8-sig', newline='') as f:
        reader = csv.DictReader(f)
        reference = list(reader)
        headers = reader.fieldnames
    assert reference and not inspect(reference, headers)
    working = copy.deepcopy(reference)
    # All three faults below are deliberately introduced, not found in the source.
    working[0]['Variant Price'] = 'CAD ' + reference[0]['Variant Price']
    working[1]['Variant Grams'] = reference[1]['Variant Grams'] + ' grams'
    working[2]['Variant Price'] = 'TBD'
    fields = [(0, 'Variant Price'), (1, 'Variant Grams'), (2, 'Variant Price')]
    changes = [{'index': i, 'column': c, 'before': working[i][c],
                'after': reference[i][c],
                'source': f'Public Shopify sample, CSV record {i+2}, {c}'}
               for i, c in fields]
    fingerprint = digest(working)
    partial = apply_reviewed(working, changes[:2], fingerprint)
    assert partial[2]['Variant Price'] == 'TBD'
    assert len(inspect(partial, headers)) == 1
    repaired = apply_reviewed(working, changes, fingerprint)
    assert repaired == reference, 'Every cell must match the independent reference.'
    assert digest(working) == fingerprint, 'Working source must not change in place.'
    assert not inspect(repaired, headers)
    bad_field = {**changes[0], 'column': 'Handle'}
    missing_source = {**changes[0], 'source': ''}
    wrong_before = {**changes[0], 'before': 'unexpected'}
    checks = {
        'stale_input_rejected': rejected(lambda: apply_reviewed(partial, changes, fingerprint)),
        'identity_edit_rejected': rejected(lambda: apply_reviewed(working, [bad_field], fingerprint)),
        'missing_source_rejected': rejected(lambda: apply_reviewed(working, [missing_source], fingerprint)),
        'wrong_before_value_rejected': rejected(lambda: apply_reviewed(working, [wrong_before], fingerprint)),
        'duplicate_change_rejected': rejected(lambda: apply_reviewed(working, [changes[0], changes[0]], fingerprint)),
        'rerun_rejected_without_new_review': rejected(lambda: apply_reviewed(repaired, changes, fingerprint)),
        'unapproved_value_preserved': partial[2]['Variant Price'] == 'TBD',
        'full_cell_reconciliation': repaired == reference,
        'no_in_place_mutation': digest(working) == fingerprint,
        'original_file_unchanged': source_bytes == source.read_bytes(),
    }
    assert all(checks.values())
    result = {
        'classification': 'Synthetic demonstration; three deliberately introduced faults.',
        'source_url': 'https://raw.githubusercontent.com/shopifypartners/product-csvs/master/apparel.csv',
        'source_sha256': hashlib.sha256(source_bytes).hexdigest(),
        'records': len(reference), 'columns': len(headers),
        'changes': changes, 'checks': checks,
        'partial_findings': inspect(partial, headers),
        'final_findings': inspect(repaired, headers),
        'status': 'Offline demonstration complete; customer validation and live import untested.',
    }
    (root / 'evidence' / 'repair-demo.json').write_text(json.dumps(result, indent=2), encoding='utf-8')
    table = '\n'.join(f"| {c['index']+2} | {c['column']} | {c['before']} | {c['after']} |" for c in changes)
    report = f'''# Catalog repair demonstration

Synthetic example using Shopify's public sample. These defects were deliberately introduced; this is not customer work.

## Changes traced to the source

| CSV record | Field | Demonstration input | Verified source value |
|---|---|---|---|
{table}

## What was verified

- The partial run corrected only the first two reviewed values. The unresolved price stayed TBD and remained flagged.
- The final run used all three source-verified values and matched all {len(reference)} records and {len(headers)} columns of the reference.
- Product identifiers, variant options, SKUs, image links and all unrelated cells remained unchanged.
- Ten checks passed, including rejecting stale input, identity changes, missing source references and repeat application.
- The original file remained unchanged.

## Limits

This demonstrates controlled offline edits and reconciliation. It does not establish live import success, customer demand, production-scale reliability or a guaranteed turnaround. A real job requires an authorized source, agreed mappings and destination-specific checks.

Source: https://raw.githubusercontent.com/shopifypartners/product-csvs/master/apparel.csv
'''
    (root / 'REPAIR-DEMO.md').write_text(report, encoding='utf-8')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    run()
