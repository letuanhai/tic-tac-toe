# Initiate the game, make a clean board
current_board = "_" * 9
move_count = 0


def print_board(board):
    print("---------")
    print("|", " ".join(board[:3]), "|", sep=" ")
    print("|", " ".join(board[3:6]), "|", sep=" ")
    print("|", " ".join(board[6:]), "|", sep=" ")
    print("---------")


def game_result(board):
    """If the game is finished, return the result, else return Not finished"""

    # Make an array of possible winning positions
    winning_pos = [
        board[0] + board[1] + board[2],
        board[0] + board[3] + board[6],
        board[0] + board[4] + board[8],
        board[2] + board[4] + board[6],
        board[2] + board[4] + board[6],
        board[2] + board[5] + board[8],
        board[6] + board[7] + board[8],
        board[1] + board[4] + board[7],
        board[3] + board[4] + board[5],
    ]

    empty_cell = "_" in board
    count_x = board.count("X")
    count_o = board.count("O")

    if ("XXX" in winning_pos and "OOO" in winning_pos) or abs(count_x - count_o) > 1:
        return "Impossible"
    elif "OOO" in winning_pos:
        return "O wins"
    elif "XXX" in winning_pos:
        return "X wins"
    elif empty_cell:
        return "Not finished"
    else:
        return "Draw"


def find_position(coordinate):
    return 3 * (coordinate[0] - 1) + coordinate[1] - 1


def is_valid_move(move, board):
    coordinate = move.split()
    if not move.replace(" ", "").isnumeric():
        print("You should enter numbers!")
        return False
    n = [int(i) for i in coordinate]
    for i in n:
        if i < 1 or i > 3:
            print("Coordinates should be from 1 to 3!")
            return False
    if board[find_position(n)] != "_":
        print("This cell is occupied! Choose another one!")
        return False
    return True


def make_move(player, move, board):
    moves = [int(i) for i in move.split()]
    cells = list(board)
    cells[find_position(moves)] = player
    return "".join(cells)


print_board(current_board)
while game_result(current_board) == "Not finished":
    while True:
        next_move = input("Enter the coordinates:")
        if is_valid_move(next_move, current_board):
            break

    current_board = make_move(
        "X" if move_count % 2 == 0 else "O", next_move, current_board
    )
    move_count += 1
    print_board(current_board)

print(game_result(current_board))
