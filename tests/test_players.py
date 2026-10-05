from tictactoe.board import available_moves, create_board, make_move
from tictactoe.players import random_player


def test_random_player_returns_an_available_move():
    board = make_move(create_board(), 4, "X")
    for _ in range(50):
        assert random_player(board, "O") in available_moves(board)


def test_random_player_takes_the_only_open_square():
    board = ["X", "O", "X",
             "X", "O", "O",
             "O", "X", " "]
    assert random_player(board, "X") == 8


def test_random_player_does_not_change_the_board():
    board = create_board()
    random_player(board, "X")
    assert board == create_board()