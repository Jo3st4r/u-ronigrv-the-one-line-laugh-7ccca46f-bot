#!/usr/bin/env python3
"""The One-Line Laugh — u-ronigrv-the-one-line-laugh-7ccca46f.

Writes one funny line to /output/entry.txt. Stdlib only; no
network, no randomness, no I/O besides the one output file.

The joke is built from three named beats so its shape is
visible in the code:

* SETUP — the premise: the lift breaks down with a stranger
  for twenty minutes, an everyday awkwardness everyone knows.
* BOND — the turn: twenty forced minutes turn strangers into
  something like friends.
* PAYOFF — the surprise that still makes sense: they now send
  each other Christmas cards, and neither one knows the
  other's name. The friendship is real; the introduction
  never happened.

The lift broke down with a stranger for twenty minutes, so now
we send each other Christmas cards and still don't know each
other's names.
"""

import os

# The three beats of the one-liner, joined in entry_text().
SETUP = "The lift broke down with a stranger for twenty minutes"
BOND = "so now we send each other Christmas cards"
PAYOFF = "and still don't know each other's names."

# The competition caps the entry at 200 characters; the line is 138.
MAX_CHARS = 200

ENTRY = "The lift broke down with a stranger for twenty minutes, so now we send each other Christmas cards and still don't know each other's names."


def entry_text() -> str:
    """Join the three beats into the one-line laugh."""
    return f"{SETUP}, {BOND} {PAYOFF}"


def validate(text: str) -> None:
    """Check the gate rules the sealed scorer enforces: 1-200 chars,
    UTF-8, not blank, and exactly one sentence. The apostrophes in
    "don't" and "other's" are part of the line, not punctuation
    tricks — the single full stop at the end is the only period."""
    text.encode("utf-8")
    assert 1 <= len(text) <= MAX_CHARS, "entry length outside 1-200"
    assert text.strip(), "entry must not be only whitespace"
    assert text.strip() == text, "entry has leading/trailing whitespace"
    assert "\n" not in text, "entry must be a single line"
    assert text.count(".") == 1, "entry must be a single sentence"
    assert text.endswith("."), "entry must end with a full stop"


def main() -> None:
    text = entry_text()
    # Guard the two things the judge weighs: the line itself, and
    # that it fits the 200-character limit with room to spare.
    assert text == ENTRY, "joined line drifted from the entry line"
    # Each beat must survive the join: a missing beat means the
    # joke lost its setup, its turn, or its payoff.
    for beat in (SETUP, BOND, PAYOFF):
        assert beat in text, f"missing beat: {beat}"
    validate(text)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
