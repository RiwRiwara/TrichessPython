import pygame
from model.assets import PIECES_IMGS
import os

class Piece:
    piece_type = "base" 

    def __init__(self, color):
        self.color = color
        pygame.init() 
        self.img_path, self.img_obj = self.get_image_path_and_obj()

    def get_image_path_and_obj(self):
        if self.piece_type in PIECES_IMGS and self.color in PIECES_IMGS[self.piece_type]:
            path = PIECES_IMGS[self.piece_type][self.color]
            BASE_DIR = os.path.dirname(os.path.abspath(__file__)) 
            IMG_PATH = os.path.join(BASE_DIR, '..', 'assets', 'pieces', 'pawn_white.png')
            img = pygame.image.load(IMG_PATH) 
            return path, img
        else:
            raise ValueError(f"Invalid piece type or color: {self.piece_type}, {self.color}")

    def get_image(self):
        return self.img_obj

    def __repr__(self):
        return self.piece_type

    
class Pawn(Piece):
    piece_type = "pawn"

    def possible_moves(self, current_row, current_col, board):
        moves = []
        if self.color == "white":
            # Move forward by one
            if board[current_row - 1][current_col].is_empty():
                moves.append((current_row - 1, current_col))
            # Capture diagonally left
            if current_col > 0 and not board[current_row - 1][current_col - 1].is_empty() and board[current_row - 1][current_col - 1].get_piece().color != self.color:
                moves.append((current_row - 1, current_col - 1))
            # Capture diagonally right
            if current_col < 7 and not board[current_row - 1][current_col + 1].is_empty() and board[current_row - 1][current_col + 1].get_piece().color != self.color:
                moves.append((current_row - 1, current_col + 1))
            # TODO: Add logic for two square moves for pawns on their starting row.
        else:
            # TODO: Implement logic for dark pawns.
            pass
        return moves


class Rook(Piece):
    def __init__(self, color):
        super().__init__(color)
    piece_type = "rook"

class Knight(Piece):
    def __init__(self, color):
        super().__init__(color)
    piece_type = "knight"

class Bishop(Piece):
    def __init__(self, color):
        super().__init__(color)
    piece_type = "bishop"

class Queen(Piece):
    def __init__(self, color):
        super().__init__(color)
    piece_type = "queen"

class King(Piece):
    def __init__(self, color):
        super().__init__(color)
    piece_type = "king"


 