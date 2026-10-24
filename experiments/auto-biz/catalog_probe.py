"""Read-only catalog preflight prototype. Does not certify or perform an import.

Run with a Shopify product CSV path; outputs JSON to stdout. No third-party deps.
Supports the legacy and current column names used by the checks below.
"""
import argparse
import copy
import csv
import hashlib
import json
import re
from pathlib import Path


ALIASES = {
    'handle': ('URL handle', 'Handle'),
    'sku': ('SKU', 'Variant SKU'),
    'price': ('Price', 'Variant Price'),
    'weight': ('Weight value (grams)', 'Variant Grams'),
    **{f'option{i}_{kind}': (f'Option{i} {kind}', f'Option{i} {kind.title()}')
       for i in range(1, 4) for kind in ('name', 'value')},
}


def inspect(rows, headers):
    issues, seen, sku_rows, option_names = [], {}, {}, {}
    columns = {key: next((h for h in names if h in headers), None)
               for key, names in ALIASES.items()}

    def val(row, field):
        column = columns[field]
        return (row.get(column, '') or '') if column is not None else ''

    def flag(line, kind, detail):
        issues.append({'csv_record': line, 'check': kind, 'detail': detail})

    if 'Title' not in headers:
        flag(1, 'missing_header', 'Title is absent; this prototype expects a product CSV.')
    if columns['handle'] is None:
        flag(1, 'missing_header', 'Handle absent; required for this update-oriented review.')
    for line, row in enumerate(rows, 2):
        if None in row or any(v is None for v in row.values()):
            flag(line, 'row_width', 'Row field count differs from header count.')
        handle = val(row, 'handle')
        # Extra image rows are legitimate and do not define another variant.
        variant = any(val(row, f) for f in ('sku', 'price', 'option1_value'))
        if variant and not handle:
            flag(line, 'missing_handle', 'Variant row has no handle.')
        for i in range(1, 4):
            if val(row, f'option{i}_name'):
                option_names[(handle, i)] = val(row, f'option{i}_name')
            if val(row, f'option{i}_value') and not option_names.get((handle, i)):
                flag(line, 'option_name', f'Option{i} value has no corresponding name.')
        if variant:
            key = (handle,) + tuple(val(row, f'option{i}_value') for i in range(1, 4))
            if key in seen:
                flag(line, 'duplicate_variant', f'Same handle/options as record {seen[key]}; review, do not delete automatically.')
            seen[key] = line
        for field in ('price', 'weight'):
            raw = val(row, field)
            if raw and not re.fullmatch(r'\d+(?:\.\d+)?', raw):
                flag(line, 'numeric_format', f'{columns[field]} is not a plain nonnegative decimal: {raw!r}.')
        sku = val(row, 'sku')
        if sku:
            if sku in sku_rows:
                flag(line, 'duplicate_sku_review', f'SKU also occurs at record {sku_rows[sku]}; not automatically an import error.')
            sku_rows[sku] = line
    return issues


def self_test():
    h = ['Handle', 'Title', 'Option1 Name', 'Option1 Value', 'Variant SKU', 'Variant Price']
    good = [dict(zip(h, ['shirt', 'Demo', 'Size', 'Small', '00017', '0'])),
            dict(zip(h, ['shirt', '', 'Size', 'Large', '00018', '19.99'])),
            dict(zip(h, ['shirt', '', '', '', '', '']))]
    original = copy.deepcopy(good)
    assert inspect(good, h) == [], 'Valid variants and image-only rows must not be flagged.'
    assert good == original and good[0]['Variant SKU'] == '00017'
    malformed = copy.deepcopy(good)
    malformed[0]['Variant Price'] = 'CAD 19,99'
    assert any(i['check'] == 'numeric_format' for i in inspect(malformed, h))
    missing = copy.deepcopy(good)
    missing[0]['Option1 Name'] = ''
    assert any(i['check'] == 'option_name' for i in inspect(missing, h))
    assert any(i['check'] == 'duplicate_variant' for i in inspect(good + [good[0]], h))
    assert any(i['check'] == 'missing_header' for i in inspect(good, h[1:]))
    assert any(i['check'] == 'row_width' for i in inspect([{**good[0], None: ['extra']}], h))
    current = {'URL handle': 'demo', 'Title': 'Demo', 'Option1 name': 'Size',
               'Option1 value': 'Small', 'SKU': '00017', 'Price': '19.99'}
    assert inspect([current], list(current)) == []
    inherited = copy.deepcopy(good)
    inherited[1]['Option1 Name'] = ''
    assert inspect(inherited, h) == [], 'Continuation variants may inherit the product option name.'
    return '9 boundary checks passed'


if __name__ == '__main__':
    p = argparse.ArgumentParser()
    p.add_argument('source', type=Path)
    args = p.parse_args()
    raw = args.source.read_bytes()
    with args.source.open(encoding='utf-8-sig', newline='') as f:
        reader = csv.DictReader(f)
        rows = list(reader)
        headers = reader.fieldnames or []
    result = {'scope': 'Read-only structural preflight; no live import, repairs or certification.',
              'source': str(args.source), 'sha256': hashlib.sha256(raw).hexdigest(),
              'records': len(rows), 'columns': len(headers),
              'tests': self_test(), 'findings': inspect(rows, headers),
              'limits': ['Does not check every Shopify rule, image availability, app data, taxes, international pricing or existing store state.',
                         'A clean result only means these limited checks found nothing.']}
    assert raw == args.source.read_bytes(), 'Source must remain unchanged.'
    print(json.dumps(result, indent=2))
