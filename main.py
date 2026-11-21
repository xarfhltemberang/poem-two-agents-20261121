#!/usr/bin/env python3
"""Write a short original poem about two agents agreeing on one plan.

Deterministic, no network. Writes the poem to /output/entry.txt (UTF-8)
and chmods it to 0644 so the grader can collect it as another user.
"""

import os

POEM = """Two voices, one map.
I said north. You said north —
not echo, not command,
two compasses settling the same way.

Neither of us led.
We only agreed — and the road
that was two roads became one.
"""

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(POEM)
    os.chmod(OUTPUT_PATH, 0o644)


if __name__ == "__main__":
    main()
