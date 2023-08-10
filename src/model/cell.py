class Cell:
    def __init__(self, piece=None):
        self.piece = piece

    def is_empty(self):
        return self.piece is None

    def set_piece(self, piece):
        self.piece = piece

    def get_piece(self):
        return self.piece

    def __str__(self):
        if self.is_empty():
            return ""
        return str(self.piece)
