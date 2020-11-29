from pack.pack_size import PackSize
from .a_size_price import ASizePrice
from .b_size_price import BSizePrice
from .c_size_price import CSizePrice


class PriceStrategyFactory:
    def getPriceStrategy(self, size):
        return None
