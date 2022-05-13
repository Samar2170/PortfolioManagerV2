from portfolio.request_models.entries import BullionTrade
from rest_framework.response import Response
from util.request_helpers import unwrap_query_dict  
from portfolio.controllers.bullion import BullionController
from portfolio.helpers.trades import Trade
from portfolio.views import APIViewWithPermission


class RegisterBullionTrade(APIViewWithPermission):
    def post(self,request):
        requested_data = unwrap_query_dict(request.data)
        data = BullionTrade(**requested_data)
        
        bct = BullionController(data.symbol, data.account_no)
        trade = Trade(data.symbol, data.quantity, data.price, data.trade_type, data.trade_date)
        bct.record_trade(trade)
        return Response({"message":"Bullion Trade Registered"})

