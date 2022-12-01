import argparse

parser = argparse.ArgumentParser()
parser.add_argument("file")
args = parser.parse_args()


def first_challenge(cal_map: dict[str,int]) -> int: 
    values = list(cal_map.values())
    values.sort(reverse=True)
    return values[0]
    


def second_challenge(cal_map: dict[str,int]) -> int:
    values = list(cal_map.values())
    values.sort(reverse=True)
    return sum(values[:3])

def parse_file(lines: list[str]) -> dict[str,int]:
    elf_id = 1
    elf_calories = {}
    elf_calories[elf_id] = 0

    for line in lines:
        if not str.strip(line):
            elf_id = elf_id + 1
            elf_calories[elf_id] = 0
        else:
            elf_calories[elf_id] = elf_calories[elf_id] + int(line)
    
    return elf_calories

with open(args.file, "r") as file: 
    values = parse_file(file.readlines())
    first_answer = first_challenge(values)
    second_answer = second_challenge(values)
    print(f"The elf carrying the most calories is the holding {first_answer} calories")
    print(f"The top 3 elves carrying the most calories are holding {second_answer} calories")