import argparse
import copy

from typing import TypeVar
from collections.abc import Callable

parser = argparse.ArgumentParser()
parser.add_argument("file")
args = parser.parse_args()

TNode = TypeVar("TNode", bound = "Node")

class Node:
    def __init__(self: TNode, parent: TNode, name: str, size: int) -> None:
        self.parent = parent
        self.name = name
        self.size = size
        self.children: list[TNode] = []

    def is_directory(self): 
        return self.size == 0

    def get_child_dir_with_name(self:TNode, name: str):
        node = [ child for child in self.children if child.size == 0 and child.name == name ]
        return node[0]
    
    def add_child(self: TNode, name: str, size: int):
        child_node = Node(self, name, size)
        self.children.append(child_node)

    def print_tree(self: TNode, depth = 0):
        print("-" * depth, end="")
        print(f"- {self.name}", end=" ")
        
        if self.size == 0:
            print( "(dir)")
        else:
            print( f"(file, size={self.size})")

        for child in self.children:
            child.print_tree(depth + 1)

    def calculate_sub_tree_size(self: TNode) -> int:
        return self.size + sum([
            child.calculate_sub_tree_size() for child in self.children
        ])


    def get_child_dir_nodes(self: TNode) -> list [TNode]:
        return [child for child in self.children if child.is_directory()]


def find_right_sized_directories(node: TNode, func: Callable[[TNode], bool]) -> list[TNode]:
    nodes: list[TNode] = []
    if func(node):
        nodes.append(node)

    for child in node.children:
        if child.is_directory():
            matching_children = find_right_sized_directories(child, func)
            for matching_child in matching_children:
                nodes.append(matching_child)

    return nodes


def first_challenge(game: TNode) -> int:
    MAX_SUBTREE_SIZE = 100000
    max_sized: Callable[[TNode], bool] = lambda child: child.calculate_sub_tree_size() <= MAX_SUBTREE_SIZE
    max_dirs = find_right_sized_directories(game, max_sized)

    return sum([node.calculate_sub_tree_size() for node in max_dirs])

def second_challenge(game: TNode) -> int:
    TOTAL_DISK_SPACE = 70_000_000
    FREE_SPACE_NEEDED = 30_000_000
    used_disk_space = game.calculate_sub_tree_size()
    unused_disk_space = TOTAL_DISK_SPACE - used_disk_space
    space_to_free = FREE_SPACE_NEEDED - unused_disk_space

    min_sized: Callable[[TNode], bool] = lambda child: child.calculate_sub_tree_size() >= space_to_free

    deletion_candidates = find_right_sized_directories(game, min_sized)
    deletion_sizes = [child.calculate_sub_tree_size() for child in deletion_candidates]

    return min(deletion_sizes)


def parse_file(lines: list[str]) -> TNode:
    stripped_lines = [str.strip(line) for line in lines]

    root: Node = Node(None, "/", 0)
    current = root
    
    for line in stripped_lines:
        if line.startswith("$ cd"):
            desired_dir = line.split(" ")[2]
            if desired_dir == "..":
                current = current.parent
            elif desired_dir == "/":
                current = root
            else:
                current = current.get_child_dir_with_name(desired_dir)
        elif line.startswith("$ ls"):
            # We dont really care about ls because we can just loop through all the others, cd will act as our main controller
            pass
        else:
            size, name = line.split(" ")
            if size == "dir":
                size = 0
            current.add_child(name, int(size))
    return root



with open(args.file, "r") as file:
    
    
    values = parse_file(file.readlines())
    values.print_tree()
    print()

    first_answer =  first_challenge(copy.deepcopy(values))
    second_answer = second_challenge(copy.deepcopy(values))
    print(
        f"The total size of smallish directories is {first_answer}")
    print(
        f"The size of the directory to delete is {second_answer}")
# The total size of large directories is 1453349
# The number of elves with overlapped assignments is 2948823