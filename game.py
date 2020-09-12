import pygame as pg
from settings import *
from pygame.locals import QUIT
from sprites import *
from player import Player


class Game():
    def __init__(self):
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption(TITLE)
        pg.font.init()
        self.clock = pg.time.Clock()
        self.running = True
        self.playing = False

    def new(self):
        self.playing = True
        self.tiles = []
        self.bpieces = []
        self.wpieces = []
        self.load_tiles()
        self.load_pieces()
        self.player1 = Player(self, WHITE)
        self.player2 = Player(self, BLACK)

    def load_tiles(self):
        for row in range(0, ROWS):
            for column in range(0, COLUMNS):
                if row % 2 == 0:
                    if column % 2 == 0:
                        self.tiles.append(
                            Tile(self, f"{LETTERS[column]}{row+1}", WHITE, column * TILESIZE, row * TILESIZE))

                    else:
                        self.tiles.append(
                            Tile(self, f"{LETTERS[column]}{row+1}", BLACK, column * TILESIZE, row * TILESIZE))

                else:
                    if column % 2 == 0:
                        self.tiles.append(
                            Tile(self, f"{LETTERS[column]}{row+1}", BLACK, column * TILESIZE, row * TILESIZE))

                    else:
                        self.tiles.append(
                            Tile(self, f"{LETTERS[column]}{row+1}", WHITE, column * TILESIZE, row * TILESIZE))
    def load_pieces(self):
        for letter in LETTERS:
            self.bpieces.append(Pawn(self, f"{letter}2", BLACK))
            self.wpieces.append(Pawn(self, f"{letter}7", WHITE))
        self.bpieces.append(Rook(self, f"a1", BLACK))
        self.bpieces.append(Rook(self, f"h1", BLACK))
        self.wpieces.append(Rook(self, f"a8", WHITE))
        self.wpieces.append(Rook(self, f"h8", WHITE))
        self.bpieces.append(Bishop(self, f"c1", BLACK))
        self.bpieces.append(Bishop(self, f"f1", BLACK))
        self.wpieces.append(Bishop(self, f"c8", WHITE))
        self.wpieces.append(Bishop(self, f"f8", WHITE))
    def events(self):
        for event in pg.event.get():
            if event.type == QUIT:
                self.quit()

    def update(self):
        self.draw()
        pg.display.update()
    def draw_board(self):
        for tile in self.tiles:
            tile.draw()

    def draw_pieces(self):
        for bpiece in self.bpieces:
            bpiece.draw()
        for wpiece in self.wpieces:
            wpiece.draw()

    def draw(self):
        self.draw_board()
        self.draw_pieces()

    def run(self):
        while self.playing:
            self.update()
            self.events()
            self.player1.play()
            self.player1.pieces = self.wpieces
            self.player2.play()
            self.player2.pieces = self.bpieces

    def quit(self):
        self.running = False
        pg.quit()
        exit()
