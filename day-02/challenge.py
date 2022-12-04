import argparse
from collections import Counter

parser = argparse.ArgumentParser()
parser.add_argument("file")
args = parser.parse_args()

ROCK = 1
PAPER = 2
SCISSORS = 3

LOSS = 0
DRAW = 3
WIN = 6

THEIR_ROCK = 'A'
THEIR_PAPER = 'B'
THEIR_SCISSORS = 'C'


def first_challenge(round_occurrence: dict[str, int]) -> int:
    MY_ROCK = 'X'
    MY_PAPER = 'Y'
    MY_SCISSORS = 'Z'

    score_map = {
        f"{THEIR_ROCK} {MY_ROCK}": ROCK + DRAW,
        f"{THEIR_ROCK} {MY_PAPER}": PAPER + WIN,
        f"{THEIR_ROCK} {MY_SCISSORS}": SCISSORS + LOSS,

        f"{THEIR_PAPER} {MY_ROCK}": ROCK + LOSS,
        f"{THEIR_PAPER} {MY_PAPER}": PAPER + DRAW,
        f"{THEIR_PAPER} {MY_SCISSORS}": SCISSORS + WIN,

        f"{THEIR_SCISSORS} {MY_ROCK}": ROCK + WIN,
        f"{THEIR_SCISSORS} {MY_PAPER}": PAPER + LOSS,
        f"{THEIR_SCISSORS} {MY_SCISSORS}": SCISSORS + DRAW
    }

    scores = [score_map[k] * round_occurrence[k]
              for k in round_occurrence.keys()]
    return sum(scores)


def second_challenge(round_occurrence: dict[str, int]) -> int:
    NEED_LOSS = 'X'
    NEED_DRAW = 'Y'
    NEED_WIN = 'Z'

    score_map = {
        f"{THEIR_ROCK} {NEED_LOSS}": SCISSORS + LOSS,
        f"{THEIR_ROCK} {NEED_DRAW}": ROCK + DRAW,
        f"{THEIR_ROCK} {NEED_WIN}": PAPER + WIN,

        f"{THEIR_PAPER} {NEED_LOSS}": ROCK + LOSS,
        f"{THEIR_PAPER} {NEED_DRAW}": PAPER + DRAW,
        f"{THEIR_PAPER} {NEED_WIN}": SCISSORS + WIN,

        f"{THEIR_SCISSORS} {NEED_LOSS}": PAPER + LOSS,
        f"{THEIR_SCISSORS} {NEED_DRAW}": SCISSORS + DRAW,
        f"{THEIR_SCISSORS} {NEED_WIN}": ROCK + WIN
    }

    scores = [score_map[k] * round_occurrence[k]
              for k in round_occurrence.keys()]
    return sum(scores)


def parse_file(lines: list[str]) -> dict[str, int]:
    return dict(Counter([str.strip(l) for l in lines]))


with open(args.file, "r") as file:
    values = parse_file(file.readlines())
    first_answer = first_challenge(values)
    second_answer = second_challenge(values)
    print(f"My score is {first_answer}")
    print(f"The strategy score is {second_answer}")
