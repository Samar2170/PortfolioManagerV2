from django.urls import path, include
from rest_framework import routers

from portfolio.views.entries import stocks as stocks
from portfolio.views.entries import mf as mf
from portfolio.views.entries import bullion as bullion
from portfolio.views.entries import bonds as bonds
from portfolio.views.entries import debt as debt
from portfolio.views.accounts import BankAccountViewSet, DematAccountViewSet, GeneralAccountViewSet
from portfolio.views.holdings import StockHoldings, MutualFundHoldings, BullionHoldings


router = routers.DefaultRouter()
router.register(r'bank-accounts', BankAccountViewSet, basename='bank-accounts')
router.register(r'demat-accounts', DematAccountViewSet, basename='demat-accounts')
router.register(r'general-accounts', GeneralAccountViewSet, basename='general-accounts')


urlpatterns = [
    path('register-stock-trade/',stocks.RegisterStockTrade.as_view(),name='register_stock_trade'),
    path('register-mf-trade/',mf.RegisterMutualFundTrade.as_view(),name='register_mf_trade'),
    path('register-bullion-trade/',bullion.RegisterBullionTrade.as_view(),name='register_bullion_trade'),
    path('register-bond-trade/',bonds.RegisterBondTrade.as_view(),name='register_bond_trade'),
    path('register-fd-trade/',debt.RegisterFDTrade.as_view(),name='register_fd_trade'),
    path('register-unlisted-bond-trade/',debt.RegisterUnlistedBondTrade.as_view(),name='register_unlisted_bond_trade'),
    
    path('stock-holdings/',StockHoldings.as_view(),name='stock_holdings'),
    path('mf-holdings/',MutualFundHoldings.as_view(),name='mf_holdings'),
    path('bullion-holdings/',BullionHoldings.as_view(),name='bullion_holdings'),

    path('', include(router.urls)),
]