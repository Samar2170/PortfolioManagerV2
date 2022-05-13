from lib2to3.pytree import Base
from securities.models.bullion import Bullion
from portfolio.models.bullion import BullionBuyTrade, BullionHolding, BullionSellTrade
from portfolio.controllers import BaseController
from portfolio.models.accounts import GeneralAccount

class BullionController(BaseController):
    Security_Model = Bullion
    Sell_Trade_Model = BullionSellTrade
    Buy_Trade_Model = BullionBuyTrade
    Holding_Model = BullionHolding


