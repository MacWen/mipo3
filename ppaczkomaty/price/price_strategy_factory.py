from pack.pack_size import PackSize
from .a_size_price import ASizePrice
from .b_size_price import BSizePrice
from .c_size_price import CSizePrice
from .wrong_size_price import WrongSizePrice


class PriceStrategyFactory:
    def getPriceStrategy(self, size):
        if size == PackSize.A:
            return ASizePrice()
        elif size == PackSize.B:
            return BSizePrice()
        elif size == PackSize.C:
            return CSizePrice()
        else:
            return WrongSizePrice()
