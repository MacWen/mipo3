import unittest

#from id.runtime_id_generator import RuntimeIdGenerator


class RuntimeIdGeneratorTest(unittest.TestCase):
    def setUp(self):
        self.idGenerator = None

    @unittest.skip
    def testPackId(self):
        # then
        self.assertEqual('0', self.idGenerator.getPackId())
        self.assertEqual('1', self.idGenerator.getPackId())

    @unittest.skip
    def testPackMachineId(self):
        # then
        self.assertEqual('PCK0', self.idGenerator.getPackMachineId())
        self.assertEqual('PCK1', self.idGenerator.getPackMachineId())

    @unittest.skip
    def testTransportId(self):
        # then
        self.assertIsNotNone(self.idGenerator.getTransportId())
