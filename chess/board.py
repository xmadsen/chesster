from chess.piece import (
    Piece, Pawn, Bishop, Knight,
    Rook, Queen, King)


class Board():

    def __init__(self):
        self.initialize_pieces()

    def initialize_pieces(self):
        self.squares = [["-"] * 8 for _ in range(8)]
        self.pieces = []
        piece_location_dict = {
            'black': {Pawn: [(0, 6), (1, 6), (2, 6), (3, 6),
                             (4, 6), (5, 6), (6, 6), (7, 6)],
                      Bishop: [(2, 7), (5, 7)],
                      Knight: [(1, 7), (6, 7)],
                      Rook: [(0, 7), (7, 7)],
                      Queen: [(3, 7)],
                      King: [(4, 7)]},
            'white': {Pawn: [(0, 1), (1, 1), (2, 1), (3, 1),
                             (4, 1), (5, 1), (6, 1), (7, 1)],
                      Bishop: [(2, 0), (5, 0)],
                      Knight: [(1, 0), (6, 0)],
                      Rook: [(0, 0), (7, 0)],
                      Queen: [(3, 0)],
                      King: [(4, 0)]}
        }

        for color, piece_locations in piece_location_dict.items():
            for piece_type, locations in piece_locations.items():
                for location in locations:
                    piece = piece_type(location, color)
                    self.pieces.append(piece)
                    file = piece.get_file()
                    rank = piece.get_rank()
                    self.squares[rank][file] = piece

    def __str__(self):
        string = ""
        for file in reversed(self.squares):
            for piece in file:
                string += str(piece)
            string += "\n"
        return string
