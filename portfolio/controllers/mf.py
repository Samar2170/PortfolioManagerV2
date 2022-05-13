from lib2to3.pytree import Base
from securities.models.mf import MutualFund
from portfolio.models.accounts import DematAccount
from portfolio.models.mf import MutualFundBuyTrade, MutualFundHolding, MutualFundSellTrade
from portfolio.controllers import BaseController

class MutualFundController(BaseController):
    Security_Model = MutualFund
    Sell_Trade_Model = MutualFundSellTrade
    Buy_Trade_Model = MutualFundBuyTrade
    Holding_Model = MutualFundHolding

    
