#!/usr/bin/env python3
"""Write the one word for the whole internet to entry.txt in the output folder."""

import os

# One word for the whole internet: picked from eight drafts judged
# pairwise on the kit's criteria (a single word for the whole
# internet first, then funny by itself, true about the internet as a
# whole rather than one app or mood, surprising rather than the first
# obvious word, and short enough to land in one beat). The word is
# the internet as a library where everyone is shouting at once: all
# the knowledge there is, none of it quiet. The gate checks entry.txt
# as UTF-8 text of 1 to 30 characters: this word is 11 code points,
# 12 with its trailing newline (verified by a local run).
TEXT = "Loudlibrary"


def write_entry(out_dir: str) -> None:
    """Write the word, with its trailing newline, into out_dir.

    The file holds the word and nothing else: no title, no
    punctuation, no explanation, because the brief is the word alone.
    """
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(TEXT + "\n")


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    write_entry(out_dir)


if __name__ == "__main__":
    main()
