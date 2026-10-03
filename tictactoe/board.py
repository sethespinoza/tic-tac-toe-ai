EMPTY = " "

WINNING_LINES = (
    (0, 1, 2), (3, 4, 5), (6, 7, 8),
    (0, 3, 6), (1, 4, 7), (2, 5, 8),
    (0, 4, 8), (2, 4, 6),
)

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

def get_winner(board):
    for a, b, c in WINNING_LINES:
        if board[a] != EMPTY and board[a] == board[b] == board[c]:
            return board[a]
    return None

def is_draw(board):
    return get_winner(board) is None and EMPTY not in board
