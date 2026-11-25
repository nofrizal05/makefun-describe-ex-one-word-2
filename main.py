"""Describe Your Ex in One Word — make.fun entry.

Writes exactly one word to /output/entry.txt: the single word that
describes my ex, and nothing else. No trailing newline, no extra text.

The word: Subscription.

Why this word: an ex is like a subscription you forgot to cancel —
the charges keep coming long after you stopped enjoying the service,
the renewal is automatic, and cancelling takes five confirmation
screens, a chat with support, and a promise you will think about it.
It fits the brief in one word: it is the whole relationship, the
monthly reminder that something ended but never quite stopped.
One word, twelve characters, no explanation needed beyond the bill.
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
    # The entry file is plain UTF-8 text read by a byte-exact grader; a
    # single word with no shared alphabet would break the one-word read,
    # so keep the word to plain ASCII letters only.
    if not word.isascii():
        raise ValueError("word must be ASCII only")


def main() -> None:
    validate(WORD)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(WORD)


if __name__ == "__main__":
    main()
