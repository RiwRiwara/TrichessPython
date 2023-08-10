

class GameController:
    def __init__(self, board, view):
        self.board = board
        self.view = view
        self.plater_turn = 0

    def on_piece_selected(self, event, piece, row, col):
        print(f"({piece.color}, {piece}, {row}, {col})")
        MOVE_LIST = piece.get_valid_moves(row, col)

        # Update display must before udpate color
        self.view.update_display(self.board.get_board())
        self.view.update_cell_color(row, col, MOVE_LIST)

    def on_move_piece(self):
        # self.board.move_piece(row, col, row-1, col)
        pass
