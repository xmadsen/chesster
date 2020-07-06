from piece import Piece
from constants import InputConstants as ic


class TurnHandler():
    def __init__(self, board):
        self.board = board

    def process_input(self, input_key, location):
        x = location[0]
        y = location[1]
        if input_key == ' ':
            self.select(x, y)
        if input_key == ic.RIGHT_KEY:
            if location[0] + 1 <= 7:
                self.board.squares[x][y].is_hovered = False
                self.board.squares[x + 1][y].is_hovered = True
        elif input_key == ic.LEFT_KEY:
            if location[0] - 1 >= 0:
                self.board.squares[x][y].is_hovered = False
                self.board.squares[x - 1][y].is_hovered = True
        elif input_key == ic.UP_KEY:
            if location[1] + 1 <= 7:
                self.board.squares[x][y].is_hovered = False
                self.board.squares[x][y + 1].is_hovered = True
        elif input_key == ic.DOWN_KEY:
            if location[1] - 1 >= 0:
                self.board.squares[x][y].is_hovered = False
                self.board.squares[x][y - 1].is_hovered = True

    def select(self, x, y):
        piece = self.board.squares[x][y]

        if isinstance(piece, Piece):
            piece.select()

    def deselect(self, x, y):
        piece = self.board.squares[x][y]

        if isinstance(piece, Piece):
            piece.deselect()
