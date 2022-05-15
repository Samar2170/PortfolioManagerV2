from securities.constants import BANKS
from portfolio.models.accounts import BankAccount
from django.db import models

class FixedDepositHolding(models.Model):
    account=models.ForeignKey(BankAccount, on_delete=models.CASCADE)
    total_amount=models.FloatField()
    interest_rate=models.FloatField()
    ip_frequency = models.CharField(max_length=50, choices=(('Monthly', 'Monthly'), ('Quarterly', 'Quarterly'), ('Half-Yearly', 'Half-Yearly'), ('Yearly', 'Yearly'),('Maturity', 'Maturity')))
    start_date=models.DateField()
    maturity_date=models.DateField()
    maturity_amount=models.FloatField()
    is_interest_rate_floating=models.BooleanField(default=False)
    isin_code=models.CharField(max_length=50)
    
