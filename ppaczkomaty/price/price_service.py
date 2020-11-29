from .price_strategy_factory import PriceStrategyFactory
from .size_price_strategy import SizePriceStrategy
from .wrong_size_price import WrongSizePrice


class PriceService:
    def __init__(self):
        self.strategyFactory = PriceStrategyFactory()
        self.priceStrategy = WrongSizePrice()

    def price(self):
        return self.priceStrategy.price()

    def setPackSize(self, size):
        self.priceStrategy = self.strategyFactory.getPriceStrategy(self, size)
