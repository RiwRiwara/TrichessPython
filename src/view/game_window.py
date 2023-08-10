import tkinter as tk
from functools import partial

LIGHT_COLOR = "#ADD8E6"
DARK_COLOR = "#6495ED"
MOVE_GREEN = "#94FA92"
CAPTURE_RED = "#FA8072"
SELECTED_COLOR = "#FDFD97"

SQUARE_SIZE = 100

class GameWindow:
    def __init__(self):
        self.controller = None
        self.images = []
        self.rects = [[None for _ in range(8)] for _ in range(8)]  
        self.root = tk.Tk()
        self.root.title("Tri-Chess Game")
        self.canvas = tk.Canvas(self.root, width=800, height=800, bg="white")
        self.canvas.pack()
        self._tooltip = None

    def draw_board(self, board_state):
        for row in range(8):
            for col in range(8):
                x1, y1 = col * SQUARE_SIZE, row * SQUARE_SIZE
                x2, y2 = x1 + SQUARE_SIZE, y1 + SQUARE_SIZE
                color = LIGHT_COLOR if (row + col) % 2 == 0 else DARK_COLOR
                rect = self.canvas.create_rectangle(x1, y1, x2, y2, fill=color)
                self.rects[row][col] = rect  # Store the rectangle ID
                
                self.canvas.tag_bind(rect, "<Enter>", partial(self.show_tooltip, row, col))
                self.canvas.tag_bind(rect, "<Leave>", self.hide_tooltip)

                cell = board_state[row][col]
                if not cell.is_empty():
                    self.draw_piece(row, col, cell.get_piece())


    def show_tooltip(self, row, col, event):
        if self._tooltip:
            self._tooltip.destroy()
        x, y, _, _ = self.canvas.bbox("current")
        tooltip_text = f"Cell: ({row},{col})"  
        self._tooltip = tk.Toplevel(self.root)
        self._tooltip.wm_overrideredirect(True)
        self._tooltip.geometry(f"+{x + self.root.winfo_x()}+{y + self.root.winfo_y()}")
        label = tk.Label(self._tooltip, text=tooltip_text, bg="yellow", padx=10, pady=5)
        label.pack()

    def hide_tooltip(self, event):
        if self._tooltip:
            self._tooltip.destroy()
            self._tooltip = None

    def draw_piece(self, row, col, piece):
        img_path = piece.img_path
        piece_img = tk.PhotoImage(file=img_path)
        self.images.append(piece_img)

        tag = f"piece-{row}-{col}"

        x = (col * SQUARE_SIZE) + (SQUARE_SIZE / 2)
        y = (row * SQUARE_SIZE) + (SQUARE_SIZE / 2)

        image_id = self.canvas.create_image(x, y, image=piece_img, tags=tag)

        # Function to bind to the click event
        on_piece_selected = partial(self.controller.on_piece_selected,piece=piece, row=row, col=col)
        self.canvas.tag_bind(tag, "<ButtonPress-1>", on_piece_selected)

        # Also bind the image to the tooltip
        self.canvas.tag_bind(image_id, "<Enter>", partial(self.show_tooltip, row, col))
        self.canvas.tag_bind(image_id, "<Leave>", self.hide_tooltip)

        self.canvas.image = piece_img


    def update_cell_color(self, row, col, MOVE_LIST):
        rect_id = self.rects[row][col]
        MOVE_LIST_ID = [self.rects[row][col] for row, col in MOVE_LIST]
        for i in MOVE_LIST_ID:
            self.canvas.itemconfig(i, fill=MOVE_GREEN)
        self.canvas.itemconfig(rect_id, fill=SELECTED_COLOR)
        

    def update_display(self, board_state):
        self.draw_board(board_state)

    def run(self, controller):
        self.controller = controller
        self.draw_board(controller.board.get_board()) 
        self.root.mainloop()

        