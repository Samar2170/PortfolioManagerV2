from portfolio.models.bullion import BullionHolding
from portfolio.models.mf import MutualFundHolding
from portfolio.models.stocks import StockHolding
from portfolio.serializers.holdings import StockHoldingSerializer, BullionHoldingSerializer, MutualFundHoldingSerializer
from portfolio.views.base.holdings import BaseHoldings

class StockHoldings(BaseHoldings):
    Holdings_Model = StockHolding
    Serializer_Class = StockHoldingSerializer

class MutualFundHoldings(BaseHoldings):
    Holdings_Model = MutualFundHolding
    Serializer_Class = MutualFundHoldingSerializer

class BullionHoldings(BaseHoldings):
    Holdings_Model = BullionHolding
    Serializer_Class = BullionHoldingSerializer