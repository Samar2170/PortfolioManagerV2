from portfolio.models import DematAccount
from portfolio.controllers.stocks import StockController
from portfolio.models.stocks import StockHolding, StockSellTrade
from securities.models.stocks import Stock
from django.contrib.auth.models import User
import time
from portfolio.controllers.stocks import StockController
from portfolio.helpers.trades import Trade


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
    ioc = Stock.objects.get(symbol="TITAN")
    
    # Create a new stock buy trade.
    sct = StockController(ioc.symbol, account.account_code)
    trade = Trade(ioc.symbol, 100, 200, 'BUY', time.strftime("%Y-%m-%d"))
    trade2 = Trade(ioc.symbol, 100, 400, 'BUY', time.strftime("%Y-%m-%d"))
    sct.record_trade(trade)
    sct.record_trade(trade2)

    ## check buy price and quantity.
    sh = StockHolding.objects.get( account=account, security=ioc)
    print(sh.quantity == 200)
    print(sh.buy_price == 300)

    # Create a new stock sell trade.
    trade3 = Trade(ioc.symbol, 50, 280, 'SELL', time.strftime("%Y-%m-%d"))
    sct.record_trade(trade3)

    ## check sell price and quantity.
    sellt = StockSellTrade.objects.get(account=account, security=ioc, trade_id=trade3.trade_id)
    print(sellt.profit)
