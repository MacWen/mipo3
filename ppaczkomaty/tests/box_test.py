import unittest

from box.box import Box
from pack.pack_size import PackSize
from pack.pack import Pack


class BoxTest(unittest.TestCase):
    def setUp(self):
        self.box = Box(PackSize.A)

    def testEmptyByDefault(self):
        # then
        self.assertTrue(self.box.isEmpty())

    def testOccupied(self):
        # given
        pack = Pack("1", PackSize.A)
        self.box.put(pack)

        # then
        self.assertFalse(self.box.isEmpty())
