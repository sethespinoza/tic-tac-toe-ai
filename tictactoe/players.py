import random

from tictactoe.board import available_moves

def random_player(board, mark):
    return random.choice(available_moves(board))