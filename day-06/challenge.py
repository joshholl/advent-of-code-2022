import argparse
import copy
from collections import Counter

parser = argparse.ArgumentParser()
parser.add_argument("file")
args = parser.parse_args()


def find_unique_sequence(string: str, unique_amount: int) -> int:
    for i in range(0, len(string) - unique_amount):
        potential_marker = string[i: i+unique_amount]
        unique_chars = set(potential_marker)
        print(potential_marker)
        print(unique_chars)
        if len(unique_chars) == unique_amount:
            return i + unique_amount



def first_challenge(game: str) -> int:
   return find_unique_sequence(game, 4)


def second_challenge(game: str) -> int:
    return find_unique_sequence(game, 14)

def parse_file(lines: list[str]) -> str:
    return [str.strip(line) for line in lines][0]


with open(args.file, "r") as file:
    
    
    values = parse_file(file.readlines())



    first_answer =  first_challenge(copy.deepcopy(values))
    second_answer = second_challenge(copy.deepcopy(values))
    print(
        f"The number of elves with fully overlapped assignments is {first_answer}")
    print(
        f"The number of elves with overlapped assignments is {second_answer}")
