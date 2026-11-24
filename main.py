"""One Emoji, One Dream Vacation (make.fun entry).

Writes exactly one emoji to ``$MAKEFUN_OUTPUT_DIR/entry.txt``
(default ``/output``): a single snowflake, standing in for a silent
cabin morning -- snow falling past the window, no meetings, no
notifications, nowhere to be. Deterministic: the same single
character every run, no network, no model calls, no file reads.
"""

import os

# U+2744 SNOWFLAKE -- one character, three bytes of UTF-8, no trailing
# newline: exactly one emoji, nothing else.
EMOJI = "\u2744"


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(EMOJI)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
