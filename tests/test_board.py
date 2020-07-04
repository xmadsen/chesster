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


def test_board_initializes_with_correct_piece_counts():
    board = Board()

    piece_count_dict = {
        Pawn: 16,
        Bishop: 4,
        Knight: 4,
        Rook: 4,
        Queen: 2,
        King: 2
    }

    for piece_type, count in piece_count_dict.items():
        assert len(
            [piece for piece in board.pieces if
             isinstance(piece, piece_type)]) == count


def test_board_initializes_with_correct_piece_counts_for_each_color():
    board = Board()

    piece_count_dict = {
        Pawn: 8,
        Bishop: 2,
        Knight: 2,
        Rook: 2,
        Queen: 1,
        King: 1
    }

    for color in ['black', 'white']:
        for piece_type, count in piece_count_dict.items():
            assert len(
                [piece for piece in board.pieces if
                 isinstance(piece, piece_type)
                 and piece.color == color]) == count


# def test_board_initializes_with_all_pieces_in_correct_locations():
#     piece_location_dict = {

#     }
