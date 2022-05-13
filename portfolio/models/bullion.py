from django.db import models
from portfolio.models.accounts import GeneralAccount
from securities.models.bullion import Bullion

class BullionBuyTrade(models.Model):
    account = models.ForeignKey(GeneralAccount, on_delete=models.CASCADE)
    security = models.ForeignKey(Bullion, on_delete=models.CASCADE)
    quantity = models.FloatField()
    price = models.FloatField()
    total_amount = models.FloatField()
    trade_date = models.DateField()
    trade_id = models.UUIDField()

class BullionHolding(models.Model):
    account = models.ForeignKey(GeneralAccount, on_delete=models.CASCADE)
    security = models.ForeignKey(Bullion, on_delete=models.CASCADE)
    quantity = models.FloatField()
    buy_price = models.FloatField()
    total_amount = models.FloatField()

class BullionSellTrade(models.Model):
    account = models.ForeignKey(GeneralAccount, on_delete=models.CASCADE)
    security = models.ForeignKey(Bullion, on_delete=models.CASCADE)
    quantity = models.FloatField()
    buy_price = models.FloatField()
    sell_price = models.FloatField()
    total_amount = models.FloatField()
    trade_date = models.DateField()
    profit = models.FloatField(null=True)
    trade_id = models.UUIDField()
    