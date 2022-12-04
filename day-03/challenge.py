import argparse

parser = argparse.ArgumentParser()
parser.add_argument("file")
args = parser.parse_args()


def priority(c: str) -> int:
    if (c.isupper()):
        return ord(c) - 38
    elif (c.islower()):
        return ord(c) - 96
    return 0


def first_challenge(lines: list[str]) -> int:
    rucksacks = [(line[:len(line)//2], line[len(line)//2:]) for line in lines]

    def score_rucksack(sack: tuple[str, str]) -> int:
        first_compartment, second_compartment = sack
        duplicate_items = [
            item for item in first_compartment if item in second_compartment][:1]
        priorities = [priority(item) for item in duplicate_items]
        return sum(priorities)

    return sum([score_rucksack(rucksack) for rucksack in rucksacks])


def second_challenge(lines: list[str]) -> int:
    ELF_GROUP_SIZE = 3
    groups = [lines[n: n+ELF_GROUP_SIZE]
              for n in range(0, len(lines), ELF_GROUP_SIZE)]

    def check_sacks(group: list[str]):
        first_elves_rucksack = group[0]
        second_elves_rucksack = group[1]
        third_elves_rucksack = group[2]

        shared_items = [
            item for item in first_elves_rucksack if item in second_elves_rucksack and item in third_elves_rucksack]
        return priority(shared_items[0])

    return sum(check_sacks(group) for group in groups)


def parse_file(lines: list[str]) -> list[str]:
    return [str.strip(l) for l in lines]


with open(args.file, "r") as file:
    values = parse_file(file.readlines())
    first_answer = first_challenge(values)
    second_answer = second_challenge(values)
    print(f"The score for the rucks sacks is {first_answer}")
    print(f"The score for the groups is {second_answer}")
