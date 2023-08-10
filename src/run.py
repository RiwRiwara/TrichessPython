from model.board import Board
from view.game_window import GameWindow
from controller.game_controller import GameController

if __name__ == "__main__":
    board = Board()
    view = GameWindow()
    controller = GameController(board, view)
    view.run(controller)
