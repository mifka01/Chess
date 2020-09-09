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
        super().__init__(game,pos,color)
        self.value = 1
        self.image = BLACKPAWN if self.color == BLACK else WHITEPAWN

    def get_available_moves(self):
        pawn_pos = self.pos
        pawn_moves = []
        tiles = []
        if self.color == BLACK:
            for i in range(1,3):
                if pawn_pos[0] != LETTERS[0]:
                    tiles.append(next((tile for tile in self.game.tiles if tile.pos == f"{LETTERS[LETTERS.index(pawn_pos[0])-1]}{int(pawn_pos[1])+1}"), None))
                if pawn_pos[0] != LETTERS[len(LETTERS)-1]:
                    tiles.append(next((tile for tile in self.game.tiles if tile.pos == f"{LETTERS[LETTERS.index(pawn_pos[0])+1]}{int(pawn_pos[1])+1}"), None))
                for tile in tiles:
                    if tile.occupied:
                        pawn_moves.append(tile.pos)
                tile = next((tile for tile in self.game.tiles if tile.pos == f"{pawn_pos[0]}{int(pawn_pos[1])+i}"), None)
                if tile != None:
                    if not tile.occupied:
                        pawn_moves.append(tile.pos)
                    else:
                        break
        else:
            for i in range(1,3):
                if pawn_pos[0] != LETTERS[0]:
                    tiles.append(next((tile for tile in self.game.tiles if tile.pos == f"{LETTERS[LETTERS.index(pawn_pos[0])-1]}{int(pawn_pos[1])-1}"), None))
                if pawn_pos[0] != LETTERS[len(LETTERS)-1]:
                    tiles.append(next((tile for tile in self.game.tiles if tile.pos == f"{LETTERS[LETTERS.index(pawn_pos[0])+1]}{int(pawn_pos[1])-1}"), None))
                for tile in tiles:
                    if tile.occupied:
                        pawn_moves.append(tile.pos)
                tile = next((tile for tile in self.game.tiles if tile.pos == f"{pawn_pos[0]}{int(pawn_pos[1])-i}"), None)
                if tile != None:
                    if not tile.occupied:
                        pawn_moves.append(tile.pos)
                    else:
                        break

        return set(pawn_moves)


    def __str__(self):
        return self.pos


class Rook(Piece):
    def __init__(self, game, pos, color):
            super().__init__(game,pos,color)
            self.value = 5
            self.image = BLACKROOK if self.color == BLACK else WHITEROOK


    def get_available_moves(self):
        rook_pos = self.pos
        return set(rook_moves)

    def __str__(self):
        return self.pos