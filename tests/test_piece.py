import pytest
from random import randrange, choice
from chess.piece import (
    Piece, Pawn, Bishop, Knight,
    Rook, Queen, King)


@pytest.fixture
def generic_piece():
    piece = Piece((randrange(8), randrange(8)), choice(['black', 'white']))
    return piece


def test_new_piece_starts_alive(generic_piece):
    assert generic_piece.is_alive


def test_get_file_returns_correct_value(generic_piece):
    assert generic_piece.get_file() == generic_piece.location[0]


def test_get_rank_returns_correct_value(generic_piece):
    assert generic_piece.get_rank() == generic_piece.location[1]


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
    color = choice(['black', 'white'])
    for piece, value in piece_values_dict.items():
        assert piece(location, color).point_value == value
