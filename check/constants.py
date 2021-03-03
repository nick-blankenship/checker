"""
Holds all constant values and images for game 
"""

import pygame

#size of window for game
WIDTH, HEIGHT = 800, 800

#number of rows and columns for board
ROWS = 8
COLS = 8

#size of squares for board
SQUARE_SIZE = WIDTH//COLS


#rgb colors
RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GREY = (128, 128, 128)
BROWN = (89, 60, 31)
BEIGE = (244, 226, 198)

#image for kinged pieces
CROWN = pygame.transform.scale(pygame.image.load('assets/crown1.png'), (90,60))
