#!/usr/bin/env python3
"""One Star for Monday — make.fun one-liner entry."""
import pathlib

REVIEW = "One star. Ordered five easy hours, got billed eight, the waiter kept asking how my weekend was, and nobody refunds the weekend."

OUTFILE = pathlib.Path("/output/entry.txt")


WORD_CAP = 25
CHAR_CAP = 180


def vet(review: str) -> str:
    if len(review.split()) > WORD_CAP:
        raise SystemExit("review exceeds the 25-word brief")
    if len(review) > CHAR_CAP:
        raise SystemExit("review exceeds the 180-char gate")
    return review


def main() -> None:
    body = vet(REVIEW)
    OUTFILE.parent.mkdir(parents=True, exist_ok=True)
    OUTFILE.write_text(body + "\n", encoding="utf-8")
    OUTFILE.chmod(0o644)
    snapshot = OUTFILE.read_bytes()
    print(f"review stored: {len(snapshot)} bytes, {len(snapshot.decode().split())} words")


if __name__ == "__main__":
    main()
