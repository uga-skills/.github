#!/usr/bin/env python3
"""Count exact tokens for one or more files via the Anthropic Messages API
`count_tokens` endpoint.

Usage:
    bin/calc-token.py <file> [<file2> ...]

Requires ANTHROPIC_API_KEY in the environment (see ../.env_template).
"""
import json
import os
import sys
import urllib.error
import urllib.request

API_URL = "https://api.anthropic.com/v1/messages/count_tokens"
ANTHROPIC_VERSION = "2023-06-01"
MODEL = os.environ.get("ANTHROPIC_MODEL", "claude-sonnet-5")


def count_tokens(api_key: str, text: str) -> int:
    body = json.dumps(
        {"model": MODEL, "messages": [{"role": "user", "content": text}]}
    ).encode("utf-8")
    req = urllib.request.Request(
        API_URL,
        data=body,
        method="POST",
        headers={
            "x-api-key": api_key,
            "anthropic-version": ANTHROPIC_VERSION,
            "content-type": "application/json",
        },
    )
    with urllib.request.urlopen(req) as resp:
        return json.load(resp)["input_tokens"]


def main() -> int:
    if len(sys.argv) < 2:
        print("usage: calc-token.py <file> [<file2> ...]", file=sys.stderr)
        return 1

    api_key = os.environ.get("ANTHROPIC_API_KEY")
    if not api_key:
        print(
            "error: ANTHROPIC_API_KEY is not set (see ../.env_template)",
            file=sys.stderr,
        )
        return 1

    for path in sys.argv[1:]:
        with open(path, encoding="utf-8") as f:
            text = f.read()
        try:
            tokens = count_tokens(api_key, text)
        except urllib.error.HTTPError as e:
            print(f"{path}: API error {e.code}: {e.read().decode()}", file=sys.stderr)
            return 1
        print(f"{path}: {tokens} ({MODEL})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
