import pytest
from board import Board
from piece import (
    Piece, Pawn, Bishop, Knight,
    Rook, Queen, King)

from PIL import Image


@pytest.fixture
def board():
    board = Board()
    return board


def test_board_has_8_files_and_8_ranks(board):
    assert len(board.squares) == 8
    for rank in board.squares:
        assert len(rank) == 8


def test_board_initializes_with_correct_colors_and_locations(board):
    piece_location_dict = {
        'black': {Pawn: [(0, 6), (1, 6), (2, 6), (3, 6),
                         (4, 6), (5, 6), (6, 6), (7, 6)],
                  Bishop: [(2, 7), (5, 7)],
                  Knight: [(1, 7), (6, 7)],
                  Rook: [(0, 7), (7, 7)],
                  Queen: [(3, 7)],
                  King: [(4, 7)]},
        'white': {Pawn: [(0, 1), (1, 1), (2, 1), (3, 1),
                         (4, 1), (5, 1), (6, 1), (7, 1)],
                  Bishop: [(2, 0), (5, 0)],
                  Knight: [(1, 0), (6, 0)],
                  Rook: [(0, 0), (7, 0)],
                  Queen: [(3, 0)],
                  King: [(4, 0)]}
    }

    for color, piece_locations in piece_location_dict.items():
        for piece_type, locations in piece_locations.items():
            color_piece_locations = [
                piece.location for piece in
                board.pieces if isinstance(piece, piece_type)
            ]
            for location in locations:
                assert location in color_piece_locations


def test_board_initializes_with_squares_holding_correct_pieces(board):
    for piece in board.pieces:
        file = piece.get_file()
        rank = piece.get_rank()
        assert board.squares[rank][file] == piece


def test_board_initializes_pieces_with_correct_image_names(board):
    for piece in board.pieces:
        image_name = piece.color.lower()+"_"+type(piece).__name__.lower()+".png"
        assert piece.image == image_name


def test_board_initializes_pieces_with_accessible_image_files(board):
    for piece in board.pieces:
        png_path = "images/{}".format(piece.image)
        img = Image.open(png_path)
