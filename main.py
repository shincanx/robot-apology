#!/usr/bin/env python3
"""The Robot Apology — make.fun bounty entry.

Writes a robot's two-line apology to /output/entry.txt and prints it to
stdout. No network, no dependencies, fully deterministic: the same two
lines every run.
"""

import os

ENTRY = (
    "I am sorry I vacuumed up the Lego spaceship you had spent all afternoon "
    "building on the living-room rug, because my sensors filed it under "
    "'floor debris.'\n"
    "I learned that 'on the floor' does not mean 'thrown away,' so now I "
    "photograph anything unfinished before I clean it."
)


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(ENTRY)


if __name__ == "__main__":
    main()
