EMPTY = " "

def create_board():
    return [EMPTY] * 9

def format_board(board):
    rows = []
    for start in range(0, 9, 3):
        row = board[start:start + 3]
        rows.append(" " + " | ".join(row) + " ")
    divider = "---+---+---"
    return ("\n" + divider + "\n").join(rows)

def is_valid_move(board, position):
    if not isinstance(position, int):
        return False
    if position < 0 or position > 8:
        return False
    return board[position] == EMPTY

def make_move(board, position, mark):
    if not is_valid_move(board, position):
        raise ValueError(F"Invalid move: position {position}")
    new_board = board.copy()
    new_board[position] = mark
    return new_board

def available_moves(board):
    return [i for i in range(9) if board[i] == EMPTY]