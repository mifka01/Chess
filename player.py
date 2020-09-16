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
    def check_king(self):
        kings = []
        threat = []
        for piece in self.game.all_pieces:
            if piece.value == 99:
                kings.append(piece)
        for king in kings:
            if king.color == BLACK:
                for white_piece in self.game.wpieces:
                    threat += white_piece.get_available_moves()
            else:
                for black_piece in self.game.bpieces:
                    threat += black_piece.get_available_moves()
            count = threat.count(king.pos)
            if count > 0 and count < 2:
                king.checked = True
            else:
                king.checked = False
            if count > 1:
                self.winner = True
                print(f"{self.color} WINS")
                self.game.running = False
                return

        for king in kings:
            print(king.checked)
            if king.checked:
                for tile in self.game.tiles:
                    if king.pos == tile.pos:
                        tile.image = CHECKED
                        tile.draw()
            else:
                for tile in self.game.tiles:
                    if king.pos == tile.pos:
                        tile.image = BLACKTILE if king.color == BLACK else WHITETILE
                        tile.draw()
            king.draw()
            pg.display.update()
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
                                for tiley in self.game.tiles:
                                    for movey in available_moves:
                                        if movey == tiley.pos:
                                            tiley.image = AMOVE
                                            tiley.draw()
                                            for piece in self.game.all_pieces:
                                                if piece.pos == movey:
                                                    piece.draw()
                                            pg.display.update()
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
        self.check_king()
        self.move()
        for tile in self.game.tiles:
            if tile.image != BLACKTILE and tile.image != WHITETILE:
                if tile.image == CHECKED:
                    if tile.occupied == False:
                        if tile.color == BLACK:
                            tile.image = BLACKTILE
                        else:
                            tile.image = WHITETILE
                else:
                    if tile.color == BLACK:
                        tile.image = BLACKTILE
                    else:
                        tile.image = WHITETILE
            else:
                pass
        self.game.update()
        self.moved = False