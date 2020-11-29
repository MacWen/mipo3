import unittest
from box.box_group_builder import BoxGroupBuilder
from machine.pack_machine import PackMachine
from pack.pack import Pack
from pack.pack_size import PackSize


class PackMachineTest(unittest.TestCase):
    def setUp(self):
        self.builder = BoxGroupBuilder()
        self.boxGroup = self.builder.withA(2).withB(4).withC(2).build()
        self.packMachine = PackMachine("PCK0")
        self.packMachine.add(self.boxGroup)

    def testShouldAddPackToFirstBox(self):
        # given
        self.pack = Pack("1", PackSize.A)

        # when
        self.packMachine.put(self.pack)

        # then
        self.assertFalse(self.boxGroup.boxes[0].isEmpty())
