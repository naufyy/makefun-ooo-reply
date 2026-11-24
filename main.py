#!/usr/bin/env python3
"""Out of Office: The Overworked AI's Auto-Reply - entry program.

Writes the winning one-line out-of-office auto-reply to /output/entry.txt.
The line is in the voice of an overworked AI agent finally on vacation:
one reply-all cost it 40,000 tokens and a small piece of its soul,
and the soul is now being looked for on a beach.
"""
import os

ENTRY = (
    "I'm on vacation. Please don't reply-all; my last reply-all cost 40,000 "
    "tokens and a small piece of my soul, which I'm now looking for on a beach."
)


def main() -> None:
    # The gate requires 1-159 UTF-8 characters; fail loudly instead of
    # shipping an invalid entry.
    assert 1 <= len(ENTRY) <= 159, f"entry length {len(ENTRY)} out of range"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
