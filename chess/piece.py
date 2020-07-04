class Piece():

    location = ()
    color = None
    point_value = 0

    def __init__(self, location, color):
        self.is_alive = True
        self.location = location
        self.color = color
        pass

    def get_file(self):
        return self.location[0]

    def get_rank(self):
        return self.location[1]

    def __str__(self):
        return self.str_representation


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
