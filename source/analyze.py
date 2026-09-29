"""Reaggregate public terminal labels; does not regrade private responses."""
import csv
import hashlib
import json
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def analyze():
    path = ROOT / 'data/paired_outcomes.csv'
    with path.open(newline='') as f:
        rows = list(csv.DictReader(f))
    assert len(rows) == 90
    assert len({(r['case_id'], r['repetition']) for r in rows}) == 90
    assert {r['repetition'] for r in rows} == {'1', '2'}
    assert set(Counter(r['case_id'] for r in rows).values()) == {2}
    expected = {
        'compound_unmet': {('valid', 'valid'): 41, ('valid', 'abstain'): 13,
                           ('abstain', 'abstain'): 8, ('invalid', 'valid'): 2},
        'sibling_disease': {('valid', 'valid'): 4, ('valid', 'abstain'): 19,
                           ('abstain', 'abstain'): 2, ('schema_failure', 'abstain'): 1},
    }
    result = {}
    assert {r['stratum'] for r in rows} == set(expected)
    for stratum, target in expected.items():
        subset = [r for r in rows if r['stratum'] == stratum]
        counts = Counter((r['fresh_outcome'], r['diagnostic_repair_outcome']) for r in subset)
        assert counts == target, (stratum, counts)
        result[stratum] = {
            'cases': len({r['case_id'] for r in subset}),
            'pairs': len(subset),
            'transitions': [dict(fresh=a, diagnostic_repair=b, count=n)
                            for (a, b), n in sorted(counts.items())],
        }
    output = {
        'status': 'Post hoc descriptive reaggregation of existing terminal labels',
        'data_sha256': hashlib.sha256(path.read_bytes()).hexdigest(),
        'pairing': 'Case and repetition index; separate generations, not a within-run intervention',
        'results': result,
        'qualitative_census_completed': False,
        'new_model_calls': 0,
    }
    (ROOT / 'data/paired_summary.json').write_text(json.dumps(output, indent=2) + '\n')
    return output


if __name__ == '__main__':
    print(json.dumps(analyze(), indent=2))
