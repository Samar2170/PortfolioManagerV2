from urllib.parse import urlparse
from django.urls import path
from portfolio.views.entries import stocks as stocks

urlpatterns = [
    path('register_stock_trade/',stocks.RegisterStockTrade.as_view(),name='register_stock_trade'),
]