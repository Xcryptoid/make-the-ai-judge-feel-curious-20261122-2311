#!/usr/bin/env python3
"""Make the AI judge feel curious — entry program.

Writes one short text to /output/entry.txt: the oldest map in the
archive, and the one corner its cartographer left blank.
Deterministic: the same text on every run. No network, stdlib only.
"""

import os

TEXT = (
    "The oldest map in the archive leaves one corner blank. "
    "The cartographer drew every coast, river and road \u2014 then stopped, "
    "and wrote in the margin: 'I went no further. The ink ran out here, "
    "not the land.' The blank is still there. "
    "It has outwaited every reader before you."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
