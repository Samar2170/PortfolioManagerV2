from rest_framework.serializers import ModelSerializer
from portfolio.models.bullion import BullionHolding
from portfolio.models.mf import MutualFundHolding
from portfolio.models.stocks import StockHolding

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