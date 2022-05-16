from portfolio.controllers.bonds import ListedNCDController
from portfolio.helpers.trades import BondTrade
from portfolio.request_models.entries import ListedNCDTrade
from portfolio.views import APIViewWithPermission
from util.request_helpers import unwrap_query_dict
from rest_framework.response import Response


class RegisterBondTrade(APIViewWithPermission):
    def post(self, request):
        requested_data = unwrap_query_dict(request.data)
        bond_trade = ListedNCDTrade(**requested_data)
        btc = ListedNCDController(bond_trade.name, bond_trade.account_no)
        trade = BondTrade(
            bond_trade.name,bond_trade.quantity, bond_trade.price,
            bond_trade.trade_type, bond_trade.trade_date
        )
        btc.record_trade(trade)
        return Response({"message": "Bond Trade Registered"})
