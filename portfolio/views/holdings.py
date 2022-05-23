from portfolio.models.accounts import BankAccount
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

class UnlistedBondHoldings(BaseHoldings):
    Holdings_Model = UnlistedBondHolding
    Serializer_Class = UnlistedBondHoldingSerializer

class FixedDepositHoldings(BaseHoldings):
    Holdings_Model = FixedDepositHolding
    Serializer_Class = FixedDepositHoldingSerializer


from portfolio.views import APIViewWithPermission
from django.db.models import Sum
from rest_framework.response import Response

class AggregateHoldings(APIViewWithPermission):

    def get(self, request, *args, **kwargs):
        user = request.user
        stocks = StockHolding.objects.filter(account__user=user).aggregate(Sum('total_amount'))['total_amount__sum']
        bullion = BullionHolding.objects.filter(account__user=user).aggregate(Sum('total_amount'))['total_amount__sum']
        mf = MutualFundHolding.objects.filter(account__user=user).aggregate(Sum('total_amount'))['total_amount__sum']
        fd = FixedDepositHolding.objects.filter(account__user=user).aggregate(Sum('total_amount'))['total_amount__sum']
        cash = BankAccount.objects.filter(user=user).aggregate(Sum('balance'))['balance__sum']
        listed_ncd = ListedNCDHolding.objects.filter(account__user=user).aggregate(Sum('total_amount'))['total_amount__sum']
        total = stocks + bullion  + fd + cash + listed_ncd + mf
        return Response({'stocks': stocks, 'bullion': bullion, 'mf': mf, 'fd': fd, 'cash': cash,
                         'listed_ncd': listed_ncd, "total": total})
    
