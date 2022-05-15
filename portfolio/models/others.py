from django.db import models
from portfolio.models.accounts import GeneralAccount

class Recievables(models.Model):
    account=models.ForeignKey(GeneralAccount, on_delete=models.CASCADE)
    total_amount=models.FloatField()
    issuer_name=models.CharField(max_length=50)
