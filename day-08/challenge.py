import argparse
import copy

parser = argparse.ArgumentParser()
parser.add_argument("file")
args = parser.parse_args()


def take_above(row: int, col: int, forrest: list[list[int]]) -> list[int]:
    if row == 0:
        return []
    return [forrest[row_up][col] for row_up in range(row - 1, -1, -1) ]


def take_below(row: int, col: int, forrest: list[list[int]]) -> list[int]:
    if row == (len(forrest) - 1):
        return []
    return [forrest[row_down][col] for row_down in range(row + 1, len(forrest)) ]


def take_left(row: int, col: int, forrest: list[list[int]]) -> list[int]:
    if col == 0:
        return []
    
    left = [ tree for tree in forrest[row][0: col]]
    left.reverse()
    return left

def take_right(row: int, col: int, forrest: list[list[int]])-> list[int]:
    if col == (len(forrest[row]) - 1):
        return []
    return [ tree for tree in forrest[row][col + 1:]]



def first_challenge(tree: list[list[int]]) -> int:
    

    def is_larger(value: int, items: list[int]) -> bool:
        bigger = [bigger_value for bigger_value in items if bigger_value >= value]
        return len(bigger) == 0

    large_trees = []
    for row in range(0, len(tree)):
        for col in range(0, len(tree[row])):
            tree_height = tree[row][col]
            
            if is_larger(tree_height, take_above(row,col, tree)):
                large_trees.append(tree_height)
            elif is_larger(tree_height, take_below(row,col, tree)):
                 large_trees.append(tree_height)
            elif is_larger(tree_height, take_left(row,col, tree)):
                large_trees.append(tree_height)
            elif is_larger(tree_height, take_right(row,col, tree)):
                large_trees.append(tree_height)
   

    return len(large_trees)

def second_challenge(forrest: list[list[int]]) -> int:
    scenic_score = 0

    def score_view(height: int, trees: list[int]):
        score = 0
        for tree in trees:
            score = score + 1
            if tree >= height:
                break
        return score

    for row in range(1, len(forrest) - 1):
        for col in range(1, len(forrest[row])-1):
            tree_height = forrest[row][col]

            up_score = score_view(tree_height, take_above(row, col, forrest))
            down_score = score_view(tree_height, take_below(row, col, forrest))
            left_score = score_view(tree_height, take_left(row, col, forrest))
            right_score = score_view(tree_height, take_right(row, col, forrest))

            tree_scenic_score = up_score * down_score * left_score * right_score
            if tree_scenic_score > scenic_score:
                scenic_score = tree_scenic_score

    return scenic_score


def parse_file(lines: list[str]) -> list[list[int]]:

    forrest:list[list[int]] = []
    for line in lines:
        forrest.append([int(tree) for tree in line if tree != '\n'])

    return forrest



with open(args.file, "r") as file:
    values = parse_file(file.readlines())
    first_answer =  first_challenge(copy.deepcopy(values))
    second_answer = second_challenge(copy.deepcopy(values))
    print(
        f"The number of trees visible from the outside is {first_answer}")
    print(
        f"The highest possible scenic score is {second_answer}")
