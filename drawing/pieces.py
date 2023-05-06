import pygame
from config import *

black_pieces = ['P', 'B', 'N', 'R', 'K', 'Q']

white_pieces = ['p', 'b', 'n', 'r', 'k', 'q']

def invalid_position(pos):
    if pos[0] < 0 or pos[0] > 7:
        return True
    if pos[1] < 0 or pos[1] > 7:
        return True
    return False

class Pieces:
    
    def draw(self, screen, x, y):
        image = pygame.image.load(self.image_link)
        screen.blit(image, (x * chess_pieces, y * chess_pieces))
    
    def check_blank(self, x):
        return x == ' '
    
    def vertical(self, board, old_pos, new_pos):
        if old_pos[0] != new_pos[0]:
            return False
        for i in range(1, 8):
            if old_pos[1] + i == new_pos[1]:
                return True
            if invalid_position((old_pos[0], old_pos[1] + i)):
                continue
            if not self.check_blank(board[old_pos[0]][old_pos[1] + i]):
                break

        for i in range(1, 8):
            if old_pos[1] - i == new_pos[1]:
                return True
            if invalid_position((old_pos[0], old_pos[1] - i)):
                continue
            if not self.check_blank(board[old_pos[0]][old_pos[1] - i]):
                break
        return False
    
    def horizontal(self, board, old_pos, new_pos):
        if old_pos[1] != new_pos[1]:
            return False
        for i in range(1, 8):
            if old_pos[0] + i == new_pos[0]:
                return True
            if invalid_position((old_pos[0] + i, old_pos[1])):
                break
            if not self.check_blank(board[old_pos[0] + i][old_pos[1]]):
                break

        for i in range(1, 8):
            if old_pos[0] - i == new_pos[0]:
                return True
            if invalid_position((old_pos[0] - i, old_pos[1])):
                break
            if not self.check_blank(board[old_pos[0] - i][old_pos[1]]):
                break
    
    def diagonal(self, board, old_pos, new_pos):
        for i in range(1, 8):
            if old_pos[0] + i == new_pos[0] and old_pos[1] + i == new_pos[1]:
                return True
            if invalid_position((old_pos[0] + i, old_pos[1] + i)):
                break
            if not self.check_blank(board[old_pos[0] + i][old_pos[1] + i]):
                break
        
        for i in range(1, 8):
            if old_pos[0] - i == new_pos[0] and old_pos[1] - i == new_pos[1]:
                return True
            if invalid_position((old_pos[0] - i, old_pos[1] - i)):
                break
            if not self.check_blank(board[old_pos[0] - i][old_pos[1] - i]):
                break
        
        for i in range(1, 8):
            if old_pos[0] + i == new_pos[0] and old_pos[1] - i == new_pos[1]:
                return True
            if invalid_position((old_pos[0] + i, old_pos[1] - i)):
                break
            if not self.check_blank(board[old_pos[0] + i][old_pos[1] - i]):
                break
        
        for i in range(1, 8):
            if old_pos[0] - i == new_pos[0] and old_pos[1] + i == new_pos[1]:
                return True
            if invalid_position((old_pos[0] - i, old_pos[1] + i)):
                break
            if not self.check_blank(board[old_pos[0] - i][old_pos[1] + i]):
                break
        
        return False

    def vertical_moves(self, board, pos):
        moves = []
        for i in range(1, 8):
            if invalid_position((pos[0], pos[1] + i)):
                break
            if self.check_blank(board[pos[0]][pos[1] + i]):
                moves.append((pos, (pos[0], pos[1] + i)))
            else:
                if board[pos[0]][pos[1] + i] in self.anti_color:
                    moves.append((pos, (pos[0], pos[1] + i)))
                break
        for i in range(1, 8):
            if invalid_position((pos[0], pos[1] - i)):
                break
            if not self.check_blank(board[pos[0]][pos[1] - i]):
                if board[pos[0]][pos[1] - i] in self.anti_color:
                    moves.append((pos, (pos[0], pos[1] - i)))
                break
            moves.append((pos, (pos[0], pos[1] - i)))
        return moves

    def horizontal_moves(self, board, pos):
        moves = []
        for i in range(1, 8):
            if invalid_position((pos[0] + i, pos[1])):
                break
            if self.check_blank(board[pos[0] + i][pos[1]]):
                moves.append((pos, (pos[0] + i, pos[1])))
            else:
                if board[pos[0] + i][pos[1]] in self.anti_color:
                    moves.append((pos, (pos[0] + i, pos[1])))
                break
        for i in range(1, 8):
            if invalid_position((pos[0] - i, pos[1])):
                break
            if not self.check_blank(board[pos[0] - i][pos[1]]):
                if board[pos[0] - i][pos[1]] in self.anti_color:
                    moves.append((pos, (pos[0] - i, pos[1])))
                break
            moves.append((pos, (pos[0] - i, pos[1])))
        return moves

    def diagonal_moves(self, board, pos):
        moves = []
        for i in range(1, 8):
            if invalid_position((pos[0] + i, pos[1] + i)):
                break
            if self.check_blank(board[pos[0] + i][pos[1] + i]):
                moves.append((pos, (pos[0] + i, pos[1] + i)))
            else:
                if board[pos[0] + i][pos[1] + i] in self.anti_color:
                    moves.append((pos, (pos[0] + i, pos[1] + i)))
                break
        for i in range(1, 8):
            if invalid_position((pos[0] - i, pos[1] - i)):
                break
            if not self.check_blank(board[pos[0] - i][pos[1] - i]):
                if board[pos[0] - i][pos[1] - i] in self.anti_color:
                    moves.append((pos, (pos[0] - i, pos[1] - i)))
                break
            moves.append((pos, (pos[0] - i, pos[1] - i)))
        for i in range(1, 8):
            if invalid_position((pos[0] + i, pos[1] - i)):
                break
            if self.check_blank(board[pos[0] + i][pos[1] - i]):
                moves.append((pos, (pos[0] + i, pos[1] - i)))
            else:
                if board[pos[0] + i][pos[1] - i] in self.anti_color:
                    moves.append((pos, (pos[0] + i, pos[1] - i)))
                break
        for i in range(1, 8):
            if invalid_position((pos[0] - i, pos[1] + i)):
                break
            if not self.check_blank(board[pos[0] - i][pos[1] + i]):
                if board[pos[0] - i][pos[1] + i] in self.anti_color:
                    moves.append((pos, (pos[0] - i, pos[1] + i)))
                break
            moves.append((pos, (pos[0] - i, pos[1] + i)))
        return moves

class Pawn(Pieces):

    def taking_piece(self, board, old_pos, new_pos):
        if invalid_position(new_pos):
            return False
        if old_pos[1] != new_pos[1] - self.direction:
            return False
        if abs(old_pos[0] - new_pos[0]) != 1:
            return False
        if board[new_pos[0]][new_pos[1]] in self.anti_color:
            return True
        return False

    def first_move(self, board, old_pos, new_pos):
        if invalid_position(new_pos):
            return False
        if old_pos[1] == new_pos[1] - 2 * self.direction and old_pos[0] == new_pos[0]:
            if old_pos[1] != self.first_place:
                return False
            if board[new_pos[0]][new_pos[1] - self.direction] != ' ' or board[new_pos[0]][new_pos[1]] != ' ':
                # print('boo')
                return False
            return True
        return False

    def regular_move(self, board, old_pos, new_pos):
        if invalid_position(new_pos):
            return False
        if old_pos[1] != new_pos[1] - self.direction:
            return False
        if abs(old_pos[0] - new_pos[0]) != 0:
            return False
        if board[new_pos[0]][new_pos[1]] != ' ':
            return False
        return True

    def is_valid(self, board, old_pos, new_pos):
        if board[new_pos[0]][new_pos[1]] in self.color:
            return False
        if self.taking_piece(board, old_pos, new_pos):
            return True
        if self.first_move(board, old_pos, new_pos):
            return True
        if self.regular_move(board, old_pos, new_pos):
            return True
        return False

    def available_moves(self, board, pos):
        moves = []
        if self.first_move(board, pos, (pos[0], pos[1] + 2 * self.direction)):
            moves.append(((pos), (pos[0], pos[1] + 2 * self.direction)))
        if self.regular_move(board, pos, (pos[0], pos[1] + self.direction)):
            moves.append(((pos), (pos[0], pos[1] + self.direction)))
        if self.taking_piece(board, pos, (pos[0] + self.direction, pos[1] + self.direction)):
            moves.append(((pos), (pos[0] + self.direction, pos[1] + self.direction)))
        if self.taking_piece(board, pos, (pos[0] + self.direction, pos[1] - self.direction)):
            moves.append(((pos), (pos[0] + self.direction, pos[1] - self.direction)))
        return moves

class Rook(Pieces):

    def is_valid(self, board, old_pos, new_pos):
        if board[new_pos[0]][new_pos[1]] in self.color:
            return False
        if old_pos[0] != new_pos[0] and old_pos[1] != new_pos[1]:
            return False
        if old_pos[0] == new_pos[0] and old_pos[1] == new_pos[1]:
            return False
        if self.vertical(board, old_pos, new_pos):
            return True
        if self.horizontal(board, old_pos, new_pos):
            return True
        return False
    
    def available_moves(self, board, pos):
        moves = []
        moves = moves + self.vertical_moves(board, pos)
        moves = moves + self.horizontal_moves(board, pos)
        return moves

class Knight(Pieces):

    def is_valid(self, board, old_pos, new_pos):
        if invalid_position(new_pos):
            return False
        if board[new_pos[0]][new_pos[1]] in self.color:
            return False
        if new_pos[0] == old_pos[0] or new_pos[1] == old_pos[1]:
            return False
        if abs(new_pos[0] - old_pos[0]) + abs(new_pos[1] - old_pos[1]) == 3:
            return True
        return False
    
    def available_moves(self, board, pos):
        moves = []
        moves.append((pos, (pos[0] + 2, pos[1] + 1)))
        moves.append((pos, (pos[0] + 2, pos[1] - 1)))
        moves.append((pos, (pos[0] - 2, pos[1] + 1)))
        moves.append((pos, (pos[0] - 2, pos[1] - 1)))
        moves.append((pos, (pos[0] + 1, pos[1] + 2)))
        moves.append((pos, (pos[0] + 1, pos[1] - 2)))
        moves.append((pos, (pos[0] - 1, pos[1] + 2)))
        moves.append((pos, (pos[0] - 1, pos[1] - 2)))
        moves = [move for move in moves if not invalid_position(move[1]) and board[move[1][0]][move[1][1]] not in self.color]
        return moves

class Bishop(Pieces):

    def is_valid(self, board, old_pos, new_pos):
        if board[new_pos[0]][new_pos[1]] in self.color:
            return False
        if abs(old_pos[0] - new_pos[0]) != abs(old_pos[1] - new_pos[1]):
            return False
        if old_pos[0] == new_pos[0] or old_pos[1] == new_pos[1]:
            return False
        if self.diagonal(board, old_pos, new_pos):
            return True
        return False

    def available_moves(self, board, pos):
        moves = []
        moves = moves + self.diagonal_moves(board, pos)
        return moves

class Queen(Pieces):

    def is_valid(self, board, old_pos, new_pos):
        if board[new_pos[0]][new_pos[1]] in self.color:
            return False
        if self.vertical(board, old_pos, new_pos):
            return True
        if self.horizontal(board, old_pos, new_pos):
            return True
        if self.diagonal(board, old_pos, new_pos):
            return True
        return False
    
    def available_moves(self, board, pos):
        moves = []
        moves = moves + self.vertical_moves(board, pos)
        moves = moves + self.horizontal_moves(board, pos)
        moves = moves + self.diagonal_moves(board, pos)
        return moves

class white_pawn(Pawn):

    def __init__(self):
        self.image_link = 'images/white_pawn.jpg'
        self.direction = -1
        self.first_place = 6
        self.anti_color = black_pieces
        self.color = white_pieces

class black_pawn(Pawn):

    def __init__(self):
        self.image_link = 'images/black_pawn.png'
        self.direction = 1
        self.first_place = 1
        self.anti_color = white_pieces
        self.color = black_pieces

class white_rook(Rook):

    def __init__(self):

        self.image_link = 'images/white_rook.png'
        self.color = white_pieces
        self.anti_color = black_pieces

class black_rook(Rook):

    def __init__(self):

        self.image_link = 'images/black_rook.png'
        self.color = black_pieces
        self.anti_color = white_pieces

class white_knight(Knight):

    def __init__(self):

        self.image_link = 'images/white_knight.png'
        self.color = white_pieces
        self.anti_color = black_pieces

class black_knight(Knight):

    def __init__(self):

        self.image_link = 'images/black_knight.png'
        self.color = black_pieces
        self.anti_color = white_pieces

class white_bishop(Bishop):

    def __init__(self):

        self.image_link = 'images/white_bishop.png'
        self.color = white_pieces
        self.anti_color = black_pieces

class black_bishop(Bishop):

    def __init__(self):

        self.image_link = 'images/black_bishop.png'
        self.color = black_pieces
        self.anti_color = white_pieces

class white_queen(Queen):

    def __init__(self):

        self.image_link = 'images/white_queen.png'
        self.color = white_pieces
        self.anti_color = black_pieces

class black_queen(Queen):

    def __init__(self):

        self.image_link = 'images/black_queen.png'
        self.color = black_pieces
        self.anti_color = white_pieces

wp = white_pawn()
bp = black_pawn()
wr = white_rook()
br = black_rook()
wn = white_knight()
bn = black_knight()
wb = white_bishop()
bb = black_bishop()
wq = white_queen()
bq = black_queen()

class King(Pieces):

    def castled_king_side(self, board):
        if self.moved:
            return False
        if board[5][self.starting_row] == ' ' and board[6][self.starting_row] == ' ' and board[7][self.starting_row] == 'r':
            return True
        return False

    def castled_queen_side(self, board):
        if self.moved:
            return False
        if board[1][self.starting_row] == ' ' and board[2][self.starting_row] == ' ' and board[3][self.starting_row] == ' ' and board[0][self.starting_row] == 'r':
            return True
        return False

    def get_pos(self):
        return (self.x, self.y)

    def is_valid(self, board, old_pos, new_pos):
        if board[new_pos[0]][new_pos[1]] in self.color:
            return False
        if new_pos == (6, self.starting_row) and old_pos == (4, self.starting_row):
            return self.castled_king_side(board)
        if new_pos == (2, self.starting_row) and old_pos == (4, self.starting_row):
            return self.castled_queen_side(board)
        if abs(old_pos[0] - new_pos[0]) > 1 or abs(old_pos[1] - new_pos[1]) > 1:
            return False
        if old_pos[0] == new_pos[0] and old_pos[1] == new_pos[1]:
            return False
        return True
    
    def available_moves(self, board, pos):
        moves = [
            (pos, (pos[0] + 1, pos[1])),
            (pos, (pos[0] - 1, pos[1])),
            (pos, (pos[0], pos[1] + 1)),
            (pos, (pos[0], pos[1] - 1)),
            (pos, (pos[0] + 1, pos[1] + 1)),
            (pos, (pos[0] + 1, pos[1] - 1)),
            (pos, (pos[0] - 1, pos[1] + 1)),
            (pos, (pos[0] - 1, pos[1] - 1)),
            (pos, (pos[0] + 2, pos[1])),
            (pos, (pos[0] - 2, pos[1]))
        ]
        return [i for i in moves if not invalid_position(i[1]) and self.is_valid(board, pos, i[1])]

class white_king(King):

    def __init__(self):

        self.image_link = 'images/white_king.png'
        self.moved = False
        self.x = 4
        self.y = 7
        self.color = white_pieces
        self.anti_color = black_pieces
        self.starting_row = 7

class black_king(King):

    def __init__(self):

        self.image_link = 'images/black_king.png'
        self.moved = False
        self.x = 4
        self.y = 0
        self.color = black_pieces
        self.anti_color = white_pieces
        self.starting_row = 0

    # def get_pos(self):
    #     return (self.x, self.y)

    # def being_checked(self, board):
    #     for i in range(8):
    #         for j in range(8):
    #             if board[i][j] not in white_pieces:
    #                 continue
    #             if board[i][j] == 'p':
    #                 if wp.is_valid(board, (i, j), self.get_pos()):
    #                     return True
    #             elif board[i][j] == 'b':
    #                 if wb.is_valid(board, (i, j), self.get_pos()):
    #                     return True
    #             elif board[i][j] == 'r':
    #                 if wr.is_valid(board, (i, j), self.get_pos()):
    #                     return True
    #             elif board[i][j] == 'n':
    #                 if wn.is_valid(board, (i, j), self.get_pos()):
    #                     return True
    #             elif board[i][j] == 'q':
    #                 if wq.is_valid(board, (i, j), self.get_pos()):
    #                     return True
    #     return False

    # def castled_king_side(self, board):
    #     if self.moved:
    #         return False
    #     if board[5][0] == ' ' and board[6][0] == ' ' and board[7][0] == 'R':
    #         return True
    #     return False

    # def castled_queen_side(self, board):
    #     if self.moved:
    #         return False
    #     if board[1][0] == ' ' and board[2][0] == ' ' and board[3][0] == ' ' and board[0][0] == 'R':
    #         return True
    #     return False

    # def is_valid(self, board, old_pos, new_pos):
    #     if board[new_pos[0]][new_pos[1]] in black_pieces:
    #         return False
    #     if new_pos == (6, 0):
    #         return self.castled_king_side(board)
    #     if new_pos == (2, 0):
    #         return self.castled_queen_side(board)
    #     if abs(old_pos[0] - new_pos[0]) > 1 or abs(old_pos[1] - new_pos[1]) > 1:
    #         return False
    #     if old_pos[0] == new_pos[0] and old_pos[1] == new_pos[1]:
    #         return False
    #     return True

wk = white_king()
bk = black_king()