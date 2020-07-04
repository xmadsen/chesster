import pytest
from random import randrange
from chess.piece import (
    Piece, Pawn, Bishop, Knight,
    Rook, Queen, King)


def test_new_piece_starts_alive():
    test_piece = Piece((0, 0))
    assert test_piece.is_alive


def test_new_piece_has_provided_location():
    location = (randrange(8), randrange(8))
    test_piece = Piece(location)
    assert test_piece.location == location


def test_get_file_returns_correct_value():
    location = (randrange(8), randrange(8))
    test_piece = Piece(location)
    assert test_piece.get_file() == location[0]


def test_get_rank_returns_correct_value():
    location = (randrange(8), randrange(8))
    test_piece = Piece(location)
    assert test_piece.get_rank() == location[1]


def test_piece_types_have_correct_point_values():
    piece_values_dict = {
        Pawn: 1,
        Bishop: 3,
        Knight: 3,
        Rook: 5,
        Queen: 9,
        King: -1
    }
    location = (randrange(8), randrange(8))
    for piece, value in piece_values_dict.items():
        assert piece(location).point_value == value
