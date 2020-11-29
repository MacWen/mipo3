from pack.pack_size import PackSize


class MachineFreeSpaceVisitor:
    def __init__(self):
        self.quantities = {PackSize.A: 0, PackSize.B: 0, PackSize.C: 0}

    def visitBox(self, box):
        None

    def visitBoxGroup(self, boxGroup):
        None

    def visitPackMachine(self, packMachine):
        None
