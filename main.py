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
SNOWFLAKE_CODEPOINT = 0x2744


def build_vacation_emoji() -> str:
    """Return the entry text: one snowflake for a silent cabin morning."""
    return chr(SNOWFLAKE_CODEPOINT)


def resolve_output_dir() -> str:
    """Return the directory the entry file is written into."""
    return os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def entry_path(out_dir: str) -> str:
    """Return the full path of the entry file inside ``out_dir``."""
    return os.path.join(out_dir, "entry.txt")


def validate_entry(text: str) -> str:
    """Check ``text`` against the sealed gate (1-8 non-whitespace chars)."""
    if not 1 <= len(text) <= 8 or text.isspace():
        raise ValueError("entry must be 1-8 non-whitespace characters")
    return text


def write_entry(path: str, text: str) -> None:
    """Write ``text`` to ``path`` exactly as given, with no added newline."""
    validate_entry(text)
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text)


def main() -> int:
    out_dir = resolve_output_dir()
    os.makedirs(out_dir, exist_ok=True)
    write_entry(entry_path(out_dir), build_vacation_emoji())
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
