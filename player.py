import pygame as pg
from settings import *

class Player(object):
    def __init__(self, game, color):
        self.game = game
        self.score = 0
        self.color = color
        self.winner = False
        self.moved = False
        self.pieces = self.game.bpieces if self.color == BLACK else self.game.wpieces

    def move(self):
        move = None
        to = None
        while not self.moved:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.game.quit()
                if event.type == pg.MOUSEBUTTONDOWN:
                    mouse_pos = pg.mouse.get_pos()
                    for piece in self.pieces:
                        if piece.rect.collidepoint(mouse_pos[0], mouse_pos[1]):
                            move = piece
                            break
                    if move != None:
                        for tile in self.game.tiles:
                            if tile.pos == move.pos:
                                tile.occupied = False
                            if tile.rect.collidepoint(mouse_pos[0], mouse_pos[1]):
                                available_moves = move.get_available_moves()
                                if tile.pos in available_moves:
                                    to = tile
                                    break
                    if move != None and to != None:
                            print(f"Move: {move} To: {to}")
                            if to.occupied:
                                if self.color == BLACK:
                                    for piece in self.game.wpieces:
                                        if piece.pos == to.pos:
                                            self.game.wpieces.remove(piece)
                                            self.score += piece.value
                                else:
                                    for piece in self.game.bpieces:
                                        if piece.pos == to.pos:
                                            self.game.bpieces.remove(piece)
                                            self.score += piece.value
                            move.move(to.pos)
                            if move.value == 1:
                                move.ascend()
                            self.moved = True
                            break
    def play(self):
        self.move()
        self.game.update()
        self.moved = False