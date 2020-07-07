import pytest
from turnhandler import TurnHandler
from board import Board
from piece import Piece
from constants import InputConstants as ic


@pytest.fixture
def board():
    board = Board()
    return board


@pytest.fixture
def handler(board):
    handler = TurnHandler(board)
    return handler


def test_turnhandler_correctly_selects_piece_in_starting_hover_position(handler):
    piece_location = (0, 0)
    piece = handler.board.get_piece_at_location(piece_location)

    assert not piece.is_selected
    assert piece.is_hovered

    handler.select(piece_location)
    assert piece.is_selected
    assert not piece.is_hovered


def test_turnhandler_correctly_deselects_selected_piece(handler):
    piece_location = (0, 0)
    piece = handler.board.get_piece_at_location(piece_location)

    handler.select(piece_location)
    assert piece.is_selected
    assert not piece.is_hovered

    handler.deselect(piece_location)
    assert not piece.is_selected
    assert piece.is_hovered


def test_turnhandler_selects_nothing_in_blank_square(handler):
    piece_location = (2, 2)  # no piece here at start of game
    piece = handler.board.get_piece_at_location(piece_location)

    assert not isinstance(piece, Piece)

    handler.select(piece_location)
    assert not isinstance(piece, Piece)


def test_turnhandler_hovers_right_piece_on_right_key_input_from_left_wall(handler):
    starting_piece_location = (0, 0)
    starting_piece = handler.board.get_piece_at_location(
        starting_piece_location)

    assert starting_piece.is_hovered

    right_piece_location = (1, 0)
    right_piece = handler.board.get_piece_at_location(right_piece_location)

    assert not right_piece.is_hovered

    handler.process_input(ic.RIGHT_KEY)

    assert not starting_piece.is_hovered
    assert right_piece.is_hovered


def test_turnhandler_does_nothing_on_right_key_input_from_right_wall(handler):
    starting_piece_location = (7, 0)
    starting_piece = handler.board.get_piece_at_location(
        starting_piece_location)
    starting_piece.is_hovered = True

    assert starting_piece.is_hovered

    handler.process_input(ic.RIGHT_KEY)

    assert starting_piece.is_hovered


def test_turnhandler_hovers_left_piece_on_left_key_input_from_right_wall(handler):
    starting_piece_location = (7, 0)
    starting_piece = handler.board.get_piece_at_location(
        starting_piece_location)
    starting_piece.is_hovered = True

    assert starting_piece.is_hovered

    left_piece_location = (6, 0)
    left_piece = handler.board.get_piece_at_location(left_piece_location)

    assert not left_piece.is_hovered

    handler.location = starting_piece_location
    handler.process_input(ic.LEFT_KEY)

    assert not starting_piece.is_hovered
    assert left_piece.is_hovered


def test_turnhandler_does_nothing_on_left_key_input_from_left_wall(handler):
    starting_piece_location = (0, 6)
    starting_piece = handler.board.get_piece_at_location(
        starting_piece_location)
    starting_piece.is_hovered = True

    assert starting_piece.is_hovered

    handler.location = starting_piece_location
    handler.process_input(ic.LEFT_KEY)

    assert starting_piece.is_hovered


def test_turnhandler_hovers_up_piece_on_up_key_input_from_bottom_wall(handler):
    starting_piece_location = (5, 0)
    starting_piece = handler.board.get_piece_at_location(
        starting_piece_location)
    starting_piece.is_hovered = True

    assert starting_piece.is_hovered

    up_piece_location = (5, 1)
    up_piece = handler.board.get_piece_at_location(up_piece_location)

    assert not up_piece.is_hovered

    handler.location = starting_piece_location
    handler.process_input(ic.UP_KEY)

    assert not starting_piece.is_hovered
    assert up_piece.is_hovered


def test_turnhandler_does_nothing_on_up_key_input_from_top_wall(handler):
    starting_piece_location = (5, 7)
    starting_piece = handler.board.get_piece_at_location(
        starting_piece_location)
    starting_piece.is_hovered = True

    assert starting_piece.is_hovered

    handler.location = starting_piece_location
    handler.process_input(ic.UP_KEY)

    assert starting_piece.is_hovered


def test_turnhandler_hovers_down_piece_on_down_key_input_from_top_wall(handler):
    starting_piece_location = (3, 7)
    starting_piece = handler.board.get_piece_at_location(
        starting_piece_location)
    starting_piece.is_hovered = True

    assert starting_piece.is_hovered

    down_piece_location = (3, 6)
    down_piece = handler.board.get_piece_at_location(down_piece_location)

    assert not down_piece.is_hovered

    handler.location = starting_piece_location
    handler.process_input(ic.DOWN_KEY)

    assert not starting_piece.is_hovered
    assert down_piece.is_hovered


def test_turnhandler_does_nothing_on_down_key_input_from_bottom_wall(handler):
    starting_piece_location = (2, 0)
    starting_piece = handler.board.get_piece_at_location(
        starting_piece_location)
    starting_piece.is_hovered = True

    assert starting_piece.is_hovered

    handler.location = starting_piece_location
    handler.process_input(ic.DOWN_KEY)

    assert starting_piece.is_hovered
