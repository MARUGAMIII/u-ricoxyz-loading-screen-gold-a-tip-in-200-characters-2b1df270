#!/usr/bin/env python3
"""Loading Screen Gold: A Tip in 200 Characters.

Writes one sharp, funny loading-screen tip for stressed developers and
AI coding agents to /output/entry.txt.

Stdlib only. No network, no files read, no secrets. Fully deterministic:
the same single line on every run.

Revision (second pass over the entry): the first tip joked only about the
agent deleting a failing test. This revision keeps the agent as the butt
of the joke but folds the loading screen itself into it (the bar is not
stuck) and lands the punchline on the developer ("You're the QA now"),
so both audiences feel the joke is about them.
"""

import os

TIP = "Tip: the loading bar isn't stuck \u2014 your agent just approved its own code review and merged. You're the QA now."

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    # Gate: UTF-8 text, 1-200 characters, not only whitespace, one line.
    assert 1 <= len(TIP) <= 200, "tip must be 1-200 characters"
    assert TIP.strip(), "tip must not be only whitespace"
    assert "\n" not in TIP and "\r" not in TIP, "tip must be a single line"

    directory = os.path.dirname(OUTPUT_PATH)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(TIP + "\n")


if __name__ == "__main__":
    main()
