#!/usr/bin/env python3
"""Write one word describing my Wi-Fi to /output/entry.txt.

The word is "Schrödinger": the network is simultaneously connected
and not connected, and you only find out which by opening a page --
a real physics reference that names the exact lived experience of a
Wi-Fi signal that exists in both states until observed. One word,
well under the 200-character gate.
"""
import os

WORD = "Schrödinger"
# One word: connected and not connected at the same time, until observed.


def main():
    assert 1 <= len(WORD) <= 200, "entry must be 1-200 characters"
    assert WORD.strip() == WORD and " " not in WORD, "entry must be one word"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(WORD + "\n")


if __name__ == "__main__":
    main()
