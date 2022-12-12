import argparse
import copy
from typing import Callable, TypeVar
import math

parser = argparse.ArgumentParser()
parser.add_argument("file")
args = parser.parse_args()

TMonkey = TypeVar("TMonkey", bound = "Monkey")

def first_challenge(monkeys: list[TMonkey]) -> int:
    ROUNDS = 20

    relief: Callable[[int],int] = lambda n: n // 3

    for round in range(0, ROUNDS):
        print((f"ROUND {round + 1}"))
        for monkey in monkeys:
            monkey.inspect_items(monkeys, relief)
        
        for monkey in monkeys:
            monkey.print()
        print()


    for monkey in monkeys:
        print(f" Monkey {monkey.monkey_id} inspected items {monkey.items_inspected} times.")

    most_active = [monkey.items_inspected for monkey in monkeys]
    most_active.sort(reverse=True)
    
    return most_active[0] * most_active[1]

def second_challenge(monkeys: list[TMonkey]) -> int:

    print("\nChallenge 2.\n")
    ROUNDS =10_000
    
    mod_divisor = math.prod([ monkey.test_value for monkey in monkeys])
    relief: Callable[[int],int] = lambda n: n % mod_divisor
    for round in range(0, ROUNDS):
       # print((f"ROUND {round + 1}"))
        for monkey in monkeys:
            monkey.inspect_items(monkeys, relief)
        
        # for monkey in monkeys:
        #     monkey.print()
        # print()


    for monkey in monkeys:
        print(f" Monkey {monkey.monkey_id} inspected items {monkey.items_inspected} times.")

    most_active = [monkey.items_inspected for monkey in monkeys]
    most_active.sort(reverse=True)
    
    return most_active[0] * most_active[1]




class Monkey:
    def __init__(self, monkey_id: int, items: list[int], operation: str, test: tuple[int, int, int]) -> None:
        self.monkey_id = monkey_id
        self.items = items
        self.operation = operation
        self.test_value = test[0]
        self.true_target = test[1]
        self.false_target = test[2]
        self.items_inspected = 0

    def inspect_items(self, monkeyList: list[TMonkey], relief: Callable[[int],int]):
        self.items_inspected = self.items_inspected + len(self.items)
        for item in self.items:
            new_worry_level = self.inspect_item(item, relief)
            target = self.pick_monkey(new_worry_level)

            monkeyList[target].receive_item(new_worry_level)
        
        self.items = []

    
    def __eval_expression__(self: TMonkey, old: int) -> int:
        newVal = eval(self.operation, {'old':old})
        return newVal

    def inspect_item(self, item: int, relief: Callable[[int],int]) -> int:
        newWorry = self.__eval_expression__(item)
        return relief(newWorry)
      

    def pick_monkey(self, worry: int) -> int: 
        if worry % self.test_value == 0:
            return self.true_target
        else:
            return self.false_target

    def receive_item(self:TMonkey, item: int) -> None:
        self.items.append(item)

    def print(self:TMonkey)-> None:
        items_str =", ".join([str(i) for i in self.items])
        print(f"Monkey {self.monkey_id}: {items_str}")


def parse_file(lines: list[str]) -> list[TMonkey]:

    # remove empty lines and strip newline chars
    full_lines = [str.strip(line) for line in lines if len(str.strip(line)) != 0]
    monkey_details = [full_lines[i:i + 6] for i in range(0,len(full_lines),6)]


    

    monkeys: list[TMonkey] = []
    for monkey_detail in monkey_details:
        monkey_id = int(monkey_detail[0][-2][0])
        starting_items = monkey_detail[1][16:].split(", ")
        
        expression = monkey_detail[2][17:]

        test_value = int(monkey_detail[3][18:])
        truth_target = int(monkey_detail[4][-1])
        false_target = int(monkey_detail[5][-1])
        
       # print(f"{monkey_id} {starting_items} {expression_str} | {test_value} | {truth_target} {false_target}")


        monkeys.append(Monkey(monkey_id, [int(i) for i in starting_items], expression,(test_value, truth_target,false_target)))




    return monkeys



with open(args.file, "r") as file:
    values = parse_file(file.readlines())
    first_answer =  first_challenge(copy.deepcopy(values))
    second_answer = second_challenge(copy.deepcopy(values))
    print(
        f"The number of trees visible from the outside is {first_answer}")
    print(
        f"The highest possible scenic score is {second_answer}")
