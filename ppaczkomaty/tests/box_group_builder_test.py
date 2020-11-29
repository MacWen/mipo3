import unittest
from box.box_group_builder import BoxGroupBuilder
from pack.pack_size import PackSize


class BoxGroupBuilderTest(unittest.TestCase):
    def setUp(self):
        self.builder = BoxGroupBuilder()

    def testBuilder(self):
        # when
        boxGroup = self.builder.withA(2).withB(4).withC(2).build()

        # then
        self.assertEqual(8, len(boxGroup.boxes))
        self.assertEqual(PackSize.A, boxGroup.boxes[0].size)
        self.assertEqual(PackSize.B, boxGroup.boxes[2].size)
        self.assertEqual(PackSize.C, boxGroup.boxes[6].size)
