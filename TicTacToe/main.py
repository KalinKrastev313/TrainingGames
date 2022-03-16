def create_board(rows=3):
    board = []
    for row_num in range(rows):
        board.append([" "]*3)
    return board


def print_boarder_of_board(board, col=3):
    print(col*"+===", end="")
    print("+")


def value_part_of_a_row(row, col=3):
    for value in row:
        print(f"| {value} ", end="")
    print("|",)


def print_board(board):
    for row in board:
        print_boarder_of_board(board)
        value_part_of_a_row(row)
    print_boarder_of_board(board)


def place_a_stone(board):
    print("Choose a row")
    row = int(input()) - 1
    if not row in range(0, len(board)):
        print("Not a valid row")
        place_a_stone(board)
    print("Choose a column")
    col = int(input()) - 1
    print("Choose a char")
    char = input()
    board[row][col] = char


def horizontal_win(board):
    for row in board:
        if len(set(row)) == 1 and not row[0] == " ":
            return True
    else:
        return False


def vertical_win(board):
    for index in range(len(board[0])):
        if board[0][index] == board[1][index] and board[2][index] == board[0][index] and not board[0][index] == " ":
            return True
    return False


def diagonal_win(board):
    if board[0][0] == board[1][1] and board[0][0] == board[2][2] and not board[1][1] == " ":
        return True
    elif board[0][2] == board[1][1] and board [0][2] == board[2][0] and not board[1][1] == " ":
        return True
    else:
        return False


def no_win(board):
    if horizontal_win(board) or vertical_win(board) or diagonal_win(board):
        return False
    else:
        return True


board = create_board()
print_board(board)

while no_win(board):
    place_a_stone(board)
    print_board(board)



