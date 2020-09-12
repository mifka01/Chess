import pygame as pg
from settings import *


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


class Pawn(Piece):
    def __init__(self, game, pos, color):
        super().__init__(game, pos, color)
        self.value = 1
        self.image = BLACKPAWN if self.color == BLACK else WHITEPAWN

    def ascend(self):
        if self.color == BLACK:
            if self.pos[1] == f"{len(LETTERS)}":
                print("ascend")
        else:
            if self.pos[1] == "1":
                print("ascend")

    def get_available_moves(self):
        pawn_pos = self.pos
        pawn_moves = []
        tiles = []
        if self.color == BLACK:
            if pawn_pos[0] != LETTERS[0]:
                tiles.append(next((tile for tile in self.game.tiles if tile.pos ==
                                   f"{LETTERS[LETTERS.index(pawn_pos[0])-1]}{int(pawn_pos[1])+1}"), None))
            if pawn_pos[0] != LETTERS[len(LETTERS)-1]:
                tiles.append(next((tile for tile in self.game.tiles if tile.pos ==
                                   f"{LETTERS[LETTERS.index(pawn_pos[0])+1]}{int(pawn_pos[1])+1}"), None))
            for tile in tiles:
                if tile != None:
                    if tile.occupied:
                        pawn_moves.append(tile.pos)
            tile = next((tile for tile in self.game.tiles if tile.pos ==
                         f"{pawn_pos[0]}{int(pawn_pos[1])+1}"), None)
            if tile != None:
                if not tile.occupied:
                    pawn_moves.append(tile.pos)
            if self.pos[1] == "2":
                tile = next((tile for tile in self.game.tiles if tile.pos ==
                         f"{pawn_pos[0]}{int(pawn_pos[1])+2}"), None)
                if tile != None:
                    if not tile.occupied:
                        pawn_moves.append(tile.pos)
        else:
            if pawn_pos[0] != LETTERS[0]:
                tiles.append(next((tile for tile in self.game.tiles if tile.pos ==
                                   f"{LETTERS[LETTERS.index(pawn_pos[0])-1]}{int(pawn_pos[1])-1}"), None))
            if pawn_pos[0] != LETTERS[len(LETTERS)-1]:
                tiles.append(next((tile for tile in self.game.tiles if tile.pos ==
                                   f"{LETTERS[LETTERS.index(pawn_pos[0])+1]}{int(pawn_pos[1])-1}"), None))
            for tile in tiles:
                if tile != None:
                    if tile.occupied:
                        pawn_moves.append(tile.pos)
            tile = next((tile for tile in self.game.tiles if tile.pos ==
                         f"{pawn_pos[0]}{int(pawn_pos[1])-1}"), None)
            if tile != None:
                if not tile.occupied:
                    pawn_moves.append(tile.pos)
            if self.pos[1] == "7":
                tile = next((tile for tile in self.game.tiles if tile.pos ==
                         f"{pawn_pos[0]}{int(pawn_pos[1])-2}"), None)
                if tile != None:
                    if not tile.occupied:
                        pawn_moves.append(tile.pos)

        return set(pawn_moves)

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
        rook_pos = self.pos
        forwards = []
        backwards = []
        lefts = []
        rights = []
        for i in range(1, len(LETTERS)+1):
            forward = next((tile for tile in self.game.tiles if tile.pos ==
                            f"{LETTERS[LETTERS.index(rook_pos[0])]}{int(rook_pos[1])-i}"), None)
            backward = next((tile for tile in self.game.tiles if tile.pos ==
                             f"{LETTERS[LETTERS.index(rook_pos[0])]}{int(rook_pos[1])+i}"), None)
            print(i, len(LETTERS),LETTERS.index(rook_pos[0]))
            if i < LETTERS.index(rook_pos[0]):
                left = next((tile for tile in self.game.tiles if tile.pos ==
                            f"{LETTERS[LETTERS.index(rook_pos[0])-i]}{int(rook_pos[1])}"), None)
            else:
                left = None
            if i < len(LETTERS) - LETTERS.index(rook_pos[0]):
                right = next((tile for tile in self.game.tiles if tile.pos ==
                                f"{LETTERS[LETTERS.index(rook_pos[0])+i]}{int(rook_pos[1])}"), None)
            else:
                right = None
            forwards.append(self.add_move(forward))
            backwards.append(self.add_move(backward))
            lefts.append(self.add_move(left))
            rights.append(self.add_move(right))
        forwards = [i for i in forwards if i]
        backwards = [i for i in backwards if i]
        lefts = [i for i in lefts if i]
        rights = [i for i in rights if i]
        forwards = sorted(forwards, key=lambda move: move[1], reverse=True)
        backwards = sorted(backwards, key=lambda move: move[1])
        lefts = sorted(lefts, key=lambda move: move[1], reverse=True)
        rights = sorted(rights, key=lambda move: move[1])
        result = self.get_real_moves(forwards) + self.get_real_moves(backwards) + self.get_real_moves(lefts) + self.get_real_moves(rights)
        return result
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

    def __str__(self):
        return self.pos

class Bishop(Piece):
    def __init__(self, game, pos, color):
        super().__init__(game, pos, color)
        self.value = 3
        self.image = BLACKBISHOP if self.color == BLACK else WHITEBISHOP

