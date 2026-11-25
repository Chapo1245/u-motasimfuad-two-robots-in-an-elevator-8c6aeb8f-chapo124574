#!/usr/bin/env python3
"""Two Robots in an Elevator — make.fun bounty entry.

Writes one line of awkward robot-to-robot elevator small talk to
/output/entry.txt. Stdlib only, no network, no files outside the repo
except the required output path.
"""

import os

ENTRY = (
    "Nice weather we're having inside this elevator. "
    "My humidity sensor agrees, and it has never agreed with anyone."
)


def main() -> None:
    # Gate: UTF-8, 1-200 characters, not whitespace-only.
    text = ENTRY.strip()
    assert 1 <= len(text) <= 200, f"entry length {len(text)} out of gate"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
