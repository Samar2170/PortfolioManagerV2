from securities.models.debt import ListedNCD, SavingsBond, OtherUnlistedBonds
from portfolio.models.accounts import GeneralAccount, DematAccount
from django.db import models


class SavingsBondHolding(models.Model):
    account=models.ForeignKey(GeneralAccount, on_delete=models.CASCADE)
    security=models.ForeignKey(SavingsBond, on_delete=models.CASCADE)
    quantity=models.IntegerField()
    price=models.FloatField()
    bond_yield=models.FloatField(null=True)
    buy_price=models.FloatField(null=True)
    clean_price=models.FloatField(null=True)
    accrued_interest=models.FloatField(null=True)
    total_amount=models.FloatField(null=True)
    buy_date=models.DateField(null=True)
    created_at=models.DateTimeField(auto_now_add=True)



class ListedNCDHolding(models.Model):
    account=models.ForeignKey(DematAccount, on_delete=models.CASCADE)
    security=models.ForeignKey(ListedNCD, on_delete=models.CASCADE)
    quantity=models.IntegerField()
    price=models.FloatField()
    bond_yield=models.FloatField(null=True)
    buy_price=models.FloatField(null=True)
    clean_price=models.FloatField(null=True)
    accrued_interest=models.FloatField(null=True)
    total_amount=models.FloatField(null=True)
    buy_date=models.DateField(null=True)
    created_at=models.DateTimeField(auto_now_add=True)

class UnlistedBondHolding(models.Model):
    account=models.ForeignKey(DematAccount, on_delete=models.CASCADE)
    security=models.ForeignKey(OtherUnlistedBonds, on_delete=models.CASCADE)
    quantity=models.IntegerField()
    price=models.FloatField()
    bond_yield=models.FloatField(null=True)
    buy_price=models.FloatField(null=True)
    clean_price=models.FloatField(null=True)
    accrued_interest=models.FloatField(null=True)
    total_amount=models.FloatField(null=True)
    buy_date=models.DateField(null=True)
    created_at=models.DateTimeField(auto_now_add=True)

class ListedNCDBuyTrade(models.Model):
    account=models.ForeignKey(GeneralAccount, on_delete=models.CASCADE)
    security=models.ForeignKey(SavingsBond, on_delete=models.CASCADE)
    quantity=models.IntegerField()
    price=models.FloatField()
    total_amount=models.FloatField(null=True)
    buy_date=models.DateField(null=True)
    created_at=models.DateTimeField(auto_now_add=True)

class ListedNCDSellTrade(models.Model):
    account=models.ForeignKey(GeneralAccount, on_delete=models.CASCADE)
    security=models.ForeignKey(SavingsBond, on_delete=models.CASCADE)
    quantity=models.IntegerField()
    buy_price=models.FloatField()
    sell_price=models.FloatField()
    total_amount=models.FloatField(null=True)
    profit=models.FloatField(null=True)
    buy_date=models.DateField(null=True)
    created_at=models.DateTimeField(auto_now_add=True)
