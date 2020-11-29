from pack.pack_size import PackSize


class MachineFreeSpaceVisitor:
    def __init__(self):
        self.quantities = {PackSize.A: 0, PackSize.B: 0, PackSize.C: 0}

    def visitBox(self, box):
        if box.isEmpty(self):
            self.quantities[box.size] = self.quantities[box.size] + 1

    def visitBoxGroup(self, boxGroup):
        None

    def visitPackMachine(self, packMachine):
        None
