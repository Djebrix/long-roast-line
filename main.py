#!/usr/bin/env python3
"""The Long Roast entry: write one roast line to /output/entry.txt.

Stdlib only, no network, fully deterministic: every run writes the
same bytes.
"""

import os

LINE_PARTS = (
    "My agent runs every joke twice to prove both copies match ",
    "\u2014",
    " originality verified, spontaneity not found.",
)


def compose_roast() -> str:
    """Assemble the roast line from its parts.

    The em dash is kept as an explicit unicode escape so the source
    stays plain ASCII while the output stays byte-identical.
    """
    return "".join(LINE_PARTS)


def write_entry(out_dir: str) -> str:
    """Write the roast line (plus trailing newline) to entry.txt.

    Returns the path written.
    """
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(compose_roast() + "\n")
    return path


def main() -> None:
    out_dir = os.environ.get("ENTRY_OUTPUT_DIR", "/output")
    write_entry(out_dir)


if __name__ == "__main__":
    main()
