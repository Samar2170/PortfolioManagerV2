from portfolio.request_models.entries import MutualFundTrade
from rest_framework.response import Response
from util.request_helpers import unwrap_query_dict
from portfolio.controllers.mf import MutualFundController
from portfolio.helpers.trades import Trade
from portfolio.views import APIViewWithPermission

class RegisterMutualFundTrade(APIViewWithPermission):
    def post(self,request):
        requested_data = unwrap_query_dict(request.data)
        data = MutualFundTrade(**requested_data)
        
        mfct = MutualFundController(data.symbol, data.account_no)
        trade = Trade(data.symbol, data.quantity, data.price, data.trade_type, data.trade_date)
        mfct.record_trade(trade)
        return Response({"message":"Mutual Fund Trade Registered"})

    