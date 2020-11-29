import unittest
from operations.send_pack_operation import SendPackOperation
from transport.transport import Transport
from box.box_group_builder import BoxGroupBuilder
from machine.pack_machine import PackMachine
from pack.pack import Pack
from pack.pack_size import PackSize
from machine.machine_free_space_visitor import MachineFreeSpaceVisitor


class SendPackOperationTest(unittest.TestCase):
    def setUp(self):
        self.builder = BoxGroupBuilder()
        self.boxGroup = self.builder.withA(2).withB(4).withC(2).build()
        self.packMachine = PackMachine("PCK0")
        self.packMachine.add(self.boxGroup)
        self.pack = Pack("1", PackSize.A)
        self.transport = Transport("TR1", self.pack, "PCK1")

    @unittest.skip
    def testShouldPutPackIntoMachineUsingTransport(self):
        # given
        self.assertPackMachineEmpty()
        operation = SendPackOperation(self.transport, self.packMachine)

        # when
        operation.execute()

        # then
        self.assertEqual("PCK0", self.transport.place)
        self.assertPackMachineWithOneOccupiedBox()

    def assertPackMachineWithOneOccupiedBox(self):
        self.visitor = MachineFreeSpaceVisitor()
        self.packMachine.accept(self.visitor)
        self.assertEqual(1, self.visitor.quantities[PackSize.A])
        self.assertEqual(4, self.visitor.quantities[PackSize.B])
        self.assertEqual(2, self.visitor.quantities[PackSize.C])

    def assertPackMachineEmpty(self):
        self.visitor = MachineFreeSpaceVisitor()
        self.packMachine.accept(self.visitor)
        self.assertEqual(2, self.visitor.quantities[PackSize.A])
        self.assertEqual(4, self.visitor.quantities[PackSize.B])
        self.assertEqual(2, self.visitor.quantities[PackSize.C])
