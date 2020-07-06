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
    x = piece_location[0]
    y = piece_location[1]
    piece = handler.board.squares[x][y]

    assert not piece.is_selected
    assert piece.is_hovered

    handler.select(x, y)
    assert piece.is_selected
    assert not piece.is_hovered


def test_turnhandler_correctly_deselects_selected_piece(handler):
    piece_location = (0, 0)
    x = piece_location[0]
    y = piece_location[1]
    piece = handler.board.squares[x][y]

    handler.select(x, y)
    assert piece.is_selected
    assert not piece.is_hovered

    handler.deselect(x, y)
    assert not piece.is_selected
    assert piece.is_hovered


def test_turnhandler_selects_nothing_in_blank_square(handler):
    piece_location = (2, 2)  # no piece here at start of game
    x = piece_location[0]
    y = piece_location[1]
    piece = handler.board.squares[x][y]
    assert not isinstance(piece, Piece)

    handler.select(x, y)
    assert not isinstance(piece, Piece)


def test_turnhandler_hovers_right_piece_on_right_key_input_from_left_wall(handler):
    starting_piece_location = (0, 0)
    startx = starting_piece_location[0]
    starty = starting_piece_location[1]
    starting_piece = handler.board.squares[startx][starty]

    assert starting_piece.is_hovered

    right_piece_location = (1, 0)
    rightx = right_piece_location[0]
    righty = right_piece_location[1]
    right_piece = handler.board.squares[rightx][righty]

    assert not right_piece.is_hovered

    handler.process_input(ic.RIGHT_KEY, starting_piece_location)

    assert not starting_piece.is_hovered
    assert right_piece.is_hovered


def test_turnhandler_does_nothing_on_right_key_input_from_right_wall(handler):
    starting_piece_location = (7, 0)
    startx = starting_piece_location[0]
    starty = starting_piece_location[1]
    starting_piece = handler.board.squares[startx][starty]
    starting_piece.is_hovered = True

    assert starting_piece.is_hovered

    handler.process_input(ic.RIGHT_KEY, starting_piece_location)

    assert starting_piece.is_hovered


def test_turnhandler_hovers_left_piece_on_left_key_input_from_right_wall(handler):
    starting_piece_location = (7, 0)
    startx = starting_piece_location[0]
    starty = starting_piece_location[1]
    starting_piece = handler.board.squares[startx][starty]
    starting_piece.is_hovered = True

    assert starting_piece.is_hovered

    left_piece_location = (6, 0)
    leftx = left_piece_location[0]
    lefty = left_piece_location[1]
    left_piece = handler.board.squares[leftx][lefty]

    assert not left_piece.is_hovered

    handler.process_input(ic.LEFT_KEY, starting_piece_location)

    assert not starting_piece.is_hovered
    assert left_piece.is_hovered


def test_turnhandler_does_nothing_on_left_key_input_from_left_wall(handler):
    starting_piece_location = (0, 6)
    startx = starting_piece_location[0]
    starty = starting_piece_location[1]
    starting_piece = handler.board.squares[startx][starty]
    starting_piece.is_hovered = True

    assert starting_piece.is_hovered

    handler.process_input(ic.LEFT_KEY, starting_piece_location)

    assert starting_piece.is_hovered


def test_turnhandler_hovers_up_piece_on_up_key_input_from_bottom_wall(handler):
    starting_piece_location = (5, 0)
    startx = starting_piece_location[0]
    starty = starting_piece_location[1]
    starting_piece = handler.board.squares[startx][starty]
    starting_piece.is_hovered = True

    assert starting_piece.is_hovered

    up_piece_location = (5, 1)
    upx = up_piece_location[0]
    upy = up_piece_location[1]
    up_piece = handler.board.squares[upx][upy]

    assert not up_piece.is_hovered

    handler.process_input(ic.UP_KEY, starting_piece_location)

    assert not starting_piece.is_hovered
    assert up_piece.is_hovered


def test_turnhandler_does_nothing_on_up_key_input_from_top_wall(handler):
    starting_piece_location = (5, 7)
    startx = starting_piece_location[0]
    starty = starting_piece_location[1]
    starting_piece = handler.board.squares[startx][starty]
    starting_piece.is_hovered = True

    assert starting_piece.is_hovered

    handler.process_input(ic.UP_KEY, starting_piece_location)

    assert starting_piece.is_hovered


def test_turnhandler_hovers_down_piece_on_down_key_input_from_top_wall(handler):
    starting_piece_location = (3, 7)
    startx = starting_piece_location[0]
    starty = starting_piece_location[1]
    starting_piece = handler.board.squares[startx][starty]
    starting_piece.is_hovered = True

    assert starting_piece.is_hovered

    down_piece_location = (3, 6)
    downx = down_piece_location[0]
    downy = down_piece_location[1]
    down_piece = handler.board.squares[downx][downy]

    assert not down_piece.is_hovered

    handler.process_input(ic.DOWN_KEY, starting_piece_location)

    assert not starting_piece.is_hovered
    assert down_piece.is_hovered


def test_turnhandler_does_nothing_on_down_key_input_from_bottom_wall(handler):
    starting_piece_location = (2, 0)
    startx = starting_piece_location[0]
    starty = starting_piece_location[1]
    starting_piece = handler.board.squares[startx][starty]
    starting_piece.is_hovered = True

    assert starting_piece.is_hovered

    handler.process_input(ic.DOWN_KEY, starting_piece_location)

    assert starting_piece.is_hovered
