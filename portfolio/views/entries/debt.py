from portfolio.models.accounts import BankAccount, GeneralAccount
from portfolio.views import APIViewWithPermission
from portfolio.request_models.entries import UnlistedBondTrade, FDTrade
from portfolio.models.debt import UnlistedBondHolding
from portfolio.models.fd import FixedDepositHolding
from rest_framework.response import Response
from util.request_helpers import unwrap_query_dict

class RegisterFDTrade(APIViewWithPermission):
    def post(self,request):
        requested_data = unwrap_query_dict(request.data)
        data = FDTrade(**requested_data)
        account = BankAccount.objects.get(account_no=data.account_no)
        FixedDepositHolding.objects.create(account=account,
                                           total_amount=data.total_amount,
                                           interest_rate=data.interest_rate,
                                           ip_frequency=data.ip_frequency,
                                           start_date=data.start_date,
                                           maturity_date=data.maturity_date,
                                           maturity_amount=data.maturity_amount,
                                           )
        return Response('Success')

class RegisterUnlistedBondTrade(APIViewWithPermission):
    def post(self,request):
        requested_data = unwrap_query_dict(request.data)
        data = UnlistedBondTrade(**requested_data)
        account = GeneralAccount.objects.get(account_no=data.account_no)
        UnlistedBondHolding.objects.create(account=account,
                                            name=data.name,
                                            quantity=data.quantity,
                                            price=data.price,
                                            buy_price=data.buy_price,
                                            buy_date=data.buy_date,
                                            bond_yield=data.bond_yield,
                                            interest_rate=data.interest_rate,
                                            ip_frequency=data.ip_frequency,                                            
                                           maturity_date=data.maturity_date,
                                           maturity_amount=data.maturity_amount,
                                           )
        return Response('Success')