from pack.pack_size import PackSize


class BoxGroup:
    def __init__(self):
        self.sizeMapping = {PackSize.A: [PackSize.A, PackSize.B, PackSize.C], PackSize.B: [
            PackSize.B, PackSize.C], PackSize.C: [PackSize.C]}
        self.boxes = []

    def getSmallestEmptyBox(self, size):
        available = self.sizeMapping[size]
        for size in available:
            for box in self.boxes:
                if box.size == size and box.isEmpty():
                    return box
        return None

    def accept(self, visitor):
        visitor.visitBoxGroup(self)
        for box in self.boxes:
            box.accept(visitor)
