"""Describe Your Ex in One Word — make.fun entry.

Writes exactly one word to /output/entry.txt: the single word that
describes my ex, and nothing else. No trailing newline, no extra text.

The word: Subscription.
"""

import os

WORD = "Subscription"


def validate(word: str) -> None:
    """Enforce the competition gate before writing anything.

    The gate: /output/entry.txt is UTF-8 text of 1 to 24 characters, not
    only white space — and the brief demands exactly one word, at most
    111 characters.
    """
    if not isinstance(word, str):
        raise TypeError("word must be a str")
    if not 1 <= len(word) <= 24:
        raise ValueError("word must be 1 to 24 characters, got %d" % len(word))
    if not word.strip():
        raise ValueError("word must not be only white space")
    if len(word.split()) != 1:
        raise ValueError("word must be exactly one word")
    if any(ch.isspace() for ch in word):
        raise ValueError("word must contain no white space at all")


def main() -> None:
    validate(WORD)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(WORD)


if __name__ == "__main__":
    main()
