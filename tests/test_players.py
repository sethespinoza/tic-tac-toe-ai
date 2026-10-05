from tictactoe.board import (
    available_moves, 
    create_board, 
    make_move,
    get_winner,
    is_draw,
    make_move,
)
from tictactoe.players import minimax_player, other, random_player


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


def test_minimax_takes_immediate_win():
    board = ["X", "X", " ",
             "O", "O", " ",
             " ", " ", " "]
    assert minimax_player(board, "X") == 2


def test_minimax_blocks_opponent_win():
    board = ["O", "O", " ",
             "X", " ", " ",
             " ", " ", "X"]
    assert minimax_player(board, "X") == 2


def ai_never_loses(board, turn, ai):
    winner = get_winner(board)
    if winner is not None:
        return winner == ai
    if is_draw(board):
        return True

    if turn == ai:
        move = minimax_player(board, ai)
        return ai_never_loses(make_move(board, move, ai), other(ai), ai)

    return all(
        ai_never_loses(make_move(board, move, turn), ai, ai)
        for move in available_moves(board)
    )


def test_minimax_never_loses_playing_first():
    assert ai_never_loses(create_board(), "X", "X")


def test_minimax_never_loses_playing_second():
    assert ai_never_loses(create_board(), "X", "O")