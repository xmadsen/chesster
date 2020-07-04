import pytest
from chess.board import Board


def test_board_has_8_files_and_8_ranks():
    board = Board()
    assert len(board.squares) == 8
    for rank in board.squares:
        assert len(rank) == 8


def test_board_initializes_with_():
    board = Board()
