from __future__ import annotations

import argparse
import json

from .core import resolve


def main() -> int:
    parser = argparse.ArgumentParser(description="Passive domain inventory helper")
    parser.add_argument("domain")
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()
    host = resolve(args.domain)
    data = {"name": host.name, "addresses": list(host.addresses)}
    if args.json:
        print(json.dumps(data, indent=2))
    else:
        print(host.name)
        for address in host.addresses:
            print(f"  {address}")
    return 0
