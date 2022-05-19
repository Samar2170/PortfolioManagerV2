from django.db import models 

class Bullion(models.Model):
    symbol = models.CharField(max_length=100,null=True)
    default_unit = models.CharField(max_length=50)

