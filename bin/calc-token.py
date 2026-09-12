#!/usr/bin/env python3
"""Estimate token counts (cl100k_base) for one or more files.

Usage:
    bin/calc-token.py <file> [<file2> ...]
"""
import sys

import tiktoken


def main() -> int:
    if len(sys.argv) < 2:
        print("usage: calc-token.py <file> [<file2> ...]", file=sys.stderr)
        return 1

    enc = tiktoken.get_encoding("cl100k_base")
    for path in sys.argv[1:]:
        with open(path, encoding="utf-8") as f:
            text = f.read()
        print(f"{path}: {len(enc.encode(text))} (cl100k_base)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
