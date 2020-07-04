import pytest
from chess.piece import Piece


def test_new_piece_starts_alive():
    test_piece = Piece(file='a', rank='1')
    assert test_piece.is_alive


def test_new_piece_has_provided_location():
    test_piece = Piece(file='a', rank='1')
    assert test_piece.location == ('a', '1')
