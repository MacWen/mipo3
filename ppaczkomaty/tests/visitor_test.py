import unittest
from machine.machine_free_space_visitor import MachineFreeSpaceVisitor
from machine.pack_machine import PackMachine
from box.box_group_builder import BoxGroupBuilder
from pack.pack import Pack
from pack.pack_size import PackSize


class VisitorTest(unittest.TestCase):
    def setUp(self):
        self.visitor = MachineFreeSpaceVisitor()
        self.packMachine = PackMachine("PCK0")
        self.builder = BoxGroupBuilder()
        boxGroup = self.builder.withA(2).withB(4).withC(2).build()
        self.packMachine.add(boxGroup)
        self.pack = Pack("1", PackSize.B)

    @unittest.skip
    def testShouldCountWithVisitor(self):
        # given
        self.packMachine.put(self.pack)

        # when
        self.packMachine.accept(self.visitor)

        # then
        self.assertEqual(2, self.visitor.quantities[PackSize.A])
        self.assertEqual(3, self.visitor.quantities[PackSize.B])
        self.assertEqual(2, self.visitor.quantities[PackSize.C])
