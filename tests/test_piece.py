import pytest
from chess.piece import Piece


def test_new_piece_starts_alive():
    test_piece = Piece(location=(0, 0))
    assert test_piece.is_alive


def test_new_piece_has_provided_location():
    test_piece = Piece((0, 0))
    assert test_piece.location == (0, 0)


def test_get_file_returns_correct_value():
    test_piece = Piece((0, 1))
    assert test_piece.get_file() == 0


def test_get_rank_returns_correct_value():
    test_piece = Piece((0, 1))
    assert test_piece.get_rank() == 1
