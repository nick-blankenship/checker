"""
Main game file to be run to play game.

    -To play against computer leave as is and run. You can select depth of search for opponent in line 37.

    -To watch computer play itself, comment out lines 58-61 and uncomment lines 41-44. You can also select depth of search for black pieces.

-Winner will be returned as RGB tuple of color that won
"""


import pygame
from check.constants import WIDTH, HEIGHT, SQUARE_SIZE, WHITE, BLACK
from check.board import Board
from check.game import Game
from minimax.MM import minimax

FPS = 60

WIN = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("Checkers")

def get_row_col_from_mouse(pos):
    x, y = pos
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row, col


def main():
    run = True
    clock = pygame.time.Clock()
    game = Game(WIN)
    move_count = 0


    while run:
        clock.tick(FPS)

        if game.turn == WHITE:
            value, new_board = minimax(game.get_board(), 5, float('-inf'), float('inf'),  True, game)
            move_count += 1
            game.ai_move(new_board)
        #elif game.turn == BLACK:
            #value, new_board = minimax(game.get_board(), 2, float('-inf'), float('inf'),  False, game)
            #move_count += 1
            #game.ai_move(new_board)
        
        if game.winner() != None:
            print(game.winner())
            run = False

        if move_count >= 100:
            print('Draw')
            run = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row, col = get_row_col_from_mouse(pos)
                game.select(row, col)

        game.update()

    pygame.quit()



main()