from chess.piece import (
    Piece, Pawn, Bishop, Knight,
    Rook, Queen, King)


class Board():

    def __init__(self):
        self.squares = [[[]] * 8] * 8
        self.pieces = []

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
                location = (0, 0)
                for num in range(count):
                    piece = piece_type(location, color)
                    self.pieces.append(piece)
