from portfolio.controllers import BaseController
from portfolio.models.stocks import  StockBuyTrade, StockHolding, StockSellTrade
from securities.models.stocks import Stock

class StockController(BaseController):
    Security_Model = Stock
    Sell_Trade_Model = StockSellTrade
    Buy_Trade_Model = StockBuyTrade
    Holding_Model = StockHolding
