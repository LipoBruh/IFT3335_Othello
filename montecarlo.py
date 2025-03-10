import othello
import numpy as np
from minimax import GAMETIME, PONDERATION1,PONDERATION2,PONDERATION3

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





"HEURISTIQUES DE BASE DEMANDEES PAR LE TP POUR TASK 1"
def evaluate_move(move): #Was previously the only criteria in evaluate_board
    (row, col) = move
    return WEIGHTS[row][col]


def evaluate_board(board): 
    #la fx d'evaluation de base considere seulement le differentiel entre les pieces blanches ou noires sans considerer l'importance des cases
    return np.sum(board == WHITE) - np.sum(board == BLACK)

#will bonify the eval fx based on the nb of valid moves possible based on the new board.
def evaluate_nb_positions(game,player):
    return len(game.get_valid_moves(player))

"HEURISTIQUES SUPPLEMENTAIRES POUR TASK 1"



def montecarlo(board, depth, maximizing, player,alpha,beta):
    print('...')
    global GAMETIME
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
            #Score is more than just the difference in progress
            #if the move is done in a square that has a good weight for the gameplay, the score is bonified, otherwise it is penalized
            eval_score, _ = alphabeta(new_board, depth - 1, False, -player,alpha,beta)
            eval_score*=PONDERATION1
            eval_score+= PONDERATION2*evaluate_move(move) + PONDERATION3*evaluate_nb_positions(game,player)
            #
            if eval_score > max_eval:
                max_eval = eval_score
                best_move = move
                alpha=max_eval
            #
            #Pruning if out of bounds
            if eval_score < alpha:
                return max_eval, best_move
            if eval_score > beta:
                return max_eval, best_move
            #
        return max_eval, best_move
    else:
        min_eval = float("inf")


        for move in valid_moves:

            new_board = game.board.copy()
            game.apply_move(move, player)
            eval_score, _ = montecarlo(new_board, depth - 1, True, -player,alpha,beta)
            eval_score*=PONDERATION1
            eval_score+= PONDERATION2*evaluate_move(move) + PONDERATION3*evaluate_nb_positions(game,player)
            
            if eval_score < min_eval:
                min_eval = eval_score
                best_move = move
                beta=min_eval
            #
            #Pruning if out of bounds
            if eval_score < alpha:
                return min_eval, best_move
            if eval_score > beta:
                return min_eval, best_move
            #
        return min_eval, best_move
    
