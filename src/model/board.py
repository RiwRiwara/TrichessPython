from model.piece import Pawn, Rook, Knight, Bishop, Queen, King
from model.cell import Cell


class Board:
    def __init__(self):
        self._board = self.initialize_board()

    def initialize_board(self):
        board = [[Cell() for i in range(8)] for j in range(8)]

        for col in range(8):
            board[1][col].set_piece(Pawn('dark'))
            board[6][col].set_piece(Pawn('white'))
        piece_types = [Rook, Knight, Bishop, Queen, King, Bishop, Knight, Rook]
        for i, piece_type in enumerate(piece_types):
            board[0][i].set_piece(piece_type('dark'))
            board[7][i].set_piece(piece_type('white'))
        return board

    def get_cell(self, row, col):
        return self._board[row][col]

    def set_piece(self, row, col, piece):
        self._board[row][col].set_piece(piece)
        
    def get_board(self):
        return self._board
    def move_piece(self, row_from, col_from, row_to, col_to):
        piece = self._board[row_from][col_from].get_piece()
        self._board[row_from][col_from].set_piece(None)
        self._board[row_to][col_to].set_piece(piece)