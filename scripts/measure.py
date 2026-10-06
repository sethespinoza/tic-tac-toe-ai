"""Compare how many board positions plain minimax and alpha-beta search.

Run from project root with: python -m scripts.measure
"""

import time

import tictactoe.players as players
from tictactoe.board import available_moves, create_board, make_move

count = 0
original_get_winner = players.get_winner


def counting_get_winner(board):
    global count
    count += 1
    return original_get_winner(board)


players.get_winner = counting_get_winner


def plain_minimax_player(board, mark):
    best_move = None
    best_score = -2
    for move in available_moves(board):
        child = make_move(board, move, mark)
        score = players.minimax(child, players.other(mark), mark)
        if score > best_score:
            best_score = score
            best_move = move
    return best_move


def measure(label, player):
    global count
    count = 0
    start = time.perf_counter()
    move = player(create_board(), "X")
    seconds = time.perf_counter() - start
    print(f"{label}: move={move}, positions={count}, seconds={seconds:.3f}")
    return count


plain = measure("plain minimax", plain_minimax_player)
pruned = measure("alpha-beta   ", players.minimax_player)
print(f"alpha-beta searched {plain / pruned:.1f}x fewer positions")