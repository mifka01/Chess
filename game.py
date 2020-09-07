import pygame as pg
from settings import *
from pygame.locals import QUIT
from tile import Tile


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
        for row in range(0, ROWS):
            for column in range(0, COLUMNS):
                if row % 2 == 0:
                    if column % 2 == 0:
                        self.tiles.append(
                            Tile(self, f"{LETTERS[column]}{row+1}", BLACK, column * TILESIZE, row * TILESIZE))

                    else:
                        self.tiles.append(
                            Tile(self, f"{LETTERS[column]}{row+1}", WHITE, column * TILESIZE, row * TILESIZE))

                else:
                    if column % 2 == 0:
                        self.tiles.append(
                            Tile(self, f"{LETTERS[column]}{row+1}", WHITE, column * TILESIZE, row * TILESIZE))

                    else:
                        self.tiles.append(
                            Tile(self, f"{LETTERS[column]}{row+1}", BLACK, column * TILESIZE, row * TILESIZE))

    def events(self):
        for event in pg.event.get():
            if event.type == QUIT:
                self.quit()
            if event.type == pg.MOUSEBUTTONDOWN:
                mouse_pos = pg.mouse.get_pos()
                for tile in self.tiles:
                    if tile.rect.collidepoint(mouse_pos[0], mouse_pos[1]):
                        print(tile.pos)
                        break

    def update(self):
        self.draw()
        pg.display.update()

    def draw_board(self):
        for tile in self.tiles:
            tile.draw()

    def draw(self):
        self.draw_board()

    def run(self):
        while self.playing:
            self.events()
            self.update()

    def quit(self):
        self.running = False
        pg.quit()
        exit()
