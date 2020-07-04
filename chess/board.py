from chess.piece import (
    Piece, Pawn, Bishop, Knight,
    Rook, Queen, King)


class Board():

    def __init__(self):
        self.squares = [[[]] * 8] * 8
        self.pieces = []

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
                for location in locations:
                    piece = piece_type(location, color)
                    self.pieces.append(piece)
