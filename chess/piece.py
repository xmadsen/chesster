class Piece():

    location = ()

    def __init__(self, file, rank):
        self.is_alive = True
        self.location = (file, rank)
        pass
