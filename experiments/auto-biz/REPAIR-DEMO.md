# Catalog repair demonstration

Synthetic example using Shopify's public sample. These defects were deliberately introduced; this is not customer work.

## Changes traced to the source

| CSV record | Field | Demonstration input | Verified source value |
|---|---|---|---|
| 2 | Variant Price | CAD 50 | 50 |
| 3 | Variant Grams | 0 grams | 0 |
| 4 | Variant Price | TBD | 60 |

## What was verified

- The partial run corrected only the first two reviewed values. The unresolved price stayed TBD and remained flagged.
- The final run used all three source-verified values and matched all 22 records and 46 columns of the reference.
- Product identifiers, variant options, SKUs, image links and all unrelated cells remained unchanged.
- Ten checks passed, including rejecting stale input, identity changes, missing source references and repeat application.
- The original file remained unchanged.

## Limits

This demonstrates controlled offline edits and reconciliation. It does not establish live import success, customer demand, production-scale reliability or a guaranteed turnaround. A real job requires an authorized source, agreed mappings and destination-specific checks.

Source: https://raw.githubusercontent.com/shopifypartners/product-csvs/master/apparel.csv
