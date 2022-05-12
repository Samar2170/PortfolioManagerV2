from django.db import models 

class Bullion(models.Model):
    name = models.CharField(max_length=100, choices=[(
        'Gold', 'Gold'), ('Silver', 'Silver'), ('Platinum', 'Platinum'), ('Palladium', 'Palladium'), ('Other', 'Other')])
    default_unit = models.CharField(max_length=50, choices=[(
        'Kg', 'Kg'), ('Gram', 'Gram'), ('Pound', 'Pound'), ('Ounce', 'Ounce'), ('Other', 'Other')])

