"""Validate user-selected research preferences without printing their values."""
import argparse
import json
from pathlib import Path


def validate(data):
    if not isinstance(data, dict) or type(data.get('schema_version')) is not int or data['schema_version'] != 1:
        raise ValueError('invalid_schema')
    platforms = data.get('preferred_platforms')
    if not isinstance(platforms, list) or not platforms or any(not isinstance(p, str) or not p.strip() for p in platforms):
        raise ValueError('invalid_platforms')
    if data.get('research_mode') not in ('adaptive', 'broad'):
        raise ValueError('invalid_research_mode')
    budget = data.get('time_budget_minutes')
    if budget is not None and (isinstance(budget, bool) or not isinstance(budget, (int, float)) or budget <= 0 or budget == float('inf') or budget != budget):
        raise ValueError('invalid_time_budget')
    path = data.get('output_directory')
    if path is not None and (not isinstance(path, str) or not path.strip()):
        raise ValueError('invalid_output_directory')
    if not isinstance(data.get('language'), str) or not data['language'].strip():
        raise ValueError('invalid_language')
    return True


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--config', type=Path, required=True)
    args = parser.parse_args()
    try:
        validate(json.loads(args.config.read_text(encoding='utf-8-sig')))
    except (OSError, ValueError):
        print('Research configuration missing or invalid; values were not printed.')
        return 1
    print('Research preferences valid; no search performed.')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
