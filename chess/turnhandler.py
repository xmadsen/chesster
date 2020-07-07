from piece import Piece
from constants import InputConstants as ic


class TurnHandler():
    def __init__(self, board):
        self.board = board
        self.location = (0, 0)

    def process_input(self, input_key):
        x = self.location[0]
        y = self.location[1]
        if input_key == ' ':
            self.select(x, y)
        if input_key == ic.RIGHT_KEY:
            if x + 1 <= 7:
                self.board.squares[x][y].is_hovered = False
                self.board.squares[x + 1][y].is_hovered = True
                self.location = (x + 1, y)
        elif input_key == ic.LEFT_KEY:
            if x - 1 >= 0:
                self.board.squares[x][y].is_hovered = False
                self.board.squares[x - 1][y].is_hovered = True
                self.location = (x - 1, y)
        elif input_key == ic.UP_KEY:
            if y + 1 <= 7:
                self.board.squares[x][y].is_hovered = False
                self.board.squares[x][y + 1].is_hovered = True
                self.location = (x, y + 1)
        elif input_key == ic.DOWN_KEY:
            if y - 1 >= 0:
                self.board.squares[x][y].is_hovered = False
                self.board.squares[x][y - 1].is_hovered = True
                self.location = (x, y - 1)

    def select(self, location):
        x = location[0]
        y = location[1]
        piece = self.board.squares[x][y]

        if isinstance(piece, Piece):
            piece.select()

    def deselect(self, location):
        x = location[0]
        y = location[1]
        piece = self.board.squares[x][y]

        if isinstance(piece, Piece):
            piece.deselect()
