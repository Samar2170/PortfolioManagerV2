from django.db import models

class DebtSecurity(models.Model):
    name = models.CharField(max_length=100)
    face_value = models.FloatField()
    maturity_date = models.DateField()
    maturity_amount = models.FloatField()
    interest_rate = models.FloatField(null=True)
    ip_frequency = models.CharField(max_length=50, choices=(('Monthly', 'Monthly'), ('Quarterly', 'Quarterly'), ('Half-Yearly', 'Half-Yearly'), ('Yearly', 'Yearly'),('Maturity', 'Maturity')))
    ip_amount = models.FloatField(default=0)
    ip_date = models.DateField(null=True)
    is_interest_rate_floating = models.BooleanField(default=False)

class ListedNCD(DebtSecurity):
    symbol1 = models.CharField(max_length=50)
    isin_code = models.CharField(max_length=50)
    dirty_price = models.FloatField()
    clean_price = models.FloatField(null=True)
    secured = models.BooleanField(null=True)
    issuer = models.CharField(max_length=100, null=True)

# class FD(DebtSecurity):
#     issuer = models.CharField(max_length=100, choices=BANKS)

class SavingsBond(DebtSecurity):
    issuer = models.CharField(max_length=100, default='GOI')

class OtherUnlistedBonds(DebtSecurity):
    issuer = models.CharField(max_length=100)

