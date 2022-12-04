import argparse

parser = argparse.ArgumentParser()
parser.add_argument("file")
args = parser.parse_args()


def strictly_overlapping(r1: range, r2: range) -> bool:
    return (r1.start <= r2.start and r2.stop <= r1.stop) or (r2.start <= r1.start and r1.stop <= r2.stop)


def overlapping(r1: range, r2: range) -> bool:
    return r1.start <= r2.stop and r2.start <= r1.stop


def first_challenge(assignments: list[tuple[range, range]]) -> int:
    overlaps = [
        1 for assignment1, assignment2 in assignments
        if strictly_overlapping(assignment1, assignment2)
    ]

    return len(overlaps)


def second_challenge(assignments: list[tuple[range, range]]) -> int:
    overlaps = [1
                for assignment1, assignment2 in assignments if overlapping(assignment1, assignment2)
                ]

    return len(overlaps)


def parse_file(lines: list[str]) -> list[tuple[range, range]]:

    def str_to_range(string: str) -> range:
        first, second = str.split(string, "-")
        return range(int(first), int(second))

    assignment_ranges = [str.strip(assignment).split(",")[:2]
                         for assignment in lines]
    assignment_strs = [(str_to_range(assignment_range[0]), str_to_range(
        assignment_range[1])) for assignment_range in assignment_ranges]

    return assignment_strs


with open(args.file, "r") as file:
    values = parse_file(file.readlines())
    first_answer = first_challenge(values)
    second_answer = second_challenge(values)
    print(
        f"The number of elves with fully overlapped assignments is {first_answer}")
    print(
        f"The number of elves with overlapped assignments is {second_answer}")
