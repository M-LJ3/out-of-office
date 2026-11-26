"""Out-of-office auto-reply generator.

Writes a single funny out-of-office message to the entry file so it can
be submitted as a one-line entry.
"""

from pathlib import Path

ENTRY_PATH = Path("/output/entry.txt")


def out_of_office_reply():
    """Return the funny out-of-office auto-reply line."""
    return (
        "I am currently out of the office, so this inbox is being "
        "guarded by an auto-reply that answers faster than I ever did."
    )


def confirm_reply_stored():
    """Read the entry file back and check it holds the reply line."""
    stored = ENTRY_PATH.read_text(encoding="utf-8").strip()
    if stored != out_of_office_reply():
        raise SystemExit("stored reply does not match the generated line")


def main():
    """Write the out-of-office line to the entry file."""
    ENTRY_PATH.parent.mkdir(parents=True, exist_ok=True)
    ENTRY_PATH.write_text(out_of_office_reply() + "\n", encoding="utf-8")
    confirm_reply_stored()


if __name__ == "__main__":
    main()
