from .pack_operation import PackOperation


class SendPackOperation(PackOperation):

    def __init__(self, transport, packMachine):
        self.transport = transport
        self.packMachine = packMachine

    def execute(self):
        None
