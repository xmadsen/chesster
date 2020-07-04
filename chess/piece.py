class Piece():

    location = ()
    color = None

    def __init__(self, location):
        self.is_alive = True
        self.location = location
        pass

    def get_file(self):
        return self.location[0]

    def get_rank(self):
        return self.location[1]
