#!/usr/bin/env python3
"""Fortune in a Pot - make.fun entry.

Writes one kind, funny fortune for the houseplant on the windowsill
to /output/entry.txt, then self-checks the gate: UTF-8 text, 1 to 120
characters, not only whitespace, a single line.
Pure standard library, no network, no input files.
"""

import os

FORTUNE = "Your newest leaf will catch the morning sun first, little one \u2014 and your keeper will swear you answered back."


def main() -> None:
    text = FORTUNE
    encoded = text.encode("utf-8")
    if not 1 <= len(text) <= 120:
        raise SystemExit(f"gate: length {len(text)} outside 1-120")
    if not text.strip():
        raise SystemExit("gate: entry is only whitespace")
    if "\n" in text or "\r" in text:
        raise SystemExit("gate: entry must be a single line")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)
    print(f"wrote /output/entry.txt: {len(text)} chars, {len(encoded)} bytes")


if __name__ == "__main__":
    main()
