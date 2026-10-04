from tictactoe.board import (
    create_board,
    format_board,
    get_winner,
    is_draw,
    is_valid_move,
    make_move,
)

def ask_for_move(board, mark):
    while True:
        raw = input(f"Player {mark}, choose a square (1-9): ")
        try:
            position = int(raw) - 1
        except ValueError:
            print("Please enter a number from 1 to 0.")
            continue
        if not is_valid_move(board, position):
            print("That square is taken or out of range. Try a different square.")
            continue
        return position

def play():
    board = create_board()
    mark = "X"
    print("Squares are numbered like this:")
    print(format_board([str(i) for i in range(1, 10)]))

    while True:
        print()
        print(format_board(board))
        position = ask_for_move(board, mark)
        board = make_move(board, position, mark)

        if get_winner(board):
            print()
            print(format_board(board))
            print(f"Player {mark} wins!")
            return
        if is_draw(board):
            print()
            print(format_board(board))
            print("It's a draw.")
            return

        mark = "O" if mark == "X" else "X"


if __name__ == "__main__":
    play()
