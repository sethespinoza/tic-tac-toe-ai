import random

from tictactoe.board import available_moves, get_winner, is_draw, make_move

def random_player(board, mark):
    return random.choice(available_moves(board))

def other(mark):
    return "O" if mark == "X" else "X"

def minimax(board, current, me):
    winner = get_winner(board)
    if winner == me:
        return 1
    if winner is not None:
        return -1
    if is_draw(board):
        return 0
    
    scores = []
    for move in available_moves(board):
        child = make_move(board, move, current)
        scores.append(minimax(child, other(current), me))
    
    return max(scores) if current == me else min(scores)

def minimax_player(board, mark):
    best_move = None
    best_score = -2
    for move in available_moves(board):
        child = make_move(board, move, mark)
        score = minimax(child, other(mark), mark)
        if score > best_score:
            best_score = score
            best_move = move
    return best_move
    