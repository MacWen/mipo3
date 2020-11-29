class Box:
    def __init__(self, size):
        self.size = size
        self.pack = None

    def isEmpty(self):
        return self.pack is None

    def retrieve(self):
        old = self.pack
        self.pack = None
        return old

    def put(self, pack):
        self.pack = pack

    def accept(self, visitor):
        visitor.visitBox(self)
