"""
Holds functions for minimax algorithm for computer opponent to move.
"""

from copy import deepcopy
import pygame


BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

def minimax(position, depth, alpha, beta, max_player, game):
    """
    Function: Uses minimax algorithm with alpha beta pruning to search for best move of given depth.

    Input: 
            position (board object; passes in current state of the game),
            depth (int; depth of search, number of moves to look ahead),
            alpha (int; initialized to -infinity in main.py, gives current alpha value during search),
            beta (int; initialized to infinity in main.py, gives current beta value during search),
            max_player (boolean value; tells whether search is minimizing or maximizing value),
            game (game object; passes in current game)

    Output: 
            board object; Returns best game move for the depth searched.
    """
    
    if max_player:
        if depth == 0 or position.winner() != None:
            return position.evaluate(), position

        maxEval = float('-inf')
        best_move = None
        for move in get_all_moves(position, WHITE, game):
            evaluation = minimax(move, depth-1, alpha, beta, False, game)[0]
            maxEval = max(maxEval, evaluation)
            alpha = max(alpha, evaluation)
            
            if maxEval == evaluation:
                best_move = move
            elif beta <= alpha:
                break
            

        return maxEval, best_move

    else:
        if depth == 0 or position.winner() != None:
            return position.evaluate(), position

        minEval = float('inf')
        best_move = None
        for move in get_all_moves(position, BLACK, game):
            evaluation = minimax(move, depth-1, alpha, beta, True, game)[0]
            minEval = min(minEval, evaluation)
            beta = min(beta, evaluation)
            
            if minEval == evaluation:
                best_move = move
            elif beta <= alpha:
                break
            

        return minEval, best_move

def simulate_move(piece, move, board, game, skip):
    """
    Function: Simulates a move in the future state game object

    Input:
            piece (piece object; piece in which is moving),
            move (board object; move in which the piece passed in is making),
            board (board object; future state board that is going through simulation of moves),
            game (game object; current game being played),
            skip (array; pieces that are skipped in simulated move and need to be removed from board)

    Output:
            New board object that has the simulated move made on it.
    """

    board.move(piece, move[0], move[1])
    if skip:
        board.remove(skip)

    return board

def get_all_moves(board, color, game):
    """
    Function: Gets all valid moves for a particular state of the board.

    Input:
            board (board object; current state of the board to get moves from),
            color (string; color pieces to get all moves for),
            game (game object; current game being played)

    Output:
            Array of all valid moves possible for a certain color.
    """
    moves = []

    for piece in board.get_all_pieces(color):
        valid_moves = board.get_valid_moves(piece)
        for move, skip in valid_moves.items():
            temp_board = deepcopy(board)
            temp_piece = temp_board.get_piece(piece.row, piece.col)
            new_board = simulate_move(temp_piece, move, temp_board, game, skip)
            moves.append(new_board)

    return moves