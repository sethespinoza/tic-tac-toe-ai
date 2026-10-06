from tictactoe.board import (
    available_moves, 
    create_board, 
    make_move,
    get_winner,
    is_draw,
)
from tictactoe.players import minimax, minimax_player, other, random_player


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


def reference_player(board, mark):
    best_move = None
    best_score = -2
    for move in available_moves(board):
        child = make_move(board, move, mark)
        score = minimax(child, other(mark), mark)
        if score > best_score:
            best_score = score
            best_move = move
    return best_move


def collect_positions(board, turn, seen):
    key = tuple(board)
    if key in seen:
        return
    seen.add(key)
    if get_winner(board) is not None or is_draw(board):
        return
    for move in available_moves(board):
        collect_positions(make_move(board, move, turn), other(turn), seen)


def test_alpha_beta_picks_same_moves_as_plain_minimax():
    seen = set()
    collect_positions(create_board(), "X", seen)
    for key in seen:
        board = list(key)
        if get_winner(board) is not None or is_draw(board):
            continue
        if board.count(" ") > 6:
            continue
        turn = "X" if board.count("X") == board.count("O") else "O"
        assert minimax_player(board, turn) == reference_player(board, turn)