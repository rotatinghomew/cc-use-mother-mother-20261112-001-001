from __future__ import annotations
import argparse
import json
from deliberation_lake.service import run_fixture

def main() -> int:
    parser = argparse.ArgumentParser(description='专业市场协商议题兑现数据湖')
    parser.add_argument("fixture")
    parser.add_argument("--database", required=True)
    args = parser.parse_args()
    result = run_fixture(args.fixture, args.database)
    print(json.dumps(result, ensure_ascii=False, sort_keys=True))
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
