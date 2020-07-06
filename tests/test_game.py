import pytest
from game import Game
from board import Board
from cli import CliRenderer
from constants import PlayerConstants as pc


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
    assert len(game.players) == 2


def test_game_starts_with_black_player_and_white_player(game):
    player_names = [pc.BLACK_PLAYER, pc.WHITE_PLAYER]
    for player_name in player_names:
        assert player_name in [player.name for player in game.players]


def test_game_has_white_player_first(game):
    assert game.players[0].name == pc.WHITE_PLAYER
