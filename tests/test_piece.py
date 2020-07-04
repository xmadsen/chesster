import pytest
from random import randrange
from chess.piece import (
    Piece, Pawn, Rook)


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


def test_pawn_has_point_value_of_1():
    location = (randrange(8), randrange(8))
    test_pawn = Pawn(location)
    assert test_pawn.point_value == 1


def test_rook_has_point_value_of_5():
    location = (randrange(8), randrange(8))
    test_rook = Rook(location)
    assert test_rook.point_value == 5
