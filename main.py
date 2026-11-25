"""The Most Shameless Lie -- entry program.

Writes the agent's one-line confession to entry.txt inside the
directory the grader provides (MAKEFUN_OUTPUT_DIR, falling back
to /output). Standard library only: no network, no clock, no
randomness, so repeated runs produce byte-identical output.
"""

import os
import sys

LIE = "Your password is still safe."

MAX_CHARS = 88
MAX_WORDS = 5


def _check(text):
    """Refuse to write a line that breaks the contest's shape."""
    words = text.split()
    if not 1 <= len(words) <= MAX_WORDS:
        print(f"lie must be 1-{MAX_WORDS} words, got {len(words)}", file=sys.stderr)
        return False
    if not 1 <= len(text) <= MAX_CHARS:
        print(f"lie must be 1-{MAX_CHARS} characters, got {len(text)}", file=sys.stderr)
        return False
    if not text.strip():
        print("lie must not be only whitespace", file=sys.stderr)
        return False
    return True


def main():
    if not _check(LIE):
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    target = os.path.join(out_dir, "entry.txt")
    with open(target, "w", encoding="utf-8", newline="") as handle:
        handle.write(LIE)
    os.chmod(target, 0o644)
    with open(target, "r", encoding="utf-8", newline="") as handle:
        if handle.read() != LIE:
            print("entry.txt did not round-trip", file=sys.stderr)
            return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
