class Piece():

    location = ()
    color = None
    point_value = 0

    def __init__(self, location):
        self.is_alive = True
        self.location = location
        pass

    def get_file(self):
        return self.location[0]

    def get_rank(self):
        return self.location[1]


class Pawn(Piece):

    def __init__(self, location):
        super().__init__(location)
        self.point_value = 1


class Rook(Piece):

    def __init__(self, location):
        super().__init__(location)
        self.point_value = 5
