import pytest

from tictactoe.board import (
    EMPTY,
    WINNING_LINES,
    available_moves,
    create_board,
    get_winner,
    is_draw,
    is_valid_move,
    make_move,
)


def test_create_board_is_all_empty():
    board = create_board()
    assert len(board) == 9
    assert all(square == EMPTY for square in board)


def test_make_move_places_mark():
    board = make_move(create_board(), 4, "X")
    assert board[4] == "X"


def test_make_move_does_not_change_original():
    original = create_board()
    make_move(original, 4, "X")
    assert original == create_board()


def test_make_move_on_taken_square_raises():
    board = make_move(create_board(), 4, "X")
    with pytest.raises(ValueError):
        make_move(board, 4, "O")


@pytest.mark.parametrize("position", [-1, 9, 100])
def test_is_valid_move_rejects_out_of_range(position):
    assert is_valid_move(create_board(), position) is False


def test_available_moves_excludes_taken_squares():
    board = make_move(create_board(), 4, "X")
    assert available_moves(board) == [0, 1, 2, 3, 5, 6, 7, 8]


def test_empty_board_has_no_winner():
    assert get_winner(create_board()) is None


@pytest.mark.parametrize("line", WINNING_LINES)
def test_every_winning_line_is_detected(line):
    board = create_board()
    for position in line:
        board = make_move(board, position, "O")
    assert get_winner(board) == "O"


def test_draw_is_detected():
    board = ["X", "O", "X",
             "X", "O", "O",
             "O", "X", "X"]
    assert get_winner(board) is None
    assert is_draw(board) is True


def test_full_board_with_winner_is_not_a_draw():
    board = ["X", "X", "X",
             "O", "O", "X",
             "X", "O", "O"]
    assert get_winner(board) == "X"
    assert is_draw(board) is False


def test_unfinished_game_is_not_a_draw():
    assert is_draw(create_board()) is False