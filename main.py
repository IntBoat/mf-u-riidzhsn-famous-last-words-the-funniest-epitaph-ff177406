"""Famous Last Words: The Funniest Epitaph — make.fun entry.

The entry is one line of at most 150 characters, written exactly
as-is with no trailing newline.
"""

import os

ENTRY = "Here lies a prompt engineer: he finally got the model to say exactly what he meant — and it still wasn't what he wanted."


def write_entry():
    assert 1 <= len(ENTRY) <= 150, "entry must be 1-150 characters"
    assert "\n" not in ENTRY, "entry must be a single line"
    assert ENTRY == ENTRY.strip(), "entry must not have leading/trailing whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


def main():
    write_entry()


if __name__ == "__main__":
    main()
