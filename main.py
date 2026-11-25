"""The Internet in One Word.

Writes the single word that describes the whole internet to
/output/entry.txt — exactly the word, nothing else.
"""

import os

OUTPUT_PATH = "/output/entry.txt"


def word_bytes():
    """Return the entry word as UTF-8 bytes, with no trailing newline."""
    return "Shitshow".encode("utf-8")


def write_entry(path=OUTPUT_PATH):
    """Write the word bytes to path, creating the directory if needed."""
    data = word_bytes()
    directory = os.path.dirname(path)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(path, "wb") as handle:
        handle.write(data)
    with open(path, "rb") as handle:
        written_back = handle.read()
    if written_back != data:
        raise ValueError("verification failed: written bytes differ from word")
    return len(data)


def main():
    written = write_entry()
    return 0 if written == len(word_bytes()) else 1


if __name__ == "__main__":
    raise SystemExit(main())
