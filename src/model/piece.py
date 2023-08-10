from model.assets import PIECES_IMGS
import os

class Piece:
    piece_type = "base" 
    def __init__(self, color):
        self.color = color
        self.img_path = self.get_image_path_and_obj()

    def get_image_path_and_obj(self):
        if self.piece_type in PIECES_IMGS and self.color in PIECES_IMGS[self.piece_type]:
            BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
            IMG_PATH = os.path.join(BASE_DIR, 'assets', 'pieces', f'{self.piece_type}_{self.color}.png')
            return IMG_PATH
        else:
            raise ValueError(f"Invalid piece type or color: {self.piece_type}, {self.color}")

    def __repr__(self):
        return self.piece_type

    
class Pawn(Piece):
    piece_type = "pawn"
    def __init__(self, color):
        super().__init__(color)
        self.has_moved = False

    def get_valid_moves(self, row, col):
        moves = []
        # White pawn's movement
        if self.color == "white":
            # The standard one-move forward
            if row > 0:  # Ensure it's not on the top edge of the board
                moves.append((row-1, col))
            # The two-move forward on its first move
            if row == 6 and not self.has_moved:  # It's the white pawn's first move
                moves.append((row-2, col))
        # For black pawn (assuming it moves downward)
        elif  self.color == "dark":
            if row < 7:
                moves.append((row+1, col))
            if row == 1 and not self.has_moved:
                moves.append((row+2, col))
        return moves

class Rook(Piece):
    piece_type = "rook"

class Knight(Piece):
    piece_type = "knight"

class Bishop(Piece):
    piece_type = "bishop"

class Queen(Piece):
    piece_type = "queen"

class King(Piece):
    piece_type = "king"


 