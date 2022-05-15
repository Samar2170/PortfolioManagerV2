from django.db import models

class MutualFund(models.Model):
    name = models.CharField(max_length=100)
    symbol = models.CharField(max_length=50,null=True)
    sub_category = models.CharField(max_length=100,null=True)
    plan = models.CharField(max_length=100,null=True)
    expense_ratio = models.FloatField(null=True)
    aum = models.FloatField(null=True)