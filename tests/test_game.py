import pytest
from game import Game
from board import Board
from cli import CliRenderer


@pytest.fixture
def game():
    game = Game()
    return game


def test_game_starts_with_a_board(game):
    assert hasattr(game, 'board')
    assert isinstance(game.board, Board)


def test_game_starts_with_cli(game):
    assert hasattr(game, 'cli')
    assert isinstance(game.cli, CliRenderer)


def test_game_starts_with_two_players(game):
    players = ['white_player', 'black_player']

    for player in players:
        assert hasattr(game, player)
        assert isinstance(game.player, Player)
