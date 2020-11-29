from .box import Box
from .box_group import BoxGroup
from pack.pack_size import PackSize


class BoxGroupBuilder:
    def __init__(self):
        self.aBoxes = 0
        self.bBoxes = 0
        self.cBoxes = 0

    def withA(self, a):
        self.aBoxes = a
        return self

    def withB(self, b):
        self.bBoxes = b
        return self

    def withC(self, c):
        self.cBoxes = c
        return self

    def build(self):
        boxGroup = BoxGroup()
        boxes = self.buildBoxArray(PackSize.A, self.aBoxes)
        boxes.extend(self.buildBoxArray(PackSize.B, self.bBoxes))
        boxes.extend(self.buildBoxArray(PackSize.C, self.cBoxes))
        boxGroup.boxes = boxes
        return boxGroup

    def buildBoxArray(self, packSize, numberOfBoxes):
        result = []
        for i in range(0, numberOfBoxes):
            result.append(Box(packSize))
        return result
