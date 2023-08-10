class GameController:
    def __init__(self, board, view):
        self.board = board
        self.view = view

    def process_move(self, move):
        self.board.make_move(move)
        self.view.update_display(self.board.get_board())

    def play(self):
        while True:
            move = self.view.get_user_move()
            if move:
                self.process_move(move)
