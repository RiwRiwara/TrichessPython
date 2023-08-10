import tkinter as tk

LIGHT_COLOR = "#ADD8E6"
DARK_COLOR = "#6495ED"
SQUARE_SIZE = 50

class GameWindow:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Tri-Chess Game")
        self.canvas = tk.Canvas(self.root, width=400, height=400, bg="white")
        self.canvas.pack()

    def draw_board(self, board_state):
        color = LIGHT_COLOR 
        for row in range(8):
            color = DARK_COLOR if color == LIGHT_COLOR else LIGHT_COLOR 
            for col in range(8):
                x1, y1 = col * SQUARE_SIZE, row * SQUARE_SIZE
                x2, y2 = x1 + SQUARE_SIZE, y1 + SQUARE_SIZE
                self.canvas.create_rectangle(x1, y1, x2, y2, fill=color)
                
                piece = board_state[row][col]
                if piece:
                    self.canvas.create_text((x1 + x2) / 2, (y1 + y2) / 2, text=str(piece))

                color = DARK_COLOR if color == LIGHT_COLOR else LIGHT_COLOR  


    def run(self, controller):
        self.draw_board(controller.board.get_board())
        self.root.mainloop()


    def update_display(self, board_state):
        self.draw_board(board_state)
