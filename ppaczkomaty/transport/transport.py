class Transport:
    def __init__(self, id, pack, destination):
        self.id = id
        self.pack = pack
        self.destination = destination
        self.place = ""

    def setPlace(self, place):
        self.place = place
        