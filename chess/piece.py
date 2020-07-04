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


class Pawn(Piece):

    def __init__(self, location, color):
        super().__init__(location, color)
        self.point_value = 1


class Bishop(Piece):

    def __init__(self, location, color):
        super().__init__(location, color)
        self.point_value = 3


class Knight(Piece):

    def __init__(self, location, color):
        super().__init__(location, color)
        self.point_value = 3


class Rook(Piece):

    def __init__(self, location, color):
        super().__init__(location, color)
        self.point_value = 5


class Queen(Piece):

    def __init__(self, location, color):
        super().__init__(location, color)
        self.point_value = 9


class King(Piece):

    def __init__(self, location, color):
        super().__init__(location, color)
        self.point_value = -1
