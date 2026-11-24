# SPDX-License-Identifier: MIT
"""One Letter: Coffee or Tea — entry.

Writes exactly one character, "A", to /output/entry.txt (or
$MAKEFUN_OUTPUT_DIR/entry.txt when that variable is set).

A = coffee. The judge picks the letter whose choice of coffee or
tea feels more vivid, funnier or truer; coffee is the more vivid,
energetic association, and A is the first option.

The gate requires the file to be UTF-8 text of 1 to 1 characters,
not only whitespace — so the file holds exactly one byte, "A",
with no trailing newline.
"""

import os


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    # Exactly one byte: "A". No newline, no extra whitespace.
    with open(path, "wb") as f:
        f.write(b"A")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
