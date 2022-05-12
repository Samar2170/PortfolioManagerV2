from portfolio.models import DematAccount
from portfolio.controllers.stocks import StockController
from securities.models.stocks import Stock
from django.contrib.auth.models import User
import time
from portfolio.controllers.stocks import StockController

class Trade:
    def __init__(self, symbol, quantity, price, trade_type, trade_date):
        self.stock = Stock.objects.get(symbol=symbol)
        self.quantity = quantity
        self.price = price
        self.trade_type = trade_type.upper()
        self.trade_date = trade_date

def test_stock_flow():
    """
    Test the stock flow.
    """
    # Create a new account.
    account = DematAccount.objects.get(
        user=User.objects.get(username="test_user"),
        account_no="123456789",
    )
    
    # fetch new stock.
    tcs = Stock.objects.filter(symbol="TCS")
    # Create a new stock buy trade.
    sct = StockController(tcs[0].symbol, account.account_code)
    trade = Trade(tcs[0].symbol, 100, 100, 'BUY', time.strftime("%Y-%m-%d"))
    sct.record_trade(trade)
    time.sleep(1)
    # Create a new stock sell trade.
    sct = StockController(tcs[0].symbol, account.account_code)
    trade = Trade(tcs[0].symbol, 50, 80, 'SELL', time.strftime("%Y-%m-%d"))
    sct.record_trade(trade)
    time.sleep(1)

    