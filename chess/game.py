from ui import UserInterface
from cli import CliRenderer
from constants import PlayerConstants as pc
from board import Board
from player import Player


class Game():

    def __init__(self):
        self.board = Board()
        self.cli = CliRenderer(self.board)

        black_player = Player(pc.BLACK_PLAYER)
        white_player = Player(pc.WHITE_PLAYER)
        self.players = [white_player, black_player]
