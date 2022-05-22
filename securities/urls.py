from django.urls import path
from securities.views.data import ( SearchMutualFunds, SearchStocks, StockView, MutualFundView, ListNCDView, StockList, MutualFundList, ListNCDList, BullionList )

urlpatterns = [
    path('mutual-funds/search/', SearchMutualFunds.as_view(), name='search-mutual-funds'),
    path('mutual-funds/', MutualFundView.as_view(), name='mutual-fund'),
    path('stocks/search/', SearchStocks.as_view(), name='search-stocks'),
    path('stocks/', StockView.as_view(), name='stock'),
    path('listed-ncd/', ListNCDView.as_view(), name='listed-ncd'),
    path('stocks/list/', StockList.as_view(), name='stock-list'),
    path('mutual-funds/list/', MutualFundList.as_view(), name='mutual-fund-list'),
    path('listed-ncd/list/', ListNCDList.as_view(), name='listed-ncd-list'),
    path('bullion/list/', BullionList.as_view(), name='bullion-list'),
]