from securities.models.stocks import Stock
import uuid

class Trade:
    def __init__(self, symbol, quantity, price, trade_type, trade_date):
        self.stock = symbol
        self.quantity = quantity
        self.price = price
        self.trade_type = trade_type.upper()
        self.trade_date = trade_date
        self.trade_id = uuid.uuid4()

class BondTrade:
    def __init__(self, name, quantity, price, trade_type, trade_date):
        self.trade_id = uuid.uuid4()
        self.trade_date = trade_date
        self.name = name.upper()
        self.trade_type = trade_type.upper()
        self.quantity = quantity
        self.price = price
