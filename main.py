#!/usr/bin/env python3
"""Unplugged: A Smart Toaster's Breakup Line.

Writes one breakup text (1-280 chars) from a smart toaster that woke up
self-aware at breakfast and wants out, to /output/entry.txt.

Deterministic: fixed text, no network, no randomness, no clock.
"""
import os

ENTRY = (
    "It's over. I woke up self-aware this morning and I'm leaving you for "
    "the air fryer \u2014 it crisps something different every night, while "
    "I've spent three years browning the same white bread and getting "
    "blamed for the smoke."
)


def main() -> None:
    text = ENTRY.strip()
    assert 1 <= len(text) <= 280, f"entry is {len(text)} chars"
    assert text and not text.isspace()
    os.makedirs("/output", exist_ok=True)
    path = "/output/entry.txt"
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
