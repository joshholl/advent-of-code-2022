import argparse
import copy

parser = argparse.ArgumentParser()
parser.add_argument("file")
args = parser.parse_args()

NOOP = 'noop'
ADD = 'addx'
CYCLES = { NOOP: 1, ADD: 2}

START = 20
STEP = 40
def first_challenge(commands: list[tuple[str,int]]) -> int:
    register = 1
    cycle_value = []

    for command,value in commands:
        cycles = CYCLES[command]
        for _ in range(0, cycles):
            cycle_value.append(register)
        if command == ADD:
            register = register + value





   
    print(cycle_value)
    print(register)

    interesting_cycles = []
    for cycle in range(START, len(cycle_value), STEP):
        interesting_cycles.append((cycle, cycle_value[cycle - 1]))
   
    print(interesting_cycles)
    return sum([ c[0] * c[1] for c in interesting_cycles])

def second_challenge(commands: list[tuple[str,int]]) -> int:
    register = 1
    cycle_value = []
    
    for command,value in commands:
        cycles = CYCLES[command]
        for _ in range(0, cycles):
            cycle_value.append(register)
        if command == ADD:
            register = register + value


    sprite = [0,1,2]

    def move_sprite(center: int): 
        return [center - 1, center, center + 1]


    screen_cycles = [cycle_value[i:i + STEP] for i in range(0, len(cycle_value), STEP)]
    
    for screen_cycle_set in screen_cycles:
        for col in range(0, len(screen_cycle_set)):
            sprite = move_sprite(screen_cycle_set[col])
            if col in sprite:
                print("#", end="")
            else:
                print(".",end='')
            #print(f" col {col} ", sprite)
        print("")






    return 0



def parse_file(lines: list[str]) -> list[tuple[str,int]]:
    command: list[tuple[str,int]] = []
    for line in lines:
        if line.startswith(NOOP):
            command.append((NOOP,0))
        elif line.startswith(ADD):
            command.append((ADD, int(line.split()[1])))





    return command



with open(args.file, "r") as file:
    values = parse_file(file.readlines())
    first_answer =  first_challenge(copy.deepcopy(values))
    second_answer = second_challenge(copy.deepcopy(values))
    print(
        f"The number of trees visible from the outside is {first_answer}")
    print(
        f"The highest possible scenic score is {second_answer}")
