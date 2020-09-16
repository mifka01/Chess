from settings import *


def get_pawn_moves(self):
        pawn_pos = self.pos
        left = []
        right = []
        tiles = []
        blocked =  False
        if self.color == BLACK:
            if pawn_pos[0] != LETTERS[0]:
                tile = next((tile for tile in self.game.tiles if tile.pos ==
                                f"{LETTERS[LETTERS.index(pawn_pos[0])-1]}{int(pawn_pos[1])+1}"), None)
                temp = self.add_move(tile)
                if tile.occupied:
                    right.append(temp)
            if pawn_pos[0] != LETTERS[len(LETTERS)-1]:
                tile = next((tile for tile in self.game.tiles if tile.pos ==
                                f"{LETTERS[LETTERS.index(pawn_pos[0])+1]}{int(pawn_pos[1])+1}"), None)
                temp = self.add_move(tile)
                if tile.occupied:
                    left.append(temp)
            tile = next((tile for tile in self.game.tiles if tile.pos ==
                            f"{LETTERS[LETTERS.index(pawn_pos[0])]}{int(pawn_pos[1])+1}"), None)
            if tile != None:
                temp = self.add_move(tile)
                if not tile.occupied:
                    blocked = False
                    tiles.append(temp)
                else:
                    blocked = True
            if int(pawn_pos[1]) == 2:
                tile = next((tile for tile in self.game.tiles if tile.pos ==
                            f"{LETTERS[LETTERS.index(pawn_pos[0])]}{int(pawn_pos[1])+2}"), None)
                if tile != None:
                    temp = self.add_move(tile)
                    if not tile.occupied and not blocked:
                        tiles.append(temp)
        else:
            if pawn_pos[0] != LETTERS[0]:
                tile = next((tile for tile in self.game.tiles if tile.pos ==
                                f"{LETTERS[LETTERS.index(pawn_pos[0])-1]}{int(pawn_pos[1])-1}"), None)
                temp = self.add_move(tile)
                if tile.occupied:
                    right.append(temp)
            if pawn_pos[0] != LETTERS[len(LETTERS)-1]:
                tile = next((tile for tile in self.game.tiles if tile.pos ==
                                f"{LETTERS[LETTERS.index(pawn_pos[0])+1]}{int(pawn_pos[1])-1}"), None)
                temp = self.add_move(tile)
                if tile.occupied:
                    left.append(temp)
            tile = next((tile for tile in self.game.tiles if tile.pos ==
                            f"{LETTERS[LETTERS.index(pawn_pos[0])]}{int(pawn_pos[1])-1}"), None)
            if tile != None:
                temp = self.add_move(tile)
                if not tile.occupied:
                    blocked = False
                    tiles.append(temp)
                else:
                    blocked = True
            if int(pawn_pos[1]) == 7:
                tile = next((tile for tile in self.game.tiles if tile.pos ==
                            f"{LETTERS[LETTERS.index(pawn_pos[0])]}{int(pawn_pos[1])-2}"), None)
                if tile != None:
                    temp = self.add_move(tile)
                    if not tile.occupied and not blocked:
                        tiles.append(temp)

        left = sorted(left, key=lambda move: move[1])
        right = sorted(right, key=lambda move: move[1])
        tiles = sorted(tiles, key=lambda move: move[1])
        tiles = self.get_real_moves(tiles) + self.get_real_moves(left) + self.get_real_moves(right)
        return tiles
def get_rook_moves(self):
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
        if i <= LETTERS.index(rook_pos[0]):
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

def get_bishop_moves(self):
    bishop_pos = self.pos
    leftups = []
    leftdowns = []
    rightups = []
    rightdowns = []
    for i in range(1, len(LETTERS)+1):
        if i <= LETTERS.index(bishop_pos[0]):
            leftup = next((tile for tile in self.game.tiles if tile.pos ==
                            f"{LETTERS[LETTERS.index(bishop_pos[0])-i]}{int(bishop_pos[1])-i}"), None)
            rightdown = next((tile for tile in self.game.tiles if tile.pos ==
                            f"{LETTERS[LETTERS.index(bishop_pos[0])-i]}{int(bishop_pos[1])+i}"), None)
        else:
            leftup = None
            rightdown = None
        if i < len(LETTERS) - LETTERS.index(bishop_pos[0]):
            leftdown = next((tile for tile in self.game.tiles if tile.pos ==
                            f"{LETTERS[LETTERS.index(bishop_pos[0])+i]}{int(bishop_pos[1])+i}"), None)
            rightup = next((tile for tile in self.game.tiles if tile.pos ==
                            f"{LETTERS[LETTERS.index(bishop_pos[0])+i]}{int(bishop_pos[1])-i}"), None)
        else:
            leftdown = None
            rightup = None
        leftups.append(self.add_move(leftup))
        leftdowns.append(self.add_move(leftdown))
        rightups.append(self.add_move(rightup))
        rightdowns.append(self.add_move(rightdown))
    leftups = [i for i in leftups if i]
    leftdowns = [i for i in leftdowns if i]
    rightups = [i for i in rightups if i]
    rightdowns = [i for i in rightdowns if i]
    leftups = sorted(leftups, key=lambda move: move[1], reverse=True)
    leftdowns = sorted(leftdowns, key=lambda move: move[1])
    rightups = sorted(rightups, key=lambda move: move[1], reverse=True)
    rightdowns = sorted(rightdowns, key=lambda move: move[1])
    result = self.get_real_moves(leftups) + self.get_real_moves(leftdowns) + self.get_real_moves(rightups) + self.get_real_moves(rightdowns)
    return result

def get_knight_moves(self):
    knight_pos = self.pos
    result = []
    leftups = []
    leftdowns = []
    rightups = []
    rightdowns = []
    one = []
    two = []
    three = []
    four = []
    if LETTERS.index(knight_pos[0]) > 0:
        #LEFTUP
        leftups.append(self.add_move(next((tile for tile in self.game.tiles if tile.pos == f"{LETTERS[LETTERS.index(knight_pos[0])-1]}{int(knight_pos[1])-2}"), None)))
        #LEFTDOWN
        leftdowns.append(self.add_move(next((tile for tile in self.game.tiles if tile.pos == f"{LETTERS[LETTERS.index(knight_pos[0])-1]}{int(knight_pos[1])+2}"), None)))
        if LETTERS.index(knight_pos[0]) > 1:
            one.append(self.add_move(next((tile for tile in self.game.tiles if tile.pos == f"{LETTERS[LETTERS.index(knight_pos[0])-2]}{int(knight_pos[1])-1}"), None)))
            two.append(self.add_move(next((tile for tile in self.game.tiles if tile.pos == f"{LETTERS[LETTERS.index(knight_pos[0])-2]}{int(knight_pos[1])+1}"), None)))
        else:
            one.append(None)
            two.append(None)
    else:
        leftups.append(None)
        leftdowns.append(None)
    if LETTERS.index(knight_pos[0]) < len(LETTERS)-1:
        #RIGHTUP
        rightups.append(self.add_move(next((tile for tile in self.game.tiles if tile.pos == f"{LETTERS[LETTERS.index(knight_pos[0])+1]}{int(knight_pos[1])-2}"), None)))
        #RIGHTDOWN
        rightdowns.append(self.add_move(next((tile for tile in self.game.tiles if tile.pos == f"{LETTERS[LETTERS.index(knight_pos[0])+1]}{int(knight_pos[1])+2}"), None)))
        if LETTERS.index(knight_pos[0]) < len(LETTERS)-2:
            three.append(self.add_move(next((tile for tile in self.game.tiles if tile.pos == f"{LETTERS[LETTERS.index(knight_pos[0])+2]}{int(knight_pos[1])-1}"), None)))
            four.append(self.add_move(next((tile for tile in self.game.tiles if tile.pos == f"{LETTERS[LETTERS.index(knight_pos[0])+2]}{int(knight_pos[1])+1}"), None)))
        else:
            three.append(None)
            four.append(None)
    else:
        rightups.append(None)
        rightdowns.append(None)
    leftups = [i for i in leftups if i]
    leftdowns = [i for i in leftdowns if i]
    rightups = [i for i in rightups if i]
    rightdowns = [i for i in rightdowns if i]
    one  = [i for i in one if i]
    two = [i for i in two if i ]
    three  = [i for i in three if i]
    four = [i for i in four if i ]
    leftups = sorted(leftups, key=lambda move: move[1])
    leftdowns = sorted(leftdowns, key=lambda move: move[1])
    rightups = sorted(rightups, key=lambda move: move[1])
    rightdowns = sorted(rightdowns, key=lambda move: move[1])
    one = sorted(one, key=lambda move: move[1])
    two = sorted(two, key= lambda move: move[1])
    three = sorted(three, key=lambda move: move[1])
    four = sorted(four, key= lambda move: move[1])
    result = self.get_real_moves(one) + self.get_real_moves(two)+self.get_real_moves(three) + self.get_real_moves(four) + self.get_real_moves(leftups) + self.get_real_moves(leftdowns) + self.get_real_moves(rightups) + self.get_real_moves(rightdowns)
    return result

def get_king_moves(self):
    king_pos = self.pos
    moves = []
    if LETTERS.index(king_pos[0]) > 1:
        moves.append(self.add_move(next((tile for tile in self.game.tiles if tile.pos == f"{LETTERS[LETTERS.index(king_pos[0])-1]}{int(king_pos[1])}"), None)))
        if int(king_pos[1]) > 0:
            moves.append(self.add_move(next((tile for tile in self.game.tiles if tile.pos == f"{LETTERS[LETTERS.index(king_pos[0])]}{int(king_pos[1])-1}"), None)))
            moves.append(self.add_move(next((tile for tile in self.game.tiles if tile.pos == f"{LETTERS[LETTERS.index(king_pos[0])-1]}{int(king_pos[1])-1}"), None)))
    if LETTERS.index(king_pos[0]) < len(LETTERS)-1 and LETTERS.index(king_pos[0]) > 1:
        moves.append(self.add_move(next((tile for tile in self.game.tiles if tile.pos == f"{LETTERS[LETTERS.index(king_pos[0])+1]}{int(king_pos[1])}"), None)))
        if int(king_pos[1]) < len(LETTERS) -1:
            moves.append(self.add_move(next((tile for tile in self.game.tiles if tile.pos == f"{LETTERS[LETTERS.index(king_pos[0])]}{int(king_pos[1])+1}"), None)))
            moves.append(self.add_move(next((tile for tile in self.game.tiles if tile.pos == f"{LETTERS[LETTERS.index(king_pos[0])-1]}{int(king_pos[1])+1}"), None)))
            moves.append(self.add_move(next((tile for tile in self.game.tiles if tile.pos == f"{LETTERS[LETTERS.index(king_pos[0])+1]}{int(king_pos[1])+1}"), None)))
            moves.append(self.add_move(next((tile for tile in self.game.tiles if tile.pos == f"{LETTERS[LETTERS.index(king_pos[0])+1]}{int(king_pos[1])-1}"), None)))
    moves = [i for i in moves if i ]
    moves = sorted(moves, key= lambda move: move[1])
    result = []
    for move in moves:
        if len(move) > 2:
            if self.color == BLACK:
                if move[:-1] in [piece.pos for piece in self.game.wpieces]:
                    result.append(move[:-1])
            else:
                if move[:-1] in [piece.pos for piece in self.game.bpieces]:
                    result.append(move[:-1])
        else:
            result.append(move)
    return result

def get_queen_moves(self):
    result = []
    result += get_bishop_moves(self)
    result += get_rook_moves(self)
    return result