from portfolio.models.bullion import BullionHolding
from portfolio.models.mf import MutualFundHolding
from portfolio.models.stocks import StockHolding
from portfolio.models.debt import ListedNCDHolding, UnlistedBondHolding
from portfolio.models.fd import FixedDepositHolding
from portfolio.serializers.holdings import StockHoldingSerializer, BullionHoldingSerializer, MutualFundHoldingSerializer, \
    ListedNCDHoldingSerializer, UnlistedBondHoldingSerializer, FixedDepositHoldingSerializer
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

class ListedNCDHoldings(BaseHoldings):
    Holdings_Model = ListedNCDHolding
    Serializer_Class = ListedNCDHoldingSerializer

class UnlistedNCDHoldings(BaseHoldings):
    Holdings_Model = UnlistedBondHolding
    Serializer_Class = UnlistedBondHoldingSerializer

class FixedDepositHoldings(BaseHoldings):
    Holdings_Model = FixedDepositHolding
    Serializer_Class = FixedDepositHoldingSerializer

