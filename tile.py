import pygame as pg
from settings import TILESIZE

class Tile(pg.sprite.Sprite):

    def __init__(self, game, pos, color, x, y):
       pg.sprite.Sprite.__init__(self)
       self.game = game
       self.surface = pg.Surface((TILESIZE, TILESIZE))
       self.surface.fill(color)
       self.color = color
       self.rect = self.surface.get_rect()
       self.rect.x = x
       self.rect.y = y
       self.pos = pos

    def draw(self):
        pg.draw.rect(self.game.screen, self.color, self.rect)