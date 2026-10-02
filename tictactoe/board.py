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
        