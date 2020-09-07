from os import path
import pygame as pg

# WINDOW SETTINGS
WIDTH = 800
HEIGHT = 800
TITLE = "Chess"


# GAME SETTINGS
FPS = 60
BOARDSIZE = 800
ROWS = 8
COLUMNS = 8
TILESIZE = BOARDSIZE / ROWS
LETTERS = ["h", "g", "f", "e", "d", "c", "b", "a"]

#COLORS
BLACK = (0,0,0)
WHITE = (255,255,255)
#IMAGES
#BACKGROUND = pg.image.load(path.join('images','background.png'))