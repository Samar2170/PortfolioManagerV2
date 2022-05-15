from portfolio.request_models.entries import StockTrade
from rest_framework.response import Response
from util.request_helpers import unwrap_query_dict
from portfolio.controllers.stocks import StockController
from portfolio.helpers.trades import Trade
from portfolio.views import APIViewWithPermission

class RegisterStockTrade(APIViewWithPermission):
    def post(self,request):
        # import ipdb; ipdb.set_trace()
        requested_data = unwrap_query_dict(request.data)
        data = StockTrade(**requested_data)
        
        sct = StockController(data.symbol, data.account_no)
        trade = Trade(data.symbol, data.quantity, data.price, data.trade_type, data.trade_date)
        sct.record_trade(trade)
        return Response({"message":"Stock Trade Registered"})


