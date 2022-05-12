from django.db import models

class Stock(models.Model):
    company_name = models.CharField(max_length=100)
    symbol = models.CharField(max_length=50)
    industry = models.CharField(max_length=100)
    isin_code = models.CharField(max_length=50)
