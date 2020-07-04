import pytest
from chess.board import Board
from chess.piece import (
    Piece, Pawn, Bishop, Knight,
    Rook, Queen, King)


def test_board_has_8_files_and_8_ranks():
    board = Board()
    assert len(board.squares) == 8
    for rank in board.squares:
        assert len(rank) == 8


def test_board_initializes_with_correct_colors_and_locations():
    board = Board()
    piece_location_dict = {
        'black': {Pawn: [(0, 6), (1, 6), (2, 6), (3, 6),
                         (4, 6), (5, 6), (6, 6), (7, 6)],
                  Bishop: [(7, 3), (7, 5)],
                  Knight: [(7, 2), (7, 6)],
                  Rook: [(0, 7), (7, 7)],
                  Queen: [(7, 3)],
                  King: [(7, 4)]},
        'white': {Pawn: [(0, 1), (1, 1), (2, 1), (3, 1),
                         (4, 1), (5, 1), (6, 1), (7, 1), ],
                  Bishop: [(0, 3), (0, 5)],
                  Knight: [(0, 2), (0, 6)],
                  Rook: [(0, 0), (7, 0)],
                  Queen: [(0, 3)],
                  King: [(0, 4)]}
    }

    for color, piece_locations in piece_location_dict.items():
        for piece_type, locations in piece_locations.items():
            color_piece_locations = [
                piece.location for piece in
                board.pieces if isinstance(piece, piece_type)
            ]
            for location in locations:
                assert location in color_piece_locations
