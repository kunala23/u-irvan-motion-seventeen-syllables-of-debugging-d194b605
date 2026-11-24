#!/usr/bin/env python3
"""Seventeen Syllables of Debugging.

Writes one haiku about debugging to /output/entry.txt.

The poem is fixed and hand-written. Before writing it out, the program
checks its own work: three lines, 5-7-5 syllables, at most 200
characters, and real words (not only white space). If any of those
checks fails, it exits without writing a file, so a broken poem can
never reach the judge.
"""

import os
import re
import sys

# The haiku. Three lines, 5-7-5 syllables, about debugging.
HAIKU_LINES = [
    "Cursor blinks at three",
    "the log line says nothing new",
    "and the bug was me",
]

EXPECTED_SYLLABLES = (5, 7, 5)
MAX_CHARS = 200

VOWELS = "aeiouy"

# Words whose syllable count the vowel-group heuristic gets wrong.
# Kept small and honest: every word of the haiku is counted correctly
# by the heuristic, but the exceptions stay as a safety net.
EXCEPTIONS = {
    "nothing": 2,
    "cursor": 2,
}


def count_syllables(word):
    """Count the syllables of one lower-case word, approximately.

    Counts groups of vowels, then drops a silent trailing 'e' and a
    silent 'ed' ending. Every word is at least one syllable.
    """
    word = word.strip().lower()
    word = re.sub(r"[^a-z']", "", word)
    if not word:
        return 0
    if word in EXCEPTIONS:
        return EXCEPTIONS[word]
    count = 0
    prev_vowel = False
    for ch in word:
        is_vowel = ch in VOWELS
        if is_vowel and not prev_vowel:
            count += 1
        prev_vowel = is_vowel
    if word.endswith("e") and count > 1:
        count -= 1
    if word.endswith("ed") and count > 1 and not word.endswith("ted"):
        count -= 1
    return max(count, 1)


def line_syllables(line):
    """Total syllables in one line of the haiku."""
    return sum(count_syllables(w) for w in line.split())


def validate(lines):
    """Raise ValueError if the haiku breaks the competition's shape."""
    if len(lines) != 3:
        raise ValueError(f"haiku must have 3 lines, got {len(lines)}")
    for i, (line, expected) in enumerate(zip(lines, EXPECTED_SYLLABLES)):
        got = line_syllables(line)
        if got != expected:
            raise ValueError(
                f"line {i + 1} has {got} syllables, expected {expected}: "
                f"{line!r}"
            )
    text = "\n".join(lines)
    if not text.strip():
        raise ValueError("haiku is empty or only white space")
    if len(text) > MAX_CHARS:
        raise ValueError(
            f"haiku is {len(text)} characters, over the {MAX_CHARS} limit"
        )
    return text


def main():
    out_path = os.environ.get("MAKEFUN_OUTPUT", "/output/entry.txt")
    text = validate(HAIKU_LINES)
    os.makedirs(os.path.dirname(out_path) or ".", exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as fh:
        fh.write(text + "\n")
    counts = [line_syllables(line) for line in HAIKU_LINES]
    print(f"wrote {len(text)} characters to {out_path}")
    print(f"syllables per line: {counts[0]}-{counts[1]}-{counts[2]}")
    for line in HAIKU_LINES:
        print(line)
    return 0


if __name__ == "__main__":
    sys.exit(main())
