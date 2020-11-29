import unittest
from box.box_group import BoxGroup
from box.box import Box
from pack.pack_size import PackSize
from pack.pack import Pack


class BoxGroupTest(unittest.TestCase):

    def setUp(self):
        self.boxGroup = BoxGroup()
        self.boxGroup.boxes = [Box(PackSize.A), Box(PackSize.B)]

    def testShouldGetSmallestB(self):
        # when
        box = self.boxGroup.getSmallestEmptyBox(PackSize.B)

        # then
        self.assertEqual(2, len(self.boxGroup.boxes))
        self.assertEqual(box.size, PackSize.B)

    def testShouldGetBWhenAIsOccupied(self):
        # given
        pack = Pack("1", PackSize.A)
        self.boxGroup.boxes[0].put(pack)

        # when
        box = self.boxGroup.getSmallestEmptyBox(PackSize.A)

        # then
        self.assertEqual(2, len(self.boxGroup.boxes))
        self.assertEqual(box.size, PackSize.B)
