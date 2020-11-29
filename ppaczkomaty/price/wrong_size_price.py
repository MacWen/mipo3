from .size_price_strategy import SizePriceStrategy


class WrongSizePrice(SizePriceStrategy):
    def price(self):
        return -1
