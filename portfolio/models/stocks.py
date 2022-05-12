from django.db import models
from portfolio.models.accounts import DematAccount
from securities.models.stocks import Stock

class StockBuyTrade(models.Model):
    account = models.ForeignKey(DematAccount, on_delete=models.CASCADE)
    security = models.ForeignKey(Stock, on_delete=models.CASCADE)
    quantity = models.FloatField()
    price = models.FloatField()
    total_amount = models.FloatField()
    trade_date = models.DateField()

class StockHolding(models.Model):
    account = models.ForeignKey(DematAccount, on_delete=models.CASCADE)
    security = models.ForeignKey(Stock, on_delete=models.CASCADE)
    quantity = models.FloatField()
    buy_price = models.FloatField()
    total_amount = models.FloatField()

class StockSellTrade(models.Model):
    account = models.ForeignKey(DematAccount, on_delete=models.CASCADE)
    security = models.ForeignKey(Stock, on_delete=models.CASCADE)
    quantity = models.FloatField()
    buy_price = models.FloatField()
    sell_price = models.FloatField()
    total_amount = models.FloatField()
    trade_date = models.DateField()
    profit = models.FloatField(null=True)