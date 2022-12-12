import argparse
import copy
from typing import Callable

parser = argparse.ArgumentParser()
parser.add_argument("file")
args = parser.parse_args()

HEAD_INDEX = 0
X_TUPLE_INDEX = 0
Y_TUPLE_INDEX = 1
DOWN = 'D'
UP = 'U'
LEFT = 'L'
RIGHT = 'R'



def step_up(knot: tuple[int,int]) -> tuple[int,int]:
    return (knot[X_TUPLE_INDEX], knot[Y_TUPLE_INDEX] + 1)

def step_down(knot: tuple[int,int]) -> tuple[int,int]:
    return (knot[X_TUPLE_INDEX], knot[Y_TUPLE_INDEX] - 1)


def step_left(knot: tuple[int,int]) -> tuple[int,int]:
    return (knot[X_TUPLE_INDEX] - 1, knot[Y_TUPLE_INDEX])


def step_right(knot: tuple[int,int]) -> tuple[int,int]:
    return (knot[X_TUPLE_INDEX] + 1, knot[Y_TUPLE_INDEX])

def is_same_row(knotA: tuple[int,int], knotB: tuple[int,int]) -> bool:
    return knotA[Y_TUPLE_INDEX] == knotB[Y_TUPLE_INDEX]

def is_same_column(knotA: tuple[int,int], knotB: tuple[int,int]) -> bool:
    return knotA[X_TUPLE_INDEX] == knotB[X_TUPLE_INDEX]

def is_pos(num: int) -> int:
    return num > 0

def print_step(rope: list[tuple[int,int]], step: int, start = (0,0)) -> None: 
    print((f"Step {step}."))
    for y in range(21, -1, -1):
        print("{:2}".format(y),end= " ")
        for x in range(0, 27):
            curr = (x,y)
            char = "."
            if curr == rope[HEAD_INDEX]:
                char = 'H'
            elif curr == rope[len(rope)-1]:
                char = 'T'
            elif curr in rope:
                char = rope.index(curr)
            elif curr == start:
                char = 's'

            print(char, end="")
        print()
    print("   ", end='')
    for x in range(0, 27):
        s = str(x)
        print(s[len(s)- 1 ], end='')
    print()
    print('   ', end='')
    for x in range(0, 27):
        if x < 10:
            print(' ', end='')
        else:
            s = str(x)
            print(s[0], end='')
    print()
    print()

STEP_FNS = { DOWN: step_down, UP: step_up, LEFT: step_left, RIGHT:step_right}

def distance(knotA: tuple[int,int], knotB: tuple[int,int]) -> tuple[int,int]:
    return (knotA[X_TUPLE_INDEX] - knotB[X_TUPLE_INDEX],knotA[Y_TUPLE_INDEX] - knotB[Y_TUPLE_INDEX])

def first_challenge(moves: list[tuple[str,int]]) -> int:
    rope = [(0,0), (0,0)]
    tail_visits = [(0,0)]

    print_step(rope, 0)
    for direction, amount in moves:
        print(f"MOVE {direction} {amount}")
        step_fn = STEP_FNS[direction]
        for step in range(1, amount + 1):
            rope[HEAD_INDEX] = step_fn(rope[HEAD_INDEX])
            
            x_dist, y_dist = distance(rope[HEAD_INDEX], rope[HEAD_INDEX + 1])

            tail_steps = []
            if abs(y_dist) == 2:
                if is_same_column(rope[HEAD_INDEX], rope[HEAD_INDEX + 1]) or is_same_row(rope[HEAD_INDEX], rope[HEAD_INDEX + 1]):
                    tail_steps.append(direction)
                else:
                    if is_pos(y_dist):
                        tail_steps.append(UP)
                    else:
                        tail_steps.append(DOWN)
                    
                    if is_pos(x_dist):
                        tail_steps.append(RIGHT)
                    else:
                        tail_steps.append(LEFT)

            elif abs(x_dist) == 2:
                if is_same_column(rope[HEAD_INDEX], rope[HEAD_INDEX + 1]) or is_same_row(rope[HEAD_INDEX], rope[HEAD_INDEX + 1]):
                    tail_steps.append(direction)
                else:
                    if is_pos(y_dist):
                        tail_steps.append(UP)
                    else:
                        tail_steps.append(DOWN)
                    
                    if is_pos(x_dist):
                        tail_steps.append(RIGHT)
                    else:
                        tail_steps.append(LEFT) 


            for tail_step in tail_steps:
                before = rope[HEAD_INDEX + 1]
                after = STEP_FNS[tail_step](before)
                rope[HEAD_INDEX + 1] = after



            tail_visits.append(rope[HEAD_INDEX + 1])

           # print_step(rope, step)
              

    return len(set(tail_visits))


def second_challenge(moves: list[tuple[str, int]]) -> int:
    print("CHALLENGE 2", end ='\n\n')
    start = (12,5)
    rope = [(12,5),(12,5),(12,5),
            (12,5),(12,5),(12,5),
            (12,5),(12,5),(12,5),
            (12,5),]
    TAIL_INDEX = len(rope) - 1
    tail_visits = [(12,5)]

    print_step(rope, 0)
    for direction, amount in moves:
        print(f"MOVE {direction} {amount}")
        step_fn = STEP_FNS[direction]
        for step in range(1, amount + 1):
            rope[HEAD_INDEX] = step_fn(rope[HEAD_INDEX])

            for segment_index in range(1, len(rope)):
                prev = rope[segment_index - 1]
                curr = rope[segment_index ]


                x_dist, y_dist = distance(prev,curr)
                print(x_dist, y_dist)

                tail_steps:list[Callable[[tuple[int,int]], tuple[int,int]]] = []

                if abs(y_dist) == 2 or abs(x_dist) == 2:
                    if is_same_column(prev,curr):
                        if is_pos(y_dist):
                            tail_steps.append( UP)
                        else:
                            tail_steps.append( DOWN)
                    elif is_same_row(prev,curr):
                        if is_pos(x_dist):
                            tail_steps.append( RIGHT)
                        else:
                            tail_steps.append( LEFT)
                    else:
                        if is_pos(x_dist):
                            tail_steps.append(RIGHT)
                        elif not is_pos(x_dist):
                            tail_steps.append(LEFT)

                        if is_pos(y_dist):
                            tail_steps.append(UP)
                        elif not is_pos(y_dist):
                            tail_steps.append(DOWN)


                        #####
                        #     [H] [H] [H]
                        # [H] [ ] [ ] [ ] [H]
                        # [H] [ ] [T] [ ] [H]
                        # [H] [ ] [ ] [ ] [H]
                        #     [H] [H] [H]                     



                for tail_step in tail_steps:
                    after = STEP_FNS[tail_step](curr)
                    rope[segment_index] = after
                    print(f"moving segment {segment_index} {curr} is {x_dist} {y_dist} from {prev} {tail_step}  = {after}")
                    curr = rope[segment_index ]

            tail_visits.append(rope[TAIL_INDEX])

            print_step(rope, step, start)
              

    return len(set(tail_visits))


def parse_file(lines: list[str]) -> list[tuple[str,int]]:
    return [ (section[0], int(section[1])) for section in [ str.strip(line).split(' ') for line in lines ]]

with open(args.file, "r") as file:
    values = parse_file(file.readlines())
    first_answer =  first_challenge(copy.deepcopy(values))
    second_answer = second_challenge(copy.deepcopy(values))
    print(
        f"The number of trees visible from the outside is {first_answer}")
    print(
        f"The highest possible scenic score is {second_answer}")
