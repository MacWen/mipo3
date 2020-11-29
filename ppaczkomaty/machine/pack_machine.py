class PackMachine:
    def __init__(self, id):
        self.id = id
        self.groups = []

    def put(self, pack):
        for group in self.groups:
            box = group.getSmallestEmptyBox(pack.size)
            if box != None:
                box.put(pack)
                return

    def add(self, boxGroup):
        self.groups.append(boxGroup)

    def clear(self):
        self.groups = []

    def accept(self, visitor):
        visitor.visitPackMachine(self)
        for group in self.groups:
            group.accept(visitor)
