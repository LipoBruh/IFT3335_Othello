import othello
import numpy as np

EMPTY = 0
BLACK = 1
WHITE = -1
DEPTH = 6 # Profondeur du Minimax

WEIGHTS = [
    [ 500,-150,30,10,10,30,-150, 500],
    [-150,-250, 0, 0, 0, 0,-250,-150],
    [  30,   0, 1, 2, 2, 1,   0,  30],
    [  10,   0, 2,16,16, 2,   0,  10],
    [  10,   0, 2,16,16, 2,   0,  10],
    [  30,   0, 1, 2, 2, 1,   0,  30],
    [-150,-250, 0, 0, 0, 0,-250,-150],
    [ 500,-150,30,10,10,30,-150, 500],
] #From Tp specification


""

def evaluate_board(board): 
    #la fx d'evaluation de base considere seulement le differentiel entre les pieces blanches ou noires sans considerer l'importance des cases
    # previously : return np.sum(board == WHITE) - np.sum(board == BLACK)
    return 



def minimax(board, depth, maximizing, player):
    """Minimax AI with depth limit."""
    game = othello.Othello()
    game.board = board.copy()

    if depth == 0 or game.is_game_over():
        return evaluate_board(game.board), None

    valid_moves = game.get_valid_moves(player)
    best_move = None

    if maximizing:
        max_eval = float("-inf")
        for move in valid_moves:
            new_board = game.board.copy()
            game.apply_move(move, player)
            eval_score, _ = minimax(new_board, depth - 1, False, -player)
            if eval_score > max_eval:
                max_eval = eval_score
                best_move = move
        return max_eval, best_move
    else:
        min_eval = float("inf")
        for move in valid_moves:
            new_board = game.board.copy()
            game.apply_move(move, player)
            eval_score, _ = minimax(new_board, depth - 1, True, -player)
            if eval_score < min_eval:
                min_eval = eval_score
                best_move = move
        return min_eval, best_move
    
