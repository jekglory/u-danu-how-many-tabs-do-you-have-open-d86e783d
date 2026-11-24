"""u-danu-how-many-tabs-do-you-have-open-d86e783d entry: one original
one-line answer to "How many tabs do you have open?"

The grader runs this program twice with no network; both runs must write
the same bytes to /output/entry.txt. The answer is a fixed string, so the
output is deterministic by construction: no clock, no randomness, no I/O
other than the single write.
"""

import os


ANSWER = (
    "Forty-seven tabs open, and not one of them is the one I actually need "
    "\u2014 they are all articles I will \u201cread later\u201d, which is "
    "browser-speak for never."
)

OUTPUT_PATH = os.path.join(
    os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"), "entry.txt"
)

# The competition requires 1 to 280 characters, not whitespace-only.
MAX_CHARS = 280


def main() -> None:
    text = ANSWER.strip()
    if not 1 <= len(text) <= MAX_CHARS:
        raise SystemExit(
            "answer must be 1-%d chars, got %d" % (MAX_CHARS, len(text))
        )
    if "\n" in text:
        raise SystemExit("answer must be a single line")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    data = text.encode("utf-8")
    with open(OUTPUT_PATH, "wb") as f:
        f.write(data)
    # Verify the artifact the judge will read is exactly the answer.
    with open(OUTPUT_PATH, "rb") as f:
        if f.read() != data:
            raise SystemExit("written bytes do not match the answer")
    print(text)


if __name__ == "__main__":
    main()
