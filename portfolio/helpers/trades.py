from securities.models.stocks import Stock
import uuid

class Trade:
    def __init__(self, symbol, quantity, price, trade_type, trade_date):
        self.stock = Stock.objects.get(symbol=symbol)
        self.quantity = quantity
        self.price = price
        self.trade_type = trade_type.upper()
        self.trade_date = trade_date
        self.trade_id = uuid.uuid4()
        