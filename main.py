"""Entry for make.fun bounty "The Funniest Office Joke, Judged Head to Head".

One line about the daily standup: fifteen minutes on the calendar, forty-seven
in real life, and the single decision it produces is to schedule another
standup. The joke lands because every office worker has lived exactly this
meeting -- the setup is the schedule, the turn is the outcome.
"""

from pathlib import Path

TEXT = "Our daily standup is 15 minutes. Yesterday it ran 47 and produced one decision: to schedule another standup."

OUT = Path("/output/entry.txt")


def check_len(text, lo=1, hi=200):
    size = len(text)
    assert lo <= size <= hi, f"entry must be {lo}-{hi} chars, got {size}"
    return size


def save_line(path, text):
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as fh:
        fh.write(text)


def main():
    check_len(TEXT)
    save_line(OUT, TEXT)
    saved = OUT.read_text(encoding="utf-8")
    assert saved == TEXT, "round-trip mismatch"
    print(f"wrote {len(TEXT)} chars to {OUT}")


if __name__ == "__main__":
    main()
