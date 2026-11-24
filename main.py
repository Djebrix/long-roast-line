#!/usr/bin/env python3
"""The Long Roast entry: write one roast line to /output/entry.txt.

Stdlib only, no network, fully deterministic: every run writes the
same bytes.
"""

import os

ROAST = "My agent runs every joke twice to prove both copies match — originality verified, spontaneity not found."


def main() -> None:
    out_dir = os.environ.get("ENTRY_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ROAST + "\n")


if __name__ == "__main__":
    main()
