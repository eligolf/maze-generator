# Settings for the main file
# --------------------------------------------------------------------------------

import contextlib
with contextlib.redirect_stdout(None):
    import pygame
import math

    
# Screen
TITLE = 'Maze generator'

WIN_WIDTH = 702
WIN_HEIGHT = 702
SIZE = 20
THICKNESS = 1

SQX = math.floor(WIN_WIDTH/SIZE)
SQY = math.floor(WIN_HEIGHT/SIZE)

FPS = 120
# FPS depending on size of window
if 20 < SIZE:
    FPS_WIN = 60 / 4
    FPS_PROCESS = 60 * 1.5
elif 10 < SIZE <= 20:
    FPS_WIN = 60 / 1.5
    FPS_PROCESS = 60 * 2.5
elif 5 < SIZE <= 10:
    FPS_WIN = 60 / 1.3 
    FPS_PROCESS = 60 * 3
elif 0 <= SIZE <= 5:
    FPS_WIN = 60 / 1.2
else:
    FPS_WIN = 60 
    FPS_PROCESS = 60

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
ORANGE = (255, 128, 0)
PURPLE = (255, 0, 255)
PINK = (255, 153, 204)
GREY = [(x*32, x*32, x*32) for x in reversed(range(1, 8))]  # Grey scale, from light to dark

THINKING_COLOR = [RED, YELLOW] # Color of visualization of thinking process [neighbor node, current node]
CURRENT_COLOR = GREEN
VISITED_COLOR = PINK
BG = BLACK

# Text
pygame.font.init()
font = 'Helvetica'

TITLE_FONT = pygame.font.SysFont(font, 24, bold=True)
TITLE_COLOR = WHITE

OPT_FONT = pygame.font.SysFont(font, 20, bold=True)
OPT_COLOR = WHITE

OPT_FONT2 = pygame.font.SysFont(font, 18, bold=True)
OPT_COLOR2 = WHITE

GAME_FONT = pygame.font.SysFont(font, 14)
GAME_COLOR = WHITE
