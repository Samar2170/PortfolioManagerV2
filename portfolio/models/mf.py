from django.db import models
from portfolio.models.accounts import DematAccount
from securities.models.mf import MutualFund

class MutualFundBuyTrade(models.Model):
    account = models.ForeignKey(DematAccount, on_delete=models.CASCADE)
    security = models.ForeignKey(MutualFund, on_delete=models.CASCADE)
    quantity = models.FloatField()
    price = models.FloatField()
    total_amount = models.FloatField()
    trade_date = models.DateField()
    trade_id = models.UUIDField()

class MutualFundHolding(models.Model):
    account = models.ForeignKey(DematAccount, on_delete=models.CASCADE)
    security = models.ForeignKey(MutualFund, on_delete=models.CASCADE)
    quantity = models.FloatField()
    buy_price = models.FloatField()
    total_amount = models.FloatField()

class MutualFundSellTrade(models.Model):
    account = models.ForeignKey(DematAccount, on_delete=models.CASCADE)
    security = models.ForeignKey(MutualFund, on_delete=models.CASCADE)
    quantity = models.FloatField()
    buy_price = models.FloatField()
    sell_price = models.FloatField()
    total_amount = models.FloatField()
    trade_date = models.DateField()
    profit = models.FloatField(null=True)
    trade_id = models.UUIDField()