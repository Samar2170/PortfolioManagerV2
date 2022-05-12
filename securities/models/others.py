from django.db import models

class PrivateDebt(models.Model):
    counterparty = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    interest_rate = models.FloatField(null=True)
    amount = models.FloatField()
    transaction_date = models.DateField()


class Recievables(models.Model):
    counterparty = models.CharField(max_length=100)
    amount = models.FloatField()
    transaction_date = models.DateField()
    