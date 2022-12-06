import argparse
import re
import copy

parser = argparse.ArgumentParser()
parser.add_argument("file")
args = parser.parse_args()

def parse_move(moveString: str) -> tuple[int, int, int]:
    _, count, _, start, _, end = moveString.split(' ')
    return (int(count), int(start), int(end))


def print_board(board: dict[int,list[str]]) -> None:
    for key in board.keys():
        str_val = ",".join(board[key])
        print(f"{key}: {str_val }")
    print()

def count_board(board: dict[int, list[str]]) -> int:
    return sum([len(v) for v in board.values()])

def first_challenge(game: tuple[dict[int,list[str]],list[str]]) -> str:
    game_board, moves = game
    print(f"{count_board(game_board)} elements")
    print_board(game_board)
    for move in moves:
        count, start, end = parse_move(move)
        for i in range(0, count):
            game_board[end].append(game_board[start].pop())
        print(move)
        print(f"{count_board(game_board)} elements")
        print_board(game_board)
    
    tops = [ val.pop() for val in game_board.values() if len(val) >= 1 ]
    return "".join(tops)



def second_challenge(game: tuple[dict[int,list[str]],list[str]]) -> str:
    game_board, moves = game
    print(" GAME 2 \n\n")
    print(f"{count_board(game_board)} elements")
    print_board(game_board)
    for move in moves:
        count, start, end = parse_move(move)

        to_add = game_board[start][-count:]
        print(f"to add= {to_add}")
        game_board[start] = game_board[start][:-count]
        game_board[end] = game_board[end] + to_add




       
        print(move)
        print(f"{count_board(game_board)} elements")
        print_board(game_board)
    
    tops = [ val.pop() for val in game_board.values() if len(val) >= 1 ]
    return "".join(tops)


def parse_file(lines: list[str]) -> tuple[dict[int,list[str]],list[str]]:

    CRATE_SPACE = 4
    game_board_lines = [ line.replace('\n','') for line in lines if not line.startswith("move") and len(str.strip(line)) > 0] 
    game_board_lines.reverse()
    game_board_lines = game_board_lines[1:]
    

    game_board = {}
    for layer in game_board_lines:
        crates = [layer[n: n+CRATE_SPACE] for n in range(0, len(layer), CRATE_SPACE)]

        for index, crate in enumerate(crates):
            if (index + 1) not in game_board.keys():
                game_board[index + 1] = []
            
            cleansed_crate = re.sub(r'\W+', '', crate)
            if cleansed_crate:
                game_board[index + 1].append(cleansed_crate)



    return (game_board, [ str.strip(line) for line in lines if line.startswith('move')])




with open(args.file, "r") as file:
    
    
    values = parse_file(file.readlines())



    first_answer =  first_challenge(copy.deepcopy(values))
    second_answer = second_challenge(copy.deepcopy(values))
    print(
        f"The number of elves with fully overlapped assignments is {first_answer}")
    print(
        f"The number of elves with overlapped assignments is {second_answer}")
