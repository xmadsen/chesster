from piece import (
    Piece, Pawn, Bishop, Knight,
    Rook, Queen, King)


class Board():

    string = ''

    def __init__(self):
        self.initialize_pieces()

    def initialize_pieces(self):
        self.squares = [[" "] * 8 for _ in range(8)]
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
        self.string = ''
        for i, file in enumerate(reversed(self.squares)):
            if i == 0:
                self.draw_grid_top()
            if i != 0:
                self.draw_grid_middle()
            self.draw_rank(i)
            for piece in file:
                self.draw_piece(piece)
            self.string += '\n'

        self.draw_grid_bottom()
        self.draw_files()
        return self.string

    def draw_grid_top(self):
        self.string += '  ┌─' + '──┬─' * 7 + '──┐\n'

    def draw_grid_middle(self):
        self.string += '  ├─' + '──┼─' * 7 + '──┤\n'

    def draw_grid_bottom(self):
        self.string += '  └─' + '──┴─' * 7 + '──┘\n'

    def draw_files(self):
        files = 'abcdefgh'
        self.string += '    {}'.format('   '.join(files))

    def draw_rank(self, i):
        rank = str(8-i)
        self.string += '{} │'.format(rank)

    def draw_piece(self, piece):
        self.string += ' {} │'.format(piece)
