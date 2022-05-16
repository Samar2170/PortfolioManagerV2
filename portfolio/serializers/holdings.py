from rest_framework.serializers import ModelSerializer
from portfolio.models.bullion import BullionHolding
from portfolio.models.mf import MutualFundHolding
from portfolio.models.stocks import StockHolding
from portfolio.models.debt import ListedNCDHolding, UnlistedBondHolding
from portfolio.models.fd import FixedDepositHolding

class StockHoldingSerializer(ModelSerializer):
    class Meta:
        model = StockHolding
        fields = '__all__'
        depth = 1

class BullionHoldingSerializer(ModelSerializer):
    class Meta:
        model = BullionHolding
        fields = '__all__'
        depth = 1

class MutualFundHoldingSerializer(ModelSerializer):
    class Meta:
        model = MutualFundHolding
        fields = '__all__'
        depth = 1

class ListedNCDHoldingSerializer(ModelSerializer):
    class Meta:
        model = ListedNCDHolding
        fields = '__all__'
        depth = 1

class UnlistedBondHoldingSerializer(ModelSerializer):
    class Meta:
        model = UnlistedBondHolding
        fields = '__all__'
        depth = 1

class FixedDepositHoldingSerializer(ModelSerializer):
    class Meta:
        model = FixedDepositHolding
        fields = '__all__'
        depth = 1