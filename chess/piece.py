from constants import PieceConstants as pc


class Piece():

    location = ()
    color = None
    point_value = 0
    is_selected = False

    def __init__(self, location, color):
        self.is_alive = True
        self.location = location
        self.color = color
        self.image = "{}_{}.png".format(
            self.color.lower(),
            type(self).__name__.lower())

    def get_file(self):
        return self.location[0]

    def get_rank(self):
        return self.location[1]

    def __str__(self):

        if self.color == 'white':
            fg_color = pc.WHITE_COLOR
        else:
            fg_color = pc.BLACK_COLOR
        if self.is_selected:
            inverse = "7;"
        else:
            inverse = ""

        return "\033[1;{}{}m{}\033[0m".format(
            inverse,
            fg_color,
            self.str_representation)


class Pawn(Piece):
    str_representation = "P"
    point_value = 1


class Bishop(Piece):
    str_representation = "B"
    point_value = 3


class Knight(Piece):
    str_representation = "N"
    point_value = 3


class Rook(Piece):
    str_representation = "R"
    point_value = 5


class Queen(Piece):
    str_representation = "Q"
    point_value = 9


class King(Piece):
    str_representation = "K"
    point_value = -1
