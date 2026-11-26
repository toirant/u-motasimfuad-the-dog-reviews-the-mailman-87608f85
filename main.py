#!/usr/bin/env python3
"""The Dog Reviews the Mailman — make.fun entry.

Writes one funny one-line review, in the dog's own voice, to
/output/entry.txt. The gate requires 1-200 characters of UTF-8 text,
a single line, not only whitespace.
"""

import os

ENTRY = (
    "One star. He marches up to MY door every day, shoves letters "
    "through MY slot, then won't let me sniff his bag. Rude. "
    "I barked. He comes back anyway — so do I."
)


def main() -> None:
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    # Keep the entry to exactly one line: collapse any stray
    # whitespace so the gate sees a single tight review.
    line = " ".join(ENTRY.split())
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(line + "\n")


if __name__ == "__main__":
    main()
