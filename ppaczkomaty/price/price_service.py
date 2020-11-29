from .price_strategy_factory import PriceStrategyFactory
from .size_price_strategy import SizePriceStrategy
from .c_size_price import CSizePrice


class PriceService:
    def __init__(self):
        self.strategyFactory = PriceStrategyFactory()

    def price(self):
        return 10

    def setPackSize(self, size):
        None
