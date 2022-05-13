from django.db.models.signals import post_save
from django.dispatch import receiver

from portfolio.models.accounts import GeneralAccount
from .models import Account
from django.contrib.auth.models import User
from datetime import datetime
from random import randint

@receiver(post_save, sender=User)
def create_user_general_account(sender, instance, created, **kwargs):
    if created:
        account_code = str(randint(1, 99999))
        account_code = account_code + str(datetime.now().strftime('%Y%m%d%H%M%S'))
        GeneralAccount.objects.create(user=instance, account_code=account_code, account_no=account_code)
        print("BaseAccount created successfully")


