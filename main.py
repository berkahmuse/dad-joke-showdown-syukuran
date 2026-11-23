#!/usr/bin/env python3
"""Dad Joke Showdown entry (@syukuran).

Writes one dad joke (at most 200 characters) to /output/entry.txt.

The joke: a father talks to the bread, and the bread answers back.
Setup pun "feeling crumby" (crummy + bread crumbs) primes the theme;
the punchline turns "the least I can do" into "the yeast I can do",
so the turn lands on the first read and the last word is the pun.
A different angle from the sibling entries (no family member asks a
question here — the father addresses the bread itself), and a fresher
pun than the over-told thyme/time and culture-shock turns.
"""

import os
import sys

JOKE = (
    "I told the bread I was feeling crumby. "
    "It said, 'Don't worry, Dad \u2014 it's the yeast I can do.'"
)


def main() -> int:
    if not (1 <= len(JOKE) <= 200):
        print(f"entry is {len(JOKE)} chars, must be 1-200", file=sys.stderr)
        return 1
    if JOKE != JOKE.strip() or "\n" in JOKE or "\r" in JOKE:
        print("entry must be a single line with no surrounding whitespace",
              file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(JOKE)
    # Read-back guard: the file the grader reads must be exactly the joke,
    # no trailing newline, no partial write.
    with open(path, encoding="utf-8") as f:
        if f.read() != JOKE:
            print("entry.txt does not match the joke after write",
                  file=sys.stderr)
            return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
