from model.piece import Pawn, Rook, Knight, Bishop, Queen, King
from model.cell import Cell

from model.piece import Pawn, Rook, Knight, Bishop, Queen, King

class Board:
    def __init__(self):
        self._board = self.initialize_board()

    def initialize_board(self):
        board = [[Cell() for _ in range(8)] for _ in range(8)]
        for col in range(8):
            board[1][col].set_piece(Pawn('white'))
            board[6][col].set_piece(Pawn('dark'))
        piece_types = [Rook, Knight, Bishop, Queen, King, Bishop, Knight, Rook]
        for i, piece_type in enumerate(piece_types):
            board[0][i].set_piece(piece_type('white'))
            board[7][i].set_piece(piece_type('dark'))
        return board

    def get_cell(self, row, col):
        return self._board[row][col]

    def set_piece(self, row, col, piece):
        self._board[row][col].set_piece(piece)

    def make_move(self, move):
        pass
    def get_board(self):
        return self._board