import unittest
from price.a_size_price import ASizePrice
from price.b_size_price import BSizePrice
from price.c_size_price import CSizePrice
from price.price_strategy_factory import PriceStrategyFactory
from pack.pack_size import PackSize
from price.price_service import PriceService


class PriceStrategyTest(unittest.TestCase):
    def setUp(self):
        self.factory = PriceStrategyFactory()
        self.priceService = PriceService()

    @unittest.skip
    def testAPrice(self):
        # given
        aPrice = ASizePrice()

        # then
        self.assertEqual(5, aPrice.price())

    @unittest.skip
    def testBPrice(self):
        # given
        bPrice = BSizePrice()

        # then
        self.assertEqual(10, bPrice.price())

    @unittest.skip
    def testCPrice(self):
        # given
        cPrice = CSizePrice()

        # then
        self.assertEqual(15, cPrice.price())

    @unittest.skip
    def testFactoryA(self):
        # when
        strategy = self.factory.getPriceStrategy(PackSize.A)

        # then
        self.assertTrue(isinstance(strategy, ASizePrice))

    @unittest.skip
    def testFactoryB(self):
        # when
        strategy = self.factory.getPriceStrategy(PackSize.B)

        # then
        self.assertTrue(isinstance(strategy, BSizePrice))

    @unittest.skip
    def testFactoryC(self):
        # when
        strategy = self.factory.getPriceStrategy(PackSize.C)

        # then
        self.assertTrue(isinstance(strategy, CSizePrice))

    def testPriceService(self):
        # when
        self.priceService.setPackSize(PackSize.B)

        # then
        self.assertEqual(10, self.priceService.price())
