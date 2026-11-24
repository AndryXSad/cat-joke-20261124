"""The One-Line Cat Joke That Lands — entry program (program/v1).

Writes one line — a one-line joke about a cat — to /output/entry.txt
(or $MAKEFUN_OUTPUT_DIR/entry.txt when that variable is set). The line was
chosen by a local pairwise tournament over 8 original candidates, judged on
the published criteria: on-subject with a setup and a turn, biggest laugh on
first read, a fresh angle (no tired puns), tight single line, and retellable.

The winning line: a cat that screams at a closed door every morning. The
setup is the familiar ritual (scream, open, walk away); the punch lands on
the last three words, reframing the whole ritual — the cat is not asking to
go through, he is managing his human.
"""

import os
import sys

LINE = (
    "Every morning my cat screams at a closed door, I open it, he walks "
    "away \u2014 he's not asking to go through, he's managing me."
)


def validate_line(line: str) -> bool:
    """Gate the sealed scorer applies: 1-200 chars, UTF-8, not whitespace-only."""
    return bool(line.strip()) and 1 <= len(line) <= 200


def resolve_output_dir() -> str:
    """Output dir from the grader env var, falling back to /output."""
    return os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"


def main() -> int:
    # Self-check the same gate the sealed scorer applies before writing.
    if not validate_line(LINE):
        print("entry line fails the 1-200 character gate", file=sys.stderr)
        return 1
    out_dir = resolve_output_dir()
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)
    return 0


if __name__ == "__main__":
    sys.exit(main())
