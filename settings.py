from os import path
import pygame as pg

# WINDOW SETTINGS
WIDTH = 1024
HEIGHT = 1024
TITLE = "Chess"


# GAME SETTINGS
FPS = 60
BOARDSIZE = 1024
ROWS = 8
COLUMNS = 8
TILESIZE = BOARDSIZE / ROWS
LETTERS = ["h", "g", "f", "e", "d", "c", "b", "a"]

#COLORS
BLACK = (0,0,0)
WHITE = (255,255,255)

#IMAGES
WHITETILE = pg.image.load(path.join("assets", "wtile.png"))
BLACKTILE = pg.image.load(path.join("assets", "btile.png"))
AMOVE = pg.image.load(path.join("assets", "amove.png"))

BLACKPAWN = pg.image.load(path.join('assets','bpawn.png'))
WHITEPAWN = pg.image.load(path.join('assets','wpawn.png'))

BLACKROOK = pg.image.load(path.join('assets','brook.png'))
WHITEROOK = pg.image.load(path.join('assets','wrook.png'))

BLACKBISHOP = pg.image.load(path.join('assets','bbishop.png'))
WHITEBISHOP = pg.image.load(path.join('assets','wbishop.png'))