from ui import UserInterface
from cli import CliRenderer

from board import Board


class Game():

    def __init__(self):
        self.board = Board()
        self.cli = CliRenderer(self.board)
