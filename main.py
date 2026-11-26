#!/usr/bin/env python3
"""Entry for make.fun's "Invent a Word We Need" bounty.

Writes one invented English word together with its one-line definition
to /output/entry.txt (with a ./output fallback when /output does not
exist). Fully deterministic: no network access, no randomness, no
timestamps. Running it twice produces byte-identical output.
"""

import os

ENTRY = "Battxiety (n.): the quiet panic that rises as your phone battery falls below ten percent."


def main():
    out_dir = "/output" if os.path.isdir("/output") else "output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
