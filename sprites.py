import pygame as pg
from settings import *
from move_methods import *


class Tile(pg.sprite.Sprite):

    def __init__(self, game, pos, color, x, y):
        pg.sprite.Sprite.__init__(self)
        self.game = game
        self.color = color
        self.image = BLACKTILE if self.color == BLACK else WHITETILE
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.occupied = False
        self.pos = pos

    def draw(self):
        self.game.screen.blit(self.image, self.rect)

    def __str__(self):
        return self.pos


class Piece(pg.sprite.Sprite):
    def __init__(self, game, pos, color):
        pg.sprite.Sprite.__init__(self)
        self.game = game
        self.color = color
        self.pos = pos

    def move(self, pos):
        self.pos = pos
        for tile in self.game.tiles:
            if tile.pos == self.pos:
                self.rect = tile.rect
                tile.occupied = True
                self.game.screen.blit(self.image, self.rect)

    def draw(self):
        for tile in self.game.tiles:
            if tile.pos == self.pos:
                tile.occupied = True
                self.rect = tile.rect
                self.game.screen.blit(self.image, tile.rect)

    def add_move(self, value):
        if value != None:
            if not value.occupied:
                return value.pos
            else:
                return f"{value.pos}#"
        else:
            return

    def get_real_moves(self, list):
        result = []
        for move in list:
            if len(move) > 2:
                if self.color == BLACK:
                    if move[:-1] in [piece.pos for piece in self.game.wpieces]:
                        result.append(move[:-1])
                else:
                    if move[:-1] in [piece.pos for piece in self.game.bpieces]:
                        result.append(move[:-1])
                break
            else:
                result.append(move)
        return result


class Pawn(Piece):
    def __init__(self, game, pos, color):
        super().__init__(game, pos, color)
        self.value = 1
        self.image = BLACKPAWN if self.color == BLACK else WHITEPAWN

    def ascend(self):
        chosen = False
        if self.color == BLACK:
            pieces = [{"type": "Queen", "image": BLACKQUEEN},
                      {"type": "Knight", "image": BLACKKNIGHT},
                      {"type": "Bishop", "image": BLACKBISHOP},
                      {"type": "Rook", "image": BLACKROOK}
                      ]
            if self.pos[1] == f"{len(LETTERS)}":
                self.game.screen.blit(ASCEND,(BOARDSIZE/2 - ASCEND.get_width()/2, BOARDSIZE/2 - ASCEND.get_height()/2))
                for i, piece in enumerate(pieces):
                    self.game.screen.blit(piece["image"], (BOARDSIZE/2 - ASCEND.get_width() / 2 +(i*128),BOARDSIZE/2 - ASCEND.get_height()/4,128,128))
                    piece["rect"] = pg.Rect((BOARDSIZE/2 - ASCEND.get_width() / 2 +(i*128),BOARDSIZE/2 - ASCEND.get_height()/4,128,128))
                pg.display.update()
                while not chosen:
                    for event in pg.event.get():
                        if event.type == pg.MOUSEBUTTONDOWN:
                            mouse_pos = pg.mouse.get_pos()
                            for piece in pieces:
                                if piece["rect"].collidepoint(mouse_pos[0], mouse_pos[1]):
                                    self.game.bpieces.remove(self)
                                    if piece["type"] == "Queen":
                                        self.game.bpieces.append(
                                            Queen(self.game, self.pos, self.color))
                                    if piece["type"] == "Knight":
                                        self.game.bpieces.append(
                                            Knight(self.game, self.pos, self.color))
                                    if piece["type"] == "Bishop":
                                        self.game.bpieces.append(
                                            Bishop(self.game, self.pos, self.color))
                                    if piece["type"] == "Rook":
                                        self.game.bpieces.append(
                                            Rook(self.game, self.pos, self.color))
                                    chosen = True
        else:
            pieces = [{"type": "Queen", "image": WHITEQUEEN},
                      {"type": "Knight", "image": WHITEKNIGHT},
                      {"type": "Bishop", "image": WHITEBISHOP},
                      {"type": "Rook", "image": WHITEROOK}]
            if self.pos[1] == "1":
                self.game.screen.blit(ASCEND,(BOARDSIZE/2 - ASCEND.get_width()/2, BOARDSIZE/2 - ASCEND.get_height()/2))
                for i, piece in enumerate(pieces):
                    self.game.screen.blit(piece["image"], (BOARDSIZE/2 - ASCEND.get_width() / 2 +(i*128),BOARDSIZE/2 - ASCEND.get_height()/4,128,128))
                    piece["rect"] = pg.Rect((BOARDSIZE/2 - ASCEND.get_width() / 2 +(i*128),BOARDSIZE/2 - ASCEND.get_height()/4,128,128))
                pg.display.update()
                while not chosen:
                    for event in pg.event.get():
                        if event.type == pg.MOUSEBUTTONDOWN:
                            mouse_pos = pg.mouse.get_pos()
                            for piece in pieces:
                                if piece["rect"].collidepoint(mouse_pos[0], mouse_pos[1]):
                                    self.game.wpieces.remove(self)
                                    if piece["type"] == "Queen":
                                        self.game.wpieces.append(
                                            Queen(self.game, self.pos, self.color))
                                    if piece["type"] == "Knight":
                                        self.game.wpieces.append(
                                            Knight(self.game, self.pos, self.color))
                                    if piece["type"] == "Bishop":
                                        self.game.wpieces.append(
                                            Bishop(self.game, self.pos, self.color))
                                    if piece["type"] == "Rook":
                                        self.game.wpieces.append(
                                            Rook(self.game, self.pos, self.color))
                                    chosen = True

    def get_available_moves(self):
        return get_pawn_moves(self)

    def update(self):
        self.ascend()

    def __str__(self):
        return self.pos


class Rook(Piece):
    def __init__(self, game, pos, color):
        super().__init__(game, pos, color)
        self.value = 5
        self.image = BLACKROOK if self.color == BLACK else WHITEROOK

    def get_available_moves(self):
        return get_rook_moves(self)

    def __str__(self):
        return self.pos


class Bishop(Piece):
    def __init__(self, game, pos, color):
        super().__init__(game, pos, color)
        self.value = 3
        self.image = BLACKBISHOP if self.color == BLACK else WHITEBISHOP

    def get_available_moves(self):
        return get_bishop_moves(self)

    def __str__(self):
        return self.pos


class Knight(Piece):
    def __init__(self, game, pos, color):
        super().__init__(game, pos, color)
        self.value = 3
        self.image = BLACKKNIGHT if self.color == BLACK else WHITEKNIGHT

    def get_available_moves(self):
        return get_knight_moves(self)

    def __str__(self):
        return self.pos


class King(Piece):
    def __init__(self, game, pos, color):
        super().__init__(game, pos, color)
        self.value = 99
        self.checked = False
        self.image = BLACKKING if self.color == BLACK else WHITEKING

    def get_available_moves(self):
        return get_king_moves(self)

    def __str__(self):
        return self.pos


class Queen(Piece):
    def __init__(self, game, pos, color):
        super().__init__(game, pos, color)
        self.value = 9
        self.image = BLACKQUEEN if self.color == BLACK else WHITEQUEEN

    def get_available_moves(self):
        return get_queen_moves(self)

    def __str__(self):
        return self.pos
